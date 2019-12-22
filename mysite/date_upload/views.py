from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.files.storage import FileSystemStorage
from django.shortcuts import redirect
from date_upload.forms import UserForm

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required


from .forms import Data_form
from .models import Raw_data

def index (request):
    return render (request,'data_upload/index.html')

@login_required
def special(request):
    # Remember to also set login url in settings.py!
    # LOGIN_URL = '/basic_app/user_login/'
    return HttpResponse("You are logged in. Nice!")

@login_required
def user_logout(request):
    # Log out the user.
    logout(request)
    # Return to homepage.
    return HttpResponseRedirect(reverse('index'))

def register(request):

    registered = False

    if request.method == 'POST':

        # Get info from "both" forms
        # It appears as one form to the user on the .html page
        user_form = UserForm(data=request.POST)

        # Check to see both forms are valid
        if user_form.is_valid():

            # Save User Form to Database
            user = user_form.save()

            # Hash the password
            user.set_password(user.password)

            # Update with Hashed password
            user.save()

            # Registration Successful!
            registered = True

        else:
            # One of the forms was invalid if this else gets called.
            print(user_form.errors)

    else:
        # Was not an HTTP post so we just render the forms as blank.
        user_form = UserForm()

    # This is the render and context dictionary to feed
    # back to the registration.html file page.
    return render(request,'data_upload/registration.html',
                          {'user_form':user_form,
                           'registered':registered})
def form_name (request):
    context = {}
    if request.method == 'POST':
        upload_file = request.FILES ['document']
        fs = FileSystemStorage()
        name = fs.save(upload_file.name,upload_file)
        context['url'] = fs.url(name)
    form = forms.Formname()
    return render (request,'data_upload/form_page.html',context)

def models_data (request):
    models = Raw_data.objects.all()
    return render(request,'data_upload/models_list.html',{'models':models})

def models_data_upload (request):
    if request.method == 'POST':
        form = Data_form(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect ('models_data')
    else:
        form = Data_form()
    return render(request,'data_upload/models_data_upload.html',{'form':form
                                                                 }
                  )


def user_login(request):

    if request.method == 'POST':
        # First get the username and password supplied
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Django's built-in authentication function:
        user = authenticate(username=username, password=password)

        # If we have a user
        if user:
            #Check it the account is active
            if user.is_active:
                # Log the user in.
                login(request,user)
                # Send the user back to some page.
                # In this case their homepage.
                return HttpResponseRedirect(reverse('index'))
            else:
                # If account is not active:
                return HttpResponse("Your account is not active.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details supplied.")

    else:
        #Nothing has been provided for username or password.
        return render(request, 'data_upload/login.html', {})