from django.contrib import admin
from django.contrib.admin import TabularInline
from django.views import View
from nested_inline.admin import NestedStackedInline, NestedModelAdmin

from ballinat.models import Contacts, TypeOfSocialMedia, Slide, Paragraph, Subtitle, Blog, AboutUs, MesazheNgaKlientet, \
    Gjendja, Teknikat, FototEPunimit, Punim, Paragraphs, AfterSlides

"""
==================================================SLIDES ===============================================================
"""


class SlideAdmin(admin.ModelAdmin, View):
    list_display = ['image_preview', 'title',  'type_of_page', 'active_in_footer', 'active' ]
    list_editable = ['active', 'type_of_page', 'active_in_footer']


admin.site.register(Slide, SlideAdmin)

"""
==================================================AFTER SLIDES==========================================================
"""


class AfterSlidesAdmin(admin.ModelAdmin, View):
    list_display = ['title', 'pershkirmi', 'ikona',  'active' ]
    list_editable = ['active']


admin.site.register(AfterSlides, AfterSlidesAdmin)

"""
==================================================ABOUT US==============================================================
"""


class ParagraphsAdminInline(TabularInline):
    extra = 1
    model = Paragraphs


class AboutUsAdmin(admin.ModelAdmin, View):
    inlines = (ParagraphsAdminInline,)
    list_display = [ 'image_preview', 'title', 'since', 'yars_of_experience', 'experience_sentecne', 'active' ]
    list_editable = ['active']


admin.site.register(AboutUs, AboutUsAdmin)

"""
==================================================TESTIMONIAL===========================================================
"""


class MesazheNgaKlientetAdmin(admin.ModelAdmin, View):
    list_display = [ 'image_preview', 'emri_mbiemri',  'profesioni', 'mesazhi' ]


admin.site.register(MesazheNgaKlientet, MesazheNgaKlientetAdmin)

"""
==================================================BLOG==================================================================
"""


class ParagraphInline(NestedStackedInline):
    model = Paragraph
    extra = 1


class SubtitleInline(NestedStackedInline):
    model = Subtitle
    extra = 1
    inlines = [ParagraphInline]


class BlogAdmin(NestedModelAdmin):
    model = Blog
    inlines = [SubtitleInline]
    list_display = ['image_preview', 'title', 'date_created', 'active_in_footer']
    list_editable = ['date_created', 'active_in_footer']
    exclude = ["slug_blog"]


admin.site.register(Blog, BlogAdmin)

"""
==================================================GJENDJA===============================================================
"""


class GjendjaAdmin(admin.ModelAdmin, View):
    list_display = ['gjendja', 'ngjyra']


admin.site.register(Gjendja, GjendjaAdmin)


"""
==================================================TEKNIKAT==============================================================
"""


class TeknikatAdmin(admin.ModelAdmin, View):
    list_display = [ 'image_preview', 'teknika',  'pershkrimi', 'active']
    list_editable = ['active']


admin.site.register(Teknikat, TeknikatAdmin)


"""
==================================================PUNIMET===============================================================
"""


class FototEPunimitAdminInline(TabularInline):
    extra = 1
    model = FototEPunimit


class PunimAdmin(admin.ModelAdmin):
    inlines = (FototEPunimitAdminInline,)
    list_display =['image_preview', 'title',   'date_created', 'price', 'teknikat', 'gjendja']
    list_editable = [ 'date_created', 'teknikat', 'gjendja']


admin.site.register(Punim, PunimAdmin)

"""
==================================================CONTACT INFO==========================================================
"""


class ContactsAdmin(admin.ModelAdmin, View):
    list_display = ['company_name', 'active', 'phone_number','email', 'location',  'company_type']
    list_editable = ['active']


admin.site.register(Contacts, ContactsAdmin)


class TypeOfSocialMediaAdmin(admin.ModelAdmin, View):
    list_display = ['name_of_media','icon_of_social_media', 'link_of_social_media']


admin.site.register(TypeOfSocialMedia, TypeOfSocialMediaAdmin)