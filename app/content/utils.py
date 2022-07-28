from django.utils.text import slugify


def germanslugify(value):
    replacements = [
        (u'ä', u'ae'),
        (u'ö', u'oe'),
        (u'ü', u'ue'),
        (u'ß', u'ss'),
    ]
    for (s, r) in replacements:
        value = value.replace(s, r)
    return slugify(value)
