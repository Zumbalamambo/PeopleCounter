from django.shortcuts import render
from django.http import HttpResponse
from detector import analyzeImg
import json
import time

# Create your views here.
def counter( request ):
    return render( request, 'Counter/counter.html' )


def analyze( request ):
    if request.method == "POST":
        file = request.FILES['file']
        fileName = "temp/" + str(int(round(time.time()*1000))) + file.name
        with open( fileName, 'wb+' ) as destFile:
            for chunk in file.chunks():
                destFile.write( chunk )
        return HttpResponse(json.dumps(analyzeImg(fileName)))
    return HttpResponse(status=500);
