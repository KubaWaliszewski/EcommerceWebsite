import json

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.contrib.auth.models import Group


from .models import Room
from core.models import SiteConfiguration
from account.models import CustomUser
from core.decorators import admin_only, check_group


from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
@require_POST
def create_room(request, uuid):
    name = request.POST.get('name', '')
    url = request.POST.get('url', '')

    Room.objects.create(uuid=uuid, client=name, url=url)

    return JsonResponse({'message': 'Room created successfully'})


@admin_only
def admin(request):
    rooms = Room.objects.all()
    config = SiteConfiguration.objects.first()

    return render(request, 'chat/admin.html', {
        'rooms': rooms,
        'show_chat': config.show_chat,
    })


@admin_only
def room(request, uuid):
    room = Room.objects.get(uuid=uuid)

    if room.status == Room.WAITING:
        room.status = Room.ACTIVE
        room.agent = request.user
        room.save()

    return render(request, 'chat/room.html', {
        'room': room,
    })


@admin_only
@check_group(allowed_groups=['Agent'])
def delete_room(request, uuid):

    if request.user.has_perm('room.delete_room'):
        room = Room.objects.get(uuid=uuid)
        room.delete()
        messages.success(request, 'The room was deleted!')
        
        return redirect('/chat-admin/')

    else:
        messages.error(request, 'You don\'t have access to delete rooms!')

        return redirect('/chat-admin/')


@admin_only
@check_group(allowed_groups=['Agent'])
def user_detail(request, uuid):
    user = CustomUser.objects.get(pk=uuid)
    rooms = user.rooms.all()

    return render(request, 'chat/user_detail.html', {
        'user': user, 
        'rooms': rooms,
    })


    

