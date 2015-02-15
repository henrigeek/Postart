from django.db import models
from django.utils.encoding import smart_unicode
from django.contrib.auth.models import User
from django.contrib import admin
from django.conf import settings
from string import join
from easy_thumbnails.fields import ThumbnailerField
import os

class Author(models.Model):
    first_name=models.CharField(max_length=120, null=True, blank = True)
    last_name=models.CharField(max_length=120, null=True, blank = True)
    email = models.EmailField()
    headshot = models.ImageField(upload_to='profile/author_headshots')
    
    def save(self, *args, **kwargs):
        full_name = '%s%s' % (self.first_name, self.last_name)
        self.full_name = full_name.replace(' ', '')
        super(Author, self).save(*args, **kwargs)
        
    
    def __unicode__(self):
        return smart_unicode(self.emails)
    

    def __unicode__(self):              # __unicode__ on Python 2
        return self.first_name
    
    
    

class Album(models.Model):
    title = models.CharField(max_length=60)
    public = models.BooleanField(default=False)
    def __unicode__(self):
        return self.title
    def images(self):
        lst = [x.image.name for x in self.image_set.all()]
        lst = ["<a href='/media/%s'>%s</a>" % (x, x.split('/')[-1]) for x in lst]
        return join(lst, ', ')
    images.allow_tags = True
        
class Tag(models.Model):
    tag = models.CharField(max_length=50)
    def __unicode__(self):
        return self.tag

class Image(models.Model):
    authors=models.ManyToManyField(Author, blank=True)
    title = models.CharField(max_length=60, blank=True, null=True)
    image = models.FileField(upload_to="images/")
    #thumbimage = ThumbnailerField(upload_to="images/", default='DEFAULT VALUE')
    tags = models.ManyToManyField(Tag, blank=True)
    albums = models.ManyToManyField(Album, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)
    width = models.IntegerField(blank=True, null=True)
    height = models.IntegerField(blank=True, null=True)
    user = models.ForeignKey(User, null=True, blank=True)
    #def get_absolute_url(self):
    #    from django.core.urlresolvers import reverse
    #    return reverse('image-view',kwargs={'pk': self.pk})
    def get_success_url(self,*args,**kwargs):
        return reverse(success_url, kwargs={'pk' : self.object.pk})
    #def save(self, *args, **kwargs):
    #    if not self.thumbimage:
            # Setting the value of new_field with website's value
    #        self.thumbimage = self.image
        # Saving the object with the default save() function
    #    super(Image, self).save(*args, **kwargs)
    def __unicode__(self):
        return self.image.name
    
    def size(self):
            return "%s x %s" % (self.width, self.height)

    def tags_(self):
        lst = [x[1] for x in self.tags.values_list()]
        return str(join(lst, ', '))
    
    def authors_(self):
        lst = [x[1] for x in self.authors.values_list()]
        return str(join(lst, ', '))
    
    
    #    thumbnail.allow_tags = True
    
    





# Create your models here.
