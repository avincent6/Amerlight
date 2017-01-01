from django.contrib import admin

# Register your models here.
from .models import Choice, Question, Product, CaseStudie, Nav, Faq, New

# admin.site.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]

class ProductAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['product_name', 'slug', ]}),
        ('Images', {'fields': ['image_1', 'image_2', 'image_3', 'image_4', 'image_5']}),
        ('Date information', {'fields': ['update_date']}),
        ('Product Description', {'fields': ['product_description', 'product_type', 'replacement', 'installation_info']}),
        ('Product Specifications', {'fields': ['wattage', 'lumens',
         'lumens_per_watt', 'cct', 'cri', 'dimensions', 'colors', 'life_span',
         'weight', 'warranty']}),
         ('Product Certification', {'fields': ['ul_certified', 'dlc_certified', 'isIndoor', 'isOutdoor', 'isFeatured']}),
         ('Benefit List', {'fields': ['check_1', 'check_2', 'check_3', 'check_4', 'check_5']}),
         ('Specification Documents', {'fields': ['pdf_link', 'pdf_preview', 'ies_zip',
          'ies_name_1', 'ies_link_1', 'ies_name_2','ies_link_2', 'ies_name_3', 'ies_link_3']}),
         ('Applications used with this Product', {'fields': ['isAutomotive', 'isInstitutional',
          'isAirport', 'isHospital', 'isHotel']}),
    ]

class CaseStudiesAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['project_name', 'slug']}),
        ('Project Description', {'fields': ['project_description']}),
        ('Project Location Address', {'fields': ['address', 'address_link']}),
        ('Testimony', {'fields': ['testimony_quote']}),
        ('Images', {'fields': ['image_1', 'image_2', 'image_3', 'image_4', 'image_5']}),
        ('Type', {'fields': ['isIndustrial']}),
        ('Type', {'fields': ['isAutomotive']}),
        ('Type', {'fields': ['isInstitutional', 'isFeatured']}),

    ]

class NavAdmin(admin.ModelAdmin):
    fieldsets = [
    ('Featured Product Links', {'fields': ['featured_product_1', 'featured_product_2', 'featured_product_3',  'featured_product_4',  'featured_product_5']}),
    ]

class FaqAdmin(admin.ModelAdmin):
    fieldsets = [
    ('Frequently Asked Questions', {'fields': ['question', 'answer', 'resource_link' ]})
    ]

class NewAdmin(admin.ModelAdmin):
    fieldsets = [
    ('News Articles', {'fields': ['headline', 'slug', 'pub_date', 'author' ]}),
    ('Short Summary', {'fields': ['summary']}),
    ('Article', {'fields': ['article']}),
    ('Type', {'fields': ['isFeatured']}),
    ]


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
admin.site.register(Product, ProductAdmin)
admin.site.register(CaseStudie, CaseStudiesAdmin)
admin.site.register(Nav, NavAdmin)
admin.site.register(Faq, FaqAdmin)
admin.site.register(New, NewAdmin)
