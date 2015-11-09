from django.db import models

# Create your models here.
class Newsletter(models.Model):
	email = models.EmailField()
	full_name = models.CharField(default='', blank=True, null=True, max_length=120)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __unicode__(self):
		return self.email