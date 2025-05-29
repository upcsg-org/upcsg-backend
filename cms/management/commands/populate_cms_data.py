from django.core.management.base import BaseCommand
from cms.models import Article, Event, Scholarship, Internship, Announcement
from datetime import date

class Command(BaseCommand):
    help = 'Populates initial content data (articles, events, scholarships, internships, announcements)'

    def handle(self, *args, **kwargs):
        self.stdout.write('Starting to populate content data...')

        # Create articles
        article_data = [
            {
                'title': 'Internship Fair 2025',
                'body': """𝟭 𝗗𝗮𝘆 𝗟𝗲𝗳𝘁 ‘𝘁𝗶𝗹 𝘁𝗵𝗲 𝗨𝗣𝗖𝗦𝗚 𝗜𝗻𝘁𝗲𝗿𝗻𝘀𝗵𝗶𝗽 𝗙𝗮𝗶𝗿 𝟮𝟬𝟮𝟱!

                We've reached maximum capacity — on-site registration is now CLOSED.

                📣 REMINDER:
                • 𝗥𝗲𝗴𝗶𝘀𝘁𝗲𝗿𝗲𝗱 𝗽𝗮𝗿𝘁𝗶𝗰𝗶𝗽𝗮𝗻𝘁𝘀 must arrive 𝗼𝗻 𝗼𝗿 𝗯𝗲𝗳𝗼𝗿𝗲 𝟭:𝟯𝟬 𝗣𝗠. Latecomers will have their slots given to waitlisted participants present at the venue.

                • 𝗪𝗮𝗶𝘁𝗹𝗶𝘀𝘁𝗲𝗱 𝗽𝗮𝗿𝘁𝗶𝗰𝗶𝗽𝗮𝗻𝘁𝘀 are encouraged to join online instead. The 𝗼𝗻𝗹𝗶𝗻𝗲 𝗺𝗲𝗲𝘁 𝗹𝗶𝗻𝗸 𝘄𝗶𝗹𝗹 𝗯𝗲 𝘀𝗲𝗻𝘁 𝘃𝗶𝗮 𝗲𝗺𝗮𝗶𝗹. If slots open up, you may still be called to join on-site.

                Let’s make the most of this opportunity together, whether on-site or online!

                #PadayonKomsai #InternshipFair2025 #KomsaiOpportunities""",
                'author': 'UPCSG'
            },
            {
                'title': 'TUDLO: A Guilder Tutoring Program (MATH 54 Tutoring)',
                'body': """𝗠𝗮𝘁𝗵 𝟱𝟰 𝗹𝗼𝗻𝗴 𝗲𝘅𝗮𝗺 𝗶𝘀 𝗰𝗹𝗼𝘀𝗶𝗻𝗴 𝗶𝗻?

                Don’t worry, 𝗙𝗿𝗲𝘀𝗵𝗶𝗲𝘀 — we’ve got your back! 🦉💡 Come through for 𝗧𝗨𝗗𝗟𝗢: 𝗔 𝗚𝘂𝗶𝗹𝗱𝗲𝗿 𝗧𝘂𝘁𝗼𝗿𝗶𝗻𝗴 𝗣𝗿𝗼𝗴𝗿𝗮𝗺 this 𝗔𝗽𝗿𝗶𝗹 𝟮𝟯, 𝟮𝟬𝟮𝟱 (𝗪𝗲𝗱𝗻𝗲𝘀𝗱𝗮𝘆) for a study session full of support, clarity, and that classic Komsai camaraderie!

                Whether you're an early riser or get your groove on after lunch:
                𝗦𝗲𝘀𝘀𝗶𝗼𝗻 𝟭: 𝟵𝗔𝗠–𝟭𝟮𝗡𝗡
                𝗦𝗲𝘀𝘀𝗶𝗼𝗻 𝟮: 𝟭𝗣𝗠–𝟰𝗣𝗠

                Head over to 𝗔𝗦 𝟯𝟬𝟮–𝟯𝟬𝟲 and let’s conquer those formulas together.

                #TUDLO
                #PadayonKomsai
                #Math54Tutorial""",
                'author': 'UPCSG'
            },
            {
                'title': 'MX. Komsai 2025',
                'body': """𝗠𝗫 𝗞𝗢𝗠𝗦𝗔𝗜 𝟮𝟬𝟮𝟱 𝗢𝗙𝗙𝗜𝗖𝗜𝗔𝗟 𝗣𝗢𝗦𝗧𝗘𝗥

                The gears are in motion, and the countdown begins- only over a week left until we crown our Mx. Komsai 2025. With eight contenders ready to take the stage, who will rise as the next to steal the show?
                
                Don’t forget to get your ticket now for only ₱20.00!
                
                All of the proceeds will be donated to the crowned contender’s chosen charity/organization.
                🔗 https://forms.gle/NxXZKCaaYwUMcdJ4A
                
                𝗧𝗵𝗶𝘀 𝗲𝘃𝗲𝗻𝘁 𝗶𝘀 𝗽𝗿𝗲𝘀𝗲𝗻𝘁𝗲𝗱 𝗯𝘆 UP Computer Science Guild and UP Cebu Department of Computer Science.
                𝟬𝟯.𝟬𝟳.𝟮𝟱 - 𝗣𝗘𝗥𝗙𝗢𝗥𝗠𝗜𝗡𝗚 𝗔𝗥𝗧𝗦 𝗛𝗔𝗟𝗟

                𝗣𝗼𝘄𝗲𝗿𝗲𝗱 𝗯𝘆:   
                MYT Solutions

                𝗦𝘂𝗽𝗽𝗼𝗿𝘁𝗲𝗱 𝗯𝘆:
                Synacy

                𝗕𝗿𝗼𝘂𝗴𝗵𝘁 𝘁𝗼 𝘆𝗼𝘂 𝗯𝘆:
                Simantikos Statistical Society
                UPC University Student Council
                Tug-Ani
                University of the Philippines Ecological Society - UPECS
                LANOG
                Serve Up
                DOST SA UP Cebu
                UP Cebu Sciences Federation 

                𝗠𝗲𝗱𝗶𝗮 𝗣𝗮𝗿𝘁𝗻𝗲𝗿:
                Focality

                Illustration: Ishah Bautista 

                #PadayonKomsai #KomsaiWeek2025 #MxKomsai2025""",
                'author': 'UPCSG'
            },
            {
                'title': 'New Board of Directors for SY 2025-2026',
                'body': """😲🎉𝗩𝗢𝗧𝗜𝗡𝗚 𝗥𝗘𝗦𝗨𝗟𝗧𝗦 𝗔𝗥𝗘 𝗜𝗡!!!😲🎉

                GUILDERS, YOU MADE IT COUNT! 🥳🥳🥳
                The ballots have been cast, the votes have been tallied, and the results are finally in! 🗳️
                
                In a rare and exciting outcome, both candidates for the Creatives Director position—Abellanosa and Campomanes—garnered exactly 111 votes each. To resolve the tie, a virtual coin toss was held via Google Meet, facilitated by Julius Manigo Jr. of the Elections Committee.
                
                The process was witnessed by members of the Elections Committee, current UPCSG Executive Director Bazer Timothy Nuñez, UPCSG Adviser Mr. Eli Tan, and DCS Lecturer Mr. Gabriel Howard Awatin.
                
                You may view the official recording here:
                https://drive.google.com/.../1bNmQP4Cem8XsOMft8G5.../view...
                
                This procedure was carried out in accordance with Resolution 2025-03, a constitutional measure enacted to address electoral tie-break scenarios.
                𝗥𝗲𝘀𝗼𝗹𝘂𝘁𝗶𝗼𝗻 𝟮𝟬𝟮𝟱-𝟬𝟯: https://drive.google.com/.../1SJs3U12tfCdkzzhEGgx.../view...
                
                Thank you to everyone who took part in shaping the future of the UP Computer Science Guild. Your voice mattered—and it was heard loud and clear. 💚💻
                
                To all the candidates, thank you for your courage and commitment. And to our newly elected leaders, C O N G R A T U L A T I O N S ! ! ! The Komsai journey begins—led with heart, vision, and purpose.
                
                Here’s an inspirational quote from a well-known computer scientist, Grace Hopper!
                “Leadership is a two-way street, loyalty up and loyalty down. Respect for one's superiors; care for one's crew.”
                -𝗚𝗿𝗮𝗰𝗲 𝗛𝗼𝗽𝗽𝗲𝗿
                
                Executive Director: James Elijah Gabriel Ty
                Executive Vice Director: Trishia Mae Basmayor
                Secretary: Diane Angel Bustamante
                Treasurer: Karl Inopiquez
                Auditor: Chriscia Xanelle Llamas
                Marketing Director: Jesse Keane Catedral
                Creatives Director: Kimberly Campomanes
                Partnership & Linkages Director: Princess Jaena Marie De La Peña
                Communications and Logistics Director: Erik James Caliskis
                Education and Development Director: Jezreel Chad Lumbab

                Padayon, Komsai! 🚀

                #UPCSGElections2025 #PadayonKomsai""",
                'author': 'UPCSG'
            },
            {
                'title': '🗳️ 𝗚𝗨𝗜𝗟𝗗𝗘𝗥𝗦, 𝗩𝗢𝗧𝗜𝗡𝗚 𝗜𝗦 𝗡𝗢𝗪 𝗖𝗟𝗢𝗦𝗘𝗗',
                'body': """🗳️ 𝗚𝗨𝗜𝗟𝗗𝗘𝗥𝗦, 𝗩𝗢𝗧𝗜𝗡𝗚 𝗜𝗦 𝗡𝗢𝗪 𝗖𝗟𝗢𝗦𝗘𝗗

                The ballots are in. Your voices have been heard.

                As the curtain falls on this crucial moment in the Guild’s journey, we thank you for making your mark. Every vote cast is a step toward the future we are building—together.

                Stay tuned as we prepare to unveil the next leaders who will carry the torch forward.

                𝗧𝗵𝗲 𝗳𝘂𝘁𝘂𝗿𝗲 𝗯𝗲𝗴𝗶𝗻𝘀 𝘀𝗼𝗼𝗻.

                #PadayonKomsai #UPCSGElections2025""",
                'author': 'UPCSG'
            },
            {
                'title': 'Internship at Full Scale',
                'body': """Please take note of the internship program of Full Scale:

                As part of their current and upcoming software development initiatives, their primary focus remains on web application development using the C# and .NET stack. Given this direction, please clearly indicate in your CVs the projects you have worked on and the tech stacks you have experience with.
                
                Here are the key updates to their internship program:
                Required Hours: Minimum of 300 hours
                Internship Allowance: Increased to ₱15,000 per month
                New Simplified Application Process:
                For highly qualified students, you may submit their CVs directly at penot@fullscale.io. They no longer use their website for internship applications.
                They will conduct a thorough CV screening, so they encourage you to ensure that your resumes are complete—especially highlighting relevant project experience and tech stacks.
                Shortlisted applicants will proceed to a technical interview.
                
                Please note that they have limited internship slots available each year, which is why they implement a rigorous screening process to ensure a good match between the intern’s skills and the demands of their real-world, client-facing projects.""",
                'author': 'UPCSG'
            },
            {
                'title': 'About SLAS Online',
                'body': """Students from the University of the Philippines (UP) come from all walks of life. Some of them may not be able to afford to pay the full tuition and other expenses to complete their academic requirements. As the UP community transitions to remote learning, other forms of learning assistance are needed to respond to the changing times.

                To expand the support to financially-challenged students and expedite the processing support for academic activities, the University developed the Student Learning Assistance System (SLAS). The SLAS is an expansion of the Student Financial Assistance Online (SFA Online). The UP designed the SFA Online in 2014 to accept applications for tuition subsidy and allowance. Beginning on 7 September 2020, UP students may apply directly for financial support and learning assistance in the SLAS Online (slasonline.up.edu.ph). The expanded System will gather information on students' financial capacity, connectivity situation and connectivity options, and learning assistance requirements to help the University determine the support to be extended to the applicant.

                For AY 2023-2024, the SLAS Online will support applications to the following learning assistance programs:

                Grants-in-Aid Program (GIAP)

                UP created the Grants-in-Aid Program (GIAP) to reduce the cost paid by students during enrollment, based on the household's paying capacity to which a student belongs. Through the GIAP, UP may subsidize a portion of the full cost required during enrollment and, in some instances, grant additional subsidy to waive miscellaneous fees and grant monthly cash allowances.

                The UP GIAP is open to undergraduate students, including students enrolled in Law and Medicine.""",
                'author': 'UPCSG'
            },
        ]

        created_articles = []
        for data in article_data:
            article, created = Article.objects.get_or_create(
                title=data['title'],
                defaults={
                    'body': data['body'],
                    'author': data['author']
                }
            )
            created_articles.append(article)
            msg = f'Created article: {data["title"]}' if created else f'Article already exists: {data["title"]}'
            self.stdout.write(self.style.SUCCESS(msg) if created else self.style.WARNING(msg))

        # Create events
        event_data = [
            {
                'title': 'Org Fair 2025-2026',
                'image_url': 'https://scontent.fmnl10-1.fna.fbcdn.net/v/t39.30808-6/454339352_7978068715608644_1447280619382438742_n.jpg?_nc_cat=104&ccb=1-7&_nc_sid=cf85f3&_nc_ohc=VgYANCg8l6wQ7kNvwGgeGKc&_nc_oc=Adl30NnHHvVZW9v9KD1SKVwKtUmu256auvDd6nXtOBgsM7DIyQr30sKuHSZcum5VnlU&_nc_zt=23&_nc_ht=scontent.fmnl10-1.fna&_nc_gid=osMEL0q0a0Kxpif9x939Sw&oh=00_AfISW5u37KtP_xAW3n_GOqor_8vJ1sjjH7-W4M6-9V1jeA&oe=683D9B6F',
                'start_date': date(2025, 8, 21),
                'end_date': date(2025, 8, 21),
                'location': 'UP Cebu',
                'body': "Details to follow",
                'article': None,
                'external_url': None
            },
            {
                'title': 'Internship Fair 2025',
                'image_url': "https://scontent.fmnl17-8.fna.fbcdn.net/v/t39.30808-6/494218630_1194054335842347_7024423360559617811_n.jpg?_nc_cat=107&ccb=1-7&_nc_sid=127cfc&_nc_ohc=7TrDE6tvRiEQ7kNvwEqlU0c&_nc_oc=AdkOjyvE5a0x3YBSagJsVvsP6v-WUJ-x5mojAoqT8rq2nfKlqz_7LV-fMTEpzIIgrPk&_nc_zt=23&_nc_ht=scontent.fmnl17-8.fna&_nc_gid=v4K-u5hdi3zwl9nYVp20hw&oh=00_AfI99Z_qRQVyrakkBDw4s5Lwjw98bYQQ9GkvVuO_7RbXAA&oe=683D85A7",
                'start_date': date(2025, 4, 30),
                'end_date': date(2025, 4, 30),
                'location': 'Lawak Sinehan, UP Cebu',
                'body': "𝟭 𝗗𝗮𝘆 𝗟𝗲𝗳𝘁 ‘𝘁𝗶𝗹 𝘁𝗵𝗲 𝗨𝗣𝗖𝗦𝗚 𝗜𝗻𝘁𝗲𝗿𝗻𝘀𝗵𝗶𝗽 𝗙𝗮𝗶𝗿 𝟮𝟬𝟮𝟱! We've reached maximum capacity — on-site registration is now CLOSED.",
                'article': created_articles[0],
                'external_url': None
            },
            {
                'title': 'TUDLO: A Guilder Tutoring Program (MATH 54 Tutoring)',
                'image_url': "https://scontent.fmnl10-1.fna.fbcdn.net/v/t39.30808-6/491888956_1188241243090323_8888041213456360942_n.jpg?_nc_cat=101&ccb=1-7&_nc_sid=833d8c&_nc_ohc=Oi76SHg2OK0Q7kNvwGXSWw_&_nc_oc=Adn5tdyND3BHEb95kRsl7cSn1dIDyL0wDk75B_ycPxFMjUImV8KNMqY82Gm_hDePxH4&_nc_zt=23&_nc_ht=scontent.fmnl10-1.fna&_nc_gid=EobZPpZAeKG8SCBlAIHSvQ&oh=00_AfIobG4I8HGLBVFplZX2z-VRQcXaEj1VGcfZvQRck3ahgw&oe=683DA678",
                'start_date': date(2025, 4, 23),
                'end_date': date(2025, 4, 23),
                'location': 'AS 302-306, UP Cebu',
                'body': "Don’t worry, 𝗙𝗿𝗲𝘀𝗵𝗶𝗲𝘀 — we’ve got your back! 🦉💡 Come through for 𝗧𝗨𝗗𝗟𝗢: 𝗔 𝗚𝘂𝗶𝗹𝗱𝗲𝗿 𝗧𝘂𝘁𝗼𝗿𝗶𝗻𝗴 𝗣𝗿𝗼𝗴𝗿𝗮𝗺 this 𝗔𝗽𝗿𝗶𝗹 𝟮𝟯, 𝟮𝟬𝟮𝟱 (𝗪𝗲𝗱𝗻𝗲𝘀𝗱𝗮𝘆) for a study session full of support, clarity, and that classic Komsai camaraderie!",
                'article': created_articles[1],
                'external_url': None
            },
            {
                'title': 'Scratch That! An Outreach Program',
                'image_url': "https://scontent.fmnl10-1.fna.fbcdn.net/v/t39.30808-6/489336227_1177321120849002_2408889165578344413_n.jpg?_nc_cat=110&ccb=1-7&_nc_sid=127cfc&_nc_ohc=nTF5WwOqXVoQ7kNvwGSqVZ7&_nc_oc=AdkbJGu5AhU-gzXnlSQm9h997bydcv6rcAj9Sk-ezPTjp4HoC5ciBgi4Z1p7hMcTvB8&_nc_zt=23&_nc_ht=scontent.fmnl10-1.fna&_nc_gid=uCE1SKwwRDYJ-PlMABcanw&oh=00_AfLTR7Xwxnt__4mVsUqsaqPI1jQy30VGcaKg-g4EGhmWaQ&oe=683D915B",
                'start_date': date(2025, 4, 9),
                'end_date': date(2025, 4, 9),
                'location': 'Barangay Hall, Lahug',
                'body': "Don’t worry, 𝗙𝗿𝗲𝘀𝗵𝗶𝗲𝘀 — we’ve got your back! 🦉💡 Come through for 𝗧𝗨𝗗𝗟𝗢: 𝗔 𝗚𝘂𝗶𝗹𝗱𝗲𝗿 𝗧𝘂𝘁𝗼𝗿𝗶𝗻𝗴 𝗣𝗿𝗼𝗴𝗿𝗮𝗺 this 𝗔𝗽𝗿𝗶𝗹 𝟮𝟯, 𝟮𝟬𝟮𝟱 (𝗪𝗲𝗱𝗻𝗲𝘀𝗱𝗮𝘆) for a study session full of support, clarity, and that classic Komsai camaraderie!",
                'article': None,
                'external_url': 'https://www.facebook.com/photo/?fbid=1177356470845467&set=a.565851071996013'
            },
            {
                'title': 'Komsai Week 2025: Komsai Cup Mobile Legends Game Day',
                'image_url': "https://scontent.fmnl10-1.fna.fbcdn.net/v/t39.30808-6/488503396_1172725814641866_4633503204350986226_n.jpg?_nc_cat=104&ccb=1-7&_nc_sid=127cfc&_nc_ohc=0BiOeiaixGIQ7kNvwE3NO9D&_nc_oc=Adnr1DuoMNRfukQ1fZ8ouzAuG2OOXoqa8DZLn6xaPhA_yPz_85iw7X1PsGMciSPN8nc&_nc_zt=23&_nc_ht=scontent.fmnl10-1.fna&_nc_gid=nD2B-02yFZpXVuNbyUk84w&oh=00_AfIuo_9Wr1rlDhSOQrUAc0DrQDqE9nYhVw_qgVtAZ4SYMg&oe=683DA3C2",
                'start_date': date(2025, 3, 5),
                'end_date': date(2025, 3, 5),
                'location': 'Arts and Sciences Hall, UP Cebu',
                'body': "The battlefield is set, and the competition is about to get intense! ⚔️ Witness epic clashes, insane outplays, and strategic team fights as our Guilders battle for MLBB supremacy! 🏆",
                'article': None,
                'external_url': 'https://www.facebook.com/photo/?fbid=1150740586840389&set=a.565851071996013'
            },
            {
                'title': 'MX. Komsai 2025',
                'image_url': "https://scontent.fmnl10-1.fna.fbcdn.net/v/t39.30808-6/486603235_1167908521790262_6196022094202757362_n.jpg?_nc_cat=110&ccb=1-7&_nc_sid=127cfc&_nc_ohc=1DD9aCfTOHwQ7kNvwHWN-Df&_nc_oc=AdlBpWN4RioaDz4tWYJdfLfzGR1ysvbS18_ouBWEPdOCMWiAIBMUhKYyUJjjHE_-RxU&_nc_zt=23&_nc_ht=scontent.fmnl10-1.fna&_nc_gid=Cf3EZVEVWj4KCT1LaLM2mw&oh=00_AfK_K61fLO2atHlSZ1X3tXycXf7RDOxMCHv-ldc9QxqgVA&oe=683DAC88",
                'start_date': date(2025, 3, 7),
                'end_date': date(2025, 3, 7),
                'location': 'Performance Arts Hall, UP Cebu',
                'body': "Don’t worry, 𝗙𝗿𝗲𝘀𝗵𝗶𝗲𝘀 — we’ve got your back! 🦉💡 Come through for 𝗧𝗨𝗗𝗟𝗢: 𝗔 𝗚𝘂𝗶𝗹𝗱𝗲𝗿 𝗧𝘂𝘁𝗼𝗿𝗶𝗻𝗴 𝗣𝗿𝗼𝗴𝗿𝗮𝗺 this 𝗔𝗽𝗿𝗶𝗹 𝟮𝟯, 𝟮𝟬𝟮𝟱 (𝗪𝗲𝗱𝗻𝗲𝘀𝗱𝗮𝘆) for a study session full of support, clarity, and that classic Komsai camaraderie!",
                'article': created_articles[2],
                'external_url': None
            },
            {
                'title': 'Komsai Week 2025: Kode in da Dark!',
                'image_url': "https://scontent.fmnl10-1.fna.fbcdn.net/v/t39.30808-6/485875663_1162937612287353_8050073385472744523_n.jpg?stp=dst-jpg_s600x600_tt6&_nc_cat=105&ccb=1-7&_nc_sid=127cfc&_nc_ohc=NBvYhbYHz28Q7kNvwH8srcB&_nc_oc=AdmExDx3rpma8yrteQVV3A7bocKVlvtWtUMSw9drCY-iyonUyQCohacRtLAVMNSWekY&_nc_zt=23&_nc_ht=scontent.fmnl10-1.fna&_nc_gid=lAlWzUgn_KzRyJBghLj-_g&oh=00_AfJ98H0nP16XV-vcniu10GTltF0we7KDbGTgZ2IAWiTVhg&oe=683DB942",
                'start_date': date(2025, 3, 3),
                'end_date': date(2025, 3, 3),
                'location': 'Performing Arts Hall, UP Cebu',
                'body': "𝗗𝗮𝘁’𝘀 𝗿𝗶𝗴𝗵𝘁! For the first time in history, 𝗞𝗼𝗺𝘀𝗮𝗶 𝗪𝗲𝗲𝗸 𝟮𝟬𝟮𝟱 brings you its newest installment—𝑲𝒐𝒅𝒆 𝒊𝒏 𝒅𝒂 𝑫𝒂𝒓𝒌!",
                'article': None,
                'external_url': None
            },
        ]

        for data in event_data:
            event, created = Event.objects.get_or_create(
                title=data['title'],
                defaults={
                    'image_url': data['image_url'],
                    'start_date': data['start_date'],
                    'end_date': data['end_date'],
                    'location': data['location'],
                    'body': data['body'],
                    'article': data['article'],
                    'external_url': data['external_url']
                }
            )
            msg = f'Created event: {data["title"]}' if created else f'Event already exists: {data["title"]}'
            self.stdout.write(self.style.SUCCESS(msg) if created else self.style.WARNING(msg))

        # Create scholarships
        scholarship_data = [
            {
                'title': '2025 DOST Junior Level Science Scholarships',
                'image_url': 'https://scontent.fmnl17-8.fna.fbcdn.net/v/t39.30808-6/498191715_711116568096662_8815218629813709805_n.jpg?_nc_cat=107&ccb=1-7&_nc_sid=833d8c&_nc_ohc=4vjwgDLiTk4Q7kNvwGBn0Cj&_nc_oc=AdlXXoppmxicdaCp2gRN_lav9WrTxJCb_JcwVGRI7ofxq0f-btOM-Md3J4Vi8ou1Ktc&_nc_zt=23&_nc_ht=scontent.fmnl17-8.fna&_nc_gid=Qw7sruIbj_JPzpviaYJ1CA&oh=00_AfIDIlm9IN38DV3s-t4S5IJBqavE7s2tIk_7BqYY_E5SAA&oe=683DD000',
                'opening_date': date(2025, 4, 23),
                'deadline': date(2025, 5, 23),
                'requirements': 'Must be a Filipino citizen, STEM senior high graduate.',
                'benefits': 'Monthly stipend, tuition coverage, book allowance',
                'organization': 'DOST-SEI',
                'article': None,
                'external_url': 'https://region3.dost.gov.ph/2025-junior-level-science-scholarships-jlss/'
            },
            {
                'title': 'Student Learning Assistance System',
                'image_url': 'https://scontent.fmnl10-1.fna.fbcdn.net/v/t39.30808-6/489115962_1157366529736185_6164664926816216232_n.jpg?_nc_cat=100&ccb=1-7&_nc_sid=127cfc&_nc_ohc=ETUv-OdIKT0Q7kNvwFMTVgw&_nc_oc=AdkCD8w-7r-olYQGNgtjBo8VSFIWdvh2nSnXXE_bN1d5VwV90OZh3kPQTt8dYYkETiY&_nc_zt=23&_nc_ht=scontent.fmnl10-1.fna&_nc_gid=r00CCXPpZsAl3CV8Q3EcTw&oh=00_AfI19U5vAkAGbJ_T9fzft9LDO10wUeMjwk5Q9sy7mVOgHg&oe=683DC8F2',
                'opening_date': date(2025, 1, 22),
                'deadline': date(2025, 1, 30),
                'requirements': 'Bonafide students of UP. Students in need of learning assistance from UP.',
                'benefits': 'Financial assistance in the form of grants, subsidies and scholarships.',
                'organization': 'University of the Philippines',
                'article': created_articles[6],
                'external_url': None
            },
            {
                'title': 'GBF STEM-College Scholarship',
                'image_url': 'https://www.gokongweibrothersfoundation.org/temporary/storage/images/3.png',
                'opening_date': date(2025, 1, 22),
                'deadline': date(2025, 5, 30),
                'requirements': 'Check their site for more details!',
                'benefits': 'Check their site for more details!',
                'organization': 'Gokongwei Brothers Foundation',
                'article': None,
                'external_url': 'https://www.gokongweibrothersfoundation.org/programs/gbf-stem-scholarship-for-excellence'
            },
        ]

        for data in scholarship_data:
            scholarship, created = Scholarship.objects.get_or_create(
                title=data['title'],
                defaults={
                    'image_url': data['image_url'],
                    'opening_date': data['opening_date'],
                    'deadline': data['deadline'],
                    'requirements': data['requirements'],
                    'benefits': data['benefits'],
                    'organization': data['organization'],
                    'article': data['article'],
                    'external_url': data['external_url']
                }
            )
            msg = f'Created scholarship: {data["title"]}' if created else f'Scholarship already exists: {data["title"]}'
            self.stdout.write(self.style.SUCCESS(msg) if created else self.style.WARNING(msg))

        # Create internships
        internship_data = [
            {
                'title': 'Symph Dev Internship',
                'image_url': 'https://cdn.prod.website-files.com/67a5c0551e6431e75ae1aa05/68139318e0eaaa0f8c606c50_symph%20footer.svg',
                'organization': 'Symph',
                'requirements': 'Proficient in React, Django, and teamwork.',
                'benefits': 'Mentorship, allowance, and real-world dev experience',
                'opening_date': date(2025, 4, 1),
                'deadline': date(2025, 6, 13),
                'article': None,
                'external_url': 'https://www.symph.co/blog/internships-at-symph'
            },
            {
                'title': 'Full Scale Internship',
                'image_url': 'https://media.licdn.com/dms/image/v2/C4E0BAQEPP4eWqnTdmg/company-logo_200_200/company-logo_200_200/0/1630646560029/fullscale_io_logo?e=1753920000&v=beta&t=3P1AceOMt_RUJN3n4bd57ZbggrHUJgAfFAXkFNbsHTU',
                'organization': 'Full Scale',
                'requirements': 'Minimum of 300 hours, CVs to be submitted in portal',
                'benefits': '₱15,000 per month',
                'opening_date': date(2025, 4, 1),
                'deadline': date(2025, 6, 13),
                'article': created_articles[5],
                'external_url': None
            },
            {
                'title': 'Advanced World Systems, Inc. (AWS)',
                'image_url': 'https://yt3.googleusercontent.com/vtckU0sW8j7MgqC6SnO4Ed3yaG0t-fFwhUEir-9SMTOuYBIXPkfSx3fzD3YrwUj8PI46fw1Le9o=s900-c-k-c0x00ffffff-no-rj',
                'organization': 'Advanced World Systems, Inc. (AWS)',
                'requirements': 'To be updated',
                'benefits': 'To be updated',
                'opening_date': date(2025, 4, 1),
                'deadline': date(2025, 6, 13),
                'article': None,
                'external_url': None
            },
        ]

        for data in internship_data:
            internship, created = Internship.objects.get_or_create(
                title=data['title'],
                defaults={
                    'image_url': data['image_url'],
                    'organization': data['organization'],
                    'requirements': data['requirements'],
                    'benefits': data['benefits'],
                    'opening_date': data['opening_date'],
                    'deadline': data['deadline'],
                    'article': data['article'],
                    'external_url': data['external_url']
                }
            )
            msg = f'Created internship: {data["title"]}' if created else f'Internship already exists: {data["title"]}'
            self.stdout.write(self.style.SUCCESS(msg) if created else self.style.WARNING(msg))

        # Create announcements
        announcement_data = [
            {
                'title': 'New Board of Directors for SY 2025-2026',
                'image_url': 'https://scontent.fmnl17-8.fna.fbcdn.net/v/t39.30808-6/495143152_1197002582214189_9100955845038678544_n.jpg?_nc_cat=107&ccb=1-7&_nc_sid=833d8c&_nc_ohc=bD15g2Ve2a8Q7kNvwHQxyAH&_nc_oc=AdmSsD7ZgvRjaTXJw4fdSyFEVomHYPsai_DpeCp2xdkLCA1fNyiPOVEA8UqF00N8oZM&_nc_zt=23&_nc_ht=scontent.fmnl17-8.fna&_nc_gid=ra65AS3ZHZ5Nf2pIQhKneQ&oh=00_AfLvllakQ6sun_elxYrRcmspRnuXE1Ahq6DDjthFdS0mZQ&oe=683DB817',
                'summary': 'GUILDERS, YOU MADE IT COUNT! 🥳🥳🥳 The ballots have been cast, the votes have been tallied, and the results are finally in! 🗳️',
                'article': created_articles[3],
                'external_url': None
            },
            {
                'title': 'Voting Form is now CLOSED!',
                'image_url': 'https://scontent.fmnl17-3.fna.fbcdn.net/v/t39.30808-6/494700119_1196336028947511_7062262438213342343_n.jpg?_nc_cat=103&ccb=1-7&_nc_sid=127cfc&_nc_ohc=zsbPIzz8IKcQ7kNvwGtikSm&_nc_oc=Adncuv50ywa7ySeOeBJfswzOYydzEPvNmHNXjsIojytp-n35jHkJlp4zfvlLQqS7COc&_nc_zt=23&_nc_ht=scontent.fmnl17-3.fna&_nc_gid=dWbR5xRNvLJVZh1Z4Cebyg&oh=00_AfKOhZ2k5U_9rz9nfCDxI9oz2l9R52OSTXG-n-INkfJB5g&oe=683DA02F',
                'summary': 'As the curtain falls on this crucial moment in the Guild’s journey, we thank you for making your mark. Every vote cast is a step toward the future we are building—together.',
                'article': created_articles[4],
                'external_url': None
            },
            {
                'title': 'UPCSG Internship Fair in Full Swing at the Lawak Sinehan!',
                'image_url': 'https://scontent.fmnl17-8.fna.fbcdn.net/v/t39.30808-6/494590394_1195214829059631_6590297913686257157_n.jpg?_nc_cat=107&ccb=1-7&_nc_sid=127cfc&_nc_ohc=FGo9xGSIaCsQ7kNvwGjITkr&_nc_oc=AdkZONB0xg6JwWSR0lqiZufAfwt1VSvrIN3u4ekDaj3KdM_bEGv_ERLf4-lVtWOLpXs&_nc_zt=23&_nc_ht=scontent.fmnl17-8.fna&_nc_gid=EdMrDkl9O4FV_yWomzhlpw&oh=00_AfLELhYF2itRni1Sr0qT5hZWrBdC_6kI7DfA7gndLmiz4Q&oe=683DB01A',
                'summary': 'The UPCSG Internship Fair 2025 brought together five incredible companies and the next generation of innovators under one roof. From exploring internship opportunities to making real industry connections, our Guilders took one step closer to their tech careers.',
                'article': None,
                'external_url': 'https://www.facebook.com/share/p/193Xtt9gj3/'
            },
            {
                'title': 'Call to Join Public Forum of UPC Chancellor Selection 2025',
                'image_url': 'https://scontent.fmnl17-6.fna.fbcdn.net/v/t39.30808-6/483989325_1157175549530226_4369375787540854512_n.jpg?_nc_cat=109&ccb=1-7&_nc_sid=a5f93a&_nc_ohc=fnBth93hvgUQ7kNvwHSI0Y4&_nc_oc=AdkOYyxiJnrlyTG_j3SVTXdFdUBHqjIEW_RYZ_7dphq_r6d6D2fxbj0Wt2CJ2hr0mss&_nc_zt=23&_nc_ht=scontent.fmnl17-6.fna&_nc_gid=RTS_vTfB0q53CtBQRZ4zxA&oh=00_AfLPrlyXY6e6S5yuQr5wdKa0XUS-QcTyGqPsnGjeWQmAFw&oe=683DBE58',
                'summary': 'UP Cebu University Student Council calls on the UP Cebu community to take part in shaping our university’s future. The selection of our next Chancellor is a crucial process that will define the leadership and direction of UP Cebu. As students and organizations, our voices matter in ensuring a fair, transparent, and inclusive selection.',
                'article': None,
                'external_url': "https://www.facebook.com/photo/?fbid=1157175546196893&set=a.565851075329346"
            },
            {
                'title': '🏆 𝗞𝗢𝗠𝗦𝗔𝗜 𝗖𝗨𝗣 𝟮𝟬𝟮𝟱 – 𝗙𝗜𝗡𝗔𝗟 𝗢𝗩𝗘𝗥𝗔𝗟𝗟 𝗦𝗧𝗔𝗡𝗗𝗜𝗡𝗚𝗦 🏆',
                'image_url': 'https://scontent.fmnl17-5.fna.fbcdn.net/v/t39.30808-6/482321286_1154964863084628_317895712845455391_n.jpg?_nc_cat=110&ccb=1-7&_nc_sid=127cfc&_nc_ohc=jXYjQ8iY4e0Q7kNvwES6gJD&_nc_oc=AdlaUn2R_OlMXhDhZyi0oN7PSR9fsSrdcwgQslQs2vHRjN_eJoe0WBpXwJobcZqByJk&_nc_zt=23&_nc_ht=scontent.fmnl17-5.fna&_nc_gid=WVrkbfLy84PI-nVRwiOroA&oh=00_AfIiQ50mxFOj4Thfnl-bQru5kJ6pQjQs_1dPSB1-kuMT7A&oe=683DAF06',
                'summary': 'After days of intense battles, strategic plays, and unwavering house spirit, Komsai Cup 2025 has officially come to an end!',
                'article': None,
                'external_url': 'https://www.facebook.com/photo/?fbid=1154977373083377&set=a.565851071996013'
            },
            {
                'title': 'HAPPENING NOW: MX. Komsai 2025',
                'image_url': 'https://scontent.fmnl17-1.fna.fbcdn.net/v/t39.30808-6/481900158_1152387173342397_7391132821415880828_n.jpg?_nc_cat=100&ccb=1-7&_nc_sid=127cfc&_nc_ohc=053pRvB2_NMQ7kNvwEuigr4&_nc_oc=AdmT-Rb2lf8VzdTkioma1MelGDVt6SnwJsyOLThf4K1nk-PEwZduHF64wI5DA9o63Lg&_nc_zt=23&_nc_ht=scontent.fmnl17-1.fna&_nc_gid=vQX2ARARu1Wl66pAW0T4uw&oh=00_AfITk0ZkEtkwLkbAZlzLXKB5UGFxEJ3U3jaE_D6QR61TPw&oe=683D9468',
                'summary': 'In this clockwork design, who will 𝙧𝙚𝙞𝙜𝙣 when the gears of destiny align?',
                'article': None,
                'external_url': None
            },
        ]

        for data in announcement_data:
            announcement, created = Announcement.objects.get_or_create(
                title=data['title'],
                defaults={
                    'image_url': data['image_url'],
                    'summary': data['summary'],
                    'article': data['article'],
                    'external_url': data['external_url']
                }
            )
            msg = f'Created announcement: {data["title"]}' if created else f'Announcement already exists: {data["title"]}'
            self.stdout.write(self.style.SUCCESS(msg) if created else self.style.WARNING(msg))

        self.stdout.write(self.style.SUCCESS('Successfully populated all content data!'))
