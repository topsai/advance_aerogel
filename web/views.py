from django.shortcuts import render
from web.models import Blog


# Create your views here.
def home(request):
    return render(request, 'web/index.html')


def service(request):
    return render(request, 'web/services.html')


def about(request):
    return render(request, 'web/about.html')


def contact(request):
    return render(request, 'web/contact.html')


def news(request):
    data = Blog.objects.all()
    return render(request, 'web/typo.html', {"data": data})


def news_detail(request, blog_id=None):
    data = None
    if blog_id:
        data = Blog.objects.filter(id=blog_id)
    return render(request, 'web/news_detail.html', {"data": data})


def gallery(request):
    return render(request, 'web/gallery.html')


#  cn

def home_cn(request):
    return render(request, 'web_cn/index.html')


def service_cn(request):
    return render(request, 'web_cn/services.html')


def about_cn(request):
    return render(request, 'web_cn/about.html')


def contact_cn(request):
    return render(request, 'web_cn/contact.html')


def news_cn(request):
    data = Blog.objects.all()
    return render(request, 'web_cn/typo.html', {"data": data})


def news_detail_cn(request, blog_id=None):
    data = None
    if blog_id:
        data = Blog.objects.filter(id=blog_id)
    return render(request, 'web_cn/news_detail.html', {"data": data})


def gallery_cn(request):
    return render(request, 'web_cn/gallery.html')
