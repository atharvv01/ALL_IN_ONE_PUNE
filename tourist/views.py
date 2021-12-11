from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages

# Create your views here.
def Home(request):
    all_cat = Category.objects.all()
    city = Select_City.objects.all()
    error = False
    if request.method == "POST":
        cat = request.POST['category']
        city = request.POST['city']

        category = Category.objects.get(id=cat)
        city_data = Select_City.objects.get(id=city)
        places = Places.objects.filter(select_city=city_data, category=category)
        li = []
        for i in places:
            li.append(str(i.id))
        a = '_'.join(li)
        print(a)
        return redirect('places',a)
    d = {'city': city, 'all_cat': all_cat, 'error': error}
    return render(request, 'index.html', d)

def city_places(request,num):
    li = num.split('_')
    data = []
    for i in Places.objects.all():
        if str(i.id) in li:
            data.append(i)
    d = {"places":data}

    return render(request, 'places.html', d)

def Selection(request, pid):
    all_cat = Category.objects.all()
    city = Select_City.objects.all()
    data2 = Places.objects.get(id=pid)


    d = {'city': city, 'all_cat': all_cat, 'data2': data2}
    return render(request, 'selection.html', d)
def Admin_login(request):
    error = False

    if request.method == "POST":
        u = request.POST['name']
        p = request.POST['pwd']
        user = authenticate(username=u, password=p)
        if user.is_staff:
            login(request, user)
            return redirect('administration')
        else:
            error = True

    d = {'error': error}

    return render(request, 'admin_login.html', d)

def Administration(request):
    if not request.user.is_staff:
        return redirect('admin_login')
    data = User.objects.all()
    d = {'data': data}
    return render(request, 'administration.html', d)

def Add_City(request):
    if not request.user.is_staff:
        return redirect('admin_login')
    if request.method == "POST":
        c = request.POST['city']
        Select_City.objects.create(city_name=c)
        return redirect('view_city')
    return render(request, 'add_city.html')

def View_City(request):
    if not request.user.is_staff:
        return redirect('admin_login')
    city = Select_City.objects.all()
    d = {'city': city}
    return render(request, 'view_city.html', d)

def delete_City(request, pid):
    if not request.user.is_staff:
        return redirect('admin_login')
    if Select_City.objects.filter(id=pid).exists():
        data3 = Select_City.objects.get(id=pid)
        data3.delete()
        message1 = messages.info(request, '1 City is Deleted')
        return redirect('view_city')

def Add_Category(request):
    if not request.user.is_staff:
        return redirect('admin_login')
    if request.method == "POST":
        c = request.POST['cat']
        Category.objects.create(cat_name=c)
        return redirect('view_category')
    return render(request, 'add_category.html')

def View_Category(request):
    if not request.user.is_staff:
        return redirect('admin_login')
    cat = Category.objects.all()
    d = {'cat': cat}
    return render(request, 'view_category.html', d)

def delete_Category(request, pid):
    if not request.user.is_staff:
        return redirect('admin_login')
    if Category.objects.filter(id=pid).exists():
        data3 = Category.objects.get(id=pid)
        data3.delete()
        message1 = messages.info(request, '1 Category is Deleted')
        return redirect('view_category')

def Add_Places(request):
    if not request.user.is_staff:
        return redirect('admin_login')
    if request.method == "POST":
        cat = request.POST['cat']
        city = request.POST['city']
        img = request.FILES['image']
        place = request.POST['place']
        loc = request.POST['location']
        rat = request.POST['rating']
        desc = request.POST['description']
        city1 = Select_City.objects.filter(id=city).first()
        cat1 = Category.objects.filter(id=cat).first()
        Places.objects.create(category=cat1, select_city=city1, image=img, place_name=place, description=desc, location=loc, rating=rat)
        return redirect('view_places')
    cat = Category.objects.all()
    city = Select_City.objects.all()
    d = {'cat':cat, 'city': city}
    return render(request, 'add_places.html', d)

def View_Places(request):
    if not request.user.is_staff:
        return redirect('admin_login')
    place = Places.objects.all()
    d = {'place': place}
    return render(request, 'view_places.html',d)

def delete_Place(request, pid):
    if not request.user.is_staff:
        return redirect('admin_login')
    if Places.objects.filter(id=pid).exists():
        data3 = Places.objects.get(id=pid)
        data3.delete()
        message1 = messages.info(request, '1 Place is Deleted')
    return redirect('view_places')


def Edit_Place(request,pid):
    if not request.user.is_staff:
        return redirect('admin_login')
    data = Places.objects.get(id=pid)

    if request.method == "POST":
        cat = request.POST['cat']
        city = request.POST['city']
        place = request.POST['place']
        loc = request.POST['location']
        rat = request.POST['rating']
        desc = request.POST['description']
        city1 = Select_City.objects.filter(id=city).first()
        cat1 = Category.objects.filter(id=cat).first()
        data.category = cat1
        data.select_city = city1
        data.place_name = place
        data.description = desc
        data.location = loc
        data.rating = rat
        data.save()
        try:
            img = request.FILES['image']
            data.image = img
            data.save()
            message1 = messages.info(request, 'selected one is Edited')
            return redirect('view_places')
        except:
            pass
    cat = Category.objects.all()
    city = Select_City.objects.all()
    d = {'cat': cat, 'city': city, 'data': data}
    return render(request, 'edit_place.html', d)

def Logout_admin(request):
    if not request.user.is_staff:
        return redirect('admin_login')
    logout(request)
    return redirect('admin_login')



def Map(request):
    return render(request, 'map.html')
def About(request):
    return render(request, 'about.html')

def Contact(request):
    error = ""
    if request.method == "POST":
        fn = request.POST['firstname']
        ln = request.POST['lastname']
        cn = request.POST['cnum']
        em = request.POST['email']
        sub = request.POST['subject']
        try:
            tblContact.objects.create(firstname=fn,lastname=ln,contact=cn,emailid=em,subject=sub)
            error = "no"
        except:
            error = "yes"
    d = {'error': error}
    return render(request, 'contact.html',d)

def user_query(request):
    if not request.user.is_staff:
        return redirect('admin_login')
    contact = tblContact.objects.all()
    d = {'contact': contact}
    return render(request, 'user_query.html',d)

def delete_query(request,pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    contact = tblContact.objects.get(id=pid)
    contact.delete()
    return redirect('user_query')