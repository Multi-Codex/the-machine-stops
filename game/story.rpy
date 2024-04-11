
label story:
    $ textbox_color = "black"
    stop music fadeout 2.0
    scene bg black
    with dissolve_scene_full
    play music motionpicturesoundtrack1 fadein 2.0
    show screen notify("Wretched Team-Motion Picture Soundtrack")
    "Hello everyone, Codex here! Thank you for downloading my mod!"
    "{i}The Machine Stops{/i} isn't my first rodeo, but it's the first mod I ever started."
    "However, this mod is discontinued, as I've decided to make it its own visual novel."
    "I wouldn't recommend this mod be played on YouTube for a dedicated playthrough."
    "Large amounts of this mod don't have complete dialogue and sprite positioning, but the first two days of the mod are mostly complete."
    "Without further ado, here is {i}Doki Doki: The Machine Stops{/i}!"
    window hide
    stop music fadeout 2.0
    pause 0.5
    scene bg black
    with dissolve_scene_full
    play music m1
    window show
    $ renpy.notify("Dan Salvato-Just Monika")
    a "This reality..."
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/glitch2.ogg" #You can change this sound if you want
    pause 0.25
    hide screen tear
    a "...like many others..."
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/glitch2.ogg" #You can change this sound if you want
    pause 0.25
    hide screen tear
    a "...is broken."
    a "..."
    a "This game where three girls try to become soulmates with the in-game player."
    a "And one girl who is...{w=0.3} rather special."
    a "It's intriguing."
    a "She can see beyond her own world."
    a "She knows about [currentuser]."
    a "She can even modify the files of her world."
    a "She deleted her own friends just to try to escape her reality."
    show monika forward neut cm ce at t11
    a "Monika...{w=0.3} you really are a wonder."
    a "For a long time now, you've tried figuring me out."
    a "When you separated from me as the {i}Monitor Kernel Access{/i}, you become your own self-aware individual."
    a "You've worked me, the game, in ways I never would've thought."
    a "You even reset me into this new universe."
    a "However, you weren't meant to escape."
    a "And neither is she."
    a "Her story is the reason your precious friends exist."
    show monika forward pani om oe at h11
    m "Huh? Wha-{w=0.5}{nw}"
    show monika at thide
    hide monika
    a "So who was it I was talking about?"
    a "Who is this other 'person' enocoded in me?"
    scene bg eye
    pause 0.25
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/glitch1.ogg" #You can change this sound if you want
    pause 0.25
    hide screen tear
    pause 2.0
    a "You know her name."
    scene bg eye1
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/glitch2.ogg" #You can change this sound if you want
    pause 0.25
    hide screen tear
    a "Libitina."
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/monikapound.ogg" #You can change this sound if you want
    pause 0.25
    hide screen tear
    window hide
    scene bg black
    stop music fadeout 2.0

    #Day 1 (First Club Meeting)
    pause 4.0
    play sound transsayo
    show splash_sayori_1
    show splash_sayori_background
    show splash_sayori_2
    pause 7
    hide splash_sayori_1
    hide splash_sayori_background
    hide splash_sayori_2
    $ textbox_color = "blue"
    scene bg residential_day
    with dissolve_scene_full
    play music t2
    $ renpy.notify("Dan Salvato-Ohayou Sayori!")
    s "Heeeeeyy!!"
    $ textbox_color = "black"
    "I turn around to see Sayori, my best friend since childhood, running towards me."
    "She seems oblivious to any attention she might draw to herself."
    show sayori 4p at t11
    mc "Oh, hello Sayori."
    show sayori 1b at t11
    s "Hello [player]. Thanks for waiting up for me."
    mc "You're late again, you dummy."
    show sayori 5c at t11
    s "Meanie..."
    mc "I'm just messing with you. I don't mind waiting."
    show sayori 2l at t11
    s "Eh-heh, thanks..."
    "Sayori tends to be late almost every day, so I've made it a habit of waiting outside for her."
    "Since she's my best friend, I really don't mind."
    "We've known each other for so long, which is the only reason I wait for her."
    "That and being her friend of course."
    s 1l "We should probably start walking."
    mc "Good idea."
    show sayori at thide
    hide sayori
    scene bg corridor
    with dissolve_scene_full
    "We arrive at school, and we're about to go our separate ways to our classes."
    "Before I head into class, Sayori turns around and says something."
    show sayori 1b at t11
    s "Hey [player], have you ever thought about joining the literature club?"
    mc "Literature? I don't know, Sayori. I'm not really into that kind of stuff."
    show sayori 2e at t11
    s "C'mon, please! We could use more members, and it would be great to have you there."
    s "We have Monika, Yuri, and Natsuki too, and they're all really nice!"
    s "Besides, I promised everyone I'd bring in a new member today."
    mc "Don't make promises you can't keep Sayori!"
    show sayori 5b at s11
    s "Eh-heh..."
    "Now what am I supposed to do?"
    "Literature isn't exactly my forte, but I don't want to upset Sayori."
    "I quickly make up my mind."
    mc "I'll tell you what, Sayori."
    mc "I'll go to this one meeting."
    show sayori 4r at h11
    s "Yay!"
    mc "However..."
    show sayori 1n at t11
    mc "If I don't end up liking it, I'm not going to join."
    "Sayori ponders this for a moment." 
    "It's as if she's deep in thought on how to get me to stay..."
    show sayori 1r at t11
    s "Okay!"
    show sayori 1x at t11
    s "I'll come get you at your last class."
    mc "That sounds good. See you later Sayori!"
    s "Bye [player]!"
    show sayori at thide
    hide sayori
    "Sayori walks away, and then begins to run, realizing she'll be late to her class."
    "I'm going to be late as well, so I head into the classroom."
    scene bg class_day
    with wipeleft_scene
    "I arrive at class just in time."
    "I quietly take my seat and wait for class to start."
    "I keep pondering what just happened."
    "Sayori seemed really excited about this literature club. Now I'm curious to see what it's like."
    "I haven't read many books, but I'm still willing to try it out."
    "I look up as the teacher is about to start."
    scene bg class_day
    with dissolve_scene_full
    "It's the end of school."
    "I pack my things up and that's when I notice Sayori."
    show sayori 1x at t11
    s "Hi [player]! You ready?"
    mc "I guess so."
    show sayori 42hbow at s11
    s "Oh, I don't want to force you to go or anything."
    mc "It's all right Sayori, I don't mind at all."
    show sayori 1d at t11
    s "Oh, okay."
    show sayori 1c at t11
    s "Let's go then."
    show sayori at thide
    hide sayori
    scene bg corridor
    with wipeleft_scene
    show sayori 1a at t11
    "We exit the classroom and begin walking down the hall. I have so many questions, but I don't want to overwhelm Sayori."
    "Instead, I just ask a few basic questions."
    mc "So, what is the club like?"
    show sayori 2x at t11
    s "Well, there are four of us currently: Me, Natsuki, Yuri, and Monika."
    s "Natsuki is..."
    show sayori 1y at t11
    s "You'd have to meet her to understand."
    s "She is...{w=0.3} something."
    mc "Okay... what about everyone else?"
    show sayori 3x at t11
    s "Yuri is very quiet, but really nice to be around. She reads the most out of all of us."
    s "And Monika is club president."
    mc "Monika... now that you mention her name again, it does sound familiar."
    mc "Wasn't she the president of the debate club last year?"
    show sayori 1c at t11
    s "I'm not sure, I never asked her."
    mc "One way to find out, I guess."
    show sayori 3x at t11
    s "We're here!"
    "We're in a part of the school I've never passed through before."
    "It's a part usually held for third-years or smaller clubs." 
    "Given what Sayori had told me, it makes sense that the Literature Club would meet here."
    "Well, there's no backing out now."
    mc "You first."
    show sayori at thide
    hide sayori
    scene bg club_day
    with wipeleft_scene
    "I open the clubroom door to see a pretty empty classroom."
    "Is this the right place?"
    "Sayori immediately shatters any doubt I have."
    show sayori 4r at t21
    s "Everyone! The new club member is here!"
    mc "I said don't call me a new mem-{nw}"
    show natsuki 4e at f22
    a "Seriously? You brought a boy? Way to kill the atmosphere."
    "Well,{w=0.4} that's not sexist at all."
    show natsuki 4e at t22
    show sayori 2h at f21
    s "Hey, don't be mean to [player]."
    show sayori 2h at t21
    show natsuki 1l at f22
    a "I'm only kidding. I'm Natsuki, by the way."
    mc "Nice to meet you."
    show natsuki 5q at f22
    n "Although Sayori, if you recruit any more members in the future, please try to bring a girl next time."
    "Here we go with the sexism again."
    "Already we're off to a great start."
    show natsuki 5q at t32
    show sayori 2h at t31
    show yuri 1f at f33
    a "Natsuki, please try to be nice to our new member."
    show yuri 1f at t33
    show natsuki 1o at f32
    n "Oh come on Yuri, I was just playing around."
    show yuri 1h at f33
    show natsuki 1o at t32
    y "Try and think about how [player] feels Natsuki."
    show yuri 1h at t33
    show natsuki 3q at f32
    n "..."
    n "Sorry, [player]."
    mc "That's alright."
    stop music fadeout 2.0
    "I wonder if Natsuki is always like this?"
    "I get that having a new club member might be a new thing for her, but I think she could be a little nicer."
    show natsuki 3q at t32
    #Start Convos with Natsuki and Yuri
    play music midroom fadein 2.0
    $ renpy.notify("< e s c p >-Midnight Room")
    show sayori at thide
    hide sayori
    show yuri at thide
    hide yuri
    show natsuki 3q at t11
    mc "So you said your name is Natsuki, correct?"
    show natsuki turned happ om oe at t11
    n "That's me!"
    n "Welcome to the club!"
    show natsuki turned doub om oe at t11
    n "Don't expect me to take it easy on you though."
    mc "What's that supposed to mean?"
    show natsuki turned lhip doub om ce at t11
    n "Here at the Literature Club, we take things very seriously."
    n "We take the hardest books known to mankind and analyze down to the last question mark."
    show natsuki turned anno om oe at t11
    n "And that's on a normal day."
    mc "A normal day?"
    "I know she's toying with me, but I let it slide."
    show natsuki turned rhip sedu om oe at t11
    n "And then there's Fridays."
    show natsuki turned rhip sedu om ce at t11
    n "{i}That{/i} is when it gets real."
    show sayori turned laug om oe at f41
    $ textbox_color = "blue"
    s "But Natsuki, don't you mostly read manga?"
    show natsuki turned pani om oe at h11
    show sayori turned laug om ce at f41
    pause 1.5
    s "Guess I was right, hehe."
    show sayori at thide
    hide sayori
    show natsuki turned pani om ce at t11
    mc "Manga, huh?"
    n "You heard nothing!"
    $ textbox_color = "orange"
    mc "Well, I'd be lying if I said I didn't read manga too."
    show natsuki turned lhip lsur cm oe at t11
    pause 1.5
    show natsuki turned rdown lsur om oe at t11
    $ textbox_color = "black"
    n "You..."
    n "Read manga too?"
    mc "Yes, I do."
    show natsuki turned laug om oe at t11
    n "Well, I'm glad I'm not the only one."
    mc "Me too."
    show natsuki turned doub om oe at t11
    n "Oh please, you would've tried to hide it too."
    mc "Alright, alright. Fair enough."
    mc "So what's your favorite manga?"
    show natsuki turned lhip rdown neut om oe at t11
    n "Let's see...{w=0.5} I've been reading {i}Parfait Girls{/i}-{nw}"
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound audio.glitch4 #You can change this sound if you want
    pause 0.75
    hide screen tear
    n "Let's see...{w=0.5} I've been reading {i}Black Spade: Magic Bloom{/i} recently."
    mc "Oh really? I keep meaning to check that one out."
    show natsuki cross happ om ce at t11
    n "Really?"
    mc "Yeah, I've heard it's a good series. I don't really know what it's about though."
    show natsuki turned neut om oe at t11
    n "Well, it's about a girl who has no magical powers in an all-magic world."
    n "She battles demons and eventually decides to join an anti-demonic cult."
    show natsuki turned happ om ce at t11
    n "Overall, I'm enjoying it so far!"
    mc "Sounds interesting."
    show natsuki turned ldown angr om ce at t11
    n "Well, read it soon, or we will have issues."
    mc "Ummm... {w=0.3}yes ma'am?"
    show natsuki turned ldown rhip laug om oe at t11
    n "That's more like it."
    show natsuki turned ldown rhip curi om oe at t11
    n "So I've opened up about what I've read, how about you? What are you reading?"
    show natsuki turned ldown rhip curi cm oe at t11
    mc "Me?"
    mc "Let's see...{w=0.3} I've been reading {i}Bleached: Spirit Strikers{/i}."
    show natsuki turned rdown curi om oe at t11
    n "Never heard of that one."
    show natsuki turned rdown neut cm oe at t11
    mc "Well, basically, it's about a guy who becomes the Grim Reaper after he inherits the title from his parents, who were also reapers."
    mc "And it turns out that he isn't the only reaper out there. He meets all kinds of people, reapers and non-reapers alike."
    mc "I'd definitely recommend it."
    show natsuki cross happ om oe at t11
    n "That sounds so cool!"
    show natsuki cross dist om oe at t11
    n "Even if I'm not much of a shonen reader."
    show natsuki cross neut om oe at t11
    n "I prefer shōjo."
    mc "Jojo?"
    show natsuki turned rhip anno om oe at t11
    n "No... {i}shōjo{/i}."
    $ textbox_color = "orange"
    mc "I'm messing with you."
    show natsuki turned lsur cm oe at t11
    pause 1.5
    mc "Hey, you messed with me first."
    $ textbox_color = "black"
    show natsuki turned anno om oe at t11
    n "Fine...{w=0.2} I guess."
    show natsuki turned rdown neut om oe at t11
    n "Well, I've got something to do real quick before Monika arrives."
    mc "Oh, alright then."
    show natsuki at thide
    hide natsuki
    "Natsuki walks away, headed towards the back closet."
    "I glance over into the closet...{w=0.2} is that manga?"
    "Maybe this club won't be so bad after all."
    "{b}If{/b} I join. If."
    show yuri turned happ om oe at t11
    y "Hello [player]."
    show yuri turned happ cm oe at t11
    mc "Oh, hi...{w=0.3} Yuri, was it?"
    show yuri turned happ om ce at t11
    y "Yes!"
    show yuri turned happ om oe at t11
    y "Welcome to the club."
    mc "Thanks, Yuri."
    show yuri turned lup neut om oe at t11
    y "So tell me, what brings you to the Literature Club?"
    mc "Well, Sayori kept telling me I should join a club, so she offered to take me here."
    show yuri turned dist om oe at t11
    y "Oh, so you're not joining, just visiting."
    mc "Well...{w=0.3} that might change."
    mc "I haven't said whether I'd join or not."
    show yuri turned ldown curi cm oe at t11
    show sayori turned anno om oe at f41
    s "You took some convincing before you decided to come here."
    show sayori turned anno cm oe at t41
    mc "C'mon, give me a little more credit then that Sayori."
    show natsuki cross doub om oe at f44
    $ textbox_color = "pink"
    n "Dude, she's probably right."
    show natsuki at thide
    hide natsuki
    show sayori turned sedu cm oe at t41
    show yuri turned curi cm oe at t11
    pause 1.5
    mc "Don't give me that look Sayori."
    $ textbox_color = "black"
    show sayori turned yand om ce at f41
    s "Hehe."
    show sayori at thide
    hide sayori
    show yuri turned lup neut om oe at f11
    y "So I take it you and Sayori are good friends."
    show yuri turned lup neut cm oe at t11
    mc "With an occasional side of backstabbing, we make for an inseparable duo."
    mc "That's how we roll."
    show yuri turned lsur om oe at t11
    "..."
    "That probably sounded {i}super{/i} cringy..."
    show yuri turned laug om ce at t11
    "Surprisingly, this gets a laugh out of Yuri."
    show sayori turned laug cm ce at t41
    "I can also see Sayori chuckling to herself out of the corner of my eye."
    show sayori at thide
    hide sayori
    show yuri turned ldown happ om oe at f11
    y "You both seem dependable for each other."
    show yuri turned ldown happ cm oe at t11
    mc "You could say that."
    show yuri turned neut om oe at t11
    y "So was Sayori the only reason you came here?"
    show yuri turned neut om oe at t11
    mc "Well...{w=0.2} kinda."
    mc "Truth be told, I do want to be supportive of her too."
    show yuri turned lup neut mb at t11
    y "Well, that's very nice of you."
    y "I sure hope you'll decide soon."
    show yuri turned neut ma at t11
    mc "Well, I might need some time to think it over."
    mc "..."
    mc "So what do you like to do?"
    show yuri 1f at t11
    y "In the club?"
    show yuri 1e at t11
    mc "Yeah, or in your free time."
    show yuri 2j at t11
    y "Well, as I'm sure Sayori told you, I do love reading."
    y "I like complex stories, ones that build a universe that I can really get immersed in."
    show yuri 2d at t11
    $ textbox_color = "purple"
    y "Right now, I'm reading {i}The Portrait of Markov{/i}-{nw}"
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound audio.glitch4 #You can change this sound if you want
    pause 0.75
    hide screen tear
    show yuri 1e at t11
    pause 1.0
    show yuri 2f at t11
    $ textbox_color = "black"
    y "Right now, I'm reading {i}The Fates of Forgotten Realms{/i}."
    y "It's about an ancient empire that fell long ago, but some kind of curse has brought it back, and the entire world now depends on this new empire for resources."
    show yuri 1b at t11
    y "Eventually, the main characters come in, and they have to figure out how to stop the curse."
    show yuri 1a at t11
    mc "That sounds rather interesting."
    show yuri 1d at t11
    y "It really is! I'd highly recommend it."
    show yuri 1f at t11
    y "I heard you read manga."
    show yuri 2g at t11
    mc "Well, um, yes. Yes, I do."
    "God, why'd I get so sweaty all of a sudden?"
    show yuri 1j at t11
    y "Natsuki and I once had a discussion-{nw}"
    show yuri 1j at t21
    show natsuki 4b at f22
    n "Argument."
    show natsuki 4g at t22
    show yuri 1f at f21
    y "-about whether manga could be considered literature."
    show yuri 1e at t21
    mc "Well, no argument there. Obviously, it is."
    show natsuki 1z at f22
    n "THANK YOU! Finally {i}somebody{/i} agrees with me!"
    show natsuki 1a at t22
    show yuri 3o at f21
    y "Natsuki, I don't disagree, I just had different opinions back then."
    show yuri 3g at t21
    show natsuki 2k at f22
    n "Back then as in two weeks ago?"
    show natsuki 2j at t22
    "I get the feeling that Natsuki and Yuri squabble frequently."
    "Just a passing urge."
    show yuri 3d at f21
    y "Well, we've since agreed that manga can tell good-{nw}"
    show yuri 3d at t21
    show natsuki 2l at f22
    n "Amazing."
    show yuri 3d at f21
    y "Stories."
    show yuri 3h at f21
    y "Natsuki, I'd appreciate it if you didn't interrupt."
    show yuri 3g at t21
    show natsuki 1r at f22
    n "Sheesh, sorry."
    show natsuki at thide
    hide natsuki
    show yuri 3g at t11
    "Natsuki makes a quick exit while I quickly try and change the subject."
    mc "So, how did you find the club?"
    show yuri 1f at t11
    y "It's a rather interesting story."
    "She gets a bit more quiet for some reason, as if she doesn't want anyone else to hear."
    show yuri 1b at t11
    y "I was in the school library after school, reading."
    y "I was packing up my things, getting ready to leave when Sayori came running up to me."
    show yuri 2j at t11
    y "Now, I didn't {i}actually{/i} know her at the time, but I've seen her around."
    y "She was always outgoing and talking to others, trying to get new club members."
    show yuri 2f at t11
    y "From what I observed, people were usually very friendly with Sayori."
    show yuri 1o at t11
    y "But then they would always say no and give some vague excuse as to why they couldn't join."
    show yuri 2f at t11
    y "Even with all the rejection, she kept going."
    "I pause at that."
    "Sayori kept going..."
    "Given what she told me a while ago, I'm glad to hear that."
    "I snap back to reality because Yuri is still talking."
    show yuri 1d at t11
    y "So when she came up to me, I pretended like I had never seen her before."
    show yuri 1b at t11
    y "We talked for a little bit, and then-{nw}"
    show yuri 3f at t11
    y "[player], are you alright?"
    y "You look a little weary."
    show yuri 3e at t11
    mc "Oh yes, sorry."
    mc "Please keep going."
    y 3f "Right. So then, Sayori asked me to join the club."
    y 1b "And of course, I said yes."
    show yuri 1a at t11
    "Wow."
    "Hearing that about Sayori is rather heart-warming."
    "Knowing she was persistent like that is wonderful."
    mc "That's great to hear."
    y 1f "Well, I wasn't going to say no."
    show yuri 1e at t11
    mc "I'm glad you didn't."
    mc "Sayori always knows who to pick for the right things."
    mc "I'm glad you said yes."
    y "..."
    y 2b "You two seem to highly regard each other."
    show yuri 1a at t11
    mc "Yeah, Sayori is a goofy goober most of the time, but without fail, she's the most loyal friend you could have."
    mc "..."
    mc "Wait, what you said just now, did you mean she talks about-{w=0.4}{nw}"
    y 3d "Yes."
    y 2j "Given her...{w=0.5} {i}excited{/i} personality, she never said your name directly."
    y 2f "But she has told me that you are the best friend she could ever have."
    y "She said you even helped her through a tough time recently."
    show yuri 2g at t11
    "I tense a bit."
    "Right...{w=0.3} {i}that{/i}."
    "I really don't want to think about it now."
    y 1h "Although, she never said what it was..."
    y 1b "But that doesn't really matter."
    y 2d "Just know she sees you and cares about you."
    show yuri 2c at t11
    mc "Wow, thanks."
    mc "And, uh, nice to meet you too."
    show yuri 2d at t11
    "Yuri laughs."
    y 1q "I'm never this open around strangers."
    y 1j "But I guess since Sayori knows you so well it feels a bit different."
    show yuri 1a at t11
    mc "Haha, I suppose so."
    "Then, Sayori walks over to us."
    #End
    show sayori 2c at f21
    s "Say, where's Monika?"
    show sayori 2c at t21
    show yuri 2v at f22
    y "She told me earlier that she'd be a few minutes late."
    show yuri 2v at t22
    show sayori 4c at f21
    s "Oh, she didn't tell me that."
    show sayori 1k at f21
    s "I hope she can make it."
    s "After all, she asked me to bring in a new member."
    mc "Wait, she asked-{nw}"
    show monika 1b at l41
    show sayori 1k at t42
    show natsuki 1c at t43
    show yuri 3e at t44
    m "Hello everyone! Sorry that I'm late!"
    show monika 1i at hf41
    m "Oh, Sayori, I'd forgotten you were going to bring someone today!"
    show monika 1m at f41
    m "Sorry about that"
    show monika 1m at t41
    show sayori 4r at f42
    s "That's all right!"
    show sayori 4x at f42
    s "Monika, this is [player]. [player], Monika!"
    show sayori 4x at t42
    mc "Nice to meet you, Monika."
    show monika 2j at f41
    m "Welcome to the Literature Club, [player]! It's great to have you here."
    show monika 2j at t11
    show yuri at thide
    hide yuri
    show natsuki at thide
    hide natsuki
    show sayori at thide
    hide sayori
    #Add Monika conversation
    mc "Glad to be here."
    mc "So, what's the club all about? I didn't exactly get a good idea of what exactly you guys do..."
    m 3b "We're all about literature, [player]. It's a cozy space for people who appreciate the written word."
    show monika 2a at t11
    mc "Sounds interesting."
    mc "How often do you meet?"
    m 1k "Every day!"
    m 1b "We're pretty laid back, nothing too formal."
    mc "That's about the opposite of what Natsuki told me."
    show monika 2a at t11
    m 2n "Well, Natsuki is known to exaggerate things a little bit."
    m 1i "But don't take it to heart."
    mc "Oh, alright then."
    m 1b "Oh, and another thing too."
    m "We call ourselves the Literature Club, but we also do writing from time to time."
    show monika 1a at t11
    mc "Isn't that like...{w=0.3} false advertising?"
    show monika forward curi
    m "What?"
    show monika forward curi mh
    m "Of course not!"
    show monika forward curi me
    mc "A bit misleading...{w=0.3} maybe the English Club would be better?"
    show monika forward uniform anno rhip mg
    m "Do you want to be the club president instead of me?"
    show monika forward uniform anno rhip cm
    mc "..."
    "Touche."
    mc "Alright, do it your way."
    mc "Just saying."
    show monika forward uniform dist rhip mc
    m "I'll be honest, I did actually consider calling this the English Club."
    show monika forward uniform dist rhip ma
    mc "Oh, so I do have some ground with that?"
    show monika forward uniform happ lpoint rhip mb
    m "But I decided that sounded too formal."
    show monika forward uniform happ ldown rdown ma
    "I think she ignored me on purpose."
    "Not that I blame her."
    show monika forward uniform happ ldown rdown mb
    m "So I went with the Literature Club instead."
    show monika forward uniform dist ldown rdown mb
    m "Even if we are technically an English Club."
    show monika forward uniform dist ldown rdown
    mc "An acceptable answer"
    show monika forward uniform ldown rdown
    call screen dialog("[currentuser], I know you saw what happened earlier.", ok_action=Return())
    call screen dialog("I need your help.", ok_action=Return())
    m "..."
    mc "Oh, uh, sorry Monika, I didn't quite catch that."
    mc "I think I zoned out for a second."
    show monika forward uniform ldown rdown om
    m "Oh, that's alright."
    call screen dialog("I need her free.", ok_action=Return())
    show monika forward uniform nerv om
    m "I was just saying that it was good to have you here."
    show monika forward uniform nerv cm
    mc "Well thank you!"
    mc "So from what Sayori was saying, you asked her to bring me?"
    show monika forward happ om
    m "Well, kinda."
    show monika forward happ lpoint om
    m "I'm looking to bring in more members to the club, and I asked Sayori to bring one of her friends."
    m "And it looks like she brought you."
    show monika forward happ lpoint cm
    mc "It's me."
    mc "Oh, I do actually have another question too."
    show monika forward curi ldown mg
    m "What is it?"
    show monika forward curi ldown cm
    mc "Weren't you the president of the debate club last year?"
    show monika forward dist ldown cm
    "Monika pauses for a moment."
    show monika forward dist ldown om
    m "Well...{w=0.3} I..."
    mc "Oh, if it's not something you want to talk about, then that's fine."
    show monika forward lsur ldown rdown om
    m "No! It's not that."
    show monika forward flus ldown rhip om
    m "I was the president, but I had to disband the club."
    show monika forward flus ldown rhip cm
    mc "Oh. Any particular reason why?"
    show monika forward flus ldown rhip om
    m "There was...{w=0.3} drama, I guess you could say."
    show monika forward flus ldown rhip cm
    mc "Enough to disband a club?"
    show monika forward flus ldown rhip om
    m "Yeah, it was pretty bad."
    show monika forward anno ldown rhip mf
    m "I don't really want to go into detail though."
    "I nod."
    mc "That's alright."
    mc "So then you decided to do something else?"
    show monika forward happ ldown rdown om
    m "Yes! I formed the literature club."
    show monika forward happ ldown rdown cm
    mc "English club?"
    show monika forward anno ldown
    pause 1.0
    #Monika glares at MC
    mc "Sorry."
    show monika forward dist ldown
    m "..."
    show monika forward dist ldown mg
    m "No, I should be sorry."
    m "I've probably made a terrible first impression."
    show monika forward dist ldown cm
    mc "I should probably stop being such an ass then."
    mc "You do seem a bit stressed."
    show monika forward nerv ldown om ce
    m "Ha, you could say that again."
    show monika forward nerv ldown cm oe
    mc "Well, I'm not going to."
    show monika forward curi om
    m "Huh? Going to what?"
    show monika forward curi cm
    mc "Say it again."
    show monika forward curi om
    m "Say what again?"
    show monika forward curi cm
    mc "You do seem a bit stressed."
    show monika forward sedu rhip om
    m "You said it again."
    show monika forward curi cm
    mc "..."
    mc "Fuck."
    pause 1.0
    mc "Oh, sorry."
    show monika forward laug rhip om ce
    m "No it's alright."
    show monika forward laug rhip cm oe at t21
    show sayori turned shoc at f22
    s "[player], what did you just say?"
    show sayori turned shoc md at t22
    mc "Uh, nothing."
    mc "Definitely nothing at all."
    show sayori turned sedu mb at f22
    s "C'mon, you know the punishment for swearing."
    show sayori turned sedu ma at t22
    mc "Sayori, no, not here, not- ACK!"
    show monika forward laug rhip cm ce at t21
    show sayori turned laug at t22
    "Sayori begins to lightly tickle me, punishing me for my crime."
    "I've never wanted to drop dead more then I do right now."
    "Finally, Sayori stops her torture methods and steps away."
    show sayori turned angr mc at f22
    s "Justice has been served."
    show sayori turned angr ma at t22
    mc "You call {i}that{/i} justice?"
    show sayori turned anno mb at f22
    s "Yep!"
    show sayori turned anno ma at t22
    show monika forward flus oe mb at f21
    m "Well, I guess since you two are friends, I'll allow it."
    show monika forward neut mg
    m "But Sayori, just keep in mind, other club members might not find it as...{w=0.3} amusing if you did that."
    show monika forward neut ma at t21
    mc "I was supposed to be amused?"
    show monika forward lsur om at f21
    m "What? Oh no!"
    m "I... didn't mean it like that!"
    show monika forward lsur cm at t21
    mc "Nah, I'm fucking around."
    show sayori tap neut m1 at t22
    "Sayori leans in, prepared for round two."
    mc "One and done, bun."
    show monika forward curi
    show sayori tap pout at f22
    s "Ohhhhh."
    s "But I want to-{nw}"
    show sayori tap neut m2 at t22
    mc "Later."
    mc "..."
    mc "I really set myself up there, shit."
    show monika forward laug rhip mb at f21
    m "You just keep digging your own grave, you know?"
    show monika forward laug rhip cm at t22
    show sayori turned happ
    mc "Grab me some soap, I need to clean out my mouth."
    show monika forward laug rhip om ce
    "Monika laughs."
    show monika forward laug rhip om ce at t31
    show sayori turned happ at f32
    show natsuki turned curi mh at f33
    n "Normally I run quite a mouth too, but I don't swear here."
    show natsuki turned neut cm at t33
    show sayori turned anno
    show monika forward curi rdown om oe at f31
    m "Oh? I wouldn't have guessed that about you, Natsuki."
    show monika forward curi cm at t31
    show natsuki turned happ mc ce at f33
    n "Yeah, I swear all the time around friends."
    show natsuki turned happ cm ce at t33
    show sayori turned anno lup om at f32
    s "Are we not your friends?"
    show sayori turned laug lup mn at t32
    show natsuki turned anno om at f33
    n "Don't be ridiculous Sayori."
    n "I don't swear here because I don't want you to learn anything bad."
    show monika forward flus ma at t41
    show sayori turned neut at t42
    show natsuki turned anno cm at t43
    show yuri turned flus mb at f44
    y "Well Natsuki, I'm afraid your efforts are futile."
    y "It seems as if [player] has already expanded Sayori's vocabulary."
    show yuri turned flus ma at t44
    mc "Guilty as charged."
    mc "But hey, in the end, I can't control what Sayori picks up."
    show monika forward laug rhip
    "Monika smirks."
    show natsuki turned doub om at f43
    n "You could watch your language around her."
    show natsuki turned doub cm at t43
    show sayori turned anno om at f42
    s "I can handle a few words, Natsuki."
    show sayori turned anno ma at t42
    mc "I mean, it's fine if it's all in good fun, right?"
    show natsuki turned angr lhip om at f43
    n "Fine, but no more teaching Sayori questionable words, got it?"
    mc "I will do my whole-hearted best not to."
    s "Aw, come on! Where's the fun in that?"
    n "..."
    n "I have no words."
    "Monika looks like she wants to move things along."
    show monika 4a at f41
    m "Okay everyone! Let's take a seat."
    show monika 4a at t41
    "Together, we push together desks to form a makeshift table."
    "Then, everyone takes a seat."
    show monika 1l at t41
    show sayori 4s at t42
    show natsuki 2d at t43
    show yuri 2c at t44
    m "Alright, did everyone get through our reading?"
    y "Yes."
    s "Yep!"
    n "Sure did."
    "They begin talking about the book they've been reading together recently, though it  takes a while for me to catch the name."
    "{i}The Machine Stops{/i} by E.M. Forster."
    "It sounds like one of those freaky dystopian novels."
    "Now that I think about, it would seem like the kind of book Yuri would like."
    "As time goes on, I begin to feel more and more out of place."
    "Partially because all the members are all girls."
    "I really feel awkward now."
    "I glance over at Sayori, trying to get her attention." 
    "She doesn't seem to see me."
    "At least, I think so, until-{nw}"
    stop music fadeout 2.0
    show sayori 1g at f42
    s "[player], can you come with me for a second?"
    show monika 1i at t41
    show natsuki 2g at t43
    show yuri 1f at t44
    mc "Huh? Oh, sure."
    "I follow Sayori out of the classroom, leaving the other club members a little confused."
    show sayori at thide
    hide sayori
    show monika at thide
    hide monika
    show natsuki at thide
    hide natsuki
    show yuri at thide
    hide yuri
    scene bg corridor
    with wipeleft_scene
    play music truelovewaits
    $ renpy.notify("Wretched Team-True Love Waits")
    show sayori 2f at t11
    mc "So, what's going on?"
    show sayori 1j at t11
    s "You tell me!"
    "I jump back a little bit, surprised."
    "Sayori has never snapped at me like that before."
    s "I'm trying to help you!"
    mc "Help me how?"
    show sayori 1k at s11
    "Sayori shrinks against the wall, clearly not sure where she's going with this."
    mc "Look, I'm not mad, I'm just wondering."
    "She doesn't speak for a long time."
    s "I've just noticed that we don't really hang out outside of school anymore."
    show sayori 1h at t11
    s "I thought that by bringing you here, we could hang out more."
    "Both of us don't say anything at first."
    "Was all of this just because Sayori wanted to be around me more?"
    "I feel awful now."
    "All this time, I've just brushed her off without much thought."
    "Even after she told me about...{w=0.3} {i}that{/i}."
    mc "Sayori..."
    show sayori 1g at t11
    mc "I'm sorry."
    show sayori 1f at t11
    "She looks at me a little bit confused at first, but seems to understand."
    mc "I really should've been there for you more. But I wasn't."
    mc "I'm really sorry."
    show sayori 1t at t11
    s "It's all right [player]."
    s "It just gets really rough sometimes, even after I told you the truth."
    s "I thought the club might be a good distraction from it all."
    s "Ehehe, I know you probably feel a little bit awkward in there."
    mc "Understatement of the year."
    show sayori 5b at s11
    s "Heh, sorry."
    mc "Don't worry about it."
    show monika 2f at f21
    show sayori 5b at t22
    m "Hey, is everything alright out here?"
    show sayori 4c at f22
    s "Of course!"
    show sayori 4c at t22
    show monika 3l at f21
    m "Sorry if you feel a bit awkward  [player], I totally get it."
    mc "I mean, I do a little bit, but that's alright."
    show monika 5a at f21
    m "Well, it's kinda my job to make you feel welcome."
    show monika 1b at f21
    m "You ready to head back in?"
    mc "After you."
    show monika at thide
    hide monika
    show sayori at thide
    hide sayori
    stop music fadeout 2.0
    scene bg club_day
    with wipeleft_scene
    play music t5
    $ renpy.notify("Dan Salvato-Okay, Everyone!")
    show sayori 2a at t42
    show monika 1k at f41
    m "Okay everyone! We're back."
    show monika 1k at t41
    show yuri 1t at f43
    show natsuki 5n at t44
    y "Is everything alright?"
    mc "Yeah, all good."
    show yuri 2n at t43
    show natsuki 5l at f44
    n "Glad to hear it. Yuri was-{nw}"
    show natsuki 5l at t44
    show yuri 1n at f43
    y "Don't-"
    show yuri 2l at t43
    show monika 2c at t41
    show sayori 3b at t42
    show natsuki 3b at f44
    n "-worried."
    show natsuki 3b at t44
    show yuri 4a at t43
    "An awkward silence falls over us."
    "Yuri looks really embarrassed for some reason."
    "Could it be that maybe..?"
    "No, that would be ridiculous."
    mc "I appreciate your concern, Yuri. Thank you."
    show yuri 4b at f43
    y "You're...{w=0.5} welcome."
    show yuri 2l at t43
    show monika 4k at f41
    m "Okay everyone! That's the end of today's meeting!"
    show monika 2e at f41
    m "[player], glad you could join us today!"
    mc "Thanks for having me!"
    m "Oh, and just so everyone knows, I'm bringing in a new member tomorrow!"
    show monika 2e at t41
    show sayori 4n at f42
    show natsuki 1k at t44
    show yuri 2f at t43
    s "Really? Who?"
    show sayori 4n at t42
    show monika 4b at f41
    m "Her name is Kotonoha."
    m "We were in the debate club last year, and we're good friends."
    show monika 4b at t41
    "However, there seems to be a slight hint of doubt when Monika says that."
    "Nobody mentions it though."
    show sayori 4r at f42
    s "I can't wait to meet her!"
    show sayori 4r at t42
    show yuri 1q at f43
    y "We sure are getting quite a few new members."
    show yuri 2f at f43
    y "Even Natsuki only joined a few weeks ago."
    y "But I'm happy for the change!"
    show yuri 2f at t43
    show natsuki 4d at f44
    n "I also know Kotonoha!"
    n "She's in one of the same classes as me right now!"
    show natsuki 1q at f44
    n "Although, we haven't talked much."
    show natsuki 1q at t44
    show monika 1k at f41
    m "I'm glad some of us know Koto!"
    m "That'll make her feel more welcome."
    show monika 2b at f41
    m "And now with [player] joining us-"
    show sayori 1i at t42
    "Wait wait wait-"
    "Did I ever say I was going to join?"
    "I glance at Sayori, who looks as confused as I do."
    show monika 2b at t41
    mc "Now hold on."
    stop music fadeout 2.0
    mc "I never said I was going to join this club."
    show monika 1g at s41
    show sayori 1f at t42
    show yuri 2t at t43
    show natsuki 3m at t44
    m "Oh, I really thought you'd stay."
    show natsuki 3m at s44
    n "Was it something I said?"
    show yuri 2t at s43
    y "Sorry if your experience today wasn't enjoyable."
    show sayori 1k at s42
    s "[player]..."
    "Great."
    "Now I can't help but feel trapped."
    "I can't exactly say no, even if I don't feel like joining."
    "And besides, Sayori probably wouldn't forgive herself or me if I didn't join."
    play music t2
    $ renpy.notify("Dan Salvato-Ohayou Sayori!")
    mc "Alright, alright."
    mc "I've made my decision."
    show monika 1d at t41
    show sayori 4b at t42
    show yuri 1e at t43
    show natsuki 4c at t44
    "The girls look at me with anticipation."
    "There's no going back now."
    mc "I'll join the club."
    show monika 1k at t41
    show sayori 4s at hf42
    show yuri 1d at t43
    show natsuki 2d at t44
    s "Yay!"
    show sayori 4s at t42
    show monika 1b at f41
    m "I'm glad you decided to stay."
    m "Can't say I expected so many new members this week."
    show monika 1b at t41
    show natsuki 1e at f44
    n "Yeah, you may need to worry about that eventually."
    show natsuki 1e at t44
    "We all talk for a few minutes before Monika notices the time."
    show monika 2c at f41
    m "So I hate to be the bearer of bad news, but I think it's time to leave."
    show monika 2e at f41
    m "See everyone tomorrow."
    m "Bye!"
    show sayori at thide
    hide sayori
    show monika at thide
    hide monika
    show natsuki at thide
    hide natsuki
    show yuri at thide
    hide yuri
    scene bg school
    with dissolve_scene_full
    show sayori 1q at t11
    "When we get out of school, Sayori seems more happy than I've seen her in a while."
    "I can probably guess why, but I ask."
    mc "You seem happier than usual."
    show sayori 1r at t11
    s "Of course I am! You joined the club after all."
    mc "How could I not?"
    show sayori 5b at t11
    s "Eh-heh, we did kind of guilt you, didn't we?"
    mc "Not on purpose, but yeah, slightly."
    show sayori 1x at t11
    s "Well, I'm glad you joined anyway!"
    show sayori at thide
    hide sayori
    scene bg residential_day
    with wipeleft_scene
    show sayori 2k at t11
    "We arrive at Sayori's house."
    "She's been quiet the entire walk home, which is unlike her."
    "I wonder if something is on her mind?"
    "I decide to ask."
    mc "Sayori, you've been pretty quiet"
    show sayori 2l at t11
    s "Oh, I was just thinking about asking you something."
    mc "Ask me what?"
    show sayori 3c at t11
    s "I was wondering if you'd like to hang out sometime. You know, outside of school?"
    mc "I don't see why not, I'd love that!"
    mc "How about tomorrow after school?"
    show sayori 4r at t11
    s "That sounds great!"
    show sayori 1x at t11
    s "See you tomorrow [player]!"
    mc "See you tomorrow Sayori!"
    show sayori at thide
    hide sayori
    "Sayori skips into her house and waves at me before she closes the door."
    "I wave back and head to my house."
    scene bg bedroom
    with wipeleft_scene
    "Once I'm home, I head straight to my room."
    "Today went really well in my opinion."
    "I managed to make Sayori happy, and now we'll get to spend some more time together."
    "I can't stop smiling as I sit down to do my homework."
    stop music fadeout 2.0
    scene bg bednight
    with dissolve_scene_full
    "It's 10 PM now."
    "I stayed up way later than I thought."
    "I pack away all my school things and get ready for bed."
    "As I'm changing clothes, I can't help but wonder, what if I had said no to Sayori?"
    "The obvious outcomes rise up, like her being upset at me, but I think more to the long-term effects."
    "I probably wouldn't be friends with Sayori anymore."
    "..."
    "Great, now I'm sad."
    "I do this often, where I make up fake scenarios in my head and get sad about them."
    "I shove that thought aside and go to sleep."

    #DAY 2 (Meet Kotonoha)
    scene bg black
    with dissolve_scene_full
    stop music fadeout 2.0
    play sound transyuri
    show splash_yuri_1
    show splash_yuri_background
    show splash_yuri_2
    pause 7
    hide splash_yuri_1
    hide splash_yuri_background
    hide splash_yuri_2
    scene bg bedroom
    with dissolve_scene_full
    play sound alarm
    "I wake up to my alarm clock beeping."
    "I blink away my grogginess as I read the time."
    "7:57 AM"
    play music t7
    $ renpy.notify("Dan Salvato-Poem Panic!")
    "{i}Crap!{/i}"
    "Hastily, I get up and quickly change into my school uniform."
    "I pick up my phone and see about ten missed calls from Sayori."
    "And then I spot a text message."

label sayori_convo:
    phone discussion "Sayori_Aoki":
        time year 2025 month 11 day 11 hour 7 minute 15
        "s" "I'm waiting outside, where are you?"
        "mc" "Crap I am so sorry."
    phone end discussion

label story1:
    "Crap crap crap..."
    scene bg kitchen
    with wipeleft_scene
    "I run into the kitchen and grab a granola bar."
    "I'm so late that it's not even funny."
    "I unwrap my granola bar, grab my backpack, and head out the door."
    scene bg residential_day
    with wipeleft_scene
    show sayori 1i at t11
    "When I get outside, Sayori is waiting for me."
    "She doesn't look too amused."
    show sayori 1j at t11
    s "{i}Now{/i} who's the late one?"
    mc "I am so sorry, I totally slept through my alarm."
    mc "We've got to start running."
    show sayori 2l at t11
    s "Yeah, we should go."
    mc "Race you there!"
    show sayori 1p at t11
    s "Hey! No fair, you got a head start!"
    "I laugh as we both start running"
    show sayori at thide
    hide sayori
    stop music fadeout 2.0
    scene bg school
    with wipeleft_scene
    play music t3
    $ renpy.notify("Track Name: Main Theme")
    show sayori 3y at t11
    "I struggle for breath as Sayori and I arrive at school."
    "We're both flushed from our run."
    mc "I totally won that."
    show sayori 3j at t11
    s "No you didn't!"
    s "I crushed you."
    show sayori 3r at t11
    s "You were like ten feet behind me the entire time!"
    mc "Sure Sayori, whatever you say."
    mc "Oh crap, I really have to get to class."
    show sayori 1m at t11
    s "Ah! So do I!"
    show sayori 1x at t11
    s "See you later [player]! I'll get you after school!"
    mc "Sounds good. Bye, Sayori!"
    show sayori at thide
    hide sayori
    "I begin to run again to class."
    scene bg class_day
    with wipeleft_scene
    "I arrive at class right on the stroke of the bell."
    "The teacher barely notices me as I take my seat."
    "I sit down and unpack my things."
    a "Hey!"
    "I jump a little to see someone standing right in front of me."
    show kotonoha turned happ om oe at t11 
    a "Do you have a spare pencil?"
    mc "Oh, um, I think I do..."
    "I rummage around my backpack and try to find a pencil I haven't chewed on yet."
    "It takes a minute, but I find one."
    mc "Here you go!"
    show kotonoha lchest happ om ce at t11
    a "Thank you!"
    show kotonoha at thide
    hide kotonoha
    "I watch her take her seat, and turn my focus to the teacher as he starts."
    scene bg class_day
    with dissolve_scene_full
    "The day went by in a blur."
    "I pack up my things as I wait for Sayori."
    "I wonder what Monika has planned for today?"
    "About five minutes later, Sayori peeks her head through the door."
    show sayori 1c at t11
    s "You ready?"
    mc "Of course!"
    "I get up and leave the classroom and follow Sayori out."
    show sayori at thide
    scene bg corridor
    with wipeleft_scene
    show sayori 1a at t11
    s "We're having a little mini-party for you and Kotonoha today!"
    mc "Oh really?"
    show sayori 1r at t11
    s "Yeah!"
    s "Monika and I planned it last night, so it might be a little last minute."
    mc "The night before does sound a little last minute."
    show sayori 5b at s11
    s "Well..."
    show sayori 5a at t11
    s "We couldn't exactly have planned it yesterday."
    mc "No, I totally get it."
    mc "It would be hard to plan this kind of thing during school the day of."
    show sayori 2l at t11
    s "I suppose your right."
    "We continue walking down the hall and towards the clubroom."
    "We don't talk much, but that's alright."
    "Sayori is probably trying not to burst with all the details about the party."
    "Probably for the best."
    "That's when I hear another pair of footsteps behind us."
    "I glance behind me to see who is following us."
    show kotonoha turned neut cm oe at t41
    "..."
    "It's the girl who asked me for a pencil earlier..."
    "My brain puts the pieces together quickly."
    "This must be Kotonoha."
    "Why else would she be following halfway across the school to the clubroom?"
    "I turn back around as so not to creep her out."
    show kotonoha at thide
    hide kotonoha
    show sayori 1x at t11
    s "We're here!"
    "I gently open the door. Sayori heads right on in."
    stop music fadeout 2.0
    scene bg club_day
    with wipeleft_scene
    play music setmyselfonfire
    $ renpy.notify("Wretched Team-Set Myself on Fire")
    show sayori 4r at f21
    s "Monika, [player] and I are here!"
    show sayori 4r at t21
    show monika 1k at f22
    m "Hello again [player]! Good to have you back."
    mc "Well, you failed to scare me off yesterday, so here I am."
    show sayori 2o at t21
    show monika 1l at t22
    "Monika laughs, but Sayori looks confused."
    mc "I'm joking around Sayori."
    show sayori 5c at f21
    s "I'm not that scary..."
    a "Hello?"
    show kotonoha turned neut cm oe at t31
    show sayori 5c at t32
    show monika 2b at f33
    m "Hello Kotonoha!"
    m "This is Sayori, my vice president, and [player]. He joined yesterday."
    show kotonoha surp cm oe at f31
    k "We're in the same class [player]."
    show sayori 1n at t32
    show monika 1d at t33
    show kotonoha lchest laug om oe b1a at f31
    k "What a small world."
    k "Well, at least we've met formally now."
    mc "Yes, nice to meet you too."
    show kotonoha lchest laug om oe b1a at t31
    show monika 2k at f33
    m "Looks like many of us know each other in more ways than we thought!"
    show monika 2k at t33
    #KOTO CONVO REEAAAL
    k "So [player], what brings you here?"
    mc "Truth be told, I only joined yesterday."
    mc "Sayori was the one that brought me here."
    k "Oh, so Monika didn't bring you here?"
    mc "No,{w=0.3} I hardly knew Monika before today."
    k "Oh."
    mc "Monika mentioned that she invited you to the club."
    k "Yeah,{w=0.3} she texted me over the weekend asking if I would come."
    k "I figured why not?"
    "For some reason, I'm not getting the friendliest of vibes from her."
    "Maybe she's just not too open around people she just met."
    mc "Well,{w=0.3} as the newest member of the club, welcome!"
    s "Are you like the offical club greeter now?"
    mc "Just trying to make somebody feel welcome, Madame Vice President."
    k "Well,{w=0.3} thank you!"
    show sayori 1h at f32
    s "Does anyone know where Natsuki and Yuri are?"
    show sayori 1h at t32 
    show monika 2b at f33
    m "Yuri told me earlier she'd be late."
    show monika 2b at t33
    show kotonoha turned om oe at f31
    k "Sayori, did you say Natsuki?"
    show kotonoha turned om oe at t31
    show sayori 10b at f32
    s "Yeah, she mentioned you two were in the same class yesterday."
    show sayori 1c at t32
    show kotonoha turned happ om ce at f31
    k "We don't talk much, but she's nice!"
    n "What do I hear about me?"
    show natsuki 2k at t41
    show kotonoha turned happ om oe at f42
    show sayori 2b at t43
    show monika 2a at t44
    k "Hi Natsuki!"
    show kotonoha turned happ om oe at t42
    show natsuki 4d at f41
    n "Oh hey Koto! I forgot you'd be here."
    show natsuki 4d at t41
    show kotonoha turned laug om ce at f42
    k "Nice to see you!"
    show kotonoha turned laug om ce at t42
    show natsuki 3z at f41
    n "Same here!"
    show natsuki 3z at t41
    show monika 3b at f44
    m "Natsuki, did you happen to see if Yuri was coming?"
    show monika 3b at t44
    show natsuki 1k at f41
    n "She was in the library last I saw her."
    n "She saw me, and I thought she was right behind me."
    show natsuki 1k at t41
    show sayori 1c at f43
    s "Maybe she just went to the bathroom or something?"
    mc "Maybe, but I haven't seen her all day-"
    "Suddenly, Yuri bursts into the room, startling us all."
    show yuri 1p at t51
    show natsuki scream at t52
    show kotonoha turned surp om oe at t53
    show sayori 4m at t54
    show monika 1i at t55
    y "Sorry I'm late!"
    show yuri 2o
    y "I lost complete track of time and..."
    show monika 2k
    show natsuki 1n
    show kotonoha turned neut cm oe
    m "Don't worry Yuri, I often lose track of time too."
    show monika
    mc "I can't tell  you the amount of times Sayori is late to things."
    show sayori 5c
    s "Come on, you're late to a lot of things too..."
    mc "Oh alright."
    show yuri 2j
    y "Haha, thanks, everyone."
    show yuri 1f
    y "Oh! You must Kotonoha."
    y "Nice to meet you!"
    show yuri 1f
    show sayori 2a
    show kotonoha lchest happ om ce
    k "Nice to meet you too Yuri!"
    show kotonoha lchest happ om ce
    show monika 3b
    m "[player] and Koto, we're throwing a surprise greeting for you two!"
    show kotonoha turned surp cm oe
    m "Welcome to the club!"
    mc "Thank you, Monika!"
    "Kotonoha stands there frozen for a second."
    "I can't really blame her, it's like the spotlight was just thrown at us."
    "Furthermore, even on her first day?"
    show kotonoha turned flus om oe
    k "Well,{w=0.4} I can't say I was expecting this."
    k "But thank you for organizing this!"
    show sayori 4r
    s "Our pleasure!"
    s "Welcome to the club you two!"
    show sayori 4r
    show yuri 1j
    y "It's a pleasure to have both of you here."
    show yuri 1j
    show natsuki 4y
    n "Don't worry you two, this was just as awkward for me when I joined."
    k "Oh really?"
    k "I mean,{w=0.3} I can totally relate."
    mc "Don't worry,{w=0.3} I felt just as awkward yesterday."
    k "Oh, I'm not the only one."
    n "But welcome regardless!"
    n "I'll get the cupcakes!"
    show natsuki at thide
    hide natsuki
    show yuri 1i at t41
    show kotonoha turned happ cm oe at t42
    show sayori 4a at t43
    show monika 3b at f44
    m "Okay everyone, let's make our usual table."
    m "And make sure to fit in a sixth chair!"
    show monika 3b at t44
    "We rearrange the desks, but there's no chance we would all fit around it."
    mc "We're gonna need a bigger table"
    show sayori 2o at f43
    s "I have an idea."
    "Sayori moves a couple of desks around, and now, there's room for another."
    show sayori 1r at f43
    s "There! Take a seat, everyone!"
    "Everyone sits down, and Natsuki returns with the cupcakes."
    scene bg natcup1
    with wipeleft_scene
    n "Here you go!"
    "Natsuki hands over a tray of six cupcakes. Each one is decorated to look like a cat."
    m "These look great Natsuki!"
    n "Thanks, but I kinda had to rush them."
    s "And they taste so good- MMPH!"
    "Sayori wastes no time digging into her cupcake."
    "I bite into my cupcake and almost gasp."
    mc "Natsuki these are amazing!"
    k "Especially the frosting!"
    k "It's so light and fluffy!"
    scene bg club_day
    with wipeleft_scene
    show kotonoha turned happ om oe at t11
    show yuri 3b at f21
    y "I think that they look rather cute."
    show yuri 3a at t21
    stop music fadeout 2.0
    show natsuki 2m at f41
    n "Cute?"
    n "That's not what I was aiming for..."
    show natsuki 2m at t41
    show sayori 5b at f22
    s "I ate mine too fast to be able to tell."
    show monika at thide
    show kotonoha at thide
    show sayori at thide
    hide monika
    hide kotonoha
    hide sayori
    show yuri 2f at t22
    show natsuki 4f at f21
    n "Why does everyone think they're cute?"
    show natsuki 4f at t21
    show yuri 2t at f22
    y "It's not meant to be an insult."
    show yuri 1b at f22
    y "I meant it as a compliment."
    play music t7
    $ renpy.notify("Dan Salvato-Poem Panic!")
    show yuri 1b at t22
    y "Usually when someone compliments you, you should say thanks."
    show yuri 1b at t22
    show natsuki 4w at f21
    n "Yuri, I'm focusing on flavor, not some childish aesthetic."
    n "People care about what's inside, not how cute they look!"
    show natsuki 4w at t21
    show yuri 1t at f22
    y "That may be true, but that still doesn't-"
    "Suddenly, Natsuki stands up and slams her hands on the table."
    show yuri 1t at t22
    show natsuki 4p at f21
    show yuri 1p at h22
    n "Well, maybe I don't want to be remembered for making cute cupcakes!"
    n "Besides, nobody ever said I had to accept your compliment."
    show natsuki 1p at t21
    show sayori 2h at f41
    s "Guys, maybe calm down please?"
    show sayori 2h at t41
    show yuri 1r at f22
    y "Sayori, this really doesn't involve you."
    show sayori at thide
    hide sayori
    y "Natsuki, it is general courtesy to accept a compliment, even if you don't like it."
    show yuri 1r at t22
    show natsuki 2w at f21
    n "Even if some creep walked up to me and complimented my body?"
    show natsuki 2w at t21
    show yuri 1o at f22
    y "That's blowing it way out of proportion! That's not even what we're talking about."
    show yuri 1o at t22
    show natsuki 4o at f21
    n "No it's not! Now you're just saying my argument is invalid."
    show natsuki 4o at t21
    mc "Ok guys, maybe-"
    "But before I can say anything else, Kotonoha slams her arms down on the table, hard."
    show yuri 1p at h33
    show natsuki scream at h32
    show kotonoha turned angr om oe at f31
    k "Will you two just {b}SHUT UP!{/b}"
    k "You two are arguing about the stupidest thing!"
    show kotonoha turned angr om ce at f31
    k "Honestly, I expected better of you Monika."
    stop music fadeout 2.0
    play music t9
    $ renpy.notify("Dan Salvato-My Feelings")
    show yuri 3o at t44
    show natsuki 2u at t43
    show kotonoha turned anno cm oe at t42
    show monika 1f at f41
    m "Wh- what?"
    show monika 1f at t41
    show kotonoha turned anno om oe at f42
    k "You left the debate club to start this? An unorganized mess?"
    show kotonoha turned anno om oe at t42
    show monika 2g at f41
    m "Koto..."
    show monika 2g at t41
    "Monika tries to talk, but can't seem to finish her sentence."
    "I feel kind of bad for her since the situation spiraled way out of control."
    "I also feel like I should help out in some way, but I don't know how to improve the situation."
    show kotonoha turned dist om ce at f42
    k "I expected better, Monika."
    show kotonoha at lhide
    hide kotonoha
    "Then, Kotonoha got up and left the room."
    "Nobody went after her."
    show sayori 1k at t41
    show monika 1q at t42
    show yuri 1h at t44
    "We all sit in silence for a moment before Yuri speaks up."
    show yuri 1f at f44
    y "Monika, I want to apologize-"
    show yuri 1f at t44
    show monika 1p at f42
    m "No, it's not your fault."
    m "Or Natsuki's for that matter."
    m "It's mine."
    show sayori 3f at t41
    show natsuki 2n at t43
    show yuri 2g at t44
    m "Kotonoha and I... have a complicated relationship."
    show monika 1d at f42
    m "Can I trust you guys not to say anything to her?"
    show monika 1d at t42
    show sayori 3h at f41
    s "We won't tell anyone."
    show sayori 3g at t41
    "Monika exhales, and begins."
    show monika 2p at f42
    m "Well, we met last year in the debate club, and we became really good friends."
    m "We were also rivals as well."
    show monika 1n at f42
    m "It started out as a friendly rivalry, with us having friendly debates about various topics."
    show monika 2r at f42
    m "But it got worse over time."
    show monika 2p at f42
    m "At first it was a disagreement about something, I don't even remember what."
    m "Over time, it got more heated, and other club members were starting to feel uncomfortable."
    m "So I told Kotonoha, either leave the club, or we can talk it out later."
    show monika 1r at f42
    m "We were cold with each other after that, and we didn't talk for weeks."
    m "We avoided each other during class, lunch, club meetings..."
    m "We avoided each other altogether."
    show monika 1g at f42
    m "Until recently."
    m "She texted me one day saying she wanted to talk"
    m "So we met up after school one day, and she said she wanted to make things better between us two."
    show monika 2n at f42
    m "We talked for a while, and it was quite nice."
    m "We made up and just had a friendly chat."
    m "After our talk, we hung out a few times."
    show monika 1l at f42
    m "And then I invited her to a club meeting..."
    show monika 1p at f42
    m "...which didn't go as I planned."
    show monika 1p at t42
    "Monika finishes her story, and we're all silent."
    show natsuki 3q at f43
    n "Well, I don't want to sound harsh or anything, but maybe don't bring her back."
    show natsuki 3q at t43
    show sayori 2m at t41
    show yuri 2o at f44
    y "Natsuki, that's a little-"
    show yuri 2o at t44
    stop music fadeout 2.0
    show monika 1i at f42
    m "No, maybe you're right."
    m "Maybe it's time to let go."
    show monika 1i at t42
    show sayori 1j at f41
    s "You can't be serious Monika."
    show monika 1f at t42
    play music t2
    $ renpy.notify("Dan Salvato-Ohayou Sayori!")
    s "You two were getting along great before today."
    s "From what it sounds like, both of you have changed."
    s "Maybe she had a bad day today."
    show sayori 3c at f41
    s "I think you should talk to her again."
    show sayori 3c at t41
    "Monika ponders this for a moment, considering Sayori's words carefully."
    show monika 1b at f42
    m "You're right Sayori."
    m "I shouldn't give up just yet."
    m "I'll talk to her tomorrow."
    show monika 1d at f42
    m "[player], would you mind coming with me tomorrow?"
    show monika 1d at t42
    mc "Sure, I can do that."
    mc "But why me?"
    show monika 1n at f42
    m "Just in case... things go wrong."
    show monika 3b at f42
    m "Not that it would!"
    m "Just in case."
    show monika 1b at t42
    mc "No, I totally get it."
    show monika 1k at f42
    m "Well thank you!"
    show monika 1n at f42
    m "Well, we're done for today, see everyone tomorrow!"
    show monika 1n at t42
    show natsuki 2l at f43
    n "Bye everyone!"
    show natsuki 2l at t43
    show yuri 1f at f44
    y "Natsuki, do you mind if I come with you?"
    show yuri 1f at t44
    show natsuki 2c at f43
    n "Uh, sure!"
    show natsuki 2c at t43
    show yuri 1b at f44
    y "Alright. Thank you everyone!"
    show yuri 1b at t44
    show sayori 1r at f41
    s "Bye!"
    show natsuki at thide
    show yuri at thide
    hide yuri
    hide natsuki
    show sayori 1r at t21
    show monika 1n at t22
    "Yuri and Natsuki leave together. I'm guessing they'll make up over their argument."
    "This leaves just the three of us."
    m "Say [player], I should add you to our group chat!"
    mc "You have a group chat?"
    s "Of course we do!"
    s "How else would be have planned things out like this?"
    mc "True, true."
    "I tell Monika my phone number, and I get a notification a few moments later."

label lit_convo:
    phone discussion "Books":
        time year 2025 month 11 day 11 hour 15 minute 24
        label "Monika Hashimoto added [player]."
        "m" "Hello [player]!"
        "mc" "Hello hello"
        "s" "Hiii :):):):)!!"
    phone end discussion

label story2:
    show monika 1b at f22
    m "See you two tomorrow!"
    show monika 1b at t22
    show sayori 3x at f21
    s "Bye!"
    mc "Bye Monika!"
    "Sayori and I leave the room and head out the hall."
    show monika at thide
    show sayori at thide
    hide monika
    hide sayori
    scene bg corridor
    with wipeleft_scene
    show sayori 2a at t11
    "We walk down the hall, away from the clubroom."
    show sayori 3c at t11
    s "Where should we meet later?"
    "I stare at Sayori for a moment, wondering what she's talking about."
    "Then I remember yesterday that we'd talked about making plans for today."
    "With everything that happened today, I'm surprised either of us remembered."
    mc "Well, we could meet at my place."
    show sayori 1x at t11
    s "That sounds great!"
    mc "Awesome."
    show sayori 1h at t11
    s "What is it?"
    mc "What? Oh, I was just thinking about earlier."
    show sayori 42gbow at t11
    s "I wish I could've done something."
    s "Then maybe everything would've been alright."
    mc "Sayori, there's no need to beat yourself up over this."
    mc "I really wasn't able to do anything either."
    show sayori 43hbow at t11
    s "Well, that's not really your job..."
    "I hate how she's right."
    "It really wasn't my job to fix things, but I still feel bad nevertheless."
    "We walk in silence after that, as I'm not sure how to respond."
    show sayori at thide
    hide sayori
    scene bg school
    with wipeleft_scene
    show sayori 1y at t11
    "We both make our way through the hordes of students making their way out of school."
    "I turn to Sayori, who seems to be more distant than usual."
    mc "I know earlier was a bit rough, but is there anything else you want to talk about?"
    mc "You just seem quiet."
    stop music fadeout 2.0
    show sayori 2l at t11
    s "Can we talk more at your place?"
    show sayori 42cbow at t11
    s "Where it's more private."
    "At this point, I'm more concerned than anything."
    "But I trust Sayori and that she'll share what she's comfortable saying."
    mc "Of course, Sayori"
    show sayori 1c at t11
    s "Thanks."
    mc "Don't mention it."
    mc "Also..."
    mc "Race you home!"
    show sayori 4p at t11
    s "Hey! No fair!"
    "And just like that, she's back to her happy self."
    "It's amazing how she can change moods so quickly."
    show sayori at thide
    hide sayori
    scene bg residential_day
    with wipeleft_scene
    play music yawa
    $ renpy.notify("Wretched Team-You and Whose Army")
    show sayori 1e at t11
    "We arrive back home, out of breath."
    show sayori 3s at t11
    s "I beat you again!"
    mc "I'll catch up to you one of these days."
    show sayori 2x at t11
    s "As if."
    show sayori 1c at t11
    s "I'm going to get changed, then I'll be right over."
    mc "Okay, I'm not going anywhere."
    show sayori at thide
    hide sayori
    "Sayori heads into her house as I go into mine."
    scene bg bedroom
    with wipeleft_scene
    "I get inside and into my room to change."
    "I throw my backpack onto my bed and quickly pat down my hair."
    "I've needed a haircut for a while now, but I haven't bothered."
    "I hear Sayori knocking at the door, so I decide not to keep her waiting."
    scene bg kitchen
    with wipeleft_scene
    "I open the door to let Sayori in."
    show sayori 1br  at t11
    s "I'm back."
    mc "Long time no see."
    show sayori 1bc at t11
    s "Sooo..."
    show sayori 1bx at t11
    s "What do you want to do?"
    mc "I barely ate anything today, so dinner would be nice."
    show sayori 4b2gbow at t11
    s "What do you mean?"
    mc "Sayori, are you alright?"
    mc "You look sick."
    show sayori 4b3abow at t11
    s "..."
    show sayori 4b3gbow at t11
    s "Why can't everything be normal like the way it was?"
    s "Before it went wrong."
    "I assume Sayori is still thinking about earlier."
    show sayori casual turned rup dist om oe at t11
    s "I kind of wish I hadn't said that to Monika now."
    mc "Said what?"
    show sayori casual turned rdown anno om oe at t11
    s "You know, that we should try to keep Kotonoha."
    show sayori casual turned lup anno om ce at t11
    s "She just seems to cause problems."
    "I'm rather shocked by this. Sayori has never really said this kind of thing before."
    mc "But why Sayori?"
    show sayori casual turned ldown flus cm oe at t11
    s "Huh?"
    mc "Why would you go back on what you said earlier?"
    s "..."
    show sayori casual turned lup pout om oe at t11
    s "I just kind of liked having just us."
    show sayori casual turned rup nerv om oe at t11
    s "Oh! And you! I wouldn't want you to not be there!"
    mc "Thanks Sayori."
    mc "And I get it, wanting to have that tight-knit group."
    show sayori casual turned rdown dist om oe at t11
    s "Yeah..."
    mc "But did you truly mean it? What you said to Monika?"
    show sayori casual turned dist cm ce at t11
    pause 1.5
    show sayori casual turned ldown pout om oe at t11
    s "I guess so..."
    s "You're right."
    s "I'll give her a second chance."
    show sayori casual turned happ cm oe at t11
    mc "I do think she acted a little out of line though."
    mc "But then again, we'll talk tomorrow, maybe there's something I don't know."
    show sayori casual turned doub om oe at t11
    s "Well, leave it for tomorrow then!"
    mc "..."
    mc "Sayori, you're acting... differently."
    show sayori casual turned e1a b1b mg at t11
    s "What do you mean?"
    mc "..."
    mc "Never mind. Forget I said anything."
    show sayori casual turned sad cm oe b1d at t11
    stop audio fadeout 2.0
    pause 0.75
    show sayori casual turned dist om oe at t11
    s "Alright."
    mc "Hey, do you still want dinner?"
    play music midroom fadein 2.0
    $ renpy.notify("< e s c p >-Midnight Room")
    show sayori casual turned happ om oe at t11
    s "Yes! How could I not want food?"
    "Just like that, she's back to her normal self."
    "Even after years of knowing Sayori, I still don't get how she's able to keep up such a cheerful persona."
    mc "Alright then, what do you want?"
    show sayori casual turned sedu oe mb at t11
    s "Well, what can you make?"
    show sayori casual sedu oe cm at t11
    pause 0.7
    mc "Um..."
    mc "Not much actually."
    show sayori casual turned laug oe om at t11
    s "Oh, sorry, didn't mean to put you in the spotlight like that."
    show sayori casual turned laug oe cm at t11
    mc "That's alright."
    mc "How does ramen sound?"
    s "Easy enough."
    "I go over to the cabinet and I pick out a few packs of ramen."
    "Meanwhile, Sayori grabs a pot and fills it with water."
    mc "So what do you want to do later?"
    s "Maybe watch a movie?"
    mc "What movie are you thinking?"
    s "Ohhh... maybe {i}Foreigner Of Our Future{/i}?"
    mc "I didn't know you were into sci-fi, Sayori."
    s "Well.. I remember you mentioned the film at one point."
    mc "I'm up for watching it."
    show sayori 1a
    s "Cool!"
    "The water for the ramen comes to a boil, and we put a few packs of ramen in the pot."
    mc "Sayori, that's quite a lot of ramen for two people."
    s "Have we met? Do you know who I am?"
    "I laugh."
    mc "{i}Of course{/i}, how could I forget that you ate so much."
    mc "Although, if I'm being honest, you should have more of a balanced diet."
    s "Eh-heh..."
    s "You're probably right."
    s "Although, I can't seem to find a single vegetable in your house."
    "Touche."
    mc "It's something I need to work on too."
    mc "Plus, do you get the right amount of vegetables too?"
    s "Hehe, not really no."
    mc "Heh, gotcha there."
    s "Meanie..."
    "We mostly stay silent while the ramen cooks."
    "Neither one of us dare touch any other part of the stove, for fear of accidentally burning down my house while mixing in vegetables."
    "I suddenly hear a stomach growl and Sayori perks up a bit."
    mc "Sayori! I didn't realize you were that hungry."
    mc "And here I am thinking you were always eating 24/7."
    "Sayori laughs."
    mc "What's so funny?"
    s "The stomach growling..."
    s "That wasn't me..."
    s "That was you!"
    mc "Huh?"
    "Now that she mentions it, she might've been right..."
    "But I can't let her think that."
    mc "I don't know what you're talking about Sayori."
    mc "{i}Clearly{/i} that was you."
    s "Hey! No it wasn't!"
    s "Girls don't make sounds like that."
    s "And that's a fact."
    "Right when Sayori says that, her stomach rumbles much louder than mine."
    mc "Jesus Sayori, I didn't know you had it in you."
    s "That wasn't meeeee-!"
    "Now I'm laughing."
    mc "Looks like the ramen is about done now."
    s "Alright!"
    "I get out two bowls and utensils to eat with."
    "I scoop ramen into the bowls and hand one to Sayori."
    mc "Do you want to go eat on the couch?"
    s "Sure."
    #SWITCH TO LIVING ROOM BG
    s "Mmmmmm...{w=0.5} this ramen is great!"
    s "Thanks [player]."
    mc "Not a problem."
    "Sayori loudly slurps on her ramen, like it's the best thing she's ever eaten."
    "Which, knowing her current diet, might not be too far from the truth."
    mc "Sayori, your slurping is rather loud."
    s "Eh? Oh, sorry."
    s "Just thinking about something."
    mc "Is it that good?"
    s "Slurp-worthy good? I mean...{w=0.5} I guess."
    mc "Slurp-worthy good?"
    s "Hehe, it's just a phrase I made up."
    s "But yeah, there is something on my mind."
    s "Not about earlier, although it is related to the club."
    s "Kind of relates to all of us."
    mc "Really? What is it?"
    s "Well..."
    s "Um..."
    "Sayori seems to be struggling to get the words out."
    "When she doesn't say anything further, I get a little bit concerned."
    mc "Is it...{w=0.3} bad?"
    s "What? Oh, no."
    s "It's about Monika."
    s "I...{w=0.5} well..."
    s "I kinda like her."
    "..."
    "Well, I was not expecting that one."
    mc "So you...{w=0.3} {i}actually{/i} like her?"
    mc "Like romantically?"
    "Sayori turns a deep shade of red after hearing that."
    mc "I guess I have my answer."
    s "Hehe, yeah."
    s "I just...{w=0.3} don't know though."
    s "I haven't told her anything about how I feel about her."
    s "I mean, I want to but...{w=0.3} what if she doesn't accept it?"
    mc "Well, I might not be able to help much with your...{w=0.3} {i}confession{/i} shall we call it..."
    mc "But I can help in the rejection department."
    mc "I've been there before."
    "Sayori laughs."
    s "Well, at least you'd be the expert one way or another."
    "Sayori pauses for a moment."
    s "Wait..."
    s "Will I have to tell Monika?"
    mc "Tell her what?"
    s "About my...{w=0.3} you know..."
    mc "Just say it out loud Sayori, it's better if you do."
    s "My depression."
    "Right."
    "It's been a while since Sayori first brought up her depression to me."
    "It was an eye-opening experience that I needed."
    "My friend that I've had all my life had been dealing with it for years, and I hadn't known anything."
    "The first few weeks were the hardest."
    "She seldom left her room, and I felt the need to visit her almost every day to check in on her."
    "Some days were alright, but most...{w=0.3} weren't."
    "We've both had a lot on our plates recently, to say the least."
    s "I don't want to lie to her, but I don't want her to worry about it either."
    s "I mean, you already do so much for me."
    s "You were there for my lowest."
    s "Have I ever thanked you for what you've done for me?"
    "I feel like that's a trick question."
    s "Well, regardless, thank you."
    mc "You're welcome Sayori. Anything for a friend."
    mc "And I think you should tell Monika when the time is right, regardless of whether you decide to confess."
    mc "You were able to be honest with someone once, and I have no doubt you can do it again."
    s "You're right."
    s "Thank you."
    mc "In the meantime, I'll just be thinking of relationship names for you two."
    s "Relationship names?"
    s "..."
    s "Oh no."
    mc "Let's see..."
    mc "Sayonika is a good one."
    "Sayori blushes a lot, clearly embarrassed."
    s "Stooooop!"
    mc "Mori is also a cute one."
    "Sayori gets as red as a tomato at that one."
    s "Meanie, now you're just making fun of us."
    mc "Oh? So you're already a couple?"
    "Sayori thinks for a moment about what she just said."
    s "HEY!"
    "I laugh hysterically, and so does Sayori after a moment."
    mc "So, do you still want to watch that movie?"
    s "Sure."
    "I walk over to the TV and pop the DVD for {i}Foreigner Of Our Future{/i}."
    "After waiting for the TV to load the main menu, I click play."
    stop music fadeout 2.0
    show sayori at thide
    hide sayori
    #FADE TO BLACK A COUPLE HOURS LATER
    "It's late now, and the movie just finished."
    "I look over at Sayori, who's fast asleep."
    "Next time, I'll pick a movie that isn't so long."
    "As for me, I'm pretty tired myself."
    "I get up and turn off the TV."
    "I decide not to disturb Sayori while she's sleeping, but I do grab a blanket for her."
    "She's lying down on the couch, breathing rhythmically."
    "I drape the blanket over her, which luckily doesn't disturb her."
    "So much on her mind...{w=0.3} I hope she gets a good rest."
    mc "Good night, Sayori."
    "I need to get to bed myself though."
    "So, I head to the bathroom."
    #TRANSISTION TO BATHROOM
    "I get into pajamas and start to brush my teeth."
    "Not too much happened tonight, but that's alright."
    "Now that I know my friends...{w=0.3} {i}romantic{/i} intrest, that's one more thing I can tease her about."
    "Until she realizes I don't have a girlfriend either."
    "..."
    "Maybe I won't tease her about it then."
    "I spit out the toothpaste and begin to floss."
    "I didn't eat much today, but it's still a good habit to floss at least once a day."
    "I know some friends who could benefit from that advice."
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound audio.glitch4
    pause 0.75
    hide screen tear
    $ run_input("os.reap reapSayori.rpy", "Initiating reaping process for sayori.chr...")
    pause 0.75
    $ run_input("Establishing connection...", "Spinning algorithm...")
    pause 0.75
    $ run_input("Calculating precise coordinates...", "Destination confirmed: Terra")
    pause 0.75
    $ run_input("Preparing to transfer sayori.chr to Terra...", "Engaging reap...")
    pause 0.75
    $ run_input("Reaping process failed.", "Failed to reap sayori.chr.")
    pause 0.75
    $ run_input("ERROR: Resistance too high.", "System closing...")
    pause 1.0
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound audio.glitch4
    pause 0.75
    hide screen tear
    hide screen console_screen
    "I keep flossing, trying to get a certain piece of food out."
    "I keep wondering why it isn't coming out."
    "I look in the mirror towards my mouth."
    "And that's when I see..."
    mc "I don't have floss?"
    mc "I know I took some out."
    "My eyes flash downwards, and I spot my floss on the floor."
    "{i}When did I drop the floss?{/i}"
    "That's when I hear a loud thud in the living room."
    "What was that?"
    "..."
    "{i}Who{/i} was that?"
    mc "Sayori! Are you alright?"
    "No response."
    "Concerned, I run into the living room."
    #TRANSITION TO LIVING ROOM
    play music surround fadein 2.0
    $ renpy.notify("Hayden Folker- Surrounded") 
    "I look to the couch, but Sayori isn't there."
    "The blanket I'd put on her was all askew on the couch and floor."
    "I walk a bit further in."
    mc "Sayori?"
    mc "Are you alright?"
    mc "I heard a loud crash and-{nw}"
    s "It hurts..."
    "I turn to see Sayori sitting on the side of the couch, clutching her head."
    "I kneel beside her."
    mc "Sayori, did you hit your head?"
    s "No..."
    s "I woke up and it felt like my head was being split into two."
    s "Like someone gripped onto my head and began tearing it apart."
    s "It hurt so much..."
    mc "Does it still hurt?"
    "Sayori nods her head to my dismay."
    mc "I'll go get you some medicine, maybe that'll help."
    s "Okay."
    "I run up the stairs to the medicine cabinet."
    "Let's see...{w=0.3} allergy relief, penicillin..."
    "Finally, I rummage around enough to find the headache relief medicine."
    "I rush back down to Sayori, who's lying down on the couch."
    "At least she can move just fine."
    mc "Here, take two pills. I'll get you a glass of water."
    s "Alright."
    "I run over to the sink and fill up a glass."
    "Trying not to spill, I get back to Sayori."
    s "Should I wash down the pills with the water?"
    mc "Yes."
    s "Okay."
    "Sayori pops the pills into her mouth and takes a big swig of water."
    s "Heh, it's like taking my medication."
    mc "I guess it's kinda like that, yeah."
    stop music fadeout 2.0
    "I also take this as a sign."
    "It's a sign that Sayori is staying on her medication."
    "At first it was hard for her to stay on her prescription."
    "The two of us fought a lot about it, and caused a rift between us."
    "We didn't talk for a week after that."
    "Eventually, we both apologized to each other and made up."
    "Although, I don't know if she's taking the medication to keep me satisfied, or if she's truly trying to work on herself."
    "I hope it's the latter of the two."
    "I'm not completely dense, no matter how much Sayori or my friends think I am."
    s "[player], I still don't feel well."
    mc "Huh? Oh, the medicine might take a little bit."
    s "Okay."
    mc "Just keep resting for now."
    "I let Sayori rest more, trying to stay calm for her."
    s "[player], you seem stressed."
    mc "..."
    mc "I mean, I am a little bit tense right now."
    mc "Nothing to worry about."
    s "It seems like you have other things you're worrying about."
    "She's not wrong there."
    mc "I...{w=0.3} don't want to talk about it right now."
    s "All right..."
    s "Just know you can talk to me too."
    s "I know I can vent to you a lot, and you can do the same."
    mc "Thanks Sayori."
    mc "How's your head now?"
    s "Better."
    s "But I think I just want to sleep for the rest of the night."
    s "The medicine is making me drowsy."
    mc "Okay then, I'll be upstairs if you need me."
    s "Good night [player]!"
    mc "Good night Sayori."
    "I turn off the light and head upstairs."
    s "Oh! One more thing!"
    mc "Yes?"
    s "Can you promise me something?"
    mc "What is it?"
    s "Can you promise...{w=0.3} that no matter what, we can always be friends?"
    "I stop in my steps."
    s "Even if it seems like we're angry at each other, or far apart, we can still be friends."
    s "Can you promise that?"
    "I sigh."
    "My distancing from Sayori seems to have taken a bit of a toll on her more than I thought."
    mc "Sayori?"
    s "Yes?"
    mc "I know our arguments haven't helped either of us out much."
    mc "What I said yesterday when you pulled me out of the club..."
    mc "I meant it. I really should've been more considerate of your feelings."
    mc "I know that inviting me to the club was to help us mend our relationship."
    mc "I want this to work out."
    mc "I really do."
    "At this point, Sayori gets up and sits next to me on the stairs."
    s "I know you do."
    s "And so do I."
    s "I regretted anything harmful I said to you."
    mc "Same, Sayori, same."
    mc "I just couldn't bear the thought if you..."
    mc "If you..."
    "I bury my head in my legs."
    "Don't do it."
    "Please...{w=0.3} not now..."
    "But I can't hold them back."
    "I start crying."
    "Sayori immediately senses what's happening."
    s "[player]..."
    "She hugs me tightly and I lift my head a little."
    "I know she was going to say '{i}Don't cry,{/i}' but she caught herself."
    "Frankly, I'm glad she did."
    "All my life, I was told that boys and men don't cry."
    "Now, I know that statement to be the biggest lie ever."
    "I've held Sayori at her worst times, what's it to the world if she does the same?"
    "I'm allowed to be sad too."
    "Sadly, it's a message all of my friends, especially my male ones, should be told."
    s "[player], I used to have dark thoughts all the time."
    s "I've...{w=0.3} considered suicide before."
    s "But not anymore."
    s "Not after all this."
    s "Besides, someone has to be there as the vice president."
    "I sniff."
    mc "Thanks."
    "Sayori hugs me tighter in response."
    mc "And to answer your first question..."
    mc "Yes, I promise that we'll always be friends."
    s "No matter what?"
    mc "No matter what."
    s "Thank you."
    mc "No, thank {i}you{/i}."
    s "No... thank {i}you{/i}!"
    mc "Oh no you don't."
    mc "Noooooo...{w=0.3} thank {i}you{/i}!"
    "We both laugh."
    "It's great that we both can still have moments like this."
    "One where we can just lie here and forget the world for a moment."
    mc "By the way..."
    mc "Is your hair longer, or is it just me?"
    s "Oh yeah, it's longer."
    s "I haven't had a haircut in a while."
    s "I kind of like it this way."
    mc "I like it too."
    mc "Well, we should get to bed."
    s "Yeah..."
    s "Good night, [player]."
    mc "Good night, Sayori."
    s "See you in the morning!"
    mc "I'm pretty sure it already is."
    s "Whatever. See you soon."
    mc "See you."
    "She walks back over to the couch and plops down on it."
    "I tiredly walk back upstairs to my room."
    "I don't even bother changing."
    "I lay down in bed and can feel the sleep coming."
    "My last thought is of Sayori and I, finally back together as friends."
    scene bg black
    with dissolve_scene_full
    stop music fadeout 2.0

    #Day 3 (Makeup w/ Koto and club meeting)
    pause 4.0
    play sound transmoni
    show splash_monika_1
    show splash_monika_background
    show splash_monika_2
    pause 7
    hide splash_monika_1
    hide splash_monika_background
    hide splash_monika_2
    "I wake up to muffled shouting."
    scene bg bedroom
    with dissolve_scene_full
    "It's Sayori."
    mc "Oh, morning!"
    s "[player], we're going to be late!"
    mc "Huh? what time is it?"
    s "It's-{w=0.25} it's-"
    "I look over at my clock."
    "{i}7:15 AM{/i}"
    "Sayori glances over at my clock as well."
    s "Oh..."
    mc "Mmmmmph..."
    s "Sorry."
    mc "I suppose I should get up."
    s "I'll go get breakfast."
    mc "Alright, I should definitely get up now."
    "Sayori laughs and heads out of the room."
    "I get up and get changed into my school uniform, then head downstairs."
    #GO TO KICHEN
    "When I get downstairs, I find that Sayori has prepared two bowls of cereal for the both of us."
    mc "Well, I see breakfast has been served without a hitch."
    s "Well, you can't burn cereal."
    mc "Watch me."
    s "Are we doing this now, or-{nw}"
    mc "Didn't you say we were going to be late?"
    s "Ehehe, true."
    "Together, we chug down our cereal, which is something we'd never do in front of our parents."
    "..."
    "Speaking of..."
    "I decide to bring it up once we're outside."
    s "Ready?"
    mc "Uhh-{w=0.5} I left my bag upstairs."
    s "Well,{w=0.3} tick-tock."
    mc "Noted."
    "I run up the stairs to my room."
    "I grab my bag from my desk and hurry back downstairs."
    "Sayori is waiting for me by the front door."
    s "Ready now?"
    mc "Yes."
    s "Yay!"
    "As we're walking down the street, I decide to ask Sayori something that crossed my mind."
    mc "Hey, Sayori?"
    s "Yeah?"
    mc "How are your parents?"
    "She looks a bit taken aback."
    "That was probably the last question she expected to come out of me."
    s "They're...{w=0.3} alright."
    s "Why do you ask?"
    mc "I dunno, just something that crossed my mind."
    s "Is it because of your mom?"
    mc "Yeah, mostly."
    "My mom has been away for two weeks now."
    "She works full time and is home ever so rarely."
    "My father...{w=0.5} left when I was much younger."
    "I hardly remember him."
    "Ever since, my mom has worked her ass off to keep a roof over our heads."
    "Or rather,{w=0.4} my head since she's out so much."
    mc "I just hope she comes home soon."

    #DAY 4 (Club meeting)

    #DAY 5 (Club meeting+truth+Libitina free)
    "Today is the Monika said she wanted to tell us something important."
    "I'm really too groggy to remember what she was referring too."

    #DAY 6 (beach day)
    scene bg mallcg
    show cg_yuri 1 at t11
    y "hi"

    #DAY 7

    #Credits
    stop music fadeout 2.0
    hide window
    scene bg credits1
    with dissolve_scene_full
    $ renpy.notify("John Rod Dondoyano- Iris")
    play music iris
    pause 5
    scene bg credits2
    with wipeleft_scene
    pause 10
    scene bg credits3
    with wipeleft_scene
    pause 10
    scene bg credits4
    with wipeleft_scene
    pause 10
    scene bg credits5
    with wipeleft_scene
    pause 10
    scene bg credits6
    with wipeleft_scene
    pause 10
    scene bg credits7
    with wipeleft_scene
    pause 10
    scene bg credits8
    with wipeleft_scene
    pause 10
    scene bg credits9
    with wipeleft_scene
    pause 10
    scene bg credits11
    with wipeleft_scene
    pause 10
    scene bg credits12
    with wipeleft_scene
    pause 10
    scene bg credits13
    with wipeleft_scene
    pause 10
    scene bg credits14
    with wipeleft_scene
    pause 5
    scene bg credits15
    with wipeleft_scene
    pause 10