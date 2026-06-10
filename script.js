// ============================================================
// ND Youth Tobacco & Nicotine Cessation Dashboard
// Tab nav, keyword search, suggest-a-topic
// ============================================================

// ---------- Tab navigation ----------
const tabs = document.querySelectorAll('.tab');
const panels = document.querySelectorAll('.panel');

function activate(tabName) {
  tabs.forEach(t => t.classList.toggle('active', t.dataset.tab === tabName));
  panels.forEach(p => p.classList.toggle('active', p.id === tabName));
  window.scrollTo({ top: 0, behavior: 'smooth' });
}

tabs.forEach(tab => tab.addEventListener('click', () => activate(tab.dataset.tab)));

document.querySelectorAll('[data-jump]').forEach(el => {
  el.addEventListener('click', (e) => {
    // Allow anchor jumps within the active panel without switching tabs
    const target = el.dataset.jump;
    e.preventDefault();
    activate(target);
  });
});

// ---------- Keyword search (lightweight client-side) ----------
const SEARCH_INDEX = [
  // Algorithm steps (anchor jumps in #algorithm)
  { title: 'Screen at every visit (ages ≥ 10)', tab: 'algorithm', desc: 'Step 1 — opening question for tobacco/nicotine/vape use', keywords: 'screen ask vape tobacco nicotine cigarette pouch chew 10 12 adolescent' },
  { title: 'Positive screen — Assess', tab: 'algorithm', desc: 'Step 2A — product type, frequency, readiness', keywords: 'positive screen assess motivational interview readiness frequency' },
  { title: 'Pathway by age & consent', tab: 'algorithm', desc: 'Step 3 — under 14, 14–17, 18–21', keywords: 'age consent under 14 12 year old 18 21 parental' },
  { title: 'Treat — choose intervention', tab: 'algorithm', desc: 'Step 4 — pharmacotherapy, counseling, digital support', keywords: 'treat treatment NRT patch gum lozenge counseling text' },
  { title: 'Refer & follow up', tab: 'algorithm', desc: 'Step 5 — NDQuits and 2–4 week follow-up', keywords: 'refer follow up NDQuits quitline' },

  // Pages
  { title: 'AAP Screening Script', tab: 'algorithm', href: 'pages/screening-script.html', desc: 'Brief, confidential screening prompts', keywords: 'screening script AAP ask quit confidential' },
  { title: 'EHR Template / Dot Phrase', tab: 'algorithm', href: 'pages/ehr-template.html', desc: 'Smart phrase, ICD-10 codes', keywords: 'EHR Epic Cerner template ICD smart phrase F17 Z71' },
  { title: 'Vape & Pouch → NRT Translator', tab: 'algorithm', href: 'pages/nrt-translator.html', desc: 'JUUL, Elf Bar, Zyn → patch strength', keywords: 'vape pouch JUUL Elf Bar Zyn nicotine pod mg/day translator' },
  { title: 'Penn State Dependence Index ⭐', tab: 'algorithm', href: 'pages/penn-state-index.html', desc: 'Mayo Clinic simplified NRT dosing — no product math', keywords: 'penn state dependence index mayo clinic simplified NRT dosing' },
  { title: 'Motivational Interviewing Prompts', tab: 'algorithm', href: 'pages/mi-prompts.html', desc: 'MI scripts to elicit change talk', keywords: 'motivational interviewing MI change talk rulers' },
  { title: 'Family Conversation Guide', tab: 'algorithm', href: 'pages/family-guide.html', desc: 'For patients under 14 — household tobacco use', keywords: 'family guardian household 12 year old grandparent' },
  { title: 'AAP Off-Label NRT Evidence (14–17)', tab: 'algorithm', href: 'pages/aap-nrt-evidence.html', desc: 'Criteria, safety, parental consent', keywords: 'off-label NRT teen adolescent AAP 14 15 16 17' },
  { title: 'Adult Rx Quick-Reference (18–21)', tab: 'algorithm', href: 'pages/adult-rx.html', desc: 'Patch, gum, lozenge, bupropion, varenicline', keywords: 'adult Rx 18 21 bupropion varenicline' },
  { title: 'Adult NRT Dosing Table', tab: 'algorithm', href: 'pages/dosing-table.html', desc: 'Starting strengths & taper schedule (adult)', keywords: 'adult dosing table NRT patch taper' },
  { title: 'ND Counselor Directory', tab: 'algorithm', href: 'pages/counselor-directory.html', desc: 'Phone numbers & regions', keywords: 'counselor directory public health Fargo Bismarck Grand Forks Minot' },
  { title: 'Enroll in Digital / Text Support', tab: 'algorithm', href: 'pages/enroll-patient.html', desc: 'MyLifeMyQuit, This Is Quitting short codes', keywords: 'enroll digital text MyLifeMyQuit This Is Quitting smokefree' },
  { title: 'Print Referral Form', tab: 'algorithm', href: 'pages/referral-form.html', desc: 'One-page fax referral to NDQuits', keywords: 'referral form fax NDQuits' },
  { title: 'Print Screening Pathway', tab: 'algorithm', href: 'pages/screening-pathway-print.html', desc: 'Printable algorithm + screening questions', keywords: 'print pathway algorithm screening questions paper' },

  // Resources tab
  { title: 'NDQuits — One-Stop Shop', tab: 'resources', desc: '1-800-QUIT-NOW · routes patients automatically', keywords: 'NDQuits one stop shop quitline 1-800-QUIT-NOW' },
  { title: 'MyLifeMyQuit (ages 13–17)', tab: 'resources', desc: 'Text "Start My Quit" to 36072', keywords: 'mylifemyquit text teen youth 13 14 15 16 17' },
  { title: 'This Is Quitting (vape, ages 13–24)', tab: 'resources', desc: 'Text DITCHVAPE to 88709', keywords: 'this is quitting vape truth ditchvape' },
  { title: 'Mayo Clinic NRT Dosing', tab: 'resources', href: 'pages/penn-state-index.html', desc: 'Penn State Index — simplified dosing', keywords: 'mayo clinic penn state index simplified NRT dosing' },

  // CME tab
  { title: 'CME: The Landscape', tab: 'cme', href: 'pages/cme-1.html', desc: '0.25 CME · 15 min', keywords: 'cme landscape prevalence' },
  { title: 'CME: Health Reasons to Quit', tab: 'cme', href: 'pages/cme-health-effects.html', desc: '0.25 CME · health effects of vaping', keywords: 'cme health effects vape vaping reasons quit' },
  { title: 'CME: Screening & Brief Intervention', tab: 'cme', href: 'pages/cme-2.html', desc: '0.25 CME · 5 As / MI', keywords: 'cme screening brief intervention 5 As MI' },
  { title: 'CME: Penn State NRT Dosing ⭐', tab: 'cme', href: 'pages/cme-penn-state.html', desc: '0.25 CME · simplified dependence index', keywords: 'cme penn state dependence index mayo NRT' },
  { title: 'CME: Off-Label NRT for Youth', tab: 'cme', href: 'pages/cme-3.html', desc: '0.25 CME · AAP guidance', keywords: 'cme off-label NRT youth AAP' },
  { title: 'CME: Vape & Pouch Dosing', tab: 'cme', href: 'pages/cme-4.html', desc: '0.25 CME · NRT equivalents', keywords: 'cme vape pouch dosing' },
  { title: 'CME: Adolescent-Friendly Services', tab: 'cme', href: 'pages/cme-adolescent-friendly.html', desc: '0.25 CME · communication & confidentiality', keywords: 'cme adolescent friendly communication confidentiality rapport teen' },
  { title: 'CME: Systems Change & EHR Integration', tab: 'cme', href: 'pages/cme-ehr-integration.html', desc: '0.5 CME · workflow templates', keywords: 'cme ehr systems change workflow integration template' },
  { title: 'CME: Referral & Follow-up', tab: 'cme', href: 'pages/cme-5.html', desc: '0.25 CME · NDQuits triage', keywords: 'cme referral follow-up' },
  { title: 'CME: Algorithm Walkthrough', tab: 'cme', href: 'pages/cme-6.html', desc: '+0.25 CME · UpToDate style', keywords: 'cme algorithm walkthrough' },

  // Standing order
  { title: 'Printable Standing Order', tab: 'standing', desc: 'Pre-filled NRT order, indications, follow-up', keywords: 'standing order print rx patch gum lozenge bupropion varenicline' },
];

const searchBox = document.getElementById('searchBox');
const resultsBox = document.getElementById('searchResults');

function runSearch(q) {
  q = q.trim().toLowerCase();
  if (!q) { resultsBox.classList.remove('show'); return; }
  const hits = SEARCH_INDEX
    .map(item => {
      const hay = (item.title + ' ' + (item.desc || '') + ' ' + (item.keywords || '')).toLowerCase();
      const tokens = q.split(/\s+/);
      const score = tokens.reduce((s, t) => s + (hay.includes(t) ? 1 : 0), 0);
      return { item, score };
    })
    .filter(h => h.score > 0)
    .sort((a, b) => b.score - a.score)
    .slice(0, 8);

  if (!hits.length) {
    resultsBox.innerHTML = '<div class="empty">No matches. Try "vape", "12 year old", "NRT", "EHR"…</div>';
    resultsBox.classList.add('show');
    return;
  }

  resultsBox.innerHTML = hits.map(h => {
    const i = h.item;
    const href = i.href ? i.href : '#' + i.tab;
    return `<a class="res" href="${href}" data-tab="${i.tab}"><strong>${i.title}</strong><small>${i.desc || ''}</small></a>`;
  }).join('');
  resultsBox.classList.add('show');

  // Re-bind clicks to switch tabs for internal results
  resultsBox.querySelectorAll('.res').forEach(el => {
    el.addEventListener('click', (e) => {
      const href = el.getAttribute('href');
      if (href.startsWith('#')) {
        e.preventDefault();
        activate(href.slice(1));
        resultsBox.classList.remove('show');
        searchBox.value = '';
      }
      // else let normal navigation happen
    });
  });
}

if (searchBox) {
  searchBox.addEventListener('input', e => runSearch(e.target.value));
  searchBox.addEventListener('focus', e => { if (e.target.value) runSearch(e.target.value); });
  document.addEventListener('click', (e) => {
    if (!e.target.closest('.search-wrap')) resultsBox.classList.remove('show');
  });
}

// ---------- Suggest a Topic (stored in localStorage) ----------
const SUGGEST_KEY = 'ndq_suggested_topics_v1';

function loadSuggestions() {
  try { return JSON.parse(localStorage.getItem(SUGGEST_KEY) || '[]'); }
  catch (e) { return []; }
}
function saveSuggestions(list) {
  localStorage.setItem(SUGGEST_KEY, JSON.stringify(list));
}
function renderSuggestions() {
  const list = loadSuggestions();
  const box = document.getElementById('suggestList');
  if (!box) return;
  if (!list.length) {
    box.innerHTML = '<div class="muted" style="font-size:12px;padding:6px 0;">No suggestions yet — be the first!</div>';
    return;
  }
  box.innerHTML = list
    .sort((a, b) => b.votes - a.votes)
    .map((s, i) => `<div class="item"><span>${s.text}</span><button class="vote" data-idx="${i}" title="upvote">▲ ${s.votes}</button></div>`)
    .join('');
  box.querySelectorAll('.vote').forEach(b => {
    b.addEventListener('click', () => {
      const list = loadSuggestions();
      const sorted = list.sort((a, b) => b.votes - a.votes);
      const idx = parseInt(b.dataset.idx, 10);
      sorted[idx].votes += 1;
      saveSuggestions(sorted);
      renderSuggestions();
    });
  });
}
function handleSuggest(e) {
  e.preventDefault();
  const input = document.getElementById('suggestInput');
  const txt = input.value.trim();
  if (!txt) return;
  const list = loadSuggestions();
  list.push({ text: txt, votes: 1, ts: Date.now() });
  saveSuggestions(list);
  input.value = '';
  renderSuggestions();
}
window.handleSuggest = handleSuggest;
renderSuggestions();
