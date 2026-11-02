// cd editorial/poh && python3 build_docs.py && NODE_PATH=$(npm root -g) node render-docs.js
const { chromium } = require('playwright'); const path=require('path');
(async()=>{const b=await chromium.launch({args:['--allow-file-access-from-files']});const p=await b.newPage();
for(const [f,o] of [['brief.html','PoH-Brief-for-MVPs.pdf'],['guide.html','PoH-Interview-Guide-and-Leverage-Playbook.pdf']]){
 await p.goto('file://'+path.join(__dirname,f));await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(400);
 await p.pdf({path:path.join(__dirname,'export',o),format:'A4',printBackground:true,preferCSSPageSize:true});}
await b.close()})()
