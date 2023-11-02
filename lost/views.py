from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from lost.models import User, Lost, Notice


# Create your views here.


# User registration
@csrf_exempt
def register(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')
        # is it user already have
        if User.objects.filter(username=username):
            print('Username already exists')
            return render(request, 'login.html', {'error': 'Username already exists'})
        else:
            User.objects.create(username=username, password=password)
            return render(request, 'login.html')


#User login
@csrf_exempt
def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')
        # is it username already have
        if User.objects.filter(username=username):
            # is it correct
            if User.objects.filter(username=username, password=password):
                userid = User.objects.get(username=username).id
                # Get all Announcements
                notices = Notice.objects.all()
                # Get all lost items
                losts = Lost.objects.all()
                return render(request, 'index.html',{"userid":userid,"notices":notices,"losts":losts})
            else:
                print('wrong password')
                return render(request, 'login.html', {'error': 'wrong password'})
        else:
            print('Username does not exist')
            return render(request, 'login.html', {'error': 'Username does not exist'})


# Issue an announcement
@csrf_exempt
def notice(request):
    if request.method == 'GET':
        # Get all Announcements
        notices = Notice.objects.all()
        return render(request, 'index.html', {"notices": notices})
    else:
        content = request.POST.get('content')
        userid = request.POST.get('userid')
        Notice.objects.create(Content=content, userid=userid)
        # Get all Announcements
        notices = Notice.objects.all()
        # Get all lost items
        losts = Lost.objects.all()
        return render(request, 'index.html', {"notices": notices, "losts": losts})


# Delete notice
@csrf_exempt
def delnotice(request):
    # Get the Bulletin id
    id = request.GET.get('id')
    userid = request.GET.get('userid')
    # Get all Announcements
    notices = Notice.objects.all()
    # Get all lost items
    losts = Lost.objects.all()
    # is Announcements not posted by the user himself
    if Notice.objects.filter(id=id):
        if Notice.objects.filter(id=id, userid=userid):
            Notice.objects.filter(id=id).delete()
            # Get all Announcements
            notices = Notice.objects.all()
            # Get all lost items
            losts = Lost.objects.all()
            return render(request, 'index.html', {"notices": notices, "losts": losts})
        else:
            print('Announcements not posted by the user himself')
            # Get all Announcements
            notices = Notice.objects.all()
            # Get all lost items
            losts = Lost.objects.all()
            return render(request, 'index.html', {"notices": notices, "losts": losts})
    return render(request, 'index.html', {"notices": notices, "losts": losts})


# Search for lost
@csrf_exempt
def search(request):
    if request.method == 'GET':

        notices = Notice.objects.all()

        losts = Lost.objects.all()
        return render(request, 'index.html', {"notices": notices, "losts": losts})
    else:

        notices = Notice.objects.all()

        content = request.POST.get('content')
        # Search by Location，Category，UPass，Description contains content of lost property
        losts = Lost.objects.filter(Location__contains=content) | Lost.objects.filter(Category__contains=content) | Lost.objects.filter(UPass__contains=content) | Lost.objects.filter(Description__contains=content)
        return render(request, 'index.html', {'losts': losts, "notices": notices})



