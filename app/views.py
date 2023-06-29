from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect


from app.models import *

def VideoFunction(request):  

    videos=video.objects.all()
    d={'videos':videos}
    if request.method == 'POST' and request.FILES:
        video_description = request.POST['video_description']
        videofile = request.FILES['video_file']
        VO = video(Video_description=video_description, Video_file=videofile)
        VO.save()
        return HttpResponseRedirect('VideoFunction.html')
    return render(request,'VideoFunction.html',d)
