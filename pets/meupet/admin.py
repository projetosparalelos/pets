from django.contrib import admin

from meupet import models


class PetAdmin(admin.ModelAdmin):
    list_display = ('name', 'kind', 'city', 'description', 'status', 'published',
                    'created', 'modified', 'request_sent', 'active')


admin.site.register(models.Pet, PetAdmin)
admin.site.register(models.Kind)
admin.site.register(models.Photo)
