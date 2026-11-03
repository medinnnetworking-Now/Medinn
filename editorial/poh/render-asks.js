const { chromium } = require('playwright'); const path=require('path');
(async()=>{const b=await chromium.launch({args:['--allow-file-access-from-files']});const p=await b.newPage({viewport:{width:1080,height:1350}});
await p.goto('file://'+path.join(__dirname,'asks-cards.html'));await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(300);
for(const n of ['02','01','03','04']){await p.locator('#a'+n).screenshot({path:path.join(__dirname,'export','poh-ask-'+n+'.png')});}
const o=await p.evaluate(()=>[...document.querySelectorAll('.s')].map(s=>s.scrollHeight>s.clientHeight));console.log('overflow',o);
await b.close()})()
