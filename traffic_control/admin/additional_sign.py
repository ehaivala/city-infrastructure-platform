from django.contrib.gis import admin
from django.utils.translation import gettext_lazy as _
from enumfields.admin import EnumFieldListFilter

from ..constants import HELSINKI_LATITUDE, HELSINKI_LONGITUDE
from ..forms import AdditionalSignPlanModelForm, AdditionalSignRealModelForm
from ..mixins import (
    EnumChoiceValueDisplayAdminMixin,
    Point3DFieldAdminMixin,
    SoftDeleteAdminMixin,
    UserStampedAdminMixin,
    UserStampedInlineAdminMixin,
)
from ..models import (
    AdditionalSignContentPlan,
    AdditionalSignContentReal,
    AdditionalSignPlan,
    AdditionalSignReal,
)
from .audit_log import AuditLogHistoryAdmin


class BaseAdditionalSignContentInline(admin.TabularInline):
    model = None
    fields = (
        "order",
        "text",
        "device_type",
        "created_at",
        "updated_at",
        "created_by",
        "updated_by",
    )
    readonly_fields = ("created_at", "updated_at", "created_by", "updated_by")
    verbose_name = _("Additional sign content")
    verbose_name_plural = _("Additional sign contents")
    extra = 0
    ordering = ("order",)


class AdditionalSignContentPlanInline(BaseAdditionalSignContentInline):
    model = AdditionalSignContentPlan


class AdditionalSignContentRealInline(BaseAdditionalSignContentInline):
    model = AdditionalSignContentReal


@admin.register(AdditionalSignPlan)
class AdditionalSignPlanAdmin(
    EnumChoiceValueDisplayAdminMixin,
    SoftDeleteAdminMixin,
    UserStampedAdminMixin,
    UserStampedInlineAdminMixin,
    Point3DFieldAdminMixin,
    admin.OSMGeoAdmin,
    AuditLogHistoryAdmin,
):
    form = AdditionalSignPlanModelForm
    fieldsets = (
        (
            _("General information"),
            {"fields": ("owner", "mount_type", "source_id", "source_name")},
        ),
        (
            _("Location information"),
            {
                "fields": (
                    ("location", "z_coord"),
                    "direction",
                    "road_name",
                    "lane_number",
                    "lane_type",
                    "location_specifier",
                    "affect_area",
                )
            },
        ),
        (
            _("Physical properties"),
            {"fields": ("height", "color", "reflection_class", "surface_class")},
        ),
        (_("Related models"), {"fields": ("parent", "plan", "mount_plan")}),
        (_("Decision information"), {"fields": ("decision_date", "decision_id")}),
        (
            _("Validity"),
            {
                "fields": (
                    ("validity_period_start", "validity_period_end"),
                    ("seasonal_validity_period_start", "seasonal_validity_period_end"),
                    "lifecycle",
                )
            },
        ),
        (
            _("Metadata"),
            {"fields": ("created_at", "updated_at", "created_by", "updated_by")},
        ),
    )

    default_lon = HELSINKI_LONGITUDE
    default_lat = HELSINKI_LATITUDE
    default_zoom = 12
    list_display = (
        "id",
        "lifecycle",
        "location",
        "decision_date",
    )
    readonly_fields = (
        "created_at",
        "updated_at",
        "created_by",
        "updated_by",
        "source_name",
        "source_id",
    )
    raw_id_fields = ("parent", "plan", "mount_plan")
    list_filter = SoftDeleteAdminMixin.list_filter + ["owner"]
    ordering = ("-created_at",)
    inlines = (AdditionalSignContentPlanInline,)


@admin.register(AdditionalSignReal)
class AdditionalSignRealAdmin(
    EnumChoiceValueDisplayAdminMixin,
    SoftDeleteAdminMixin,
    UserStampedAdminMixin,
    UserStampedInlineAdminMixin,
    Point3DFieldAdminMixin,
    admin.OSMGeoAdmin,
    AuditLogHistoryAdmin,
):
    form = AdditionalSignRealModelForm
    fieldsets = (
        (
            _("General information"),
            {
                "fields": (
                    "owner",
                    "mount_type",
                    "permit_decision_id",
                    "attachment_url",
                    "scanned_at",
                    "operation",
                    "manufacturer",
                    "rfid",
                    "legacy_code",
                    "source_id",
                    "source_name",
                )
            },
        ),
        (
            _("Location information"),
            {
                "fields": (
                    ("location", "z_coord"),
                    "direction",
                    "road_name",
                    "lane_number",
                    "lane_type",
                    "location_specifier",
                    "affect_area",
                )
            },
        ),
        (
            _("Physical properties"),
            {
                "fields": (
                    "size",
                    "height",
                    "color",
                    "reflection_class",
                    "surface_class",
                    "condition",
                )
            },
        ),
        (
            _("Related models"),
            {"fields": ("parent", "additional_sign_plan", "mount_real")},
        ),
        (
            _("Installation information"),
            {
                "fields": (
                    "installation_id",
                    "installation_details",
                    "installation_date",
                    "installation_status",
                    "installed_by",
                )
            },
        ),
        (
            _("Validity"),
            {
                "fields": (
                    ("validity_period_start", "validity_period_end"),
                    ("seasonal_validity_period_start", "seasonal_validity_period_end"),
                    "lifecycle",
                )
            },
        ),
        (
            _("Metadata"),
            {"fields": ("created_at", "updated_at", "created_by", "updated_by")},
        ),
    )
    default_lon = HELSINKI_LONGITUDE
    default_lat = HELSINKI_LATITUDE
    default_zoom = 12
    list_display = (
        "id",
        "additional_sign_plan",
        "legacy_code",
        "installation_id",
        "installation_details",
        "installation_date",
        "size",
        "mount_real",
        "mount_type",
        "height",
        "installation_status",
        "validity_period_start",
        "validity_period_end",
        "condition",
        "reflection_class",
        "surface_class",
        "seasonal_validity_period_start",
        "seasonal_validity_period_end",
        "owner",
        "lifecycle",
        "road_name",
        "lane_number",
        "lane_type",
        "location_specifier",
        "rfid",
        "direction",
        "operation",
        "manufacturer",
        "permit_decision_id",
        "color",
        "attachment_url",
        "scanned_at",
        "created_at",
        "created_by",
        "updated_at",
        "updated_by",
        "source_id",
        "source_name",
    )
    readonly_fields = (
        "created_at",
        "updated_at",
        "created_by",
        "updated_by",
        "source_name",
        "source_id",
    )
    raw_id_fields = ("parent", "additional_sign_plan", "mount_real")
    ordering = ("-created_at",)
    list_filter = SoftDeleteAdminMixin.list_filter + [
        ("lifecycle", EnumFieldListFilter),
        ("installation_status", EnumFieldListFilter),
        ("condition", EnumFieldListFilter),
        ("reflection_class", EnumFieldListFilter),
        ("surface_class", EnumFieldListFilter),
        ("location_specifier", EnumFieldListFilter),
        ("color", EnumFieldListFilter),
        "owner",
    ]
    search_fields = (
        "additional_sign_plan__id",
        "content__device_type__code",
        "content__device_type__description",
        "content__text",
        "size",
        "mount_real__id",
        "height",
        "reflection_class",
        "surface_class",
        "owner",
        "road_name",
        "lane_number",
        "lane_type",
        "source_id",
        "source_name",
    )
    inlines = (AdditionalSignContentRealInline,)
