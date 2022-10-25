from django.db import models
from django.utils.text import slugify
from django_resized import ResizedImageField
from ckeditor.fields import RichTextField

#=================Snippet for sitemaps========================
class Snippet(models.Model):
    title = models.CharField(max_length=80)
    slug = models.SlugField(blank=True, null=True)
    body = models.TextField()
def save(self, *args, **kwargs):
    self.slug = slugify(self.title)
    super().save(*args, **kwargs)
def get_absolute_url(self):
    return f'/{self.slug}'
#================Data models=====================================
class AttractionCategory(models.Model):
    """
    This class creates database tables for categories for each attraction in
    natural park bucegi
    """
    name = models.CharField(max_length=30)
    slug = models.SlugField()
    class Meta:
        verbose_name = 'Attraction Category'
        verbose_name_plural = "Attraction Categories"

class Attraction(models.Model):
    """
    This class creates database tables for each attraction in natural park bucegipark
    linked to attraction category table above, by ForeignKey. The images for attraction
    will be automatically resized using a package : django-resized. Default settings in
    settings.py file.
    """
    name = models.CharField(max_length=30)
    image = ResizedImageField(size=[640,None], upload_to='attraction_images',)
    text = RichTextField()
    categ = models.ForeignKey(AttractionCategory, on_delete=models.CASCADE)
    slug = models.SlugField()
