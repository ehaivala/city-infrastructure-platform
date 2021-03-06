import uuid

from auditlog.registry import auditlog
from django.conf import settings
from django.contrib.gis.db import models
from django.core.exceptions import ValidationError
from django.db.models import Q
from django.utils.translation import gettext_lazy as _
from enumfields import Enum, EnumField, EnumIntegerField

from ..mixins.models import (
    SoftDeleteModel,
    SourceControlModel,
    UpdatePlanLocationMixin,
    UserControlModel,
)
from .common import (
    Condition,
    DeviceTypeTargetModel,
    InstallationStatus,
    LaneNumber,
    LaneType,
    Lifecycle,
    Reflection,
    Size,
    TrafficControlDeviceType,
)
from .mount import MountPlan, MountReal, MountType
from .plan import Plan
from .utils import SoftDeleteQuerySet


class LocationSpecifier(Enum):
    RIGHT = 1
    LEFT = 2
    ABOVE = 3
    MIDDLE = 4
    VERTICAL = 5

    class Labels:
        RIGHT = _("Right side")
        LEFT = _("Left side")
        ABOVE = _("Above")
        MIDDLE = _("Middle")
        VERTICAL = _("Vertical")


class SignpostPlan(
    UpdatePlanLocationMixin, SourceControlModel, SoftDeleteModel, UserControlModel
):
    id = models.UUIDField(
        primary_key=True, unique=True, editable=False, default=uuid.uuid4
    )
    location = models.PointField(_("Location (2D)"), srid=settings.SRID)
    height = models.DecimalField(
        _("Height"), max_digits=5, decimal_places=2, blank=True, null=True
    )
    direction = models.IntegerField(_("Direction"), default=0)
    device_type = models.ForeignKey(
        TrafficControlDeviceType,
        verbose_name=_("Device type"),
        on_delete=models.PROTECT,
        limit_choices_to=Q(
            Q(target_model=None) | Q(target_model=DeviceTypeTargetModel.SIGNPOST)
        ),
    )
    value = models.IntegerField(_("Signpost value"), blank=True, null=True)
    txt = models.CharField(_("Signpost txt"), max_length=254, blank=True, null=True)
    parent = models.ForeignKey(
        "self",
        verbose_name=_("Parent Signpost Plan"),
        on_delete=models.PROTECT,
        blank=True,
        null=True,
    )
    mount_plan = models.ForeignKey(
        MountPlan,
        verbose_name=_("Mount Plan"),
        on_delete=models.PROTECT,
        blank=True,
        null=True,
    )
    mount_type = models.ForeignKey(
        MountType,
        verbose_name=_("Mount type"),
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
    )
    decision_date = models.DateField(_("Decision date"))
    decision_id = models.CharField(
        _("Decision id"), max_length=254, blank=True, null=True
    )
    validity_period_start = models.DateField(
        _("Validity period start"), blank=True, null=True
    )
    validity_period_end = models.DateField(
        _("Validity period end"), blank=True, null=True
    )
    plan = models.ForeignKey(
        Plan,
        verbose_name=_("Plan"),
        on_delete=models.PROTECT,
        related_name="signpost_plans",
        blank=True,
        null=True,
    )
    owner = models.ForeignKey(
        "traffic_control.Owner",
        verbose_name=_("Owner"),
        blank=False,
        null=False,
        on_delete=models.PROTECT,
    )
    size = EnumField(
        Size,
        verbose_name=_("Size"),
        max_length=1,
        default=Size.MEDIUM,
        blank=True,
        null=True,
    )
    reflection_class = EnumField(
        Reflection,
        verbose_name=_("Reflection"),
        max_length=2,
        default=Reflection.R1,
        blank=True,
        null=True,
    )
    seasonal_validity_period_start = models.DateField(
        _("Seasonal validity period start"), blank=True, null=True
    )
    seasonal_validity_period_end = models.DateField(
        _("Seasonal validity period end"), blank=True, null=True
    )
    attachment_class = models.CharField(
        _("Attachment class"), max_length=254, blank=True, null=True
    )
    target_id = models.CharField(_("Target ID"), max_length=254, blank=True, null=True)
    target_txt = models.CharField(
        _("Target txt"), max_length=254, blank=True, null=True
    )
    responsible_entity = models.CharField(
        _("Responsible entity"), max_length=254, blank=True, null=True
    )
    electric_maintainer = models.CharField(
        _("Electric maintainer"), max_length=254, blank=True, null=True
    )
    lifecycle = EnumIntegerField(
        Lifecycle, verbose_name=_("Lifecycle"), default=Lifecycle.ACTIVE
    )
    road_name = models.CharField(_("Road name"), max_length=254, blank=True, null=True)
    lane_number = EnumField(
        LaneNumber, verbose_name=_("Lane number"), default=LaneNumber.MAIN_1, blank=True
    )
    lane_type = EnumField(
        LaneType,
        verbose_name=_("Lane type"),
        default=LaneType.MAIN,
        blank=True,
    )
    location_specifier = EnumIntegerField(
        LocationSpecifier,
        verbose_name=_("Location specifier"),
        default=LocationSpecifier.RIGHT,
        blank=True,
        null=True,
    )

    objects = SoftDeleteQuerySet.as_manager()

    class Meta:
        db_table = "signpost_plan"
        verbose_name = _("Signpost Plan")
        verbose_name_plural = _("Signpost Plans")
        unique_together = ["source_name", "source_id"]

    def __str__(self):
        return f"{self.id} {self.device_type} {self.txt}"

    def save(self, *args, **kwargs):
        if not self.device_type.validate_relation(DeviceTypeTargetModel.SIGNPOST):
            raise ValidationError(
                f'Device type "{self.device_type}" is not allowed for signposts'
            )

        super().save(*args, **kwargs)


class SignpostPlanFile(models.Model):
    id = models.UUIDField(
        primary_key=True, unique=True, editable=False, default=uuid.uuid4
    )
    file = models.FileField(
        _("File"), blank=False, null=False, upload_to="planfiles/signpost/"
    )
    signpost_plan = models.ForeignKey(
        SignpostPlan, on_delete=models.CASCADE, related_name="files"
    )

    class Meta:
        db_table = "signpost_plan_file"
        verbose_name = _("Signpost Plan File")
        verbose_name_plural = _("Signpost Plan Files")

    def __str__(self):
        return "%s" % self.file


class SignpostReal(SourceControlModel, SoftDeleteModel, UserControlModel):
    id = models.UUIDField(
        primary_key=True, unique=True, editable=False, default=uuid.uuid4
    )
    signpost_plan = models.ForeignKey(
        SignpostPlan,
        verbose_name=_("Signpost Plan"),
        on_delete=models.PROTECT,
        blank=True,
        null=True,
    )
    location = models.PointField(_("Location (2D)"), srid=settings.SRID)
    height = models.DecimalField(
        _("Height"), max_digits=5, decimal_places=2, blank=True, null=True
    )
    direction = models.IntegerField(_("Direction"), default=0)
    device_type = models.ForeignKey(
        TrafficControlDeviceType,
        verbose_name=_("Device type"),
        on_delete=models.PROTECT,
        limit_choices_to=Q(
            Q(target_model=None) | Q(target_model=DeviceTypeTargetModel.SIGNPOST)
        ),
    )
    value = models.IntegerField(_("Signpost value"), blank=True, null=True)
    txt = models.CharField(_("Signpost txt"), max_length=254, blank=True, null=True)
    parent = models.ForeignKey(
        "self",
        verbose_name=_("Parent Signpost Real"),
        on_delete=models.PROTECT,
        blank=True,
        null=True,
    )
    mount_real = models.ForeignKey(
        MountReal,
        verbose_name=_("Mount Real"),
        on_delete=models.PROTECT,
        blank=True,
        null=True,
    )
    mount_type = models.ForeignKey(
        MountType,
        verbose_name=_("Mount type"),
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
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
    validity_period_start = models.DateField(
        _("Validity period start"), blank=True, null=True
    )
    validity_period_end = models.DateField(
        _("Validity period end"), blank=True, null=True
    )
    condition = EnumIntegerField(
        Condition,
        verbose_name=_("Condition"),
        default=Condition.VERY_GOOD,
        blank=True,
        null=True,
    )
    owner = models.ForeignKey(
        "traffic_control.Owner",
        verbose_name=_("Owner"),
        blank=False,
        null=False,
        on_delete=models.PROTECT,
    )
    size = EnumField(
        Size,
        verbose_name=_("Size"),
        max_length=1,
        default=Size.MEDIUM,
        blank=True,
        null=True,
    )
    reflection_class = EnumField(
        Reflection,
        verbose_name=_("Reflection"),
        max_length=2,
        default=Reflection.R1,
        blank=True,
        null=True,
    )
    material = models.CharField(_("Material"), max_length=254, blank=True, null=True)
    seasonal_validity_period_start = models.DateField(
        _("Seasonal validity period start"), blank=True, null=True
    )
    seasonal_validity_period_end = models.DateField(
        _("Seasonal validity period end"), blank=True, null=True
    )
    organization = models.CharField(
        _("Organization"), max_length=254, blank=True, null=True
    )
    manufacturer = models.CharField(
        _("Manufacturer"), max_length=254, blank=True, null=True
    )
    attachment_class = models.CharField(
        _("Attachment class"), max_length=254, blank=True, null=True
    )
    target_id = models.CharField(_("Target ID"), max_length=254, blank=True, null=True)
    target_txt = models.CharField(
        _("Target txt"), max_length=254, blank=True, null=True
    )
    responsible_entity = models.CharField(
        _("Responsible entity"), max_length=254, blank=True, null=True
    )
    electric_maintainer = models.CharField(
        _("Electric maintainer"), max_length=254, blank=True, null=True
    )
    lifecycle = EnumIntegerField(
        Lifecycle, verbose_name=_("Lifecycle"), default=Lifecycle.ACTIVE
    )
    road_name = models.CharField(_("Road name"), max_length=254, blank=True, null=True)
    lane_number = EnumField(
        LaneNumber, verbose_name=_("Lane number"), default=LaneNumber.MAIN_1, blank=True
    )
    lane_type = EnumField(
        LaneType,
        verbose_name=_("Lane type"),
        default=LaneType.MAIN,
        blank=True,
    )
    location_specifier = EnumIntegerField(
        LocationSpecifier,
        verbose_name=_("Location specifier"),
        default=LocationSpecifier.RIGHT,
        blank=True,
        null=True,
    )

    objects = SoftDeleteQuerySet.as_manager()

    class Meta:
        db_table = "signpost_real"
        verbose_name = _("Signpost Real")
        verbose_name_plural = _("Signpost Reals")
        unique_together = ["source_name", "source_id"]

    def __str__(self):
        return f"{self.id} {self.device_type} {self.txt}"

    def save(self, *args, **kwargs):
        if not self.device_type.validate_relation(DeviceTypeTargetModel.SIGNPOST):
            raise ValidationError(
                f'Device type "{self.device_type}" is not allowed for signposts'
            )

        super().save(*args, **kwargs)


class SignpostRealFile(models.Model):
    id = models.UUIDField(
        primary_key=True, unique=True, editable=False, default=uuid.uuid4
    )
    file = models.FileField(
        _("File"), blank=False, null=False, upload_to="realfiles/signpost/"
    )
    signpost_real = models.ForeignKey(
        SignpostReal, on_delete=models.CASCADE, related_name="files"
    )

    class Meta:
        db_table = "signpost_real_file"
        verbose_name = _("Signpost Real File")
        verbose_name_plural = _("Signpost Real Files")

    def __str__(self):
        return f"{self.file}"


auditlog.register(SignpostPlan)
auditlog.register(SignpostReal)
