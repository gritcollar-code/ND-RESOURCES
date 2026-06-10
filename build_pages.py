#!/usr/bin/env python3
"""Generate all subpages for the ND Tobacco Cessation Dashboard.

All pages get a 'last updated' stamp and a printable layout.
Spelling: NDQuits (one word) per ND Health & Human Services convention.
"""
import pathlib, datetime

LAST_UPDATED = "June 10, 2026"

TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>{title} — NDQuits Dashboard</title>
<link rel="stylesheet" href="../styles.css" />
<link rel="stylesheet" href="_shared.css" />
</head>
<body class="subpage">
<header class="topbar">
  <div class="brand">
    <div class="logo">ND</div>
    <div>
      <h1>North Dakota Youth Tobacco &amp; Nicotine Cessation</h1>
      <p class="sub">Clinician One-Stop Shop · NDQuits Youth Treatment Initiative</p>
    </div>
  </div>
  <nav class="tabs">
    <a class="tab" href="../index.html">← Back to Dashboard</a>
  </nav>
</header>
<main>
  <div class="crumb"><a href="../index.html">Dashboard</a> · {section}</div>
  <h1 class="page-title">{title}</h1>
  <p class="lede">{lede}</p>
  <div class="card">
    {body}
  </div>
  <div class="print-row">
    <button class="primary" onclick="window.print()">🖨 Print this page</button>
    <a class="ghost" href="../index.html">◀ Back to Dashboard</a>
  </div>
  <p class="updated">Last updated: {updated} · Verify currency before printing for clinical use.</p>
</main>
<footer><p>NDQuits Youth Treatment Initiative · CEASE Grant · Last updated {updated}</p></footer>
</body>
</html>
"""

PAGES = {
    "screening-script.html": {
        "section": "Treatment Algorithm · Step 1",
        "title": "AAP Screening Script",
        "lede": "Use this brief, age-appropriate script at every health supervision visit for patients age 10 and older.",
        "body": """
<h3>Opening (build rapport)</h3>
<div class="script-block">"Before we wrap up, I ask all my patients a few questions about things that affect their health. Everything you share stays between us unless you're in danger."</div>

<h3>Core screen</h3>
<div class="script-block">"Have you ever tried smoking a cigarette, vaping, using a nicotine pouch like Zyn, or chewing tobacco — even once?"</div>

<h3>If yes — quantify</h3>
<ul>
  <li>"What do you use? (vape, pouch, cigarette, chew, other)"</li>
  <li>"How often — daily, weekly, only at parties?"</li>
  <li>"How much per day? (pods/day, pouches/day, cigarettes/day)"</li>
  <li>"How soon after waking up do you use it?" <em>(time-to-first-use is a strong dependence marker)</em></li>
</ul>

<h3>Readiness</h3>
<div class="script-block">"On a scale of 0–10, how interested are you in cutting down or stopping?"</div>

<div class="callout"><strong>Why it works:</strong> Brief, normalized, confidential. Avoids "lecture mode" and opens the door for follow-up advice and treatment.</div>
"""
    },

    "ehr-template.html": {
        "section": "Treatment Algorithm · Step 1",
        "title": "EHR Template / Dot Phrase",
        "lede": "Drop-in template for Epic, Cerner, and Athena. Covers screening, assessment, plan, and ICD-10 codes.",
        "body": """
<h3>Smart phrase: <code>.youthnicotine</code></h3>
<div class="script-block" style="font-style:normal;font-family:monospace;font-size:13px;">
TOBACCO / NICOTINE / VAPE SCREEN<br/>
Status: *** (never / former / current)<br/>
Product(s): *** (cigarettes / vape / pouch / chew / cigar)<br/>
Frequency: *** per day<br/>
Time to first use: *** min after waking<br/>
Penn State Dependence Index score: *** (/9)<br/>
Readiness to quit (0–10): ***<br/>
Co-use: *** (cannabis / alcohol / none)<br/>
<br/>
Advice given: *** (brief / extended)<br/>
Plan: *** (NRT / counseling / referral / re-screen)<br/>
Referral: *** (NDQuits / MyLifeMyQuit / counselor)<br/>
Follow-up: *** weeks
</div>

<h3>ICD-10 codes</h3>
<table>
<thead><tr><th>Code</th><th>Description</th></tr></thead>
<tbody>
<tr><td>F17.210</td><td>Nicotine dependence, cigarettes, uncomplicated</td></tr>
<tr><td>F17.290</td><td>Nicotine dependence, other tobacco / vape</td></tr>
<tr><td>Z71.6</td><td>Tobacco abuse counseling</td></tr>
<tr><td>Z72.0</td><td>Tobacco use (non-dependent)</td></tr>
</tbody>
</table>

<div class="callout"><strong>Tip:</strong> Ask your EHR team to add a dropdown for "vape" and "pouch" — current SNOMED defaults often miss these. See the <a href="cme-ehr-integration.html">EHR Integration CME module</a> for templated workflows.</div>
"""
    },

    "nrt-translator.html": {
        "section": "Treatment Algorithm · Step 2A",
        "title": "Vape &amp; Pouch → NRT Dose Translator",
        "lede": "Approximate nicotine intake from modern products and match to a starting NRT patch strength.",
        "body": """
<div class="callout"><strong>Simpler alternative:</strong> Use the <a href="penn-state-index.html">Penn State Dependence Index</a> instead — Mayo Clinic's approach skips product-by-product nicotine math.</div>

<h3>Vapes (disposables &amp; pods)</h3>
<table>
<thead><tr><th>Product example</th><th>Nicotine</th><th>Approx mg/day if used daily</th><th>Suggested patch</th></tr></thead>
<tbody>
<tr><td>JUUL pod (5%)</td><td>40 mg/pod</td><td>1 pod/day ≈ 20–25 mg absorbed</td><td>21 mg</td></tr>
<tr><td>Elf Bar BC5000</td><td>5% (50 mg/mL)</td><td>1 bar over ~4 days ≈ 15–20 mg/day</td><td>14–21 mg</td></tr>
<tr><td>Lost Mary OS5000</td><td>5%</td><td>15–20 mg/day</td><td>14–21 mg</td></tr>
<tr><td>Half-pod or light user</td><td>—</td><td>≤ 10 mg/day</td><td>7–14 mg</td></tr>
</tbody>
</table>

<h3>Nicotine pouches</h3>
<table>
<thead><tr><th>Product</th><th>Per pouch</th><th>Daily use</th><th>Suggested patch</th></tr></thead>
<tbody>
<tr><td>Zyn 3 mg</td><td>3 mg (≈ 1 mg absorbed)</td><td>5–8/day</td><td>7–14 mg</td></tr>
<tr><td>Zyn 6 mg</td><td>6 mg (≈ 2 mg absorbed)</td><td>5–8/day</td><td>14–21 mg</td></tr>
<tr><td>On! 4 mg</td><td>4 mg</td><td>10+/day</td><td>21 mg</td></tr>
</tbody>
</table>

<div class="callout"><strong>Add short-acting NRT</strong> (gum 2 mg or lozenge 2 mg) for breakthrough cravings — q1–2h prn, max 20/day.</div>
<p class="muted">Doses for &lt; 18 are off-label per AAP guidance; document shared decision-making and obtain parental consent.</p>
"""
    },

    "penn-state-index.html": {
        "section": "Treatment Algorithm · Step 2A",
        "title": "Penn State Cigarette Dependence Index ⭐ (Mayo Clinic approach)",
        "lede": "A simplified, validated way to dose NRT — no product-by-product nicotine calculations needed.",
        "body": """
<div class="callout"><strong>Why use it?</strong> The Penn State Cigarette Dependence Index (also adapted for non-cigarette products) lets you dose NRT from a single score. Mayo Clinic recommends this approach for clinicians who don't want to track milligrams per pod or pouch.</div>

<h3>The Penn State Dependence Index (0–9)</h3>
<table>
<thead><tr><th>Question</th><th>Points</th></tr></thead>
<tbody>
<tr><td>How soon after waking do you use your first product?</td>
  <td>&lt; 5 min = 3 · 6–30 min = 2 · 31–60 min = 1 · &gt; 60 min = 0</td></tr>
<tr><td>How many cigarettes (or pods / pouches / cans) per day?</td>
  <td>&lt; 5 = 0 · 5–9 = 1 · 10–19 = 2 · 20–29 = 3 · ≥ 30 = 4 (for non-cigarettes, use equivalent units)</td></tr>
<tr><td>Do you wake at night to use?</td><td>Yes = 1 · No = 0</td></tr>
<tr><td>Is it hard to refrain in places where forbidden?</td><td>Yes = 1 · No = 0</td></tr>
</tbody>
</table>

<h3>Dosing from the score</h3>
<table>
<thead><tr><th>Score</th><th>Dependence</th><th>Suggested adult NRT</th></tr></thead>
<tbody>
<tr><td>0–2</td><td>Low</td><td>Patch 7 mg + gum/lozenge 2 mg prn</td></tr>
<tr><td>3–4</td><td>Moderate</td><td>Patch 14 mg + gum/lozenge 2 mg q1–2h prn</td></tr>
<tr><td>5–6</td><td>High</td><td>Patch 21 mg + gum/lozenge 4 mg q1–2h prn</td></tr>
<tr><td>7–9</td><td>Very high</td><td>Patch 21 mg + 7 mg add-on; combination NRT; consider bupropion or varenicline (≥ 18)</td></tr>
</tbody>
</table>

<h3>For &lt; 18 (off-label per AAP)</h3>
<p>Use the same score, but reduce the starting strength by one level and document shared decision-making with parental consent. See <a href="aap-nrt-evidence.html">AAP off-label NRT evidence</a>.</p>

<div class="callout"><strong>References:</strong> Mayo Clinic Nicotine Dependence Center · Foulds J. <em>Penn State Cigarette Dependence Index</em>. <a href="#">CME module on this instrument</a>.</div>
"""
    },

    "mi-prompts.html": {
        "section": "Treatment Algorithm · Step 2A",
        "title": "Motivational Interviewing Prompts",
        "lede": "Short, evidence-based prompts to help youth move along the change cycle without preaching.",
        "body": """
<h3>Open the conversation</h3>
<ul>
  <li>"What do you like about vaping?"</li>
  <li>"What don't you like about it?"</li>
  <li>"If you decided to quit, what would be your biggest reason?"</li>
</ul>

<h3>Importance &amp; confidence rulers</h3>
<div class="script-block">"On a scale of 0–10, how important is it for you to quit?<br/>Why a 6 and not a 3? What would make it an 8?"</div>

<h3>Affirm change talk</h3>
<ul>
  <li>"It sounds like your basketball coach noticing your wind matters to you."</li>
  <li>"You've already cut back from a pod a day to half — that took effort."</li>
</ul>

<h3>Plan</h3>
<div class="script-block">"What's one small step you could try this week?"</div>

<div class="callout"><strong>Avoid:</strong> lecturing, scare tactics, confronting, or arguing for change. Let the patient voice the reasons.</div>
"""
    },

    "family-guide.html": {
        "section": "Treatment Algorithm · Step 3",
        "title": "Family Conversation Guide (Under 14)",
        "lede": "When the household uses tobacco or nicotine, the family is part of the treatment plan. This guide helps frame that conversation.",
        "body": """
<h3>Before the visit</h3>
<ul>
  <li>Confirm who the legal guardian is and who lives in the home.</li>
  <li>Identify other household users — they may need NDQuits referral too.</li>
</ul>

<h3>With the patient (privately first)</h3>
<div class="script-block">"Is it OK if I bring your grandma into this conversation? What would you like her to know — and not know?"</div>

<h3>With the family</h3>
<ul>
  <li>Frame nicotine as an <strong>addiction</strong>, not a behavior problem.</li>
  <li>Acknowledge the household context without shaming.</li>
  <li>Offer NDQuits to <em>every</em> adult user in the home.</li>
  <li>Discuss removing products from accessible locations.</li>
</ul>

<div class="callout"><strong>Policy reminder:</strong> Parental consent is required in ND for pharmacotherapy in patients &lt; 18. If a guardian cannot be reached during the visit, document the attempt and arrange a follow-up call.</div>
"""
    },

    "aap-nrt-evidence.html": {
        "section": "Treatment Algorithm · Step 3",
        "title": "AAP Off-Label NRT Evidence (Ages 14–17)",
        "lede": "Summary of the American Academy of Pediatrics recommendation supporting off-label NRT for adolescents with moderate-to-severe nicotine dependence.",
        "body": """
<h3>The recommendation</h3>
<div class="callout">The AAP suggests that, given the effectiveness of NRT in adults and the severe harms of continued tobacco use, NRT <strong>may be considered off-label</strong> for adolescents who are moderately-to-severely addicted to nicotine and are motivated to quit.</div>

<h3>Selection criteria</h3>
<ul>
  <li>Daily nicotine use (≥ ½ pod/day, ≥ 5 cigarettes/day, or ≥ 5 pouches/day) — or Penn State Index ≥ 4</li>
  <li>Time-to-first-use &lt; 30 min after waking</li>
  <li>Failed behavioral approach OR severe withdrawal</li>
  <li>Readiness to quit ≥ 7/10</li>
  <li>Parental / guardian consent (ND requirement)</li>
</ul>

<h3>Safety</h3>
<ul>
  <li>Combination therapy (patch + short-acting) is safer than continued tobacco/vape use.</li>
  <li>Monitor for skin irritation, sleep disturbance, vivid dreams.</li>
  <li>Avoid bupropion / varenicline in &lt; 18 — not recommended.</li>
</ul>

<p class="muted">Reference: AAP Clinical Practice Guideline (latest update). Document shared decision-making in the chart.</p>
"""
    },

    "adult-rx.html": {
        "section": "Treatment Algorithm · Step 3",
        "title": "Adult Rx Quick Reference (Ages 18–21)",
        "lede": "First-line FDA-approved pharmacotherapy for patients 18 and older.",
        "body": """
<table>
<thead><tr><th>Agent</th><th>Starting dose</th><th>Duration</th><th>Notes</th></tr></thead>
<tbody>
<tr><td>Nicotine patch</td><td>21 mg/day if &gt; 10 cig/day; 14 mg if less</td><td>8–12 weeks, then taper</td><td>Apply to clean dry skin daily; rotate site.</td></tr>
<tr><td>Nicotine gum</td><td>4 mg if &gt; 25 cig/day, else 2 mg q1–2h prn</td><td>8–12 weeks</td><td>Park-and-chew technique.</td></tr>
<tr><td>Nicotine lozenge</td><td>4 mg if first use &lt; 30 min after waking; else 2 mg</td><td>8–12 weeks</td><td>Do not chew or swallow.</td></tr>
<tr><td>Bupropion SR</td><td>150 mg daily × 3 days, then 150 mg BID</td><td>7–12 weeks; can extend</td><td>Avoid seizure history, eating disorders.</td></tr>
<tr><td>Varenicline</td><td>0.5 mg daily × 3d, 0.5 mg BID × 4d, 1 mg BID</td><td>12 weeks; can extend</td><td>Highest single-agent quit rate. Monitor neuropsych.</td></tr>
</tbody>
</table>

<div class="callout"><strong>Combination therapy</strong> (patch + gum/lozenge) is the most effective NRT regimen and is preferred for moderate-to-heavy users.</div>
"""
    },

    "dosing-table.html": {
        "section": "Treatment Algorithm · Step 4",
        "title": "Adult NRT Dosing Table",
        "lede": "Adult dosing reference for choosing the right starting NRT strength and combination. For pediatric (off-label) dosing, see callout below.",
        "body": """
<div class="callout"><strong>⚠ This table is for ADULT patients (≥ 18).</strong><br/>
For patients &lt; 18, doses are off-label — start one strength lower and consult the <a href="aap-nrt-evidence.html">AAP off-label NRT evidence</a> page. The simpler <a href="penn-state-index.html">Penn State Dependence Index</a> approach is preferred when possible.</div>

<h3>Adult — by nicotine load</h3>
<table>
<thead><tr><th>Daily nicotine intake</th><th>Patch</th><th>Add short-acting?</th></tr></thead>
<tbody>
<tr><td>Light (&lt; 10 mg/day)</td><td>7 mg</td><td>Lozenge 2 mg prn</td></tr>
<tr><td>Moderate (10–20 mg/day)</td><td>14 mg</td><td>Gum or lozenge 2 mg q1–2h prn</td></tr>
<tr><td>Heavy (&gt; 20 mg/day)</td><td>21 mg</td><td>Gum or lozenge 4 mg q1–2h prn</td></tr>
<tr><td>Very heavy / pod-a-day vape</td><td>21 mg + consider 7 mg add-on</td><td>Combination NRT</td></tr>
</tbody>
</table>

<h3>Taper schedule (adult)</h3>
<ul>
  <li>Weeks 1–6: starting dose</li>
  <li>Weeks 7–8: step down one level</li>
  <li>Weeks 9–10: step down again</li>
  <li>Week 11+: short-acting only as needed</li>
</ul>

<div class="callout">Re-assess at 2 and 4 weeks. If still craving / using, <strong>increase</strong> dose rather than discontinue.</div>

<div style="margin-top:24px;padding-top:18px;border-top:1px solid #E5DFD2;">
  <a href="../index.html#standing" class="link forward">▶ Go to Printable Standing Order</a>
  &nbsp;<a href="../index.html#algorithm" class="link">◀ Back to Algorithm</a>
</div>
"""
    },

    "counselor-directory.html": {
        "section": "Treatment Algorithm · Step 4",
        "title": "ND Cessation Counselor Directory",
        "lede": "Cessation counselors and behavioral health providers serving North Dakota — minimum patient age listed for each.",
        "body": """
<table>
<thead><tr><th>Provider</th><th>Region</th><th>Min age</th><th>Modality</th><th>Contact</th></tr></thead>
<tbody>
<tr><td>NDQuits</td><td>Statewide</td><td>All ages (routes by age)</td><td>Phone / text</td><td>1-800-QUIT-NOW</td></tr>
<tr><td>MyLifeMyQuit (via NDQuits)</td><td>Statewide</td><td>13–17</td><td>Text / chat</td><td>Text "Start My Quit" to 36072</td></tr>
<tr><td>Fargo Cass Public Health</td><td>Cass County</td><td>All ages</td><td>In-person + tele</td><td>(701) 241-1383</td></tr>
<tr><td>Bismarck-Burleigh Public Health</td><td>Burleigh / Morton</td><td>All ages</td><td>In-person</td><td>(701) 355-1540</td></tr>
<tr><td>Grand Forks Public Health</td><td>Grand Forks</td><td>All ages</td><td>In-person</td><td>(701) 787-8100</td></tr>
<tr><td>First District Health Unit</td><td>Minot / NW ND</td><td>All ages</td><td>In-person + tele</td><td>(701) 852-1376</td></tr>
<tr><td>Custer Health</td><td>S Central ND</td><td>All ages</td><td>In-person</td><td>(701) 667-3370</td></tr>
</tbody>
</table>

<div class="callout">When in doubt, call <strong>NDQuits (1-800-QUIT-NOW)</strong>. They will route the patient to the closest counselor and handle scheduling — and they cover all ages.</div>

<p class="muted">Facility-specific tobacco treatment specialists (CHI, Sanford, Essentia) are intentionally not listed here to keep this directory universally applicable and easy to maintain. Contact your facility's internal directory for in-system referrals.</p>
"""
    },

    "enroll-patient.html": {
        "section": "Treatment Algorithm · Step 4",
        "title": "Enroll a Patient in Digital / Text Support",
        "lede": "Three-step enrollment to free, evidence-based text-message support programs.",
        "body": """
<h3>MyLifeMyQuit (ages 13–17)</h3>
<ol>
  <li>Patient texts <strong>"Start My Quit"</strong> to <strong>36072</strong>.</li>
  <li>Coach replies within minutes; sessions are confidential.</li>
  <li>Free; no insurance needed.</li>
</ol>

<h3>This Is Quitting (vape-specific, ages 13–24)</h3>
<ol>
  <li>Text <strong>"DITCHVAPE"</strong> to <strong>88709</strong>.</li>
  <li>Daily supportive messages tailored to age &amp; quit stage.</li>
</ol>

<h3>SmokefreeTXT for Teens (ages 13+)</h3>
<ol>
  <li>Text <strong>"QUIT"</strong> to <strong>47848</strong>.</li>
  <li>6–8 weeks of structured texts.</li>
</ol>

<div class="callout">Hand the patient a printed card with these short codes before they leave the visit — uptake jumps when enrollment happens in-room.</div>
"""
    },

    "referral-form.html": {
        "section": "Treatment Algorithm · Step 5",
        "title": "Print Referral Form",
        "lede": "Standard one-page referral to NDQuits. Fax to 1-800-483-3114 or eFax through your EHR.",
        "body": """
<table>
<thead><tr><th>Field</th><th>Entry</th></tr></thead>
<tbody>
<tr><td>Patient name</td><td>______________________</td></tr>
<tr><td>DOB</td><td>___ / ___ / ______</td></tr>
<tr><td>Phone</td><td>______________________</td></tr>
<tr><td>Best time to reach</td><td>______________________</td></tr>
<tr><td>Product(s) used</td><td>☐ Cigarette &nbsp; ☐ Vape &nbsp; ☐ Pouch &nbsp; ☐ Chew</td></tr>
<tr><td>Penn State Index score</td><td>____ / 9</td></tr>
<tr><td>Readiness (0–10)</td><td>______</td></tr>
<tr><td>Parent/guardian consent (if &lt; 18)</td><td>______________________</td></tr>
<tr><td>Referring clinician</td><td>______________________</td></tr>
<tr><td>Clinic / NPI</td><td>______________________</td></tr>
<tr><td>Date</td><td>___ / ___ / ______</td></tr>
</tbody>
</table>
"""
    },

    "screening-pathway-print.html": {
        "section": "Treatment Algorithm · Printable",
        "title": "Printable Algorithm + Screening Questions",
        "lede": "A single-page paper reference for clinicians who prefer hard copy. Includes the full pathway and core screening script.",
        "body": """
<h3>Step 1 — Screen (every visit, ages ≥ 10)</h3>
<p><em>"Have you ever tried smoking, vaping, nicotine pouches, or chew?"</em></p>

<h3>Step 2 — Branch</h3>
<table>
<thead><tr><th>Positive screen</th><th>Negative screen</th></tr></thead>
<tbody><tr>
<td>Assess product, frequency, readiness. Score Penn State Index.</td>
<td>Brief positive reinforcement + counsel on vape/pouch risks. Document &amp; re-screen.</td>
</tr></tbody>
</table>

<h3>Step 3 — Age &amp; consent pathway</h3>
<ul>
  <li><strong>Under 14:</strong> Counseling + family-based intervention. Parental consent required for any pharmacotherapy.</li>
  <li><strong>14–17:</strong> Behavioral first; off-label NRT per AAP if dependent + motivated. Parental consent required in ND.</li>
  <li><strong>18–21:</strong> Full NRT, varenicline, bupropion. No parental consent. Refer NDQuits.</li>
</ul>

<h3>Step 4 — Treat</h3>
<ul>
  <li>Pharmacotherapy — dose by Penn State Index or product translator.</li>
  <li>Counseling — ND public health units or NDQuits coaches.</li>
  <li>Digital / text — MyLifeMyQuit, This Is Quitting.</li>
</ul>

<h3>Step 5 — Refer &amp; follow up</h3>
<p><strong>NDQuits: 1-800-QUIT-NOW</strong> · Follow-up in 2–4 weeks · Document plan.</p>

<div class="callout"><strong>⚠ Printed copy?</strong> Check the dashboard for the latest version. This page was last updated """ + LAST_UPDATED + """.</div>
"""
    },

    # ============== CME modules ==============
    "cme-1.html": {
        "section": "CME Module",
        "title": "1. The Landscape — ND youth tobacco &amp; nicotine use",
        "lede": "0.25 AMA PRA Category 1 Credit™ · 3–5 minutes · hybrid AI-avatar format",
        "body": """
<h3>Learning objectives</h3>
<ul>
  <li>Describe the prevalence of tobacco, nicotine, vape, and pouch use among ND youth.</li>
  <li>Identify the products most commonly used today.</li>
  <li>Recognize that approximately two-thirds of youth users <strong>want to quit</strong>.</li>
</ul>

<h3>Key facts</h3>
<ul>
  <li>1 in 5 ND students in grades 9–12 currently uses a tobacco or nicotine product.</li>
  <li>Vapes and nicotine pouches dominate first-use among adolescents.</li>
  <li>Most youth users are interested in quitting but are rarely asked.</li>
</ul>

<div class="callout">After watching, complete the 4-question post-test below to claim your credit.</div>
<button class="primary">Take post-test</button>
"""
    },
    "cme-health-effects.html": {
        "section": "CME Module",
        "title": "2. Health Reasons to Quit — Vape &amp; Novel Product Effects",
        "lede": "0.25 AMA PRA Category 1 Credit™ · 3–5 minutes",
        "body": """
<h3>Learning objectives</h3>
<ul>
  <li>Summarize the cardiopulmonary, neurodevelopmental, and oral health effects of vaping.</li>
  <li>Counter the "vaping is a safer alternative" framing with evidence-based patient language.</li>
  <li>Tailor counseling for adolescent brains and motivations.</li>
</ul>

<h3>Key effects to discuss</h3>
<ul>
  <li><strong>Cardiopulmonary:</strong> EVALI, increased heart rate &amp; BP, reduced exercise tolerance.</li>
  <li><strong>Neurodevelopmental:</strong> adolescent brain still developing — nicotine affects attention, mood, addiction risk.</li>
  <li><strong>Oral:</strong> gum recession, pouch-related lesions.</li>
  <li><strong>Mental health:</strong> bidirectional association with anxiety and depression.</li>
</ul>
<button class="primary">Start module</button>
"""
    },
    "cme-2.html": {
        "section": "CME Module",
        "title": "3. Screening &amp; Brief Intervention",
        "lede": "0.25 AMA PRA Category 1 Credit™ · 3–5 minutes",
        "body": """
<h3>Learning objectives</h3>
<ul>
  <li>Apply the 5 A's / AAR framework in routine visits.</li>
  <li>Use confidential, non-judgmental motivational interviewing prompts.</li>
  <li>Document screening using ICD-10 codes that support billing.</li>
</ul>
<button class="primary">Start module</button>
"""
    },
    "cme-penn-state.html": {
        "section": "CME Module",
        "title": "4. NRT Dosing via the Penn State Dependence Index ⭐",
        "lede": "0.25 AMA PRA Category 1 Credit™ · Mayo Clinic-recommended approach",
        "body": """
<h3>Learning objectives</h3>
<ul>
  <li>Administer the 4-question Penn State Cigarette Dependence Index (adapted for non-cigarettes).</li>
  <li>Translate the resulting score directly to a starting NRT regimen.</li>
  <li>Recognize when to add bupropion / varenicline (adults) or seek behavioral-only care (under 18).</li>
</ul>

<h3>Why this matters</h3>
<p>The Index removes the cognitive load of converting JUUL pods, Elf Bar puffs, or Zyn pouches to mg/day. A single score does the work.</p>

<p>Reference: <a href="penn-state-index.html">Penn State Dependence Index quick page</a>.</p>
<button class="primary">Start module</button>
"""
    },
    "cme-3.html": {
        "section": "CME Module",
        "title": "5. Off-Label NRT for Youth",
        "lede": "0.25 AMA PRA Category 1 Credit™ · 3–5 minutes",
        "body": """
<h3>Learning objectives</h3>
<ul>
  <li>State the AAP recommendation for off-label NRT in adolescents.</li>
  <li>Identify which patients meet criteria.</li>
  <li>Counsel on parental consent and document shared decision-making.</li>
</ul>
<button class="primary">Start module</button>
"""
    },
    "cme-4.html": {
        "section": "CME Module",
        "title": "6. Vape &amp; Pouch Dosing",
        "lede": "0.25 AMA PRA Category 1 Credit™ · 3–5 minutes",
        "body": """
<h3>Learning objectives</h3>
<ul>
  <li>Translate daily vape pod / pouch use into nicotine mg/day.</li>
  <li>Match patient nicotine load to a starting NRT regimen.</li>
</ul>
<button class="primary">Start module</button>
"""
    },
    "cme-adolescent-friendly.html": {
        "section": "CME Module",
        "title": "7. Adolescent-Friendly Services",
        "lede": "0.25 AMA PRA Category 1 Credit™ · 3–5 minutes",
        "body": """
<h3>Learning objectives</h3>
<ul>
  <li>Establish trust and confidentiality with adolescent patients.</li>
  <li>Use developmentally appropriate language without parental presence.</li>
  <li>Document confidential disclosures while complying with mandatory-reporter and consent law.</li>
</ul>

<h3>Practical tips</h3>
<ul>
  <li>Spend the first 5 minutes of every adolescent visit one-on-one.</li>
  <li>State your confidentiality policy <em>before</em> asking sensitive questions.</li>
  <li>Normalize: "I ask everyone these questions — it's not because I think anything is wrong."</li>
</ul>
<button class="primary">Start module</button>
"""
    },
    "cme-ehr-integration.html": {
        "section": "CME Module",
        "title": "8. Systems Change &amp; EHR Integration",
        "lede": "0.5 AMA PRA Category 1 Credits™ · workflow change + templates you can copy",
        "body": """
<h3>Learning objectives</h3>
<ul>
  <li>Build a sustainable team-based screening workflow (MA → clinician → follow-up).</li>
  <li>Implement an EHR dot-phrase, smart-set, or order panel for cessation.</li>
  <li>Track screening rates and quit attempts in a dashboard or registry.</li>
</ul>

<h3>Copy-paste templates from clinics already doing this</h3>
<ul>
  <li><strong>Epic SmartPhrase:</strong> <code>.youthnicotine</code> — see <a href="ehr-template.html">EHR template page</a>.</li>
  <li><strong>MA rooming checklist:</strong> "Vape / nicotine / pouch use in past 30 days?" added to vitals screen.</li>
  <li><strong>Order set:</strong> NRT patch + lozenge bundle linked to ICD-10 F17.290.</li>
</ul>

<h3>Measure what matters</h3>
<ul>
  <li>% of 11–21 yo visits with documented screening</li>
  <li>% of positive screens with brief intervention</li>
  <li>Quit attempts at 3 and 6 months</li>
</ul>
<button class="primary">Start module</button>
"""
    },
    "cme-5.html": {
        "section": "CME Module",
        "title": "9. Referral &amp; Follow-up",
        "lede": "0.25 AMA PRA Category 1 Credit™ · 3–5 minutes",
        "body": """
<h3>Learning objectives</h3>
<ul>
  <li>Use NDQuits as a single-call triage line.</li>
  <li>Build a follow-up workflow that closes the "ask → treat" gap.</li>
</ul>
<button class="primary">Start module</button>
"""
    },
    "cme-6.html": {
        "section": "CME Module",
        "title": "Algorithm Walkthrough — UpToDate-style credit",
        "lede": "+0.25 AMA PRA Category 1 Credit™ · earned by clicking through the algorithm",
        "body": """
<p>Open the <a href="../index.html#algorithm">Treatment Algorithm</a> and step through each node. Credit is awarded after viewing all five steps.</p>
<button class="primary">Launch walkthrough</button>
"""
    },
}

OUT = pathlib.Path(__file__).parent / "pages"
OUT.mkdir(exist_ok=True)

for fname, data in PAGES.items():
    html = TEMPLATE.format(updated=LAST_UPDATED, **data)
    (OUT / fname).write_text(html)
    print(f"wrote {fname}")

print(f"\nGenerated {len(PAGES)} pages in {OUT}")
print(f"Last updated stamp: {LAST_UPDATED}")
