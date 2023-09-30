from django.shortcuts import render
from django.http import JsonResponse
from django.utils import timezone
from main.models import PlyMeta, SongMeta, SongInPly, PlyTitleEmbedding

def index(request):
    return render(request, "1_index.html")

def input(request):
    return render(request, "2_input.html")

def loading(request):
    return render(request, "3_loading.html")

def output(request):
    return render(request, "4_output.html")