from django.shortcuts import render_to_response

# Create your views here.
import models 

def home(request):
  content = models.getAll()
  return render_to_response('index.html', {'content' : content})
