document.addEventListener("DOMContentLoaded", function () {
  const slideshows = document.querySelectorAll(".hero-slideshow");

  slideshows.forEach(function (slideshow) {
    const slides = slideshow.querySelectorAll(".hero-slide");
    if (slides.length <= 1) return;

    let current = 0;

    setInterval(function () {
      slides[current].classList.remove("is-active");
      current = (current + 1) % slides.length;
      slides[current].classList.add("is-active");
    }, 6000);
  });
});