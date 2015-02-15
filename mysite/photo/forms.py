from django import forms
from photo.models import Albums, Image, Author

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['first_name', 'last_name','email']

class AlbumForm(forms.ModelForm):
    class Meta:
        model = Albums
   
class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        
def upload_file(request):
    if request.method == 'POST':
        form = ModelFormWithFileField(request.POST, request.FILES)
        if form.is_valid():
            # file is saved
            form.save()
            return HttpResponseRedirect('/success/url/')
    else:
        form = ModelFormWithFileField()
    return render(request, 'create_file.html', {'form': form})
        
        
        