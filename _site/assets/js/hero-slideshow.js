document.addEventListener("DOMContentLoaded", function () {
  const slideshows = document.querySelectorAll(".hero-slideshow");

  slideshows.forEach(function (slideshow) {
    const slides = Array.from(slideshow.querySelectorAll(".hero-slide"));
    if (slides.length <= 1) return;

    const backButton = slideshow.querySelector(".hero-slideshow-back");
    const forwardButton = slideshow.querySelector(".hero-slideshow-forward");
    const reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
    let current = Math.max(0, slides.findIndex(function (slide) {
      return slide.classList.contains("is-active");
    }));
    let timer;

    function showSlide(index) {
      current = (index + slides.length) % slides.length;

      slides.forEach(function (slide, slideIndex) {
        const isActive = slideIndex === current;
        slide.classList.toggle("is-active", isActive);
        slide.setAttribute("aria-hidden", String(!isActive));
      });
    }

    function stopAutoplay() {
      window.clearInterval(timer);
      timer = undefined;
    }

    function startAutoplay() {
      stopAutoplay();
      if (!reduceMotion && !slideshow.matches(":hover") && !slideshow.contains(document.activeElement)) {
        timer = window.setInterval(function () {
          showSlide(current + 1);
        }, 6000);
      }
    }

    function move(direction) {
      showSlide(current + direction);
      startAutoplay();
    }

    backButton.addEventListener("click", function () {
      move(-1);
    });

    forwardButton.addEventListener("click", function () {
      move(1);
    });

    slideshow.addEventListener("keydown", function (event) {
      if (event.key === "ArrowLeft") {
        event.preventDefault();
        move(-1);
      } else if (event.key === "ArrowRight") {
        event.preventDefault();
        move(1);
      }
    });

    slideshow.addEventListener("mouseenter", stopAutoplay);
    slideshow.addEventListener("mouseleave", startAutoplay);
    slideshow.addEventListener("focusin", stopAutoplay);
    slideshow.addEventListener("focusout", function (event) {
      if (!slideshow.contains(event.relatedTarget)) startAutoplay();
    });

    showSlide(current);
    startAutoplay();
  });
});
