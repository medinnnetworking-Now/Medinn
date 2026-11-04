const { chromium } = require('playwright'); const path=require('path');
(async()=>{const b=await chromium.launch({args:['--allow-file-access-from-files']});let p=await b.newPage({viewport:{width:1080,height:1350}});
await p.goto('file://'+path.join(__dirname,'ig-carousel.html'));await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(400);
for(let i=1;i<=7;i++){const ov=await p.evaluate(i=>{const s=document.getElementById('s'+i);return s.scrollHeight>s.clientHeight},i);console.log('s'+i,'overflow',ov);await p.locator('#s'+i).screenshot({path:path.join(__dirname,'export','poh-ig-0'+i+'.png')});}
p=await b.newPage({viewport:{width:1080,height:1080}});await p.goto('file://'+path.join(__dirname,'ig-logo.html'));await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(300);
await p.locator('#l').screenshot({path:path.join(__dirname,'export','poh-ig-profile-logo-1080.png')});await b.close()})()
