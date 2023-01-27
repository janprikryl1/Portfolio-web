from django.http import HttpResponse
from django.shortcuts import render
from .models import Message, Screenshot, Project


# Create your views here.
def index(request):
    return render(request, "index.html")


def contact(request):
    return render(request, "contact.html")


def save_message(request):
    message = Message(name=request.POST['name'], email=request.POST['email'], subject=request.POST['subject'],
                      message=request.POST['message'])
    message.save()
    return HttpResponse()

def projects(request):
    return render(request, "projects.html", {"projects":Project.objects.all()})

def project_details(request):
    project = Project.objects.get(id=int(request.GET['project_id']))
    return render(request, "project_details.html", {"project":project})

# Chyby stránky
def handler404(request, *args, **argv):  # Stránka nenalezena
    pass  # return render(request, "error.html", {'code': 404})


def handler500(request, *args, **argv):  # Jiná chyba
    pass  # return render(request, "error.html", {'code': 500})
