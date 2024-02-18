from django.contrib import admin
from .models import About, Category, Comment, SocialLink
from .models import Blog
# Register your models here.


class BlogAdmin(admin.ModelAdmin):
    # Handle populating slug dynamically
    # As we write the blog title, the slug should be populated
    prepopulated_fields = {'slug': ('title',)}
    # List all the fields you want to be shown on the admin
    list_display = ('title', 'category', 'author', 'status', 'is_featured')
    # Add search functionality
    # to search foreign key like category, we use category__category_name
    # it means we are not searching directly the category filed in the Blog model,
    # we are going to the category model, and seach the category_name field
    # so we are pointing to Category Model >> category_name field.
    search_fields = ('id', 'title', 'category__category_name', 'status')
    # If you want to be able to edit a particular field directly on the listed rows
    list_editable = ('is_featured',)





class AboutAdmin(admin.ModelAdmin):
    def has_add_permission():
        count = About.objects.all().count()
        if count == 0:
            return True
        return False



admin.site.register(Category)
admin.site.register(Blog, BlogAdmin)
# admin.site.register(About, AboutAdmin)
admin.site.register(SocialLink)
admin.site.register(Comment)
