from django.shortcuts import render
from .models import Product, HashTag, Category


def main_view(request):
    if request.method == 'GET':
        return render(request, 'layouts/index.html')


def products_view(request):
    if request.method == 'GET':
        products = Product.objects.all()
        context = {
            "products": products,
        }
        return render(request, 'products/products.html', context=context)


def hashtags_view(request):
    if request.method == 'GET':
        hashtags = HashTag.objects.all()
        context = {
            "hashtags": hashtags,
        }
        return render(request, 'hashtags/hashtags.html', context=context)


def categories_view(request):
    categories = Category.objects.all()
    context = {
        "categories": categories,
    }
    return render(request, 'categories/categories.html', context=context)