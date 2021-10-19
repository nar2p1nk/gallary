from django import forms

from gallary.models import Profiles

class PostForm(forms.Form):
    Ftitle = forms.CharField()
    Fcreated_by = forms.CharField(label='Created by: ',max_length=35)
    Fimg = forms.ImageField(label='image')

class PostForm2(forms.ModelForm):
    class Meta:
        model = Profiles
        fields = ['title','created_by','img']
