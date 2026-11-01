// cd editorial/poh && python3 build_poh.py && NODE_PATH=$(npm root -g) node render.js
const { chromium } = require('playwright'); const path=require('path'), fs=require('fs');
(async()=>{const b=await chromium.launch({args:['--allow-file-access-from-files']});const out=path.join(__dirname,'export');fs.mkdirSync(out,{recursive:true});
 const pad=n=>String(n).padStart(2,'0');
 const p=await b.newPage({viewport:{width:1080,height:1350}});await p.goto('file://'+path.join(__dirname,'slides.html'));await p.evaluate(()=>document.fonts.ready);
 for(let i=1;i<=7;i++) await (await p.$('#s'+pad(i))).screenshot({path:path.join(out,`poh-launch-slide-${pad(i)}.png`)});
 await p.pdf({path:path.join(out,'poh-launch-carousel.pdf'),width:'1080px',height:'1350px',printBackground:true});
 // logo files: lockups on dark and light, avatar
 const l=await b.newPage({viewport:{width:1600,height:520}});
 for(const [name,bg,fg] of [['dark','#05070D','#EDF1FA'],['light','#FFFFFF','#102B50']]){
  fs.writeFileSync(path.join(__dirname,'lockup.html'),`<!doctype html><meta charset="utf-8"><style>@font-face{font-family:B;src:url(../../bricolage.woff2);font-weight:200 800}body{margin:0;width:1600px;height:520px;background:${bg};display:flex;align-items:center;gap:56px;padding:0 90px;box-sizing:border-box}img{width:340px;height:340px;border-radius:50%}div{font:700 150px/.95 B;letter-spacing:-.05em;color:${fg}}small{display:block;font:500 40px/1.2 B;letter-spacing:-.01em;color:#6E95FF;margin-top:20px}</style><img src="../../poh-mark.png"><div>People of<br>Healthcare<small>A Medinn initiative</small></div>`);
  await l.goto('file://'+path.join(__dirname,'lockup.html'));await l.evaluate(()=>document.fonts.ready);await l.waitForTimeout(300);await l.screenshot({path:path.join(out,`poh-logo-lockup-${name}.png`)});}
 await b.close();})();
