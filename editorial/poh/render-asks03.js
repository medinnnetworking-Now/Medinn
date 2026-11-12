const { chromium } = require('playwright'); const path=require('path');
(async()=>{const b=await chromium.launch({args:['--allow-file-access-from-files']});const p=await b.newPage({viewport:{width:1080,height:1350}});
for(const [f,o] of [['asks03-named.html','poh-asks03-named-DRAFT.png'],['asks03-anon.html','poh-asks03-anon-DRAFT.png']]){
await p.goto('file://'+path.join(__dirname,f));await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(300);
console.log(f,'overflow',await p.evaluate(()=>{const s=document.querySelector('.s');return s.scrollHeight>s.clientHeight}));
await p.screenshot({path:path.join(__dirname,'export',o)});}
await b.close()})()
