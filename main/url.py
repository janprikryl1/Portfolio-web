from django.urls import path

from . import views

urlpatterns = [
    # "odkazy" na funkce vracející HTML soubory
    path('', views.index, name='index'),
    path('contact', views.contact, name='contact'),
    path('save_message', views.save_message, name='save_message'),
    path('projects', views.projects, name='projects'),
    path('project_details', views.project_details, name='project_details'),
    ]