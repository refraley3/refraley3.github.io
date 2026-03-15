// Simple vanilla JS slideshow for gallery index
(function(){
  function initSlideshow(root){
    var slides = Array.from(root.querySelectorAll('.slide'));
    if(!slides.length) return;
    var prevBtn = root.querySelector('.prev');
    var nextBtn = root.querySelector('.next');
    var dots = Array.from(root.querySelectorAll('.dot'));
    var current = slides.findIndex(s=>s.classList.contains('active'));
    if(current < 0) current = 0;
    var interval = 14000;
    var timer = null;

    function show(index){
      index = (index + slides.length) % slides.length;
      slides.forEach((s,i)=> s.classList.toggle('active', i===index));
      dots.forEach((d,i)=> d.classList.toggle('active', i===index));
      current = index;
    }
    function next(){ show(current+1); }
    function prev(){ show(current-1); }
    function start(){ stop(); timer = setInterval(next, interval); }
    function stop(){ if(timer) { clearInterval(timer); timer = null; } }

    if(nextBtn) nextBtn.addEventListener('click', function(e){ e.preventDefault(); next(); start(); });
    if(prevBtn) prevBtn.addEventListener('click', function(e){ e.preventDefault(); prev(); start(); });
    dots.forEach(function(d){ d.addEventListener('click', function(e){ var idx = Number(this.dataset.index); show(idx); start(); }); });

    root.addEventListener('mouseenter', stop);
    root.addEventListener('mouseleave', start);
    root.addEventListener('focusin', stop);
    root.addEventListener('focusout', start);

    document.addEventListener('keydown', function(e){ if(document.activeElement && (document.activeElement.tagName==='INPUT' || document.activeElement.tagName==='TEXTAREA')) return; if(e.key==='ArrowLeft') { prev(); start(); } else if(e.key==='ArrowRight') { next(); start(); }});

    start();
  }

  document.addEventListener('DOMContentLoaded', function(){
    var roots = document.querySelectorAll('.slideshow');
    roots.forEach(initSlideshow);
  });
})();
