from django.views.generic import ListView, DetailView, UpdateView, CreateView, UpdateView, DeleteView, ArchiveIndexView
from django.core.urlresolvers import reverse, reverse_lazy
from photo.models import Tag, Image, Album, Author
from django.contrib.auth.models import User
from django.conf import settings
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.utils.decorators import method_decorator


def logout_view(request):
    auth.logout(request)
    # Redirect to a success page.
    return HttpResponseRedirect("/photo/")


#class ProtectedView(ListView):
 #   @method_decorator(login_required)
  #  def dispatch(self, *args, **kwargs):
   #     return super(ProtectedView, self).dispatch(*args, **kwargs)

#class LoginRequiredMixin(object):
#    @classmethod
#    def as_view(cls, **initkwargs):
#        view = super(LoginRequiredMixin, cls).as_view(**initkwargs)
#        return login_required(view)


class ListAuthor(ListView):
    model = Author
    template_name = 'Author_List.html'
    
    #def get_queryset(self):
    #    self.author = get_object_or_404(Author, name=self.args[0])
    #    return Image.objects.filter(image=self.image)

class AuthorView(DetailView):
    model = Author
    template_name ='Author_Detail.html'
    #def get_queryset(self):
    #    self.author = get_object_or_404(Author, name=self.args[0])
    #    return Image.objects.filter(image=self.image)


class ImageView(DetailView):
    model = Image
    fields = ['name','ratings','authors']
    allow_empty = True
    template_name = 'image.html'

    
class ImageArchive(ArchiveIndexView):
    model = Image
    date_field="created"

    
class ListImage(ListView):
    template_name = 'Image_List.html'
    model = Image

class TopImage(ListView):
    queryset= Image.objects.order_by('-title')[:10]
    template_name = 'top_pictures.html'


class AuthorCreate(CreateView):
    def get_success_url(self):
        return reverse('photo:create-user',args=(self.object.pk,))
    model = Author
    template_name = 'author_create.html'
    fields = ['first_name','last_name','headshot','email']
    
    

    
class ImageCreate(CreateView):
    model = Image
    template_name='image_create.html'
    fields = ['title','image']
    def get_success_url(self,*args,**kwargs):
        return reverse('photo:image-view', kwargs={'pk' : self.object.pk})
    
    
class ImageUpdate(UpdateView):
    model = Image
    template_name = 'image_update.html'
    
class ImageDelete(DeleteView):
    model = Image
    template_name = 'image_delete.html'
    success_url='/photo/'
    #def get_form_kwargs(self, *args, **kwargs):
    #    kwargs = super(ImageDelete, self).get_form_kwargs(
    #        *args, **kwargs)
    #    return kwargs
    
def ImageLike(request, pk):
    if pk:
        a=Image.objects.get(id=pk)
        count=a.rating
        count+=1
        a.rating=count
        a.save()
    return HttpResponseRedirect('/photo/image/%s' %pk)

def CreateUser(request, pk):
    if pk:
        a=Author.objects.get(id=pk)
        name = a.first_name + a.last_name
        email_user=a.email
        user = User.objects.create_user(name,email_user,'')
        user.last_name=a.last_name
        user.first_name = a.first_name
        user.save()
    return HttpResponseRedirect('/photo/author/%s' %pk)


