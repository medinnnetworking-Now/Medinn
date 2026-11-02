# Rebuilds the People of Healthcare launch-kit zip into editorial/dist/ (not committed). Run: python3 editorial/poh/package_kit.py
import zipfile, os
R=os.path.abspath(os.path.join(os.path.dirname(__file__),'..','..'))+'/'; P=R+'editorial/poh/export/'
os.makedirs(R+'editorial/dist',exist_ok=True)
z=zipfile.ZipFile(R+'editorial/dist/PeopleOfHealthcare_LaunchKit_Medinn.zip','w',zipfile.ZIP_DEFLATED)
z.writestr('README_WHICH-IS-WHICH.txt','''PEOPLE OF HEALTHCARE - launch kit - WHICH FILE IS FOR WHAT
1_WHATSAPP_poster: one image to send with the WhatsApp message (QR opens the form)
2_ANNOUNCEMENT_instagram_carousel_7-slides: post all 7 as one carousel, in order
3_ANNOUNCEMENT_linkedin_carousel_PDF: upload as a LinkedIn document
4_BRIEF_to_attach_when_inviting: 2-page brief to attach to DMs and emails
5_INTERNAL_interview-guide: for your own use only
6_LOGOS: mark (blue, navy) and lockups (dark, light)
Form: https://medinn.in/people-of-healthcare#form   Page: https://medinn.in/people-of-healthcare
''')
z.write(P+'poh-whatsapp-poster-1080x1350.png','1_WHATSAPP_poster/PoH-WhatsApp-poster-1080x1350.png')
pn=['cover-connecting-with-50-MVPs','the-ecosystem','the-number-50','five-lenses','doctors-can-be-builders','how-to-nominate','closing-and-link']
for i,n in enumerate(pn,1): z.write(P+f'poh-launch-slide-{i:02d}.png',f'2_ANNOUNCEMENT_instagram_carousel_7-slides/PoH-IG-{i:02d}-{n}.png')
z.write(P+'poh-launch-carousel.pdf','3_ANNOUNCEMENT_linkedin_carousel_PDF/PoH-LinkedIn-carousel-7-slides-UPLOAD-AS-DOCUMENT.pdf')
z.write(P+'PoH-Brief-for-MVPs.pdf','4_BRIEF_to_attach_when_inviting/PoH-Brief-for-MVPs.pdf')
z.write(P+'PoH-Interview-Guide-and-Leverage-Playbook.pdf','5_INTERNAL_interview-guide/PoH-Interview-Guide-and-Leverage-Playbook.pdf')
for a,b in [('poh-logo-mark-blue-512.png','PoH-mark-blue-512.png'),('poh-logo-mark-navy-512.png','PoH-mark-navy-512.png'),('poh-logo-lockup-dark.png','PoH-lockup-dark.png'),('poh-logo-lockup-light.png','PoH-lockup-light.png')]: z.write(P+a,'6_LOGOS/'+b)
z.close(); print('wrote editorial/dist/PeopleOfHealthcare_LaunchKit_Medinn.zip')
