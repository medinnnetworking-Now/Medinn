# Soft look (palette 2), insight-first. Builds r01/r02 carousels and the article pages from one content definition.
import html,sys
sys.path.insert(0,'.')
from content import ROWS
e=html.escape
NAV,ACC,RED='#20558A','#2F6FA8','#B3261E'
SER='Before I Leave Med School · Research'
CSS=f'''*{{box-sizing:border-box;margin:0;padding:0}}body{{background:#777}}
.s{{width:1080px;height:1350px;position:relative;overflow:hidden;margin-bottom:24px;display:flex;flex-direction:column;background:#fdfefe;background-image:radial-gradient(circle at 92% 4%,rgba(47,111,168,.16),transparent 36%),repeating-linear-gradient(transparent 0 52px,rgba(47,111,168,.16) 52px 54px);color:#1d2125;font-family:Arial,Helvetica,sans-serif;padding:0 84px}}
.s:before{{content:'';position:absolute;left:62px;top:0;bottom:0;width:2px;background:rgba(224,92,80,.45)}}.s:after{{content:'';position:absolute;left:18px;top:60px;bottom:60px;width:26px;background:radial-gradient(circle,#dbe5f0 0 9px,#b7c7d9 10px 11px,transparent 12px) 0 0/26px 150px repeat-y;pointer-events:none}}
.ruler{{position:relative;height:30px;margin-top:0;background:repeating-linear-gradient(90deg,#7f98b3 0 2px,transparent 2px 19px) bottom/100% 9px no-repeat,repeating-linear-gradient(90deg,#4d6d8f 0 2px,transparent 2px 76px) bottom/100% 17px no-repeat}}.ruler span{{position:absolute;top:0;font-size:11px;color:#6d86a1;font-weight:700}}
.ghost{{position:absolute;right:50px;top:128px;font:700 330px/1 Arial;color:rgba(47,111,168,.05);letter-spacing:-.05em;pointer-events:none}}
.s>*{{position:relative}}.s>.ghost{{position:absolute}}.s>.ft{{position:absolute}}
.hd{{display:flex;justify-content:space-between;align-items:center;padding:52px 0 14px;border-bottom:0;font-size:20px;letter-spacing:.05em;color:{NAV};font-weight:700}}.hd i{{font-style:normal;font-weight:400;color:#8896a6}}
.kick{{margin-top:60px;color:{ACC};font-size:25px;letter-spacing:.06em;font-weight:700}}
h1{{font-weight:300;font-size:88px;line-height:1.06;margin-top:26px;letter-spacing:-.02em}}h1 b,h2 b{{font-weight:700;color:{NAV}}}
h2{{font-weight:300;font-size:78px;line-height:1.08;margin-top:24px;letter-spacing:-.015em}}
.sub{{font-family:'Times New Roman',Times,serif;font-size:42px;line-height:1.3;margin-top:34px;color:#3a4552}}
.au{{margin-top:36px;font-size:26px;color:#3a4552}}.id{{display:inline-block;width:26px;height:26px;border-radius:50%;background:#A6CE39;color:#fff;font:700 13px/26px Arial;text-align:center;vertical-align:middle;margin-left:6px}}
.pills{{margin-top:auto;margin-bottom:96px;display:flex;gap:14px}}.pills span{{border:1.5px solid #b9c9dc;color:{NAV};padding:12px 26px;border-radius:999px;font-size:24px;font-weight:700}}.pills .f{{background:#e8f0f9;border-color:#e8f0f9}}
.ft{{position:absolute;left:84px;right:84px;bottom:34px;display:flex;justify-content:space-between;font-size:19px;color:#8896a6}}
.p{{font-family:'Times New Roman',Times,serif;font-size:54px;line-height:1.36;margin-top:34px}}.p em{{font-style:normal;background:linear-gradient(transparent 58%,#FFEA8A 58%);border-radius:4px;padding:0 4px}}
.q{{font-family:Arial;font-weight:300;font-size:70px;line-height:1.12;margin-top:40px;letter-spacing:-.015em}}.q b{{font-weight:700;color:{NAV}}}
.steps{{margin-top:40px;display:grid;gap:18px}}.st{{display:grid;grid-template-columns:84px 1fr;gap:22px;padding:24px 28px;background:rgba(255,255,255,.92);border:2px solid #d8e4f1;border-radius:26px;box-shadow:0 6px 0 rgba(47,111,168,.08);align-items:center}}
.st .n{{width:72px;height:72px;border-radius:50%;color:#fff;font:700 38px/72px Arial;text-align:center;background:var(--c,#2F6FA8)}}.st:nth-child(1){{--c:#2F6FA8}}.st:nth-child(2){{--c:#1A9A8F}}.st:nth-child(3){{--c:#E8704F}}.st:nth-child(4){{--c:#D9A000}}.st:nth-child(5){{--c:#7B5CC4}}.st b{{font-size:40px;color:{NAV}}}.st span{{display:block;font-family:'Times New Roman',Times,serif;font-size:38px;margin-top:6px;color:#3a4552;line-height:1.28}}
.note{{margin-top:30px;font-size:28px;color:{RED};font-weight:700}}.src{{margin-top:20px;font-size:20px;color:#8896a6;letter-spacing:.03em}}

.big{{display:flex;align-items:flex-end;gap:26px;margin-top:20px}}.big .n{{font:700 190px/0.8 Arial;color:{NAV};letter-spacing:-.06em}}.big .t{{font-size:46px;line-height:1.08;font-weight:300;padding-bottom:14px}}.big .t b{{font-weight:700;color:{NAV}}}
.dots{{display:flex;gap:20px;align-items:center;margin-top:24px}}.dots i{{width:48px;height:48px;border-radius:50%;display:block}}.dots .p{{background:{ACC}}}.dots .u{{border:5px dashed #D9534F;background:#fff}}.dots .g{{border:5px solid #E0A500;background:#fff}}
.leg{{display:flex;gap:30px;font-size:22px;margin-top:12px;color:#3a4552}}.leg b{{color:{NAV}}}
.hookline{{font-family:'Times New Roman',Times,serif;font-size:35px;line-height:1.25;margin-top:20px;color:#2b3440}}
.path{{position:relative;margin-top:36px}}.path:before{{content:'';position:absolute;left:34px;top:30px;bottom:30px;border-left:4px dotted #b9c9dc}}
.pn{{display:grid;grid-template-columns:70px 1fr;gap:26px;align-items:center;padding:15px 0;position:relative}}.pn:nth-child(1) .c{{--c:#2F6FA8}}.pn:nth-child(2) .c{{--c:#1A9A8F}}.pn:nth-child(3) .c{{--c:#E8704F}}.pn:nth-child(4) .c{{--c:#D9A000}}.pn:nth-child(5) .c{{--c:#7B5CC4}}.pn:nth-child(6) .c{{--c:#D9457A}}.pn:nth-child(7) .c{{--c:#2F6FA8}}.pn .c{{width:70px;height:70px;border-radius:50%;background:#fff;border:3px solid var(--c);color:var(--c);font:700 24px/64px Arial;text-align:center}}.pn.on .c{{background:var(--c);color:#fff}}
.pn b{{font-size:37px;color:{NAV};display:block}}.pn span{{font-family:'Times New Roman',Times,serif;font-size:31px;color:#3a4552;display:block;line-height:1.22}}.pn em{{font-style:normal;font-size:20px;font-weight:700;color:{RED};letter-spacing:.05em;margin-left:12px}}
table{{border-collapse:separate;border-spacing:0;margin-top:34px;width:100%;font-size:22px;background:rgba(255,255,255,.95);border:2px solid #d3e1f0;border-radius:24px;overflow:hidden;box-shadow:0 6px 0 rgba(47,111,168,.08)}}th{{text-align:left;padding:14px 12px;font-size:18px;letter-spacing:.05em;color:#fff;background:{NAV}}}td{{padding:14px 10px;border-bottom:1.5px solid #e3eaf2;vertical-align:top}}tr.hl td{{background:#FFF7D1}}
.chip{{font-weight:700;font-size:16px;padding:4px 12px;border-radius:999px;white-space:nowrap}}.gry{{background:#e9edf2;color:#556}}.ok{{background:#e1eefa;color:#1f5a8a}}.bad{{background:#fde5e2;color:#9c241b}}.mid{{background:#fff0c4;color:#7a5200}}'''
def hd(art,i,n): return f'<div class="hd"><span>{SER.upper()}</span><i>{art["id"]} · {i}/{n}</i></div><div class="ruler">'+''.join(f'<span style="left:{k*76+4}px">{k}</span>' for k in range(12))+'</div>'
def ft(i,n): return f'<div class="ft"><span>Dr. Sidharth Narayanan · House Surgeon, GMC Kozhikode</span><span>{i:02d} / {n:02d}</span></div>'
def steps(items,start=1): return '<div class="steps">'+''.join(f'<div class="st"><div class="n">{k}</div><div><b>{e(a)}</b><span>{e(b)}</span></div></div>' for k,(a,b) in enumerate(items,start))+'</div>'
def table(hl):
    rows=''.join(f'<tr class="{"hl" if r[0]==hl else ""}"><td>{r[0]}</td><td><b>{e(r[1])}</b></td><td>{e(r[2])}</td><td><span class="chip {r[4]}">{r[3]}</span></td></tr>' for r in ROWS)
    return f'<table><tr><th>#</th><th>PROJECT</th><th>OUTPUT</th><th>STATUS</th></tr>{rows}</table>'
SNAP=f'''<svg viewBox="0 0 912 300" style="width:100%;margin-top:40px"><line x1="10" y1="250" x2="900" y2="250" stroke="#b9c9dc" stroke-width="3"/><text x="10" y="292" font-size="22" fill="#8896a6" font-family="Arial">TIME</text>
<rect x="400" y="30" width="110" height="210" rx="14" fill="#e8f0f9" stroke="{ACC}" stroke-width="3"/><g fill="{ACC}">'''+''.join(f'<circle cx="{x}" cy="{y}" r="9"/>' for x,y in [(425,85),(462,65),(490,115),(432,145),(470,180),(445,215),(492,205),(418,190)])+f'''</g>
<text x="455" y="22" text-anchor="middle" font-size="24" font-weight="700" fill="{NAV}" font-family="Arial">ONE MOMENT</text><g stroke="#d3dce8" stroke-width="3" stroke-dasharray="3 10"><line x1="400" y1="140" x2="260" y2="140"/><line x1="510" y1="140" x2="650" y2="140"/></g>
<text x="200" y="146" text-anchor="middle" font-size="24" fill="#8896a6" font-family="Arial">before</text><text x="710" y="146" text-anchor="middle" font-size="24" fill="#8896a6" font-family="Arial">after</text></svg>'''
# ---- content: each slide = (kick, inner html) ----
def P(t): return f'<div class="p">{t}</div>'
def H2(t): return f'<h2>{t}</h2>'
R01=dict(id='R01',slug='how-i-got-into-research',title='How Do You Actually Get Into Research?',short='How I got into research',
 sub='You see a problem. Then you go after it. Here is how, step by step.',
 inbrief=['Most people get into research for a portfolio. I got into it purely because I loved reading, building on it and building a narrative.','How you get in: you see a problem. Say it as one question, and check whether someone has already answered it.','My own questions started before I joined medical college. I forgot them for a while. In second year they came back, and eventually led me from research to market research.'],
 slides=[
 ('UNDERGRADUATE RESEARCH · HOW TO',None),
 ('THE USUAL START',H2('Most students start with <b>the portfolio.</b>')+P('A lot of people get into undergraduate research to go abroad, write the USMLE, or clear PLAB or AMC.')+P('<em>That is a reason to start. It is not a reason to keep going.</em>')),
 ('STEP 1 · THE QUESTION',H2('Start from something that <b>bothers you.</b>')+steps([('Something you saw','On a ward, in a clinic, on campus.'),('One sentence','If you cannot say it as a question, it is not ready.'),('Check it exists','Has someone already asked it? That is your review of literature.')])),
 ('MY START',H2('Mine started <b>before medical college.</b>')+P('I studied at PC Thomas Classes. Just before my drop year, an individual who believed in me quite a lot told me about whole-food, plant-based diets and veganism.')+P('He talked to me about Dr. Michael Greger, Neal Barnard, and the Physicians Committee for Responsible Medicine.')),
 ('MY START',H2('I was <b>skeptical,</b> yet I listened.')+P('He showed me Cowspiracy and Seaspiracy. A lot of it, in several instances, did not have solid scientific data behind it.')+P('But whole-food, plant-based diets did have substance to them. <em>I kept that close to my heart.</em>')),
 ('THE CROSSROADS',H2('I had <b>enough</b> of NEET UG.')+P('After my first attempt, I had enough marks for veterinary medicine or BDS, and I had decided to take whatever I got.')+P('But what he told me about preventive medicine and nutrition got me thinking. I told my mom and dad that I wanted to give it another go.')),
 ('THEN I FORGOT',H2('I joined college and <b>let it go.</b>')+P('I was consumed by the need to fit in, to be validated, to be understood. I discussed these ideas, and was ridiculed for a while.')+P('COVID twice. Politics, arts, college dynamics. I forgot all the whys and hows of why I got there.')),
 ('LOOKING BACK',H2('The atmosphere did not foster <b>academic thinking.</b>')+P('When I look back, the overall atmosphere did not foster much academic thinking or even discourse.')+P('But all those decisions led me to where I am right now.')),
 ('THE QUESTIONS CAME BACK',H2('In second year, I <b>took a few steps back.</b>')+P('I reanalysed what I might have always wanted to do, and I started going department by department, ward by ward.')+P('<em>That is where R02 starts.</em>')),
 ('TRY THIS',H2('Before you pick a topic:')+steps([('Write down','What bothered you on the ward this week.'),('Pick one','The one you cannot stop thinking about.'),('Search','Has it been asked? Read before you plan.'),('Then talk','Take the question, not a topic, to a professor.')])+'<div class="note">Next: R02. Case reports and cross-sectional studies.</div>')])
R02=dict(id='R02',slug='nutrition-oncology-and-the-ncd-project',title='How Do You Do Case Reports and Cross-Sectional Studies? What Worked.',short='Case reports and cross-sectional studies',
 sub='Two study designs I used in medical college. One paper took a case on the ward. One took a survey. Here is what worked, and what did not.',
 inbrief=['A case report tells the detailed story of one patient. A cross-sectional study takes a snapshot of many people at one point in time.','What worked: a rare case seen on the ward, and a focused question on one patient group. What did not: a campus-wide survey with far too much data.','Plan the analysis before you collect, and keep the question small.'],
 slides=[
 ('UNDERGRADUATE RESEARCH · HOW TO',None),
 ('TWO DESIGNS',H2('One patient. Or <b>many.</b>')+steps([('Case report','The detailed story of one patient, usually a rare or unusual case.'),('Cross-sectional study','A snapshot of a group at one point in time. How common is it?')])+'<div class="note">I did both. Here is what worked, and what did not.</div>'),
 ('DESIGN 1 · CASE REPORT',H2('Start with a case <b>on the ward.</b>')+P('We see cases every day. There are always rare cases in wards. These cases have unique aspects that need to be covered, presented in forums and published.')+P('<em>I believe undergraduates should do this from the very beginning.</em>')),
 ('CASE REPORT · HOW',H2('How a case report <b>comes together.</b>')+steps([('Pick the case','Something rare, or something that taught you a lesson.'),('Consent','Take the patient\u2019s written consent before you write.'),('Follow a guideline','The CARE guidelines give you the checklist.'),('Review the literature','What has been reported before, and what is new here?')])+'<div class="src">SOURCE: CARE (CAse REport) reporting guidelines, care-statement.org</div>'),
 ('WHAT WORKED · CASE REPORT',H2('A metastatic solitary fibrous tumour, <b>published.</b>')+P('We worked on a case report on a metastatic solid tumour with a review of literature. It took about one and a half years to get published.')+'<div class="note">Indian J Med Paediatr Oncol, Apr 2025. I was sixth author.</div>'),
 ('DESIGN 2 · CROSS-SECTIONAL',H2('A cross-sectional study is a <b>snapshot.</b>')+P('You look at a population at <em>one point in time</em>. It tells you how common something is. It cannot tell you what caused what.')+SNAP),
 ('CROSS-SECTIONAL · HOW',H2('Draft the <b>protocol</b> first.')+steps([('Question and objectives','What exactly are you asking?'),('Design, setting, population','Who, where, and how many?'),('Tools and variables','What will you measure, and how?'),('Analysis plan','Which tables will the paper need?'),('Approvals and consent','Research and ethics committee, before the first participant.')])),
 ('WHAT WORKED · CROSS-SECTIONAL',H2('A narrow question on <b>one patient group.</b>')+P('The nutrition question I carried from second year became a nutritional assessment of cancer patients. Dr. Asma Rahim and Dr. Ashik Refeek told me to narrow it down. It took almost one and a half years to publish.')+'<div class="note">Indian J Med Paediatr Oncol, Mar 2026. Second author.</div>'),
 ('WHAT DID NOT WORK',H2('We collected first. <b>We understood later.</b>')+P('The campus NCD survey used WHO STEPS 1 and 2. We had approvals. But it took another one and a half years to get into the data.')+P('Too much data. Unsegmented, without the tools or the team to structure it or publish it.')),
 ('THE OUTCOME',H2('An award, and <b>no paper.</b>')+'<div class="p" style="font-size:38px;margin-top:16px">The NCD project earned me the KUHS UG Research Award, one of the first from my college. I was never able to publish it.</div>'+table('1').replace('<table>','<table style="margin-top:14px;font-size:16.5px">')),
 ('WHAT WORKED, IN ONE LIST',H2('Why two worked and <b>one did not:</b>')+steps([('A small question','One patient group, or one patient.'),('A mentor who had published','Guidance before collecting data.'),('A plan for the analysis','Empty tables drawn first.'),('Patience','Both published ones took about a year and a half.')])+'<div class="note">Next: R03. Research on real patients.</div>')])
HOOK1="""<div class="kick" style="margin-top:24px">UNDERGRADUATE RESEARCH · A DATA STORY</div><div class="big"><div class="n">8</div><div class="t">research projects<br><b>so far.</b></div></div>
<div class="dots"><i class="p"></i><i class="p"></i><i class="p"></i><i class="p"></i><i class="u"></i><i class="u"></i><i class="g"></i><i class="g"></i></div><div class="leg"><span><b>4</b> published</span><span><b style="color:#B3261E">2</b> never were</span><span><b style="color:#9a6b00">2</b> in progress</span></div>
<div class="hookline">Most people get into research for a portfolio. I got into it purely because I loved reading, building on it and building a narrative.</div>"""+table('1').replace('<table>','<table style="margin-top:14px;font-size:16.5px">')
JOURNEY='<h2 style="font-size:68px">Step by step. <b>Seven articles.</b></h2>'+'<div class="p" style="font-size:34px;margin-top:14px">Why I got into research, every project so far, and what you could learn from me. Today: AI-enabled datasets, and market research.</div><div class="path">'+''.join(f'<div class="pn {"on" if i==0 else ""}"><div class="c">R0{i+1}</div><div><b>{a}{"<em>YOU ARE HERE</em>" if i==0 else ""}</b><span>{b}</span></div></div>' for i,(a,b) in enumerate([('Why I got into research','Choose a question you will still care about'),('What worked','Case reports and cross-sectional studies'),('The electives','Research on real patients'),('From research to innovation','How I moved into markets and domains'),('Meta-analysis and more','Other formats, and getting them published'),('Bio-entrepreneurship','Where research can lead'),('The undergraduate guide','What I wish I had known')]))+'</div>'
R01['slides']=[('HOOK',HOOK1),('THE JOURNEY',JOURNEY)]+R01['slides']
def carousel(art):
    n=len(art['slides']);out=''
    for i,(kick,inner) in enumerate(art['slides'],1):
        if inner is None:
            inner=f'<h1>{art["title_html"]}</h1><div class="sub">{e(art["sub"])}</div><div class="au">Sidharth Narayanan, MBBS <span class="id">iD</span></div><div class="pills"><span class="f">Cite</span><span>Save</span><span>Share</span><span>Swipe →</span></div>'
        kk='' if kick in ('HOOK',) else f'<div class="kick">{kick}</div>'
        out+=f'<section class="s" id="s{i}">'+('' if kick=="HOOK" else f'<div class="ghost">{i:02d}</div>')+f'{hd(art,i,n)}{kk}{inner}{ft(i,n)}</section>'
    return f'<!doctype html><meta charset="utf-8"><style>{CSS}</style>{out}'
R01['title_html']='How do you <b>actually</b> get into research?'
R02['title_html']='How do you do <b>case reports</b> &amp; <b>cross-sectional</b> studies? <b>What worked.</b>'
for a,nm in ((R01,'r01'),(R02,'r02')): open(f'{nm}.html','w').write(carousel(a))
print('ok')
