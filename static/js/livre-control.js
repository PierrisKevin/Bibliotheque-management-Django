// control des suppresion 
const del_btn = document.querySelectorAll(".options a:nth-child(2) i")
const del_modal = document.querySelector(".modal-supr")
const overlay = document.querySelector(".overlay-all")
const exit = document.querySelector(".exit-del")

del_btn.forEach(del => {
    del.addEventListener("click", (e)=>{
        del_modal.classList.remove("hidden")
        overlay.classList.remove("hidden")
        let child = del.parentNode.parentNode.parentNode.childNodes[5].childNodes[1]
        const delValeur = document.querySelector(".delValue")
        delValeur.setAttribute("href", "/livre/"+child.textContent)
        console.log(delValeur)
    })
    
});
exit.addEventListener("click", ()=>{
    del_modal.classList.add("hidden")
    overlay.classList.add("hidden")
})

//ajout controls
const valeur = document.querySelector(".add_and_edit")
const formulaire = document.querySelector(".formulaire")
add_btn = document.querySelector(".add-btn")
exit_add = document.querySelector(".exit-add")
add_modal = document.querySelector(".modal-ajout")
add_btn.addEventListener("click", ()=>{
    formulaire.reset()
    valeur.value = "add"
    add_modal.classList.remove("hidden")
    overlay.classList.remove("hidden")
})
exit_add.addEventListener("click", ()=>{
    add_modal.classList.add("hidden")
    overlay.classList.add("hidden")
})

//modification
const edit_btn = document.querySelectorAll(".options a:nth-child(1) i")
const allInputs = document.querySelectorAll(".modal-ajout input")

edit_btn.forEach(edit => {
    edit.addEventListener("click", (e)=>{
        valeur.value = "edit"
        let allValues = e.target.parentNode.parentNode.parentNode.childNodes
        const code_livre = allValues[5].childNodes[1].textContent
        const titre = allValues[7].childNodes[1].textContent
        const auteur = allValues[7].childNodes[3].textContent

        const date_edit = allValues[9].childNodes[1].innerText
        const edition = allValues[9].childNodes[3].innerText
        


        const allData = [code_livre, titre, auteur, date_edit, edition]
        for(i=0;i<allData.length;i++){
            allInputs[i+1].value = allData[i]
        }
        add_modal.classList.remove("hidden")
        overlay.classList.remove("hidden")
        
    })
});