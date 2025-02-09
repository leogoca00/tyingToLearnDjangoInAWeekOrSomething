from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path("", views.first),
    path("about/", views.about), #The idea behind include() is to make it easy to plug-and-play URLs.
    path("home/", include("timeapp.urls")), #El include funciona para decir cual va a ser la pagina principal, en este caso, home/, ahora para visitrar la funcion de first hay que ir a home/ y para visitar about hay que ir a home/about
                                            #entonces al include se le llama prefijo
    


]