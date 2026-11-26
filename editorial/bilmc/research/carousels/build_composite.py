# Composite article: "An Undergrad's Guide to UG Research". Facts from the author's manuscript, accounts of 13-24 Nov 2026, and publications.md. Run from repo root.
import sys,html
sys.path.insert(0,'editorial/bilmc/research/carousels')
from content import ROWS
e=html.escape
SL='undergrads-guide-to-ug-research'; URL=f'https://medinn.in/before-i-leave-medical-college/research/{SL}'
def li(items): return '<ol>'+''.join(f'<li><b>{e(a)}</b>{e(b)}</li>' for a,b in items)+'</ol>'
P1='/before-i-leave-medical-college/research/how-i-got-into-research'
P2='/before-i-leave-medical-college/research/nutrition-oncology-and-the-ncd-project'
P3='/before-i-leave-medical-college/research/electives-juvenile-justice-oncology-and-nutrition'
rows=''.join(f'<tr class="{"hl" if r[0]=="5" else ""}"><td>{r[0]}</td><td><b>{e(r[1])}</b></td><td>{e(r[2])}</td><td><span class="chip {r[4]}">{r[3]}</span></td></tr>' for r in ROWS)
body=f'''
<h2>Most people do it for the <b>portfolio.</b> I did it for the <b>story.</b></h2>
<p>A lot of people get into undergraduate research to go abroad, write the USMLE, or clear PLAB or AMC. I got into it purely because I loved reading, building on it and building a narrative.</p>
<p>This is the guide I wish I had had: how I got in, the studies I did, what worked, and what I got wrong. It covers a cross-sectional study, a case report, electives, a peer review of an online preprint, and a 25-year retrospective analysis that got into the Journal of the American Heart Association. Each part has its own full article. Here is the whole arc in one place.</p>

<h2>1. How you actually get in: <b>see a problem.</b></h2>
<p>It started before medical college, with a person who believed in me and talked to me about evidence-based medicine, plant-based diets, and how food can fundamentally change healthcare. He gave me books, including <i>How Not to Die</i>. I was skeptical of some of what I saw and read, and that was the first lesson: separate the claim from the data. I decided to repeat for MBBS. Then I joined college and lost track of that spark. Midway in first year he sent me the book he always talked about, and I started thinking about research again.</p>
'''+li([('Observe','A problem you saw, on a ward, in a clinic, on campus.'),('Ask','Turn it into one answerable research question.'),('Review the literature','Search PubMed and Google Scholar, read abstracts, then full texts. Find the gap.'),('Find a guide','If you are inside an institution, a faculty member in the right department who agrees to guide you.')])+f'''
<p><a href="{P1}">Read the full story: Part 1, How do you actually get into research?</a></p>

<h2>2. The cross-sectional study: <b>a mountain of data, no paper.</b></h2>
<p>Dr. Jerin James and I were two hungry undergrads who knew nothing. We studied risk factors for non-communicable diseases among medical students, using the WHO STEPS protocol, and the opportunity came as a health camp run by the College Union, where we would not otherwise have got the data.</p>
'''+li([('Narrow the topic','Who, how, which parent studies and guidelines, which tool.'),('Find a framework','We found the WHO STEPS protocol and built the questionnaire.'),('Write the protocol','It needed anthropometric and biochemical data too.'),('Clear the Institutional Research Committee','Take the corrections, resubmit, wait for clearance.'),('Clear the Institutional Ethics Committee','Printouts, a request, and a meeting.'),('Collect, then analyse','We worked in SPSS, Excel and Google Sheets, and depended on Dr. Ashik to teach us SPSS.')])+f'''
<p>It earned us the KUHS UG Research Award, one of the first from our college. We never published it. We had a guide who had published, but we did not orient the project with them well enough, and we spread ourselves too thin. That study is why we realised we needed a forum to understand research and actually learn the basics, which is the idea behind CMC Analytica.</p>
<p><a href="{P2}">Read the full article: Part 2, How do you do a cross-sectional study?</a></p>

<h2>3. The electives: <b>one posting, several projects.</b></h2>
<p>Our electives were a rare chance to choose a topic. In Community Medicine, our HOD and preceptor let us explore juvenile justice. We obtained permissions from magistrates, attended hearings, spoke to NGOs and social workers, and saw case files through the appropriate channels. We presented it and made a report, but because the data involved children, we chose not to publish. Not everything should be published.</p>
<p>In Medical Oncology, the topic I had once discussed with my professor, nutrition and cancer, came back as the elective topic. We learnt nutritional assessment tools and how to ask patients the right questions, and I saw that nobody was helping patients with their diet, before or after diagnosis. That posting produced a nutritional assessment study and a case report. None of it was a solo effort: my collaborators in Medical Oncology were Dr. Varun, Dr. Punya and Dr. Shadi, with our guide Dr. Sanudev, and in juvenile justice Dr. Varsha, Raniya, Shana and Sreelakshmi S.</p>
<p><a href="{P3}">Read the full article: Part 3, What can one elective do for your research?</a></p>

<h2>4. The case report: <b>fairly easy, if done properly.</b></h2>
<p>There are always rare cases in a big tertiary care hospital. Our guide, Dr. Sanudev, told us about an interesting one. It was mostly retrospective: we took consent from the patient at follow-up, collected the old records, the histopathology slides and the imaging, and had next-generation sequencing done. We reviewed existing cases to show what made ours stand out, and wrote and rewrote. The first submission was rejected. We corrected it, resubmitted, and answered the reviewers one by one. It took almost a year to be published.</p>
'''+li([('Find the case','Through a guide, or on the wards.'),('Get written consent','From the patient, usually at follow-up.'),('Collect what exists','Records, slides, imaging, any tests you add.'),('Follow CARE','The international guideline for case reports. Cite it.'),('Expect rejection','Correct, resubmit, answer every reviewer comment.')])+f'''

<h2>5. The online preprint review: <b>an amusing start.</b></h2>
<p>My first published credit was not a study. It was a peer review of an online preprint, "Artificial Intelligence in Healthcare: 2023 Year in Review", in JMIRx Med, a virtual collaborative live review discussion, in September 2024. It is funny, and it is also a real way in: you learn to read a paper critically, and you get your name on something published.</p>
'''+li([('Reviewing teaches you to read','You see how papers are built, and where they are weak.'),('It is open to undergrads','Look for collaborative or community reviews of preprints.'),('Credit is real','Check how contributors are listed, and cite it accurately.')])+f'''

<h2>6. The 25-year retrospective analysis that got into <b>JAHA.</b></h2>
<p>Before my final-year examinations, a senior who had been doing meta-analyses and systematic reviews started an international forum to guide students around the world. The idea was to work together, remotely, on publicly available datasets and problem statements. Trying to tick every box in the undergraduate research journey, I joined an analysis using the CDC WONDER database.</p>
<p>It was hard. I did not own a laptop, my internet was poor, and I was studying for final-year MBBS examinations. I got the datasets wrong at first, I screwed up the analysis, then did it again, and my co-authors eventually helped me finish it. Midway through my house surgency, the paper was published: <b>"Rising Obesity-Driven Cardiac Mortality Among Young Adults in the United States: A 25-Year Retrospective Analysis (1999 to 2023)"</b>, in the Journal of the American Heart Association, October 2026 (DOI 10.1161/JAHA.126.049462). I am the fourth author, and the analysis used CDC WONDER multiple-cause-of-death data for ages 15 to 44.</p>
'''+li([('Use public data','Open datasets such as CDC WONDER are free to use. Check the source\'s terms and your journal\'s requirements.'),('Work remotely, with a team','Co-authors across the world can fix what you get wrong.'),('Redo it','Wrong datasets and wrong analyses happen. Check, then rerun.'),('Be honest about your role','I am the fourth author on this paper.')])+f'''

<h2>Everything, in one table</h2>
<div class="fig"><div class="card"><table><tr><th>#</th><th>PROJECT</th><th>OUTPUT</th><th>STATUS</th></tr>{rows}</table></div><p class="cap">Every project, and what happened to it. Source: author, ORCID and journal records. Author positions as listed on each paper.</p></div>

<h2>What I wish I had known</h2>
'''+li([('Start from a problem you saw','Then one question, then the literature, then a guide.'),('Orient your guide','Brief them on the plan before you collect, not after.'),('Plan the analysis first','Draw the empty tables, know the software, and plan the paper.'),('Approvals before data','The Institutional Research Committee, then the Institutional Ethics Committee.'),('Find collaborators','Credit them, publicly.'),('Publish what you can','Protect what you must, such as data about children.'),('Expect rejection','Correct, resubmit, answer every comment.'),('Keep the question small','One question beats a mountain of data.')])+'''
<p>Undergraduate research should not just be about collecting publications and certificates. It should be about understanding problems, building a scientific temperament, learning how to question evidence, and finding ways to solve those problems.</p>

<h2>Read the guidelines</h2>
<p>These are summarised in our own words in the series. Use the official documents for anything you submit, and cite them.</p>
<ul class="refs-list">
<li>CARE (case reports): Gagnier JJ, Kienle G, Altman DG, Moher D, Sox H, Riley D; the CARE Group. <i>BMJ Case Rep</i> 2013;2013:bcr2013201554.</li>
<li>STROBE (observational studies): von Elm E, Altman DG, Egger M, Pocock SJ, Gotzsche PC, Vandenbroucke JP. <i>BMJ</i> 2007;335:806-808.</li>
<li>WHO. The WHO STEPwise approach to noncommunicable disease risk factor surveillance (STEPS).</li>
<li>ICMR. National Ethical Guidelines for Biomedical and Health Research Involving Human Participants, 2017.</li>
<li>Our case report: <a href="https://doi.org/10.1055/s-0045-1808241">doi.org/10.1055/s-0045-1808241</a>. Our JAHA paper: <a href="https://doi.org/10.1161/JAHA.126.049462">doi.org/10.1161/JAHA.126.049462</a>. The JMIRx Med review: <a href="https://doi.org/10.2196/65151">doi.org/10.2196/65151</a>.</li></ul>
'''
sub='My experience through cross-sectional studies, case reports, electives, online preprint reviews, and a 25-year retrospective analysis that got into JAHA.'
brief=['Most people do undergraduate research for a portfolio. I did it for the story. This is the whole arc, with a guide beside each step.','Six experiences: a cross-sectional study that earned an award and never published, electives, a case report, an online preprint review, and a 25-year retrospective analysis published in JAHA.','What I wish I had known: orient your guide, plan the analysis first, find collaborators, expect rejection.']
page=f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><meta name="robots" content="noindex">
<title>An Undergrad's Guide to UG Research | Before I Leave Med School · Research</title><meta name="description" content="{e(sub)} Dr. Sidharth Narayanan, CMC Analytica.">
<link rel="canonical" href="{URL}"><meta property="og:title" content="An Undergrad's Guide to UG Research"><meta property="og:description" content="{e(sub)}"><meta property="og:image" content="https://medinn.in/research-guide-og.jpg"><meta property="og:type" content="article"><meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="/medinn-logo.png"><link rel="stylesheet" href="/essays/research.css"><style>.refs-list{{margin:10px 0 0 20px;font-size:17px;line-height:1.5}}.refs-list li{{margin-top:8px}}.body a{{color:#20558A;font-weight:700}}</style></head><body>
<div class="bar"><a href="/before-i-leave-medical-college">&larr; Before I Leave Med School · Research</a><i>THE GUIDE</i></div><div class="ruler"></div>
<div class="wrap"><img src="/essays/img/cmc-analytica-logo.png" alt="CMC Analytica" style="height:76px;margin-top:26px;display:block"><div class="kick">UNDERGRADUATE RESEARCH · THE FULL GUIDE</div>
<h1>An <b>Undergrad's Guide</b> to UG Research</h1><div class="sub">{e(sub)}</div><div class="au">Dr. Sidharth Narayanan <span class="id">iD</span></div><div class="aff">2020 MBBS batch · Calicut Medical College</div>
<div class="pills"><button class="f" id="cite" type="button" data-cite="Narayanan S. An Undergrad's Guide to UG Research. Before I Leave Med School, Research. Medinn, 2026. {URL}">Cite</button><a href="#ledger">The table</a><button id="share" type="button">Share</button></div>
<div class="brief"><h3>IN BRIEF</h3><ul>{''.join(f'<li>{e(x)}</li>' for x in brief)}</ul></div>
<div class="body">{body.replace('<div class="fig">','<div class="fig" id="ledger">')}</div>
<div class="nav"><a href="{P1}">Part 1</a><a href="{P2}">Part 2</a><a href="{P3}">Part 3</a></div>
<div class="foot"><b>CMC Analytica</b> · Calicut Medical College · College Union · 2026–2027 · Published on <a href="/">Medinn</a></div></div>
<script>document.getElementById('cite').onclick=function(){{var t=this.dataset.cite;if(navigator.clipboard){{navigator.clipboard.writeText(t);this.textContent='Citation copied'}}}};document.getElementById('share').onclick=function(){{var u=location.href;if(navigator.share){{navigator.share({{title:document.title,url:u}}).catch(function(){{}})}}else if(navigator.clipboard){{navigator.clipboard.writeText(u);this.textContent='Link copied'}}}};</script></body></html>'''
open(f'before-i-leave-medical-college/research/{SL}.html','w').write(page)
print('composite ok',len(body.split()),'words')
