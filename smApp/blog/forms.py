from django import forms
from .models import Post,comment,Profile
from django.contrib.auth.models import User

class PostFeed(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('title','text','image')

class CommentForm(forms.ModelForm):
	class Meta:
		model = comment
		fields = ('text',)

class UserForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ('first_name','last_name','email')

class ProfileForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ('profile_pic','location','birth_date','bio')