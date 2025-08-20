# views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Project, BlogPost, Comment, SocialLink, Hero, About, Testimonial, Service, OurStory, WhyChooseUs
from django.core.paginator import Paginator
from django.contrib.auth.forms import UserCreationForm
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings

def home(request):
    hero = Hero.objects.first()  
    about = About.objects.all()  
    our_story = OurStory.objects.first()
    why_choose = WhyChooseUs.objects.first()
    testimonials = Testimonial.objects.all()
    social_links = SocialLink.objects.all()
    services = Service.objects.all()
    projects = Project.objects.all().order_by('-created_at')[:4]
    blogs = BlogPost.objects.all().order_by('-created_at')[:4]
    return render(request, 'home.html', {
        'hero': hero,
        'about_sections': about,
        'our_story': our_story,
        'why_choose': why_choose,
        "services": services,
        'testimonials': testimonials,
        "social_links": social_links,
        'projects': projects,
        'blog_posts': blogs
    })

def blog(request):
    posts = BlogPost.objects.all().order_by('-created_at')
    paginator = Paginator(posts, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'blog.html', {'blog_posts': page_obj})

def blog_detail(request, slug):
    blog = get_object_or_404(BlogPost, slug=slug)
    blog.views += 1
    blog.save()

    if request.method == "POST":
        if "like" in request.POST:
            blog.likes += 1
            blog.save()
            return redirect('blog_detail', slug=slug)

        elif "comment" in request.POST:
            name = request.POST.get("name")
            content = request.POST.get("content")
            if name and content:
                Comment.objects.create(name=name, content=content, blog=blog)
            return redirect('blog_detail', slug=slug)

    comments = blog.comments.all()
    return render(request, 'blog_details.html', {
        'post': blog,
        'comments': comments
    })

def projects(request):
    projects = Project.objects.all().order_by('-created_at')
    paginator = Paginator(projects, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'projects.html', {'projects': page_obj})

def project_detail(request, slug):
    project = get_object_or_404(Project, slug=slug)
    project.views += 1
    project.save()

    if request.method == "POST":
        if "like" in request.POST:
            project.likes += 1
            project.save()
            return redirect('project_details', slug=slug)

        elif "comment" in request.POST:
            name = request.POST.get("name")
            content = request.POST.get("content")
            if name and content:
                Comment.objects.create(name=name, content=content, project=project)
            return redirect('project_details', slug=slug)

    comments = project.comments.all()
    return render(request, 'project_details.html', {
        'project': project,
        'comments': comments
    })


def signup_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


def contact(request):
    social_links = SocialLink.objects.all()
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        subject = f"New Contact Form Submission from {name}"
        body = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"

        try:
            send_mail(
                subject,
                body,
                settings.EMAIL_HOST_USER,  # sender
                [settings.EMAIL_HOST_USER],  # receiver (your email)
                fail_silently=False,
            )
            messages.success(request, "✅ Your message has been sent successfully!")
        except Exception as e:
            messages.error(request, f"❌ Error sending message: {e}")

        return redirect("contact")

    return render(request, "contact.html",{"social_links": social_links,})