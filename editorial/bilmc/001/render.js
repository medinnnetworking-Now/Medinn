// cd editorial/bilmc/001 && python3 build_slides.py && python3 build_posters.py && NODE_PATH=$(npm root -g) node render.js
const { chromium } = require('playwright'); const path=require('path'), fs=require('fs');
(async()=>{const b=await chromium.launch();const out=path.join(__dirname,'export');fs.mkdirSync(path.join(out,'posters'),{recursive:true});
 const pad=n=>String(n).padStart(2,'0');
 let p=await b.newPage({viewport:{width:1080,height:1350}});
 await p.goto('file://'+path.join(__dirname,'slides.html'));await p.evaluate(()=>document.fonts.ready);
 for(let i=1;i<=12;i++) await (await p.$('#s'+pad(i))).screenshot({path:path.join(out,`bilmc-001-slide-${pad(i)}.png`)});
 await p.pdf({path:path.join(out,'bilmc-001-carousel.pdf'),width:'1080px',height:'1350px',printBackground:true});
 p=await b.newPage({viewport:{width:1080,height:1350}});
 await p.goto('file://'+path.join(__dirname,'posters.html'));await p.evaluate(()=>document.fonts.ready);
 const n=await p.$$eval('section',s=>s.length);
 for(let i=1;i<=n;i++) await (await p.$('#p'+pad(i))).screenshot({path:path.join(out,'posters',`bilmc-001-poster-${pad(i)}.png`)});
 const t=await b.newPage({viewport:{width:1200,height:630}});await t.goto('file://'+path.join(__dirname,'thumbnail.html'));await t.evaluate(()=>document.fonts.ready);
 await t.screenshot({path:path.join(out,'bilmc-001-thumbnail-1200x630.png')});
 // figure plates used inside the article page
 p=await b.newPage({viewport:{width:1080,height:1350},deviceScaleFactor:2});await p.goto('file://'+path.join(__dirname,'slides.html'));await p.evaluate(()=>document.fonts.ready);
 const fd=path.join(__dirname,'..','..','..','essays','img');fs.mkdirSync(fd,{recursive:true});
 for(const [id,name] of [['s03','fig-1-timetable'],['s04','fig-2-stepping-stone'],['s05','fig-3-pathway'],['s06','fig-4-overlap'],['s07','fig-5-bridge'],['s09','fig-6-ecosystem'],['s10','fig-7-capabilities']]){
  const el=await p.$(`#${id} .art svg`)||await p.$(`#${id} .art`);await el.screenshot({path:path.join(fd,name+'.png')});}
 await b.close();})();
