const carousel = document.querySelector('.carousel');
const carouselContainer = carousel.querySelector('.carousel-container');
const slides = carousel.querySelectorAll('.carousel-slide');
const prevBtn = carousel.querySelector('.carousel-prev');
const nextBtn = carousel.querySelector('.carousel-next');
const slideWidth = slides[0].clientWidth;
let slideIndex = 0;

function slideNext() {
    slideIndex++;
    if (slideIndex > slides.length - 8) {
        slideIndex = 0;
    }
    carouselContainer.style.transform = `translateX(-${slideWidth * slideIndex}px)`;
}

function slidePrev() {
    slideIndex--;
    if (slideIndex < 0) {
        slideIndex = slides.length - 8;
    }
    carouselContainer.style.transform = `translateX(-${slideWidth * slideIndex}px)`;
}

let slideInterval = setInterval(slideNext, 5000);

prevBtn.addEventListener('click', () => {
    clearInterval(slideInterval);
    slidePrev();
});

nextBtn.addEventListener('click', () => {
    clearInterval(slideInterval);
    slideNext();
});

carousel.addEventListener('mouseleave', () => {
    slideInterval = setInterval(slideNext, 5000);
});