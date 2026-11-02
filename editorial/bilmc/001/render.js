// cd editorial/bilmc/001 && python3 build_slides.py && python3 build_posters.py && NODE_PATH=$(npm root -g) node render.js
const { chromium } = require('playwright'); const path=require('path'), fs=require('fs');
(async()=>{const b=await chromium.launch();const out=path.join(__dirname,'export');for(const f of fs.existsSync(out)?fs.readdirSync(out):[]) if(/^bilmc-001-slide-\d+\.png$/.test(f)) fs.unlinkSync(path.join(out,f));fs.mkdirSync(path.join(out,'posters'),{recursive:true});
 const pad=n=>String(n).padStart(2,'0');
 let p=await b.newPage({viewport:{width:1080,height:1350}});
 await p.goto('file://'+path.join(__dirname,'slides.html'));await p.evaluate(()=>document.fonts.ready);
  const secs=await p.$$('section.slide');for(let i=0;i<secs.length;i++) await secs[i].screenshot({path:path.join(out,`bilmc-001-slide-${pad(i+1)}.png`)});
 console.log(secs.length,'slides exported');
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
 const hk=await b.newPage({viewport:{width:1080,height:1350}});await hk.goto('file://'+path.join(__dirname,'hook.html'));await hk.evaluate(()=>document.fonts.ready);
 await (await hk.$('#hook')).screenshot({path:path.join(out,'bilmc-001-linkedin-hook-1080x1350.png')});
 const lp=await b.newPage({viewport:{width:1080,height:1350}});await lp.goto('file://'+path.join(__dirname,'launch-poster.html'));await lp.evaluate(()=>document.fonts.ready);
 await (await lp.$('#poster')).screenshot({path:path.join(out,'bilmc-001-LAUNCH-poster-1080x1350.png')});
 const lq=await b.newPage({viewport:{width:1080,height:1350}});await lq.goto('file://'+path.join(__dirname,'launch-poster-photo.html'));await lq.evaluate(()=>document.fonts.ready);
 await (await lq.$('#poster')).screenshot({path:path.join(out,'bilmc-001-LAUNCH-poster-with-MedX-photo-1080x1350.png')});
 await b.close();})();
