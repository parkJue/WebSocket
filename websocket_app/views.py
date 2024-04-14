# from django.http import FileResponse
from django.shortcuts import render

def websocket_test(request):
    return render(request, "websocket_app/websocket_test.html")
