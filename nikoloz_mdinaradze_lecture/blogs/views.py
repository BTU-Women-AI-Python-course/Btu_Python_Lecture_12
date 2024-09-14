from django.shortcuts import render

from blogs.models import Blog


# Create your views here.
def blogs_list(request):
    all_blogs = Blog.objects.all()
    context = {
        'blogs': all_blogs
    }
    return render(request, 'blogs/blogs_list.html', context=context)


def blogs_detail(request, blog_id):
    blog = Blog.objects.get(pk=blog_id)
    context = {
        'blog': blog
    }
    return render(request, 'blogs/blogs_detail.html', context=context)
