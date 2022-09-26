from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


def index(request: HttpRequest) -> HttpResponse:
    context = {}
    return render(request, "index.html", context=context)


def room(request: HttpRequest, room_name: str) -> HttpResponse:
    context = {
        "room_name": room_name
    }
    return render(request, "chatroom.html", context=context)
