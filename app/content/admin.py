from django.contrib import admin
from content.models import Info, News, Place, Opening, OwlImage, Intro

owl_text = [
    """
Diese Bilder werden auf der Startseite durchlaufen und angezeigt.
Der Name muss einzigartig sein.
""",
    """
Die Bilddatein müssen PNG-, JPEG- bzw. JPG-Datein sein.
Der Name der Datei sollte dem Inhalt entsprechen und wird nicht gespeichert,
wenn diese Datei bereits existiert.
""", ]


class InfoAdmin(admin.ModelAdmin):
    list_display = ('title', 'header', 'prior', 'get_days_display')
    fieldsets = (
        (None, {'fields': ('header', 'title', 'description',)}),
        ('An welchem Tag soll diese Information auf der Startseite angezeigt werden?',
         {'fields': ('days',)}),
        ('Wichtige ausnahme Information', {'fields': ('prior', 'start_date', 'end_date',)}),
    )

    @admin.display(description='Anzeigetage')
    def get_days_display(self, obj):
        days = [Info.WEEKDAY_CHOICES[int(i)][1] for i in obj.days]
        return days


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


class OwlImageAdmin(admin.ModelAdmin):
    list_display = ('name', )

    fieldsets = (
        (owl_text[0], {'fields': ('name',)}),
        (owl_text[1], {'fields': ('img',)}),
    )


class IntroAdmin(admin.ModelAdmin):
    list_display = ('url_path', 'title',)

    fieldsets = (
        (None, {'fields': ('title', 'url_path')}),
        ('Kontext', {'fields': ('header', 'description_list',)}),
    )


admin.site.register(Info, InfoAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(Place, PlaceAdmin)
admin.site.register(Opening, OpeningAdmin)
admin.site.register(OwlImage, OwlImageAdmin)
admin.site.register(Intro, IntroAdmin)
