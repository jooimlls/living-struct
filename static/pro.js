//  const cards = document.querySelectorAll('.card');

//   function showOnScroll() {
//     const triggerBottom = window.innerHeight * 0.85;
//     cards.forEach((card, index) => {
//       const cardTop = card.getBoundingClientRect().top;
//       if (cardTop < triggerBottom) {
//         setTimeout(() => card.classList.add('show'), index * 150); // stagger effect
//       }
//     });
//   }

//   window.addEventListener('scroll', showOnScroll);
//   showOnScroll();

   const track = document.querySelector('.carousel-track');
    const items = document.querySelectorAll('.item');
    const next = document.querySelector('.next');
    const prev = document.querySelector('.prev');

    let index = 0;
    const visibleSlides = 3; // number of visible items at once

    function updateCarousel() {
      track.style.transform = `translateX(-${index * (100 / visibleSlides)}%)`;
    }

    next.addEventListener('click', () => {
      if (index < items.length - visibleSlides) index++;
      else index = 0;
      updateCarousel();
    });

    prev.addEventListener('click', () => {
      if (index > 0) index--;
      else index = items.length - visibleSlides;
      updateCarousel();
    });

    // Auto-slide every 4 seconds
    setInterval(() => {
      if (index < items.length - visibleSlides) index++;
      else index = 0;
      updateCarousel();
    }, 4000);