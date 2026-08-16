from django.shortcuts import render


from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
]

def index(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")
        # Handle message delivery or database saving here
    return render(request, "index.html")