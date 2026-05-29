#!/usr/bin/env python3
"""Generate all subpages for the ND Tobacco Cessation Dashboard."""
import os, pathlib

TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>{title} — ND Cessation Dashboard</title>
<link rel="stylesheet" href="../styles.css" />
<link rel="stylesheet" href="_shared.css" />
</head>
<body class="subpage">
<header class="topbar">
  <div class="brand">
    <div class="logo">ND</div>
    <div>
      <h1>North Dakota Youth Tobacco &amp; Nicotine Cessation</h1>
      <p class="sub">Clinician One-Stop Shop · Advisory Council Aligned Dashboard</p>
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
  <a href="../index.html" class="back-btn">← Back to Dashboard</a>
</main>
<footer><p>Built from Advisory Council meeting · 05/19/2026 · v1.2</p></footer>
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
Readiness to quit (0–10): ***<br/>
Co-use: *** (cannabis / alcohol / none)<br/>
<br/>
Advice given: *** (brief / extended)<br/>
Plan: *** (NRT / counseling / referral / re-screen)<br/>
Referral: *** (ND Quits / MyLifeMyQuit / counselor)<br/>
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

<div class="callout"><strong>Tip:</strong> Ask your EHR team to add a dropdown for "vape" and "pouch" — current SNOMED defaults often miss these.</div>
"""
    },

    "nrt-translator.html": {
        "section": "Treatment Algorithm · Step 2A",
        "title": "Vape & Pouch → NRT Dose Translator",
        "lede": "Approximate nicotine intake from modern products and match to a starting NRT patch strength.",
        "body": """
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
<p class="muted">Doses for youth are off-label per AAP guidance; document shared decision-making and obtain parental consent if &lt; 18.</p>
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
  <li>Identify other household users — they may need quitline referral too.</li>
</ul>

<h3>With the patient (privately first)</h3>
<div class="script-block">"Is it OK if I bring your grandma into this conversation? What would you like her to know — and not know?"</div>

<h3>With the family</h3>
<ul>
  <li>Frame nicotine as an <strong>addiction</strong>, not a behavior problem.</li>
  <li>Acknowledge the household context without shaming.</li>
  <li>Offer the quitline to <em>every</em> adult user in the home.</li>
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
  <li>Daily nicotine use (≥ ½ pod/day, ≥ 5 cigarettes/day, or ≥ 5 pouches/day)</li>
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
        "title": "NRT Dosing Table",
        "lede": "Quick reference for choosing the right starting NRT strength and combination.",
        "body": """
<h3>By nicotine load</h3>
<table>
<thead><tr><th>Daily nicotine intake</th><th>Patch</th><th>Add short-acting?</th></tr></thead>
<tbody>
<tr><td>Light (&lt; 10 mg/day)</td><td>7 mg</td><td>Lozenge 2 mg prn</td></tr>
<tr><td>Moderate (10–20 mg/day)</td><td>14 mg</td><td>Gum or lozenge 2 mg q1–2h prn</td></tr>
<tr><td>Heavy (&gt; 20 mg/day)</td><td>21 mg</td><td>Gum or lozenge 4 mg q1–2h prn</td></tr>
<tr><td>Very heavy / pod-a-day vape</td><td>21 mg + consider 7 mg add-on</td><td>Combination NRT</td></tr>
</tbody>
</table>

<h3>Taper schedule</h3>
<ul>
  <li>Weeks 1–6: starting dose</li>
  <li>Weeks 7–8: step down one level</li>
  <li>Weeks 9–10: step down again</li>
  <li>Week 11+: short-acting only as needed</li>
</ul>

<div class="callout">Re-assess at 2 and 4 weeks. If still craving / using, <strong>increase</strong> dose rather than discontinue.</div>
"""
    },

    "counselor-directory.html": {
        "section": "Treatment Algorithm · Step 4",
        "title": "ND Cessation Counselor Directory",
        "lede": "Cessation counselors and behavioral health providers serving North Dakota.",
        "body": """
<table>
<thead><tr><th>Provider</th><th>Region</th><th>Modality</th><th>Contact</th></tr></thead>
<tbody>
<tr><td>ND Quits Coach Line</td><td>Statewide</td><td>Phone / text</td><td>1-800-QUIT-NOW</td></tr>
<tr><td>National Jewish Health</td><td>Statewide (tele)</td><td>Phone coaching</td><td>via ND Quits</td></tr>
<tr><td>Fargo Cass Public Health</td><td>Cass County</td><td>In-person + tele</td><td>(701) 241-1383</td></tr>
<tr><td>Bismarck-Burleigh Public Health</td><td>Burleigh / Morton</td><td>In-person</td><td>(701) 355-1540</td></tr>
<tr><td>Grand Forks Public Health</td><td>Grand Forks</td><td>In-person</td><td>(701) 787-8100</td></tr>
<tr><td>First District Health Unit</td><td>Minot / NW ND</td><td>In-person + tele</td><td>(701) 852-1376</td></tr>
<tr><td>Custer Health</td><td>S Central ND</td><td>In-person</td><td>(701) 667-3370</td></tr>
</tbody>
</table>

<div class="callout">When in doubt, call <strong>ND Quits (1-800-QUIT-NOW)</strong>. They will route the patient to the closest counselor and handle scheduling.</div>
"""
    },

    "enroll-patient.html": {
        "section": "Treatment Algorithm · Step 4",
        "title": "Enroll a Patient in Digital / Text Support",
        "lede": "Three-step enrollment to free, evidence-based text-message support programs.",
        "body": """
<h3>My Life, My Quit (ages 13–17)</h3>
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

<h3>SmokefreeTXT for Teens</h3>
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
        "lede": "Standard one-page referral to ND Quits. Fax to 1-800-483-3114 or eFax through your EHR.",
        "body": """
<table>
<thead><tr><th>Field</th><th>Entry</th></tr></thead>
<tbody>
<tr><td>Patient name</td><td>______________________</td></tr>
<tr><td>DOB</td><td>___ / ___ / ______</td></tr>
<tr><td>Phone</td><td>______________________</td></tr>
<tr><td>Best time to reach</td><td>______________________</td></tr>
<tr><td>Product(s) used</td><td>☐ Cigarette &nbsp; ☐ Vape &nbsp; ☐ Pouch &nbsp; ☐ Chew</td></tr>
<tr><td>Readiness (0–10)</td><td>______</td></tr>
<tr><td>Parent/guardian consent (if &lt; 18)</td><td>______________________</td></tr>
<tr><td>Referring clinician</td><td>______________________</td></tr>
<tr><td>Clinic / NPI</td><td>______________________</td></tr>
<tr><td>Date</td><td>___ / ___ / ______</td></tr>
</tbody>
</table>
<div style="margin-top:18px;"><button class="primary" onclick="window.print()">Print this form</button></div>
"""
    },

    "cme-1.html": {
        "section": "CME Module",
        "title": "1. The Landscape — ND youth tobacco &amp; nicotine use",
        "lede": "0.25 AMA PRA Category 1 Credit™ · 15 minutes · self-paced",
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

<div class="callout">After reading, complete the 4-question post-test below to claim your credit.</div>
<button class="primary">Take post-test</button>
"""
    },
    "cme-2.html": {
        "section": "CME Module",
        "title": "2. Screening &amp; Brief Intervention",
        "lede": "0.5 AMA PRA Category 1 Credit™ · 30 minutes",
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
    "cme-3.html": {
        "section": "CME Module",
        "title": "3. Off-Label NRT for Youth",
        "lede": "0.5 AMA PRA Category 1 Credit™ · 30 minutes",
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
        "title": "4. Vape &amp; Pouch Dosing",
        "lede": "0.25 AMA PRA Category 1 Credit™ · 15 minutes",
        "body": """
<h3>Learning objectives</h3>
<ul>
  <li>Translate daily vape pod / pouch use into nicotine mg/day.</li>
  <li>Match patient nicotine load to a starting NRT regimen.</li>
</ul>
<button class="primary">Start module</button>
"""
    },
    "cme-5.html": {
        "section": "CME Module",
        "title": "5. Referral &amp; Follow-up",
        "lede": "0.25 AMA PRA Category 1 Credit™ · 15 minutes",
        "body": """
<h3>Learning objectives</h3>
<ul>
  <li>Use ND Quits as a single-call triage line.</li>
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
<p>Open the <a href="../index.html">Treatment Algorithm</a> and step through each node. Credit is awarded after viewing all five steps.</p>
<button class="primary">Launch walkthrough</button>
"""
    },
}

OUT = pathlib.Path(__file__).parent / "pages"
OUT.mkdir(exist_ok=True)

for fname, data in PAGES.items():
    html = TEMPLATE.format(**data)
    (OUT / fname).write_text(html)
    print(f"wrote {fname}")

print(f"\nGenerated {len(PAGES)} pages in {OUT}")
