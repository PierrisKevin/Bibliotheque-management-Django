from django.shortcuts import redirect, render
from .models import *

def livre_add_modif(request):
    userData = request.user
    allLivre = livre.objects.all()
    if request.method=="POST":
        valeur = request.POST.get("valeur")
        if valeur=="search":
            search = request.POST.get("search")
            allLivre = livre.objects.filter(titre__icontains = search)
        else:
            code_livre = request.POST.get("code_livre")
            titre = request.POST.get("titre")
            auteur = request.POST.get("auteur")
            edit_liv =request.POST.get("edition")
            date_edit =request.POST.get("date_edit")


            if valeur=="add":
                livres = livre.objects.create(code_livre=code_livre,titre=titre,auteur=auteur, edition_liv=edit_liv,date_edit=date_edit)
                livres.save()
            elif valeur=="edit":
                livres = livre.objects.get(code_livre=code_livre)
                livres.titre = titre
                livres.auteur = auteur
                livres.edition_liv = edit_liv
                livres.date_edit = date_edit
                livres.save()
    
    return render(request, 'livre.html',{"livres": allLivre, "active" : "livre", "users": userData})
                
def livre_supr(request):
    if request.method=="POST":
        code_livre = request.POST.get("code_livre")
        lvr = livre.objects.get(code_livre=code_livre)
        lvr.delete()
    return redirect("home")


