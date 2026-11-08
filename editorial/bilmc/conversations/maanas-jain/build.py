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
 <div style="padding:26px 0;border-top:3px solid var(--black)">Founder and CTO, Quintubate Pvt Ltd</div>
 <div style="padding:26px 0;border-top:3px solid var(--black)">MBBS, AIIMS Jodhpur</div>
 <div style="padding:26px 0;border-top:3px solid var(--black);border-bottom:3px solid var(--black)">Internal Medicine, Rutgers University, USA</div></div>
<p class="src" style="margin-top:20px">Sources: Dr. Jain’s Instagram profile (@quintubate); his answers to People of Healthcare.</p>
<p class="sub" style="margin-top:auto;margin-bottom:100px;font-size:38px">Before starting residency, he set out to build Quintubate.</p>{foot()}</section>''')
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

def qa(i,tag,kind,q,ans,color='var(--black)',size=44):
    return f'''<section class="slide" id="q{i}">{run(kind,tag)}
<p class="lab" style="margin-top:6px;color:var(--grey)">I asked</p>
<h2 class="h" style="font-size:66px;margin-top:14px">{q}</h2>
<div class="art"><p class="lab" style="color:var(--blue);margin-bottom:16px">Dr. Maanas Jain</p>
<div style="border-left:10px solid {color};padding:6px 0 6px 36px;font-family:var(--serif);font-size:{size}px;line-height:1.22;font-weight:500">{ans}</div></div>{foot()}</section>'''
S.append(f'''<section class="slide" id="s07">{run("question","In conversation")}
<h2 class="h" style="margin-top:6px;font-size:88px">I asked him ten questions about building in Indian healthcare.</h2>
<div class="art"><img src="{A}conversation-frame.jpg" style="width:100%;display:block;border:4px solid var(--black)"><p class="cap">His answers, in his words, for People of Healthcare.</p></div>{foot()}</section>''')
S.append(qa(1,"What he is building","insight","What are you building?","“Quintubate is an initiative focussed on democratizing access to high-tech, expensive medical devices… at a sustainable cost for Indian healthcare.”"))
S.append(qa(2,"His flagship","evidence","What is your biggest project?","“UVEAL attaches to existing laryngoscopes and transforms them into cost-effective videolaryngoscopes… brings down the cost of videolaryngoscopy from the lakhs to the thousands. In a span of 6 months since commercialization, UVEAL is being used by 250+ doctors across India and 12 other countries.”","var(--blue)",40).replace("</div></div>{foot()}","</div><p class=\"src\">The 250+ doctors and 12 countries are Dr. Jain’s own figures.</p></div>{foot()}") if False else qa(2,"His flagship","evidence","What is your biggest project?","“UVEAL attaches to existing laryngoscopes and transforms them into cost-effective videolaryngoscopes… brings down the cost of videolaryngoscopy from the lakhs to the thousands. In a span of 6 months since commercialization, UVEAL is being used by 250+ doctors across India and 12 other countries.”","var(--blue)",40))
S.append(qa(3,"The bottleneck","critique","What are the bottlenecks you face?","“The medical device ecosystem is largely limited to a select few companies, all based internationally, and hence healthcare in India is not supportive of made-in-India devices. Clinicians are not aware, and are skeptical of Indian medical device startups.”","var(--red)",40))
S.append(qa(4,"The bridges","insight","What bridges need to be built?","“There needs to be an ecosystem for hospitals to learn about new licensed products developed by medical device startups as well as an incentive to adopt such indigenously designed devices. Regulators and medical colleges need to be on the lookout and supportive to push for the adoption of such devices to promote a culture of development.”","var(--black)",40))
S.append(qa(5,"Adoption","insight","How can we increase adoption and discovery?","“Fostering dialogue between medical device startups and existing hospitals, and having the opportunity to present the work to them would greatly enhance the chances of adoption.”","var(--black)",46))
S.append(qa(6,"The future","critique","How do you see the future of healthcare?","“The trend of medical devices is towards consolidation of all high-tech products in a select few companies, none of which are based in India. If Indian [doctors and hospitals] do not push for development and adoption of indigenous devices, medical device innovation in India will inevitably stagnate.”","var(--red)",40))
S.append(qa(7,"The opportunity","insight","What needs to be done?","“There is a big opportunity. Since very few medical devices are actually made in India, there is a huge scope for founders to pitch in and innovate to fill that large gap.”","var(--black)",46))
S.append(f'''<section class="slide" id="ask">{run("question","What he needs")}
<h2 class="h" style="margin-top:6px;font-size:84px">What he needs right now.</h2>
<div class="art" style="display:grid;gap:0;font-family:var(--serif);font-size:44px;line-height:1.15;font-weight:600">
 <div style="padding:30px 0;border-top:3px solid var(--black)">Meetings with hospitals and administrators, to explain the device and how it can be procured.</div>
 <div style="padding:30px 0;border-top:3px solid var(--black)">Access to grants for new prototype development.</div>
 <div style="padding:30px 0;border-top:3px solid var(--black);border-bottom:3px solid var(--black)">An introduction to hospital administrators and government healthcare officials.</div></div>{foot()}</section>''')
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
