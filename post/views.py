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


def product_detail_view(request, product_id):
    if request.method == 'GET':
        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return render(request, 'errors/404.html')
        context = {
            "product": product
        }
        return render(request, 'products/product_detail.html', context)


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
