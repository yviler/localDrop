const element = document.querySelectorAll(".data");
const audio = new Audio("/static/assets/sounds/click.wav");

element.forEach((row) => {
  row.addEventListener("mouseenter", () => {
    audio.currentTime = 0;
    audio.play();
  });
});
