from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage
import os
from django.contrib.staticfiles.views import serve
from django.http import HttpResponse
import subprocess

command = 'python chequeaiml/scripts/main.py --input_image ../media/Cheque_1.jpg'


def simple_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        print(result.stdout)
        print(result.stderr)

        

        
        response = serve(request,'../static/cq/Cheque_details.xlsx')
        return response

        return render(request, 'core/simple_upload.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'core/simple_upload.html')

#def chequeupdate(request):
 #   return render(request,'core/chequeupdate.html')  