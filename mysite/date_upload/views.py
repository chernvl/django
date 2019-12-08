from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.files.storage import FileSystemStorage
from django.shortcuts import redirect

from .forms import Data_form
from .models import Raw_data

def index (request):
    return render (request,'data_upload/index.html')

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
