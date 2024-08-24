from django.shortcuts import render, redirect
from django.http import HttpResponse

def index(request):
    return HttpResponse(f"<h1> {request.tenant} index </h1>")


