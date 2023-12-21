from django.shortcuts import render, redirect

from .forms import ProductCreateForm, ProductCreateForm2, CommentCreateForm, CategoryCreateForm
from .models import Product, HashTag, Category, Comment


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
            "product": product,
            'form': CommentCreateForm()
        }
        return render(request, 'products/product_detail.html', context)
    elif request.method == 'POST':
        form = CommentCreateForm(request.POST, request.FILES)
        if form.is_valid():
            Comment.objects.create(product_id=product_id, **form.cleaned_data)
            return redirect('product_detail', product_id=product_id)
        context = {
            'form': form,
        }
        return render(request, 'products/product_detail.html', context)


def product_create(request):
    if request.method == 'GET':
        context = {
            "form": ProductCreateForm
        }
        return render(request, 'products/products.create.html', context)
    elif request.method == 'POST':
        form = ProductCreateForm2(request.POST, request.FILES)
        if form.is_valid():
            Product.objects.create(**form.cleaned_data)
            return redirect("/products/")
        context = {
            "form": form
        }
        return render(request, 'products/products.create.html', context)


def categories_view(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        context = {
            "categories": categories,
        }
        return render(request, 'categories/categories.html', context=context)


def category_create_view(request):
    if request.method == 'GET':
        context = {
            "categories": CategoryCreateForm(),
        }
        return render(request, 'categories/categories_create.html', context=context)

    elif request.method == 'POST':
        form = CategoryCreateForm(request.POST)
        if form.is_valid():
            Category.objects.create(**form.cleaned_data)
            return redirect('/categories/')
        context = {
            "form": form
        }
        return render(request, 'categories/categories_create.html', context=context)


def hashtags_view(request):
    if request.method == 'GET':
        hashtags = HashTag.objects.all()
        context = {
            "hashtags": hashtags,
        }
        return render(request, 'hashtags/hashtags.html', context=context)
