from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from .models import Blog, Category

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
