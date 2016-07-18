from django.contrib import admin

# Register your models here.
from .models import Choice, Question, Product, CaseStudie

# admin.site.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]

class ProductAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['product_name']}),
        ('Images', {'fields': ['image_1', 'image_2', 'image_3', 'image_4', 'image_5']}),
        ('Date information', {'fields': ['update_date']}),
        ('Product Description', {'fields': ['product_description', 'replacement']}),
        ('Product Specifications', {'fields': ['wattage', 'lumens',
         'lumens_per_watt', 'cct', 'cri', 'dimensions', 'colors', 'life_span',
         'weight', 'warranty']}),
         ('Product Certification', {'fields': ['ul_certified', 'dlc_certified', 'isIndoor']}),
    ]

class CaseStudiesAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['project_name']}),
        ('Project Description', {'fields': ['project_description']}),
        ('Project Location Address', {'fields': ['address']}),
    ]

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
admin.site.register(Product, ProductAdmin)
admin.site.register(CaseStudie, CaseStudiesAdmin)
