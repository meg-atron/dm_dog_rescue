from django.shortcuts import render

def index(request):
  return render(request, 'dogs/dogs.html')

def dog_detail(request):
  return render(request, 'dogs/dog_detail.html')

def search(request):
  return render(request, 'dogs/search.html')