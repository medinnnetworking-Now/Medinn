const { chromium } = require('playwright'); const path=require('path'),fs=require('fs');
(async()=>{const b=await chromium.launch();const out=path.join(__dirname,'export');fs.mkdirSync(out,{recursive:true});
 const p=await b.newPage({viewport:{width:1080,height:1350}});await p.goto('file://'+path.join(__dirname,'slides.html'));await p.evaluate(()=>document.fonts.ready);
 const s=await p.$$('section.slide');for(let i=0;i<s.length;i++) await s[i].screenshot({path:path.join(out,`maanas-slide-${String(i+1).padStart(2,'0')}.png`)});
 await p.pdf({path:path.join(out,'maanas-carousel.pdf'),width:'1080px',height:'1350px',printBackground:true});await b.close();console.log(s.length,'exported');})();
