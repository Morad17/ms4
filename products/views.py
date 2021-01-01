from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower

from .models import Product, Category, Seasonal, Specials
from .forms import ProductForm

def all_products(request):
    """The view to show all products"""

    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "Search criteria not found!")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)
    current_sorting = f'{sort}_{direction}'


    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/products.html', context)


@login_required
def add_product(request):
    """Adds a product to the store"""
    if not request.user.is_superuser:
        messages.error(request, 'sorry, only store owners can do that')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to add product. Please ensure the form is valid.')
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)

@login_required
def edit_product(request, product_id):
    """Edit a product in the store"""
    if not request.user.is_superuser:
        messages.error(request, 'sorry, only store owners can do that')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to update product. Please ensure the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/add_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)

@login_required
def delete_product(request, product_id):
    """Delete a Product from the store"""
    if not request.user.is_superuser:
        messages.error(request, 'sorry, only store owners can do that')
        return redirect(reverse('home'))
        
    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('products'))

def seasonal_products(request):
    """Populate Seasonal products"""

    seasonal = Seasonal.objects.all()
    context = {
            'seasonal': seasonal,
        }

    return render(request, 'seasonal/hot_products.html', context)

def specials_products(request):
    """Populate Special Offer products """

    specials = Specials.objects.all()
    context = {
            'specials': specials,
        }

    return render(request, 'specials/hot_products.html', context)

def hot_products(request):
    """Populate Hot products Page"""

    products = Product.objects.filter(rating__gt=4)
    specials = Specials.objects.all()
    seasonal = Seasonal.objects.all()
    context = {
            'products': products,
            'seasonal': seasonal,
            'specials': specials,
        }

    return render(request, 'products/hot_products.html', context)



def product_detail(request, product_id):
    """The view to show individual product details"""
    product = get_object_or_404(Product, pk=product_id)
    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)

def specials_detail(request, product_id):
    """The view to show individual specials product details"""
    specials = get_object_or_404(Specials, pk=product_id)
    product = specials
    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)

def seasonal_detail(request, product_id):
    """The view to show individual seasional product details"""
    seasonal = get_object_or_404(Seasonal, pk=product_id)
    product = seasonal
    context = {
        'product': product,
    }
    return render(request, 'products/product_detail.html', context)