# Builds slides.html for Article 001 from the Ledger system. Edit copy here, then run render.js.
URL = 'medinn.in/bilmc/more-than-a-training-ground'
def run(tag, label): return f'<div class="run"><span>Before I Leave Medical College · 001</span><span class="tag {tag}">{label}</span></div>'
def foot(n): return '<div class="foot"><div><b>Dr. Sidharth Narayanan</b> <span>· House Surgeon, GMC Kozhikode</span></div><div class="n">@@N@@</div></div>'
def hatch(i): return f'<defs><pattern id="h{i}" width="14" height="14" patternUnits="userSpaceOnUse" patternTransform="rotate(45)"><line x1="0" y1="0" x2="0" y2="14" stroke="currentColor" stroke-width="2.5"/></pattern></defs>'
S = []
# 01 COVER
S.append(f'''<section class="slide" id="s01">{run("insight","Article 001")}
<h1 class="h" style="font-size:118px;margin-top:6px">Medical college is more than a training ground for doctors.</h1>
<div style="margin-top:auto;margin-bottom:100px;display:flex;align-items:flex-end;justify-content:space-between;gap:40px">
 <div style="max-width:480px">
  <p class="lab" style="margin-bottom:14px">How to read this series</p>
  <div class="lab" style="display:grid;gap:10px;font-size:21px"><span><b style="color:var(--red)">■ Red</b> a critique</span><span><b>■ Black</b> an insight</span><span><b style="color:var(--blue)">■ Blue</b> the evidence</span></div>
  <p style="font-family:var(--serif);font-size:38px;line-height:1.2;margin-top:34px">On medical education, from a house surgeon’s lens.</p>
 </div>
 <div style="position:relative"><img class="portrait" src="../../assets/medx-speaker.jpg" alt="Dr. Sidharth Narayanan speaking at MedX Talks" style="width:360px;height:450px;border-radius:180px 180px 0 0;border:4px solid var(--black)">
  <div class="lab" style="position:absolute;left:-4px;right:-4px;bottom:-4px;background:var(--blue);color:var(--white);padding:10px 14px;font-size:18px">MedX Talks · 25 Oct 2026</div></div>
</div>{foot(1)}</section>''')
# 01b THE PREMISE (new): states the stance before anything else
S.append(f'''<section class="slide" id="s01b">{run("insight","The premise")}
<h2 class="h" style="margin-top:6px;font-size:90px">MBBS is the foundation of every doctor’s career. Right now, it feels <span class="r">undervalued.</span></h2>
<p class="sub" style="font-size:38px">This series starts there: bringing value back to undergraduate medical education.</p>
<div class="art"><svg viewBox="0 0 904 420">{hatch(1)}
 <g stroke="currentColor" stroke-width="3.5">
  <rect x="2" y="120" width="330" height="170" fill="url(#h1)"/><rect x="346" y="120" width="170" height="170" fill="#fff"/><rect x="530" y="120" width="180" height="170" fill="#fff"/><rect x="724" y="120" width="178" height="170" fill="#fff"/></g>
 <g class="mo" font-size="21" font-weight="700" fill="currentColor" text-anchor="middle"><rect x="42" y="168" width="250" height="74" fill="#fff" stroke="currentColor" stroke-width="3"/><text class="mo" x="167" y="212">CLINICAL PRACTICE</text>
  <text class="mo" x="431" y="200">RESEARCH</text><text class="mo" x="620" y="200">TECHNOLOGY</text><text class="mo" x="813" y="196">ENTREPRE-</text><text class="mo" x="813" y="222">NEURSHIP</text></g>
 <rect x="2" y="300" width="900" height="112" fill="currentColor"/>
 <text class="se" x="40" y="368" font-size="46" font-weight="600" fill="#fff">MBBS</text><text class="mo" x="190" y="364" font-size="22" fill="#fff">FOUNDATION OF EVERY DOCTOR’S CAREER</text>
 <rect x="690" y="318" width="190" height="42" fill="var(--red)"/><text class="mo" x="785" y="346" text-anchor="middle" font-size="20" font-weight="700" fill="#fff">UNDERVALUED</text></svg>
<p class="cap">Fig. 0 — Clinical practice rests on it, and so does everything else a doctor may choose to build.</p></div>{foot(0)}</section>''')
# 02 QUESTION
S.append(f'''<section class="slide" id="s02">{run("question","The question")}
<div style="position:absolute;right:30px;top:210px;font-family:var(--serif);font-style:italic;font-weight:300;font-size:760px;line-height:1;color:var(--red);opacity:.16">?</div>
<h2 class="h" style="position:relative;margin-top:30px;font-size:108px">We train doctors. But is that all a medical college should aspire to do?</h2>
<p class="cap" style="margin-top:auto;margin-bottom:100px;font-size:26px;color:var(--black);position:relative">A reflection from within medical education.</p>{foot(2)}</section>''')
# 03 TIMETABLE
rows=['L L P L T','L P L L T','T T E L P','L P T E Q']
def cell(t,x,y):
    w,h=168,92
    if t=='L': return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="currentColor"/>'
    if t=='P': return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="url(#h3)" stroke="currentColor" stroke-width="3"/>'
    if t=='E': return f'<rect x="{x+1.5}" y="{y+1.5}" width="{w-3}" height="{h-3}" fill="none" stroke="currentColor" stroke-width="3"/><rect x="{x+14}" y="{y+14}" width="{w-28}" height="{h-28}" fill="none" stroke="currentColor" stroke-width="3"/>'
    if t=='T': return f'<rect x="{x+1.5}" y="{y+1.5}" width="{w-3}" height="{h-3}" fill="#fff" stroke="currentColor" stroke-width="3"/><line x1="{x+14}" y1="{y+46}" x2="{x+w-14}" y2="{y+46}" stroke="currentColor" stroke-width="4"/>'
    return f'<rect x="{x+1.5}" y="{y+1.5}" width="{w-3}" height="{h-3}" fill="#fff" stroke="var(--red)" stroke-width="4" stroke-dasharray="10 9"/><text x="{x+w/2}" y="{y+68}" text-anchor="middle" class="se" font-size="64" font-style="italic" fill="var(--red)">?</text>'
g=''.join(cell(t,c*184,r*106) for r,row in enumerate(rows) for c,t in enumerate(row.split()))
leg=''.join(f'<g transform="translate({x} 450) scale(.17)">{cell(t,0,0)}</g><text class="mo" x="{x+36}" y="468" font-size="22" fill="currentColor">{l}</text>' for x,t,l in [(0,'L','Lectures'),(205,'P','Practicals'),(425,'E','Exams'),(580,'T','Postings')])
S.append(f'''<section class="slide" id="s03">{run("critique","Fig. 1")}
<h2 class="h" style="margin-top:6px">Are we getting the most out of undergraduate medical education?</h2>
<div class="art"><svg viewBox="0 0 904 500">{hatch(3)}{g}{leg}</svg>
<p class="cap">Fig. 1 — The undergraduate timetable (illustrative). <b style="color:var(--red)">What fills the empty cell?</b></p></div>{foot(3)}</section>''')
# 04 STEPPING STONE (red = critique)
S.append(f'''<section class="slide t-red" id="s04">{run("critique","Fig. 2")}
<h2 class="h" style="margin-top:6px">Has MBBS become a stepping stone to <span style="white-space:nowrap">NEET-PG?</span></h2>
<p class="sub">…rather than an experience students fully value in itself.</p>
<div class="art"><svg viewBox="0 0 904 470">{hatch(4)}
 <rect x="2" y="330" width="290" height="130" fill="url(#h4)" stroke="currentColor" stroke-width="3"/>
 <rect x="306" y="230" width="290" height="230" fill="none" stroke="currentColor" stroke-width="4" stroke-dasharray="10 9"/>
 <rect x="610" y="90" width="292" height="370" fill="#fff"/>
 <rect x="30" y="350" width="150" height="46" fill="var(--red)"/><text class="mo" x="40" y="383" font-size="27" font-weight="700" fill="#fff">MBBS</text>
 <text class="mo" x="636" y="152" font-size="27" font-weight="700" fill="var(--red)">NEET-PG</text>
 <text class="se" x="451" y="372" text-anchor="middle" font-size="130" font-style="italic" fill="#fff">?</text>
 <g stroke="currentColor" stroke-width="5" stroke-linecap="round" fill="none"><circle cx="150" cy="238" r="24" fill="var(--red)"/><path d="M150 262 V318 M150 276 L118 300 M150 276 L184 252 M150 318 L130 330 M150 318 L172 330"/></g>
 <path d="M200 218 C 330 120, 470 70, 600 70" fill="none" stroke="currentColor" stroke-width="5" stroke-dasharray="3 14" stroke-linecap="round"/><path d="M580 50 L606 70 L582 90" fill="none" stroke="currentColor" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/></svg>
<p class="cap">Fig. 2 — The step, and the staircase beyond it.</p></div>{foot(4)}</section>''')
# 05 UNTAPPED OPPORTUNITY
S.append(f'''<section class="slide" id="s05">{run("critique","Fig. 3")}
<h2 class="h" style="margin-top:6px;font-size:90px">Students see clinical problems every day. What happens to the <span class="r">solutions</span> they imagine?</h2>
<div class="art"><svg viewBox="0 0 904 380">
 <line x1="100" y1="90" x2="335" y2="90" stroke="currentColor" stroke-width="6"/>
 <line x1="335" y1="90" x2="570" y2="90" stroke="var(--red)" stroke-width="5" stroke-dasharray="3 15" stroke-linecap="round"/>
 <line x1="570" y1="90" x2="805" y2="90" stroke="var(--red)" stroke-width="5" stroke-dasharray="3 15" stroke-linecap="round" opacity=".5"/>
 <circle cx="100" cy="90" r="62" fill="currentColor"/><circle cx="335" cy="90" r="62" fill="currentColor"/>
 <circle cx="570" cy="90" r="62" fill="#fff" stroke="var(--red)" stroke-width="4" stroke-dasharray="3 12" stroke-linecap="round"/>
 <circle cx="805" cy="90" r="62" fill="#fff" stroke="var(--red)" stroke-width="4" stroke-dasharray="3 12" stroke-linecap="round" opacity=".5"/>
 <g class="se" font-size="58" font-weight="600" text-anchor="middle"><text class="se" x="100" y="110" fill="#fff">1</text><text class="se" x="335" y="110" fill="#fff">2</text><text class="se" x="570" y="110" fill="var(--red)">3</text><text class="se" x="805" y="110" fill="var(--red)" opacity=".5">4</text></g>
 <g class="mo" font-size="22" font-weight="600" text-anchor="middle" fill="currentColor"><text class="mo" x="100" y="200">CLINICAL</text><text class="mo" x="100" y="228">OBSERVATION</text><text class="mo" x="335" y="214">IDEA</text><text class="mo" x="570" y="214" fill="var(--red)">PROTOTYPE</text><text class="mo" x="805" y="214" fill="var(--red)" opacity=".6">VALIDATION</text></g>
 <circle cx="452" cy="90" r="26" fill="var(--red)"/><text class="se" x="452" y="106" text-anchor="middle" font-size="40" font-style="italic" fill="#fff">?</text>
 <text class="se" x="0" y="330" font-size="44" font-style="italic" fill="var(--red)">The pathway exists. The support often doesn’t.</text></svg>
<p class="cap">Fig. 3 — From clinical observation to validation.</p></div>{foot(5)}</section>''')
# 06 VENN (insight)
S.append(f'''<section class="slide" id="s06">{run("insight","Fig. 4")}
<h2 class="h" style="margin-top:6px">Clinical understanding needs to meet <span style="text-decoration:underline;text-decoration-thickness:6px;text-underline-offset:10px">engineering expertise.</span></h2>
<div class="art"><svg viewBox="0 0 904 620">{hatch(6)}
 <g fill="url(#h6)" fill-opacity=".22" stroke="currentColor" stroke-width="3.5"><circle cx="452" cy="200" r="190"/><circle cx="322" cy="404" r="190"/><circle cx="582" cy="404" r="190"/></g>
 <g class="se" font-size="32" font-weight="600" text-anchor="middle" fill="currentColor">
  <text class="se" x="452" y="104">Clinical</text><text class="se" x="452" y="142">understanding</text>
  <text class="se" x="248" y="470" font-size="29">Engineering</text><text class="se" x="248" y="504" font-size="29">expertise</text>
  <text class="se" x="656" y="470" font-size="29">Research &amp;</text><text class="se" x="656" y="504" font-size="29">collaboration</text></g>
 <rect x="342" y="306" width="220" height="104" rx="52" fill="currentColor"/>
 <text x="452" y="349" text-anchor="middle" font-size="26" font-weight="700" fill="#fff">Healthcare</text><text x="452" y="382" text-anchor="middle" font-size="26" font-weight="700" fill="#fff">innovation</text></svg>
<p class="cap">Fig. 4 — Where the pieces overlap.</p></div>{foot(6)}</section>''')
# 07 REVERSE TREND (evidence + critique)
S.append(f'''<section class="slide" id="s07">{run("evidence","Fig. 5")}
<h2 class="h" style="margin-top:6px;font-size:80px">Technology institutions are building bridges towards medicine. <span class="r">What about the other direction?</span></h2>
<div class="art"><svg viewBox="0 0 904 430">{hatch(7)}
 <path d="M0 392 q38 -16 76 0 t76 0 t76 0 t76 0 t76 0 t76 0 t76 0 t76 0 t76 0 t76 0 t76 0 t76 0" fill="none" stroke="currentColor" stroke-width="3" opacity=".25"/>
 <g style="color:var(--blue)"><rect x="2" y="150" width="248" height="240" fill="url(#h7)" stroke="currentColor" stroke-width="3.5"/>
  <rect x="22" y="236" width="208" height="76" fill="#fff" stroke="currentColor" stroke-width="3"/>
  <g stroke="currentColor" stroke-width="3.5" fill="none"><line x1="250" y1="150" x2="520" y2="150"/><line x1="250" y1="190" x2="520" y2="190"/><path d="M250 190 L295 150 L340 190 L385 150 L430 190 L475 150 L520 190"/></g>
  <g stroke="currentColor" stroke-width="9"><line x1="340" y1="190" x2="340" y2="392"/><line x1="430" y1="190" x2="430" y2="392"/></g>
  <g class="mo" font-size="19" font-weight="700" text-anchor="middle" fill="currentColor"><text class="mo" x="126" y="268">TECHNOLOGY</text><text class="mo" x="126" y="294">INSTITUTIONS</text></g></g>
 <rect x="654" y="150" width="248" height="240" fill="#fff" stroke="var(--red)" stroke-width="3.5" stroke-dasharray="12 9"/>
 <rect x="674" y="236" width="208" height="76" fill="#fff" stroke="currentColor" stroke-width="3"/>
 <g class="mo" font-size="19" font-weight="700" text-anchor="middle" fill="currentColor"><text class="mo" x="778" y="268">MEDICAL</text><text class="mo" x="778" y="294">COLLEGES</text></g>
 <line x1="520" y1="150" x2="654" y2="150" stroke="var(--red)" stroke-width="6" stroke-dasharray="3 16" stroke-linecap="round"/>
 <circle cx="588" cy="80" r="36" fill="var(--red)"/><text class="se" x="588" y="97" text-anchor="middle" font-size="52" font-style="italic" fill="#fff">?</text></svg>
<p class="src">Sources: IIT Madras, Department of Medical Sciences and Technology and its BS in Medical Sciences and Engineering · IIT Kharagpur, School of Medical Science and Technology · IIT Kanpur, Gangwal School of Medical Sciences and Technology.</p></div>{foot(7)}</section>''')
# 08 NOT ANOTHER SUBJECT (insight with the wrong fix struck in red)
S.append(f'''<section class="slide" id="s08">{run("insight","The proposal")}
<h2 class="h" style="font-size:112px;margin-top:6px">Not another <span class="r" style="text-decoration:line-through;text-decoration-thickness:8px">compulsory subject.</span></h2>
<p class="sub" style="font-weight:600">An environment that makes research and innovation possible, for students who want to explore.</p>
<div class="art"><svg viewBox="0 0 904 300">
 <rect x="2" y="30" width="380" height="230" fill="none" stroke="var(--red)" stroke-width="4" stroke-dasharray="12 10"/>
 <text class="se" x="192" y="132" text-anchor="middle" font-size="34" font-weight="600" fill="var(--red)">Another</text><text class="se" x="192" y="182" text-anchor="middle" font-size="34" font-weight="600" fill="var(--red)">compulsory subject</text>
 <line x1="30" y1="124" x2="354" y2="124" stroke="var(--red)" stroke-width="6"/><line x1="30" y1="174" x2="354" y2="174" stroke="var(--red)" stroke-width="6"/>
 <path d="M430 150 H506 M480 122 L510 150 L480 178" fill="none" stroke="currentColor" stroke-width="6" stroke-linecap="round" stroke-linejoin="round"/>
 <circle cx="738" cy="150" r="148" fill="currentColor"/>
 <text class="se" x="738" y="132" text-anchor="middle" font-size="34" font-weight="600" font-style="italic" fill="#fff">An environment</text>
 <text class="se" x="738" y="178" text-anchor="middle" font-size="32" fill="#fff">that supports</text><text class="se" x="738" y="216" text-anchor="middle" font-size="32" fill="#fff">exploration</text></svg></div>{foot(8)}</section>''')
# 09 ECOSYSTEM
S.append(f'''<section class="slide" id="s09">{run("insight","Fig. 6")}
<h2 class="h" style="margin-top:6px">A medical student with the <span style="text-decoration:underline;text-decoration-thickness:6px;text-underline-offset:10px">people and tools</span> to try.</h2>
<div class="art"><svg viewBox="0 0 904 570">
 <g stroke="currentColor" stroke-width="3" stroke-dasharray="3 10" stroke-linecap="round"><line x1="452" y1="270" x2="452" y2="82"/><line x1="452" y1="270" x2="740" y2="196"/><line x1="452" y1="270" x2="640" y2="478"/><line x1="452" y1="270" x2="264" y2="478"/><line x1="452" y1="270" x2="164" y2="196"/></g>
 <circle cx="452" cy="270" r="100" fill="currentColor"/>
 <text class="se" x="452" y="268" text-anchor="middle" font-size="36" font-weight="600" fill="#fff">Medical</text><text class="se" x="452" y="310" text-anchor="middle" font-size="36" font-weight="600" fill="#fff">student</text>
 <g fill="#fff" stroke="currentColor" stroke-width="3.5"><rect x="312" y="30" width="280" height="90" rx="6"/><rect x="590" y="144" width="300" height="104" rx="6"/><rect x="486" y="432" width="308" height="92" rx="6"/><rect x="110" y="432" width="308" height="104" rx="6"/><rect x="6" y="144" width="316" height="104" rx="6"/></g>
 <g class="se" font-size="32" font-weight="600" text-anchor="middle" fill="currentColor">
  <text class="se" x="452" y="86">Mentorship</text><text class="se" x="740" y="208">Research</text><text class="se" x="640" y="488">Prototyping</text>
  <text class="se" x="264" y="476">Engineering</text><text class="se" x="264" y="514">partnerships</text>
  <text class="se" x="164" y="190" font-size="30">Clinical innovation</text><text class="se" x="164" y="228" font-size="30">challenges</text></g></svg>
<p class="cap">Fig. 6 — What the environment could offer.</p></div>{foot(9)}</section>''')
# 10 CAPABILITIES
col=lambda items,c:''.join(f'<div class="{c}">{t}</div>' for t in items)
S.append(f'''<section class="slide" id="s10">{run("insight","Fig. 7")}
<h2 class="h" style="margin-top:6px;font-size:84px">What medical college builds can be applied <span style="text-decoration:underline;text-decoration-thickness:6px;text-underline-offset:10px">far beyond</span> the clinic.</h2>
<div class="art"><div style="display:grid;grid-template-columns:1fr 70px 1fr;align-items:stretch">
 <div><p class="lab" style="margin-bottom:14px;color:var(--grey)">What training builds</p>{col(["Working under pressure","Deciding with incomplete information","Managing competing responsibilities","Working within resource limits"],"c1")}</div>
 <div style="display:flex;align-items:center;justify-content:center"><svg width="52" height="52" viewBox="0 0 52 52"><path d="M6 26 H44 M28 10 L46 26 L28 42" fill="none" stroke="#0B0B0B" stroke-width="6" stroke-linecap="round" stroke-linejoin="round"/></svg></div>
 <div><p class="lab" style="margin-bottom:14px">Where it can apply</p>{col(["Healthcare research","Product development","Entrepreneurship","Healthcare operations"],"c2")}</div></div>
<p class="cap" style="margin-top:20px">Fig. 7 — Skills built in training, and where else they can go.</p></div>{foot(10)}</section>''')
# 11 TWO THINGS (black)
S.append(f'''<section class="slide t-black" id="s11">{run("insight","The bigger vision")}
<h2 class="h" style="margin-top:6px">Two things, together.</h2>
<div class="art" style="display:grid">
 <div style="display:flex;gap:40px;align-items:baseline;padding:46px 0;border-top:3px solid #fff"><span style="font-family:var(--serif);font-style:italic;font-size:150px;line-height:.8;color:var(--red-on-black)">1</span><p style="font-family:var(--serif);font-size:70px;line-height:1.05;font-weight:600">Improve the education we provide.</p></div>
 <div style="display:flex;gap:40px;align-items:baseline;padding:46px 0;border-top:3px solid #fff;border-bottom:3px solid #fff"><span style="font-family:var(--serif);font-style:italic;font-size:150px;line-height:.8">2</span><p style="font-family:var(--serif);font-size:70px;line-height:1.05;font-weight:600">Expand what medical education can enable.</p></div></div>{foot(11)}</section>''')
# 12 CLOSING (black)
S.append(f'''<section class="slide t-black" id="s12">{run("insight","Article 001")}
<p style="font-family:var(--serif);font-weight:600;font-size:74px;line-height:1.06;margin-top:10px">A medical college should be more than a place where we learn medicine. It should be a place where we learn <u style="text-decoration-thickness:5px;text-underline-offset:9px">what we can do with it.</u></p>
<div style="margin-top:auto;display:flex;align-items:center;gap:30px"><img class="portrait" src="../../assets/author-portrait.jpg" alt="Dr. Sidharth Narayanan" style="width:150px;height:150px;border-radius:50%;border:4px solid #fff">
 <div><p style="font-family:var(--serif);font-size:42px;font-weight:600">Dr. Sidharth Narayanan</p><p class="cap" style="margin-top:8px;color:#fff;opacity:.85">House Surgeon, GMC Kozhikode<br>290+ days into internship</p></div></div>
<div style="margin:34px 0 100px;background:#fff;color:var(--black);padding:30px 36px"><p class="lab" style="color:var(--grey)">Read the full article</p><p style="font-family:var(--mono);font-size:30px;font-weight:700;margin-top:10px;color:var(--blue);white-space:nowrap">{URL}</p></div>{foot(12)}</section>''')
css='''.c1,.c2{padding:24px 26px;font-family:var(--serif);font-size:34px;line-height:1.15;font-weight:600;margin-bottom:14px;min-height:104px;display:flex;align-items:center}
.c1{border:3px solid var(--black)} .c2{background:var(--black);color:#fff}'''
body='\n'.join(S); import re as _re
parts=body.split('@@N@@'); total=len(parts)-1
body=''.join(p+(f'{i+1:02d} / {total:02d}' if i<total else '') for i,p in enumerate(parts))
open('slides.html','w').write(f'<!doctype html><html lang="en"><head><meta charset="utf-8"><title>BILMC 001 carousel</title><link rel="stylesheet" href="../../system/ledger.css"><style>{css}</style></head><body>\n'+body+'\n</body></html>')
print(len(S),'slides')

