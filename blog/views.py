from django.shortcuts import render


def view_blog(request):
    return render(request, 'blog.html', {})
