from django.shortcuts import render
from .models import Process
import subprocess
# from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')

def run_ffmpeg(request):
    sample_str = ""
    p1 = subprocess.Popen("ffmpeg", stderr=subprocess.STDOUT, stdout=subprocess.PIPE, shell=False, universal_newlines=True)
    for line in p1.stdout:
        sample_str = sample_str + line
    my_dict = {"sample_str":sample_str}
    return render(request, 'index.html', context=my_dict)

def start_process(request):
    p1 = subprocess.Popen("python str_gen.py", shell=True)
    return render(request, 'index.html')

def show_process(request):
    p = Process.objects.all()
    my_dict = {"process_str": []}
    for pro in p:
        # print(pro.pid)
        my_dict["process_str"].append(pro.pid + " " + pro.remark)
    print(my_dict)
    return render(request, 'index.html', context=my_dict)

