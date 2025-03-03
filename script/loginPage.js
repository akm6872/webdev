let signup_box= document.querySelector(".signup-box-js");
let student_box=document.querySelector(".student-box-js")

let signup=document.querySelector(".signup-js");
let student=document.querySelector(".student-js");



signup_box.addEventListener("click",()=>{
    student.style.display = "none";
    signup.style.display = "flex";
})

student_box.addEventListener("click", ()=>{
    signup.style.display = "none";
    student.style.display = "flex";
})

