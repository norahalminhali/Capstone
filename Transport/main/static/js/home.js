// Animation for stats section on scroll
function animateStatsOnView() {
  const stats = document.querySelectorAll('.stat-box');
  const observer = new IntersectionObserver((entries, observer) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('stat-animate');
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.3 });
  stats.forEach(stat => observer.observe(stat));
}

document.addEventListener('DOMContentLoaded', function() {
  animateStatsOnView();
});

// CSS (add to your CSS file):
// .stat-box { opacity: 0; transform: translateY(40px); transition: all 0.7s cubic-bezier(.4,1.4,.6,1); }
// .stat-box.stat-animate { opacity: 1; transform: translateY(0); }
