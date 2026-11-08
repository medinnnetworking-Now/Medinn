# Builds slides.html for the Maanas Jain / Quintubate conversation (BILMC x PoH). Run: python3 build.py && NODE_PATH=$(npm root -g) node render.js
A='../../../assets/quintubate/'
def run(tag,label,color=''): return f'<div class="run" style="{color}"><span>Before I Leave Medical College · A conversation</span><span class="tag {tag}">{label}</span></div>'
def foot(color=''): return f'<div class="foot" style="{color}"><div><b>Dr. Sidharth Narayanan</b> <span>· House Surgeon, GMC Kozhikode</span></div><div class="n">@@N@@</div></div>'
S=[]
S.append(f'''<section class="slide" id="s01">{run("insight","Conversation 01")}
<img src="{A}uveal-cover.jpg" style="position:absolute;left:0;top:130px;width:1080px">
<div style="position:absolute;left:88px;right:88px;top:790px"><p class="lab" style="color:var(--grey);margin-bottom:16px">On medical education, from a house surgeon’s lens</p><h1 class="h" style="font-size:92px">A conversation with Dr. Maanas Jain.</h1><p class="sub" style="font-size:38px;margin-top:20px">The story of Quintubate.</p></div>{foot()}</section>''')
S.append(f'''<section class="slide" id="s02">{run("insight","The premise")}
<h2 class="h" style="font-size:88px;margin-top:6px">MBBS is the foundation of every doctor’s career. Right now, it feels <span class="r">undervalued.</span></h2>
<p class="sub">This series is about bringing that value back, and about what the foundation can lead to.</p>
<p class="sub" style="margin-top:40px;font-weight:600">This one sits between the series and People of Healthcare: a doctor who set out to build.</p>{foot()}</section>''')
S.append(f'''<section class="slide" id="s03">{run("insight","Meet")}
<h2 class="h" style="margin-top:6px;font-size:110px">Dr. Maanas Jain</h2>
<div style="margin-top:44px;display:grid;gap:0;font-family:var(--serif);font-size:48px;line-height:1.15;font-weight:600">
 <div style="padding:26px 0;border-top:3px solid var(--black)">Founder, Quintubate Pvt Ltd</div>
 <div style="padding:26px 0;border-top:3px solid var(--black)">MBBS, AIIMS Jodhpur</div>
 <div style="padding:26px 0;border-top:3px solid var(--black);border-bottom:3px solid var(--black)">Internal Medicine, Rutgers University, USA</div></div>
<p class="src" style="margin-top:20px">Source: Dr. Jain’s Instagram profile (@quintubate).</p>
<p class="sub" style="margin-top:auto;margin-bottom:100px;font-size:40px">Before starting residency, he set out to build Quintubate.</p>{foot()}</section>''')
S.append(f'''<section class="slide" id="s04">{run("critique","The gap")}
<h2 class="h" style="margin-top:6px;font-size:84px">A laryngoscope costs ₹1,000 to 2,000. A video-laryngoscope costs <span class="r">lakhs.</span></h2>
<div class="art"><img src="{A}price-frame.jpg" style="width:100%;display:block;border:4px solid var(--black)">
<p class="src">Source: figures as shown in Dr. Jain’s own video. ₹2,00,000 to ₹3,00,000 for a video-laryngoscope.</p></div>{foot()}</section>''')
S.append(f'''<section class="slide" id="s05">{run("evidence","The device")}
<h2 class="h" style="margin-top:6px;font-size:96px">UVEAL: turning the laryngoscope a hospital already has into a video-laryngoscope.</h2>
<p class="sub" style="font-size:38px">A universal video-enabling attachment that sends the view to a smartphone.</p>
<div class="art"><p class="src" style="font-size:22px;margin-top:0">Source: quintubate.com. The company describes UVEAL as smartphone-powered, compatible with existing laryngoscopes, and starting under ₹10,000; the video-laryngoscope comparison is the company’s own. The device is described by the company as CDSCO certified.</p></div>{foot()}</section>''')
S.append(f'''<section class="slide" id="s06">{run("evidence","In use")}
<h2 class="h" style="margin-top:6px;font-size:84px">A real intubation, at a government hospital.</h2>
<div class="art"><img src="{A}real-intubation-frame.jpg" style="width:100%;display:block;border:4px solid var(--black)">
<p class="src">Source: Dr. Jain’s video, captioned “A real intubation with UVEAL at Civil Hospital, Gandhinagar”.</p></div>{foot()}</section>''')
S.append(f'''<section class="slide" id="s07">{run("question","In conversation")}
<h2 class="h" style="margin-top:6px;font-size:88px">I asked him how a medical student starts building.</h2>
<div class="art"><img src="{A}conversation-frame.jpg" style="width:100%;display:block;border:4px solid var(--black)"><p class="cap">The conversation.</p></div>{foot()}</section>''')
def qa(i,q,tag):
    return f'''<section class="slide" id="s0{i}">{run("question",tag)}
<p class="lab" style="margin-top:6px;color:var(--grey)">I asked</p>
<h2 class="h" style="font-size:78px;margin-top:14px">{q}</h2>
<div class="art"><p class="lab" style="color:var(--blue);margin-bottom:14px">Dr. Jain</p>
<div style="border:4px dashed var(--blue);padding:44px;min-height:380px;font-family:var(--serif);font-size:40px;line-height:1.25;color:var(--blue)">[DRAFT: add his answer from your conversation, verbatim or lightly edited. Nothing is quoted until he approves.]</div></div>{foot()}</section>'''
S.append(qa(8,'What did you see in practice that made you want to build this?','Question 1'))
S.append(qa(9,'What stopped you, and what helped you start?','Question 2'))
S.append(qa(10,'What would you tell a student who has a problem and no idea where to begin?','Question 3'))
S.append(f'''<section class="slide" id="s11" style="background:#05070D;color:#EDF1FA">
<div style="position:absolute;right:-280px;top:-280px;width:900px;height:900px;border-radius:50%;background:radial-gradient(circle,rgba(66,110,230,.34),transparent 66%)"></div>
{run("insight","People of Healthcare","color:#EDF1FA").replace("tag insight","tag insight\" style=\"color:#EDF1FA")}
<h2 style="font-family:Bricolage,Helvetica,sans-serif;font-weight:800;font-size:104px;line-height:1.0;margin-top:6px;position:relative">Some doctors don’t wait. <span style="color:#6E95FF">They build.</span></h2>
<p style="font-size:42px;line-height:1.3;margin-top:36px;max-width:860px;position:relative;font-family:Inter,sans-serif">I am connecting with 50 healthcare and MedTech leaders and builders in Kerala before 2026 ends, through People of Healthcare.</p>
<div style="margin:auto 0 100px;background:linear-gradient(150deg,#1C3B9A,#0F1E52);border-radius:30px;padding:34px 40px;position:relative"><p class="lab" style="opacity:.8">Know someone building in healthcare?</p><p style="font-family:var(--mono);font-size:32px;font-weight:700;margin-top:10px">medinn.in/people-of-healthcare</p></div>{foot("color:#EDF1FA")}</section>''')
body='\n'.join(S); parts=body.split('@@N@@'); total=len(parts)-1
body=''.join(p+(f'{i+1:02d} / {total:02d}' if i<total else '') for i,p in enumerate(parts))
open('slides.html','w').write('<!doctype html><html lang="en"><head><meta charset="utf-8"><title>BILMC x PoH: Maanas Jain</title><link rel="stylesheet" href="../../../system/ledger.css"><style>@font-face{font-family:Bricolage;src:url(../../../../bricolage.woff2);font-weight:200 800}</style></head><body>\n'+body+'\n</body></html>')
print(len(S),'slides')
