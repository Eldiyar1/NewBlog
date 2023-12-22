from django.db.models import Q
from django.shortcuts import render, redirect

from blog import settings
from .forms import ProductCreateForm, ProductCreateForm2, CommentCreateForm, CategoryCreateForm
from .models import Product, HashTag, Category, Comment


def main_view(request):
    if request.method == 'GET':
        return render(request, 'layouts/index.html')


def products_view(request):
    if request.method == 'GET':
        print(request.user)
        products = Product.objects.all()
        search = request.GET.get('search')
        order = request.GET.get('order')

        if search:
            # products = products.filter(title__icontains=search) | products.filter(content__icontains=search)
            products = products.filter(
                Q(title__icontains=search) |
                Q(content__icontains=search)
            )

        if order == 'title':
            products = products.order_by('title')
        elif order == '-title':
            products = products.order_by('-title')
        elif order == 'created_at':
            products = products.order_by('created_at')
        elif order == '-created_at':
            products = products.order_by('-created_at')

        max_page = products.__len__() / settings.PAGE_SIZE

        if round(max_page) < max_page:
            max_page = round(max_page) + 1
        else:
            max_page = round(max_page)

        page = int(request.GET.get('page', 1))

        start = (page - 1) * settings.PAGE_SIZE
        end = page * settings.PAGE_SIZE

        products = products[start:end]
        context = {
            "products": products,
            "pages": range(1, max_page + 1)
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
            return redirect(f'/product/{product_id}/')
        context = {
            'form': form,
        }
        return render(request, 'products/product_detail.html', context)


def product_update_view(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        return render(request, 'errors/404.html')
    if request.method == 'GET':
        context = {
            "form": ProductCreateForm2(instance=product)
        }
        return render(request, 'products/product_update.html', context)
    elif request.method == 'POST':
        form = ProductCreateForm2(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect(f'/products/{product.id}/')
        return render(request, 'products/product_update.html', {"form": form})


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
