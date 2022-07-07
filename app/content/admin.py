from django.contrib import admin
from content.models import Info, News, Place, Opening


class InfoAdmin(admin.ModelAdmin):
    pass


class NewsAdmin(admin.ModelAdmin):
    pass


class PlaceAdmin(admin.ModelAdmin):
    pass


class OpeningAdmin(admin.ModelAdmin):
    pass


admin.site.register(Info, InfoAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(Place, PlaceAdmin)
admin.site.register(Opening, OpeningAdmin)
