

from django.shortcuts import render, get_object_or_404
from .models import Visitor
from django.shortcuts import render




def detail(request, unique_identifier):
    visitor = get_object_or_404(Visitor, unique_identifier=unique_identifier)
    return render(request, 'detail.html', {'visitor': visitor})

