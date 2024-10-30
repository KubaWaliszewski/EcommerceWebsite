from django.contrib import admin
from django.urls import path, include

from django.conf import settings 
from django.conf.urls.static import static 


urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin-panel/', include('admin_panel.urls')),
    path('order/', include('orders.urls')),
    path('payments/', include('payments.urls')),
    path('paypal-ipn/', include('paypal.standard.ipn.urls')),
    path('', include('cart.urls')),
    path('my-account/', include('client.urls')),
    path('', include('core.urls')),
    path('', include('account.urls')),
    path('', include('chat.urls', namespace='chat')),
    path('', include('shop.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)