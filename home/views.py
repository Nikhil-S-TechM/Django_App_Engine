from django.shortcuts import render, redirect
from .models import Process
import subprocess
# from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')

def back(request):
    return redirect(request, index)



def run_ffmpeg(request):
    sample_str = ""
    p1 = subprocess.Popen("ffmpeg", stderr=subprocess.STDOUT, stdout=subprocess.PIPE, shell=False, universal_newlines=True)
    for line in p1.stdout:
        sample_str = sample_str + line
    my_dict = {"sample_str":sample_str}
    return render(request, 'ffmpeg.html', context=my_dict)

def start_process(request):
    p1 = subprocess.Popen("python str_gen.py", shell=True)
    # print(p1.stdout)
    # for line in p1.stdout:
        # sample_str = sample_str + line
    my_dict = {"sample_str":'processes are created...!'}
    return render(request, 'start_process.html', context=my_dict)

def show_process(request):
    p = Process.objects.all()
    p_list = []
    for pro in p:
        # print(pro.pid)
        data = pro.pid +" "+ pro.remark
        p_list.append(data)
    return render(request, 'show_process.html', context={'process_str':p_list})

