from django.contrib import admin
from .models import Newsletter
from .forms import NewsletterForm

# Register your models here.

class NewsletterAdmin(admin.ModelAdmin):
	list_display = ["email", "timestamp", "updated"]
	form = NewsletterForm


admin.site.register(Newsletter, NewsletterAdmin)