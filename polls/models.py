from django.db import models

# Create your models here.
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
    image_1 = models.CharField(max_length=200)
    image_2 = models.CharField(max_length=200)
    image_3 = models.CharField(max_length=200)
    image_4 = models.CharField(max_length=200)
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
    life_span = models.CharField(max_length=10)
    weight = models.CharField(max_length=20)
    warranty = models.CharField(max_length=30)
    replacement = models.CharField(max_length=30)
    ul_certified = models.BooleanField(default = False)
    dlc_certified = models.BooleanField(default = False)
    isIndoor = models.BooleanField(default = False)
    def __str__(self):
        return self.product_name

class CaseStudie(models.Model):
    project_name = models.CharField(max_length=100)
    project_description = models.CharField(max_length=200)
    address = models.CharField(max_length=150)
    def __str__(self):
        return self.project_name
