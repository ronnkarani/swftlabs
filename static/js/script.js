particlesJS("particles-js", {
  particles: {
    number: {
      value: 100,
      density: {
        enable: true,
        value_area: 1000
      }
    },
    color: {
      value: "#ffffff"
    },
    shape: {
      type: "circle"
    },
    opacity: {
      value: 0.8,
      random: true
    },
    size: {
      value: 2,
      random: true
    },
    line_linked: {
      enable: false
    },
    move: {
      enable: true,
      speed: 0.6,
      direction: "none",
      random: true,
      straight: false,
      bounce: false
    }
  },
  interactivity: {
    events: {
      onhover: { enable: false },
      onclick: { enable: false }
    }
  },
  retina_detect: true
});


document.addEventListener('DOMContentLoaded', () => {
  const userDropdown = document.querySelector('.user-dropdown');
  if (!userDropdown) return;

  const dropdownContent = userDropdown.querySelector('.dropdown-content');
  const arrow = userDropdown.querySelector('.dropdown-arrow'); // arrow element
  const menuToggle = document.getElementById('menu-toggle');

  const toggleDropdown = () => {
    dropdownContent.classList.toggle('active');
    arrow.classList.toggle('rotated');
  };

  // ✅ Only open/close dropdown when arrow is clicked
  arrow.addEventListener('click', (e) => {
    e.stopPropagation();
    toggleDropdown();
  });

  // Keep dropdown open when clicking inside
  dropdownContent.addEventListener('click', (e) => {
    e.stopPropagation();
  });

  // Close dropdown on outside click
  document.addEventListener('click', () => {
    dropdownContent.classList.remove('active');
    arrow.classList.remove('rotated');
  });

  // Close dropdown when mobile menu closes
  if (menuToggle) {
    menuToggle.addEventListener('change', () => {
      if (!menuToggle.checked) {
        dropdownContent.classList.remove('active');
        arrow.classList.remove('rotated');
      }
    });
  }
});
