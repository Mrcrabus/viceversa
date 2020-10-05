from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def reverse(request):
    reverse_text = request.GET['q'][::-1]
    return render(request, 'reverse.html', {'usertext': reverse_text})
