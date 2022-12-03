label valoria_backstory:
    pov "Why'd you have to move away? What happened?"
    v "It's... it's super complicated, and long, and-"
    pov "Don't worry, I'll listen."
    v "..."
    v "When we were kids we used to play tag all the time."
    v "We'd run through town, not caring if we bumped into anyone or not."
    pov "..."
    pov "(This seems... familiar.)"
    show valoria laughing
    v "You could never win though, I was always able to keep from getting tagged."
    pov "I... that's not true!"
    show valoria confused
    pov "I was able to tag you once!"
    show valoria smiling
    v "You..."
    pov "I remembered, I'm sorry it took me a minute."
    show valoria happy
    v "Thank goodness..."
    pov "I- it's just been so long and, I was so devastated when you never came out to play anymore, I just didn't know what happened."
    pov "I thought I lost my friend..."
    v "I'm sorry..."
    v "We had to run... we had no other option."
    v "Ever since, it's been so hard. Now, my mom's fallen ill."
    pov "I- is she going to be alright?"
    v "Probably not, we're not wanted anywhere. Unable to get a doctor because we look different..."
    pov "That can't be right, we gotta-"
    v "It's ok, [povname]. She's with my sister up in the mountains. I want her to spend her final moments in the peace and quiet."
    pov "You should go see her, at least."
    v "No..."
    v "I want my last memories of my mom to be ones where shes been cheerful... not an empty shell on deaths door."
    v "..."
    menu:
        v "Do you think that's foolish?"

        "Yes":
            pov "... I think you should be with your mother, I think she'd want that."
            v "You're probably right..."
            v "But I'm my own person, I get to choose how I remember her."
            v "Still... am I making the right choice?"
            pov "..."
            v "I'm sorry, it's not your call to make, is it?"
            pov "No... it's fine, sorry if what I said offended you."
            show valoria laughing
            v "I learned to get some pretty thick skin so don't worry about it."


        "No":
            v "Really?"
            pov "It's your choice how you want to remember your mom... still, I know it probably pains your that you aren't there with her."
            v "It does..."
            show valoria sad
            v "My sister is furious at me, she screamed at me when I left, calling me selfish."
            pov "It may very well be a selfish thing to do... but that doesn't make it wrong."
            show valoria blush
            v "Thanks [povname]. I appreciate the honesty."
            pov "Of course, we may have been separated for all these years, but I'm here for you now."
            v "Same here..."

        show valoria
        "Valoria reaches out and touches you."
        pov "Huh?"
        show valoria mischievous
        v "You're it!"
        pov "You mother-"
        hide valoria
        "Valoria sprints away from you, you stumble as you get up but manage to stay on your feet and start chasing her."
        "The two of you play tag in the darkness until you're greeted by the morning sun."
        jump forest_morning


label give_space:
    pov "I'm sorry..."
    pov "I'll give you some space... looks like you need it."
    v "Wait-"
    pov "Hmm?"
    v "Nothing... nevermind."
    pov "Alright... I'll be right back."
    "It seems she wanted to tell you something, but you feel it's better to not ask too many questions."
    hide valoria
    "You go and warm up by the campfire for a bit."
    "After a few minutes, you go back to check on Valoria."
    "However, it seems while you were away she fell asleep."
    "You grab a blanket and cover her up, then return to your sleeping bag and turn in for the night."
    jump forest_morning
