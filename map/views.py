from django.conf import settings
from django.contrib.admin.views.decorators import staff_member_required
from django.http import JsonResponse
from django.shortcuts import render
from django.utils.translation import ugettext as _

from .models import Layer


@staff_member_required
def map_view(request):
    return render(request, "index.html")


def map_config(request):
    language_code = request.LANGUAGE_CODE
    basemaps = []
    for basemap in Layer.objects.filter(is_basemap=True):
        basemaps.append(
            {
                "identifier": basemap.identifier,
                "name": getattr(basemap, f"name_{language_code}"),
            }
        )

    overlays = []
    for overlay in Layer.objects.filter(is_basemap=False):
        overlays.append(
            {
                "identifier": overlay.identifier,
                "name": getattr(overlay, f"name_{language_code}"),
            }
        )

    config = {
        "basemapConfig": {
            "name": _("Basemaps"),
            "layers": basemaps,
            "sourceUrl": settings.BASEMAP_SOURCE_URL,
        },
        "overlayConfig": {
            "name": _("Overlays"),
            "layers": overlays,
            "sourceUrl": settings.OVERLAY_SOURCE_URL,
        },
    }
    return JsonResponse(config)
