const show_pass = document.querySelector(".show-pass")
const pass_contain = document.querySelector('input[type="password"]')
const btn_submit = document.querySelector('input[type="submit"]')

show_pass.addEventListener("mousedown",()=>{
    pass_contain.setAttribute("type", "text")
})
show_pass.addEventListener("mouseup",()=>{
    pass_contain.setAttribute("type", "password")
})

btn_submit.addEventListener("click", ()=>{
    btn_submit.disable = true
    btn_submit.style.opacity = ".6"
})

