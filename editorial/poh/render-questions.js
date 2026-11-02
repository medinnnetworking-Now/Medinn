const { chromium } = require('playwright'); const path=require('path');
(async()=>{const b=await chromium.launch({args:['--allow-file-access-from-files']});const p=await b.newPage({viewport:{width:1080,height:1350}});
await p.goto('file://'+path.join(__dirname,'question-cards.html'));await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(300);
for(let i=1;i<=7;i++){await p.locator('#q'+i).screenshot({path:path.join(__dirname,'export','poh-q'+i+'.png')});}
await b.close()})()
