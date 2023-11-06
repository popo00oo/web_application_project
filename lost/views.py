from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from lost.models import User, Lost, Notice
from django.contrib import messages
from lost.forms import RegisterForm,LoginForm
from django.contrib.auth.hashers import make_password,check_password



# Create your views here.

# User registration
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            User.objects.create(
                username=form.cleaned_data['username'],
                password=make_password(form.cleaned_data['password'])  # Hash password
            )
            messages.success(request, 'Your account has been created! You are now able to log in.')
            return redirect('login')
        else:
            # The form will contain the validation error
            messages.error(request, 'Username already exists')

            return redirect('login')

    else:
        form = RegisterForm()
    return redirect('register')





#User login
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = User.objects.get(username=username)
            # Check the password
            if check_password(password, user.password):
                userid = User.objects.get(username=username).id
                messages.success(request,'Already login')
                notices = Notice.objects.all()

                losts = Lost.objects.all()
                #return redirect('view')
                return render(request, 'index.html', {"userid":userid,"notices": notices, "losts": losts})


            else:
                messages.error(request, 'Username or password error')
                return redirect('login')
        except User.DoesNotExist:
            messages.error(request, 'Username or password error')
            return redirect('login')
    else:
        # Display the login form
        return render(request, 'login.html')





# Issue an announcement
def notice(request):
    if request.method == 'GET':
        # Get all Announcements
        notices = Notice.objects.all()
        losts = Lost.objects.all()
        userid = request.POST.get('userid')

        return render(request, 'index.html',{"userid":userid,"notices": notices, "losts": losts})

    else:
        content = request.POST.get('content')
        userid = request.POST.get('userid')
        Notice.objects.create(Content=content, userid=userid)
        # Get all Announcements
        # Get all lost items
        notices = Notice.objects.all()
        losts = Lost.objects.all()

        return render(request, 'index.html',{"userid":userid,"notices": notices, "losts": losts})




# Delete notice
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
            return render(request, 'index.html', {"userid":userid,"notices": notices, "losts": losts})
        else:
            print('Announcements not posted by the user himself')
            # Get all Announcements
            notices = Notice.objects.all()
            # Get all lost items
            losts = Lost.objects.all()
            return render(request, 'index.html', {"userid":userid,"notices": notices, "losts": losts})
    return render(request, 'index.html', {"notices": notices, "losts": losts})


# Search for lost
def search(request):
    if request.method == 'GET':
        userid = request.POST.get('userid')

        notices = Notice.objects.all()

        losts = Lost.objects.all()
        return render(request, 'index.html', {"userid":userid,"notices": notices, "losts": losts})
    else:

        notices = Notice.objects.all()

        content = request.POST.get('content')
        userid = request.POST.get('userid')
        # Search by Location，Category，UPass，Description contains content of lost property
        losts = Lost.objects.filter(Location__contains=content) | Lost.objects.filter(Category__contains=content) | Lost.objects.filter(UPass__contains=content) | Lost.objects.filter(Description__contains=content)
        return render(request, 'index.html', {"userid":userid,'losts': losts, "notices": notices})