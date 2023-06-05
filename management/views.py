from django.shortcuts import redirect, render
from .models import *
from django.contrib.auth import authenticate, login, logout

def adherant_add_modif(request):
    allAdherant = adherant.objects.all()
    userData = request.user
    if str(userData)=="AnonymousUser":return redirect("login")

    if request.method=="POST":
        valeur = request.POST.get("valeur")
        print("valeur : ", valeur)
        if valeur=="search":
            search = request.POST.get("search")
            if search:
                allAdherant = adherant.objects.filter(nom__icontains = search)
        else:
            matricule = request.POST.get("matricule")
            nom = request.POST.get("nom")
            prenom =request.POST.get("prenom")
            date_naiss = request.POST.get("date_naissance")
            lieu_naiss = request.POST.get("lieu_naissance")
            adresse = request.POST.get("adresse")
            num_tel = request.POST.get("numTel")

            if valeur=="add":
                adherants = adherant.objects.create(matricule=matricule,nom=nom,prenom=prenom,date_naissance=date_naiss,lieu_naissance=lieu_naiss,adresse=adresse,num_tel=num_tel)
                adherants.save()
            elif valeur=="edit":
                adherants = adherant.objects.get(matricule=matricule)
                adherants.nom = nom
                adherants.prenom = prenom
                adherants.date_naissance = date_naiss
                adherants.lieu_naissance = lieu_naiss
                adherants.adresse = adresse
                adherants.num_tel = num_tel
                adherants.save()
    return render(request, 'adherant.html',{"adherants": allAdherant, "active" : "adh", "users": userData})
                
def adherent_supr(request, matricule):
    adh = adherant.objects.get(matricule=matricule)
    adh.delete()
    return redirect("home")



def loginViews(request):
    error = ""
    if request.method=="POST":
        nom = request.POST.get("nom")
        mdp = request.POST.get("password")

        user = authenticate(username=nom, password=mdp)
        if user:
            login(request, user)
            return redirect("home")
        else:error="Erreur de connexion"
    return render(request, 'login.html', {"erreur": error})

def disconnectUser(request):
    logout(request)
    return redirect("login")