# Variant A (journal article) in five colour palettes, one page each.
SER='BEFORE I LEAVE MED SCHOOL · RESEARCH'
T='I Want to Tell You How I Got Into Research'
P=[
 ('1','Navy and olive (current)','#14344A','#4F7A21','#C0342B','#FFF2B3','#f4f6f8','#e3efd3','#3a5e14','#f8d9d6','#b3261e','#ffe9b0','#7a5200','#14344A'),
 ('2','PubMed blue','#20558A','#2F6FA8','#B3261E','#FFF4C2','#eef4fa','#dcecf8','#1f5a8a','#fbdcd8','#9c241b','#ffe9b0','#7a5200','#20558A'),
 ('3','Wine and gold','#6B1D2A','#9A7B1E','#6B1D2A','#FBEFC4','#f7f3ee','#e6efd9','#3d5a1a','#f3d6d9','#8b1d2c','#f8e3a8','#6d5200','#6B1D2A'),
 ('4','Deep teal and coral','#0B4F5C','#1A8F8A','#D9534F','#FFF0C2','#eff7f7','#d6efe9','#0f6a52','#fde0dd','#b8352f','#ffe9b0','#7a5200','#0B4F5C'),
 ('5','Charcoal and orange','#1F2937','#E8590C','#C2410C','#FFEDD5','#f3f4f6','#dcfce7','#166534','#fee2e2','#b91c1c','#fef3c7','#92400e','#1F2937'),
]
ROWS=[('1','WHO STEPS 1 & 2 risk-factor survey (NCD)','Presented at national forums and UG conferences','NOT PUBLISHED','bad'),
('2','Nutritional assessment of cancer patients','Indian J Med Paediatr Oncol, Mar 2026','PUBLISHED','ok'),
('3','Metastatic solitary fibrous tumour, parapharyngeal','Indian J Med Paediatr Oncol, Apr 2025','PUBLISHED','ok'),
('4','Retrosternal goitre case series','Ongoing','IN PROGRESS','mid')]
out=['<!doctype html><meta charset="utf-8"><style>*{box-sizing:border-box;margin:0;padding:0}body{background:#777}.s{width:1080px;height:1350px;position:relative;overflow:hidden;margin-bottom:24px;display:flex;flex-direction:column;background:#fff;color:#1d2125;font-family:Arial,Helvetica,sans-serif}']
for n,name,nav,acc,red,hl,stripe,okb,okc,badb,badc,midb,midc,btn in P:
    out.append(f'''.p{n} .bar{{background:{nav};color:#fff;padding:26px 64px;display:flex;justify-content:space-between;font-size:22px;letter-spacing:.04em}}
.p{n} .tag{{color:{acc};font-size:28px;margin:46px 64px 0;border-bottom:4px solid {acc};padding-bottom:8px}}
.p{n} h1{{font-weight:400;font-size:80px;line-height:1.08;margin:30px 64px 0;letter-spacing:-.01em}}
.p{n} .au{{margin:26px 64px 0;font-size:30px}}.p{n} .id{{display:inline-block;width:30px;height:30px;border-radius:50%;background:#A6CE39;color:#fff;font:700 15px/30px Arial;text-align:center;vertical-align:middle;margin-left:6px}}
.p{n} .ab{{margin:34px 64px 0;font-family:'Times New Roman',Times,serif;font-size:34px;line-height:1.34}}.p{n} .ab p{{margin-top:12px}}.p{n} .ab b{{font-family:Arial;color:{red};font-size:27px;letter-spacing:.03em}}
.p{n} table{{border-collapse:collapse;margin:34px 64px 0;width:952px;font-size:22px}}.p{n} th{{background:{nav};color:#fff;text-align:left;padding:12px;font-size:19px;letter-spacing:.05em}}.p{n} td{{padding:13px 12px;border-bottom:1px solid #d4d8dc;vertical-align:top}}.p{n} tr:nth-child(even) td{{background:{stripe}}}.p{n} tr.hl td{{background:{hl}}}
.p{n} .chip{{font-weight:700;font-size:17px;padding:5px 10px;border-radius:4px;white-space:nowrap}}.p{n} .ok{{background:{okb};color:{okc}}}.p{n} .bad{{background:{badb};color:{badc}}}.p{n} .mid{{background:{midb};color:{midc}}}
.p{n} .btns{{margin:auto 64px 56px;display:flex;gap:14px;font-size:24px}}.p{n} .btns span{{border:2px solid {btn};color:{btn};padding:12px 24px;border-radius:6px;font-weight:700}}.p{n} .btns span.f{{background:{btn};color:#fff}}
.p{n} .lab{{position:absolute;right:30px;top:80px;background:{hl};color:#222;font:700 20px Arial;padding:8px 14px;border-radius:4px;border:2px solid {acc}}}''')
out.append('</style>')
for n,name,*_ in P:
    rows=''.join(f'<tr class="{"hl" if r[0]=="1" else ""}"><td>{r[0]}</td><td><b>{r[1]}</b></td><td>{r[2]}</td><td><span class="chip {r[4]}">{r[3]}</span></td></tr>' for r in ROWS)
    out.append(f'''<section class="s p{n}"><div class="bar"><b>{SER}</b><span>R01</span></div><div class="lab">PALETTE {n} · {name.upper()}</div>
<div class="tag">ORIGINAL EXPERIENCE · UNDERGRADUATE RESEARCH</div><h1>{T}</h1><div class="au">Sidharth Narayanan, MBBS <span class="id">iD</span></div>
<div class="ab"><p><b>BACKGROUND:</b> A lot of people get into undergraduate research to build a portfolio.</p><p><b>METHODS:</b> One drop year, and one person who believed in me.</p><p><b>RESULTS:</b> I joined college and forgot why I got there.</p><p><b>CONCLUSIONS:</b> The questions came back in second year.</p></div>
<table><tr><th>#</th><th>PROJECT</th><th>OUTPUT</th><th>STATUS</th></tr>{rows}</table>
<div class="btns"><span class="f">Cite</span><span>Save</span><span>Share</span></div></section>''')
open('palettes.html','w').write('\n'.join(out))
