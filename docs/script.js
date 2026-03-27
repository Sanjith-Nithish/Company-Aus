// Initialize Icons
lucide.createIcons();

// Mobile Navigation
const mobileBtn = document.querySelector('.mobile-menu-btn');
const navLinks = document.querySelector('.nav-links');

mobileBtn.addEventListener('click', () => {
  const isActive = navLinks.classList.toggle('active');
  const icon = mobileBtn.querySelector('i');
  icon.setAttribute('data-lucide', isActive ? 'x' : 'menu');
  lucide.createIcons();
});

// Close menu on link click
document.querySelectorAll('.nav-links a').forEach(link => {
  link.addEventListener('click', () => {
    navLinks.classList.remove('active');
    mobileBtn.querySelector('i').setAttribute('data-lucide', 'menu');
    lucide.createIcons();
  });
});

// Smooth Scroll Setup
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
  anchor.addEventListener('click', function(e) {
    const targetId = this.getAttribute('href');
    if(targetId === '#') return;
    
    e.preventDefault();
    const targetEl = document.querySelector(targetId);
    if(targetEl) {
      window.scrollTo({
        top: targetEl.getBoundingClientRect().top + window.pageYOffset - 70,
        behavior: 'smooth'
      });
    }
  });
});

// Form Validation
const form = document.getElementById('contactForm');
const statusDiv = document.getElementById('formStatus');

form.addEventListener('submit', (e) => {
  e.preventDefault();
  
  const name = document.getElementById('name').value.trim();
  const email = document.getElementById('email').value.trim();
  const message = document.getElementById('message').value.trim();
  
  statusDiv.className = 'form-status'; // reset
  
  if(!name || !email || !message) {
    showMsg('Please fill in all required fields.', 'error');
    return;
  }
  
  if(!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) {
    showMsg('Please enter a valid email address.', 'error');
    return;
  }
  
  // Successful simulation
  showMsg('Thank you, we’ll be in touch soon.', 'success');
  form.reset();
  setTimeout(() => statusDiv.classList.add('hidden'), 5000);
});

function showMsg(text, type) {
  statusDiv.textContent = text;
  statusDiv.classList.add(type);
  statusDiv.classList.remove('hidden');
}

// Header Scroll Shadow
window.addEventListener('scroll', () => {
  document.querySelector('.header').style.boxShadow = 
    window.scrollY > 50 ? 'var(--shadow-md)' : 'var(--shadow-sm)';
});
