from django.shortcuts import render, get_object_or_404

from main.models import Product, Category


def home(request):
    category = Category.objects.all()
    return render(request, 'main/index.html', {'navcategory': category})


def about(request):
    category = Category.objects.all()
    return render(request, 'main/about.html', {'navcategory': category})


def contact(request):
    category = Category.objects.all()
    return render(request, 'main/contact.html', {'navcategory': category})


def products(request, category_slug):
    categories = get_object_or_404(Category, slug=category_slug)
    data = {
        'navcategory': Category.objects.filter(status=True, parent=None),
        "category": categories,
        "products": Product.objects.filter(category=categories, status=True),
        "subcategories": Category.objects.filter(status=True).exclude(parent=None)
    }

    return render(request, 'main/products.html', data)
