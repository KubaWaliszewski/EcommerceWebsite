from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import OrderItem, Order
from payments.models import Payment
from cart.models import Cart
from .forms import OrderCreateForm
from client.models import Address


@login_required
def order_create(request):
    cart_id = request.session.get('cart_id')
    if not cart_id:
        return redirect('cart:cart_detail')
    
    cart = get_object_or_404(Cart, id=cart_id)

    if not cart or not cart.items.exists():
        return redirect('cart:cart_detail') 

    user_address = None
    if request.user.is_authenticated:
        user_address = Address.objects.filter(user=request.user, default=True).first()

    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        payment_method = request.POST.get('payment_method')
        if form.is_valid():
            order = form.save(commit=False)
            order.is_paid = False

            if request.user.is_authenticated:
                order.user = request.user   
                order.email = request.user.email

            order.save()


            insufficient_stock = False

            for item in cart.items.all():
                product = item.product

                if item.quantity > product.stock:
                    insufficient_stock = True
                    
                    messages.error(
                        request, 
                        f"Insufficient quantity of {product.name}. Available: {product.stock}, ordered: {item.quantity}."
                    )
                    break  

            if insufficient_stock:
                order.delete() 
                return redirect('cart:cart_detail')

            for item in cart.items.all():
                OrderItem.objects.create(
                    order=order,
                    product=item.product,
                    price=item.product.price,
                    quantity=item.quantity,
                )

            product = item.product
            product.stock -= item.quantity

            if product.stock <= 0:
                product.is_available = False
            
            product.save()


            cart.delete()
            del request.session['cart_id']
            
            if payment_method == 'paypal':
                return redirect(reverse('payments:checkout', args=[order.id]))
            elif payment_method == 'bank_transfer':
                return redirect(reverse('payments:bank-transfer-payment', args=[order.id]))

    initial_data = {}
    
    if user_address:
        initial_data = {
            'full_name': f"{user_address.first_name} {user_address.last_name}",
            'address': user_address.address,
            'address2': user_address.address2,
            'city': user_address.city,
            'zip_code': user_address.zip_code,
            'country': user_address.country,
            'phone': user_address.phone,
        }
    form = OrderCreateForm(initial=initial_data)

    return render(request, 'orders/order_create.html', {
        'OrderCreateForm': form,
        'cart': cart,
    })

