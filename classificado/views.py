from django.shortcuts import redirect, render, get_object_or_404
from .models import Category, Adverts, FeedBack
from datetime import datetime

def index(request):
    categories = Category.objects.all()
    adverts = Adverts.objects.all().order_by('-id')
    return render(request, 'pages/index.html', {'adverts':adverts, 'categories':categories})

def announce(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        category = request.POST.get('category')
        city = request.POST.get('city')
        district = request.POST.get('district')
        image_1 = request.FILES.get('image_1')
        image_2 = request.FILES.get('image_2')
        image_3 = request.FILES.get('image_3')
        price = request.POST.get('price')
        
        add = Adverts.objects.create(user_id=request.user.id, title=title, description=description,
                                     category_id=category, city=city, district=district,
                                     image_1=image_1, image_2=image_2, image_3=image_3, price=price,
                                     date=datetime.now())        
        return redirect('home')        
    else:
        categories = Category.objects.all()    
        return render(request, 'pages/announce.html', {'categories':categories})

def filter(request, Categoria):
    categories = Category.objects.all()
    adverts = Adverts.objects.filter(category__name=Categoria)
    return render(request, 'pages/index.html', {'adverts':adverts, 'categories':categories})

def my_ads(request):
    my_ads = Adverts.objects.filter(user=request.user.id)
    return render(request, 'pages/my_ads.html', {'my_ads':my_ads})

def remove_ads(request, id):
    remove = Adverts.objects.get(id=id)
    remove.delete()
    return redirect('my_ads')
    
def item(request, title, id):
    announcement = get_object_or_404(Adverts, id=id)
    return render(request, 'pages/item.html', {'announcement':announcement})    