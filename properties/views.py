from django.shortcuts import render
from django.views.generic import View
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from properties.models import Property, Category
from geodata.models import POI
from .filters import PropertyFilter


class Home(View):

    def get(self, request):
        return render(request, 'properties/index.html', {})


class Map(View):

    def get(self, request):
        return render(request, 'properties/map.html', {})


class PropertyList(ListView):

    model = Property


class PropertyDetail(DetailView):

    model = Property


class SearchView(View):

    def post(self, request):
        return render(request, 'properties/search.html', {})
