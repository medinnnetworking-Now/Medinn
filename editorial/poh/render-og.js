// Rebuilds /people-of-healthcare-og.jpg (the link-preview image). cd editorial/poh && NODE_PATH=$(npm root -g) node render-og.js
const { chromium } = require('playwright'); const path=require('path');
(async()=>{const b=await chromium.launch({args:['--allow-file-access-from-files']});const p=await b.newPage({viewport:{width:1200,height:630}});
await p.goto('file://'+path.join(__dirname,'og.html'));await p.evaluate(()=>document.fonts.ready);
await p.screenshot({path:path.join(__dirname,'export','people-of-healthcare-og.png')});await b.close()})()
