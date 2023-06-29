// Join as Talent slide

$(document).ready(function() {
    var slides = $(".carousel-slide");
    var currentSlide = 0;

    // Show the first slide initially
    slides.eq(currentSlide).addClass("active");

    // Function to slide to the next slide
    function nextSlide() {
        slides.eq(currentSlide).removeClass("active");
        currentSlide = (currentSlide + 1) % slides.length;
        slides.eq(currentSlide).addClass("active");
    }

    // Automatically slide to the next slide every 5 seconds
    setInterval(nextSlide, 5000);
});