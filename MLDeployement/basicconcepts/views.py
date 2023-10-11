from django.shortcuts import render
from django.http import HttpResponse

def welcome(request):
    return render(request, 'index.html')

def User(request):
    username = request.GET.get('username', '')  # Use request.GET.get to safely retrieve 'username'

    return render(request, 'user.html', {'name': username})  # Pass 'username' as a key-value pair in the dictionary
