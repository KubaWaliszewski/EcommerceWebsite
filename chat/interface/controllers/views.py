import json

from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.contrib import messages

from core.interface.decorators import admin_only, check_group
from chat.infrastructure.repositories.room_repository import RoomRepository
from chat.infrastructure.repositories.user_repository import UserRepository
from chat.infrastructure.repositories.site_configuration_repository import SiteConfigurationRepository
from chat.application.use_cases.get_admin_dashboard_data import GetAdminDashboardDataUseCase
from chat.application.use_cases.room_use_cases import (
    CreateRoomUseCase,
    DeleteRoomUseCase,
    GetOrUpdateRoomUseCase,
)


@require_POST
def create_room(request, uuid):
    name = request.POST.get('name', '')
    url = request.POST.get('url', '')

    room_repository = RoomRepository()
    create_room_use_case = CreateRoomUseCase(room_repository)

    create_room_use_case.execute(uuid, name, url)

    return JsonResponse({'message': 'Room created successfully'})


@admin_only
def admin(request):
    room_repository = RoomRepository()
    site_config_repository = SiteConfigurationRepository()

    get_admin_data_use_case = GetAdminDashboardDataUseCase(room_repository, site_config_repository)
    data = get_admin_data_use_case.execute()

    return render(request, 'chat/admin.html', {
        'rooms': data['rooms'],
        'show_chat': data['show_chat'],
    })


@admin_only
def room(request, uuid):
    room_repository = RoomRepository()
    get_or_update_room_use_case = GetOrUpdateRoomUseCase(room_repository)

    room = get_or_update_room_use_case.execute(uuid, request.user)

    return render(request, 'chat/room.html', {
        'room': room,
    })


@admin_only
@check_group(allowed_groups=['Agent'])
def delete_room(request, uuid):
    if request.user.has_perm('room.delete_room'):
        room_repository = RoomRepository()
        delete_room_use_case = DeleteRoomUseCase(room_repository)

        delete_room_use_case.execute(uuid)

        messages.success(request, 'The room was deleted!')
        return redirect('/chat-admin/')

    messages.error(request, 'You don\'t have access to delete rooms!')
    return redirect('/chat-admin/')


@admin_only
@check_group(allowed_groups=['Agent'])
def user_detail(request, uuid):
    user = UserRepository.get_user(uuid)
    rooms = RoomRepository.get_all_by_user(user)

    return render(request, 'chat/user_detail.html', {
        'user': user, 
        'rooms': rooms,
    })


    

