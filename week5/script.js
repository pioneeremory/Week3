const buttons = document.querySelectorAll("button");

function random(number) {
  return Math.floor(Math.random() * (number + 1));
}
// when button is clicked change the bg color of that button
buttons.forEach(btn => {
    btn.addEventListener("click", () => {
        const rndCol = `rgb(${random(255)} ${random(255)} ${random(255)})`;
        btn.style.backgroundColor = rndCol;
});
});

const myBox = document.getElementById("myBox");

function changeColor(event){
    event.target.style.backgroundColor = "green";
    event.target.textContent = "EAT MORE 🍕";
    event.target.style.fontSize = "5.5rem"; 
    document.body.style.backgroundColor = "lightBlue";
}
myBox.addEventListener("click", changeColor);

const videoWrapper = document.querySelector(".video-wrapper");

video-wrapper.addEventListener("mouseover", event => {
    event.target.style.backgroundColor = "orange";
    event.target.textContent = "Warning, NSFW";
});
