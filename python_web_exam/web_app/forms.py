from django import forms
import re
from python_web_exam.web_app.models import Profile, Album


class CreateProfile(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('user_name', 'email', 'age')
        widgets = {
            'user_name': forms.TextInput(attrs={
                'placeholder': 'Username'
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'Email'
            }),
            'age': forms.TextInput(attrs={
                'placeholder': 'Age'
            }),
        }

    def clean(self):
        username = self.cleaned_data.get('user_name')
        if not re.match(r'^[A-Za-z0-9_]+$', username):
            raise forms.ValidationError('Ensure this value contains only letters, numbers, and underscore.')


class CreateAlbum(forms.ModelForm):
    class Meta:
        model = Album
        fields = ('name', 'artist', 'genre', 'description', 'image', 'price')
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Album Name'
            }),
            'artist': forms.TextInput(attrs={
                'placeholder': 'Artist'
            }),
            'description': forms.Textarea(attrs={
                'placeholder': 'Description'
            }),
            'image': forms.TextInput(attrs={
                'placeholder': 'Image URL'
            }),
            'price': forms.TextInput(attrs={
                'placeholder': 'Price'
            }),
        }


class EditAlbum(forms.ModelForm):
    class Meta:
        model = Album
        fields = '__all__'


class DeleteAlbum(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            field.required = False

    def save(self, commit=True):
        self.instance.delete()
        return self.instance

    class Meta:
        model = Album
        fields = '__all__'


class DeleteProfile(forms.ModelForm):
    def save(self, commit=True):
        self.instance.delete()
        Album.objects.all().delete()
        return self.instance

    class Meta(forms.ModelForm):
        model = Profile
        fields = ()
