# Rebuilds the Article 001 posts zip into editorial/dist/ (not committed). Run: python3 editorial/bilmc/001/package_posts.py
import zipfile, os, json
R=os.path.abspath(os.path.join(os.path.dirname(__file__),'..','..','..'))+'/'; E=R+'editorial/bilmc/001/export/'
os.makedirs(R+'editorial/dist',exist_ok=True)
names=['cover','premise-MBBS-foundation','the-question','timetable','stepping-stone-NEETPG','pathway-observation-to-validation','overlap-clinical-plus-engineering','bridge-technology-to-medicine','not-another-compulsory-subject','the-environment','capabilities-beyond-clinic','two-things-together','closing-and-link']
takes=json.load(open(R+'editorial/bilmc/001/takes.json'))['takes']
z=zipfile.ZipFile(R+'editorial/dist/Article001_Posts_Medinn.zip','w',zipfile.ZIP_DEFLATED)
z.writestr('README_WHICH-IS-WHICH.txt','''ARTICLE 001 - Before I Leave Medical College
1_INSTAGRAM_carousel_13-slides: post all 13 as one carousel, in order
2_LINKEDIN_carousel_PDF: upload as a LinkedIn document
3_LINKEDIN_hook-image_alternative: image + link post, or a teaser
4_INSTAGRAM_daily-posters_1-per-day: one poster a day, captions in captions.md
5_LAUNCH_posters_and_photos: launch poster (plain), launch poster with the MedX photo, and the MedX photos
6_LINK-PREVIEW_image
Article: https://medinn.in/before-i-leave-medical-college/more-than-a-training-ground
''')
for i,n in enumerate(names,1): z.write(E+f'bilmc-001-slide-{i:02d}.png',f'1_INSTAGRAM_carousel_13-slides/IG-{i:02d}-{n}.png')
z.write(E+'bilmc-001-carousel.pdf','2_LINKEDIN_carousel_PDF/LinkedIn-carousel-13-slides-UPLOAD-AS-DOCUMENT.pdf')
z.write(E+'bilmc-001-linkedin-hook-1080x1350.png','3_LINKEDIN_hook-image_alternative/LinkedIn-hook-image-1080x1350.png')
for i,t in enumerate(takes,1): z.write(E+f'posters/bilmc-001-poster-{i:02d}.png',f'4_INSTAGRAM_daily-posters_1-per-day/Day-{i:02d}-{t["id"]}.png')
z.write(E+'bilmc-001-LAUNCH-poster-1080x1350.png','5_LAUNCH_posters_and_photos/LAUNCH-poster-plain.png')
z.write(E+'bilmc-001-LAUNCH-poster-with-MedX-photo-1080x1350.png','5_LAUNCH_posters_and_photos/LAUNCH-poster-with-MedX-photo.png')
for f in sorted(os.listdir(E+'launch-photos')): z.write(E+'launch-photos/'+f,'5_LAUNCH_posters_and_photos/'+f)
z.write(R+'bilmc-001-og.jpg','6_LINK-PREVIEW_image/article-link-preview-1200x630.jpg')
z.close(); print('wrote editorial/dist/Article001_Posts_Medinn.zip')
