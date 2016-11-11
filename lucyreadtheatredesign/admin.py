from __future__ import unicode_literals

from copy import deepcopy

from django.contrib import admin

from mezzanine.galleries.models import Gallery
from mezzanine.galleries.admin import GalleryAdmin

gallery_fieldsets = deepcopy(GalleryAdmin.fieldsets)
gallery_fieldsets[0][1]["fields"] += ("featured_image",)
GalleryAdmin.fieldsets = gallery_fieldsets

admin.site.unregister(Gallery)
admin.site.register(Gallery, GalleryAdmin)
