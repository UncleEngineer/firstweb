from django.shortcuts import render
from django.http import HttpResponse
from .models import Post, ProductDemo

def Homepage(request):
    all_posts = Post.objects.all()

    return render(request, 'company/home.html', {'all_posts': all_posts})


def about(request):
    data = ProductDemo.objects.all() # --> SELECT * from company_productdemo
    context = {'data':data} # attachment
    return render(request, 'company/about.html',context)


def product(request):
    data = ProductDemo.objects.all() # --> SELECT * from company_productdemo
    context = {'data':data} # attachment
    return render(request, 'company/product.html',context)
