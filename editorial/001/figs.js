// exports the inked figure plates (slide .art regions) for use inside the article page
const { chromium } = require('playwright'); const path=require('path'); const fs=require('fs');
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:1350},deviceScaleFactor:2});
await p.goto('file://'+path.join(__dirname,'slides.html'));await p.evaluate(()=>document.fonts.ready);
const out=path.join(__dirname,'..','..','essays','img');fs.mkdirSync(out,{recursive:true});
for(const [id,name] of [['s03','fig-1-timetable'],['s05','fig-3-pathway'],['s07','fig-5-bridge'],['s09','fig-6-ecosystem']]){
  const svg=await p.$('#'+id+' .art svg'); await svg.screenshot({path:path.join(out,name+'.png')});}
await b.close()})();
