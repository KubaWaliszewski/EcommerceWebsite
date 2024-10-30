from django.shortcuts import redirect
from django.contrib import messages
from functools import wraps
from django.urls import reverse
from django.contrib.auth.decorators import login_required


def admin_only(view_func):
    @login_required
    def wrapper_function(request, *args, **kwargs):
        group = request.user.groups.first().name if request.user.groups.exists() else None

        if group == 'Client' or group == None:
            return redirect('home')

        if group == 'Agent' or group == 'Manager':
            return view_func(request, *args, **kwargs)
        
    return wrapper_function


def check_group(allowed_groups=[], redirect_url=None):
    def decorator(view_func):
        @wraps(view_func)
        @login_required  
        def wrapper_func(request, *args, **kwargs):
            if not set(allowed_groups).intersection(request.user.groups.values_list('name', flat=True)): 
                messages.error(request, "You don't have access to this function.")
                
                target_url = reverse(redirect_url) if redirect_url else request.META.get('HTTP_REFERER', '/')
                
                return redirect(target_url)
            
            return view_func(request, *args, **kwargs)
        
        return wrapper_func
    return decorator
