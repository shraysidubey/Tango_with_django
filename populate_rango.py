import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tango_with_django.settings')

import django
django.setup()

from rango.models import Category, Page


def populate():
    python_cat = add_cat('Python', 300, 64)

    add_page(cat=python_cat,
        views=300,
        title="Official Python Tutorial",
        url="http://docs.python.org/2/tutorial/")

    add_page(cat=python_cat,
        views=100,
        title="How to Think like a Computer Scientist",
        url="http://www.greenteapress.com/thinkpython/")

    add_page(cat=python_cat,
        views=150,
        title="Learn Python in 10 Minutes",
        url="http://www.korokithakis.net/tutorials/python/")

    django_cat = add_cat("Django", 100, 32)

    add_page(cat=django_cat,
        views=500,
        title="Official Django Tutorial",
        url="https://docs.djangoproject.com/en/1.5/intro/tutorial01/")

    add_page(cat=django_cat,
        views=10,
        title="Django Rocks",
        url="http://www.djangorocks.com/")

    add_page(cat=django_cat,
        views=840,
        title="How to Tango with Django",
        url="http://www.tangowithdjango.com/")

    frame_cat = add_cat("Other Frameworks", 220, 16)

    add_page(cat=frame_cat,
        views=1000,
        title="Bottle",
        url="http://bottlepy.org/docs/dev/")

    add_page(cat=frame_cat,
        views=30,
        title="Flask",
        url="http://flask.pocoo.org")

    # Print out what we have added to the user.
    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print "- {0} - {1}".format(str(c), str(p))

def add_page(cat,views, title, url):
    p = Page.objects.get_or_create(category=cat, title=title)[0]
    p.url=url
    p.views=views
    p.save()
    return p

def add_cat(name, views, likes):
    c = Category.objects.get_or_create(name=name)[0]
    c.views = views
    c.likes = likes
    c.save()
    return c

# Start execution here!
if __name__ == '__main__':
    print "Starting Rango population script..."
    populate()