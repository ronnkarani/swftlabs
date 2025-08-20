# models.py
from django.db import models
from django.utils.text import slugify
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.text import Truncator


# Hero Section
class Hero(models.Model):
    greeting =models.CharField(max_length=255, default="Hi 👋, welcome to")
    name = models.CharField(max_length=100)
    subtitle = RichTextUploadingField(max_length=500, blank=True)
    image = models.ImageField(upload_to='hero/', blank=True, null=True)

    def __str__(self):
        return self.name

# About Section
class About(models.Model):
    title = models.CharField(max_length=255)
    content = RichTextUploadingField()

    def __str__(self):
        return self.title
    

class OurStory(models.Model):
    title = models.CharField(max_length=255, default="Our Story")
    content = RichTextUploadingField()

    def __str__(self):
        return self.title


class WhyChooseUs(models.Model):
    title = models.CharField(max_length=255, default="Why Choose Us")
    points = RichTextUploadingField(help_text="Use bullet points or HTML list here")

    def __str__(self):
        return self.title

class Service(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=255, blank=True, null=True)
    description = RichTextUploadingField()
    icon = models.CharField(max_length=50, help_text="Add emoji or icon code e.g., ⭐️, 💼, 🎖️")

    def __str__(self):
        return self.title

class SocialLink(models.Model):
    PLATFORM_CHOICES = [
        ("facebook", "Facebook"),
        ("twitter", "Twitter"),
        ("linkedin", "LinkedIn"),
        ("github", "GitHub"),
        ("instagram", "Instagram"),
        ("youtube", "YouTube"),
    ]

    platform = models.CharField(max_length=50, choices=PLATFORM_CHOICES)
    url = models.URLField()

    def __str__(self):
        return f"{self.get_platform_display()} - {self.url}"
class Project(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    description = RichTextUploadingField()
    image = models.ImageField(upload_to='projects/')
    technologies = models.TextField()
    repo_url = models.URLField(blank=True, null=True)
    live_url = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    views = models.PositiveIntegerField(default=0)
    likes = models.PositiveIntegerField(default=0)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def tech_list(self):
        return [tech.strip() for tech in self.technologies.split(',')]
    
    def __str__(self):
        return self.title  

    def comment_count(self):
        return self.comments.count()

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    excerpt = models.TextField()
    image = models.ImageField(upload_to='blogs/')
    content = RichTextUploadingField()    
    author = models.CharField(max_length=100, default="Ronny")
    created_at = models.DateField(auto_now_add=True)
    views = models.PositiveIntegerField(default=0)
    likes = models.PositiveIntegerField(default=0)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
        
    def __str__(self):
        return self.title
    
    def comment_count(self):
        return self.comments.count()

class Comment(models.Model):
    name = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


    # This will work for either a project or blog
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True, blank=True, related_name="comments")
    blog = models.ForeignKey(BlogPost, on_delete=models.CASCADE, null=True, blank=True, related_name="comments")

    def __str__(self):
        return f"Comment by {self.name}"
    
# Testimonial Section
class Testimonial(models.Model):
    name = RichTextUploadingField(max_length=300)
    role = RichTextUploadingField(max_length=300, blank=True)
    content = RichTextUploadingField()
    image = models.ImageField(upload_to='testimonials/', blank=True, null=True)
    featured = models.BooleanField(default=False)

    def __str__(self):
        return self.name