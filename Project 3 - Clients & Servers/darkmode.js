
// check for previous session localstorage
let storedTheme = localStorage.getItem('storedTheme');
if (storedTheme == 'dark-mode')
{
    document.body.classList.toggle('dark-mode');
}
else
{
    console.log('local storage is clear');
}


function darkmodetoggle() {
    var element = document.body;
    element.classList.toggle("dark-mode");

    console.log(element.classList);
    localStorage.setItem('storedTheme', element.classList);
  }