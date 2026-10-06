/* Medinn site content.
   Edit this file to change text, timeline entries, work, services and the gallery.
   Upload new photos or videos to the repository root first, then reference them by file name.
   Keep the quotes, commas and brackets exactly as they are around your edits. */

/* GALLERY: add a line for each photo or video. Newest first reads best.
   Photo:  { "type": "image", "src": "my-photo.jpg", "caption": "What it shows" },
   Video:  { "type": "video", "src": "my-clip.mp4", "poster": "my-clip-cover.jpg", "caption": "What it shows" },
   Link:   { "type": "link", "src": "cover.jpg", "url": "https://www.instagram.com/reel/...", "caption": "Watch the reel" },
*/
const GALLERY = [
 {
  "type": "image",
  "src": "p-handover1.jpg",
  "caption": "The Handover, 2026"
 },
 {
  "type": "image",
  "src": "oncoscope-stage.jpg",
  "caption": "Speaking at Oncoscope, Calicut Medical College"
 },
 {
  "type": "image",
  "src": "p-hackgroup.jpg",
  "caption": "Medical & Surgical Intervention Hackathon, TinkerSpace Calicut"
 },
 {
  "type": "image",
  "src": "claude-hackathon.jpg",
  "caption": "Claude Hackathon, second prize with team Cosense"
 },
 {
  "type": "image",
  "src": "p-summit.jpg",
  "caption": "IEDC Summit, NIT Calicut"
 },
 {
  "type": "image",
  "src": "p-hospex.jpg",
  "caption": "Hospex Healthcare Expo 2025, Kochi"
 },
 {
  "type": "image",
  "src": "healthtech-panel.jpg",
  "caption": "HealthTech panel, IEDC Summit"
 },
 {
  "type": "image",
  "src": "p-hackposter.jpg",
  "caption": "Hackathon poster, September 2026"
 },
 {
  "type": "image",
  "src": "p-icaim.jpg",
  "caption": "Doctors AI and ICAIM"
 },
 {
  "type": "image",
  "src": "p-nutrition2.jpg",
  "caption": "Nutrition Primers with Good Food Guru"
 },
 {
  "type": "image",
  "src": "p-dia.jpg",
  "caption": "DIA-KMTC MedTech Conference"
 },
 {
  "type": "image",
  "src": "p-evolve.jpg",
  "caption": "Evolve, with MEDPG"
 }
];

/* SERVICES: the seven services in the Explore services overlay and the Services section. */
const SERVICES = [
 { id: 'brand', icon: 'palette', title: 'Brand & positioning', tag: 'Identity and voice for doctor-led ventures.',
   text: 'Brand identity, positioning and communication strategy for doctor-led ventures, clinics and diagnostics, including founder and physician positioning.',
   get: ['Brand identity and positioning', 'Communication strategy and campaign voice', 'Founder and physician positioning', 'Launch collateral, posters and social content'],
   for: 'Clinics, diagnostics chains and doctor-led startups',
   proof: ['RM Healthcare', 'Reezet Health', 'Project HealthSpan', 'Med/Acc', 'Cytokine Lectures brand identity'] },
 { id: 'ops', icon: 'briefcase', title: 'Consulting & operations', tag: 'Run the business side of a healthcare or edtech venture.',
   text: 'Operations, marketing and distribution set up the way they were run at Cytokine Lectures: team roles, campaign calendars, community management and revenue tracking, built for small teams without a heavy tech stack.',
   get: ['Operating model and team roles', 'Marketing and distribution playbooks', 'Community and forum operations', 'Campaign and revenue tracking'],
   for: 'Early-stage edtech and healthcare companies',
   proof: ['Cytokine Lectures, COO for 3+ years', 'Med/Acc, Marketing & Outreach Head', 'MEDPG Calicut, Outreach Lead'] },
 { id: 'edtech', icon: 'cap', title: 'Edtech growth systems', tag: 'Reach medical students at scale.',
   text: 'College-to-college outreach, student ambassador networks and WhatsApp-led distribution for medical education and healthcare products, built to work without a heavy tech stack.',
   get: ['College-to-college outreach', 'Student ambassador networks', 'WhatsApp-led distribution', 'Webinar and programme launches'],
   for: 'Medical education companies and products sold to students and young doctors',
   proof: ['Cytokine Lectures', 'MEDPG Calicut (current)', 'KNYA Medical Apparel', 'Doc Tutorials', "Doctor Bhatia's"] },
 { id: 'clinical', icon: 'seal', title: 'Clinical validation', tag: 'Clinician input before a product meets patients or buyers.',
   text: 'Clinical review, product evaluation and structured problem statements for early-stage healthcare ventures, so that what gets built matches how care is actually delivered.',
   get: ['Clinical review of product and workflow', 'Product evaluation with clinician feedback', 'Structured clinical problem statements', 'Market strategy input'],
   for: 'Healthtech and MedTech founders, accelerators and product teams',
   proof: ['Med/Acc clinical validation and product evaluation', 'Surgical hackathon, Cochin', 'Cosense, Claude hackathon second prize'] },
 { id: 'pilot', icon: 'flask', title: 'Pilot projects for startups', tag: 'Take a product into a real setting.',
   text: 'Pilot planning and on-the-ground coordination with medical colleges, student communities and clinicians across Malabar: the right site, the right participants and a closed feedback loop.',
   get: ['Pilot scope and success measures', 'Site and partner introductions', 'Participant and clinician outreach', 'Feedback collection and a findings summary'],
   for: 'MedTech and healthtech startups preparing for a first deployment',
   proof: ['Hospex 2025 startup outreach', 'CureKart co-presentation', 'Med/Acc startup network', 'IEDC GMC Kozhikode'] },
 { id: 'eco', icon: 'buildings', title: 'MedTech ecosystems for institutes', tag: 'Innovation cells, partnerships and programmes.',
   text: 'Interdisciplinary hackathons, medical-college innovation cells and medicine × engineering partnerships that connect clinicians with engineers, makers, startups and state innovation bodies, to grow Malabar\'s biomedical startup ecosystem.',
   get: ['Innovation and entrepreneurship cell setup', 'Medicine × engineering partnerships', 'Hackathons and device deconstruction labs', 'Links to state innovation bodies'],
   for: 'Medical colleges, engineering institutes and hospitals',
   proof: ['IEDC GMC Kozhikode', 'NIT Calicut × Calicut Medical College', 'TinkerHub & TinkerSpace', 'Repair Café × device lab', 'Kerala Startup Mission'] },
 { id: 'events', icon: 'calendar', title: 'Events, summits & hackathons', tag: 'Concept to on-the-day operations.',
   text: 'End-to-end delivery of conferences, bootcamps, webinars and hackathons: concept, speakers, marketing, design, outreach and on-the-day operations.',
   get: ['Concept, programme and speakers', 'Marketing, design and outreach', 'On-the-day operations', 'Bootcamps, webinars and hackathons'],
   for: 'Edtech companies, colleges and professional communities',
   proof: ['The Handover Bootcamp', 'Oncoscope', 'AI in Healthcare Conclave (Hospex)', 'Medical & Surgical Intervention Hackathon', 'Medicine Magnum', 'Corporate MD'] },
];

/* D: the universe, timeline (events), selected work (works) and logo wall (orgs). */
const D = {
 "nodes": [
  {
   "id": "cytokine",
   "name": "Cytokine Lectures",
   "mono": "Cy",
   "logo": "logo-cytokine.png",
   "hasLogo": true
  },
  {
   "id": "medpg",
   "name": "MEDPG Calicut",
   "mono": "MP",
   "logo": "logo-medpg.png",
   "hasLogo": true
  },
  {
   "id": "bhatia",
   "name": "Doctor Bhatia's",
   "mono": "DB",
   "logo": "logo-dbmci.png",
   "hasLogo": true
  },
  {
   "id": "doctut",
   "name": "Doc Tutorials",
   "mono": "DT",
   "logo": "logo-doctut.png",
   "hasLogo": true
  },
  {
   "id": "maya",
   "name": "Maya Edu",
   "mono": "ME",
   "logo": "mark-maya.png",
   "hasLogo": true
  },
  {
   "id": "doctorsai",
   "name": "Doctors AI",
   "mono": "DA",
   "logo": "logo-doctorsai.png",
   "hasLogo": true
  },
  {
   "id": "hospex",
   "name": "Hospex",
   "mono": "HX",
   "logo": "mark-hospex.png",
   "hasLogo": true
  },
  {
   "id": "oncoscope",
   "name": "Oncoscope",
   "mono": "On",
   "logo": "",
   "hasLogo": false
  },
  {
   "id": "gfg",
   "name": "Good Food Guru",
   "mono": "GFG",
   "logo": "logo-gfg.png",
   "hasLogo": true
  },
  {
   "id": "ksum",
   "name": "Kerala Startup Mission",
   "mono": "KS",
   "logo": "mark-ksum.png",
   "hasLogo": true
  },
  {
   "id": "nit",
   "name": "NIT Calicut",
   "mono": "NIT",
   "logo": "logo-nitc.png",
   "hasLogo": true
  },
  {
   "id": "iedc",
   "name": "IEDC GMC Kozhikode",
   "mono": "IE",
   "logo": "logo-iedc.png",
   "hasLogo": true
  },
  {
   "id": "tinker",
   "name": "TinkerHub & TinkerSpace",
   "mono": "TS",
   "logo": "logo-tinkerspace.png",
   "hasLogo": true
  },
  {
   "id": "medacc",
   "name": "Med/Acc",
   "mono": "MA",
   "logo": "logo-medacc.png",
   "hasLogo": true
  },
  {
   "id": "reezet",
   "name": "Reezet Health",
   "mono": "Rz",
   "logo": "logo-reezet.png",
   "hasLogo": true
  },
  {
   "id": "healthspan",
   "name": "Project HealthSpan",
   "mono": "HS",
   "logo": "",
   "hasLogo": false
  },
  {
   "id": "knya",
   "name": "KNYA Medical Apparel",
   "mono": "KN",
   "logo": "logo-knya.png",
   "hasLogo": true
  },
  {
   "id": "research",
   "name": "Research & publications",
   "mono": "Res",
   "logo": "",
   "hasLogo": false
  },
  {
   "id": "certs",
   "name": "Certifications",
   "mono": "Cert",
   "logo": "",
   "hasLogo": false
  }
 ],
 "hub": {
  "name": "Dr. Sidharth Narayanan · Medinn",
  "role": "Clinician-builder · edtech and MedTech systems for Malabar · since 2024",
  "text": "19 organizations and bodies around one practice: edtech growth, events, innovation ecosystems, ventures and research. Tap any node to see the role, the years and the proof."
 },
 "detail": {
  "cytokine": {
   "name": "Cytokine Lectures",
   "tag": "Edtech",
   "role": "Edtech Growth Strategist & COO · 3+ years",
   "text": "The biggest piece of the Medinn story. A clinician-led edtech platform with 50+ college communities built over 3+ years, WhatsApp discussion forums with 3,000+ members, and faculty portfolios for surgery and medicine. Helped build close to ₹50L in lifetime revenue, including ₹12L+ from the online webinar series. Also behind The Handover bootcamp for new doctors and the Cytokine Prescription Guide for interns and GPs.",
   "links": [],
   "img": "",
   "rel": [
    "Doctors AI"
   ]
  },
  "medpg": {
   "name": "MEDPG Calicut",
   "tag": "Edtech",
   "role": "Current · Outreach Lead since July 2026",
   "text": "Current role. Community engagement and outreach for the offline NEET PG face-to-face programme, through podcasts and posters. Marketing for Evolve, a NEET PG programme by the House Surgeons Association of GMC Kozhikode with MEDPG, including a 60-day MCQ campaign.",
   "links": [],
   "img": "p-evolve.jpg",
   "rel": [
    "Doctor Bhatia's"
   ]
  },
  "bhatia": {
   "name": "Doctor Bhatia's",
   "tag": "Edtech",
   "role": "Former marketing intern · 2022",
   "text": "Content creation and campus outreach for a NEET PG edtech, on a commission-based role. ₹4-5L+ direct sales.",
   "links": [],
   "img": "",
   "rel": [
    "MEDPG Calicut",
    "Doc Tutorials"
   ]
  },
  "doctut": {
   "name": "Doc Tutorials",
   "tag": "Edtech",
   "role": "Organizer, Medicine Magnum",
   "text": "Organized Medicine Magnum, a national medicine quiz and one of the early flagship events of Doc Tutorials.",
   "links": [],
   "img": "p-magnum.jpg",
   "rel": [
    "Doctor Bhatia's"
   ]
  },
  "maya": {
   "name": "Maya Edu",
   "tag": "Edtech",
   "role": "Outreach",
   "text": "Outreach for an AI-powered clinical learning platform with a differential diagnosis engine, practice cases from partner universities and exam preparation.",
   "links": [],
   "img": "",
   "rel": [
    "Med/Acc",
    "Reezet Health"
   ]
  },
  "doctorsai": {
   "name": "Doctors AI",
   "tag": "Events",
   "role": "Undergraduate Student Lead · 2024 to present",
   "text": "A physician-led AI community. Organizing committee for the October 2024 global summit, speaker at the December 2024 AI in Healthcare Virtual Global Summit, and organizer of a hands-on AI workshop. Undergraduate student member of the Indian College of Artificial Intelligence in Medicine (ICAIM).",
   "links": [],
   "img": "p-icaim.jpg",
   "rel": [
    "Cytokine Lectures"
   ]
  },
  "hospex": {
   "name": "Hospex",
   "tag": "Events",
   "role": "Outreach to startups · 2025",
   "text": "At Hospex Healthcare Expo 2025 in Kochi: reached out to healthcare startups, organized and marketed the AI in Healthcare Conclave, and co-presented CureKart, a pharma supply chain startup.",
   "links": [],
   "img": "p-hospex.jpg",
   "rel": []
  },
  "oncoscope": {
   "name": "Oncoscope",
   "tag": "Events",
   "role": "Organizing Head 2025 · Organizing Committee 2026",
   "text": "All-India undergraduate oncology conference at Government Medical College, Calicut. The 2026 edition, on 16 May, also launched the IEDC at the college.",
   "links": [
    {
     "label": "2025 post",
     "url": "https://www.linkedin.com/posts/dr-sidharth-narayanan-7013281b8_oncoscope25-activity-7313210637067632641-EBtI"
    },
    {
     "label": "2026 post",
     "url": "https://www.linkedin.com/posts/dr-sidharth-narayanan-7013281b8_oncoscope2026-iedc-medicalinnovation-activity-7461294745915617280-MyGe"
    }
   ],
   "img": "oncoscope-stage.jpg",
   "rel": [
    "IEDC GMC Kozhikode"
   ]
  },
  "gfg": {
   "name": "Good Food Guru",
   "tag": "Events",
   "role": "Collaborator · Nutrition Primers (2026)",
   "text": "Cytokine × Good Food Guru: Nutrition Primers, a multi-masterclass series for doctors with clinical nutritionists from leading hospitals in India and the UAE. Session 1 ran online on 3 June 2026 with 50+ attendees.",
   "links": [],
   "img": "p-nutrition2.jpg",
   "rel": []
  },
  "ksum": {
   "name": "Kerala Startup Mission",
   "tag": "Ecosystem",
   "role": "Ecosystem partner",
   "text": "The IEDC at GMC Kozhikode sits within the Kerala Startup Mission network, and the IEDC Summit at NIT Calicut was organized by KSUM and NIT Calicut.",
   "links": [],
   "img": "p-summit.jpg",
   "rel": [
    "IEDC GMC Kozhikode",
    "NIT Calicut"
   ]
  },
  "nit": {
   "name": "NIT Calicut",
   "tag": "Ecosystem",
   "role": "Panelist · Delegate · IEDC partner",
   "text": "Panelist on the HealthTech track at the IEDC Summit (19 October 2024) with Dr. Moopen's iNEST, delegate at the AI in Healthcare summit, and a visit to NIT Calicut's Centre for Innovation, Entrepreneurship & Incubation to start interdisciplinary projects with Calicut Medical College.",
   "links": [
    {
     "label": "IEDC workflow",
     "url": "https://www.linkedin.com/posts/dr-sidharth-narayanan-7013281b8_biomedical-malabar-activity-7508524487974207488-be_x"
    },
    {
     "label": "AI summit",
     "url": "https://www.linkedin.com/posts/medin-networking_ai-aihc-ugcPost-7404788491001327616-rXIN"
    }
   ],
   "img": "p-nitvisit.jpg",
   "rel": [
    "Kerala Startup Mission",
    "IEDC GMC Kozhikode"
   ]
  },
  "iedc": {
   "name": "IEDC GMC Kozhikode",
   "tag": "Ecosystem",
   "role": "Student Lead · early advocate",
   "text": "Pushed for an Innovation and Entrepreneurship Development Centre at the medical college, driven by a vision of a biomedical technology corridor from Malabar. Launched on 16 May 2026 and now building a workflow with NIT Calicut, the Kerala Startup Mission, TinkerHub and TinkerSpace.",
   "links": [
    {
     "label": "Workflow post",
     "url": "https://www.linkedin.com/posts/dr-sidharth-narayanan-7013281b8_biomedical-malabar-activity-7508524487974207488-be_x"
    },
    {
     "label": "Launch post",
     "url": "https://www.linkedin.com/posts/dr-sidharth-narayanan-7013281b8_oncoscope2026-iedc-medicalinnovation-activity-7461294745915617280-MyGe"
    }
   ],
   "img": "p-repair.jpg",
   "rel": [
    "Kerala Startup Mission",
    "NIT Calicut",
    "TinkerHub & TinkerSpace",
    "Oncoscope"
   ]
  },
  "tinker": {
   "name": "TinkerHub & TinkerSpace",
   "tag": "Ecosystem",
   "role": "Hackathons and Repair Café · 2025 to present",
   "text": "Co-organized the surgical hackathon at TinkerHub Cochin (2025) and the overnight Medical & Surgical Intervention Hackathon at TinkerSpace Calicut (5-6 September 2026, 40+ participants). A Repair Café follows this month.",
   "links": [
    {
     "label": "Hackathon post",
     "url": "https://www.linkedin.com/posts/dr-sidharth-narayanan-7013281b8_malabar-tinkerspace-calicut-activity-7502369609082167296-BzCp"
    },
    {
     "label": "Repair Café post",
     "url": "https://www.linkedin.com/posts/dr-sidharth-narayanan-7013281b8_tinkerspace-activity-7510251401655103488-5Lbz"
    }
   ],
   "img": "p-hackgroup.jpg",
   "rel": [
    "IEDC GMC Kozhikode"
   ]
  },
  "medacc": {
   "name": "Med/Acc",
   "tag": "Ventures",
   "role": "Marketing & Outreach Head · earlier Consulting Intern (2025)",
   "text": "A medical accelerator working with startups. Started on clinical validation, product evaluation and market strategy, and now leads marketing and outreach.",
   "links": [],
   "img": "",
   "rel": [
    "Reezet Health",
    "Maya Edu"
   ]
  },
  "reezet": {
   "name": "Reezet Health",
   "tag": "Ventures",
   "role": "Brand Strategy & Marketing · currently shelved",
   "text": "Brand identity, positioning and communication strategy for a doctor-led metabolic wellness programme.",
   "links": [],
   "img": "",
   "rel": [
    "Med/Acc",
    "Maya Edu"
   ]
  },
  "healthspan": {
   "name": "Project HealthSpan",
   "tag": "Ventures",
   "role": "Marketing & Brand Strategy",
   "text": "Brand and positioning work for a planned advanced diagnostics and preventive healthcare chain.",
   "links": [],
   "img": "",
   "rel": []
  },
  "knya": {
   "name": "KNYA Medical Apparel",
   "tag": "Ventures",
   "role": "Distribution partner · 2025 onwards",
   "text": "Distribution partner for KNYA scrubs, selling through campus and student ambassador networks. ₹2L+ direct sales in 2025 and ₹1.5L+ passive direct sales in 2026.",
   "links": [],
   "img": "",
   "rel": []
  },
  "research": {
   "name": "Research & publications",
   "tag": "Research",
   "role": "Author and co-author · award recipient",
   "text": "Two oncology publications, the KUHS Research Appreciation Award (2024), and third prize for a paper presentation at MedMeet 3.0.",
   "links": [
    {
     "label": "ORCID",
     "url": "https://orcid.org/0009-0004-6361-5050"
    },
    {
     "label": "Case report (DOI)",
     "url": "https://doi.org/10.1055/s-0045-1808241"
    }
   ],
   "img": "p-kuhs.jpg",
   "rel": []
  },
  "certs": {
   "name": "Certifications",
   "tag": "Research",
   "role": "Credentials",
   "text": "Johns Hopkins (via Coursera) systematic review and meta-analysis, Bioentrepreneurship Basic Certification, and the 5-day residential Bio-entrepreneurship Advanced Certification at IIT Palakkad.",
   "links": [],
   "img": "",
   "rel": []
  }
 },
 "works": [
  {
   "cat": "Growth",
   "title": "Cytokine Lectures",
   "role": "Edtech Growth Strategist & COO · 3+ years",
   "text": "Scaled operations, marketing and distribution for a clinician-led edtech platform across 50+ college communities. Built the brand identity, WhatsApp discussion forums and faculty portfolios for surgery and medicine, organized the online webinar series and the Handover Bootcamp, and is expanding into a clinical segment.",
   "result": "Close to ₹50L lifetime revenue, which Medinn helped build · ₹12L+ from the online webinar series · 50+ college communities · 3,000+ forum members",
   "img": "logo-cytokine.png",
   "links": []
  },
  {
   "cat": "Growth",
   "title": "Cytokine Prescription Guide, Edition 1",
   "role": "Co-author · for interns and GPs",
   "text": "\"See the condition. Know what to write.\" A practical prescription guide for interns and general practitioners, conceived by Cytokine Lectures in association with MEDPG Calicut.",
   "result": "Edition 1",
   "img": "p-rxguide.jpg",
   "links": []
  },
  {
   "cat": "Growth",
   "title": "MEDPG Calicut · current",
   "role": "Outreach Lead · July 2026 to present",
   "text": "Community engagement and outreach for the offline NEET PG face-to-face programme, through podcasts and posters, plus the Evolve 60-day MCQ campaign with the House Surgeons Association.",
   "result": "Current role · podcasts, posters and campaigns",
   "img": "logo-medpg.png",
   "links": []
  },
  {
   "cat": "Growth",
   "title": "Doctor Bhatia's (DBMCI)",
   "role": "Former marketing intern · NEET PG edtech · 2022",
   "text": "Content creation and campus outreach campaigns, on a commission-based role.",
   "result": "₹4-5L+ direct sales",
   "img": "",
   "links": []
  },
  {
   "cat": "Growth",
   "title": "DOPA, Doctors Own Prep Academy",
   "role": "Academic content creator · NEET UG · 2020-21",
   "text": "Created educational content for NEET UG aspirants and early MBBS learners, and contributed to mentorship and question paper development. Where the edtech work began.",
   "result": "First edtech role",
   "img": "",
   "links": []
  },
  {
   "cat": "Growth",
   "title": "GTech µLearn × YIP 5.0",
   "role": "Outreach intern · June-July 2023",
   "text": "Selected for the Earn While You Learn programme to engage colleges across Kozhikode and raise participation in YIP 5.0, the Young Innovators Programme.",
   "result": "Kozhikode college outreach",
   "img": "",
   "links": []
  },
  {
   "cat": "Growth",
   "title": "Evolve, with MEDPG",
   "role": "NEET PG marketing project · House Surgeons Association × MEDPG",
   "text": "Evolve, \"the house surgeon to the resident\": a NEET PG programme engineered by the House Surgeons Association of GMC Kozhikode with MEDPG, with previous-year questions, clinical correlates, high-yield MCQs, grand tests and a community of doctors. Marketing included a 60-day NEET PG MCQ campaign.",
   "result": "60-day MCQ campaign",
   "img": "p-evolve.jpg",
   "links": []
  },
  {
   "cat": "Growth",
   "title": "KNYA Medical Apparel",
   "role": "Distribution partner · 2025 onwards",
   "text": "Distribution partner for KNYA scrubs, selling through campus and student ambassador networks across Kerala.",
   "result": "₹2L+ direct sales in 2025 · ₹1.5L+ passive direct sales in 2026",
   "img": "",
   "links": []
  },
  {
   "cat": "Events",
   "title": "AI in Healthcare Conclave, with Hospex",
   "role": "Outreach to startups · organizer & marketing · 2025",
   "text": "Reached out to healthcare startups, and organized and marketed the AI in Healthcare Conclave alongside Hospex, bringing startups and student delegates into one room.",
   "result": "Startups and student delegates",
   "img": "p-hospex.jpg",
   "links": []
  },
  {
   "cat": "Events",
   "title": "Doctors AI Global Summit 2024",
   "role": "Organizing Committee & Speaker",
   "text": "Part of the organizing team for the October 2024 summit run by a physician-led AI community, and a speaker at its AI in Healthcare Virtual Global Summit in December 2024.",
   "result": "Undergraduate Student Lead, Doctors AI, since 2024",
   "img": "",
   "links": []
  },
  {
   "cat": "Events",
   "title": "AI in Healthcare hands-on workshop",
   "role": "Organizer · Doctors AI, with Cytokine as academic partner",
   "text": "A three-hour virtual workshop for UG and PG medical students on practical AI in healthcare. Held on 26 October 2024.",
   "result": "Virtual · for UG and PG students",
   "img": "",
   "links": [
    {
     "label": "LinkedIn post",
     "url": "https://www.linkedin.com/feed/update/urn:li:activity:7281516171776917505"
    }
   ]
  },
  {
   "cat": "Events",
   "title": "Surgical Hackathon, TinkerHub Cochin",
   "role": "Co-organizer · 2025",
   "text": "A surgical hackathon in Cochin bringing clinicians, designers and engineers together around surgical problems. Managed logistics, mentorship and cross-disciplinary evaluation.",
   "result": "Cross-disciplinary teams",
   "img": "",
   "links": []
  },
  {
   "cat": "Events",
   "title": "Medical & Surgical Intervention Hackathon",
   "role": "Organizer · 5-6 September 2026, TinkerSpace Calicut with IEDC CMC",
   "text": "An overnight hackathon, \"Build for CMC\", bringing healthcare and tech communities together to build practical AI, hardware and robotics solutions for medical and surgical challenges. The first medical hackathon at the college.",
   "result": "40+ participants · Repair Café and a medical college workshop to follow",
   "img": "p-hackgroup.jpg",
   "links": [
    {
     "label": "LinkedIn post",
     "url": "https://www.linkedin.com/posts/dr-sidharth-narayanan-7013281b8_malabar-tinkerspace-calicut-activity-7502369609082167296-BzCp"
    },
    {
     "label": "Reel",
     "url": "https://www.instagram.com/reel/Dc7aeL2BnOi/"
    }
   ]
  },
  {
   "cat": "Events",
   "title": "The Handover 2026, by Cytokine",
   "role": "Conceptualized, ran, marketed and executed · 20-21 September 2026",
   "text": "From MBBS to house surgeon: a two-day offline internship bootcamp for new doctors across Kerala, with Medicine, Emergency Medicine, Surgery and Orthopaedics tracks, 50+ suture sets and The Handover Handbook. In partnership with Baby Memorial Hospital group, with MEDPG and KNYA scrubs.",
   "result": "15+ colleges · 100+ attendees",
   "img": "p-handover2.jpg",
   "links": [
    {
     "label": "LinkedIn post",
     "url": "https://www.linkedin.com/posts/cytokinelectures_handover-medical-suturing-ugcPost-7510316634084122625-zreR"
    },
    {
     "label": "Review reel",
     "url": "https://www.instagram.com/reel/DdjjE6mPwAl/"
    },
    {
     "label": "Talk reel",
     "url": "https://www.instagram.com/reel/DdrRGUSMUek/"
    }
   ]
  },
  {
   "cat": "Events",
   "title": "Oncoscope",
   "role": "Organizing Head 2025 · Organizing Committee 2026",
   "text": "All-India undergraduate oncology conference hosted at Government Medical College, Calicut. The 2026 edition, on 16 May, also launched the IEDC at the college.",
   "result": "National conference, two editions",
   "img": "oncoscope-stage.jpg",
   "links": [
    {
     "label": "2025 post",
     "url": "https://www.linkedin.com/posts/dr-sidharth-narayanan-7013281b8_oncoscope25-activity-7313210637067632641-EBtI"
    },
    {
     "label": "2025 post (2)",
     "url": "https://lnkd.in/p/gDhFbaMy"
    },
    {
     "label": "2026 post",
     "url": "https://www.linkedin.com/posts/dr-sidharth-narayanan-7013281b8_oncoscope2026-iedc-medicalinnovation-activity-7461294745915617280-MyGe"
    }
   ]
  },
  {
   "cat": "Events",
   "title": "Nutrition Primers",
   "role": "Community builder · Cytokine × Good Food Guru",
   "text": "A one-of-a-kind masterclass series priming doctors on nutrition and dietary counselling, with clinical nutritionists from leading hospitals in India and the UAE. Session 1, The Modern Doctor's Framework for Navigating Nutrition, ran online on 3 June 2026 for physicians, PG trainees and practitioners. Planned next: diabetes and metabolic nutrition, key NCDs, and nutrition in cancer care.",
   "result": "50+ online attendees · first of a multi-masterclass series",
   "img": "p-nutrition2.jpg",
   "links": []
  },
  {
   "cat": "Events",
   "title": "Medicine Magnum",
   "role": "Organizer · with Doc Tutorials · 2021",
   "text": "All-India medicine quiz for UGs and interns, one of the early flagship events of Doc Tutorials, with prizes worth ₹1 lakh. Run with College Union 2021, Calicut Medical College.",
   "result": "National reach",
   "img": "p-magnum.jpg",
   "links": []
  },
  {
   "cat": "Events",
   "title": "Corporate MD",
   "role": "Organizer & Host",
   "text": "A webinar series orienting doctors on Medical Affairs. The flagship session featured Medical Advisors and key opinion leaders.",
   "result": "~100 attendees at the flagship session",
   "img": "",
   "links": []
  },
  {
   "cat": "Ecosystems",
   "title": "IEDC, GMC Kozhikode",
   "role": "Student Lead · early advocate",
   "text": "Pushed for an Innovation and Entrepreneurship Development Centre at the medical college, driven by a vision of a biomedical technology corridor originating from Malabar. Launched on 16 May 2026 and now building a workflow with NIT Calicut, the Kerala Startup Mission, TinkerHub and TinkerSpace.",
   "result": "Ideathons, programmes and summits delivered",
   "img": "p-nitvisit.jpg",
   "links": [
    {
     "label": "Workflow with NIT Calicut",
     "url": "https://www.linkedin.com/posts/dr-sidharth-narayanan-7013281b8_biomedical-malabar-activity-7508524487974207488-be_x"
    },
    {
     "label": "IEDC launch",
     "url": "https://www.linkedin.com/posts/dr-sidharth-narayanan-7013281b8_oncoscope2026-iedc-medicalinnovation-activity-7461294745915617280-MyGe"
    }
   ]
  },
  {
   "cat": "Ecosystems",
   "title": "IEDC Summit, NIT Calicut",
   "role": "Panelist · HealthTech track · 19 October 2024",
   "text": "Panel on \"Bridging the Gap: Why Healthcare Needs Engineers for Groundbreaking Innovations\", run by Dr. Moopen's iNEST at the summit organized by the Kerala Startup Mission and NIT Calicut.",
   "result": "Invited panelist",
   "img": "p-summit.jpg",
   "links": []
  },
  {
   "cat": "Ecosystems",
   "title": "Claude Hackathon, Assistive Tech",
   "role": "Second prize · 4 October 2026",
   "text": "A 48-hour AI × hardware hackathon for assistive tech at TinkerSpace Calicut, with Claude Community India. Team Cosense built a wearable safety band concept for patients prone to wandering, such as those living with dementia.",
   "result": "Second prize",
   "img": "claude-hackathon.jpg",
   "links": []
  },
  {
   "cat": "Ecosystems",
   "title": "Repair Café × Medical Device Deconstruction Lab",
   "role": "IEDC GMC Kozhikode with TinkerSpace Kozhikode · October 2026",
   "text": "Exploring, understanding and reimagining medical devices at Government Medical College Kozhikode, with follow-up discussions and a workshop to come.",
   "result": "Upcoming",
   "img": "p-repair.jpg",
   "links": [
    {
     "label": "LinkedIn post",
     "url": "https://www.linkedin.com/posts/dr-sidharth-narayanan-7013281b8_tinkerspace-activity-7510251401655103488-5Lbz"
    }
   ]
  },
  {
   "cat": "Ecosystems",
   "title": "DIA-KMTC MedTech Conference",
   "role": "Participant · 2026",
   "text": "Kerala MedTech conference on quality systems and regulatory topics, attended as part of building ties with the state MedTech ecosystem.",
   "result": "Ecosystem engagement",
   "img": "p-dia.jpg",
   "links": [
    {
     "label": "LinkedIn post",
     "url": "https://www.linkedin.com/posts/dr-sidharth-narayanan-7013281b8_medtech-capa-qmsr-activity-7464003634633252864-inVR"
    }
   ]
  },
  {
   "cat": "Ecosystems",
   "title": "AI in Healthcare Summit, NIT Calicut",
   "role": "Delegate · 2025",
   "text": "Attended the AI in healthcare summit at NIT Calicut.",
   "result": "Delegate",
   "img": "",
   "links": [
    {
     "label": "LinkedIn post",
     "url": "https://www.linkedin.com/posts/medin-networking_ai-aihc-ugcPost-7404788491001327616-rXIN"
    }
   ]
  },
  {
   "cat": "Brands",
   "title": "Med/Acc",
   "role": "Marketing & Outreach Head · earlier Consulting Intern",
   "text": "A medical accelerator working with startups. Began with clinical validation, product evaluation and market strategy, and now leads marketing and outreach.",
   "result": "Current role",
   "img": "",
   "links": []
  },
  {
   "cat": "Brands",
   "title": "D2H, Doctor to Home",
   "role": "Pipeline project",
   "text": "A doctor-to-home platform for at-home healthcare services, in the pipeline.",
   "result": "In the pipeline",
   "img": "",
   "links": []
  },
  {
   "cat": "Brands",
   "title": "Project HealthSpan",
   "role": "Marketing & Brand Strategy",
   "text": "Brand and positioning work for a planned advanced diagnostics and preventive healthcare chain.",
   "result": "In development",
   "img": "",
   "links": []
  },
  {
   "cat": "Brands",
   "title": "Maya Edu",
   "role": "Outreach",
   "text": "Outreach for an AI-powered clinical learning platform with a differential diagnosis engine, practice cases from partner universities and exam preparation.",
   "result": "Ongoing",
   "img": "",
   "links": []
  },
  {
   "cat": "Brands",
   "title": "RM Healthcare",
   "role": "Marketing & design",
   "text": "Marketing and design for a clinics and diagnostics network based in Nilambur.",
   "result": "Clinics & diagnostics network, Nilambur",
   "img": "",
   "links": []
  },
  {
   "cat": "Brands",
   "title": "Reezet Health",
   "role": "Brand Strategy & Marketing · currently shelved",
   "text": "Brand identity, positioning and communication strategy for a doctor-led metabolic wellness programme.",
   "result": "Past project",
   "img": "",
   "links": []
  }
 ],
 "events": [
  {
   "year": "Before 2024",
   "items": [
    {
     "when": "2020-21",
     "title": "DOPA, Doctors Own Prep Academy",
     "role": "Academic content creator for NEET UG aspirants and early MBBS learners",
     "img": "",
     "imgMax": "440px",
     "url": "",
     "linkLabel": ""
    },
    {
     "when": "Oct-Nov 2021",
     "title": "Medicine Magnum",
     "role": "Organizer, all-India medicine quiz with Doc Tutorials and College Union 2021, Calicut Medical College",
     "img": "p-magnum.jpg",
     "imgMax": "300px",
     "url": "",
     "linkLabel": ""
    },
    {
     "when": "2022",
     "title": "Doctor Bhatia's",
     "role": "Marketing intern, NEET PG edtech",
     "img": "",
     "imgMax": "440px",
     "url": "",
     "linkLabel": ""
    },
    {
     "when": "2022",
     "title": "Cytokine Lectures",
     "role": "Head of Operations, later COO",
     "img": "",
     "imgMax": "440px",
     "url": "",
     "linkLabel": ""
    },
    {
     "when": "16 Jun - 17 Jul 2023",
     "title": "GTech µLearn × YIP 5.0",
     "role": "Outreach intern, engaging colleges across Kozhikode for the Young Innovators Programme",
     "img": "",
     "imgMax": "440px",
     "url": "",
     "linkLabel": ""
    }
   ]
  },
  {
   "year": "2024",
   "items": [
    {
     "when": "October 2024",
     "title": "Doctors AI Global Summit",
     "role": "Organizing Committee member; undergraduate student member of ICAIM",
     "img": "p-icaim.jpg",
     "imgMax": "440px",
     "url": "",
     "linkLabel": ""
    },
    {
     "when": "October 2024",
     "title": "Young Innovators Programme (K-DISC)",
     "role": "District-level winner with a nutrition app idea",
     "img": "",
     "imgMax": "440px",
     "url": "",
     "linkLabel": ""
    },
    {
     "when": "2024",
     "title": "Medinn begins",
     "role": "Started as Medinn Networking, connecting healthcare innovators, students and doctors",
     "img": "",
     "imgMax": "440px",
     "url": "",
     "linkLabel": ""
    },
    {
     "when": "19 Oct 2024",
     "title": "IEDC Summit, NIT Calicut",
     "role": "Panelist, HealthTech track: why healthcare needs engineers, with Dr. Moopen's iNEST",
     "img": "healthtech-panel.jpg",
     "imgMax": "440px",
     "url": "",
     "linkLabel": ""
    },
    {
     "when": "26 Oct 2024",
     "title": "AI in Healthcare hands-on workshop",
     "role": "Organizer, with Doctors AI and Cytokine",
     "img": "",
     "imgMax": "440px",
     "url": "",
     "linkLabel": ""
    },
    {
     "when": "27 Oct 2024",
     "title": "MedMeet 3.0, Calicut Medical College",
     "role": "Third prize, paper presentation of the KUHS award project on NCD risk factors among medical students",
     "img": "p-kuhs.jpg",
     "imgMax": "440px",
     "url": "",
     "linkLabel": ""
    },
    {
     "when": "14-15 Dec 2024",
     "title": "AI in Healthcare Virtual Global Summit",
     "role": "Speaker, Doctors AI",
     "img": "cert-doctorsai.jpg",
     "imgMax": "440px",
     "url": "",
     "linkLabel": ""
    }
   ]
  },
  {
   "year": "2025",
   "items": [
    {
     "when": "April 2025",
     "title": "Oncoscope 2025",
     "role": "Organizing Head, all-India oncology conference at GMC Calicut",
     "img": "oncoscope-stage.jpg",
     "imgMax": "440px",
     "url": "https://www.linkedin.com/posts/dr-sidharth-narayanan-7013281b8_oncoscope25-activity-7313210637067632641-EBtI",
     "linkLabel": "LinkedIn post"
    },
    {
     "when": "2025",
     "title": "Hospex Healthcare Expo 2025, Kochi",
     "role": "Organized and marketed the AI in Healthcare Conclave, startup outreach, and co-presented CureKart, a pharma supply chain startup",
     "img": "p-hospex.jpg",
     "imgMax": "440px",
     "url": "",
     "linkLabel": ""
    },
    {
     "when": "2025",
     "title": "Surgical Hackathon, TinkerHub Cochin",
     "role": "Co-organizer: logistics, mentorship, evaluation",
     "img": "",
     "imgMax": "440px",
     "url": "",
     "linkLabel": ""
    },
    {
     "when": "21-25 Oct 2025",
     "title": "Bio-entrepreneurship Advanced Certification",
     "role": "Residential course, IIT Palakkad with Kerala Biotechnology Commission",
     "img": "cert-iitpkd.jpg",
     "imgMax": "440px",
     "url": "https://www.linkedin.com/posts/dr-sidharth-narayanan-7013281b8_biotech-kbc-kerala-activity-7393547127483817984-iCHj",
     "linkLabel": "LinkedIn post"
    },
    {
     "when": "2025",
     "title": "AI in Healthcare Summit, NIT Calicut",
     "role": "Delegate",
     "img": "",
     "imgMax": "440px",
     "url": "",
     "linkLabel": ""
    }
   ]
  },
  {
   "year": "2026",
   "items": [
    {
     "when": "16 May 2026",
     "title": "Oncoscope 2.0 and IEDC launch",
     "role": "Organizing Committee, with the launch of the IEDC at the college",
     "img": "oncoscope2-banner.jpg",
     "imgMax": "440px",
     "url": "https://www.linkedin.com/posts/dr-sidharth-narayanan-7013281b8_oncoscope2026-iedc-medicalinnovation-activity-7461294745915617280-MyGe",
     "linkLabel": "LinkedIn post"
    },
    {
     "when": "2026",
     "title": "DIA-KMTC MedTech Conference",
     "role": "Participant, Thiruvananthapuram",
     "img": "p-dia.jpg",
     "imgMax": "440px",
     "url": "",
     "linkLabel": ""
    },
    {
     "when": "2026",
     "title": "NIT Calicut visit",
     "role": "At the Centre for Innovation, Entrepreneurship & Incubation, starting interdisciplinary projects between NIT Calicut and Calicut Medical College",
     "img": "p-nitvisit.jpg",
     "imgMax": "440px",
     "url": "https://www.linkedin.com/posts/dr-sidharth-narayanan-7013281b8_biomedical-malabar-activity-7508524487974207488-be_x",
     "linkLabel": "LinkedIn post"
    },
    {
     "when": "3 June 2026",
     "title": "Nutrition Primers #1",
     "role": "Online masterclass for doctors with clinical nutritionists from India and the UAE, Cytokine × Good Food Guru. 50+ online attendees",
     "img": "nutrition-primers.jpg",
     "imgMax": "440px",
     "url": "",
     "linkLabel": ""
    },
    {
     "when": "July 2026",
     "title": "MEDPG Calicut",
     "role": "Outreach Lead, current role: community engagement with podcasts, posters and a 60-day MCQ campaign",
     "img": "logo-medpg.png",
     "imgMax": "260px",
     "url": "",
     "linkLabel": ""
    },
    {
     "when": "5-6 Sept 2026",
     "title": "Medical & Surgical Intervention Hackathon",
     "role": "Organizer, overnight at TinkerSpace Calicut with IEDC CMC. 40+ participants",
     "img": "p-hackposter.jpg",
     "imgMax": "360px",
     "url": "https://www.instagram.com/reel/Dc7aeL2BnOi/",
     "linkLabel": "Hackathon reel"
    },
    {
     "when": "20-21 Sept 2026",
     "title": "The Handover, by Cytokine",
     "role": "Two-day internship bootcamp for new doctors across Kerala, conceptualized, run, marketed and executed. 100+ attendees from 15+ colleges",
     "img": "p-handover2.jpg",
     "imgMax": "440px",
     "url": "https://www.linkedin.com/posts/cytokinelectures_handover-medical-suturing-ugcPost-7510316634084122625-zreR",
     "linkLabel": "LinkedIn post"
    },
    {
     "when": "4 October 2026",
     "title": "Claude Hackathon: AI × Hardware for Assistive Tech",
     "role": "Second prize with team Cosense, 48 hours at TinkerSpace Calicut with Claude Community India",
     "img": "claude-hackathon.jpg",
     "imgMax": "300px",
     "url": "",
     "linkLabel": ""
    },
    {
     "when": "October 2026",
     "title": "Repair Café × Medical Device Deconstruction Lab",
     "role": "IEDC GMC Kozhikode with TinkerSpace Kozhikode",
     "img": "p-repair.jpg",
     "imgMax": "440px",
     "url": "https://www.linkedin.com/posts/dr-sidharth-narayanan-7013281b8_tinkerspace-activity-7510251401655103488-5Lbz",
     "linkLabel": "LinkedIn post"
    }
   ]
  }
 ],
 "services": [
  {
   "tab": "Edtech systems",
   "title": "Edtech growth systems",
   "text": "College-to-college outreach, student ambassador networks and WhatsApp-led distribution for medical education and healthcare products, built to work without a heavy tech stack.",
   "proofs": [
    "Cytokine Lectures",
    "MEDPG Calicut (current)",
    "KNYA Medical Apparel",
    "Doc Tutorials",
    "Doctor Bhatia's"
   ]
  },
  {
   "tab": "Events",
   "title": "Events, summits & hackathons",
   "text": "End-to-end delivery of conferences, bootcamps, webinars and hackathons: concept, speakers, marketing, design, outreach and on-the-day operations.",
   "proofs": [
    "AI in Healthcare Conclave (Hospex)",
    "Oncoscope",
    "Handover Bootcamp",
    "Corporate MD",
    "Medicine Magnum",
    "Surgical hackathon, Cochin",
    "Kozhikode medical hackathon",
    "Doctors AI summit 2024"
   ]
  },
  {
   "tab": "Brand",
   "title": "Healthcare brand & positioning",
   "text": "Brand identity, positioning and communication strategy for doctor-led ventures, clinics and diagnostics, including founder and physician positioning.",
   "proofs": [
    "RM Healthcare",
    "Reezet Health",
    "Project HealthSpan",
    "Med/Acc"
   ]
  },
  {
   "tab": "MedTech ecosystems",
   "title": "MedTech innovation ecosystems & strategy",
   "text": "Interdisciplinary hackathons, medical-college innovation cells and medicine × engineering partnerships that connect clinicians with engineers, makers, startups and state innovation bodies, to grow Malabar's biomedical startup ecosystem.",
   "proofs": [
    "IEDC GMC Kozhikode",
    "Interdisciplinary hackathons",
    "NIT Calicut × Calicut Medical College",
    "TinkerHub & TinkerSpace",
    "Repair Café × device lab",
    "Kerala Startup Mission"
   ]
  },
  {
   "tab": "Ventures",
   "title": "Venture support & clinical validation",
   "text": "Clinical input, product evaluation and market strategy for early-stage healthcare ventures, plus structured clinical problem statements that makers and startups can build on.",
   "proofs": [
    "Med/Acc",
    "Surgical hackathon, Cochin",
    "Cosense (Claude hackathon)",
    "YIP nutrition app"
   ]
  }
 ],
 "orgs": [
  {
   "name": "Cytokine Lectures",
   "mono": "Cy",
   "rel": "Edtech Growth Strategist & COO · 3+ years",
   "logo": "logo-cytokine.png",
   "hasLogo": true
  },
  {
   "name": "MEDPG Calicut",
   "mono": "MP",
   "rel": "Outreach Lead · current",
   "logo": "logo-medpg.png",
   "hasLogo": true
  },
  {
   "name": "Doctor Bhatia's",
   "mono": "DB",
   "rel": "Former marketing intern",
   "logo": "logo-dbmci.png",
   "hasLogo": true
  },
  {
   "name": "DOPA, Doctors Own Prep Academy",
   "mono": "DO",
   "rel": "Academic content creator, NEET UG (2020-21)",
   "logo": "logo-dopa.png",
   "hasLogo": true
  },
  {
   "name": "Doc Tutorials",
   "mono": "DT",
   "rel": "Organizer, Medicine Magnum (2021)",
   "logo": "logo-doctut.png",
   "hasLogo": true
  },
  {
   "name": "Maya Edu",
   "mono": "ME",
   "rel": "Outreach",
   "logo": "logo-maya.png",
   "hasLogo": true
  },
  {
   "name": "KNYA Medical Apparel",
   "mono": "KN",
   "rel": "Distribution partner · Handover partner",
   "logo": "logo-knya.png",
   "hasLogo": true
  },
  {
   "name": "Doctors AI",
   "mono": "DA",
   "rel": "Undergraduate Student Lead",
   "logo": "logo-doctorsai.png",
   "hasLogo": true
  },
  {
   "name": "Hospex",
   "mono": "HX",
   "rel": "Outreach to startups · AI Conclave",
   "logo": "logo-hospex.png",
   "hasLogo": true
  },
  {
   "name": "Oncoscope",
   "mono": "On",
   "rel": "Organizing Head 2025 · Committee 2026",
   "logo": "oncoscope2-banner.jpg",
   "hasLogo": true
  },
  {
   "name": "Kerala Startup Mission",
   "mono": "KS",
   "rel": "IEDC ecosystem partner",
   "logo": "logo-ksum.png",
   "hasLogo": true
  },
  {
   "name": "TinkerHub",
   "mono": "TH",
   "rel": "Hackathons in Cochin and Calicut",
   "logo": "logo-tinkerhub.png",
   "hasLogo": true
  },
  {
   "name": "TinkerSpace Calicut",
   "mono": "TS",
   "rel": "Hackathons and Repair Café",
   "logo": "logo-tinkerspace.png",
   "hasLogo": true
  },
  {
   "name": "IEDC GMC Kozhikode",
   "mono": "IE",
   "rel": "Student Lead",
   "logo": "logo-iedc.png",
   "hasLogo": true
  },
  {
   "name": "NIT Calicut",
   "mono": "NIT",
   "rel": "Panelist, delegate and IEDC partner",
   "logo": "logo-nitc.png",
   "hasLogo": true
  },
  {
   "name": "IIT Palakkad Technology I-Hub Foundation (IPTIF)",
   "mono": "IP",
   "rel": "Bio-entrepreneurship Advanced Certification, 2025",
   "logo": "logo-iptif.png",
   "hasLogo": true
  },
  {
   "name": "Kerala Biotechnology Commission",
   "mono": "KBC",
   "rel": "Bio-entrepreneurship certifications",
   "logo": "logo-kbc.png",
   "hasLogo": true
  },
  {
   "name": "Med/Acc",
   "mono": "MA",
   "rel": "Marketing & Outreach Head",
   "logo": "logo-medacc.png",
   "hasLogo": true
  },
  {
   "name": "RM Healthcare",
   "mono": "RM",
   "rel": "Marketing & design · clinics and diagnostics, Nilambur",
   "logo": "logo-rm.png",
   "hasLogo": true
  },
  {
   "name": "Reezet Health",
   "mono": "Rz",
   "rel": "Brand strategy & marketing",
   "logo": "logo-reezet.png",
   "hasLogo": true
  },
  {
   "name": "D2H, Doctor to Home",
   "mono": "D2H",
   "rel": "Pipeline project · at-home healthcare platform",
   "logo": "logo-d2h.png",
   "hasLogo": true
  },
  {
   "name": "Project HealthSpan",
   "mono": "HS",
   "rel": "Marketing & brand strategy",
   "logo": "",
   "hasLogo": false
  },
  {
   "name": "Good Food Guru",
   "mono": "GFG",
   "rel": "Nutrition Primers partner",
   "logo": "logo-gfg.png",
   "hasLogo": true
  },
  {
   "name": "Young Innovators Programme (K-DISC)",
   "mono": "YIP",
   "rel": "District-level winner · outreach intern (2023)",
   "logo": "logo-yip.png",
   "hasLogo": true
  },
  {
   "name": "Government Medical College, Kozhikode",
   "mono": "GMC",
   "rel": "Generalist · Literary Club Secretary · IEDC Student Lead",
   "logo": "logo-gmckkd.png",
   "hasLogo": true
  },
  {
   "name": "Indian College of AI in Medicine (ICAIM)",
   "mono": "IC",
   "rel": "Undergraduate student member · aligned with Doctors AI",
   "logo": "logo-doctorsai.png",
   "hasLogo": true
  },
  {
   "name": "CureKart",
   "mono": "CK",
   "rel": "Co-presenter at Hospex 2025 · pharma supply chain startup",
   "logo": "logo-curekart.png",
   "hasLogo": true
  },
  {
   "name": "GTech µLearn",
   "mono": "µL",
   "rel": "YIP 5.0 outreach intern, 2023",
   "logo": "logo-yip.png",
   "hasLogo": true
  }
 ],
 "inner": [
  "cytokine",
  "medpg",
  "doctorsai",
  "iedc",
  "tinker",
  "medacc"
 ],
 "outer": [
  "bhatia",
  "doctut",
  "maya",
  "hospex",
  "oncoscope",
  "gfg",
  "ksum",
  "nit",
  "reezet",
  "healthspan",
  "knya",
  "research",
  "certs"
 ]
};
