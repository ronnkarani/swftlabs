from django.contrib import admin
from .models import Project, BlogPost, SocialLink, Hero, About, Testimonial, Service, OurStory, WhyChooseUs, Category

@admin.register(Hero)
class HeroAdmin(admin.ModelAdmin):
    list_display = ('name', 'greeting', 'subtitle')

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('title',)

@admin.register(OurStory)
class OurStoryAdmin(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(WhyChooseUs)
class WhyChooseUsAdmin(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("title", "subtitle")
    search_fields = ("title", "subtitle", "description")

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('name', 'role', 'featured')
    list_filter = ('featured',)

@admin.register(SocialLink)
class SocialLinkAdmin(admin.ModelAdmin):
    list_display = ("platform", "url")


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ("title", "category", "created_at")
    list_filter = ("category",)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}  # auto-fill slug from name
    list_display = ("name", "slug")

admin.site.register(Project)
