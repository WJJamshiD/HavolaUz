from gc import unfreeze
from django.db import models


class Link(models.Model):
    name = models.CharField(max_length=50)   # Varchar(50)
    description = models.TextField(null=True)         # varchar(-)
    url = models.URLField(help_text='Iltimos to\'g\ri URL kiriting!')                  # Varchar()
    created_at = models.DateTimeField(auto_now_add=True)      # TIMESTAMP
    modified_at = models.DateTimeField(auto_now=True)

    # objects = models.Manager()

    def __str__(self):  # -> str(object) => 
        return self.name

    # class Meta:


# class LinkChangesHistory(models.Model):
#     link = models.ForeignKey(Link, on_delete=models.CASCADE) # 3
#     name = models.CharField(max_length=50)   # Varchar(50)
#     description = models.TextField(null=True)         # varchar(-)
#     url = models.URLField()                  # Varchar()
#     created_at = models.DateTimeField(auto_now_add=True)      # TIMESTAMP


# Link.objects.all()  -- barcha linklarni olish
# Link.objects.first()  -- tablitsadagi 1-linkni olish
# Link.objects.last()  -- tablitsadagi oxirgi linkni olish
# yangi_link = Link.objects.create(name='', ...)  -- yangi obyekt yaratadi va db ga ham saqlaydi

# python manage.py makemigrations   -->   
# python manage.py migrate   --> 
# python manage.py showmigrations -->
# python manage.py shell  -> django shell ni ochadi
