import tkinter as tk
from tkinter import ttk, messagebox, font
import random
import time

class PositiveThoughtsApp:
    def __init__(self, root):
        self.root = root
        self.root.title("MindBoost - Positive Affirmations")
        self.root.geometry("800x500")
        self.root.minsize(700, 450)
        self.root.configure(bg='#2A2A2A')
        
        # Custom color scheme
        self.colors = {
            'background': '#2A2A2A',
            'primary': '#4A90E2',
            'secondary': '#6C5CE7',
            'accent': '#FF6B6B',
            'text': '#FFFFFF',
            'card_bg': '#363636'
        }
        
        # Configure styles
        self.configure_styles()
        
        # Initialize thoughts database
        self.thoughts = self.create_thoughts_list()
        
        # Create GUI elements
        self.create_widgets()
        
        # Schedule first thought update
        self.update_thought()
        
        # Set window to stay on top
        self.root.attributes('-topmost', True)
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)

    def configure_styles(self):
        style = ttk.Style()
        style.theme_use('clam')
        
        # Configure styles
        style.configure('TFrame', background=self.colors['background'])
        style.configure('Card.TFrame', 
                       background=self.colors['card_bg'],
                       borderwidth=2,
                       relief='raised',
                       bordercolor='#404040')
        style.configure('Primary.TButton',
                       font=('Segoe UI', 12, 'bold'),
                       background=self.colors['primary'],
                       foreground=self.colors['text'],
                       borderwidth=0,
                       padding=10)
        style.map('Primary.TButton',
                 background=[('active', self.colors['secondary']),
                             ('pressed', self.colors['accent'])])
        style.configure('Quote.TLabel',
                        font=('Segoe UI', 14, 'italic'),
                        background=self.colors['card_bg'],
                        foreground=self.colors['text'],
                        wraplength=650,
                        padding=20)
        style.configure('Header.TLabel',
                       font=('Segoe UI', 24, 'bold'),
                       background=self.colors['background'],
                       foreground=self.colors['primary'])
        style.configure('Secondary.TLabel',
                       font=('Segoe UI', 10),
                       background=self.colors['background'],
                       foreground='#AAAAAA')

    def create_thoughts_list(self):
        return [
            "You are capable of amazing things.",
            "Every challenge is an opportunity for growth.",
            "Your potential is limitless.",
            "Today is filled with endless possibilities.",
            "You radiate positive energy and confidence.",
            "Small progress is still progress. Celebrate it!",
            "We cannot solve problems with the kind of thinking we employed when we came up with them. —Albert Einstein",
            "Learn as if you will live forever, live like you will die tomorrow. —Mahatma Gandhi",
"Stay away from those people who try to disparage your ambitions. Small minds will always do that, but great minds will give you a feeling that you can become great too. —Mark Twain",
"When you give joy to other people, you get more joy in return. You should give a good thought to the happiness that you can give out. —Eleanor Roosevelt",
"When you change your thoughts, remember to also change your world. —Norman Vincent Peale",
"It is only when we take chances that our lives improve. The initial and the most difficult risk we need to take is to become honest. —Walter Anderson",
"Nature has given us all the pieces required to achieve exceptional wellness and health, but has left it to us to put these pieces together. —Diane McLaren",
"Success is not final; failure is not fatal: It is the courage to continue that count. —Winston Churchill",
"It is better to fail in originality than to succeed in imitation. —Herman Melville",
"The road to success and the road to failure are almost exactly the same. —Colin R. Davis",
"Success usually comes to those who are too busy to be looking for it. —Henry David Thoreau",
"Develop success from failures. Discouragement and failure are two of the surest stepping stones to success. —Dale Carnegie",
"Nothing in the world can take the place of persistence. Talent will not; nothing is more common than unsuccessful men with talent. Genius will not; unrewarded genius is almost a proverb. Education will not; the world is full of educated derelicts. The slogan ‘Press On’ has solved and always will solve the problems of the human race. —Calvin Coolidge",
"There are three ways to ultimate success: The first way is to be kind. The second way is to be kind. The third way is to be kind. —Mister Rogers",
"Success is peace of mind, which is a direct result of self-satisfaction in knowing you made the effort to become the best of which you are capable. —John Wooden",
"I never dreamed about success. I worked for it. —Estée Lauder",
"Success is getting what you want; happiness is wanting what you get.―W. P. Kinsella",
"The pessimist sees difficulty in every opportunity. The optimist sees opportunity in every difficulty. —Winston Churchill",
"Don’t let yesterday take up too much of today. —Will Rogers",
"You learn more from failure than from success. Don’t let it stop you. Failure builds character. —Unknown",
"If you are working on something that you really care about, you don’t have to be pushed. The vision pulls you. —Steve Jobs",
"Experience is a hard teacher because she gives the test first, the lesson afterward. ―Vernon Sanders Law",
"To know how much there is to know is the beginning of learning to live. —Dorothy West",
"Goal setting is the secret to a compelling future. —Tony Robbins",
"Concentrate all your thoughts upon the work in hand. The sun’s rays do not burn until brought to a focus. —Alexander Graham Bell",
"Either you run the day or the day runs you. —Jim Rohn",
"I’m a great believer in luck, and I find the harder I work, the more I have of it. —Thomas Jefferson",
"When we strive to become better than we are, everything around us becomes better too. —Paulo Coelho",
"Opportunity is missed by most people because it is dressed in overalls and looks like work. —Thomas Edison",
"Setting goals is the first step in turning the invisible into the visible. —Tony Robbins",
"Your work is going to fill a large part of your life, and the only way to be truly satisfied is to do what you believe is great work. And the only way to do great work is to love what you do. If you haven’t found it yet, keep looking. Don’t settle. As with all matters of the heart, you’ll know when you find it. —Steve Jobs",
"Women challenge the status quo because we are never it. —Cindy Gallop",
"We don’t just sit around and wait for other people. We just make, and we do. —Arlan Hamilton",
"Think like a queen. A queen is not afraid to fail. Failure is another stepping stone to greatness. —Oprah Winfrey",
"The strongest actions for a woman is to love herself, be herself and shine amongst those who never believed she could. —Unknown",
"Whenever you see a successful woman, look out for three men who are going out of their way to try to block her. —Yulia Tymoshenko",
"Some women choose to follow men, and some choose to follow their dreams. If you’re wondering which way to go, remember that your career will never wake up and tell you that it doesn’t love you anymore. —Lady Gaga",
"The thing women have yet to learn is nobody gives you power. You just take it. ― Roseanne Barr",
"No woman wants to be in submission to a man who isn’t in submission to God! ―T. D. Jakes",
"A witty woman is a treasure; a witty beauty is a power. ― George Meredith",
"When a woman becomes her own best friend, life is easier. —Diane Von Furstenberg",
"If you want something said, ask a man; if you want something done, ask a woman. —Margaret Thatcher",
"We need women at all levels, including the top, to change the dynamic, reshape the conversation, to make sure women’s voices are heard and heeded, not overlooked and ignored. —Sheryl Sandberg",
"It took me quite a long time to develop a voice, and now that I have it, I am not going to be silent. —Madeleine Albright",
"Women must learn to play the game as men do. —Eleanor Roosevelt",
"I swear, by my life and my love of it, that I will never live for the sake of another man, nor ask another man to live for mine. —Ayn Rand",
"He who conquers himself is the mightiest warrior. —Confucius",
"Try not to become a man of success, but rather become a man of value. —Albert Einstein",
"One man with courage makes a majority. —Andrew Jackson",
"One secret of success in life is for a man to be ready for his opportunity when it comes. —Benjamin Disraeli",
"A man who has committed a mistake and doesn’t correct it is committing another mistake. —Confucius Kongzi",
"The successful man will profit from his mistakes and try again in a different way. —Dale Carnegie",
"A successful man is one who can lay a firm foundation with the bricks others have thrown at him. —David Brinkley",
"He is a wise man who does not grieve for the things which he has not, but rejoices for those which he has. —Epictetus",
"You’ve got to get up every morning with determination if you’re going to go to bed with satisfaction. —George Lorimer",
"Education is the most powerful weapon which you can use to change the world. —Nelson Mandelav",
"The most difficult thing is the decision to act; the rest is merely tenacity. —Amelia Earhart",
"You’ll find that education is just about the only thing lying around loose in this world, and it’s about the only thing a fellow can have as much of as he’s willing to haul away. —John Graham",
"Take the attitude of a student, never be too big to ask questions, never know too much to learn something new. —Augustine Og Mandino",
"It is remarkable how much long-term advantage people like us have gotten by trying to be consistently not stupid, instead of trying to be very intelligent. —Charlie Munger",
"You can’t be that kid standing at the top of the waterslide, overthinking it. You have to go down the chute. —Tina Fey",
"When I believe in something, I’m like a dog with a bone. —Melissa McCarthy",
"And the day came when the risk to remain tight in a bud was more painful than the risk it took to blossom. —Anaïs Nin",
"The standard you walk past is the standard you accept. —David Hurley",
"I’ve searched all the parks in all the cities and found no statues of committees. —Gilbert K. Chesterton",
"Success is stumbling from failure to failure with no loss of enthusiasm. ―Winston Churchill",
"Keep your eyes on the stars, and your feet on the ground. ―Theodore Roosevelt",
"Do not stop thinking of life as an adventure. You have no security unless you can live bravely, excitingly, imaginatively; unless you can choose a challenge instead of competence. ―Eleanor Roosevelt",
"Perfection is not attainable. But if we chase perfection we can catch excellence. —Vince Lombardi",
"Get a good idea and stay with it. Dog it, and work at it until it’s done right. —Walt Disney",
"Optimism is the faith that leads to achievement. Nothing can be done without hope and confidence. —Helen Keller",
"The elevator to success is out of order. You’ll have to use the stairs, one step at a time. —Joe Girard",
"Be a positive energy trampoline—absorb what you need and rebound more back. —Dave Carolan",
"People often say that motivation doesn’t last. Well, neither does bathing—that’s why we recommend it daily. —Zig Ziglar",
"Work until your bank account looks like a phone number. —Unknown",
"I am so clever that sometimes I don’t understand a single word of what I am saying. —Oscar Wilde",
"People say nothing is impossible, but I do nothing every day. —Winnie the Pooh",
"Life is like a sewer … what you get out of it depends on what you put into it. —Tom Lehrer",
"I always wanted to be somebody, but now I realize I should have been more specific. —Lily Tomlin",
"Talent wins games, but teamwork and intelligence win championships. —Michael Jordan",
"Individual commitment to a group effort—that is what makes a team work, a company work, a society work, a civilization work. —Vince Lombardi",
"Teamwork is the ability to work together toward a common vision. The ability to direct individual accomplishments toward organizational objectives. It is the fuel that allows common people to attain uncommon results. —Andrew Carnegie",
"Coming together is a beginning. Keeping together is progress. Working together is a success. —Henry Ford",
"Alone we can do so little, together we can do so much. —Helen Keller",
"Remember, teamwork begins by building trust. And the only way to do that is to overcome our need for invulnerability. —Patrick Lencioni",
"I invite everyone to choose forgiveness rather than division, teamwork over personal ambition. —Jean-Francois Cope",
"Just one small positive thought in the morning can change your whole day. —Dalai Lama",
"Opportunities don’t happen, you create them. —Chris Grosser",
"Love your family, work super hard, live your passion. —Gary Vaynerchuk",
"It is never too late to be what you might have been. —George Eliot",
"Don’t let someone else’s opinion of you become your reality. —Les Brown",
"If you’re not positive energy, you’re negative energy. —Mark Cuban",
"I am not a product of my circumstances. I am a product of my decisions. —Stephen R. Covey",
"Do the best you can. No one can do more than that. ―John Wooden",
"If you can dream it, you can do it. ―Walt Disney",
"Do what you can, with what you have, where you are. ―Theodore Roosevelt",
"The greatest discovery of my generation is that a human being can alter his life by altering his attitudes. —William James",
"One of the differences between some successful and unsuccessful people is that one group is full of doers, while the other is full of wishers. —Edmond Mbiaka",
"I’d rather regret the things I’ve done than regret the things I haven’t done. —Lucille Ball",
"You cannot plow a field by turning it over in your mind. To begin, begin. ―Gordon B. Hinckley.",
"When you arise in the morning, think of what a privilege it is to be alive, to think, to enjoy, to love. —Marcus Aurelius",
"Mondays offer new beginnings 52 times a year! —David Dweck",
"Be miserable. Or motivate yourself. Whatever has to be done, it’s always your choice. —Wayne Dyer",
"Your Monday morning thoughts set the tone for your whole week. See yourself getting stronger, and living a fulfilling, happier, and healthier life. —Germany Kent",
"Friday sees more smiles than any other day of the workweek! —Kate Summers",
"Oh! It’s Friday again. Share the love that was missing during the week. In a worthy moment of peace and bliss. —S. O’ Sade",
"Every Friday, I like to high-five myself for getting through another week on little more than caffeine, willpower, and inappropriate humor. —Nanea Hoffman",
"Make a Friday a day to celebrate work well done that you can be proud of, knowing that you just didn’t put in time to the next paycheck. —Byron Pulsifer",
"When you leave work on Friday, leave work. Don’t let technology follow you throughout your weekend (answering text messages and emails). Take a break. You will be more refreshed to begin the workweek if you have had a break. —Catherine Pulsifer",
"You can get everything in life you want if you will just help enough other people get what they want. —Zig Ziglar",
"Inspiration does exist, but it must find you working. —Pablo Picasso",
"Don’t settle for average. Bring your best to the moment. Then, whether it fails or succeeds, at least you know you gave all you had. —Angela Bassett",
"Show up, show up, show up, and after a while the muse shows up, too. —Isabel Allende",
"Don’t bunt. Aim out of the ballpark. Aim for the company of immortals. ―David Ogilvy",
"I have stood on a mountain of no’s for one yes. —Barbara Elaine Smith",
"If you believe something needs to exist, if it’s something you want to use yourself, don’t let anyone ever stop you from doing it. —Tobias Lütke",
"Don’t look at your feet to see if you are doing it right. Just dance. ―Anne Lamott",
"Someone’s sitting in the shade today because someone planted a tree a long time ago. —Warren Buffet",
"True freedom is impossible without a mind made free by discipline. ―Mortimer J. Adler",
"Rivers know this: there is no hurry. We shall get there someday. ―A. A. Milne",
"There is a vitality, a life force, an energy, a quickening that is translated through you into action, and because there is only one of you in all time, this expression is unique. And if you block it, it will never exist through any other medium and will be lost. ―Martha Graham",
"Small is not just a stepping stone. Small is a great destination itself. ―Jason Fried",
"He that can have patience can have what he will. ―Benjamin Franklin",
"The only one who can tell you ‘you can’t win’ is you, and you don’t have to listen. —Jessica Ennis",
"Set your goals high, and don’t stop till you get there. —Bo Jackson",
"Take your victories, whatever they may be, cherish them, use them, but don’t settle for them. —Mia Hamm",
"Life can be much broader once you discover one simple fact: Everything around you that you call life was made up by people that were no smarter than you. And you can change it, you can influence it. … Once you learn that, you’ll never be the same again. —Steve Jobs",
"Life is like riding a bicycle. To keep your balance, you must keep moving. —Albert Einstein",
"What you do speaks so loudly that I cannot hear what you say. —Ralph Waldo Emerson",
"I have never let my schooling interfere with my education. —Mark Twain",
"If you can’t yet do great things, do small things in a great way. ―Napoleon Hill",
"If you really want to do something, you’ll find a way. If you don’t, you’ll find an excuse. ―Jim Rohn",
"Be sure you put your feet in the right place, then stand firm. ―Abraham Lincoln",
"Live out of your imagination, not your history. —Stephen Covey",
"Do not wait for the perfect time and place to enter, for you are already onstage. —Unknown",
"The greater the difficulty, the more the glory in surmounting it. ―Epicurus",
"Courage doesn’t always roar. Sometimes courage is a quiet voice at the end of the day saying, ‘I will try again tomorrow.’ —Mary Anne Radmacher",
"If the decisions you make about where you invest your blood, sweat, and tears are not consistent with the person you aspire to be, you’ll never become that person. ―Clayton M. Christensen",
"Fear of what other people will think is the single most paralyzing dynamic in business and in life. The best moment of my life was the day I realized that I no longer give a damn what anybody thinks. That’s enormously liberating and freeing, and it’s the only way to live your life and do your business —Cindy Gallop",
"The only way of discovering the limits of the possible is to venture a little way past them into the impossible. ―Arthur C. Clarke",
"Worry is a misuse of imagination. —Unknown",
"Courage is the most important of all the virtues because, without courage, you can’t practice any other virtue consistently. ―Maya Angelou",
"I never look back, darling. It distracts from the now. —Edna Mode",
"A year from now you will wish you had started today. —Unknown",
"The reason we struggle with insecurity is because we compare our behind the scenes with everyone else’s highlight reel. —Steve Furtick",
"Somewhere, something incredible is waiting to be known. —Carl Sagan",
"I will not lose, for even in defeat, there’s a valuable lesson learned, so it evens up for me. —Jay-Z",
"I do not try to dance better than anyone else. I only try to dance better than myself. —Arianna Huffington",
"If you don’t risk anything, you risk even more. —Erica Jong",
"Failure is simply the opportunity to begin again, this time more intelligently. —Henry Ford",
"Our greatest glory is not in never falling, but in rising every time we fall. —Confucius",
"If you change the way you look at things, the things you look at change. —Wayne Dyer",
"We must reach out our hand in friendship and dignity, both to those who would befriend us and those who would be our enemy. —Arthur Ashe",
"It’s fine to celebrate success, but it is more important to heed the lessons of failure. —Bill Gates",
"I can’t tell you how many times I’ve been given a no, only to find that a better, brighter, bigger yes was right around the corner. —Arlan Hamilton",
"We need to accept that we won’t always make the right decisions, that we’ll screw up royally sometimes—understanding that failure is not the opposite of success, it’s part of success. —Ariana Huffington",
"When everything seems to be going against you, remember that the airplane takes off against the wind, not with it. —Henry Ford",
"You cannot always control what goes on outside. But you can always control what goes on inside. —Wayne Dyer",
"We are what we repeatedly do. Excellence, then, is not an act, but a habit. —Aristotle",
"Start where you are. Use what you have. Do what you can. —Arthur Ashe",
"Hustle beats talent when talent doesn’t hustle. —Ross Simmonds",
"Everything you’ve ever wanted is sitting on the other side of fear. —George Addair",
"The question isn’t who is going to let me; it’s who is going to stop me. —Ayn Rand",
"Every strike brings me closer to the next home run. —Babe Ruth",
"I have not failed. I’ve just found 10,000 ways that won’t work. —Thomas Edisonv",
"Don’t worry about failure; you only have to be right once. —Drew Houston",
"You carry the passport to your own happiness. —Diane Von Furstenberg",
"Never let success get to your head, and never let failure get to your heart. —Drake",
"Ideation without execution is delusion. —Robin Sharma",
"Make sure your worst enemy doesn’t live between your own two ears. —Laird Hamilton",
"It is a rough road that leads to the heights of greatness. —Lucius Annaeus Seneca",
"For the great doesn’t happen through impulse alone, and is a succession of little things that are brought together. —Vincent Van Gogh",
"If we take care of the moments, the years will take care of themselves. —Maria Edgeworth",
"Resilience is when you address uncertainty with flexibility. —Unknown",
"Sometimes magic is just someone spending more time on something than anyone else might reasonably expect. —Raymond Joseph Teller",
"It’s not the will to win that matters—everyone has that. It’s the will to prepare to win that matters. —Paul Bryant",
"As a single footstep will not make a path on the earth, so a single thought will not make a pathway in the mind. To make a deep physical path, we walk again and again. To make a deep mental path, we must think over and over the kind of thoughts we wish to dominate our lives. —Henry David Thoreau",
"Never give up on a dream just because of the time it will take to accomplish it. The time will pass anyway. —Earl Nightingale",
"True humility is not thinking less of yourself; it is thinking of yourself less. —Unknown",
"The two most important days in your life are the day you’re born and the day you find out why. —Mark Twain.",
"Nothing ever goes away until it teaches us what we need to know. —Pema Chodron",
"We can see through others only when we can see through ourselves. —Bruce Lee",
"First, forget inspiration. Habit is more dependable. Habit will sustain you whether you’re inspired or not. Habit will help you finish and polish your stories. Inspiration won’t. Habit is persistence in practice. ―Octavia Butler",
"The best way out is always through. ―Robert Frost",
"The battles that count aren’t the ones for gold medals. The struggles within yourself—the invisible, inevitable battles inside all of us—that’s where it’s at. —Jesse Owens",
"If there is no struggle, there is no progress. —Frederick Douglass",
"Someone will declare, ‘I am the leader!’ and expect everyone to get in line and follow him or her to the gates of heaven or hell. My experience is that it doesn’t happen that way. Others follow you based on the quality of your actions rather than the magnitude of your declarations. ―Bill Walsh",
"Courage is like a muscle. We strengthen it by use. —Ruth Gordo",
"Relentlessly prune bullshit, don’t wait to do things that matter, and savor the time you have. That’s what you do when life is short. —Paul Graham",
"More is lost by indecision than wrong decision. —Marcus Tullius Cicero",
"If the highest aim of a captain were to preserve his ship, he would keep it in port forever. —Thomas Aquinas",
"You can be the ripest, juiciest peach in the world, and there’s still going to be somebody who hates peaches. —Dita Von Teese",
"Keep a little fire burning; however small, however, hidden. ―Cormac McCarthy",
"You’ll never get bored when you try something new. There’s really no limit to what you can do. —Dr. Seuss",
"I think it’s intoxicating when somebody is so unapologetically who they are. —Don Cheadle",
"You can never leave footprints that last if you are always walking on tiptoe. —Leymah Gbowee",
"If you don’t like the road you’re walking, start paving another one. —Dolly Parton",
"If it makes you nervous, you’re doing it right. —Childish Gambino",
"What you do makes a difference, and you have to decide what kind of difference you want to make. —Jane Goodall",
"I choose to make the rest of my life the best of my life. —Louise Hay",
"In order to be irreplaceable one must always be different. —Coco Chanel",
"Anything can make me stop and look and wonder, and sometimes learn. —Kurt Vonnegut",
"People’s passion and desire for authenticity is strong. —Constance Wu",
"A surplus of effort could overcome a deficit of confidence. —Sonia Sotomayor",
"Doubt is a killer. You just have to know who you are and what you stand for. —Jennifer Lopez",
"No one changes the world who isn’t obsessed. —Billie Jean King",
"I learned a long time ago that there is something worse than missing the goal, and that’s not pulling the trigger.—Mia Hamm"
"Some people want it to happen, some wish it would happen, others make it happen. —Michael Jordan",

            # Add your 250 thoughts here
            # ... (remaining thoughts)
        ]

    def create_widgets(self):
        main_frame = ttk.Frame(self.root)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Header
        header_frame = ttk.Frame(main_frame)
        header_frame.pack(fill=tk.X, pady=(0, 20))
        
        ttk.Label(header_frame, 
                 text="🌟 MindBoost",
                 style='Header.TLabel').pack(side=tk.LEFT)
        
        self.status_label = ttk.Label(header_frame,
                                    text="Next refresh: 2:00:00",
                                    style='Secondary.TLabel')
        self.status_label.pack(side=tk.RIGHT)
        
        # Thought card
        card_frame = ttk.Frame(main_frame, style='Card.TFrame')
        card_frame.pack(fill=tk.BOTH, expand=True, pady=10)
        
        self.thought_label = ttk.Label(card_frame,
                                     style='Quote.TLabel',
                                     anchor=tk.CENTER)
        self.thought_label.pack(fill=tk.BOTH, expand=True)
        
        # Control panel
        control_frame = ttk.Frame(main_frame)
        control_frame.pack(fill=tk.X, pady=20)
        
        self.refresh_btn = ttk.Button(control_frame,
                                    text="🔄 New Thought",
                                    style='Primary.TButton',
                                    command=self.update_thought)
        self.refresh_btn.pack(side=tk.RIGHT, ipadx=20)
        
        self.time_progress = ttk.Progressbar(control_frame,
                                          orient=tk.HORIZONTAL,
                                          length=200,
                                          mode='determinate')
        self.time_progress.pack(side=tk.RIGHT, padx=20)
        
        self.time_remaining = 7200  # 2 hours in seconds
        self.update_progress()

    def update_progress(self):
        progress_value = (7200 - self.time_remaining) / 72
        self.time_progress['value'] = progress_value
        self.time_remaining -= 1
        if self.time_remaining <= 0:
            self.time_remaining = 7200
        mins, secs = divmod(self.time_remaining, 60)
        hours, mins = divmod(mins, 60)
        self.status_label.config(text=f"Next refresh: {hours:02}:{mins:02}:{secs:02}")
        self.root.after(1000, self.update_progress)

    def get_random_thought(self):
        return random.choice(self.thoughts)

    def update_thought(self):
        new_thought = self.get_random_thought()
        self.animate_thought_change(new_thought)
        self.time_remaining = 7200

    def animate_thought_change(self, new_thought):
        # Improved animation with valid color transitions
        original_bg = self.colors['card_bg']
        text_color = self.colors['text']
        
        # Fade out
        for i in range(10, 0, -1):
            blend = self.color_interpolate(text_color, original_bg, i/10)
            self.thought_label.configure(foreground=blend)
            self.root.update()
            time.sleep(0.03)
        
        self.thought_label.configure(text=new_thought)
        
        # Fade in
        for i in range(0, 11):
            blend = self.color_interpolate(original_bg, text_color, i/10)
            self.thought_label.configure(foreground=blend)
            self.root.update()
            time.sleep(0.03)
        
        self.thought_label.configure(foreground=text_color)

    def color_interpolate(self, start_hex, end_hex, factor):
        """Helper function for color transitions"""
        start = int(start_hex[1:], 16)
        end = int(end_hex[1:], 16)
        
        r = int(((start >> 16) & 0xFF) * (1 - factor) + ((end >> 16) & 0xFF) * factor)
        g = int(((start >> 8) & 0xFF) * (1 - factor) + ((end >> 8) & 0xFF) * factor)
        b = int((start & 0xFF) * (1 - factor) + (end & 0xFF) * factor)
        return f'#{r:02x}{g:02x}{b:02x}'

    def on_close(self):
        self.root.attributes('-topmost', False)
        if messagebox.askokcancel("Quit", "Do you want to close MindBoost?"):
            self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    default_font = font.nametofont("TkDefaultFont")
    default_font.configure(family="Segoe UI", size=10)
    app = PositiveThoughtsApp(root)
    root.mainloop()