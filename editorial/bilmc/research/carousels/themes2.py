# Journal base + arcade fonts + marker highlights (marker), and handwritten versions (ballpoint, fountain). Content from soft.py.
import soft
from soft import R01,R02,ROWS,SER,e
from themes import hd_j,ft,build as _b
F='../fonts/'
def mk(c,op='.9'): return f"url(\"data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 200 40' preserveAspectRatio='none'><path d='M3 9 Q60 2 120 6 T197 4 L199 15 Q196 28 198 35 Q120 40 60 37 T4 38 L1 24 Q4 16 3 9 Z' fill='{c}' fill-opacity='{op}'/></svg>\")"
YEL,PNK,MNT,CYN='%23FFE14D','%23FF9EC4','%238BF0C7','%237FDFFF'
FACE=f'''@font-face{{font-family:Bricolage;src:url(../../../../bricolage.woff2);font-weight:200 800}}@font-face{{font-family:Mono;src:url(../../../essays/fonts/mono-normal.woff2)}}
@font-face{{font-family:Caveat;src:url({F}Caveat.ttf);font-weight:400 700}}@font-face{{font-family:Aurore;src:url({F}WaitingForTheSunrise.ttf)}}'''
BASE=FACE+f'''*{{box-sizing:border-box;margin:0;padding:0}}body{{background:#999}}
.s{{width:1080px;height:1350px;position:relative;overflow:hidden;margin-bottom:24px;display:flex;flex-direction:column;background:var(--paper,#fff);color:var(--ink,#111);padding:0 96px;font-family:'Times New Roman',Times,serif}}
.hd{{margin-top:56px;display:flex;justify-content:space-between;font:400 19px Mono,monospace;letter-spacing:.1em;color:#20558A;padding-bottom:12px;border-bottom:1px solid #20558A;flex:none;position:relative}}.hd:after{{content:'';position:absolute;left:0;right:0;bottom:-6px;border-bottom:3px solid #20558A}}.hd i{{font-style:normal;color:#555}}
.kick{{margin-top:62px;font:400 22px Mono,monospace;letter-spacing:.12em;color:#B3261E;font-weight:500}}
h1,h2{{font-family:Bricolage,Arial,sans-serif;font-weight:800;letter-spacing:-.03em;line-height:1.02}}h1{{font-size:92px;margin-top:22px}}h2{{font-size:74px;margin-top:22px}}
h1 b,h2 b{{font-weight:800;color:inherit;background-image:{mk(YEL)};background-size:100% 78%;background-position:0 78%;background-repeat:no-repeat;padding:0 .12em;margin:0 -.04em;-webkit-box-decoration-break:clone;box-decoration-break:clone}}
.sub{{font:italic 400 42px/1.3 'Times New Roman',serif;margin-top:28px;color:#333}}.au{{font:400 22px Mono,monospace;margin-top:30px;color:#333}}.id{{display:inline-block;width:22px;height:22px;border-radius:50%;background:#A6CE39;color:#fff;font:700 11px/22px Arial;text-align:center;margin-left:6px}}
.p{{margin-top:32px;font:400 56px/1.38 'Times New Roman',serif}}
.p em{{font-style:normal;background-image:{mk(YEL)};background-size:100% 85%;background-position:0 80%;background-repeat:no-repeat;padding:0 .14em;margin:0 -.05em;-webkit-box-decoration-break:clone;box-decoration-break:clone}}
.p em:nth-of-type(2n){{background-image:{mk(PNK)}}}
.steps{{margin-top:30px;display:grid;gap:6px}}.st{{display:grid;grid-template-columns:96px 1fr;gap:22px;padding:20px 0;border-bottom:1px solid #aaa;align-items:center}}
.st .n{{width:84px;height:76px;font:800 50px/76px Bricolage;text-align:center;background:{mk(YEL)} center/100% 100% no-repeat}}.st:nth-child(2) .n{{background-image:{mk(MNT)}}}.st:nth-child(3) .n{{background-image:{mk(PNK)}}}.st:nth-child(4) .n{{background-image:{mk(CYN)}}}.st:nth-child(5) .n{{background-image:{mk(YEL)}}}
.st b{{font:800 36px Bricolage,Arial;display:block}}.st span{{font:400 38px/1.3 'Times New Roman',serif;display:block;margin-top:4px;color:#222}}
.note{{margin-top:30px;font:500 26px Mono,monospace;color:#B3261E}}.src{{font:400 17px Mono,monospace;color:#666;margin-top:16px}}svg{{margin-top:26px}}
table{{border-collapse:collapse;width:100%;font:400 18px Arial;margin-top:16px;border-top:3px solid #111;border-bottom:3px solid #111}}th{{text-align:left;padding:10px 8px;font:500 14px Mono,monospace;letter-spacing:.08em;border-bottom:1.5px solid #111}}td{{padding:10px 8px;border-bottom:1px solid #ccc;vertical-align:top}}tr.hl td{{background:#FFF1A8}}
.chip{{font:500 13px Mono,monospace;letter-spacing:.04em;white-space:nowrap}}.ok{{color:#20558A}}.bad{{color:#B3261E}}.mid{{color:#8a6100}}
.path{{margin-top:22px;border-top:2px solid #111}}.pn{{display:grid;grid-template-columns:96px 1fr;gap:18px;align-items:baseline;padding:14px 0;border-bottom:1px solid #aaa}}.pn .c{{font:800 28px Bricolage;color:#20558A}}.pn.on .c{{color:#B3261E}}.pn b{{font:800 34px Bricolage,Arial;display:block}}.pn span{{font:400 31px 'Times New Roman',serif;display:block;color:#222}}.pn em{{font:500 14px Mono,monospace;font-style:normal;color:#B3261E;margin-left:12px}}
.big{{display:flex;align-items:flex-end;gap:26px;margin-top:28px}}.big .n{{font:800 230px/0.8 Bricolage;letter-spacing:-.05em;color:#111;background-image:{mk(YEL)};background-size:100% 40%;background-position:0 88%;background-repeat:no-repeat;padding-right:.05em}}.big .t{{font:800 52px/1.08 Bricolage;padding-bottom:12px}}.big .t b{{font-weight:800;color:inherit;background-image:{mk(PNK)};background-size:100% 72%;background-position:0 80%;background-repeat:no-repeat;padding:0 .1em}}
.hookline{{font:italic 400 42px/1.3 'Times New Roman',serif;margin-top:22px;color:#222}}.tbl{{margin-top:22px;font:500 15px Mono,monospace;letter-spacing:.1em;color:#20558A}}
.pills{{margin-top:auto;margin-bottom:96px;display:flex;gap:14px}}.pills span{{font:500 21px Mono,monospace;border:1.5px solid #20558A;color:#20558A;padding:10px 22px}}.pills .f{{background:#20558A;color:#fff}}
.ft{{position:absolute;left:96px;right:96px;bottom:36px;display:flex;justify-content:space-between;font:400 17px Mono,monospace;color:#666;border-top:1px solid #999;padding-top:12px}}
.hand{{display:none}}'''
BP=f'''.s{{--ink:#14309a}}.p,.sub,.st span,.pn span,.hookline,.note{{font-family:Caveat,cursive;color:#14309a;text-shadow:0 0 .5px rgba(20,48,154,.6)}}
.p{{font-size:76px;line-height:1.12;font-weight:500}}.sub{{font-size:58px;font-style:normal;line-height:1.1}}.st span{{font-size:50px;line-height:1.1}}.pn span{{font-size:42px}}.hookline{{font-size:56px;font-style:normal;line-height:1.1}}.note{{font-size:52px;color:#B3261E;font-weight:600}}
h1,h2,.st b,.pn b,.big .t{{font-family:Caveat,cursive;font-weight:700;color:#14309a;letter-spacing:0}}h1{{font-size:118px;line-height:.98}}h2{{font-size:100px;line-height:.98}}.st b{{font-size:54px}}.pn b{{font-size:48px}}.big .t{{font-size:78px}}.big .n{{font-family:Caveat,cursive;font-weight:700;color:#14309a;font-size:260px}}.st .n{{font-family:Caveat,cursive;font-size:70px;color:#14309a}}.pn .c{{font-family:Caveat,cursive;font-size:40px}}
.hand{{display:block;font:600 50px Caveat,cursive;color:#B3261E;transform:rotate(-2deg);margin-top:18px}}.s{{background-image:linear-gradient(90deg,transparent 0 70px,rgba(215,70,60,.35) 70px 72px,transparent 72px)}}'''
FP=f'''.s{{--paper:#FFFDF6;--ink:#16245c}}.p,.sub,.st span,.pn span,.hookline,.note{{font-family:Aurore,cursive;color:#16245c;text-shadow:0 0 1.2px rgba(22,36,92,.7)}}
.p{{font-size:72px;line-height:1.22}}.sub{{font-size:58px;font-style:normal;line-height:1.25}}.st span{{font-size:44px;line-height:1.25}}.pn span{{font-size:36px}}.hookline{{font-size:50px;font-style:normal;line-height:1.25}}.note{{font-size:46px;color:#9b1c1c}}
h1,h2,.st b,.pn b,.big .t{{font-family:Aurore,cursive;font-weight:400;color:#16245c;letter-spacing:0;text-shadow:0 0 1.6px rgba(22,36,92,.6)}}h1{{font-size:124px;line-height:1.0}}h2{{font-size:104px;line-height:1.0}}.st b{{font-size:50px}}.pn b{{font-size:44px}}.big .t{{font-size:72px}}.big .n{{font-family:Aurore,cursive;font-weight:400;color:#16245c;font-size:250px}}.st .n{{font-family:Aurore,cursive;font-size:64px;color:#16245c}}.pn .c{{font-family:Aurore,cursive;font-size:36px}}
.hand{{display:block;font:400 50px Aurore,cursive;color:#9b1c1c;transform:rotate(-2deg);margin-top:18px}}'''
BP+=""".big{margin-top:12px}.big .n{font-size:190px}.hookline{margin-top:8px}.tbl{margin-top:12px}.hand{margin-top:6px}.path{margin-top:12px}.pn{padding:8px 0}.st{padding:12px 0}.steps{margin-top:18px;gap:2px}.p{margin-top:22px}.hookline{{font-size:46px}}.hand{{font-size:42px}}.pn b{{font-size:40px}}.pn span{{font-size:34px}}.st span{{font-size:42px}}.st b{{font-size:46px}}""".replace('{{','{').replace('}}','}')
FP+=""".big{margin-top:12px}.big .n{font-size:190px}.hookline{margin-top:8px}.tbl{margin-top:12px}.hand{margin-top:6px}.path{margin-top:12px}.pn{padding:8px 0}.st{padding:12px 0}.steps{margin-top:18px;gap:2px}.p{margin-top:22px}.hookline{{font-size:40px}}.hand{{font-size:38px}}.pn b{{font-size:32px}}.pn span{{font-size:26px}}.pn{{padding:4px 0}}.st span{{font-size:36px}}.st b{{font-size:42px}}.p{{font-size:56px}}.h2{{}}""".replace('{{','{').replace('}}','}')
import os
LOGO='../../../assets/cmc-analytica-logo.png'; JJ='../../../assets/jerin-james.jpg'
def logo_html():
    return (f'<img src="{LOGO}" style="height:260px;width:auto;flex:none;object-fit:contain;display:block">' if os.path.exists(LOGO) else '<div style="height:84px;padding:0 24px;border:3px dashed #20558A;color:#20558A;font:500 22px Mono,monospace;display:flex;align-items:center;letter-spacing:.08em">CMC ANALYTICA<br>[LOGO HERE]</div>')
def photo_html(src,name,role,ph):
    img=(f'<img src="{src}" style="width:140px;height:140px;border-radius:50%;object-fit:cover;border:4px solid #111">' if os.path.exists(src) else f'<div style="width:140px;height:140px;border-radius:50%;border:3px dashed #aaa;display:flex;align-items:center;justify-content:center;font:400 16px Mono,monospace;color:#888;text-align:center">{ph}</div>')
    return f'<div style="display:flex;align-items:center;gap:22px">{img}<div><div style="font:800 38px Bricolage,Arial">{name}</div><div style="font:400 20px Mono,monospace;color:#555;margin-top:6px">{role}</div></div></div>'
def cover2(art):
    return f'<div style="margin-top:20px">{logo_html()}</div><h1 style="font-size:78px;margin-top:10px">{art["title_html"]}</h1><div class="sub" style="font-size:36px;margin-top:16px">{e(art["sub"])}</div><div style="margin-top:auto;margin-bottom:96px"><div style="font:800 38px Bricolage,Arial">Dr. Sidharth Narayanan <span style="font:400 24px Mono,monospace;color:#555">· 2020 MBBS batch</span></div><div style="font:800 38px Bricolage,Arial;margin-top:10px">Dr. Jerin James <span style="font:400 24px Mono,monospace;color:#555">· 2020 MBBS batch</span></div></div>'
def ft2(i,n,art): return f'<div class="ft"><span>{"CMC Analytica · Calicut Medical College · College Union · 2026–2027" if art["id"]=="R02" else "Dr. Sidharth Narayanan · House Surgeon, GMC Kozhikode"}</span><span>{i:02d} / {n:02d}</span></div>'
def hd_j2(art,i,n):
    lg=f'<img src="{LOGO}" style="height:46px;width:auto;flex:none;object-fit:contain;margin:0 18px">' if os.path.exists(LOGO) and art['id']=='R02' and i>1 else ''
    return f'<div class="hd"><span>{SER.upper()}</span>{lg}<i>PART {art["id"][-1]} · {i}/{n}</i></div>'
def hook(art,hand):
    t=soft.table('1')
    return f'<div class="kick">UNDERGRADUATE RESEARCH · A DATA STORY</div><div class="big"><div class="n">8</div><div class="t">research projects<br><b>so far.</b></div></div><div class="hookline">Most people get into research for a portfolio. I got into it purely because I loved reading, building on it and building a narrative.</div><div class="tbl">TABLE 1 · THE RESEARCH LEDGER</div>'+t+(f'<div class="hand">↑ #1 won an award. It never got published.</div>' if hand else '')
def build(art,theme,name,css,hand):
    sl=list(art['slides']);n=len(sl);out=''
    for i,(kick,inner) in enumerate(sl,1):
        if inner is None:
            inner=f'<h1>{art["title_html"]}</h1><div class="sub">{e(art["sub"])}</div><div class="au">Sidharth Narayanan, MBBS <span class="id">iD</span></div><div class="pills"><span class="f">Cite</span><span>Save</span><span>Share</span><span>Swipe →</span></div>'
        kk=f'<div class="kick">{kick}</div>'
        if kick=='HOOK': inner=hook(art,hand); kk=''
        if art['id']=='R02' and inner.startswith('<h1>'): inner=cover2(art)
        out+=f'<section class="s" id="s{i}">{hd_j2(art,i,n)}{kk}{inner}{ft2(i,n,art)}</section>'
    open(f'{name}.html','w').write(f'<!doctype html><meta charset="utf-8"><style>{BASE}{css}</style>{out}')
for a,nm in ((R01,'r01'),(R02,'r02')):
    build(a,'m',f'{nm}-marker','',False); build(a,'b',f'{nm}-ballpoint',BP,True); build(a,'f',f'{nm}-fountain',FP,True)
print('themes2 ok')
