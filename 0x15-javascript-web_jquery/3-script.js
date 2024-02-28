const header = document.querySelector("header");
const division = document.querySelector("#red_header");
division.addEventListener("click", () => {
  header.classList.add('red');
});
