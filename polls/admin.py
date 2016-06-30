from django.contrib import admin

# Register your models here.

from .models import Choice, Question, Product

# admin.site.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]

class ProductAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['product_name']}),
        ('Date information', {'fields': ['update_date']}),
        ('Product Description', {'fields': ['product_description']}),
    ]
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
admin.site.register(Product, ProductAdmin)
