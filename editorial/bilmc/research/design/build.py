# Three design variants for the Research sub-series, 3 sample slides each (cover, master table, story). Facts come from ../publications.md and the author's manuscript only.
SER='Before I Leave Med School · Research'
AUTH='Dr. Sidharth Narayanan · House Surgeon, GMC Kozhikode'
ROWS=[('1','WHO STEPS 1 & 2 risk-factor survey (NCD)','Cross-sectional','Presented at national forums and UG conferences','NOT PUBLISHED','bad'),
('2','Nutritional assessment of cancer patients','Cross-sectional','Indian J Med Paediatr Oncol, Mar 2026 (2nd author)','PUBLISHED','ok'),
('3','Metastatic solitary fibrous tumour, parapharyngeal','Case report','Indian J Med Paediatr Oncol, Apr 2025 (6th author)','PUBLISHED','ok'),
('4','Juvenile justice and recidivism (elective)','Field study','Report and forums; not pushed for publication','NOT PUBLISHED','bad'),
('5','Obesity-driven cardiac mortality, US adults 15 to 44','Meta-analysis (CDC WONDER)','JAHA, Oct 2026 (4th author)','PUBLISHED','ok'),
('6','Retrosternal goitre','Case series','Ongoing','IN PROGRESS','mid')]
Q1='But I saw it from a different perspective.'
Q2='It all started with how I got into MBBS in the first place.'
H='Most people do undergraduate research for a portfolio. I did it for a different reason.'
T='I Want to Tell You How I Got Into Research'
css='''*{box-sizing:border-box;margin:0;padding:0}body{background:#777}
.s{width:1080px;height:1350px;position:relative;overflow:hidden;margin-bottom:24px;display:flex;flex-direction:column}
'''
# ---------- VARIANT A: journal article / PubMed ----------
cssA='''.A{background:#fff;color:#1d2125;font-family:Arial,Helvetica,sans-serif}
.A .bar{background:#14344A;color:#fff;padding:26px 64px;display:flex;justify-content:space-between;font-size:22px;letter-spacing:.04em}
.A .bar b{font-weight:700}.A .tag{color:#4F7A21;font-size:30px;letter-spacing:.02em;padding:0 64px;margin-top:54px;border-bottom:4px solid #6f9a3a;margin-left:64px;margin-right:64px;padding:0 0 8px}
.A h1{font-weight:400;font-size:88px;line-height:1.08;margin:34px 64px 0;letter-spacing:-.01em}
.A .au{margin:30px 64px 0;font-size:30px}.A .id{display:inline-block;width:30px;height:30px;border-radius:50%;background:#A6CE39;color:#fff;font:700 15px/30px Arial;text-align:center;vertical-align:middle;margin-left:6px}
.A .ab{margin:48px 64px 0;font-family:'Times New Roman',Times,serif;font-size:40px;line-height:1.36}.A .ab p{margin-top:16px}.A .ab b{font-family:Arial;color:#C0342B;font-size:32px;letter-spacing:.03em}
.A .btns{margin:auto 64px 56px;display:flex;gap:14px;font-size:24px}.A .btns span{border:2px solid #14344A;color:#14344A;padding:12px 24px;border-radius:6px;font-weight:700}.A .btns span.f{background:#14344A;color:#fff}
.A .ft{position:absolute;bottom:20px;left:64px;right:64px;font-size:19px;color:#667;display:flex;justify-content:space-between}
.A table{border-collapse:collapse;margin:34px 64px 0;width:952px;font-size:23px}.A th{background:#14344A;color:#fff;text-align:left;padding:14px 12px;font-size:20px;letter-spacing:.05em}.A td{padding:16px 12px;border-bottom:1px solid #d4d8dc;vertical-align:top}.A tr:nth-child(even) td{background:#f4f6f8}.A tr.hl td{background:#FFF2B3}
.A .chip{font-weight:700;font-size:18px;padding:5px 10px;border-radius:4px;display:inline-block;white-space:nowrap}.A .ok{background:#e3efd3;color:#3a5e14}.A .bad{background:#f8d9d6;color:#b3261e}.A .mid{background:#ffe9b0;color:#7a5200}
.A .body{margin:44px 64px 0;font-family:'Times New Roman',Times,serif;font-size:36px;line-height:1.45}.A .body:first-letter{font-size:130px;float:left;line-height:.8;margin:12px 14px 0 0;color:#14344A}
.A .pull{margin:40px 64px 0;border-left:8px solid #4F7A21;padding:6px 0 6px 26px;font-size:50px;line-height:1.15;font-family:Arial}.A cite{font-size:20px;color:#14344A;vertical-align:super}
'''
def A():
    s1=f'''<section class="s A"><div class="bar"><b>{SER.upper()}</b><span>R01</span></div><div class="tag">ORIGINAL EXPERIENCE · UNDERGRADUATE RESEARCH</div>
<h1>{T}</h1><div class="au">Sidharth Narayanan, MBBS <span class="id">iD</span></div><div style="margin:8px 64px 0;font-size:22px;color:#667">Government Medical College, Kozhikode</div>
<div class="ab"><p><b>BACKGROUND:</b> A lot of people get into undergraduate research to build a portfolio.</p><p><b>METHODS:</b> One drop year, and one person who believed in me before I had seen a medical college.</p><p><b>RESULTS:</b> I joined college and forgot all the whys and hows of why I got there.</p><p><b>CONCLUSIONS:</b> The questions came back in second year.</p></div>
<div style="margin:36px 64px 0;font-size:24px;color:#14344A"><b>KEYWORDS:</b> undergraduate research; medical education; motivation; nutrition</div><div style="margin:20px 64px 0;background:#f4f6f8;border:2px solid #d4d8dc;padding:18px 22px;font-size:21px;color:#445">Cite as: Narayanan S. I want to tell you how I got into research. Before I Leave Med School · Research, R01. Medinn, 2026.</div><div class="btns"><span class="f">Cite</span><span>Save</span><span>Share</span><span>Next: R02 →</span></div></section>'''
    rows=''.join(f'<tr class="{"hl" if r[0]=="1" else ""}"><td>{r[0]}</td><td><b>{r[1]}</b><br><span style="color:#556">{r[2]}</span></td><td>{r[3]}</td><td><span class="chip {r[5]}">{r[4]}</span></td></tr>' for r in ROWS)
    s2=f'''<section class="s A"><div class="bar"><b>{SER.upper()}</b><span>R02</span></div><div class="tag">TABLE 1 · THE RESEARCH LEDGER</div>
<h1 style="font-size:56px">Every project, and what happened to it.</h1><table><tr><th>#</th><th>PROJECT</th><th>OUTPUT</th><th>STATUS</th></tr>{rows}</table>
<div class="ft"><span>Source: author, ORCID and journal records.</span><span>{AUTH}</span></div></section>'''
    s3=f'''<section class="s A"><div class="bar"><b>{SER.upper()}</b><span>R01 · p.2</span></div><div class="tag">MAIN TEXT</div>
<p class="body">A lot of people get into undergraduate research for the sole purpose of building a portfolio so that they can go abroad, write the USMLE exam, or see it as a clearance aspect for their PLAB or AMC exams.<cite>[1]</cite></p>
<div class="pull">{Q1}<br>{Q2}</div><div class="ft"><span>[1] Author’s account, 2026.</span><span>{AUTH}</span></div></section>'''
    return s1+s2+s3
# ---------- VARIANT B: spreadsheet ----------
cssB='''.B{background:#fff;color:#222;font-family:Arial,Helvetica,sans-serif}
.B .rib{background:#217346;color:#fff;padding:20px 28px;display:flex;align-items:center;gap:18px;font-size:22px}.B .rib b{font-size:26px}.B .rib span{background:rgba(255,255,255,.18);padding:6px 14px;border-radius:4px;font-size:19px}
.B .fx{display:flex;align-items:center;border-bottom:2px solid #c9c9c9;font-size:24px;background:#f3f3f3;height:62px}.B .fx i{width:130px;text-align:center;border-right:2px solid #c9c9c9;font-style:normal;color:#444;height:62px;line-height:62px;background:#fff}.B .fx em{padding:0 18px;color:#217346;font-style:italic;font-weight:700}.B .fx div{padding:0 10px;white-space:nowrap;overflow:hidden}
.B .grid{flex:1;display:grid;position:relative;font-size:26px}.B .ch{background:#e7e7e7;border:1px solid #c9c9c9;text-align:center;font-size:20px;color:#444;padding:6px 0}.B .rh{background:#e7e7e7;border:1px solid #c9c9c9;text-align:center;font-size:20px;color:#444;display:flex;align-items:center;justify-content:center}.B .c{border:1px solid #d9d9d9;padding:10px 14px;line-height:1.25;overflow:hidden}.B .sel{outline:5px solid #217346;outline-offset:-3px;background:#fff;z-index:2}
.B .tabs{display:flex;gap:0;background:#e7e7e7;border-top:2px solid #c9c9c9;font-size:21px}.B .tabs span{padding:12px 26px;border-right:1px solid #c9c9c9}.B .tabs span.on{background:#fff;color:#217346;font-weight:700;border-top:4px solid #217346}
.B .na{color:#C00000;font-weight:700}.B .t{color:#217346;font-weight:700}.B .y{background:#FFF2CC}.B .hd{background:#217346;color:#fff;font-weight:700;font-size:21px;letter-spacing:.05em}
.B .note{position:absolute;right:50px;bottom:120px;width:420px;background:#FFF2CC;border:2px solid #d8b400;padding:18px;font-size:24px;line-height:1.3;box-shadow:6px 8px 0 rgba(0,0,0,.18)}
'''
def Bgrid(cols,rows,cells,sel=None,w=None):
    # cells: dict (r,c)->(html,cls,span cols,span rows)
    out=f'<div class="grid" style="grid-template-columns:70px {cols};grid-template-rows:44px repeat({rows},1fr)"><div class="ch"></div>'
    n=len(cols.split())
    for i in range(n): out+=f'<div class="ch">{chr(65+i)}</div>'
    placed={}
    for r in range(1,rows+1):
        out+=f'<div class="rh">{r}</div>'
        c=0
        while c<n:
            if (r,c) in cells:
                h,cl,sc=cells[(r,c)]; out+=f'<div class="c {cl}" style="grid-column:span {sc}">{h}</div>'; c+=sc
            else: out+='<div class="c"></div>'; c+=1
    return out+'</div>'
def B():
    rib=lambda l:f'<div class="rib"><b>⊞</b><b>{SER}</b><span>{l}</span><span style="margin-left:auto">Share</span><span>Cite</span></div>'
    tabs=lambda on:'<div class="tabs">'+''.join(f'<span class="{"on" if x==on else ""}">{x}</span>' for x in ['R01','R02','R03','R04','R05','R06','R07','Ledger'])+'</div>'
    fx=lambda ref,f:f'<div class="fx"><i>{ref}</i><em>fx</em><div>{f}</div></div>'
    c1={(1,0):('<span style="font-size:20px;letter-spacing:.06em">UNDERGRADUATE RESEARCH · R01</span>','hd',6),
      (2,0):(f'<b style="font-size:60px;line-height:1.02;font-family:Arial">{T}</b>','sel',6),(3,0):('author','','1'),
      (4,0):('Background','hd',1),(4,1):('A lot of people get into undergraduate research for the sole purpose of building a portfolio.','',5),
      (5,0):('Trigger','hd',1),(5,1):('One person, a vegan, who believed in me before I had seen a medical college.','',5),
      (6,0):('Status','hd',1),(6,1):('Forgotten, once I joined college.','',3),(6,4):('<span class="na">#REF!</span>','',2),
      (7,0):('Returned','hd',1),(7,1):('Second year. The questions came back.','y',5)}
    c1[(3,0)]=(AUTH,'',6)
    s1=f'<section class="s B">{rib("R01")}{fx("B2","=STORY(&quot;"+H[:62]+"…&quot;)")}'+Bgrid('190px 1fr 1fr 1fr 1fr 1fr',13,c1)+tabs('R01')+'</section>'
    cs={(1,0):('#','hd',1),(1,1):('Project','hd',2),(1,3):('Output','hd',2),(1,5):('Published','hd',1)}
    for i,r in enumerate(ROWS):
        cs[(2+i*2,0)]=(r[0],'',1); cs[(2+i*2,1)]=(f'<b>{r[1]}</b>','y' if r[0]=='1' else '',2); cs[(2+i*2,3)]=(r[3],'y' if r[0]=='1' else '',2)
        cs[(2+i*2,5)]=('<span class="t">TRUE</span>' if r[5]=='ok' else ('<span class="na">#N/A</span>' if r[5]=='bad' else 'PENDING'),'y' if r[0]=='1' else '',1)
    s2=f'<section class="s B">{rib("Ledger")}{fx("F4","=COUNTIF(F2:F13,TRUE)")}'+Bgrid('70px 1fr 1fr 1fr 1fr 150px',13,cs)+tabs('Ledger')+'</section>'
    cq={(1,0):('FROM THE MANUSCRIPT','hd',6),(2,0):(f'<b style="font-size:54px;line-height:1.1;font-family:Arial">{Q1}</b>','sel y',6),(3,0):(f'<span style="font-size:40px">{Q2}</span>','',6),(5,0):('A lot of people get into undergraduate research for the sole purpose of building a portfolio so that they can go abroad, write the USMLE, or see it as a clearance aspect for PLAB or AMC.','',6)}
    s3=f'<section class="s B">{rib("R01")}{fx("B2","=QUOTE(R01,2)")}'+Bgrid('190px 1fr 1fr 1fr 1fr 1fr',12,cq)+'<div class="note"><b>Comment:</b> the portfolio reason is the common one. This is not that story.</div>'+tabs('R01')+'</section>'
    return s1+s2+s3
# ---------- VARIANT C: dark data dashboard ----------
cssC='''.C{background:#0E1621;color:#E6EDF3;font-family:'JetBrains Mono',monospace;background-image:linear-gradient(rgba(76,201,240,.06) 1px,transparent 1px),linear-gradient(90deg,rgba(76,201,240,.06) 1px,transparent 1px);background-size:54px 54px;padding:60px 64px 56px}
.C .top{display:flex;justify-content:space-between;font-size:20px;letter-spacing:.08em;color:#8FA3B8;text-transform:uppercase}.C .q{margin-top:44px;color:#4CC9F0;font-size:25px}.C .q b{color:#FFB703}
.C h1{font-family:Arial,Helvetica,sans-serif;font-weight:700;font-size:104px;line-height:1.02;margin-top:26px;letter-spacing:-.02em}.C h1 em{font-style:normal;color:#FFB703}
.C .chips{display:flex;gap:12px;flex-wrap:wrap;margin-top:36px}.C .chips span{border:2px solid #2d3b4d;padding:14px 20px;border-radius:6px;font-size:27px;background:#142130}.C .chips .g{color:#2EC27E;border-color:#2EC27E}.C .chips .r{color:#FF5D5D;border-color:#FF5D5D}.C .chips .a{color:#FFB703;border-color:#FFB703}
.C .box{margin-top:auto;border:2px solid #2d3b4d;background:#142130;padding:36px 40px;border-radius:8px;font-size:34px;line-height:1.4}.C .box b{color:#FFB703}
.C .foot{display:flex;justify-content:space-between;margin-top:26px;font-size:19px;color:#8FA3B8;border-top:2px solid #2d3b4d;padding-top:16px}
.C .log{font-family:Arial;font-size:44px;line-height:1.25;margin-top:30px;border-left:8px solid #FFB703;padding-left:30px}.C .ts{color:#8FA3B8;font-size:22px;margin-top:40px}
'''
def C():
    s1=f'''<section class="s C"><div class="top"><span>{SER}</span><span>R01</span></div><div class="q">&gt; SELECT story FROM research WHERE id = <b>'R01'</b>;  <span style="color:#2EC27E">1 result</span></div>
<h1>I Want to Tell You How I Got Into <em>Research.</em></h1>
<div class="chips"><span class="g">drop_year = TRUE</span><span class="a">mentor = 1</span><span class="r">why = NULL (forgot)</span><span class="g">returned = 2nd year</span></div>
<div class="box"><b>{H}</b></div><div class="foot"><span>{AUTH}</span><span>01 / 10</span></div></section>'''
    # scatter schematic
    pts=[(150,430,'ok','2025'),(330,360,'ok','2026'),(520,300,'ok','2026'),(710,250,'ok','2026')]
    svg='''<svg viewBox="0 0 952 560" style="width:100%;margin-top:34px"><g stroke="#2d3b4d" stroke-width="2"><line x1="70" y1="500" x2="940" y2="500"/><line x1="70" y1="40" x2="70" y2="500"/>'''+''.join(f'<line x1="70" y1="{y}" x2="940" y2="{y}" stroke-dasharray="4 10"/>' for y in (380,260,140))+'</g>'
    labs=[('Case report',140,'#2EC27E',True),('Nutrition',300,'#2EC27E',True),('Meta-analysis',470,'#2EC27E',True),('NCD survey',640,'#FF5D5D',False),('Goitre series',810,'#FFB703',False)]
    for i,(l,x,c,pub) in enumerate(labs):
        y=150 if pub else (400 if c=='#FF5D5D' else 330)
        if pub: svg+=f'<circle cx="{x+30}" cy="{y}" r="22" fill="{c}"/>'
        elif c=='#FF5D5D': svg+=f'<circle cx="{x+30}" cy="{y}" r="22" fill="none" stroke="{c}" stroke-width="5" stroke-dasharray="6 7"/><text x="{x+30}" y="{y+12}" text-anchor="middle" font-size="34" fill="{c}" font-family="Arial">?</text>'
        else: svg+=f'<circle cx="{x+30}" cy="{y}" r="22" fill="none" stroke="{c}" stroke-width="5"/>'
        svg+=f'<text x="{x+30}" y="535" text-anchor="middle" font-size="18" fill="#8FA3B8" font-family="JetBrains Mono">{l}</text>'
    svg+='<text x="76" y="30" font-size="18" fill="#8FA3B8" font-family="JetBrains Mono">PUBLISHED</text><text x="76" y="480" font-size="18" fill="#8FA3B8" font-family="JetBrains Mono">NOT PUBLISHED</text></svg>'
    s2=f'''<section class="s C"><div class="top"><span>{SER}</span><span>R02</span></div><div class="q">&gt; PLOT outcome BY project;</div><h1 style="font-size:64px">The point that never <em>published.</em></h1>{svg}
<div class="chips"><span class="g">● published</span><span class="r">○ not published</span><span class="a">○ in progress</span></div><div class="foot"><span>Schematic. Not to scale.</span><span>{AUTH}</span></div></section>'''
    s3=f'''<section class="s C"><div class="top"><span>{SER}</span><span>R01 · LOG</span></div><div class="ts">entry_001 · why_i_got_into_research</div>
<div class="log">{Q1}</div><div class="log" style="margin-top:50px;border-color:#4CC9F0">{Q2}</div>
<div class="box" style="margin-top:auto">A lot of people get into undergraduate research for the sole purpose of <b>building a portfolio</b> so that they can go abroad, write the USMLE, or clear PLAB or AMC.</div><div class="foot"><span>{AUTH}</span><span>03 / 10</span></div></section>'''
    return s1+s2+s3
for n,css_,f in (('A',cssA,A),('B',cssB,B),('C',cssC,C)):
    open(f'variant-{n}.html','w').write(f'<!doctype html><meta charset="utf-8"><style>@font-face{{font-family:"JetBrains Mono";src:url(../../../../essays/fonts/mono-normal.woff2)}}{css}{css_}</style>'+f())
print('ok')
