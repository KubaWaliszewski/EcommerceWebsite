from django.shortcuts import render, redirect

from core.decorators import check_group
from .models import SiteConfiguration
from shop.models import Product, Category

def home(request):
    newest_products = Product.objects.filter(is_available=True).order_by('-created_at')[:8]
     
    try:
        electronics_category = Category.objects.get(slug='electronics')  
        tools_category = Category.objects.get(slug='tools')  
    except Category.DoesNotExist:
        electronics_category = None
        tools_category = None

    electronics_products = Product.objects.filter(category=electronics_category, is_available=True)[:8] if electronics_category else []

    tools_products = Product.objects.filter(category=tools_category, is_available=True)[:8] if tools_category else []

    return render(request, 'core/home.html', {
        'products': newest_products,
        'electronics_products': electronics_products,
        'tools_products': tools_products,
    })


def contact(request):
    config, _ = SiteConfiguration.objects.get_or_create(pk=1)

    return render(request, 'core/contact.html', {
        'show_chat': config.show_chat,
    })


@check_group(allowed_groups=['Agent',], redirect_url='chat:admin')
def toggle_chat(request):

    config, _ = SiteConfiguration.objects.get_or_create(pk=1) 
    config.show_chat = not config.show_chat
    config.save()

    return redirect('chat:admin')
#
#
#
#
#
#
#
#