from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

class Blog(models.Model):
	Author = 			models.ForeignKey(User)
	BlogTitle = 		models.CharField(blank=False, null=False, max_length=140, unique=True)
	BlogDescription = 	models.CharField(blank=True, null=True, max_length=140)
	Content = 			models.TextField(blank=False, null=False)
	NumComments = 		models.IntegerField(null=True, blank=True)
	Publish = 			models.BooleanField(default=True)
	Created = 			models.DateTimeField(auto_now_add=True, auto_now=False)
	Updated = 			models.DateTimeField(auto_now_add=False, auto_now=True)
	BlogSlug = 			models.SlugField(max_length=140, blank=True)

	def __str__(self):
		return self.BlogTitle

	class Meta:
		ordering = ['-Created']

	def get_absolute_url(self):
		return reverse('blogengine.views.getpost', args=[self.BlogSlug])