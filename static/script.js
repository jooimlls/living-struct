
    function openPopup() {
      document.getElementById("popup").style.display = "flex";
    }

    function closePopup() {
      document.getElementById("popup").style.display = "none";
    }

    // Optional: Close popup by clicking outside the box
    window.onclick = function(e) {
      const popup = document.getElementById("popup");
      if (e.target === popup) {
        popup.style.display = "none";
      }
    }
    console.log("Hamburger element:", hamburger); 
    const hamburger = document.querySelector(".hamburger");
    const navbar = document.querySelector(".navbar");

    function toggleMenu() {
      hamburger.classList.toggle("active");
      navbar.classList.toggle("active");
    }

    document.addEventListener("click", (e) => {
      document.querySelectorAll(".dropdown.open").forEach(drop => {
        if (!drop.contains(e.target)) drop.classList.remove("open");
      });
    });
