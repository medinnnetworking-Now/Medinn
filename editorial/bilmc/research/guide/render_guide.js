const {chromium}=require('playwright');const path=require('path'),fs=require('fs');
(async()=>{const b=await chromium.launch();fs.mkdirSync('export',{recursive:true});const p=await b.newPage({viewport:{width:900,height:1200}});
await p.goto('file://'+path.join(__dirname,'guide.html'));await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(400);
const bad=await p.evaluate(()=>[...document.querySelectorAll('section.pg')].map((s,i)=>{const f=s.querySelector('.ft').getBoundingClientRect().top;let m=0;[...s.children].forEach(c=>{if(!c.classList.contains('ft')&&!c.classList.contains('top')&&c.tagName!=='STYLE'){const r=c.getBoundingClientRect();m=Math.max(m,r.bottom)}});return m>f-6?`p${i+1}(+${Math.round(m-f)})`:0}).filter(Boolean));console.log('overflow:',bad);
const s=await p.$$('section.pg');for(let i=0;i<s.length;i++) await s[i].screenshot({path:`export/guide-${String(i+1).padStart(2,'0')}.png`});
await p.pdf({path:'export/CMC-Analytica-Guide-Cross-Sectional-and-Case-Reports.pdf',width:'794px',height:'1123px',printBackground:true});await b.close();})();
