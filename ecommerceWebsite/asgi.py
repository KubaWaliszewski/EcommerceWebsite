import os
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommerceWebsite.settings')

# Import Channels po ustawieniu Django settings
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from chat import routing

application = ProtocolTypeRouter(
    {
        'http': get_asgi_application(),  # Przesunięte do środka ProtocolTypeRouter
        'websocket': AllowedHostsOriginValidator(
            AuthMiddlewareStack(
                URLRouter(routing.websocket_urlpatterns)
            )
        ),
    }
)