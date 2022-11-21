init python:
    reyl = NPC("Reyl", {"hp": 150, "atk": 100, "def": 100}, True, "atk", [5, 15, 25, 50, 75])       
    mom = NPC("Mom", {"hp": 100, "atk": 175, "def": 150}, False, "hp", [15, 25, 50, 75, 100])



# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define pov = Character("[povname]")

define m = Character("Mom")

define anon = Character("???")

define r = Character("Reyl")


# The game starts here.
screen map:
    textbutton "Map" xalign .95 yalign 0 action Jump("map_screen")
screen inv:
    textbutton "Bag" xalign .90 yalign 0 action Jump("inv_screen")
screen tele:
    textbutton "Telegraph" xalign .85 yalign 0 action Jump("tele_screen")



# Scene 1 - Intro
label intro:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room
    $ initname = ""
    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    "Zarik's conquests in Solton and Nyqual made him a living legend in Thal. He quickly rose to the rank of General, and commanded the army of Pangual, his home province. Though Zarik's conquests didn't stop on the battlefield."
    "In the year 143 of the Thalan calendar, Zarik ursurped Dyton as Emperor of Thal. His charisma had garnered him the support of the entire army, so his rise to power was met with little resistance. Indeed, even the Thalan people loved Emperor Zarik"
    "This love, however, is now nothing more than a fleeting memory."


label character_info:
    scene bg character creation
    python:
        povname = renpy.input("What is your name?", length=32)
        povname = povname.strip()
    
    menu:
        "What is your gender?"

        "Male":
            $ povgender = "Male"
        "Female":
            $ povgender = "Female"
        "Non-Binary":
            $ povgender = "Non-Binary"
        "Other":
            $ povgender = "Other"

    python:
        if not povname:
            if povgender == "Male":
                povname = "Threcius"
            elif povgender == "Female":
                povname = "Patrella"
            elif povgender == "Non-Binary":
                povname = "Ledoucious"
            else:
                povname = "Othrecious"
    menu:
        "Your name is [povname], correct?"

        "Yes":
            if povname == initname:
                "You said that wasn't your name... but whatever."
                "Anyways... let's begin."
            else:
                "Splendid! Let's begin."

        "No":
            "My apologies..."
            "Please re-enter your information."
            $ initname = povname
            jump character_info

    "You wake up suddenly, immediately noticed you have a throbbing headache."
    "No, this is not some foreshadowing to a secret power which lay dormant within you, you are hungover after drinking all night at the local bar."
    "By yourself, of course."
    pov "Hey!"
    "Woah, woah, calm down, it's not because you don't have any friends, it's just that they couldn't make it."
    "Anyway, you get out of bed and walk out of your room to see your mom cooking breakfast."
label begin:
    scene bg diningroom
    show mom happy

    m "Oh, you're finally awake, good morning sleepy head."
    pov "Good morning mom."
    show mom wondering
    m "You were out late last night, special occassion?"
    pov "No, nothing of the sort."
    show mom grinning
    m "Just needed to take the edge off?"
    pov "Yeah."
    show mom wave
    m "Well eat up, I gotta head to work, I'll see you later."
    pov "See ya mom."
   
    scene bg bedroom

    "You head back to your room to get changed for work, however you notice a note on your window sill."
    menu:
        "Do you wish to read the note"

        "Yes":
            "You decide to read the note."
        "No":
            menu:
                "Are you sure you don't want to read the note?"

                "Yes, I'm sure.":
                    menu:
                        "But it's vital to the plot, you can't continue without it."

                        "I'm not reading it!":
                            "If this is your wish, then I must comply. To the journey that could have been, farewell [povname]..." 
                            return
                        "Fine, I'll read it!":
                            "Wonderful! I knew you'd come around!"
                "Actually, I changed my mind, I'll read it.":
                    "You made a wise decision, [povname]!"
    centered "Hello [povname], I've been keeping close tabs on you. I think I might have some valuable information you may be interested in. Meet me under the weeping willow at 9:30, you know the spot. Peace."
    pov "What the fuck????"
    pov "Am I being stalked?"
    pov "Also, he signed off with peace like that makes it any better."
    pov "I'm gonna go give this creep a piece of my mind."
    "You decide to go to the weeping willow to confront your stalker."

# Scene 2 - Meeting Reyl
label willow:
    scene bg willow
    "You arrive at the weeping willow and are greeted with the sight of nobody at all."
    pov "What's with this? This is the spot he told me to come to, so where the hell is he?"
    anon "Yoohoo"
    pov "Who said that?"
    anon "Up here, man."
    "You look up to see a man laying on a branch, reading a book."
    pov "Oh..."
    pov "Are you the one that wrote the letter?"
    anon "I'm your guy."
    pov "What the hell was that about? 'I've had my eye on you'? That's fucking creepy, man."
    anon "Relax dude, it's not like that."
    "The man jumps down from the branch."
    show reyl
    pov "Then what the hell is it like?"
    show reyl explain
    anon "Ugh... fine, yes, I've been watching you, but only for, like, five days maybe?"
    pov "FIVE DAYS???"
    anon "Yeah, I had to be sure you were the right guy."
    pov "Right guy?"
    anon "Yea, I'll have to explain, but the fact you knew what weeping willow means I was right!"
    pov "Wait... what do you mean?"
    anon "You found me here, I never told you which weeping willow it was."
    pov "Oh... I guess I just found my way here instinctively."
    show reyl grinning
    anon "See, instincts man, you got em!"
    pov "You think so... wait, no, who the hell are you?"
    show reyl sorry
    anon "Oops, my bad, I guess I never introduced myself ♥"
    show reyl introduce
    r "The name's Reyl, it's a pleasure to finally meet you."
    pov "Finally?"
    show reyl explain
    r "I've heard so much about you from your uncle."
    show reyl
    pov "You know my uncle?"
    show reyl explain
    r "Yeah me and Teach go way back. Hes taught me everything I've ever known."
    show reyl
    pov "Really?"
    show reyl explain
    r "Oh fuck yea, he's helped me a lot through the years, well anyway, he wanted me to find you."
    show reyl
    pov "What for? Will I get to see him, I haven't seen him in ages."
    show reyl sorry
    r "About that..."
    show reyl serious
    r "He was made prisoner by the Emperor."
    pov "What the hell does the Emperor want with my uncle?"
    show reyl sorry
    r "About that also..."
    show reyl serious
    r "The Emperor is your uncle's brother... and well you can put two and two together..."
    pov "Wait..."
    show reyl tilt
    r "Hm?"
    pov "My dad is the Emperor???"
    show reyl yup
    r "Mhm."
    pov "There's no fucking way..."
    show reyl handing
    r "Well, I figured you'd say that, and so did your uncle, take this."
    "Reyl hands you a note written in your uncle's handwriting."
    scene bg letter
    centered "[povname], I'm sorry for not telling you sooner, perhaps it wouldn't have turned out like this. What Reyl tells you is true, your father is Emperor Zarik. He left your mother before he ever knew she was pregnant. In between the time he left and you were born, he became Emperor. I was still in contact with your mother, and after seeing what horrible things he was doing, I had her flee to an isolated location. He only just recently somehow found out he had a son. If you are reading this now, it means your father has imprisoned me. I assume he plans to torture me to find out where you are. I do not plan on telling them, but please, take your mother and run. As far away as possible. I'm sorry [povname], I've always loved you as a son, if only we were dealt a better fate."
    scene bg willow
    show reyl waiting
    "You drop to your knees."
    show reyl instructing
    r "Welp, you heard... no read... the man. Go get your mom and run."
    pov "I can't..."
    show reyl angry
    r "Don't be such a fucking pussy man, I mean, how are you gonna be such a pussy you can't even do the pussiest thing a man could do when faced with hardship?"
    pov "No..."
    show reyl confused
    r "Hm?"
    pov "I can't leave him behind..."
    r "Who? A friend?"
    pov "No dipshit."
    "You rise to your feet."
    show reyl shocked
    pov "Theres no way in hell I'm gonna run away and leave my uncle behind."
    show reyl confused
    r "Oh?"
    r "Well this is most unexpected..."
    show reyl grinning
    r "But not really though ♥. I was expecting this outcome all along."
    pov "But..."
    show reyl explain
    r "Hey man, that letter is just what your uncle wants you to do. I knew any sensible man wouldn't leave his family behind."
    show reyl grinning
    r "Well, some of the stuff I've seen you do isn't so sensible. Going telegram club to talk to women... pathetic."
    pov "How the hell did you know that?"
    show reyl mischievous
    r "I've kept my eye on you, remember?"
    pov "Right... creep."
    show reyl
    r "We can settle that later, right now we need to get your mom to a safe location."
    pov "Right... just because I'm not running doesn't mean she has to stay with me."
    show reyl hurry
    r "Exactly, let's go!" 

    $ reyl.relationship_up(2)

# Scene 3 - Meeting Mom
label mom_work:
    scene bg diner
    "You arrive at your mom's work and bust through the door."
    pov "MOM!"
    "There are some murmers among the patrons."
    "Your mom, who just finished serving a table, walks over to you."
    show mom confused
    m "What is it sweety?"
    pov "You gotta get out of here... the Emperor, no, dad, has imprisoned Uncle Ethryl."
    show mom wonder
    m "Is that so..."
    pov "Is that all you have to say? He's gonna come for you next probably."
    show mom explain
    m "Ethryl and me knew this day was coming sooner or later. Sorry if I don't seem very surprised."
    pov "So if youn know already, get as far away as possible. Please mom... I can't lose you."
    show mom disagree
    m "Oh sweety... I'm sorry, I can't do that."
    pov "Why the hell not? Are you just gonna give up and let him take you?"
    show mom explain
    m "No, not at all."
    pov "Then???"
    m "Well... you're probably gonna go and try to save him right?"
    pov "Yeah..."
    show mom thinking
    m "Well, I know you... You're too, how do I say this nicely..."
    show mom grinning
    m "Weak?"
    pov "..."
    show mom laugh
    m "So I can't just let you go by yourself."
    pov "But I have Reyl! I'll be fine!"
    show reyl at left with moveinleft
    show mom confused at right with move
    r "Yo!"
    m "Who's this sweety?"
    r "The name's Reyl, pleasure to finally meet you. I've heard so much about you from Ethryl, and I must say, you look ever better in person."
    show mom blush
    m "Oh... why thank you"
    pov "HEY!!"
    r "Oh, sorry... Yeah I know this kid's uncle. He took me in a while back."
    m "You trust him, [povname]?"
    pov "I don't even know to be honest with you... I can't explain it, but part of me knows what Reyl says is true."
    show reyl happy
    r "I told you ya had instincts ♥"
    show mom thinking
    m "I see..."
    show mom confident
    m "Then I will trust him as well, well I've actually heard about him from Ethryl a few times..."
    pov "Really???"
    show mom
    m "I've never met the man though."
    show reyl grinning
    r "It's true, I would've known if I met a beauty like you before."
    show mom blush
    m "Oh stop it."
    pov "Thats my mom, man..."
    show reyl sorry
    r "Oh, right, sorry..."
    show reyl thinking
    r "Anyway... what were you planning on doing then?"
    show mom confident
    m "Well, joining you guys of course!"
    show reyl shocked
    pov "WHAT?"
    show mom explain
    m "Oh I guess I never told you, but I met your father in the army..."
    show mom proud
    m "I'm quite the skilled fighter if I do say so myself."
    show reyl hearts
    pov "You've kept a lot from me..."
    show mom sorry
    m "Sorry ♥"
    pov "Forget it..."
    show mom grinning
    show reyl thinking
    r "Well, we have a merry band of three then... we just need to figure out where your uncle is being held."
    show manager
    show mom surprised
    show reyl surprised
    "Manager" "Do you people mind? You are disrupting my business. Also, Sherthy get back to work."
    show mom sorry
    m "Oh, sorry Borj... I think I'm gonna need some time off though."
    "Manager" "I won't allow it, get back out there and--"
    show mom wave
    m "Goodbye Borj ♥"
    "The three of you head back to your house to gather some supplies."

# Scene 4 - Gather Supplies at Home
label house:
    scene bg diningroom
    show mom at right
    show reyl at left
    "You arrive back at your house with your mom and Reyl."
    pov "Here we are."
    show mom happy
    m "Make yourself at home Reyl ♥"
    show reyl hearts
    r "Why thank you ♥. I'm sure we won't be long though."
    "You pinch yourself to make sure what you're witinessing isn't some sort of nightmare."
    show reyl happy
    pov "Anyway... I'll grab some stuff from my room to take."
    m "I'll grab some food for us to eat along the way, it won't be much though..."
    r "We're gonna need it... I'm not sure trains would be safe, army probably has a close eye on them. We're gonna need to travel by foot most likely."
    pov "I'm sure that won't be an issue."
    show mom worried
    m "Are you sure dear? You were never the athletic type, you were wiped out after 30 minutes when we went hiking that one time."
    show reyl laugh
    pov "MOM!!!"
    show mom laugh
    r "I'll carry you if you need ♥"
    pov "Shut up."
    show mom
    show reyl
    pov "Anyways... I'll be right back."
    scene bg bedroom
    "You look around your room for anything that might be of use."
    "You found a {color=#0000ffff}map{/color}, {color=#0000ffff}portable telegraph{/color}, and a {color=#0000ffff}backpack{/color}."
    pov "These should come in handy."
    "You can access the map by pressing this button."
    show screen map
    "You can access your bag by pressing this button."
    show screen inv
    "You can access the portable telegraph by pressing this button."
    show screen tele
    "..."
    "..."
    "..."
    "Ahem."
    pov "What?"
    "I believe you owe me a 'Thank you'?"
    pov "Oh... thanks man."
    "Yeah whatever..."
    "Moving on, you meet back up with your mom and Reyl out in the dining room."
    scene bg diningroom
    show reyl at left
    show mom at right
    r "Who were you talking to in there?"
    pov "Um..."
    "None of your business man."
    show reyl dejected
    r "Jeez..."
    show reyl
    m "Find anything sweety?"
    pov "Yeah, I got a few things."
    "You show them what you gathered."
    show reyl excited
    r "Oh sweet is that one of those fancy portable telegraphs?"
    pov "Yeah, pretty cool huh?"
    m "I got it for him for his birthday this year."
    show reyl hearts
    pov "This map should be useful too, maps out the entire country."
    show reyl
    r "Damn! We're far as fuck from the capital."
    m "I'm sure we'll make it in no time at all!"
    r "Well, better get started then. Anything else you guys are missing?"
    m "I think I'm all set what about you dear?"
    pov "I'm good as well I think."
    r "Well in that case..."
    show reyl grinning
    r "Let's get this show on the road."
    show mom unamused
    m "..."
    pov "..."
    show reyl nervous
    "..."
    show reyl annoyed
    r "You too?"
    "I didn't want to break the silence."
    r "Whatever."
    show mom
    show reyl
    m "Shall we then?"
    "You nod."
    hide reyl
    hide mom
    "The three of you start on your journey, blissfully unaware of what is in store for you in the coming weeks."
    r "Spoiler alert!"
    "Ugh..."

# Scene 5 - Small talk on your trip
label journey_start:
    scene bg village outskirts
    show reyl
    r "Man oh man... I'm starving."
    pov "We left an hour ago."
    r "And I didn't have any breakfast!"
    pov "Should've ate while you waited for me at the tree."
    r "Hindenburg's 20/20 I guess."
    show reyl at left with move
    show mom at right with moveinright
    m "I believe the saying in hindsight's 20/20."
    show reyl embarassed
    r "Oh right..."
    pov "Who the hell is Hindenburg?"
    r "Oh I guess you wouldn't know that."
    show mom confused
    pov "What?"
    r "Forget it."
    show reyl nervous
    pov "Okay..."
    hide reyl
    show mom centered with move
    m "(What a strange man.)"
    pov "(Yeah but if Uncle Ethryl trusts him...)"
    m "(He seems trustworthy enough... just very weird.)"
    m "(He does know how to compliment a lady though.)"
    show mom blush
    pov "(Really!?)"
    show mom grinning
    show mom right with move
    show reyl confused
    r "What are you guys talking about?"
    show giggling
    m "Oh nothing!"

# Scene 6 - Meeting Valoria
define v = Character("Valoria")
label meet_valoria:
    scene bg night forest

    "Before you know it, the sky became blanketed in only the darkness of the night."
    "The three of you had been walking for hours, and you decided to set up camp just outside the forest."
    "It's quiet. The world feels still. Everyone is asleep, except for you."
    "You're tired, but there's too much on your mom. You met a guy who apparently is great friends with your uncle."
    "Then you find out, from this same guy, that your uncle was kidnapped... by your father... who is also the Emperor."
    "And to make matters worse, your mom decided to join you."
    "It's almost too much to process."
    pov "(If I close my eyes a bit longer, maybe then I can sleep. I'll save the worrying for the morning... no, I don't have time to worry.)"
    "You get comfortable and begin the fall into a deep slumber..."
    "{i}CRACK!{/i}"
    "Or not."
    pov "What the hell was that?"
    "You jolt awake and sit upward."
    pov "(I should keep my voice down... it sounded like a branch.)"
    pov "(Probably just an animal.)"
    pov "(Yeah... it's probably like a raccon, or a bear, or something...)"
    "You freeze up."
    pov "(What if it is a bear!?)"
    pov "(Nah... it's probably fine.)"
    "You stop worrying and try to lie back down... but before you get the chance you feel a hand around your mouth."
    pov "Mmph!?"
    anon "God, do you ever shut up?"
    pov "MMMMHPH!!!!"
    "You struggle against your attacker. You get a glance behind them and you make out the outline of two others."
    "It seems like they brought friends."
    "Your struggling wakes up your mom."
    show mom worried
    m "What the hell is going on?"
    "She noticed you being restrained by the intruder and, without hesitation, jumps out of her sleeping bag."
    "Reyl, however, is sleeping soundly on the ground behind her."
    show mom angry
    m "Wake the fuck up!"
    "She kicks him."
    show reyl tired at left with moveinleft
    show mom at right with move
    r "Huh, wuzzat? Is it the end of the world?"
    m "It's about to be if you don't help me deal with these punks."
    show reyl surprised
    r "Oh shit!"
    "The two of them jump on top of the intruders."
    hide reyl
    hide mom
    # play scuffle sound effect
    # dust cloud animation
    r "TAKE THAT YOU HAG!"
    m "NEVER TOUCH MY HONEYBUN AGAIN BITCH!"
    anon "WHAHAAAAAAAAAAAAAAAAAAAAAAAA!"
    "The scuffle carries on for several more seconds before the three intruders end up in a pile."
    show mom exhausted at right
    show reyl exhausted at left
    m "Whew! Thank god that's over. If it weren't for your super hot mom you'd be toast!"
    pov "..."
    pov "Just what I wanted to hear, thanks mom!"
    show mom grinning
    m "I'm just glad you're ok!"
    pov "Yeah I'm fine, doesn't look like they are though."
    "Two of them are unconscious, but one of them is stirring awake--!"
    # kick sound effect
    show reyl mad
    anon "ARGH!"
    r "Get back to your loser pile, loser!"
    anon "Who are you calling a loser?"
    "{i}SMACK!{/i}"
    r "OHHHH..."
    show reyl knocked out
    "Reyl falls into the loser pile, taking the loser's place."
    hide reyl
    pov "What's your problem man?"
    show valoria masked angry
    hide mom
    anon "Funny you should ask."
    show valoria masked evil grinning
    "In an instant, the attacker manages to draw a knife on you and your mom." 
    "Amazing, considering the three of you delivered just moments ago."
    anon "You're my problem!"
    "Oh snap! She went there!"
    "Unfortunately for you however, you're all worn out from the previous scuffle, and with Reyl knocked out and your mom gone..."
    "Wait..."
    "WHERE'S YOUR MOTHER BOY?"
    pov "HOW THE HELL SHOULD I KNOW!?"
    "{i}CLANG!{/i}"
    show valoria masked knocked out
    anon "Ohhh hoh... my cranium..."
    "Your attacker falls to the ground, revealing your mom standing behind them with a frying pan in hand."
    show mom at right
    pov "Damn mom!"
    m "I hope I didn't hit them too hard..."
    m "Anyway... bandits and assassins aren't what they used to be {i}sigh{/i}."
    pov "Well, let's see who this bandit is."
    "You take off their mask, and..."
    "It's a stunning beauty!"
    show valoria
    show reyl intrigued at left with moveinleft
    show mom grinning
    r "Oh what do we have here..."
    r "You're quite the looker..."
    show reyl grinning
    r "Why don't you tell us your name?"
    anon "..."
    show reyl annoyed
    r "Yo! Tell us your name!"
    anon "..."
    show reyl angry
    pov "Bro..."
    pov "You suck at interrogation."
    show reyl dejected
    r "Yeah I know."
    m "I'm not sure we'll get much out of her... keep an eye on her for a bit, won't you sweety?"
    pov "Yeah alright..."
    "Reyl and your mom retreat back towards their sleeping bags."
    hide reyl
    hide mom
    "It's just the two of you. The other two intruders don't seem to be waking up anytime soon."
    "You still can't help but feeling like you recognize this person."
    pov "Err..."
    pov "You don't have to tell us your name, but... maybe don't attack us like that next time."
    show valoria blush
    anon "..."
    pov "Well alright, I'll just sit--"
    v "It's Valoria..."
    pov "Huh?"
    v "Valoria, that's my name."
    pov "Oh, my name's--"
    v "I know who you are, [povname]."
    show valoria smirk
    pov "(How does everyone know my name before I know them!?)"
    pov "How do you..."
    v "We used to play together all the time as kids."
    show valoria disappointed
    v "I guess you forgot though..."
    pov "I'm sorry..."
    pov "I don't remember a lot, in fact, I don't even remember what happened yesterday."
    show valoria sad
    v "Don't sweat it."
    pov "Alright..."
    pov "But still, if you knew me, why did you guys attack us?"
    show valoria confused
    v "You guys?"
    v "I'm by myself..."
    pov "Then who are those guys?"
    v "I have no idea..."
    show valoria embarassed
    v "But to answer your question, I didn't know it was you... sorry."
    v "It's my first time doing this actually..."
    v "I didn't want to, it's just..."
    show valoria crying
    pov "It's ok... you don't have to answer."
    pov "I'll be right back."
    "You go over to the stew sitting over the fire and grab a bowl for Valoria."
    pov "Here you go, you're probably hungry."
    show valoria smiling
    v "Like you wouldn't believe..."
    "Valoria takes her time eating the food. It seems like she hasn't eaten in a while, but you don't want to ask her too many questions."
    pov "Is it any good?"
    show valoria happy
    v "It's amazing."
    pov "Yep... mom always makes good food, even if we're in the middle of nowhere."
    show valoria laughing
    v "She always made the best snacks."
    pov "Yeah... she still does too."
    show valoria sad
    v "You really don't remember me then?"
    pov "No, I don't..."
    v "It's ok... we had to move away when we were still young, it's not your fault."
    menu:
        "Valoria looks pretty upset, what will you do?"

        "Ask her what happened":
            jump valoria_backstory
        "Give her some space":
            jump give_space

            