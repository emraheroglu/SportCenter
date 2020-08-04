from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render


# Create your views here.
from home.models import Setting, ContactFormMessage, ContactFormu
from product.models import Category, Product


def index(request):
    setting = Setting.objects.get(pk=1)
    category = Category.objects.all()
    context = {'setting': setting,
               'page':'home',
               'category': category,
               }
    return render(request, 'index.html', context)

def hakkimizda(request):
    setting = Setting.objects.get(pk=1)
    context = {'setting': setting, 'page':'hakkimizda'}
    return render(request, 'hakkimizda.html', context)

def iletisim(request):
    #formu kaydetmek için bu fonksiyon yazıldı
    if request.method == 'POST': #form post ediliyor
        form = ContactFormu(request.POST)
        if form.is_valid():
            data = ContactFormMessage()
            data.name = form.cleaned_data['name']
            data.email = form.cleaned_data['email']
            data.subject = form.cleaned_data['subject']
            data.message = form.cleaned_data['message']
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()
            messages.success(request, "Mesajınız başarı ile gönderilmiştir, Teşekkür Ederiz")
            return HttpResponseRedirect ('/iletisim')

    #forma ulaşmak için bu kodlar yazıldı
    setting = Setting.objects.get(pk=1)
    form = ContactFormu()
    context = {'setting': setting,
               'form': form
               }
    return render(request, 'iletisim.html', context)

def referanslar(request):
    setting = Setting.objects.get(pk=1)
    context = {'setting': setting, 'page':'referanslar'}
    return render(request, 'referanslar.html', context)

def blog(request):
    setting = Setting.objects.get(pk=1)
    context = {'setting': setting,'page':'blog'}
    return render(request, 'blog.html', context)

def singleblog(request):
    setting = Setting.objects.get(pk=1)
    context = {'setting': setting,'page':'singleblog'}
    return render(request, 'singleblog.html', context)

def galeri(request):
    setting = Setting.objects.get(pk=1)
    context = {'setting': setting,'page':'galeri'}
    return render(request, 'galeri.html', context)

def fiyatlar(request):
    setting = Setting.objects.get(pk=1)
    context = {'setting': setting,'page':'fiyatlar'}
    return render(request, 'fiyatlar.html', context)

def join(request):
    setting = Setting.objects.get(pk=1)
    context = {'setting': setting,'page':'join'}
    return render(request, 'join.html', context)

def login(request):
    setting = Setting.objects.get(pk=1)
    context = {'setting': setting,'page':'login'}
    return render(request, 'login.html', context)