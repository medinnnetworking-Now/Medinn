const { chromium } = require('playwright'); const path=require('path');
(async()=>{const b=await chromium.launch({args:['--allow-file-access-from-files']});const p=await b.newPage({viewport:{width:1080,height:1350}});
await p.goto('file://'+path.join(__dirname,'chat-cards.html'));await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(300);
const names={c1:'01-intro',c2:'02-about-you',c3:'03-questions',c4:'04-thank-you'};
for(const id of Object.keys(names)){await p.locator('#'+id).screenshot({path:path.join(__dirname,'export','poh-chat-'+names[id]+'.png')});}
await b.close()})()
