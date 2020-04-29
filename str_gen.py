import time
from datetime import datetime
import django

django.setup()

from home.models import Process

i = 0
while(i < 10):
    p = Process(pid=str(i), remark=str(datetime.now()))
    p.save()
    i = i + 1
    time.sleep(5)



