from django.contrib import admin

# Register your models here.
from .models import Choice, Question, Product, CaseStudie, Nav

# admin.site.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]

class ProductAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['product_name', 'slug']}),
        ('Images', {'fields': ['image_1', 'image_2', 'image_3', 'image_4', 'image_5']}),
        ('Date information', {'fields': ['update_date']}),
        ('Product Description', {'fields': ['product_description', 'replacement']}),
        ('Product Specifications', {'fields': ['wattage', 'lumens',
         'lumens_per_watt', 'cct', 'cri', 'dimensions', 'colors', 'life_span',
         'weight', 'warranty']}),
         ('Product Certification', {'fields': ['ul_certified', 'dlc_certified', 'isIndoor', 'isOutdoor', 'isFeatured']}),
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

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
admin.site.register(Product, ProductAdmin)
admin.site.register(CaseStudie, CaseStudiesAdmin)
admin.site.register(Nav, NavAdmin)
