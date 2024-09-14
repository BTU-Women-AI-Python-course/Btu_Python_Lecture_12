from django.shortcuts import render, get_object_or_404

from blogs.models import Blog


# Create your views here.
def blogs_list(request):
    all_blogs = Blog.objects.all()
    context = {
        'blogs': all_blogs
    }
    return render(request, 'blogs/blogs_list.html', context=context)


def blogs_detail(request, blog_id):
    try:
        blog = Blog.objects.get(id=blog_id)
    except Blog.DoesNotExist:
        return render(request, 'not_found_404.html')
    context = {
        'blog': blog
    }
    return render(request, 'blogs/blogs_detail.html', context=context)
