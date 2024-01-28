var dialog = confirm("Voulez-vous traduire la page en anglais ?");
if (dialog) {
    window.location.href = "test7_english_version.html"; // Replace with the desired URL
} else {
    console.log('French');
}

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
  