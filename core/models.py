from enum import unique
from django.db import models
from users.models import User


LANGUAGES = (
    ("Uzbek", "O'zbek tili"),    
    ("Russian", "Rus tili"),    
    ("English", "Ingliz tili"),    
    ("Other", "Boshqa"),    
    ("Several", "Bir nechta"),    
)

class LinkType(models.Model):
    # id = models.PrimaryKey(unique=True)
    name = models.CharField(max_length=100)
    # LinkType  *  --->  1  Section
    section = models.ForeignKey("Section", on_delete=models.CASCADE)
    slug = models.SlugField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Section(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class GeneralLink(models.Model):
    name = models.CharField(max_length=250)
    url = models.URLField(max_length=350, null=True, blank=True)
    photo = models.ImageField(upload_to='general-link')
    # need to install Pillow to use ImageField (pip install Pillow)
    type = models.ForeignKey(LinkType, on_delete=models.SET_NULL, null=True)
    # GeneralLink  *   ---->   1 LinkType 
    section = models.ForeignKey(Section, on_delete=models.SET_NULL, null=True)
    short_description = models.CharField(max_length=150)
    description = models.TextField(null=True, blank=True)
    tags = models.ManyToManyField("Tag", blank=True)
    company = models.ForeignKey("Company", on_delete=models.SET_NULL, null=True, blank=True)
    language = models.CharField(max_length=50, choices=LANGUAGES, null=True, blank=True)
    author = models.ForeignKey("users.User", on_delete=models.SET_NULL, null=True, blank=True)
    slug = models.SlugField(max_length=250, unique=True)
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class CompanyType(models.Model):
    name = models.CharField(max_length=150)
    slug = models.SlugField(max_length=150, unique=True)

    def __str__(self):
        return self.name


class Company(models.Model):
    name = models.CharField(max_length=150)
    url = models.URLField(max_length=200, null=True, blank=True)
    photo = models.ImageField(upload_to='companies')
    type = models.ForeignKey(CompanyType, on_delete=models.SET_NULL, null=True)
    short_description = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    address = models.CharField(max_length=100)
    slug = models.SlugField(max_length=150, unique=True)
    author = models.ForeignKey("users.User", on_delete=models.SET_NULL, null=True)
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)

    def __str__(self):
        return self.name


# TABLES (DATABASE) RELATIONS

# Link  *   --->  1  Section
# section = models.ForeignKey(Section, on_delete=models.CASCADE)

# Link  *    --->  * Tag
# tags = models.ManyToManyField("Tag")

# Link  1    --->  1  Table
# table_name = models.OneToOneField(Table, on_delete=models.CASCADE)

