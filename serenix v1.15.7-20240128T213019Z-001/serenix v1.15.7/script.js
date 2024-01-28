var dialog = confirm("Voulez-vous traduire la page en anglais ?");
if (dialog) {
    console.log('English')
}
else {
    console.log('French')
}

function search_concerts() {
    let input = document.getElementById('searchbar').value
    input=input.toLowerCase();
    let x = document.getElementsByClassName('concerts');
      
    for (i = 0; i < x.length; i++) { 
        if (!x[i].innerHTML.toLowerCase().includes(input)) {
            x[i].style.display="none";
        }
        else {
            x[i].style.display="list-item";                 
        }
    }
}

function changeBackground() {
    // récupérer l'élément body
    const body = document.querySelector("body");
    // changer la couleur de fond
    body.style.backgroundImage = "url(https://pbs.twimg.com/media/FnT3S1pWQAAJC0J.jpg:large)";

}

function basicBackground() {

    const body = document.querySelector("body");
    // changer la couleur de fond
    body.style.backgroundImage = "url(https://www.peintures1825.fr/wp-content/uploads/2018/04/1998_1-1.jpg)";

}

function HellfestBackground() {

    const body = document.querySelector("body");
    // changer la couleur de fond
    body.style.backgroundImage = "url(https://api-cdn.arte.tv/img/v2/image/ksN5Q9drCGcBFB8u3o63MC/1920x1080)";

}

function LesnuitscourtesBackground() {

    const body = document.querySelector("body");
    // changer la couleur de fond
    body.style.backgroundImage = "url(https://radio.vinci-autoroutes.com/medias/image/f8d6c61c5be145e6ba7d10554e3d35ff.jpg)";

}

function RockenSeineBackground() {

    const body = document.querySelector("body");
    // changer la couleur de fond
    body.style.backgroundImage = "url(https://www.rollingstone.fr/wp-content/uploads/2017/07/rock-en-seine.jpg)";

}

function foncEntre_id(){
    document.querySelector("#idea").classList.remove("black");
    document.querySelector("#idea").classList.add("aqua");
    document.querySelector("#purpose").classList.remove("size_transition_out");
    document.querySelector("#purpose").classList.add("size_transition_over")
}

function foncQuitte_id() {
    document.querySelector("#idea").classList.remove("aqua");
    document.querySelector("#idea").classList.add("black");
    document.querySelector("#purpose").classList.remove("size_transition_over");
    document.querySelector("#purpose").classList.add("size_transition_out")
}

function foncEntre_purpose(){
    document.querySelector("#purpose").classList.remove("black");
    document.querySelector("#purpose").classList.add("aqua");
    document.querySelector("#idea").classList.remove("size_transition_out");
    document.querySelector("#idea").classList.add("size_transition_over")
}
    
function foncQuitte_purpose() {
    document.querySelector("#purpose").classList.remove("aqua");
    document.querySelector("#purpose").classList.add("black");
    document.querySelector("#idea").classList.remove("size_transition_over");
    document.querySelector("#idea").classList.add("size_transition_out")
}

function foncQuitte_purpose() {
    document.querySelector("#purpose").classList.remove("aqua");
    document.querySelector("#purpose").classList.add("black");
    document.querySelector("#idea").classList.remove("size_transition_over");
    document.querySelector("#idea").classList.add("size_transition_out")
}

function hide_id() {
    document.querySelector("#id_img").classList.add("hide");
    document.querySelector("#id_card p").classList.add("hide");
    document.querySelector("#id_card h3").classList.remove("hide");
    document.querySelector("#id_card").classList.add("id_card_background");
    document.querySelector("#id_card").classList.remove("id_card_shadow");
}

function reveal_id() {
    document.querySelector("#id_img").classList.remove("hide");
    document.querySelector("#id_card p").classList.remove("hide");
    document.querySelector("#id_card h3").classList.add("hide");
    document.querySelector("#id_card").classList.remove("id_card_background");
    document.querySelector("#id_card").classList.add("id_card_shadow");
}

function hide_id2() {
    document.querySelector("#id_img2").classList.add("hide");
    document.querySelector("#id_card2 p").classList.add("hide");
    document.querySelector("#id_card2 h3").classList.remove("hide");
    document.querySelector("#id_card2").classList.add("id_card_background");
    document.querySelector("#id_card2").classList.remove("id_card_shadow");
}

function reveal_id2() {
    document.querySelector("#id_img2").classList.remove("hide");
    document.querySelector("#id_card2 p").classList.remove("hide");
    document.querySelector("#id_card2 h3").classList.add("hide");
    document.querySelector("#id_card2").classList.remove("id_card_background");
    document.querySelector("#id_card2").classList.add("id_card_shadow");
}

function hide_id3() {
    document.querySelector("#id_img3").classList.add("hide");
    document.querySelector("#id_card3 p").classList.add("hide");
    document.querySelector("#id_card3 h3").classList.remove("hide");
    document.querySelector("#id_card3").classList.add("id_card_background");
    document.querySelector("#id_card3").classList.remove("id_card_shadow");
}

function reveal_id3() {
    document.querySelector("#id_img3").classList.remove("hide");
    document.querySelector("#id_card3 p").classList.remove("hide");
    document.querySelector("#id_card3 h3").classList.add("hide");
    document.querySelector("#id_card3").classList.remove("id_card_background");
    document.querySelector("#id_card3").classList.add("id_card_shadow");
}

function hide_id4() {
    document.querySelector("#id_img4").classList.add("hide");
    document.querySelector("#id_card4 p").classList.add("hide");
    document.querySelector("#id_card4 h3").classList.remove("hide");
    document.querySelector("#id_card4").classList.add("id_card_background");
    document.querySelector("#id_card4").classList.remove("id_card_shadow");
}

function reveal_id4() {
    document.querySelector("#id_img4").classList.remove("hide");
    document.querySelector("#id_card4 p").classList.remove("hide");
    document.querySelector("#id_card4 h3").classList.add("hide");
    document.querySelector("#id_card4").classList.remove("id_card_background");
    document.querySelector("#id_card4").classList.add("id_card_shadow");
}

test3.js
document.addEventListener("DOMContentLoaded", function() {
    const slider = document.querySelector(".slider");
    const prevBtn = document.querySelector(".prev");
    const nextBtn = document.querySelector(".next");
    const slideWidth = slider.clientWidth;
    const slideCount = slider.childElementCount;
    let currentPosition = 0;
  
    // Function to move the slider to a specific position
    function moveSlider(position) {
      slider.style.transform = `translateX(-${position}px)`;
    }
  
    // Function to move the slider to the next position
    function nextSlide() {
      if (currentPosition >= slideWidth * (slideCount - 1)) {
        currentPosition = 0;
      } else {
        currentPosition += slideWidth;
      }
      moveSlider(currentPosition);
    }
  
    // Function to move the slider to the previous position
    function prevSlide() {
      if (currentPosition <= 0) {
        currentPosition = slideWidth * (slideCount - 1);
      } else {
        currentPosition -= slideWidth;
      }
      moveSlider(currentPosition);
    }
  
    // Event listeners for navigation arrows
    nextBtn.addEventListener("click", nextSlide);
    prevBtn.addEventListener("click", prevSlide);
  
    // Automatic slide change every 10 seconds
    setInterval(nextSlide, 10000);
  });
  