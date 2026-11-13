# Sample: lighter, less blocky journal look + insight-first opener for R02. Palette 2. Not final copy.
NAV,ACC,RED='#20558A','#2F6FA8','#B3261E'
css=f'''*{{box-sizing:border-box;margin:0;padding:0}}body{{background:#777}}
.s{{width:1080px;height:1350px;position:relative;overflow:hidden;margin-bottom:24px;display:flex;flex-direction:column;background:#fff;color:#1d2125;font-family:Arial,Helvetica,sans-serif;padding:0 84px}}
.hd{{display:flex;justify-content:space-between;align-items:center;padding:52px 0 18px;border-bottom:1.5px solid #cfd9e6;font-size:20px;letter-spacing:.05em;color:{NAV};font-weight:700}}
.hd i{{font-style:normal;font-weight:400;color:#8896a6}}
.kick{{margin-top:64px;color:{ACC};font-size:25px;letter-spacing:.06em;font-weight:700}}
h1{{font-weight:300;font-size:92px;line-height:1.06;margin-top:26px;letter-spacing:-.02em}}h1 b{{font-weight:700;color:{NAV}}}
h2{{font-weight:300;font-size:72px;line-height:1.08;margin-top:26px;letter-spacing:-.015em}}h2 b{{font-weight:700;color:{NAV}}}
.sub{{font-family:'Times New Roman',Times,serif;font-size:42px;line-height:1.3;margin-top:36px;color:#3a4552}}
.au{{margin-top:40px;font-size:26px;color:#3a4552}}.id{{display:inline-block;width:26px;height:26px;border-radius:50%;background:#A6CE39;color:#fff;font:700 13px/26px Arial;text-align:center;vertical-align:middle;margin-left:6px}}
.pills{{margin-top:auto;margin-bottom:96px;display:flex;gap:14px}}.pills span{{border:1.5px solid #b9c9dc;color:{NAV};padding:12px 26px;border-radius:999px;font-size:24px;font-weight:700}}.pills .f{{background:#e8f0f9;border-color:#e8f0f9}}
.ft{{position:absolute;left:84px;right:84px;bottom:34px;display:flex;justify-content:space-between;font-size:19px;color:#8896a6}}
.p{{font-family:'Times New Roman',Times,serif;font-size:46px;line-height:1.38;margin-top:34px}}.p em{{font-style:normal;background:linear-gradient(transparent 62%,#FFF1B8 62%)}}
.steps{{margin-top:50px}}.st{{display:grid;grid-template-columns:110px 1fr;gap:20px;padding:30px 0;border-top:1.5px solid #dde5ef}}.st:last-child{{border-bottom:1.5px solid #dde5ef}}
.st .n{{font-size:62px;font-weight:300;color:{ACC}}}.st b{{font-size:36px;color:{NAV}}}.st span{{display:block;font-family:'Times New Roman',Times,serif;font-size:36px;margin-top:8px;color:#3a4552;line-height:1.3}}
.note{{margin-top:34px;font-size:28px;color:{RED};font-weight:700}}
.src{{margin-top:22px;font-size:20px;color:#8896a6;letter-spacing:.03em}}'''
def s(inner,n): return f'<section class="s"><div class="hd"><span>BEFORE I LEAVE MED SCHOOL · RESEARCH</span><i>R02 · {n}/10</i></div>{inner}<div class="ft"><span>Dr. Sidharth Narayanan · House Surgeon, GMC Kozhikode</span><span>{n:02d} / 10</span></div></section>'
svg=f'''<svg viewBox="0 0 912 330" style="width:100%;margin-top:56px"><line x1="10" y1="260" x2="900" y2="260" stroke="#b9c9dc" stroke-width="3"/><text x="10" y="310" font-size="22" fill="#8896a6" font-family="Arial">TIME</text>
<rect x="400" y="30" width="110" height="230" rx="14" fill="#e8f0f9" stroke="{ACC}" stroke-width="3"/>
<g fill="{ACC}">'''+''.join(f'<circle cx="{x}" cy="{y}" r="9"/>' for x,y in [(425,90),(462,70),(490,120),(432,150),(470,185),(445,225),(492,215),(418,200)])+f'''</g>
<text x="455" y="22" text-anchor="middle" font-size="24" font-weight="700" fill="{NAV}" font-family="Arial">ONE MOMENT</text>
<g stroke="#d3dce8" stroke-width="3" stroke-dasharray="3 10" fill="none"><line x1="400" y1="150" x2="120" y2="150"/><line x1="510" y1="150" x2="790" y2="150"/></g>
<text x="200" y="140" text-anchor="middle" font-size="24" fill="#8896a6" font-family="Arial">before</text><text x="710" y="140" text-anchor="middle" font-size="24" fill="#8896a6" font-family="Arial">after</text></svg>'''
S=[s(f'<div class="kick">UNDERGRADUATE RESEARCH · HOW TO</div><h1>How do you run a <b>cross-sectional study</b> on NCD risk factors?</h1><div class="sub">What I learnt doing one in medical college, including what I got wrong.</div><div class="au">Sidharth Narayanan, MBBS <span class="id">iD</span></div><div class="pills"><span class="f">Cite</span><span>Save</span><span>Share</span><span>Swipe →</span></div>',1),
s(f'<div class="kick">STEP 1 · THE DESIGN</div><h2>A cross-sectional study is a <b>snapshot.</b></h2><div class="p">You look at a population at <em>one point in time</em>. You measure risk factors and conditions together.</div>{svg}<div class="p" style="font-size:40px">It tells you how common something is. It cannot tell you what caused what.</div>',2),
s(f'<div class="kick">STEP 2 · THE TOOL</div><h2>Do not invent your questions. <b>Use a framework.</b></h2><div class="steps"><div class="st"><div class="n">1</div><div><b>Questionnaire</b><span>Tobacco, alcohol, diet, physical activity</span></div></div><div class="st"><div class="n">2</div><div><b>Physical measurements</b><span>Height, weight, waist, blood pressure</span></div></div><div class="st"><div class="n">3</div><div><b>Biochemical tests</b><span>Blood glucose, cholesterol</span></div></div></div><div class="note">We ran Steps 1 and 2.</div><div class="src">SOURCE: WHO STEPS, the stepwise approach to NCD risk factor surveillance.</div>',3)]
open('sample_soft.html','w').write(f'<!doctype html><meta charset="utf-8"><style>{css}</style>'+''.join(S))
