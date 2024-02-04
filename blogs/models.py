from django.db import models
# Import User
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


# Create your models here.


class Category(models.Model):
    category_name = models.CharField(max_length=50, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    # To tell django the correct plural spelling of Category
    # If not django will write it as categorys in the admin panel
    class Meta:
       verbose_name_plural =  'categories'
    
    # Whenever you write any member function inside the class,
    # you should always pass self as a parameter.
    # Here, self is nothing but the Category model itself.
    # This is setting the string representation of this particular model
    def __str__(self):
        return self.category_name



# Making drop down
STATUS_CHOICES =(
    ("Draft", "Draft"),
    ("Published", "Published")
)

class Blog(models.Model):
    title = models.CharField(max_length=100)
    # A slog is the part of a URL that identifies a particular page on a website
    # In fact, It's a title itself with the hyphen instead of the space in between words
    # The slug represent the title, and it's a part of the URL part, seperated with hyphens
    # Slug is very uuseful when it comes to SEO
    slug = models.SlugField(max_length=150, unique=True, blank=True)
    # When you delete a specific category, then the blog post associated with that
    # particular category should also be deleted.
    # That means we will delete all those posts of the category associated with it is deleted
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    # If the user is deleted, this particular blog post should be deleted
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # This image will be uploaded to:
    # uploads/the year the blog was created/the month/ the day
    featured_image = models.ImageField(upload_to='uploads/%Y/%m/%d')
    short_description = models.TextField(max_length=500)
    blog_body = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="Draft")
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    # Code to insure blog_body does not exceed 1000
    def calculate_word_count(self):
        return len(self.blog_body.split())
    
    def save(self, *args, **kwargs):
        # Ensure that the word count does not exceed 1000
        if self.calculate_word_count() > 1000:
            raise ValidationError("Word cannot Exceed 1000")
        
        super().save(*args, **kwargs)
    
    # Remember to install pillow since we are working with image
    # pip install Pillow
    # Make sure the virtual environment is activated when installing the pillow
    

    # Whenever you write any member function inside the class,
    # you should always pass self as a parameter.
    # Here, self is nothing but the Category model itself.
    # This is setting the string representation of this particular model
    def __str__(self):
        return self.title
    
    # Don't forget to make migration
    # python manage.py makemigrations
    # python manage.py migrate
    
    # also don't forget to register the model to the admin.py
    # admin.site.register(Blog)
    


