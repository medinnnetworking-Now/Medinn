const { chromium } = require('playwright'); const path=require('path');
(async()=>{const b=await chromium.launch({args:['--allow-file-access-from-files']});const p=await b.newPage({viewport:{width:1080,height:1350}});
await p.goto('file://'+path.join(__dirname,'asks-campaign-poster.html'));await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(300);
console.log('overflow',await p.evaluate(()=>{const s=document.querySelector('.s');return s.scrollHeight>s.clientHeight}));
await p.screenshot({path:path.join(__dirname,'export','poh-asks-campaign-poster.png')});await b.close()})()
