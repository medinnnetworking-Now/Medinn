const {chromium}=require('playwright');const path=require('path'),fs=require('fs');
(async()=>{const b=await chromium.launch();fs.mkdirSync('export',{recursive:true});
for(const v of ['r01-quest','r02-quest','r01-journal','r02-journal']){const p=await b.newPage({viewport:{width:1080,height:1350}});await p.goto('file://'+path.join(__dirname,`${v}.html`));await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(300);
const bad=await p.evaluate(()=>[...document.querySelectorAll('section.s')].map((s,i)=>{const f=s.querySelector('.ft').getBoundingClientRect().top;let m=0;[...s.children].forEach(c=>{if(!c.classList.contains('ft')&&!c.classList.contains('pills'))m=Math.max(m,c.getBoundingClientRect().bottom)});return m>f-8?i+1:0}).filter(Boolean));console.log(v,'overflow:',bad);
const s=await p.$$('section.s');for(let i=0;i<s.length;i++) await s[i].screenshot({path:`export/${v}-${String(i+1).padStart(2,'0')}.png`});
await p.pdf({path:`export/${v}.pdf`,width:'1080px',height:'1350px',printBackground:true});}
await b.close()})();
