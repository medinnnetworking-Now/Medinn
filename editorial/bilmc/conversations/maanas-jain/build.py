# v3: Article 002 carousel. Slides 1-2 in the Ledger series look, 3-12 in the PoH (Medinn dark blue) look.
A='../../../assets/quintubate/'; P='../../../assets/'
import illustrations as I
INK,ACC,BG='#EDF1FA','#6E95FF','#05070D'
def ill(f,u): return f(INK,ACC,BG,u)
def run(label,dark=False,tag='insight'):
    c='color:#EDF1FA' if dark else ''
    return f'<div class="run" style="{c}"><span>{"People of Healthcare" if dark else "Before I Leave Medical College · 002"}</span><span class="tag {tag}" style="{c}">{label}</span></div>'
def foot(dark=False):
    c='color:#EDF1FA' if dark else ''
    return f'<div class="foot" style="{c}"><div><b>Dr. Sidharth Narayanan</b> <span>· House Surgeon, GMC Kozhikode</span></div><div class="n">@@N@@</div></div>'
def poh(i,label,inner,tag='insight'):
    return f'''<section class="slide poh" id="s{i:02d}">{run(label,True,tag)}<div class="glow"></div><div style="position:relative;display:flex;flex-direction:column;flex:1">{inner}</div>{foot(True)}</section>'''
def quote(q,a,size=42):
    return f'<p class="pq">{q}</p><div class="pa" style="font-size:{size}px">{a}</div>'
S=[]
# 1 COVER (series look): hook + both photos
S.append(f'''<section class="slide" id="s01">{run("Article 002")}
<h1 class="h" style="font-size:90px;margin-top:4px">Before I leave medical college, I want to tell you about <span class="r">Quintubate.</span></h1>
<p class="sub" style="font-size:38px;margin-top:22px;margin-bottom:36px;font-weight:500">A video-laryngoscope costs lakhs. A doctor’s idea brings it to thousands.</p>
<div style="margin-top:auto;margin-bottom:104px;display:flex;gap:36px;align-items:flex-end">
 <div style="flex:1"><img src="{P}author-portrait.jpg" style="width:100%;aspect-ratio:1/1;object-fit:cover;object-position:50% 25%;border-radius:50%;border:4px solid var(--black);display:block"><p class="lab" style="margin-top:12px;font-size:20px"><b>Dr. Sidharth Narayanan</b><br><span style="color:var(--grey)">House Surgeon, GMC Kozhikode</span></p></div>
 <div style="flex:1"><img src="{A}maanas-circle.png" style="width:100%;aspect-ratio:1/1;object-fit:cover;border-radius:50%;border:4px solid var(--blue);background:#EDEFF1;display:block"><p class="lab" style="margin-top:12px;font-size:20px"><b>Dr. Maanas Jain</b><br><span style="color:var(--blue)">Founder and CTO, Quintubate</span></p></div></div>{foot()}</section>''')
# 2 PREMISE
S.append(f'''<section class="slide" id="s02">{run("The premise")}
<h2 class="h" style="font-size:92px;margin-top:6px">MBBS is the foundation of every doctor’s career. Right now, it feels <span class="r">undervalued.</span></h2>
<p class="sub">This series is about bringing that value back, and about what the foundation can lead to.</p>
<p class="sub" style="margin-top:44px;font-weight:600">So I asked someone who built on it.</p>
<p class="cap" style="margin-top:auto;margin-bottom:100px;font-size:24px;color:var(--black)">Next: People of Healthcare →</p>{foot()}</section>''')
# 3 SHIFT TO PoH
S.append(poh(3,"Meet",f'''<p class="lab" style="color:#6E95FF;margin-top:6px">People of Healthcare</p>
<p style="font-size:38px;line-height:1.3;margin-top:18px;max-width:880px">I am connecting with 50 healthcare and MedTech leaders and builders before 2026 ends. This is one of them.</p>
<div style="margin-top:46px;display:flex;gap:40px;align-items:center"><img src="{A}maanas-circle.png" style="width:300px;height:300px;object-fit:cover;border-radius:50%;border:3px solid #6E95FF;background:#EDEFF1">
<div><h2 class="ph">Dr. Maanas Jain</h2><p style="font-size:30px;line-height:1.35;margin-top:14px">Founder and CTO, Quintubate Pvt. Ltd.</p></div></div>
<div class="card" style="margin-top:44px"><p style="font-size:28px;line-height:1.4">MBBS, AIIMS Jodhpur<br>Internal Medicine, Rutgers University, USA<br>Before starting residency, he set out to build Quintubate.</p></div>
<p class="srcd" style="margin-top:18px">Sources: Dr. Jain’s Instagram profile (@quintubate); his answers to People of Healthcare.</p>'''))
# 4 GAP
S.append(poh(4,"The gap",f'''<h2 class="ph" style="font-size:80px">A laryngoscope costs ₹1,000 to 2,000. A video-laryngoscope costs <span class="pb">lakhs.</span></h2>
<div style="margin-top:auto;margin-bottom:96px">{ill(I.cost,'c4')}<p class="srcd">Drawn to scale. Video-laryngoscope figures as shown in Dr. Jain’s own video; the UVEAL figure is the company’s.</p></div>'''))
# 5 HOW IT WORKS
S.append(poh(5,"UVEAL",f'''<h2 class="ph" style="font-size:78px">UVEAL turns the laryngoscope a hospital already has into a video-laryngoscope.</h2>
<div style="margin-top:auto;margin-bottom:96px">{ill(I.device,'d5')}<p class="srcd">How it works: the laryngoscope already in the hospital, the attachment, and the phone already in the doctor’s pocket. Illustration, not to scale.</p></div>'''))
# 5b IN USE
S.append(poh(6,"In use",f'''<h2 class="ph" style="font-size:78px">A real intubation, at a government hospital.</h2>
<div style="margin-top:auto;margin-bottom:96px"><img src="{A}real-intubation-frame.jpg" style="width:100%;border-radius:24px;display:block"><p class="srcd">A real intubation with UVEAL at Civil Hospital, Gandhinagar (Dr. Jain’s video). The company states the device is CDSCO certified. Dr. Jain says 250+ doctors across India and 12 other countries use UVEAL.</p></div>'''))
# 6 Q1 Q2
S.append(poh(6,"In his words",quote("What are you building, and what do you want the world to know?","“Quintubate is an initiative focussed on democratizing access to high-tech, expensive medical devices… at a sustainable cost for Indian healthcare.” <br><br>“UVEAL brings down the cost of videolaryngoscopy from the lakhs to the thousands. In a span of 6 months since commercialization, UVEAL is being used by 250+ doctors across India and 12 other countries.”",36),'question'))
# 7 Q3
S.append(poh(7,"The bottleneck",quote("What are the bottlenecks you face?","“The medical device ecosystem is largely limited to a select few companies, all based internationally, and hence healthcare in India is not supportive of made-in-India devices. Clinicians are not aware, and are skeptical of Indian medical device startups.”",44)))
# 8 Q4 Q5
S.append(poh(8,"The bridges",quote("What bridges need to be built, and how do we increase adoption?","“There needs to be an ecosystem for hospitals to learn about new licensed products developed by medical device startups as well as an incentive to adopt such indigenously designed devices. Regulators and medical colleges need to be on the lookout and supportive.” <br><br>“Fostering dialogue between medical device startups and existing hospitals would greatly enhance the chances of adoption.”",34)))
S.append(poh(9,"The missing bridge",f'''<h2 class="ph" style="font-size:80px">Who builds the bridge between the startup and the hospital?</h2>
<div style="margin-top:auto;margin-bottom:96px">{ill(I.bridge,'b9')}<p class="srcd">An illustration of the gap Dr. Jain describes. Regulators, medical colleges and grants are the supports he names.</p></div>''',"question"))
# 9 Q8 Q9
S.append(poh(10,"The future",quote("How do you see the future of healthcare, and what needs to be done?","“If Indian [doctors and hospitals] do not push for development and adoption of indigenous devices, medical device innovation in India will inevitably stagnate.” <br><br>“There is a big opportunity. Since very few medical devices are actually made in India, there is a huge scope for founders to pitch in and innovate to fill that large gap.”",36)))
# 10 ASK
S.append(poh(11,"What he needs",f'''<h2 class="ph" style="font-size:88px">What he needs <span class="pb">right now.</span></h2>
<div style="margin-top:auto;margin-bottom:96px;display:grid;gap:18px">
 <div class="card"><p style="font-size:34px;line-height:1.3">Meetings with hospitals and administrators, to explain the device and how it can be procured.</p></div>
 <div class="card"><p style="font-size:34px;line-height:1.3">Access to grants for new prototype development.</p></div>
 <div class="card"><p style="font-size:34px;line-height:1.3">Introductions to hospital administrators and government healthcare officials.</p></div></div>''','question'))
# 11 MY TAKE
S.append(poh(12,"Why this matters",f'''<h2 class="ph" style="font-size:78px">A doctor sees a problem at the bedside. What happens next depends on whether anyone makes room for the solution.</h2>
<p style="font-size:36px;line-height:1.35;margin-top:44px;max-width:880px;opacity:.92">MBBS is where doctors learn to see what needs fixing. The next step needs hospitals willing to look, grants, and a culture that adopts what is built here.</p>
<div style="margin-top:auto;margin-bottom:96px;display:flex;gap:26px;align-items:center"><img src="{A}conversation-frame.jpg" style="width:300px;height:170px;object-fit:cover;border-radius:18px"><p class="srcd" style="margin:0">The conversation with Dr. Jain.</p></div>'''))
# 13 CLOSE + CTA
S.append(poh(13,"Your turn",f'''<h2 class="ph" style="font-size:96px">Some doctors don’t wait. <span class="pb">They build.</span></h2>
<p style="font-size:40px;line-height:1.3;margin-top:30px;max-width:880px">Know a hospital administrator, regulator or grant-maker who should meet Dr. Jain?</p>
<div class="box" style="margin-top:auto;margin-bottom:96px;display:flex;gap:34px;align-items:center"><img src="{A}qr-introduce.png" style="width:230px;height:230px;border-radius:16px;background:#fff">
<div><p class="lab" style="opacity:.8">Introduce him through Medinn</p><p style="font-size:32px;line-height:1.25;margin-top:10px;font-weight:700">Scan, or send a WhatsApp message to Medinn</p>
<p class="lab" style="opacity:.8;margin-top:20px">Read the article</p><p style="font-family:var(--mono);font-size:22px;font-weight:700;margin-top:6px;word-break:break-all">medinn.in/before-i-leave-medical-college/some-doctors-dont-wait</p></div></div>'''))
body='\n'.join(S); parts=body.split('@@N@@'); total=len(parts)-1
body=''.join(p+(f'{i+1:02d} / {total:02d}' if i<total else '') for i,p in enumerate(parts))
css='''@font-face{font-family:Bricolage;src:url(../../../../bricolage.woff2);font-weight:200 800}
.poh{background:#05070D;color:#EDF1FA}.poh .glow{position:absolute;right:-280px;top:-280px;width:900px;height:900px;border-radius:50%;background:radial-gradient(circle,rgba(66,110,230,.34),transparent 66%)}
.poh .run,.poh .foot{color:#EDF1FA}.poh .tag{border-color:#EDF1FA}.poh .tag.question{background:#6E95FF;color:#05070D;border-color:#6E95FF}
.ph{font-family:Bricolage,Helvetica,sans-serif;font-weight:800;font-size:96px;line-height:1.02;letter-spacing:-.01em}.pb{color:#6E95FF}
.pq{font-family:Bricolage,Helvetica,sans-serif;font-weight:700;font-size:56px;line-height:1.08;margin-top:4px}
.pa{margin-top:auto;margin-bottom:96px;background:#0D1220;border:1px solid rgba(190,210,255,.2);border-left:8px solid #6E95FF;border-radius:22px;padding:34px 38px;font-family:Inter,sans-serif;line-height:1.32;font-weight:500}
.card{background:#0D1220;border:1px solid rgba(190,210,255,.2);border-radius:24px;padding:26px 32px}
.box{background:linear-gradient(150deg,#1C3B9A,#0F1E52);border-radius:30px;padding:30px 38px}
.srcd{font-family:var(--mono);font-size:20px;line-height:1.45;color:#8E9AB3;margin-top:14px}'''
open('slides.html','w').write('<!doctype html><html lang="en"><head><meta charset="utf-8"><title>BILMC 002 x PoH: Maanas Jain</title><link rel="stylesheet" href="../../../system/ledger.css"><style>'+css+'</style></head><body>\n'+body+'\n</body></html>')
print(len(S),'slides')
