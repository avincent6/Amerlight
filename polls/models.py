from django.db import models

# Create your models here.

class Nav(models.Model):
    featured_product_1 = models.CharField(max_length=100)
    featured_product_2 = models.CharField(max_length=100)
    featured_product_3 = models.CharField(max_length=100)
    featured_product_4 = models.CharField(max_length=100)
    featured_product_5 = models.CharField(max_length=100)
    def __str__(self):
        return self.featured_products_1



class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text

class Product(models.Model):
    product_name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=50)
    image_1 = models.CharField(max_length=200)
    image_2 = models.CharField(max_length=200)
    image_3 = models.CharField(max_length=200)
    image_4 = models.CharField(max_length=250)
    image_5 = models.CharField(max_length=200)
    update_date = models.DateTimeField('date updated')
    product_description = models.CharField(max_length=200)
    wattage = models.CharField(max_length=20)
    lumens = models.CharField(max_length=20)
    lumens_per_watt = models.CharField(max_length=20)
    cct = models.CharField(max_length=30)
    cri = models.CharField(max_length=20)
    dimensions = models.CharField(max_length=30)
    colors = models.CharField(max_length=40)
    life_span = models.CharField(max_length=25)
    weight = models.CharField(max_length=20)
    warranty = models.CharField(max_length=30)
    replacement = models.CharField(max_length=30)
    ul_certified = models.BooleanField(default = False)
    dlc_certified = models.BooleanField(default = False)
    isIndoor = models.BooleanField(default = False)
    isOutdoor = models.BooleanField(default = False)
    isFeatured = models.BooleanField(default=False)
    class Meta:
        ordering = ['product_name']
    def __str__(self):
        return self.product_name

class CaseStudie(models.Model):
    project_name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=50)
    project_description = models.CharField(max_length=200)
    address = models.CharField(max_length=150)
    address_link = models.CharField(max_length=150)
    pdf_link = models.CharField(max_length=200)
    video_link = models.CharField(max_length=150)
    testimony_quote = models.CharField(max_length=250)
    image_1 = models.CharField(max_length=200)
    image_2 = models.CharField(max_length=200)
    image_3 = models.CharField(max_length=200)
    image_4 = models.CharField(max_length=200)
    image_5 = models.CharField(max_length=200)
    isIndustrial = models.BooleanField(default = False)
    isAutomotive = models.BooleanField(default = False)
    isInstitutional = models.BooleanField(default = False)
    isFeatured = models.BooleanField(default=False)

    def __str__(self):
        return self.project_name
