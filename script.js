// ============================================================
// NDQuits Youth Treatment Initiative — Dashboard
// Tab nav · keyword search · suggest-a-topic
// flowchart modal · sample-patient walkthrough · view toggle
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
    const target = el.dataset.jump;
    e.preventDefault();
    activate(target);
  });
});

// ---------- View toggle (List / Flowchart / Sample Patient) ----------
const viewBtns = document.querySelectorAll('.vt[data-view]');
const viewPanes = document.querySelectorAll('.view-pane');

viewBtns.forEach(btn => {
  btn.addEventListener('click', () => {
    const v = btn.dataset.view;
    viewBtns.forEach(b => b.classList.toggle('active', b === btn));
    viewPanes.forEach(p => {
      const match = p.id === 'view-' + v;
      p.classList.toggle('active', match);
      if (match) { p.removeAttribute('hidden'); } else { p.setAttribute('hidden', ''); }
    });
  });
});

// ---------- Flowchart modal ----------
const NODE_INFO = {
  screen: {
    title: 'Step 1 · Screen every visit',
    body: `<p>At every health supervision visit for patients ≥ 10 years old, ask the core screening question:</p>
      <p><em>"Have you ever tried smoking, vaping, nicotine pouches, or chew?"</em></p>
      <p>Time-to-first-use after waking is the strongest dependence marker — always quantify if the answer is yes.</p>`,
    links: [
      ['AAP Screening Script', 'pages/screening-script.html'],
      ['EHR Dot-Phrase', 'pages/ehr-template.html'],
      ['🖨 Print screening questions', 'pages/screening-pathway-print.html']
    ]
  },
  positive: {
    title: 'Step 2A · Positive Screen → Assess',
    body: `<p>Assess product, frequency, readiness, and co-use. Use the <strong>Penn State Dependence Index</strong> to skip product-by-product nicotine math.</p>
      <ul>
        <li>Product type (vape, pouch, cigarette, chew)</li>
        <li>Frequency &amp; nicotine strength</li>
        <li>Readiness to quit (0–10)</li>
        <li>Cannabis / alcohol co-use</li>
      </ul>`,
    links: [
      ['⭐ Penn State Dependence Index', 'pages/penn-state-index.html'],
      ['Vape/Pouch → NRT translator', 'pages/nrt-translator.html'],
      ['MI prompts cheat sheet', 'pages/mi-prompts.html']
    ]
  },
  negative: {
    title: 'Step 2B · Negative Screen → Prevent',
    body: `<p>Brief positive reinforcement, counsel on risks of vape and pouch use, document, and re-screen at the next visit.</p>
      <p>Re-screening matters — early experimentation often becomes daily use between visits.</p>`,
    links: [
      ['🖨 Print prevention talking points', 'pages/screening-pathway-print.html']
    ]
  },
  age: {
    title: 'Step 3 · Age &amp; Consent Pathway',
    body: `<p>The recommended pathway depends on age and parental consent status in ND.</p>
      <ul>
        <li><strong>&lt; 14:</strong> Counseling and family-based intervention. Pharmacotherapy requires parental consent.</li>
        <li><strong>14–17:</strong> Behavioral first; off-label NRT per AAP if dependent and motivated. Parental consent generally required.</li>
        <li><strong>18–21:</strong> Full NRT, varenicline, bupropion. No parental consent needed.</li>
      </ul>`,
    links: []
  },
  'age-under14': {
    title: 'Under 14 — Counseling + family approach',
    body: `<p>Focus on behavioral support and engaging the household. Pharmacotherapy is rarely first-line under 14, and requires parental consent.</p>
      <p>If the household uses nicotine, treat the family as a unit — offer NDQuits to every adult user.</p>`,
    links: [['Family Conversation Guide', 'pages/family-guide.html']]
  },
  'age-14-17': {
    title: '14 – 17 — Off-label NRT eligible',
    body: `<p>Behavioral first. Add off-label NRT per AAP when the patient is moderately-to-severely dependent and motivated.</p>
      <p>Parental / guardian consent is required in ND. Document shared decision-making.</p>`,
    links: [
      ['AAP off-label NRT evidence', 'pages/aap-nrt-evidence.html'],
      ['⭐ Penn State Index', 'pages/penn-state-index.html']
    ]
  },
  'age-18-21': {
    title: '18 – 21 — Full adult Rx options',
    body: `<p>FDA-approved NRT, bupropion, and varenicline all eligible. Combination NRT (patch + short-acting) is the most effective regimen.</p>`,
    links: [
      ['Adult Rx quick-reference', 'pages/adult-rx.html'],
      ['Adult NRT dosing table', 'pages/dosing-table.html']
    ]
  },
  treat: {
    title: 'Step 4 · Treat — Choose intervention',
    body: `<p>Three parallel intervention paths — pick one or combine.</p>
      <ul>
        <li><strong>Pharmacotherapy:</strong> dose by Penn State Index, or by product translator.</li>
        <li><strong>Counseling:</strong> local public-health unit or NDQuits coach.</li>
        <li><strong>Digital / text:</strong> MyLifeMyQuit, This Is Quitting.</li>
      </ul>`,
    links: [
      ['Adult NRT dosing table', 'pages/dosing-table.html'],
      ['Counselor directory', 'pages/counselor-directory.html'],
      ['Enroll patient (text support)', 'pages/enroll-patient.html']
    ]
  },
  refer: {
    title: 'Step 5 · Refer NDQuits + follow up',
    body: `<p>One call covers all youth and adult referrals: <strong>NDQuits 1-800-QUIT-NOW</strong>.</p>
      <p>Schedule a follow-up at 2–4 weeks. Document the plan in the EHR.</p>`,
    links: [
      ['Print referral form', 'pages/referral-form.html'],
      ['Print standing order', '#standing']
    ]
  }
};

const modalOverlay = document.getElementById('modalOverlay');
const modalBody = document.getElementById('modalBody');
const modalClose = document.getElementById('modalClose');

function openModal(key) {
  const data = NODE_INFO[key];
  if (!data) return;
  const linksHtml = data.links.length
    ? `<div class="actions">${data.links.map(([t, u]) => `<a class="link" href="${u}">${t}</a>`).join('')}</div>`
    : '';
  modalBody.innerHTML = `<h3>${data.title}</h3>${data.body}${linksHtml}`;
  modalOverlay.removeAttribute('hidden');
}
function closeModal() {
  modalOverlay.setAttribute('hidden', '');
}
if (modalClose) modalClose.addEventListener('click', closeModal);
if (modalOverlay) modalOverlay.addEventListener('click', (e) => {
  if (e.target === modalOverlay) closeModal();
});
document.addEventListener('keydown', (e) => {
  if (e.key === 'Escape') closeModal();
});

document.querySelectorAll('.node[data-info]').forEach(node => {
  node.addEventListener('click', () => openModal(node.dataset.info));
});

// ---------- Sample patient walkthroughs ----------
const SAMPLE_CASES = {
  case1: {
    name: 'Maya, 12 years old',
    summary: 'Daily Elf Bar vaping (~½ bar/day). Lives with grandparents who also use nicotine. Wants to quit (8/10). Penn State Index: 5.',
    steps: [
      { t: 'Step 1 — Screen', d: 'Maya self-discloses Elf Bar use. Note time-to-first-use and product strength.', w: '✅ Positive screen. She volunteered the information — good rapport.' },
      { t: 'Step 2A — Assess', d: 'Penn State Index = 5 (moderate-high). Readiness 8/10. Co-use: none reported. Household exposure: yes.', w: '🎯 Moderate-to-severe dependence + high motivation = strong cessation candidate.' },
      { t: 'Step 3 — Age pathway: UNDER 14', d: 'Counseling-first pathway. Pharmacotherapy requires parental consent. Maya wants help but no guardian is at the visit.', w: '⚠ Cannot start NRT today. Document parental consent attempt, schedule follow-up call.' },
      { t: 'Step 4 — Treat', d: 'Enroll in <strong>MyLifeMyQuit</strong> (texting program for 13–17, but accepts referrals from clinicians at her age). Offer NDQuits family enrollment for the grandparents.', w: '📱 Hand Maya a printed card with the short code: "Start My Quit" to 36072.' },
      { t: 'Step 5 — Refer + follow up', d: 'Call NDQuits 1-800-QUIT-NOW for the household. Schedule re-check in 2 weeks to reassess and obtain parental consent for NRT if dependence persists.', w: '✅ In this sandbox, no real calls are made.' }
    ],
    finalCallout: 'Maya is a great example of why the under-14 pathway leans on counseling first — and why involving the family changes outcomes.'
  },
  case2: {
    name: 'Jordan, 16 years old',
    summary: '5 Zyn 6 mg pouches/day. First use within 10 min of waking. Readiness 7/10. Penn State Index: 6. Parent reachable today.',
    steps: [
      { t: 'Step 1 — Screen', d: 'Jordan reports Zyn use during the confidential portion of the visit.', w: '✅ Positive screen.' },
      { t: 'Step 2A — Assess', d: 'Penn State Index = 6 (high dependence). Time-to-first-use < 30 min = strong dependence marker. Readiness 7/10.', w: '🎯 Meets AAP off-label NRT criteria.' },
      { t: 'Step 3 — Age pathway: 14–17', d: 'Off-label NRT per AAP is appropriate. Parental consent required in ND.', w: '📞 Parent reachable today — obtain verbal + written consent and document.' },
      { t: 'Step 4 — Treat', d: 'Start nicotine patch <strong>14 mg/day</strong> + lozenge 2 mg prn (Penn State Index 6 → moderate-high regimen, one step down for &lt; 18). Schedule MI counseling.', w: '💊 Off-label use — document shared decision-making in chart.' },
      { t: 'Step 5 — Refer + follow up', d: 'Refer NDQuits for coaching backup. Schedule 2-week and 4-week follow-up. Print the standing order.', w: '🖨 In this sandbox, no real call is placed.' }
    ],
    finalCallout: 'Jordan illustrates the 14–17 pathway: off-label NRT + parental consent + behavioral support, all in one visit.'
  },
  case3: {
    name: 'Alex, 20 years old',
    summary: '1 pack/day cigarettes + 1 JUUL pod/day. Readiness 9/10. Penn State Index: 8. Adult — full Rx options.',
    steps: [
      { t: 'Step 1 — Screen', d: 'Alex discloses dual cigarette and JUUL use during the visit.', w: '✅ Positive screen. Combined cigarette + vape use is common in this age group.' },
      { t: 'Step 2A — Assess', d: 'Penn State Index = 8 (very high). Readiness 9/10. Excellent candidate for aggressive cessation Rx.', w: '🎯 Strong case for combination NRT or varenicline.' },
      { t: 'Step 3 — Age pathway: 18–21', d: 'Adult, no parental consent needed. All FDA-approved Rx available.', w: '✅ Full adult options.' },
      { t: 'Step 4 — Treat', d: 'Start <strong>varenicline</strong> (highest single-agent quit rate) OR combination NRT: patch 21 mg + lozenge 4 mg prn. Counsel on neuropsych monitoring if varenicline.', w: '💊 Discuss preference and side-effect profile.' },
      { t: 'Step 5 — Refer + follow up', d: 'Refer NDQuits coaching. Schedule 1-, 4-, and 12-week follow-up. Print the standing order.', w: '🖨 In this sandbox, no real call is placed.' }
    ],
    finalCallout: 'Alex shows the adult pathway: full Rx options, highest-efficacy agents, and intensive follow-up.'
  }
};

const samplePicker = document.getElementById('samplePicker');
const sampleFlow = document.getElementById('sampleFlow');

if (samplePicker) {
  samplePicker.addEventListener('click', (e) => {
    const card = e.target.closest('.sample-card');
    if (!card) return;
    document.querySelectorAll('.sample-card').forEach(c => c.classList.toggle('active', c === card));
    renderSample(card.dataset.case);
  });
}

function renderSample(key) {
  const c = SAMPLE_CASES[key];
  if (!c) return;
  const html = `
    <h3 style="margin-bottom:6px;">${c.name}</h3>
    <p class="muted" style="margin-bottom:14px;">${c.summary}</p>
    ${c.steps.map(s => `
      <div class="sample-step">
        <h4>${s.t}</h4>
        <p>${s.d}</p>
        <div class="what">${s.w}</div>
      </div>
    `).join('')}
    <div class="sample-warn">${c.finalCallout}</div>
    <button class="sample-reset" onclick="resetSample()">Try another patient ↻</button>
  `;
  sampleFlow.innerHTML = html;
  sampleFlow.removeAttribute('hidden');
}
window.resetSample = function() {
  sampleFlow.setAttribute('hidden', '');
  document.querySelectorAll('.sample-card').forEach(c => c.classList.remove('active'));
  window.scrollTo({ top: 0, behavior: 'smooth' });
};

// ---------- Keyword search (lightweight client-side) ----------
const SEARCH_INDEX = [
  { title: 'Screen at every visit (ages ≥ 10)', tab: 'algorithm', desc: 'Step 1 — opening question for tobacco/nicotine/vape use', keywords: 'screen ask vape tobacco nicotine cigarette pouch chew 10 12 adolescent' },
  { title: 'Positive screen — Assess', tab: 'algorithm', desc: 'Step 2A — product type, frequency, readiness', keywords: 'positive screen assess motivational interview readiness frequency' },
  { title: 'Pathway by age & consent', tab: 'algorithm', desc: 'Step 3 — under 14, 14–17, 18–21', keywords: 'age consent under 14 12 year old 18 21 parental' },
  { title: 'Treat — choose intervention', tab: 'algorithm', desc: 'Step 4 — pharmacotherapy, counseling, digital support', keywords: 'treat treatment NRT patch gum lozenge counseling text' },
  { title: 'Refer & follow up', tab: 'algorithm', desc: 'Step 5 — NDQuits and 2–4 week follow-up', keywords: 'refer follow up NDQuits quitline' },
  { title: 'Try a Sample Patient 🧪', tab: 'algorithm', desc: 'Walk through cases without real calls', keywords: 'sample test fake patient sandbox tutorial example walkthrough' },
  { title: 'Interactive Flowchart 🌳', tab: 'algorithm', desc: 'Visual flowchart — click nodes for details', keywords: 'flowchart flow chart diagram visual' },

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
  { title: 'Print Screening Pathway', tab: 'algorithm', href: 'pages/screening-pathway-print.html', desc: 'Printable algorithm + screening questions', keywords: 'print pathway algorithm screening questions paper printable' },

  { title: 'NDQuits — One-Stop Shop', tab: 'resources', desc: '1-800-QUIT-NOW · routes patients automatically', keywords: 'NDQuits one stop shop quitline 1-800-QUIT-NOW' },
  { title: 'MyLifeMyQuit (ages 13–17)', tab: 'resources', desc: 'Text "Start My Quit" to 36072', keywords: 'mylifemyquit text teen youth 13 14 15 16 17' },
  { title: 'This Is Quitting (vape, ages 13–24)', tab: 'resources', desc: 'Text DITCHVAPE to 88709', keywords: 'this is quitting vape truth ditchvape' },
  { title: 'Mayo Clinic NRT Dosing', tab: 'resources', href: 'pages/penn-state-index.html', desc: 'Penn State Index — simplified dosing', keywords: 'mayo clinic penn state index simplified NRT dosing' },

  { title: 'CME: The Landscape', tab: 'cme', href: 'pages/cme-1.html', desc: '0.25 CME · 3–5 min', keywords: 'cme landscape prevalence' },
  { title: 'CME: Health Reasons to Quit', tab: 'cme', href: 'pages/cme-health-effects.html', desc: '0.25 CME · health effects of vaping', keywords: 'cme health effects vape vaping reasons quit' },
  { title: 'CME: Screening & Brief Intervention', tab: 'cme', href: 'pages/cme-2.html', desc: '0.25 CME · 5 As / MI', keywords: 'cme screening brief intervention 5 As MI' },
  { title: 'CME: Penn State NRT Dosing ⭐', tab: 'cme', href: 'pages/cme-penn-state.html', desc: '0.25 CME · simplified dependence index', keywords: 'cme penn state dependence index mayo NRT' },
  { title: 'CME: Off-Label NRT for Youth', tab: 'cme', href: 'pages/cme-3.html', desc: '0.25 CME · AAP guidance', keywords: 'cme off-label NRT youth AAP' },
  { title: 'CME: Vape & Pouch Dosing', tab: 'cme', href: 'pages/cme-4.html', desc: '0.25 CME · NRT equivalents', keywords: 'cme vape pouch dosing' },
  { title: 'CME: Adolescent-Friendly Services', tab: 'cme', href: 'pages/cme-adolescent-friendly.html', desc: '0.25 CME · communication & confidentiality', keywords: 'cme adolescent friendly communication confidentiality rapport teen' },
  { title: 'CME: Systems Change & EHR Integration', tab: 'cme', href: 'pages/cme-ehr-integration.html', desc: '0.5 CME · workflow templates', keywords: 'cme ehr systems change workflow integration template' },
  { title: 'CME: Referral & Follow-up', tab: 'cme', href: 'pages/cme-5.html', desc: '0.25 CME · NDQuits triage', keywords: 'cme referral follow-up' },
  { title: 'CME: Algorithm Walkthrough', tab: 'cme', href: 'pages/cme-6.html', desc: '+0.25 CME · UpToDate style', keywords: 'cme algorithm walkthrough' },

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

  resultsBox.querySelectorAll('.res').forEach(el => {
    el.addEventListener('click', (e) => {
      const href = el.getAttribute('href');
      if (href.startsWith('#')) {
        e.preventDefault();
        activate(href.slice(1));
        resultsBox.classList.remove('show');
        searchBox.value = '';
      }
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
