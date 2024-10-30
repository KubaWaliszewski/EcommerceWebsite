from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST
from django.http import JsonResponse
from django.contrib import messages

from shop.models import Product
from .models import Cart, CartItem



@require_POST
def cart_add(request, product_id):
    cart_id = request.session.get('cart_id')

    if not cart_id:
        cart = Cart.objects.create()
        request.session['cart_id'] = cart.id
    else:
        try:
            cart = Cart.objects.get(id=cart_id)
        except Cart.DoesNotExist:
            cart = Cart.objects.create()
            request.session['cart_id'] = cart.id

    product = get_object_or_404(Product, id=product_id)

    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)

   
    if not created:
        if cart_item.quantity + 1 > product.stock:
            response_data = {
                'success': False,
                'message': f"Insufficient stock of product {product.name}. Available: {product.stock}, in your cart: {cart_item.quantity}."
            }
            return JsonResponse(response_data)
        else:
            cart_item.quantity += 1  
    else:
        if product.stock < 1:
            response_data = {
                'success': False,
                'message': f"Insufficient stock of product {product.name}. Maximum quantity available: {product.stock}."
            }
            return JsonResponse(response_data)

    cart_item.save()  

    response_data = {
        'success': True,
        'message': f'Added {product.name} to cart'
    }

    return JsonResponse(response_data)


def cart_detail(request):
    cart_id = request.session.get('cart_id')
    cart = None

    if cart_id:
        cart = get_object_or_404(Cart, id=cart_id)

    if not cart or not cart.items.exists():
        cart = None

    return render(request, 'cart/cart.html', {
        'cart': cart,
    })


def cart_remove(request, product_id):
    cart_id = request.session.get('cart_id')
    cart = get_object_or_404(Cart, id=cart_id)
    item = get_object_or_404(CartItem, id=product_id, cart=cart)
    item.delete()

    return redirect('cart:cart_detail')


def change_quantity(request, product_id):
    cart_id = request.session.get('cart_id')
    if not cart_id:
        return redirect('cart:cart_detail')
    cart = get_object_or_404(Cart, id=cart_id)
    try:
        item = CartItem.objects.get(cart=cart, product_id=product_id)
    except CartItem.DoesNotExist:
        return redirect('cart:cart_detail')

    action = request.GET.get('action')

    if action:
        if action == 'increase':
            if item.quantity + 1 > item.product.stock:
                messages.error(
                    request,
                    f"Insufficient stock of product {item.product.name}. Maximum quantity available: {item.product.stock}."
                )
                return redirect('cart:cart_detail')
            item.quantity += 1
            
        elif action == 'decrease':
            if item.quantity > 1:
                item.quantity -= 1
                
            else:
                item.delete()  
                return redirect('cart:cart_detail')
            
            item.save()
        item.save()

        

    return redirect('cart:cart_detail')


