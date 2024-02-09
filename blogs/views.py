from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from .models import Blog, Category
# the Q object allows you to make the complex lookups such as 'or' operations
from django.db.models import Q

# Create your views here.

def posts_by_category(request, category_id):
    # Fetch the posts that belongs to the category with the id category_id
    posts = Blog.objects.filter(status='Published', category = category_id)
    
    # Fetch the category name
    
    # If we don't want to show the user an error page, but redirect the user to
    # home page when the resource is not available
    # try:
    #     category = Category.objects.get(pk=category_id)
    # except:
    #     # redirect the user to homepage or perform any other custom action
    #     return redirect('home')
    
    # The correct way to handle request if the resorce doest not exist
    # In this case, if the category does not exist.
    # Use get_object_or_404() when you want to show 404 error page
    category = get_object_or_404(Category, pk=category_id)
    

    
    context = {
        'posts': posts,
        'category': category,
    }
    print(posts)
    return render(request, 'posts_by_category.html', context)


def blogs(request, slug):
    single_blog = get_object_or_404(Blog, slug=slug, status='Published')
    context = {
        'single_blog': single_blog,
    }
    return render(request, 'blogs.html', context)



def search(request):
    keyword = request.GET.get('keyword')
    print('keyword==>', keyword)
    
    blogs = Blog.objects.filter(Q(title__icontains=keyword) | Q(short_description__icontains=keyword) | Q(blog_body__icontains=keyword) , status='Published') # The comma means 'and'
    # print(blogs)
    context = {
        'blogs': blogs,
        'keyword':keyword
    }
    return render(request, 'search.html', context)
    




