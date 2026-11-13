const { chromium } = require('playwright'); const path=require('path');
(async()=>{const b=await chromium.launch({args:['--allow-file-access-from-files']});const p=await b.newPage({viewport:{width:1080,height:1350}});
await p.goto('file://'+path.join(__dirname,'hero-hanan.html'));await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(400);
console.log('overflow',await p.evaluate(()=>{const t=document.querySelector('.tx');return t.scrollHeight>t.clientHeight}));
await p.screenshot({path:path.join(__dirname,'export','poh-hero-Hanan-Kasim.png')});await b.close()})()
