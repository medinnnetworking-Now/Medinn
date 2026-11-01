# Turns takes.json into posters.html (one 1080x1350 poster per take). Critique = red, insight = black on white,
# question = black slide. Add a take to takes.json, run this, then render.js.
import json,html
d=json.load(open('takes.json')); out=[]
LABEL={'critique':'Critique','insight':'Insight','question':'The question','evidence':'Evidence'}
for i,t in enumerate(d['takes'],1):
    typ=t['type']; dark = typ=='question'
    cls='slide t-black' if dark else 'slide'
    head=html.escape(t['headline']); sup=html.escape(t.get('support',''))
    colour='var(--red)' if typ=='critique' else ('#fff' if dark else 'var(--black)')
    mark={'critique':'<div style="width:120px;height:14px;background:var(--red);margin-bottom:34px"></div>','insight':'<div style="width:120px;height:14px;background:var(--black);margin-bottom:34px"></div>','question':'<div style="font-family:var(--serif);font-style:italic;font-weight:300;font-size:340px;line-height:.6;color:var(--red-on-black);margin-bottom:60px">?</div>','evidence':''}[typ]
    size=96 if len(t['headline'])<95 else (84 if len(t['headline'])<150 else 72)
    out.append(f'''<section class="{cls}" id="p{i:02d}">
<div class="run"><span>Before I Leave Medical College · 001</span><span class="tag {typ}">{LABEL[typ]}</span></div>
<div style="margin-top:20px">{mark}<h2 class="h" style="font-size:{size}px;color:{colour}">{head}</h2>
{f'<p class="sub" style="margin-top:34px;font-size:40px;color:inherit">{sup}</p>' if sup else ''}</div>
<div style="margin-top:auto;margin-bottom:104px"><p class="src" style="font-size:22px">From the article: Medical College Is More Than a Training Ground for Doctors<br>{d['url']}</p></div>
<div class="foot"><div><b>Dr. Sidharth Narayanan</b> <span>· House Surgeon, GMC Kozhikode</span></div><div class="n">{i:02d}</div></div></section>''')
open('posters.html','w').write('<!doctype html><html lang="en"><head><meta charset="utf-8"><title>BILMC 001 posters</title><link rel="stylesheet" href="../../system/ledger.css"></head><body>\n'+'\n'.join(out)+'\n</body></html>')
print(len(out),'posters')
