# Builds the two article pages (palette 2, notebook look) from content.py and soft.py. Run from repo root.
import sys,html
sys.path.insert(0,'editorial/bilmc/research/carousels')
from content import R01 as C1,R02 as C2,ROWS,SER
import soft
e=html.escape
def li(items): return '<ol>'+''.join(f'<li><b>{e(a)}</b>{e(b)}</li>' for a,b in items)+'</ol>'
HOW={
'R01':'<h2>You see a <b>problem.</b> Then you go after it.</h2><p>Most people get into research for a portfolio, a way to go abroad, write the USMLE, or clear PLAB or AMC. I got into it purely because I loved reading, building on it and building a narrative. That is what keeps you going when the data gets hard.</p><p>So how do you actually get in? Three checks:</p>'+li([('Something you saw','On a ward, in a clinic, on campus.'),('One sentence','If you cannot say it as a question, it is not ready.'),('Check it exists','Has someone already asked it? That is your review of literature.')]),
'R02':'<h2>One patient. Or <b>many.</b></h2><p>A case report tells the detailed story of one patient, usually a rare or unusual case. A cross-sectional study takes a snapshot of a group at one point in time and tells you how common something is. I did both. Here is what worked.</p><h2>Design 1 · <b>Case report</b></h2><p>We see cases every day, and there are always rare cases in wards. Their unique aspects deserve to be covered, presented and published. <em>I believe undergraduates should do this from the very beginning.</em></p>'+li([('Pick the case','Something rare, or something that taught you a lesson.'),('Consent','Take the patient&rsquo;s written consent before you write.'),('Follow a guideline','The CARE (CAse REport) guidelines give you the checklist.'),('Review the literature','What has been reported before, and what is new here?')])+'<p><b>What worked:</b> a case report on a metastatic solitary fibrous tumour of the parapharyngeal region, with review of literature. It took about one and a half years to publish (Indian J Med Paediatr Oncol, April 2025; I was sixth author).</p><h2>Design 2 · <b>Cross-sectional study</b></h2><p>You look at a population at <em>one point in time</em>. It cannot tell you what caused what. Draft the protocol first:</p>'+li([('Question and objectives','What exactly are you asking?'),('Design, setting, population','Who, where, and how many?'),('Tools and variables','What will you measure, and how?'),('Analysis plan','Which tables will the paper need? Draw them before you collect a single row.'),('Approvals and consent','Research and ethics committee, before the first participant.')])+'<p><b>What worked:</b> a narrow question on one patient group, a nutritional assessment of cancer patients (Indian J Med Paediatr Oncol, March 2026; second author). <b>What did not:</b> the campus NCD survey, with far too much data.</p>'}
AFTER={'R01':'<h2>Before you pick a topic</h2>'+li([('Write down','What bothered you on the ward this week.'),('Pick one','The one you cannot stop thinking about.'),('Search','Has it been asked? Read before you plan.'),('Then talk','Take the question, not a topic, to a professor.')])+'<h2>Where this goes</h2><p>The questions led me from public health into products, and slowly into understanding markets and domains. I now enjoy market research, and I am working on AI-enabled dataset creation.</p>',
'R02':'<h2>Why two worked and <b>one did not</b></h2>'+li([('A small question','One patient group, or one patient.'),('A mentor who had published','Guidance before collecting data.'),('A plan for the analysis','Empty tables drawn first.'),('Patience','Both published ones took about a year and a half.')])}
def page(art,C,prev,nxt,refs):
    body=''
    for b in C['body']:
        if isinstance(b,tuple): body+= f'<h2>{e(b[1])}</h2>' if b[0]=='h' else f'<p class="cl">{e(b[1])}</p>'
        else: body+=f'<p>{e(b)}</p>'
    rows=''.join(f'<tr class="{"hl" if r[0]==C["highlight"] else ""}"><td>{r[0]}</td><td><b>{e(r[1])}</b></td><td>{e(r[2])}</td><td><span class="chip {r[4]}">{r[3]}</span></td></tr>' for r in ROWS)
    url=f'https://medinn.in/before-i-leave-medical-college/research/{art["slug"]}'
    cite=f'Narayanan S. {art["title"]} {SER}, {art["id"]}. Medinn, 2026. {url}'
    brief=''.join(f'<li>{e(x)}</li>' for x in art['inbrief'])
    refhtml=''.join(f'<li>{r}</li>' for r in refs)
    return f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><meta name="robots" content="noindex">
<title>{e(art["title"])} | {SER}</title><meta name="description" content="{e(art["sub"])} {e(SER)}, {art["id"]}. Dr. Sidharth Narayanan, House Surgeon, GMC Kozhikode.">
<link rel="canonical" href="{url}"><meta property="og:title" content="{e(art["title"])}"><meta property="og:description" content="{e(art["sub"])}"><meta property="og:image" content="https://medinn.in/research-{art["id"].lower()}-og.jpg"><meta property="og:type" content="article"><meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="/medinn-logo.png"><link rel="stylesheet" href="/essays/research.css"></head><body>
<div class="bar"><a href="/before-i-leave-medical-college">&larr; {SER}</a><i>{art["id"]}</i></div><div class="ruler"></div>
<div class="wrap"><div class="kick">UNDERGRADUATE RESEARCH · HOW TO</div>
<h1>{art["title_html"]}</h1><div class="sub">{e(art["sub"])}</div><div class="au">Sidharth Narayanan, MBBS <span class="id">iD</span></div><div class="aff">Government Medical College, Kozhikode</div>
<div class="pills"><button class="f" id="cite" type="button" data-cite="{e(cite)}">Cite</button><a href="#table1">Table 1</a><button id="share" type="button">Share</button></div>
<div class="brief"><h3>IN BRIEF</h3><ul>{brief}</ul></div>
<div class="body">{HOW[art["id"]]}<h4>MY STORY</h4>{body}{AFTER[art["id"]]}</div>
<div class="fig" id="table1"><h3>TABLE 1 · THE RESEARCH LEDGER</h3><div class="card"><table><tr><th>#</th><th>PROJECT</th><th>OUTPUT</th><th>STATUS</th></tr>{rows}</table></div><p class="cap">Every project, and what happened to it. Source: author, ORCID and journal records. Author positions as listed on each paper.</p></div>
{"<div class=refs><h3>REFERENCES</h3><ol>"+refhtml+"</ol></div>" if refs else ""}
<div class="nav">{prev}{nxt}</div>
<div class="foot"><b>Dr. Sidharth Narayanan</b> · House Surgeon, GMC Kozhikode · Published on <a href="/">Medinn</a></div></div>
<script>document.getElementById('cite').onclick=function(){{var t=this.dataset.cite;if(navigator.clipboard){{navigator.clipboard.writeText(t);this.textContent='Citation copied'}}}};document.getElementById('share').onclick=function(){{var u=location.href;if(navigator.share){{navigator.share({{title:document.title,url:u}}).catch(function(){{}})}}else if(navigator.clipboard){{navigator.clipboard.writeText(u);this.textContent='Link copied'}}}};</script></body></html>'''
p1=page(soft.R01,C1,'<span></span>','<a href="/before-i-leave-medical-college/research/nutrition-oncology-and-the-ncd-project">Next: R02 &rarr;</a>',[])
p2=page(soft.R02,C2,'<a href="/before-i-leave-medical-college/research/how-i-got-into-research">&larr; R01</a>','<span></span>',['World Health Organization. WHO STEPS: the STEPwise approach to noncommunicable disease risk factor surveillance. <a href="https://www.who.int/teams/noncommunicable-diseases/surveillance/systems-tools/steps" rel="noopener" target="_blank">who.int</a>'])
open('before-i-leave-medical-college/research/how-i-got-into-research.html','w').write(p1)
open('before-i-leave-medical-college/research/nutrition-oncology-and-the-ncd-project.html','w').write(p2)
print('pages ok')
