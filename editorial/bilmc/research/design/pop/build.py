# Three bold directions for the Research series: hook (8 projects) + lesson (R01 "You see a problem") in each. Facts from ../../content.py only.
import sys,html
sys.path.insert(0,'../../carousels')
from content import ROWS
e=html.escape
T=[(r[0],r[1],r[2],r[3],r[4]) for r in ROWS]
SHORT={'1':'WHO STEPS 1&2 NCD risk-factor survey','2':'Nutritional assessment of cancer patients','3':'Metastatic solitary fibrous tumour, parapharyngeal','4':'Juvenile justice and recidivism','5':'Obesity-driven cardiac mortality, US 15 to 44','6':'Retrosternal goitre case series','7':'AI-enabled dataset creation','8':'Peer review: AI in Healthcare 2023 (preprint)'}
JR={'1':'KUHS UG Research Award','2':'Indian J Med Paediatr Oncol · 2026','3':'Indian J Med Paediatr Oncol · 2025','4':'Report + forums · elective','5':'JAHA · Oct 2026','6':'Ongoing','7':'Working on it now','8':'JMIRx Med · Sep 2024'}
css='''@font-face{font-family:Bricolage;src:url(../../../../../bricolage.woff2);font-weight:200 800}@font-face{font-family:Mono;src:url(../../../../../essays/fonts/mono-normal.woff2)}
*{box-sizing:border-box;margin:0;padding:0}body{background:#555}.s{width:1080px;height:1350px;position:relative;overflow:hidden;margin-bottom:24px;display:flex;flex-direction:column;font-family:Arial,Helvetica,sans-serif}
'''
# ================= V1: NEON PUBMED (cyberpunk search results) =================
css+='''.v1{background:#070B1A;color:#E8F4FF;padding:56px 70px;background-image:radial-gradient(circle at 12% 8%,rgba(0,229,255,.28),transparent 40%),radial-gradient(circle at 92% 96%,rgba(255,43,214,.26),transparent 42%),repeating-linear-gradient(transparent 0 3px,rgba(0,229,255,.045) 3px 4px)}
.v1 .top{display:flex;justify-content:space-between;font:400 20px Mono,monospace;letter-spacing:.08em;color:#00E5FF}.v1 .search{margin-top:26px;display:flex;border:2px solid #00E5FF;border-radius:16px;box-shadow:0 0 24px rgba(0,229,255,.45),inset 0 0 18px rgba(0,229,255,.15);overflow:hidden}
.v1 .search div{flex:1;padding:20px 24px;font:400 25px Mono,monospace;color:#E8F4FF}.v1 .search b{background:#FF2BD6;color:#fff;padding:20px 30px;font:700 24px Arial;letter-spacing:.06em;box-shadow:0 0 24px rgba(255,43,214,.7)}
.v1 .res{margin-top:34px;font:800 150px/0.9 Bricolage,Arial;letter-spacing:-.04em;color:#fff;text-shadow:5px 0 #FF2BD6,-5px 0 #00E5FF}.v1 .res small{font:700 38px Arial;letter-spacing:.02em;color:#00E5FF;text-shadow:none;margin-left:20px}
.v1 .sub{font:400 27px/1.3 Mono,monospace;color:#9fb7d4;margin-top:14px}
.v1 .card{display:grid;grid-template-columns:54px 1fr auto;gap:16px;align-items:center;margin-top:12px;padding:12px 18px;border:1.5px solid rgba(0,229,255,.35);border-radius:14px;background:rgba(10,20,45,.78)}.v1 .card .n{font:700 28px Mono,monospace;color:#00E5FF}.v1 .card b{font-size:23px;line-height:1.15;color:#fff;display:block}.v1 .card span{font:400 17px Mono,monospace;color:#9fb7d4}
.v1 .tag{font:700 16px Mono,monospace;padding:6px 12px;border-radius:999px;letter-spacing:.05em}.v1 .ok{color:#00E5FF;border:1.5px solid #00E5FF;box-shadow:0 0 12px rgba(0,229,255,.6)}.v1 .bad{color:#FF4D6D;border:1.5px dashed #FF4D6D}.v1 .mid{color:#FFD60A;border:1.5px solid #FFD60A}
.v1 .ft{margin-top:auto;font:400 18px Mono,monospace;color:#6f87a6;display:flex;justify-content:space-between}
.v1 h1{font:800 104px/0.98 Bricolage,Arial;letter-spacing:-.03em;margin-top:34px;text-shadow:4px 0 #FF2BD6,-4px 0 #00E5FF}.v1 h1 em{font-style:normal;color:#FFD60A;text-shadow:3px 0 #FF2BD6}
.v1 .lvl{font:700 24px Mono,monospace;color:#FF2BD6;letter-spacing:.12em;margin-top:30px}
.v1 .q{display:grid;grid-template-columns:78px 1fr;gap:20px;align-items:center;margin-top:22px;padding:24px 26px;border-radius:20px;background:rgba(10,20,45,.82);border:2px solid var(--c);box-shadow:0 0 22px var(--c2)}.v1 .q i{font:800 60px Bricolage;font-style:normal;color:var(--c)}.v1 .q b{font:700 38px Arial;display:block;color:#fff}.v1 .q span{font:400 25px/1.3 Mono,monospace;color:#9fb7d4;display:block;margin-top:6px}
.v1 .bar{margin-top:30px;height:22px;border-radius:99px;border:2px solid #00E5FF;overflow:hidden}.v1 .bar div{width:14%;height:100%;background:linear-gradient(90deg,#00E5FF,#FF2BD6);box-shadow:0 0 16px #00E5FF}'''
def v1_hook():
    cards=''.join(f'<div class="card"><div class="n">{r[0]}</div><div><b>{e(SHORT[r[0]])}</b><span>{e(JR[r[0]])}</span></div><div class="tag {r[4]}">{r[3]}</div></div>' for r in T)
    return f'''<section class="s v1"><div class="top"><span>MEDINN://RESEARCH_LEDGER</span><span>R01 · 1/12</span></div>
<div class="search"><div>undergraduate research AND narayanan s[Author]</div><b>SEARCH</b></div>
<div class="res">8<small>results</small></div><div class="sub">Most people get into research for a portfolio. I got into it for the narrative.</div>{cards}
<div class="ft"><span>Dr. Sidharth Narayanan · House Surgeon, GMC Kozhikode</span><span>01 / 12</span></div></section>'''
def v1_lesson():
    q=lambda n,t,d,c,c2:f'<div class="q" style="--c:{c};--c2:{c2}"><i>{n}</i><div><b>{t}</b><span>{d}</span></div></div>'
    return f'''<section class="s v1"><div class="top"><span>MEDINN://LESSON_01</span><span>R01 · 3/12</span></div><div class="lvl">&gt; LESSON 01 // HOW TO GET INTO RESEARCH</div>
<h1>You see a <em>problem.</em> Then you go after it.</h1>
{q(1,'Something you saw','On a ward, in a clinic, on campus.','#00E5FF','rgba(0,229,255,.35)')}{q(2,'One sentence','If you cannot say it as a question, it is not ready.','#FF2BD6','rgba(255,43,214,.35)')}{q(3,'Check it exists','Has someone already asked it? That is your review of literature.','#FFD60A','rgba(255,214,10,.3)')}
<div class="bar"><div></div></div><div class="ft" style="margin-top:22px"><span>Dr. Sidharth Narayanan · House Surgeon, GMC Kozhikode</span><span>03 / 12</span></div></section>'''
# ================= V2: ARCADE QUEST (game HUD) =================
css+='''.v2{background:#150C2E;color:#fff;padding:52px 64px;background-image:linear-gradient(rgba(255,255,255,.04) 2px,transparent 2px),linear-gradient(90deg,rgba(255,255,255,.04) 2px,transparent 2px),radial-gradient(circle at 80% 0,rgba(255,214,0,.2),transparent 40%);background-size:36px 36px,36px 36px,auto}
.v2 .hud{display:flex;justify-content:space-between;font:400 22px Mono,monospace;color:#FFD600;letter-spacing:.06em;border:3px solid #FFD600;padding:12px 18px;border-radius:10px;box-shadow:6px 6px 0 #7A2CFF}
.v2 h1{font:800 112px/0.95 Bricolage,Arial;letter-spacing:-.03em;margin-top:34px;text-shadow:6px 6px 0 #7A2CFF}.v2 h1 em{font-style:normal;color:#FFD600}
.v2 .sub{font:400 26px/1.35 Mono,monospace;color:#c9b8ff;margin-top:14px}
.v2 .grid{display:grid;grid-template-columns:repeat(4,1fr);gap:14px;margin-top:26px}.v2 .t{border:3px solid #fff;border-radius:14px;padding:12px 12px 14px;background:#22134a;box-shadow:5px 5px 0 #000;min-height:196px;position:relative}
.v2 .t b{font:800 44px Bricolage;color:#FFD600;display:block}.v2 .t span{font:400 17px/1.25 Mono,monospace;display:block;color:#e7defe;margin-top:4px}.v2 .t em{position:absolute;left:10px;right:10px;bottom:12px;font:700 15px Mono,monospace;font-style:normal;text-align:center;padding:5px;border-radius:6px;color:#150C2E}
.v2 .t.ok{border-color:#2EE6A6}.v2 .t.ok em{background:#2EE6A6}.v2 .t.bad{border-color:#FF4D6D}.v2 .t.bad em{background:#FF4D6D}.v2 .t.mid{border-color:#FFD600}.v2 .t.mid em{background:#FFD600}
.v2 .ft{margin-top:auto;font:400 18px Mono,monospace;color:#9d87d6;display:flex;justify-content:space-between}
.v2 .quest{margin-top:30px;border:3px solid #fff;border-radius:18px;padding:26px 28px;background:#22134a;box-shadow:7px 7px 0 #000}.v2 .quest .o{display:grid;grid-template-columns:62px 1fr;gap:18px;align-items:center;padding:16px 0;border-top:2px dashed rgba(255,255,255,.25)}.v2 .quest .o:first-of-type{border-top:0}
.v2 .box{width:56px;height:56px;border:4px solid #2EE6A6;border-radius:10px;color:#2EE6A6;font:800 40px/46px Arial;text-align:center}.v2 .o b{font:700 36px Arial;display:block}.v2 .o span{font:400 24px/1.3 Mono,monospace;color:#c9b8ff;display:block;margin-top:4px}
.v2 .xp{margin-top:28px;font:700 22px Mono,monospace;color:#FFD600}.v2 .xpb{height:30px;border:3px solid #fff;border-radius:8px;margin-top:8px;overflow:hidden}.v2 .xpb div{width:14%;height:100%;background:repeating-linear-gradient(90deg,#FFD600 0 16px,#ffb300 16px 20px)}'''
def v2_hook():
    lab={'ok':'CLEARED','bad':'NO PAPER','mid':'LOADING...'}
    tiles=''.join(f'<div class="t {r[4]}"><b>{r[0]}</b><span>{e(SHORT[r[0]])}</span><em>{lab[r[4]]}</em></div>' for r in T)
    return f'''<section class="s v2"><div class="hud"><span>PLAYER 1 · DR. SIDHARTH</span><span>R01 · 1/12</span></div>
<h1>8 research <em>quests.</em></h1><div class="sub">4 cleared. 2 never made it to a paper. 2 still loading. Most people play for the portfolio. I played for the story.</div><div class="grid">{tiles}</div>
<div class="ft"><span>Dr. Sidharth Narayanan · House Surgeon, GMC Kozhikode</span><span>01 / 12</span></div></section>'''
def v2_lesson():
    o=lambda t,d:f'<div class="o"><div class="box">&#10003;</div><div><b>{t}</b><span>{d}</span></div></div>'
    return f'''<section class="s v2"><div class="hud"><span>QUEST 01 · GET INTO RESEARCH</span><span>R01 · 3/12</span></div>
<h1>You see a <em>problem.</em> Then you go after it.</h1><div class="sub">Objectives. Complete all three before you pick a topic.</div>
<div class="quest">{o('Something you saw','On a ward, in a clinic, on campus.')}{o('One sentence','If you cannot say it as a question, it is not ready.')}{o('Check it exists','Has someone already asked it? That is your review of literature.')}</div>
<div class="xp">REWARD: A QUESTION WORTH ASKING</div><div class="xpb"><div></div></div><div class="ft"><span>Dr. Sidharth Narayanan · House Surgeon, GMC Kozhikode</span><span>03 / 12</span></div></section>'''
# ================= V3: GLITCH ZINE (pop-art comic) =================
css+='''.v3{background:#FFF6E0;color:#0b0b0b;padding:54px 64px;background-image:radial-gradient(rgba(255,45,120,.28) 3px,transparent 3.5px);background-size:26px 26px}
.v3 .top{display:flex;justify-content:space-between;font:800 22px Bricolage,Arial;letter-spacing:.06em}.v3 .top b{background:#0b0b0b;color:#FFE600;padding:6px 14px;transform:rotate(-2deg);display:inline-block}
.v3 .burst{position:absolute;right:46px;top:120px;width:360px;height:360px;background:#FFE600;border:6px solid #0b0b0b;clip-path:polygon(50% 0,60% 18%,80% 8%,80% 30%,100% 34%,88% 52%,100% 70%,78% 74%,80% 96%,60% 86%,50% 100%,40% 86%,20% 96%,22% 74%,0 70%,12% 52%,0 34%,20% 30%,20% 8%,40% 18%);display:flex;align-items:center;justify-content:center;font:800 220px Bricolage;letter-spacing:-.06em;filter:drop-shadow(10px 10px 0 #0b0b0b)}
.v3 h1{font:800 104px/0.94 Bricolage,Arial;letter-spacing:-.04em;margin-top:60px;max-width:700px;text-shadow:5px 5px 0 #FF2D78}.v3 h1 em{font-style:normal;background:#00D1FF;padding:0 10px;border:5px solid #0b0b0b;display:inline-block;transform:rotate(-2deg);text-shadow:none}
.v3 .bub{margin-top:40px;background:#fff;border:6px solid #0b0b0b;border-radius:30px;padding:26px 32px;font:700 38px/1.2 Arial;position:relative;box-shadow:10px 10px 0 #0b0b0b;max-width:820px}.v3 .bub:after{content:'';position:absolute;left:70px;bottom:-34px;border:18px solid transparent;border-top:34px solid #0b0b0b}
.v3 .stk{display:flex;flex-wrap:wrap;gap:14px;margin-top:60px}.v3 .stk span{font:800 26px Bricolage;padding:10px 18px;border:5px solid #0b0b0b;border-radius:12px;box-shadow:6px 6px 0 #0b0b0b;transform:rotate(var(--r))}
.v3 .stk .ok{background:#2EE6A6}.v3 .stk .bad{background:#FF2D78;color:#fff}.v3 .stk .mid{background:#FFE600}
.v3 .ft{margin-top:auto;font:800 20px Bricolage;letter-spacing:.04em;display:flex;justify-content:space-between}
.v3 .panels{display:grid;gap:24px;margin-top:36px}.v3 .pn{display:grid;grid-template-columns:120px 1fr;gap:22px;align-items:center;background:#fff;border:6px solid #0b0b0b;border-radius:22px;padding:22px 26px;box-shadow:9px 9px 0 #0b0b0b}.v3 .pn i{font:800 100px/1 Bricolage;font-style:normal;color:var(--c);-webkit-text-stroke:5px #0b0b0b}.v3 .pn b{font:800 44px Bricolage;display:block}.v3 .pn span{font:400 28px/1.3 Arial;display:block;margin-top:4px}
.v3 .rule{font:800 34px Bricolage;letter-spacing:.1em;background:#0b0b0b;color:#FFE600;display:inline-block;padding:8px 18px;transform:rotate(-2deg);margin-top:36px}'''
def v3_hook():
    st=''.join(f'<span class="{r[4]}" style="--r:{(-3,2,-1,3,-2,1,-3,2)[i]}deg">{r[3] if r[4]!="ok" else "PUBLISHED"} #{r[0]}</span>' for i,r in enumerate(T))
    return f'''<section class="s v3"><div class="top"><b>BEFORE I LEAVE MED SCHOOL</b><span>R01 · 1/12</span></div><div class="burst">8</div>
<h1>research projects. <em>So far.</em></h1><div class="bub">Most people do research for the portfolio. I did it to build a narrative.</div><div class="stk">{st}</div>
<div class="ft"><span>Dr. Sidharth Narayanan · House Surgeon, GMC Kozhikode</span><span>01 / 12</span></div></section>'''
def v3_lesson():
    p=lambda n,t,d,c:f'<div class="pn" style="--c:{c}"><i>{n}</i><div><b>{t}</b><span>{d}</span></div></div>'
    return f'''<section class="s v3"><div class="top"><b>RULE #1</b><span>R01 · 3/12</span></div>
<h1 style="margin-top:44px">You see a <em>problem.</em> Then you go after it.</h1><div class="rule">HOW TO GET INTO RESEARCH</div>
<div class="panels">{p(1,'Something you saw','On a ward, in a clinic, on campus.','#00D1FF')}{p(2,'One sentence','If you cannot say it as a question, it is not ready.','#FF2D78')}{p(3,'Check it exists','Has someone already asked it? That is your review of literature.','#FFE600')}</div>
<div class="ft"><span>Dr. Sidharth Narayanan · House Surgeon, GMC Kozhikode</span><span>03 / 12</span></div></section>'''
open('pop.html','w').write(f'<!doctype html><meta charset="utf-8"><style>{css}</style>'+v1_hook()+v1_lesson()+v2_hook()+v2_lesson()+v3_hook()+v3_lesson())
print('ok')
