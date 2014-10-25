from django.shortcuts import render, get_object_or_404
from gallery.models import Category, Image


def gallery(request):
    categories = Category.objects.all().order_by('name')
    images = Image.objects.all()
    return render(request, 'gallery/gallery.html', {'section': 'gallery',
                                                    'cat_selection': 'all',
                                                    'categories': categories,
                                                    'images': images})


def gallery_category(request, category_id):
    cat = get_object_or_404(Category, pk=category_id)
    categories = Category.objects.all().order_by('name')
    images = Image.objects.filter(category_id=cat.id)
    return render(request, 'gallery/gallery.html', {'images': images,
                                                    'categories': categories,
                                                    'section': 'gallery',
                                                    'cat': cat.id})