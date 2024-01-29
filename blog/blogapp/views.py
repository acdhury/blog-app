from django.shortcuts import render,redirect, Http404
from .models import *  
from .forms import BlogForm


def index(request):
    return render(request, "blogapp/index.html")


# All blogs made will be shown here
def blogs(request):
    blog_list = Blogs.objects.all()  
    return render(request, "blogapp/blogs.html", {'blogs': blog_list})  # Pass the queryset to the template context


# Will be redirected to a form where one could add a new blog 
def add_blog(request):
    if request.method == "POST":
        form = BlogForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("blogs")
    else:
        form = BlogForm()
    
    return render(request, "blogapp/add_blog.html", {"form": form})



#certain blog will be deleted after clicking on the button
def delete_blog(request, blog_id):
    try:
        blog = Blogs.objects.get(pk=blog_id)
    except Blogs.DoesNotExist:
        raise Http404("Blog does not exist")

    blog.delete()
    
    return redirect('blogs') 



# Will be able to edit the existing blog
def update_blog(request, id):
    blog = Blogs.objects.get(pk=id)
    form = BlogForm(request.POST or None, instance=blog)
    if form.is_valid():
        form.save()
        return redirect("blogs")
    return render(request, "blogapp/update.html", {
        "blog":blog,
        "form":form
    })

