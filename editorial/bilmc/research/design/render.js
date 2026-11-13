const {chromium}=require('playwright');const path=require('path'),fs=require('fs');
(async()=>{const b=await chromium.launch();fs.mkdirSync('export',{recursive:true});
for(const v of ['A','B','C']){const p=await b.newPage({viewport:{width:1080,height:1350}});await p.goto('file://'+path.join(__dirname,`variant-${v}.html`));await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(300);
const s=await p.$$('section.s');for(let i=0;i<s.length;i++) await s[i].screenshot({path:`export/variant-${v}-${i+1}.png`});}
await b.close();console.log('done')})();
