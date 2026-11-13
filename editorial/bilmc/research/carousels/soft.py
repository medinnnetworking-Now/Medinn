# Soft look (palette 2), insight-first. Builds r01/r02 carousels and the article pages from one content definition.
import html,sys
sys.path.insert(0,'.')
from content import ROWS
e=html.escape
NAV,ACC,RED='#20558A','#2F6FA8','#B3261E'
SER='Before I Leave Med School · Research'
CSS=f'''*{{box-sizing:border-box;margin:0;padding:0}}body{{background:#777}}
.s{{width:1080px;height:1350px;position:relative;overflow:hidden;margin-bottom:24px;display:flex;flex-direction:column;background:#fff;color:#1d2125;font-family:Arial,Helvetica,sans-serif;padding:0 84px}}
.hd{{display:flex;justify-content:space-between;align-items:center;padding:52px 0 18px;border-bottom:1.5px solid #cfd9e6;font-size:20px;letter-spacing:.05em;color:{NAV};font-weight:700}}.hd i{{font-style:normal;font-weight:400;color:#8896a6}}
.kick{{margin-top:60px;color:{ACC};font-size:25px;letter-spacing:.06em;font-weight:700}}
h1{{font-weight:300;font-size:88px;line-height:1.06;margin-top:26px;letter-spacing:-.02em}}h1 b,h2 b{{font-weight:700;color:{NAV}}}
h2{{font-weight:300;font-size:78px;line-height:1.08;margin-top:24px;letter-spacing:-.015em}}
.sub{{font-family:'Times New Roman',Times,serif;font-size:42px;line-height:1.3;margin-top:34px;color:#3a4552}}
.au{{margin-top:36px;font-size:26px;color:#3a4552}}.id{{display:inline-block;width:26px;height:26px;border-radius:50%;background:#A6CE39;color:#fff;font:700 13px/26px Arial;text-align:center;vertical-align:middle;margin-left:6px}}
.pills{{margin-top:auto;margin-bottom:96px;display:flex;gap:14px}}.pills span{{border:1.5px solid #b9c9dc;color:{NAV};padding:12px 26px;border-radius:999px;font-size:24px;font-weight:700}}.pills .f{{background:#e8f0f9;border-color:#e8f0f9}}
.ft{{position:absolute;left:84px;right:84px;bottom:34px;display:flex;justify-content:space-between;font-size:19px;color:#8896a6}}
.p{{font-family:'Times New Roman',Times,serif;font-size:54px;line-height:1.36;margin-top:34px}}.p em{{font-style:normal;background:linear-gradient(transparent 62%,#FFF1B8 62%)}}
.q{{font-family:Arial;font-weight:300;font-size:70px;line-height:1.12;margin-top:40px;letter-spacing:-.015em}}.q b{{font-weight:700;color:{NAV}}}
.steps{{margin-top:44px}}.st{{display:grid;grid-template-columns:100px 1fr;gap:18px;padding:30px 0;border-top:1.5px solid #dde5ef}}.st:last-child{{border-bottom:1.5px solid #dde5ef}}
.st .n{{font-size:56px;font-weight:300;color:{ACC};line-height:1}}.st b{{font-size:40px;color:{NAV}}}.st span{{display:block;font-family:'Times New Roman',Times,serif;font-size:38px;margin-top:6px;color:#3a4552;line-height:1.28}}
.note{{margin-top:30px;font-size:28px;color:{RED};font-weight:700}}.src{{margin-top:20px;font-size:20px;color:#8896a6;letter-spacing:.03em}}
table{{border-collapse:collapse;margin-top:34px;width:100%;font-size:22px}}th{{text-align:left;padding:12px 10px;font-size:18px;letter-spacing:.05em;color:{NAV};background:#eef4fa;border-bottom:2px solid #cfd9e6}}td{{padding:14px 10px;border-bottom:1.5px solid #e3eaf2;vertical-align:top}}tr.hl td{{background:#FFF7D1}}
.chip{{font-weight:700;font-size:16px;padding:4px 12px;border-radius:999px;white-space:nowrap}}.ok{{background:#e1eefa;color:#1f5a8a}}.bad{{background:#fde5e2;color:#9c241b}}.mid{{background:#fff0c4;color:#7a5200}}'''
def hd(art,i,n): return f'<div class="hd"><span>{SER.upper()}</span><i>{art["id"]} · {i}/{n}</i></div>'
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
R01=dict(id='R01',slug='how-i-got-into-research',title='How Do You Choose a Research Question You Will Still Care About in a Year?',short='How I got into research',
 sub='I started from the wrong place, then found my way back.',
 inbrief=['Many students pick a research topic for the portfolio. A question that bothers you is easier to carry than a topic chosen for a CV.','Start from something you saw. Say it as one question. Check whether someone has already answered it.','My own questions started before I joined medical college. I forgot them for a while, and they came back.'],
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
 ('TRY THIS',H2('Before you pick a topic:')+steps([('Write down','What bothered you on the ward this week.'),('Pick one','The one you cannot stop thinking about.'),('Search','Has it been asked? Read before you plan.'),('Then talk','Take the question, not a topic, to a professor.')])+'<div class="note">Next: R02. How to run a cross-sectional study.</div>')])
R02=dict(id='R02',slug='nutrition-oncology-and-the-ncd-project',title='How Do You Run a Cross-Sectional Study on NCD Risk Factors?',short='The NCD project',
 sub='What I learnt doing one in medical college, including what I got wrong.',
 inbrief=['A cross-sectional study is a snapshot. It tells you how common something is, not what caused it.','Use an established framework, such as WHO STEPS, instead of inventing your questions. Write the protocol and get approvals before you collect data.','Plan the analysis before the data. I did not, and it cost me years.'],
 slides=[
 ('UNDERGRADUATE RESEARCH · HOW TO',None),
 ('STEP 1 · THE DESIGN',H2('A cross-sectional study is a <b>snapshot.</b>')+P('You look at a population at <em>one point in time</em>. You measure risk factors and conditions together.')+SNAP+'<div class="p" style="font-size:40px;margin-top:20px">It tells you how common something is. It cannot tell you what caused what.</div>'),
 ('STEP 2 · THE TOOL',H2('Do not invent your questions. <b>Use a framework.</b>')+steps([('Questionnaire','Tobacco, alcohol, diet, physical activity'),('Physical measurements','Height, weight, waist, blood pressure'),('Biochemical tests','Blood glucose, cholesterol')])+'<div class="note">We ran Steps 1 and 2.</div><div class="src">SOURCE: WHO STEPS, the stepwise approach to NCD risk factor surveillance.</div>'),
 ('STEP 3 · THE PROTOCOL',H2('Draft the <b>protocol</b> first.')+steps([('Question and objectives','What exactly are you asking?'),('Design, setting, population','Who, where, and how many?'),('Tools and variables','What will you measure, and how?'),('Analysis plan','Which tables will the paper need?'),('Ethics and consent','Who approves it, and how do you take consent?')])),
 ('STEP 4 · APPROVALS',H2('No data before <b>approval.</b>')+P('Take the protocol to the Institutional Research Committee and the Ethics Committee. We had both before we collected anything.')+P('<em>Approval comes before the first participant, not after the first spreadsheet.</em>')),
 ('STEP 5 · THE ANALYSIS PLAN',H2('Plan the analysis <b>before</b> the data.')+P('Decide your variables, how you will code them, and what the empty tables look like. <em>Draw the tables before you collect a single row.</em>')+P('I did not do this. That is the part of the story that cost me.')),
 ('HOW MINE STARTED',H2('It started on <b>the wards.</b>')+P('In second year I went department by department, ward by ward. I tried to understand why the diet books were always empty, and filled up with renal diets and milk and eggs.')+P('Dr. Asma Rahim and Dr. Ashik Refeek told me to narrow it down.')),
 ('THE OPPORTUNITY',H2('A health camp. <b>Why waste the data?</b>')+P('The then College Union was running a health camp. A lot of tests would be done.')+P('<em>Why not assess the risk factors of all the students on campus?</em> That is how we drafted the WHO STEPS 1 and 2 protocol.')),
 ('WHAT WENT WRONG',H2('We collected first. <b>We understood later.</b>')+P('It took another one and a half years to get into the data, and learn to process it with SPSS and Excel.')+P('That took a lot of my time in the final year, particularly the eighth semester.')),
 ('THE MISTAKE',H2('We spread <b>ourselves too thin.</b>')+P('Too much data. Far too much data. Unsegmented, without the tools or the team to understand it, structure it properly or even publish it.')),
 ('THE OUTCOME',H2('An award, and <b>no paper.</b>')+P('We presented a report at national forums and undergraduate conferences. The project earned me the KUHS UG Research Award.')+table('1')+'<div class="note" style="font-size:26px">I was never able to publish it.</div>'),
 ('DO IT BETTER',H2('If I did it again:')+steps([('One question','Not every risk factor at once.'),('Fewer variables','Only what you will analyse.'),('Analysis plan first','Empty tables before data.'),('A mentor who has published','Before you collect, not after.')])+'<div class="note">Next: R03. How to do research on real patients.</div>')])
def carousel(art):
    n=len(art['slides']);out=''
    for i,(kick,inner) in enumerate(art['slides'],1):
        if inner is None:
            inner=f'<h1>{art["title_html"]}</h1><div class="sub">{e(art["sub"])}</div><div class="au">Sidharth Narayanan, MBBS <span class="id">iD</span></div><div class="pills"><span class="f">Cite</span><span>Save</span><span>Share</span><span>Swipe →</span></div>'
        out+=f'<section class="s" id="s{i}">{hd(art,i,n)}<div class="kick">{kick}</div>{inner}{ft(i,n)}</section>'
    return f'<!doctype html><meta charset="utf-8"><style>{CSS}</style>{out}'
R01['title_html']='How do you choose a <b>research question</b> you will still care about in a year?'
R02['title_html']='How do you run a <b>cross-sectional study</b> on NCD risk factors?'
for a,nm in ((R01,'r01'),(R02,'r02')): open(f'{nm}.html','w').write(carousel(a))
print('ok')
