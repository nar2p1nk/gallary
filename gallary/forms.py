from django import forms


class PostForm(forms.Form):
    title = forms.CharField(widget=forms.TextInput(attrs={'class' : 'title'}), max_length=80)
    created_by = forms.CharField(label='created by', max_length=35)
    img = forms.ImageField()

