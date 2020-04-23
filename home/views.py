from django.shortcuts import render
import subprocess
# from django.http import HttpResponse

# Create your views here.
def index(request):
    pipe = subprocess.Popen("python str_gen.py", stdout=subprocess.PIPE, shell=True)
    sample_str = pipe.communicate()[0]
    print(sample_str)
    my_dict = {"sample_str":sample_str}
    return render(request, 'index.html', context=my_dict)