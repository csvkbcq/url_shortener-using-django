from django.shortcuts import render, redirect, get_object_or_404
from .forms import URLForm
from .models import URL
import string
import random

def generate_short_url():
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(6))

def home(request):
    form = URLForm(request.POST or None)
    if form.is_valid():
        url_instance = form.save(commit=False)
        url_instance.short_url = generate_short_url()
        url_instance.save()
        return render(request, 'shortener/success.html', {'short_url': url_instance.short_url})
    return render(request, 'shortener/home.html', {'form': form})

def redirect_url(request, short_url):
    url_instance = get_object_or_404(URL, short_url=short_url)
    return redirect(url_instance.original_url)
