from django.db import models
from django.utils import timezone
# Create your models here.
from django.utils.text import slugify
from django.db.models.signals import pre_save, post_save
import pretty_errors
class Article(models.Model):
  title = models.CharField(max_length=120)
  slug = models.SlugField(max_length= 50,blank= True , null= True)
  content = models.TextField()
  timestamp = models.DateTimeField(auto_now_add = True)
  updated = models.DateTimeField(auto_now = True)
  publish = models.DateField(auto_now_add = False, auto_now = False, default= timezone.now,null=True, blank= True)

  def save(self, *args, **kwargs):
    # if self.slug is None:
    #   self.slug = slugify(self.title)
    super().save(*args, **kwargs)

def article_pre_save(sender, instance,*args, **kwargs):
  print('pre-save')
  # if instance.slug is None:
  instance.slug = slugify(instance.title)
pre_save.connect(article_pre_save, sender = Article)


def article_post_save(*args, **kwargs):
  print('post-save')
  if created:
      instance.slug = slugify(instance.title)
      instance.save()
post_save.connect(article_post_save, sender = Article)