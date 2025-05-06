function toggleMenu() {
    const menu = document.querySelector(".menu-links");
    const icon = document.querySelector(".hamburger-icon");
    menu.classList.toggle("open");
    icon.classList.toggle("open");
}

window.open(
    'https://google.com',
    '_blank' // <- This is what makes it open in a new window.
  );