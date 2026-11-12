const { chromium } = require('playwright'); const path=require('path');
(async()=>{const b=await chromium.launch({args:['--allow-file-access-from-files']});let p=await b.newPage({viewport:{width:1080,height:1350}});
await p.goto('file://'+path.join(__dirname,'feature-hanan-poster.html'));await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(300);
console.log('poster overflow',await p.evaluate(()=>{const s=document.querySelector('.s');return s.scrollHeight>s.clientHeight}));
await p.screenshot({path:path.join(__dirname,'export','PoH-feature-Hanan-Kasim-DRAFT.png')});
p=await b.newPage({viewport:{width:1200,height:630}});await p.goto('file://'+path.join(__dirname,'hanan-og.html'));await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(300);
await p.locator('#o').screenshot({path:path.join(__dirname,'export','hanan-og.png')});await b.close()})()
