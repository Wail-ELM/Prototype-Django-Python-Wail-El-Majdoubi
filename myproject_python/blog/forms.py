from django import forms
from .models import Article
from django.contrib.auth.forms import UserCreationForm

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content']

class CustomUserCreationForm(UserCreationForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ('email',)

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("The two password fields didn't match.")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1']) 
        if commit:
            user.save()
        return user