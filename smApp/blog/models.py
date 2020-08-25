from django.db import models
from django.conf import settings
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User


class Post(models.Model):
	author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	title = models.CharField(max_length=200)
	text = models.TextField()
	image = models.ImageField(upload_to='images/', blank=True)
	published_date = models.DateTimeField(blank=True, null=True)

    
	def publish(self):
		self.published_date = timezone.now()
		self.save()
	def __str__(self):
		return self.title

class comment(models.Model):
	post = models.ForeignKey('blog.Post',on_delete = models.CASCADE, related_name = 'comments')
	author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	text = models.TextField()
	created_date = models.DateTimeField(default = timezone.now())
	approved = models.BooleanField(default = False)


	def approve_comment(self):
		self.approved = True
		self.save()

	def __str__(self):
		return self.text

class Profile(models.Model):
	user = models.OneToOneField(User,on_delete=models.CASCADE)
	bio = models.TextField(blank=True)
	location = models.CharField(max_length=50, blank=True)
	birth_date = models.DateTimeField(null=True, blank=True) 
	profile_pic = models.ImageField(upload_to="images/profile", blank=True)


@receiver(post_save, sender=User)
def create_profile(sender, instance, created,**kwargs):
	if created:
		Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
	instance.profile.save()
