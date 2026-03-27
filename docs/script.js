/* ΓöÇΓöÇ NAV ΓöÇΓöÇ */
const nav=document.getElementById('nav');
window.addEventListener('scroll',()=>{
  nav.classList.toggle('solid',window.scrollY>50);
  document.getElementById('floatBtn').style.opacity=window.scrollY>300?'1':'0';
});

/* ΓöÇΓöÇ MOBILE MENU ΓöÇΓöÇ */
function toggleMenu(){
  const b=document.getElementById('burger');
  const m=document.getElementById('mob-menu');
  b.classList.toggle('open');
  m.classList.toggle('open');
}
function closeMenu(){
  document.getElementById('burger').classList.remove('open');
  document.getElementById('mob-menu').classList.remove('open');
}

/* ΓöÇΓöÇ EXPERTISE TABS ΓöÇΓöÇ */
function showExp(idx,el){
  document.querySelectorAll('.exp-tab').forEach(t=>t.classList.remove('on'));
  el.classList.add('on');
  document.querySelectorAll('.exp-pane').forEach((p,i)=>p.classList.toggle('on',i===idx));
}

/* ΓöÇΓöÇ SCROLL REVEAL ΓöÇΓöÇ */
const io=new IntersectionObserver(entries=>{
  entries.forEach(e=>{if(e.isIntersecting){e.target.classList.add('v');io.unobserve(e.target);}});
},{threshold:.1});
document.querySelectorAll('.r,.rl,.rr').forEach(el=>io.observe(el));

/* ΓöÇΓöÇ STAT COUNTERS ΓöÇΓöÇ */
function runCounters(){
  document.querySelectorAll('.stat-n[data-target]').forEach(el=>{
    const target=+el.dataset.target;
    let n=0;
    const step=Math.ceil(target/30);
    const int=setInterval(()=>{
      n=Math.min(n+step,target);
      el.innerHTML=n+'<em>+</em>';
      if(n>=target)clearInterval(int);
    },40);
  });
}
const statObs=new IntersectionObserver(entries=>{
  if(entries[0].isIntersecting){runCounters();statObs.disconnect();}
},{threshold:.5});
const statsEl=document.querySelector('.hero-stats');
if(statsEl)statObs.observe(statsEl);

/* ΓöÇΓöÇ CONTACT FORM ΓöÇΓöÇ */
function sendForm(e){
  e.preventDefault();
  const name=document.getElementById('f-name').value.trim();
  const email=document.getElementById('f-email').value.trim();
  const msg=document.getElementById('f-msg').value.trim();
  if(document.getElementById('hp').value)return;
  if(!name||!email||!msg){
    alert('Please fill in the required fields (Name, Email, Message).');return;
  }
  if(!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)){
    alert('Please enter a valid email address.');return;
  }
  const form=document.getElementById('contact-form');
  const ok=document.getElementById('f-ok');
  form.style.display='none';
  ok.style.display='block';
  setTimeout(()=>{
    ok.style.display='none';
    form.style.display='block';
    ['f-name','f-company','f-email','f-phone','f-service','f-msg'].forEach(id=>{
      const el=document.getElementById(id);
      if(el)el.value='';
    });
  },6000);
}