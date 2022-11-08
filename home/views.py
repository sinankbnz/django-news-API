from django.shortcuts import render
import requests

def index(request):
    response = requests.get('https://inshorts.deta.dev/news?category=science')
    response1 = requests.get('https://inshorts.deta.dev/news?category=sports')
    response2 = requests.get('https://inshorts.deta.dev/news?category')
    response3 = requests.get('https://inshorts.deta.dev/news?category=business')

    sports = response1.json()
    data1 = sports['data']

    all = response2.json()
    data2 = all['data']

    business = response3.json()
    data3 = business['data']

    posts = response.json()
    data = posts['data']
    return render(request, 'index.html', {'posts': data,'sports':data1, 'all':data2, 'business':data3})

def category(request):
    return render(request,'category.html')
def contact(request):
    return render(request,'contact.html')
def single(request):
    return render(request,'single.html')