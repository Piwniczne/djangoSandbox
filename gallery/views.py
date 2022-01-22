from django.shortcuts import render
from .models import *
# Create your views here.

def getContextGalleryBase():
    context = {}
    context['nbar'] = "gallery"
    return context

def home(request):
    #looking inside of template directory
    categories = Category.objects.all()
    context = getContextGalleryBase()
    context['categories'] = categories
    for category in categories:
        imagesInCat = Image.objects.filter(category=category).order_by('-dataCreated')[0]
        category.image = imagesInCat

    return render(request, 'gallery/gallery.html', context)


#Function based view
def categoryPage(request, slug):
    context = getContextGalleryBase()
    try:
        categories = Category.objects.all()
        category = Category.objects.get(slug=slug)
        images = Image.objects.filter(category=category).order_by('-dataCreated')[:6] #last six
        context['images'] = images
        context['category'] = category
        context['categories'] = categories

        for img in images:
            img.shortDescription = img.description[:130]
    except:
        print('category display exception raised')

    return render(request, 'gallery/category.html', context)



#Function based view
def imageDetailPage(request, slugCategory, slugImage):
    context = getContextGalleryBase()
    try:
        category = Category.objects.get(slug=slugCategory)
        image = Image.objects.get(slug=slugImage)
        context['image'] = image
        context['category'] = category
        categories = Category.objects.all()
        context['categories'] = categories

    except:
        print('category display exception raised')

    return render(request, 'gallery/image.html', context)