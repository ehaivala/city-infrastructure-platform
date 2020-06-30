import uuid

from auditlog.registry import auditlog
from django.conf import settings
from django.contrib.gis.db import models
from django.contrib.gis.geos import Point
from django.core.exceptions import ValidationError
from django.db.models import Q
from django.utils.translation import gettext_lazy as _
from enumfields import EnumField, EnumIntegerField

from ..mixins.models import SoftDeleteModel, UserControlModel
from .common import (
    Color,
    Condition,
    DeviceTypeTargetModel,
    LaneNumber,
    LaneType,
    Lifecycle,
    Reflection,
    Surface,
    TrafficControlDeviceType,
)
from .plan import Plan
from .traffic_sign import (
    InstallationStatus,
    LocationSpecifier,
    TrafficSignPlan,
    TrafficSignReal,
)
from .utils import SoftDeleteQuerySet


class AbstractAdditionalSign(SoftDeleteModel, UserControlModel):
    id = models.UUIDField(
        primary_key=True, unique=True, editable=False, default=uuid.uuid4
    )
    location = models.PointField(
        _("Location (2D)"), srid=settings.SRID, blank=True, null=True
    )
    affect_area = models.PolygonField(
        _("Affect area (2D)"), srid=settings.SRID, blank=True, null=True
    )

    reflection_class = EnumField(
        Reflection,
        verbose_name=_("Reflection"),
        max_length=2,
        default=Reflection.R1,
        blank=True,
        null=True,
    )
    surface_class = EnumField(
        Surface,
        verbose_name=_("Surface"),
        max_length=6,
        default=Surface.FLAT,
        blank=True,
        null=True,
    )
    color = EnumIntegerField(
        Color, verbose_name=_("Color"), default=Color.BLUE, blank=True, null=True
    )

    road_name = models.CharField(_("Road name"), max_length=254, blank=True, null=True)
    lane_number = EnumField(
        LaneNumber, verbose_name=_("Lane number"), default=LaneNumber.MAIN_1, blank=True
    )
    lane_type = EnumField(
        LaneType, verbose_name=_("Lane type"), default=LaneType.MAIN, blank=True,
    )
    location_specifier = EnumIntegerField(
        LocationSpecifier,
        verbose_name=_("Location specifier"),
        default=LocationSpecifier.RIGHT,
        blank=True,
        null=True,
    )

    decision_id = models.CharField(
        _("Decision id"), max_length=254, blank=True, null=True
    )
    decision_date = models.DateField(_("Decision date"))
    installation_id = models.CharField(
        _("Installation id"), max_length=254, blank=True, null=True
    )
    installation_date = models.DateField(_("Installation date"), blank=True, null=True)
    installation_status = EnumField(
        InstallationStatus,
        verbose_name=_("Installation status"),
        max_length=10,
        default=InstallationStatus.IN_USE,
        blank=True,
        null=True,
    )
    installed_by = models.CharField(_("Installed by"), max_length=256, blank=True)
    owner = models.CharField(_("Owner"), max_length=256)

    validity_period_start = models.DateField(
        _("Validity period start"), blank=True, null=True
    )
    validity_period_end = models.DateField(
        _("Validity period end"), blank=True, null=True
    )
    seasonal_validity_period_start = models.DateField(
        _("Seasonal validity period start"), blank=True, null=True
    )
    seasonal_validity_period_end = models.DateField(
        _("Seasonal validity period end"), blank=True, null=True
    )
    lifecycle = EnumIntegerField(
        Lifecycle, verbose_name=_("Lifecycle"), default=Lifecycle.ACTIVE
    )

    objects = SoftDeleteQuerySet.as_manager()

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if not self.location and self.parent:
            self.location = Point(
                self.parent.location.x,
                self.parent.location.y,
                srid=self.parent.location.srid,
            )

        super().save(*args, **kwargs)


class AdditionalSignPlan(AbstractAdditionalSign):
    parent = models.ForeignKey(
        TrafficSignPlan,
        verbose_name=_("Parent Traffic Sign Plan"),
        on_delete=models.PROTECT,
        related_name="additional_signs",
        blank=True,
        null=True,
    )
    plan = models.ForeignKey(
        Plan,
        verbose_name=_("Plan"),
        on_delete=models.PROTECT,
        related_name="additional_sign_plans",
        blank=True,
        null=True,
    )

    class Meta:
        db_table = "additional_sign_plan"
        verbose_name = _("Additional Sign Plan")
        verbose_name_plural = _("Additional Sign Plans")

    def __str__(self):
        return f"AdditionalSignPlan {self.id}"


class AdditionalSignReal(AbstractAdditionalSign):
    parent = models.ForeignKey(
        TrafficSignReal,
        verbose_name=_("Parent Traffic Sign Real"),
        on_delete=models.PROTECT,
        related_name="additional_signs",
        blank=True,
        null=True,
    )
    additional_sign_plan = models.ForeignKey(
        AdditionalSignPlan,
        verbose_name=_("Additional Sign Plan"),
        on_delete=models.PROTECT,
        blank=True,
        null=True,
    )
    condition = EnumIntegerField(
        Condition,
        verbose_name=_("Condition"),
        default=Condition.VERY_GOOD,
        blank=True,
        null=True,
    )
    manufacturer = models.CharField(
        _("Manufacturer"), max_length=254, blank=True, null=True
    )
    rfid = models.CharField(_("RFID"), max_length=254, blank=True, null=True)

    class Meta:
        db_table = "additional_sign_real"
        verbose_name = _("Additional Sign Real")
        verbose_name_plural = _("Additional Sign Reals")

    def __str__(self):
        return f"AdditionalSignReal {self.id}"


class AbstractAdditionalSignContent(UserControlModel):
    id = models.UUIDField(
        primary_key=True, unique=True, editable=False, default=uuid.uuid4
    )

    device_type = models.ForeignKey(
        TrafficControlDeviceType,
        verbose_name=_("Device type"),
        on_delete=models.PROTECT,
        limit_choices_to=Q(
            Q(target_model=None) | Q(target_model=DeviceTypeTargetModel.TRAFFIC_SIGN)
        ),
    )
    text = models.CharField(verbose_name=_("Content text"), max_length=256, blank=True)
    order = models.SmallIntegerField(
        verbose_name=_("Order"), default=1, blank=False, null=False
    )

    class Meta:
        ordering = ("order",)
        abstract = True

    def save(self, *args, **kwargs):
        if not self.device_type.validate_relation(DeviceTypeTargetModel.TRAFFIC_SIGN):
            raise ValidationError(
                f'Device type "{self.device_type}" is not allowed for traffic signs'
            )

        super().save(*args, **kwargs)


class AdditionalSignContentPlan(AbstractAdditionalSignContent):
    parent = models.ForeignKey(
        AdditionalSignPlan,
        verbose_name=_("Parent Additional Sign Plan"),
        on_delete=models.CASCADE,
        related_name="content",
        blank=False,
        null=False,
    )

    class Meta:
        verbose_name = _("Additional Sign Content Plan")
        verbose_name_plural = _("Additional Sign Content Plans")

    def __str__(self):
        return f"AdditionalSignContentPlan at position {self.order} for {self.parent}"


class AdditionalSignContentReal(AbstractAdditionalSignContent):
    parent = models.ForeignKey(
        AdditionalSignReal,
        verbose_name=_("Parent Additional Sign Real"),
        on_delete=models.CASCADE,
        related_name="content",
        blank=False,
        null=False,
    )

    class Meta:
        verbose_name = _("Additional Sign Content Real")
        verbose_name_plural = _("Additional Sign Content Reals")

    def __str__(self):
        return f"AdditionalSignContentReal at position {self.order} for {self.parent}"


auditlog.register(AdditionalSignPlan)
auditlog.register(AdditionalSignReal)
auditlog.register(AdditionalSignContentPlan)
auditlog.register(AdditionalSignContentReal)