# Three explanatory illustrations as SVG strings. ink/acc/bg are swapped for the page (white) and the carousel (dark).
def hatch(i,ink): return f'<defs><pattern id="h{i}" width="12" height="12" patternUnits="userSpaceOnUse" patternTransform="rotate(45)"><line x1="0" y1="0" x2="0" y2="12" stroke="{ink}" stroke-width="2.2"/></pattern></defs>'
def cost(ink,acc,bg,uid='c'):
    # linear scale: 3,00,000 = 840px
    k=840/300000
    w=lambda v:max(4,round(v*k))
    return f'''<svg viewBox="0 0 904 380" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Bars drawn to scale: a laryngoscope at 1,000 to 2,000 rupees, UVEAL under 10,000 rupees, a video-laryngoscope at 2 to 3 lakh rupees">{hatch(uid,ink)}
<g font-family="Inter,Helvetica,Arial,sans-serif" fill="{ink}">
<text x="0" y="28" font-size="20" font-weight="700" letter-spacing="1.5" font-family="JetBrains Mono,monospace">DRAWN TO SCALE (₹)</text>
<text x="0" y="86" font-size="26" font-weight="600">Standard laryngoscope</text>
<rect x="0" y="100" width="{w(1000)}" height="34" fill="{ink}"/><rect x="{w(1000)}" y="100" width="{w(1000)-w(0)}" height="34" fill="url(#h{uid})"/>
<text x="{w(2000)+14}" y="126" font-size="24" font-weight="700" font-family="JetBrains Mono,monospace">₹1,000 to 2,000</text>
<text x="0" y="192" font-size="26" font-weight="600" fill="{acc}">UVEAL attachment (company figure)</text>
<rect x="0" y="206" width="{w(10000)}" height="34" fill="{acc}"/>
<text x="{w(10000)+14}" y="232" font-size="24" font-weight="700" font-family="JetBrains Mono,monospace" fill="{acc}">starts under ₹10,000</text>
<text x="0" y="298" font-size="26" font-weight="600">Video-laryngoscope (as shown in his video)</text>
<rect x="0" y="312" width="{w(200000)}" height="34" fill="{ink}"/><rect x="{w(200000)}" y="312" width="{w(300000)-w(200000)}" height="34" fill="url(#h{uid})" stroke="{ink}" stroke-width="2"/>
<text x="{w(200000)-210}" y="372" font-size="24" font-weight="700" font-family="JetBrains Mono,monospace">₹2,00,000 to ₹3,00,000</text></g></svg>'''
def device(ink,acc,bg,uid='d'):
    return f'''<svg viewBox="0 0 904 440" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="A laryngoscope with a UVEAL attachment on the blade, a cable running to a smartphone that shows the airway view">
<g fill="none" stroke="{ink}" stroke-width="5" stroke-linejoin="round" stroke-linecap="round">
 <rect x="230" y="190" width="70" height="210" rx="8" fill="{bg}"/>
 <g stroke-width="2.5" opacity=".6"><line x1="236" y1="230" x2="294" y2="230"/><line x1="236" y1="256" x2="294" y2="256"/><line x1="236" y1="282" x2="294" y2="282"/><line x1="236" y1="308" x2="294" y2="308"/><line x1="236" y1="334" x2="294" y2="334"/></g>
 <rect x="226" y="168" width="78" height="30" rx="5" fill="{bg}"/>
 <path d="M300 168 L 520 168 C 590 168, 626 146, 640 96 L 616 90 C 606 126, 580 140, 520 140 L 300 140 Z" fill="{bg}"/></g>
<g fill="{acc}" stroke="{acc}" stroke-width="3"><rect x="400" y="116" width="96" height="46" rx="6"/></g>
<g fill="none" stroke="{acc}" stroke-width="5" stroke-linecap="round"><path d="M496 132 C 560 120, 600 190, 720 190 L 735 200" stroke-dasharray="1 0"/></g>
<g fill="{bg}" stroke="{ink}" stroke-width="5"><rect x="640" y="200" width="190" height="210" rx="22"/></g>
<rect x="656" y="226" width="158" height="140" rx="8" fill="{acc}" opacity=".25"/>
<circle cx="735" cy="296" r="38" fill="none" stroke="{acc}" stroke-width="5"/><circle cx="735" cy="296" r="14" fill="{acc}"/>
<g font-family="JetBrains Mono,monospace" font-size="21" font-weight="700" fill="{ink}"><text x="0" y="300">EXISTING</text><text x="0" y="326">LARYNGOSCOPE</text>
<text x="330" y="236" fill="{acc}"></text><text x="380" y="70" fill="{acc}">UVEAL ATTACHMENT</text><text x="640" y="436">SMARTPHONE VIEW</text></g>
<path d="M150 296 L 222 296" stroke="{ink}" stroke-width="3" stroke-dasharray="3 9" stroke-linecap="round"/>
<path d="M448 78 L 448 112" stroke="{acc}" stroke-width="3" stroke-dasharray="3 9" stroke-linecap="round"/></svg>'''
def bridge(ink,acc,bg,uid='b'):
    return f'''<svg viewBox="0 0 904 400" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Medical device startups on one side, hospitals on the other, and a missing bridge between them held up by regulators, medical colleges and grants">{hatch(uid,ink)}
<g font-family="JetBrains Mono,monospace" font-weight="700" fill="{ink}" text-anchor="middle" font-size="21">
 <rect x="2" y="90" width="250" height="210" fill="url(#h{uid})" stroke="{ink}" stroke-width="4"/><rect x="26" y="162" width="202" height="66" fill="{bg}" stroke="{ink}" stroke-width="3"/><text x="127" y="192">MEDICAL DEVICE</text><text x="127" y="216">STARTUPS</text>
 <rect x="652" y="90" width="250" height="210" fill="{bg}" stroke="{ink}" stroke-width="4"/><rect x="676" y="162" width="202" height="66" fill="{bg}" stroke="{ink}" stroke-width="3"/><text x="777" y="204">HOSPITALS</text></g>
<line x1="252" y1="90" x2="652" y2="90" stroke="{acc}" stroke-width="7" stroke-dasharray="3 17" stroke-linecap="round"/>
<circle cx="452" cy="40" r="32" fill="{acc}"/><text x="452" y="58" text-anchor="middle" font-size="46" font-style="italic" font-family="Fraunces,Georgia,serif" fill="{bg}">?</text>
<g stroke="{ink}" stroke-width="8"><line x1="330" y1="96" x2="330" y2="300"/><line x1="452" y1="96" x2="452" y2="300"/><line x1="574" y1="96" x2="574" y2="300"/></g>
<g font-family="JetBrains Mono,monospace" font-weight="700" font-size="19" fill="{ink}" text-anchor="middle"><text x="330" y="336">REGULATORS</text><text x="452" y="336">MEDICAL</text><text x="452" y="360">COLLEGES</text><text x="574" y="336">GRANTS</text></g></svg>'''
if __name__=='__main__':
    d='/home/user/Medinn/essays/img'
    for n,f in [('poh-quintubate-cost',cost),('poh-quintubate-device',device),('poh-quintubate-bridge',bridge)]:
        open(f'{d}/{n}.svg','w').write(f('#EDF1FA','#6E95FF','#05070D',n[-4:]))
    print('ok')
