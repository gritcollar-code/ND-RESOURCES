// ---------- Tab navigation ----------
const tabs = document.querySelectorAll('.tab');
const panels = document.querySelectorAll('.panel');

function activate(tabName) {
  tabs.forEach(t => t.classList.toggle('active', t.dataset.tab === tabName));
  panels.forEach(p => p.classList.toggle('active', p.id === tabName));
  window.scrollTo({ top: 0, behavior: 'smooth' });
}

tabs.forEach(tab => tab.addEventListener('click', () => activate(tab.dataset.tab)));

// Internal jump links
document.querySelectorAll('[data-jump]').forEach(el => {
  el.addEventListener('click', (e) => {
    e.preventDefault();
    activate(el.dataset.jump);
  });
});
