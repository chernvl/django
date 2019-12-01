from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.files.storage import FileSystemStorage

from .import forms

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

