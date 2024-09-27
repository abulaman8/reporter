// Navbar Menu Sheet
console.log("hello")

const sidebar = document.getElementById("menu-sheet");
const menu = document.getElementById("menu");
const close = document.getElementById("close-menu");
const contents = document.getElementById("contents");
const sidebarContents = document.querySelectorAll(".sidebar-items")

menu.addEventListener("click", () => {
  sidebar.style.width = "90vw";
  sidebar.style.visibility = "visible";
  contents.style.visibility = "visible";
});
close.addEventListener("click", () => {
  sidebar.style.width = "0px";
  setTimeout(() => {
    sidebar.style.visibility = "hidden";
  }, 300);
  contents.style.visibility = "hidden";
});

let currentPath = window.location.pathname.split('/')[1]
console.log(window.location.pathname.split('/'))
if (currentPath == 'order' && window.location.pathname.split('/').length == 4 &&window.location.pathname.split('/')[2] == 'new') {
  currentPath = 'new'
}
if (currentPath == 'admin') {
  currentPath = window.location.pathname.split('/')[2]
}
console.log(currentPath)


sidebarContents.forEach(content => {
  if(content.classList.contains(currentPath)) {
    content.classList.add('active')
  }
})




