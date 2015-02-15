from string import join
import os
from os.path import join as pjoin
from django.db import models
from django.contrib import admin
from photo.models import Album, Image, Tag, Author
from django.conf import settings
from PIL import Image as PImage


class AlbumAdmin(admin.ModelAdmin):
    search_fields = ["title"]
    list_display = ["title"]
    #def images(self):
    #        lst = [x.image.name for x in self.image_set.all()]
    #        lst = ["<a href='/media/%s'>%s</a>" % (x, x.split('/')[-1]) for x in lst]
    #        return join(lst, ', ')
    #images.allow_tags = True
    
class AuthorAdmin(admin.ModelAdmin):
    list_display = ["__unicode__", "first_name", "last_name", "email"]
    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.save()

class TagAdmin(admin.ModelAdmin):
    list_display = ["tag"]

class ImageAdmin(admin.ModelAdmin):
    # search_fields = ["title"]
    list_display = ["__unicode__", "title", "user", "rating", "size", "tags_","created","authors_"]
    list_filter = ["tags", "albums", "user"]

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.save()

admin.site.register(Album, AlbumAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Image, ImageAdmin)
admin.site.register(Author,AuthorAdmin)

# Register your models here.
