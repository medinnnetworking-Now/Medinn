# Two more carousel themes for R01 and R02: "quest" (arcade, pop) and "journal" (classic, light, readable). Content comes from soft.py.
import html,copy
import soft
from soft import R01,R02,ROWS,SER,e
SHORT={'1':'WHO STEPS 1&2 NCD survey','2':'Nutrition assessment, cancer patients','3':'Metastatic solitary fibrous tumour','4':'Juvenile justice and recidivism','5':'Obesity-driven cardiac mortality','6':'Retrosternal goitre case series','7':'AI-enabled dataset creation','8':'Peer review: AI in healthcare'}
CSS_Q='''@font-face{font-family:Bricolage;src:url(../../../../bricolage.woff2);font-weight:200 800}@font-face{font-family:Mono;src:url(../../../essays/fonts/mono-normal.woff2)}
*{box-sizing:border-box;margin:0;padding:0}body{background:#555}
.s{width:1080px;height:1350px;position:relative;overflow:hidden;margin-bottom:24px;display:flex;flex-direction:column;background:#150C2E;color:#fff;padding:0 64px;font-family:Arial,Helvetica,sans-serif;background-image:linear-gradient(rgba(255,255,255,.04) 2px,transparent 2px),linear-gradient(90deg,rgba(255,255,255,.04) 2px,transparent 2px),radial-gradient(circle at 82% 0,rgba(255,214,0,.2),transparent 40%);background-size:36px 36px,36px 36px,auto}
.hud{margin-top:52px;display:flex;justify-content:space-between;font:400 21px Mono,monospace;color:#FFD600;letter-spacing:.06em;border:3px solid #FFD600;padding:12px 18px;border-radius:10px;box-shadow:6px 6px 0 #7A2CFF;flex:none}
.kick{margin-top:34px;align-self:flex-start;font:700 22px Mono,monospace;letter-spacing:.08em;background:#7A2CFF;color:#fff;padding:8px 16px;border-radius:8px;border:3px solid #000;box-shadow:4px 4px 0 #000}
h1{font:800 100px/0.97 Bricolage,Arial;letter-spacing:-.03em;margin-top:28px;text-shadow:6px 6px 0 #7A2CFF}h1 b,h2 b{color:#FFD600;font-weight:800}
h2{font:800 78px/1.0 Bricolage,Arial;letter-spacing:-.03em;margin-top:26px;text-shadow:5px 5px 0 #7A2CFF}
.sub{font:400 28px/1.35 Mono,monospace;color:#c9b8ff;margin-top:22px}.au{font:400 24px Mono,monospace;color:#c9b8ff;margin-top:26px}.id{display:none}
.p{margin-top:26px;background:#fff;color:#150C2E;border:5px solid #000;border-radius:22px;padding:28px 34px;font:400 50px/1.32 'Times New Roman',serif;box-shadow:9px 9px 0 #000}.p em{font-style:normal;background:#FFE680;padding:0 4px;border-radius:4px}
.steps{margin-top:26px;display:grid;gap:16px}.st{display:grid;grid-template-columns:78px 1fr;gap:20px;align-items:center;padding:20px 24px;background:#22134a;border:3px solid var(--c,#2EE6A6);border-radius:18px;box-shadow:6px 6px 0 #000}
.st .n{width:66px;height:66px;border-radius:12px;background:var(--c,#2EE6A6);color:#150C2E;font:800 42px/66px Bricolage;text-align:center}.st:nth-child(1){--c:#2EE6A6}.st:nth-child(2){--c:#FFD600}.st:nth-child(3){--c:#FF6B9A}.st:nth-child(4){--c:#4CC9F0}.st:nth-child(5){--c:#B79CFF}
.st b{font:700 36px Arial;display:block}.st span{font:400 26px/1.3 Mono,monospace;color:#c9b8ff;display:block;margin-top:4px}
.note{margin-top:22px;font:700 28px Mono,monospace;color:#FFD600}.src{font:400 18px Mono,monospace;color:#9d87d6;margin-top:14px}
svg{background:#fff;border:5px solid #000;border-radius:18px;padding:14px;margin-top:24px;box-shadow:7px 7px 0 #000}
table{border-collapse:separate;border-spacing:0;width:100%;font-size:17px;margin-top:16px;background:#fff;color:#150C2E;border:4px solid #000;border-radius:16px;overflow:hidden;box-shadow:7px 7px 0 #000}th{background:#7A2CFF;color:#fff;text-align:left;padding:10px;font:700 15px Mono,monospace;letter-spacing:.05em}td{padding:9px 10px;border-bottom:2px solid #e6e0f6;vertical-align:top}tr.hl td{background:#FFF0A6}
.chip{font:700 13px Mono,monospace;padding:3px 9px;border-radius:6px;white-space:nowrap;color:#150C2E}.ok{background:#2EE6A6}.bad{background:#FF6B9A}.mid{background:#FFD600}
.path{margin-top:24px;display:grid;gap:10px}.pn{display:grid;grid-template-columns:76px 1fr;gap:20px;align-items:center;padding:10px 18px;background:#22134a;border:3px solid #fff;border-radius:16px;box-shadow:5px 5px 0 #000}.pn .c{width:64px;height:64px;border-radius:12px;background:#FFD600;color:#150C2E;font:800 24px/64px Bricolage;text-align:center}.pn.on .c{background:#2EE6A6}.pn b{font:700 32px Arial;display:block}.pn span{font:400 22px Mono,monospace;color:#c9b8ff;display:block}.pn em{font:700 15px Mono,monospace;font-style:normal;color:#2EE6A6;margin-left:10px}
.grid{display:grid;grid-template-columns:repeat(4,1fr);gap:14px;margin-top:26px}.t{border:3px solid #fff;border-radius:14px;padding:12px 12px 52px;background:#22134a;box-shadow:5px 5px 0 #000;min-height:210px;position:relative}.t b{font:800 44px Bricolage;color:#FFD600;display:block}.t span{font:400 17px/1.25 Mono,monospace;display:block;color:#e7defe;margin-top:4px}.t em{position:absolute;left:10px;right:10px;bottom:12px;font:700 15px Mono,monospace;font-style:normal;text-align:center;padding:5px;border-radius:6px;color:#150C2E}
.t.ok{border-color:#2EE6A6}.t.ok em{background:#2EE6A6}.t.bad{border-color:#FF6B9A}.t.bad em{background:#FF6B9A}.t.mid{border-color:#FFD600}.t.mid em{background:#FFD600}
.pills{margin-top:auto;margin-bottom:96px;display:flex;gap:14px}.pills span{font:700 22px Mono,monospace;border:3px solid #fff;border-radius:10px;padding:10px 20px;box-shadow:4px 4px 0 #000}.pills .f{background:#FFD600;color:#150C2E;border-color:#000}
.ft{position:absolute;left:64px;right:64px;bottom:34px;display:flex;justify-content:space-between;font:400 18px Mono,monospace;color:#9d87d6}'''
CSS_J='''*{box-sizing:border-box;margin:0;padding:0}body{background:#999}
.s{width:1080px;height:1350px;position:relative;overflow:hidden;margin-bottom:24px;display:flex;flex-direction:column;background:#fff;color:#111;padding:0 96px;font-family:'Times New Roman',Times,serif}
.hd{margin-top:56px;display:flex;justify-content:space-between;font:700 19px Arial;letter-spacing:.12em;color:#20558A;padding-bottom:12px;border-bottom:1px solid #20558A;flex:none;position:relative}.hd:after{content:'';position:absolute;left:0;right:0;bottom:-6px;border-bottom:3px solid #20558A}.hd i{font-style:normal;font-weight:400;color:#555}
.kick{margin-top:64px;font:700 23px Arial;letter-spacing:.14em;color:#B3261E}
h1{font:700 86px/1.04 'Times New Roman',serif;letter-spacing:-.01em;margin-top:22px}h1 b,h2 b{color:#20558A;font-weight:700}
h2{font:700 70px/1.06 'Times New Roman',serif;margin-top:22px;letter-spacing:-.01em}
.sub{font:italic 400 42px/1.3 'Times New Roman',serif;margin-top:28px;color:#333}.au{font:400 26px Arial;margin-top:32px;color:#333}.id{display:inline-block;width:22px;height:22px;border-radius:50%;background:#A6CE39;color:#fff;font:700 11px/22px Arial;text-align:center;margin-left:6px}
.p{margin-top:34px;font:400 58px/1.38 'Times New Roman',serif}.p em{font-style:normal;background:#FFF1A8;padding:0 3px}
.steps{margin-top:30px;border-top:2px solid #111}.st{display:grid;grid-template-columns:80px 1fr;gap:20px;padding:26px 0;border-bottom:1px solid #999;align-items:baseline}.st .n{font:700 52px 'Times New Roman',serif;color:#20558A}.st b{font:700 36px Arial;display:block}.st span{font:400 36px/1.3 'Times New Roman',serif;display:block;margin-top:6px;color:#222}
.note{margin-top:30px;font:700 28px Arial;color:#B3261E}.src{font:400 19px Arial;color:#666;margin-top:16px}
svg{margin-top:26px}
table{border-collapse:collapse;width:100%;font:400 18px Arial;margin-top:18px;border-top:3px solid #111;border-bottom:3px solid #111}th{text-align:left;padding:10px 8px;font:700 15px Arial;letter-spacing:.08em;border-bottom:1.5px solid #111}td{padding:10px 8px;border-bottom:1px solid #ccc;vertical-align:top}tr.hl td{background:#FFF7CC}
.chip{font:700 14px Arial;letter-spacing:.04em;white-space:nowrap}.ok{color:#20558A}.bad{color:#B3261E}.mid{color:#8a6100}
.path{margin-top:22px;border-top:2px solid #111}.pn{display:grid;grid-template-columns:90px 1fr;gap:18px;align-items:baseline;padding:14px 0;border-bottom:1px solid #999}.pn .c{font:700 28px Arial;color:#20558A}.pn.on .c{color:#B3261E}.pn b{font:700 34px Arial;display:block}.pn span{font:400 31px 'Times New Roman',serif;display:block;color:#222}.pn em{font:700 15px Arial;font-style:normal;color:#B3261E;margin-left:12px;letter-spacing:.06em}
.big{display:flex;align-items:flex-end;gap:26px;margin-top:30px}.big .n{font:700 230px/0.8 'Times New Roman',serif;color:#20558A}.big .t{font:400 54px/1.08 'Times New Roman',serif;padding-bottom:12px}.big .t b{font-weight:700;color:#20558A}
.hookline{font:italic 400 44px/1.3 'Times New Roman',serif;margin-top:22px;color:#222}
.pills{margin-top:auto;margin-bottom:96px;display:flex;gap:14px}.pills span{font:700 22px Arial;border:1.5px solid #20558A;color:#20558A;padding:10px 24px}.pills .f{background:#20558A;color:#fff}
.ft{position:absolute;left:96px;right:96px;bottom:36px;display:flex;justify-content:space-between;font:400 18px Arial;color:#666;border-top:1px solid #999;padding-top:12px}'''
def hd_q(art,i,n): return f'<div class="hud"><span>PLAYER 1 · DR. SIDHARTH</span><span>{art["id"]} · {i}/{n}</span></div>'
def hd_j(art,i,n): return f'<div class="hd"><span>{SER.upper()}</span><i>PART {art["id"][-1]} · {i}/{n}</i></div>'
def ft(i,n): return f'<div class="ft"><span>Dr. Sidharth Narayanan · House Surgeon, GMC Kozhikode</span><span>{i:02d} / {n:02d}</span></div>'
def hook_quest():
    lab={'ok':'CLEARED','bad':'NO PAPER','mid':'LOADING...'}
    tiles=''.join(f'<div class="t {r[4]}"><b>{r[0]}</b><span>{e(SHORT[r[0]])}</span><em>{lab[r[4]]}</em></div>' for r in ROWS)
    return f'<h1>8 research <b>quests.</b></h1><div class="sub">4 cleared. 2 never made it to a paper. 2 still loading. Most people play for the portfolio. I played for the story.</div><div class="grid">{tiles}</div>'
def hook_journal():
    t=soft.table('1').replace('<table>','<table>')
    return f'<div class="kick">UNDERGRADUATE RESEARCH · A DATA STORY</div><div class="big"><div class="n">8</div><div class="t">research projects<br><b>so far.</b></div></div><div class="hookline">Most people get into research for a portfolio. I got into it purely because I loved reading, building on it and building a narrative.</div><div style="margin-top:26px;font:700 15px Arial;letter-spacing:.1em;color:#20558A">TABLE 1 · THE RESEARCH LEDGER</div>'+t
def build(art,theme,name):
    sl=list(art['slides']);n=len(sl);out=''
    for i,(kick,inner) in enumerate(sl,1):
        if inner is None:
            inner=f'<h1>{art["title_html"]}</h1><div class="sub">{e(art["sub"])}</div><div class="au">Sidharth Narayanan, MBBS <span class="id">iD</span></div><div class="pills"><span class="f">Cite</span><span>Save</span><span>Share</span><span>Swipe →</span></div>'
        if kick=='HOOK':
            inner=hook_quest() if theme=='q' else hook_journal(); kk=''
        else:
            kk=f'<div class="kick">{kick}</div>' if not (theme=='j' and False) else ''
        if theme=='q' and kick=='HOOK': kk=''
        if theme=='j' and kick=='HOOK': kk=''
        h=hd_q(art,i,n) if theme=='q' else hd_j(art,i,n)
        out+=f'<section class="s" id="s{i}">{h}{kk}{inner}{ft(i,n)}</section>'
    css=CSS_Q if theme=='q' else CSS_J
    open(f'{name}.html','w').write(f'<!doctype html><meta charset="utf-8"><style>{css}</style>{out}')
for a,nm in ((R01,'r01'),(R02,'r02')):
    # fix journal hook for R01 only; R02 has no HOOK slide
    build(a,'q',f'{nm}-quest'); build(a,'j',f'{nm}-journal')
print('themes ok')
