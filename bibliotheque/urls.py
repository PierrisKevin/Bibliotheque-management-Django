from django.contrib import admin
from django.urls import path
from management.views import adherant_add_modif,adherent_supr, loginViews, disconnectUser
from livre.views import livre_supr, livre_add_modif

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", loginViews, name="login"),
    path("logout/", disconnectUser, name="logout"),
    path("index/", adherant_add_modif, name="home"),
    path("index/<int:matricule>/", adherent_supr, name="adherent_suprimmer"),
    path("livre/", livre_add_modif, name="livre"),
    path("livre/<int:code_livre>/", livre_supr, name="livre_del"),
]
