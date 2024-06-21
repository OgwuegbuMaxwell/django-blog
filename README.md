![Screenshot (140)](https://github.com/OgwuegbuMaxwell/django-blog/assets/53094485/14f9b3a5-5b07-4742-9436-e88a39412624)


![Screenshot (141)](https://github.com/OgwuegbuMaxwell/django-blog/assets/53094485/1965a7d2-98f5-4c98-ae44-0e51a4f6060a)


![Screenshot (142)](https://github.com/OgwuegbuMaxwell/django-blog/assets/53094485/f12b6138-7da8-4748-880b-73b3fa48bb85)


![Screenshot (143)](https://github.com/OgwuegbuMaxwell/django-blog/assets/53094485/72213dea-1eca-4fd9-b9f5-24a0ed3ee56b)



# Django Blog

## Introduction

This repository contains the code for a simple blog developed using the Django framework. The blog supports categories, customizable posts, user comments, and social links integration. It's designed to be a straightforward example of a Django application implementing basic CRUD operations and several Django models.

## Features

- **Blog Posts**: Create, update, delete, and read blog posts with images, categorization, and featured options.
- **Categories**: Organize posts into categories.
- **Comments**: Users can comment on blog posts.
- **Social Links**: Add social media links to the blog.
- **User Authentication**: Manage user sign-up and login.

## Models

- `Category`: Represents different categories under which blog posts can be grouped.
- `Blog`: Represents the blog post containing a title, slug, content, etc.
- `Comment`: Represents comments made on blog posts.
- `SocialLink`: Stores social media platform names and URLs.
- `About`: Provides information about the blog or the organization.

## Installation

To get this project up and running on your local machine, follow these steps:

1. Clone the repository:
git clone [](https://github.com/your-username/django-blog.git)

2. Change into the project directory:
`cd django-blog`

3. Install the required packages:
`pip install -r requirements.txt`

4. Apply the migrations:

`python manage.py makemigrations`
`python manage.py migrate`

5. Start the development server:
`python manage.py runserver
`

6. Open a browser and go to `http://127.0.0.1:8000` to view the app.

## Configuration

Make sure to update the `settings.py` file with your settings, especially the `SECRET_KEY`, database configurations, and `DEBUG` settings.

## Dependencies

- Django
- Pillow (for image upload functionality)

## Contributions

Contributions are welcome! Please fork the repository and open a pull request with your features or fixes.



