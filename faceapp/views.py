from django.shortcuts import render
from django.http import HttpResponse
from .models import Photo
from faceapp.forms import ImageForm
from django.views.generic import CreateView, DetailView
import os
from faceapp import algorythm

class AnswerView(DetailView):
    template_name = 'faceapp/result.html'
    model = Photo

class SortView(CreateView):
    template_name = 'faceapp/home.html'
    model = Photo
    form_class = ImageForm

    def get_success_url(self):
        my_object = Photo.objects.latest('pk')
        absolute_path = os.path.join(os.getcwd(), 'media', 'images', os.path.split(my_object.image.url)[1])
        answer = algorythm.is_criminal(absolute_path)

        my_object.is_criminal = answer
        my_object.save()
        
        return f"result/{my_object.pk}"
