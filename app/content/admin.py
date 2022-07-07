from django.contrib import admin
from content.models import Info, News, Place, Opening


class InfoAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'prior', 'days')
    fieldsets = (
        (None, {'fields': ('title', 'description',)}),
        ('An welchem Tag soll diese Information auf der Startseite angezeigt werden?',
         {'fields': ('days',)}),
        ('Wichtige ausnahme Information', {'fields': ('prior', 'start_date', 'end_date',)}),
    )


class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'description',)
    fieldsets = (
        (None, {'fields': ('title',)}),
        ('Kontext:', {'fields': ('description', 'date',)}),
    )


class PlaceAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ['name']
    autocomplete_fields = ['meals', ]

    fieldsets = (
        (None, {'fields': ('name',)}),
        ('Alle Produkte an diesem Ort:', {'fields': ('meals',)}),
    )


class OpeningAdmin(admin.ModelAdmin):
    list_display = ('place', 'times')
    autocomplete_fields = ['place', ]

    fieldsets = (
        (None, {'fields': ('place',)}),
        ('An welchen Tagen hat der Ort geöffnet?', {'fields': ('times',)}),
    )


admin.site.register(Info, InfoAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(Place, PlaceAdmin)
admin.site.register(Opening, OpeningAdmin)
