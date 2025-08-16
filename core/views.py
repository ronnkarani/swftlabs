# views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Project, BlogPost, Comment
from django.core.paginator import Paginator

def home(request):
    projects = Project.objects.all().order_by('-created_at')[:4]
    blogs = BlogPost.objects.all().order_by('-created_at')[:4]
    return render(request, 'home.html', {
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
    return render(request, "contact.html")