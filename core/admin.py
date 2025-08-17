from django.contrib import admin
from .models import Project, BlogPost, SocialLink

@admin.register(SocialLink)
class SocialLinkAdmin(admin.ModelAdmin):
    list_display = ("platform", "url")

admin.site.register(Project)
admin.site.register(BlogPost)
