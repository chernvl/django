from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.files.storage import FileSystemStorage
from django.shortcuts import redirect
from date_upload.forms import UserForm

from .forms import Data_form
from .models import Raw_data

def index (request):
    return render (request,'data_upload/index.html')

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
