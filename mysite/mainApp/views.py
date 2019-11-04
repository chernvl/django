from django.shortcuts import render
from django.core.files.storage import FileSystemStorage

# Create your views here.
def index(request):
    return render(request, 'mainApp/homePage.html')

def contacts(request):
    return  render(request, 'mainApp/basic.html', {'values': ['E-mail:', 'test@test.test']})

def upload (request):
    if request.method == 'POST':
        uplaoded_file = request.FILES ['document']
        fs = FileSystemStorage()
        fs.save(uplaoded_file.name,uplaoded_file)
    return render(request,'mainApp/upload.html')
