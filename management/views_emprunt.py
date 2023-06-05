from django.shortcuts import redirect, render
from .models import *

def adherant_add_modif(request):
    allEmprunt = emprunt.objects.all()
    if request.method=="POST":
        valeur = request.POST.get("valeur")
        if valeur=="search":
            search = request.POST.get("search")
            allEmprunt = emprunt.objects.filter(titre__icontains = search)
        else:
            code_livre = request.POST.get("code_livre")
            matricule = request.POST.get("matricule")
            date_remis = request.POST.get("date_remis")
            nb_exemp =request.POST.get("nb_exemp")


            if valeur=="add":
                adh = adherant.objects.get(matricule=matricule)
                lvr = livre.objects.get(code_livre=code_livre)
                empr = emprunt.objects.create(code_livre=lvr,matricule=adh,date_remis=date_remis, nb_exemp=nb_exemp)
                empr.save()
            elif valeur=="edit":
                empr = emprunt.objects.get(code_livre=code_livre, matricule=matricule)
                empr.date_remis = date_remis
                empr.nb_exemp = nb_exemp
                nb_exemp.save()

                
def emprunt_supr(request):
    if request.method=="POST":
        identifiant = request.POST.get("identifiant")
        empr = emprunt.objects.get(id=identifiant)
        empr.delete()
    return redirect("home")


