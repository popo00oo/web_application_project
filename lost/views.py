from django.shortcuts import render,  redirect
from django.views.decorators.csrf import csrf_exempt
from lost.models import User, Lost, Notice
from django.contrib import messages
from django.urls import reverse

# Create your views here.
from django.http import HttpResponseRedirect


# User registration
@csrf_exempt
def register(request):
    if request.method == 'GET':
        #return render(request, 'login.html')
        # Ensure No Resubmission so use redirect
        return redirect('login')

    else:
        username = request.POST.get('username')
        password = request.POST.get('password')
        # is it user already have
        if User.objects.filter(username=username).exists():

           # print('Username already exists')
          messages.error(request, 'Username already exists')
          #return render(request, 'login.html', {'error': 'Username already exists'})
          #Ensure No Resubmission so use redirect
          return redirect('register')

        else:
            User.objects.create(username=username, password=password)
            messages.success(request, 'Your account has been created! You are now able to log in.')
            #return render(request, 'login.html', {'error': 'Username already exists'})
            return redirect('register')




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
                #print('wrong password')
                messages.error(request, 'Wrong password')
                #return render(request, 'login.html', {'error': 'wrong password'})
                return redirect('login')


        else:
            #print('Username does not exist')
            messages.error(request, 'Username does not exist')
            #return render(request, 'login.html', {'error': 'Username does not exist'})
            return redirect('login')




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


