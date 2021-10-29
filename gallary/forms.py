from django import forms
from gallary.models import Profiles

class PostForm(forms.Form):
    img = forms.ImageField(label='image')
    title = forms.CharField()
    created_by = forms.CharField(label='Created by: ',max_length=35)

class PostForm2(forms.ModelForm):
    class Meta:
        model = Profiles
        fields = '__all__'
        widgets = {
            'img': forms.FileInput(attrs={'class':'input'}),
            'title': forms.TextInput(attrs={'placeholder': 'enter title','class':'textInput title'}),
            'created_by': forms.TextInput(attrs={'placeholder': 'enter name of artist','class':'textInput artist'})
        }
