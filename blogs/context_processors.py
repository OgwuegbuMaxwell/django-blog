

from .models import Category


def get_categories(request):
    categories = Category.objects.all()
    #print(categories)  # Print categories for debugging
    return dict(categories = categories)


