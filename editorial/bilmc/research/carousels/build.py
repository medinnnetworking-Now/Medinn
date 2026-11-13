import sys,html
sys.path.insert(0,'.')
from content import *
NAV,ACC,RED,HL,STRIPE='#20558A','#2F6FA8','#B3261E','#FFF4C2','#eef4fa'
CSS=f'''*{{box-sizing:border-box;margin:0;padding:0}}body{{background:#777}}
.s{{width:1080px;height:1350px;position:relative;overflow:hidden;margin-bottom:24px;display:flex;flex-direction:column;background:#fff;color:#1d2125;font-family:Arial,Helvetica,sans-serif}}
.bar{{background:{NAV};color:#fff;padding:26px 64px;display:flex;justify-content:space-between;font-size:22px;letter-spacing:.04em;font-weight:700}}
.tag{{color:{ACC};font-size:28px;margin:46px 64px 0;border-bottom:4px solid {ACC};padding-bottom:8px;letter-spacing:.02em}}
h1{{font-weight:400;font-size:80px;line-height:1.06;margin:32px 64px 0;letter-spacing:-.01em}}
.au{{margin:26px 64px 0;font-size:30px}}.id{{display:inline-block;width:30px;height:30px;border-radius:50%;background:#A6CE39;color:#fff;font:700 15px/30px Arial;text-align:center;vertical-align:middle;margin-left:6px}}
.hook{{margin:30px 64px 0;border-left:10px solid {ACC};padding:8px 0 8px 28px;font-size:44px;line-height:1.15;font-weight:700}}
.ab{{margin:30px 64px 0;font-family:'Times New Roman',Times,serif;font-size:31px;line-height:1.3}}.ab p{{margin-top:12px}}.ab b{{font-family:Arial;color:{RED};font-size:27px;letter-spacing:.03em}}
.lab{{margin:60px 64px 0;font-weight:700;color:{RED};font-size:34px;letter-spacing:.05em}}
.txt{{margin:26px 64px 0;font-family:'Times New Roman',Times,serif;line-height:1.3}}
.txt p+p{{margin-top:.7em}}
.quote{{margin:50px 64px 0;border-left:10px solid {ACC};padding:8px 0 8px 30px;font-family:Arial;font-weight:700;line-height:1.12}}
table{{border-collapse:collapse;margin:34px 64px 0;width:952px;font-size:23px}}th{{background:{NAV};color:#fff;text-align:left;padding:13px 12px;font-size:19px;letter-spacing:.05em}}td{{padding:15px 12px;border-bottom:1px solid #d4d8dc;vertical-align:top}}tr:nth-child(even) td{{background:{STRIPE}}}tr.hl td{{background:{HL}}}
.chip{{font-weight:700;font-size:17px;padding:5px 10px;border-radius:4px;white-space:nowrap}}.ok{{background:#dcecf8;color:#1f5a8a}}.bad{{background:#fbdcd8;color:#9c241b}}.mid{{background:#ffe9b0;color:#7a5200}}
.btns{{margin:auto 64px 90px;display:flex;gap:14px;font-size:24px}}.btns span{{border:2px solid {NAV};color:{NAV};padding:12px 24px;border-radius:6px;font-weight:700}}.btns span.f{{background:{NAV};color:#fff}}
.ft{{position:absolute;bottom:26px;left:64px;right:64px;font-size:20px;color:#667;display:flex;justify-content:space-between;border-top:2px solid #d4d8dc;padding-top:14px}}
.na{{color:#B3261E;font-weight:700;font-family:'JetBrains Mono',monospace}}'''
def e(t): return html.escape(t)
def slide(art,i,n,inner,tag):
    return f'<section class="s"><div class="bar"><span>{SER.upper()}</span><span>{art["id"]} · {i}/{n}</span></div><div class="tag">{tag}</div>{inner}<div class="ft"><span>Dr. Sidharth Narayanan · House Surgeon, GMC Kozhikode</span><span>{i:02d} / {n:02d}</span></div></section>'
def table(hl):
    rows=''.join(f'<tr class="{"hl" if r[0]==hl else ""}"><td>{r[0]}</td><td><b>{e(r[1])}</b></td><td>{e(r[2])}</td><td><span class="chip {r[4]}">{r[3]}</span></td></tr>' for r in ROWS)
    return f'<table><tr><th>#</th><th>PROJECT</th><th>OUTPUT</th><th>STATUS</th></tr>{rows}</table>'
def text(label,paras,size=52,tag='RESULTS'):
    return f'<div class="lab">{label}</div><div class="txt" style="font-size:{size}px">'+''.join(f'<p>{e(p)}</p>' for p in paras)+'</div>'
def quote(t,size=64): return f'<div class="quote" style="font-size:{size}px">{e(t)}</div>'
def cover(art,tagline):
    ab=''.join(f'<p><b>{k}:</b> {e(v)}</p>' for k,v in art['abstract'])
    big=len(art["title"])>50
    return f'<h1 style="{"font-size:60px" if big else ""}">{e(art["title"])}</h1><div class="au">Sidharth Narayanan, MBBS <span class="id">iD</span></div><div class="hook">{e(art["hook"])}</div><div class="ab" style="{"font-size:27px" if big else ""}">{ab}</div><div class="btns"><span class="f">Cite</span><span>Save</span><span>Share</span><span>{tagline}</span></div>'
S1=[]  # R01
def add(L,art,tag,inner): L.append((tag,inner))
r1=[('ORIGINAL EXPERIENCE · UNDERGRADUATE RESEARCH',cover(R01,'Swipe →')),
('BACKGROUND',text('BACKGROUND',['A lot of people get into undergraduate research for the sole purpose of building a portfolio so that they can go abroad, write the USMLE exam, or see it as a clearance aspect for their PLAB or AMC exams.'],56)),
('THE DIFFERENCE',quote('But I saw it from a different perspective.',78)+quote('It all started with how I got into MBBS in the first place.',60)),
('METHODS',text('METHODS',['I studied at PC Thomas Classes, and just before my drop year, I was influenced by an individual who believed in me quite a lot.','He told me all about whole-food, plant-based diets and veganism. He was a vegan himself.'],56)),
('METHODS',text('METHODS',['He talked to me about Dr. Michael Greger, Neal Barnard, and the greats who had been working on preventive medicine and the Physicians Committee for Responsible Medicine.','This was even before I had even seen a medical college for the first time.'],52)),
('SKEPTICISM',text('SKEPTICISM',['He showed me Cowspiracy, Seaspiracy and all these movies that showed us what happens when you consume a lot of meat.','I was skeptical about a lot of this, but yet I listened to him because whole-food, plant-based diets did have substance to them. And I kept that close to my heart.'],48)),
('THE CROSSROADS',text('THE CROSSROADS',['I was very infuriated and washed away by the amount of time invested into NEET UG preparation. I had enough of it.','After my first attempt, I had enough marks to get into veterinary medicine or BDS, and I had decided that I would take whatever I got.'],50)),
('THE CROSSROADS',quote('I told my mom and dad that I wanted to give it another go.',70)+'<div class="txt" style="font-size:44px;margin-top:40px"><p>And that’s how I decided to drop and repeat for an MBBS seat.</p></div>'),
('RESULTS',text('RESULTS',['When I joined college, I was actually consumed by the need to fit in, to be validated, to be understood, to be loved.','I discussed these ideas with some of them in the initial days, but I was ridiculed for a while. I guess I just pushed them all out.'],52)),
('RESULTS',text('RESULTS',['COVID twice. College dynamics, politics, arts. All of it took up a lot of my attention.','I forgot about that guardian angel who actually took me to medical college. I forgot all the whys and hows of why I got there.'],52)),
('CONCLUSIONS',text('CONCLUSIONS',['But you could say that all these decisions led me to where I am right now.'],58)+quote('I didn’t know then that these ideas would eventually become the foundation of my interest in research.',50)+'<div class="btns" style="margin-top:auto"><span class="f">Next: R02 →</span><span>Cite</span><span>Share</span></div>')]
r2=[('ORIGINAL EXPERIENCE · UNDERGRADUATE RESEARCH',cover(R02,'Swipe →')),
('BACKGROUND',text('BACKGROUND',['While in second year, I started going department by department, ward by ward, trying to understand oncology and nutrition and what was being done.'],56)),
('OBSERVATION',quote('Why were the diet books always empty?',76)+'<div class="txt" style="font-size:44px;margin-top:40px"><p>I tried to understand if there was a nutritionist on board, why the diet books were always filled up with renal-related diets, and the diet was always just milk and eggs.</p></div>'),
('REVIEW OF LITERATURE',text('REVIEW OF LITERATURE',['So I started reading. I started going into journals. I started looking up random terms in oncology, trying to understand what a review of literature was.','So who was assessing whether the people in Malabar were getting higher cancer rates due to this very rate of consumption?'],50)),
('NARROWING IT DOWN',text('NARROWING IT DOWN',['My dear professor and HOD, Dr. Asma Rahim, and Dr. Ashik Refeek told me to narrow it down.','We started making it into nutritional assessment of patients, and then we modified it to cancer patients.','I took this very project to Dr. Sanudev. He told me we could do it, and then I let go of that project for a while.'],44)),
('METHODS',text('METHODS',['It was an initiative by the then College Union to run a health camp.','A lot of data would come in, a lot of tests would be done. Why waste it if we could assess the health metrics and risk factors of all the students on campus?'],50)),
('METHODS',text('METHODS',['We drafted a protocol based on the WHO STEPS 1 and 2 programme, where we assess the risk factors for NCDs.','With Institutional Research Committee approval and Ethics Committee approval.'],54)),
('RESULTS',text('RESULTS',['It took another one and a half years for me to get into the data, understand it and learn how to process it using SPSS and Excel formulas.','We eventually managed to prepare a report and present it at national forums and undergraduate conferences.'],50)),
('LIMITATIONS',quote('To this day, I believe we spread ourselves too thin.',70)+'<div class="txt" style="font-size:48px;margin-top:44px"><p>Too much data. Far too much data. Unsegmented, without the necessary tools or the team to understand the data, structure it properly or even publish it.</p></div>'),
('CONCLUSIONS',text('CONCLUSIONS',['The project eventually earned me the KUHS UG Research Award.','But to my dismay, I was never able to publish it.'],40)+table('1')+'<div style="margin:30px 64px 0;font-family:Times,serif;font-size:36px">That is something that will always bother me. And it is something that I will owe the people who made it possible, and the campus, for a while.</div>'),
('NEXT',quote('Next: the electives. Juvenile justice, oncology and nutrition.',66)+'<div class="btns" style="margin-top:auto"><span class="f">R03 →</span><span>Cite</span><span>Share</span></div>')]
for art,sl,name in ((R01,r1,'r01'),(R02,r2,'r02')):
    n=len(sl)
    # cover has its own footer so use the same wrapper
    out=''.join(slide(art,i+1,n,inner,tag) for i,(tag,inner) in enumerate(sl))
    open(f'{name}.html','w').write(f'<!doctype html><meta charset="utf-8"><style>{CSS}</style>{out}')
print('ok')
