const notesContainer =  document.querySelector(".notes-container")
const addNoteButton = document.querySelector(".add-note-button")
let notes = document.querySelectorAll(".input-box")

function showNotes(){
    notesContainer.innerHTML = localStorage.getItem("notes");
}
showNotes();

function updateLocalStorage(){
    localStorage.setItem("notes", notesContainer.innerHTML);
}

addNoteButton.addEventListener("click", () => {
    let note = document.createElement("p");
    let img = document.createElement("img");
    note.className = "input-box";
    note.setAttribute("contenteditable", "true");
    img.src = "delete.png";
    notesContainer.appendChild(note).appendChild(img);
    updateLocalStorage(); 


})

notesContainer.addEventListener("click", function(e){
    if(e.target.tagName === "IMG"){
        e.target.parentElement.remove();
        updateLocalStorage();
    }
})

document.addEventListener("keydown", event => {
    if(event.key === "Enter"){
        event.preventDefault();
        addNoteButton.click();
    }
    updateLocalStorage();
})