from django.shortcuts import render

def index(request):
    return render(request, 'home/index.html')

from django.shortcuts import render

def error_404(request, exception):
    return render(request, 'errors/404.html', status=404)

def error_403(request, exception):
    return render(request, 'errors/403.html', status=403)

def error_500(request):
    return render(request, 'errors/500.html', status=500)

