init:
    $ buttonpop = False

label start:
    stop music    

    $ mc_name = "Shaun"
    $ _game_menu_screen = "navigation"

    $ mc_gender = 1
    $ mc_clothes = 0

    $ charlie_love = 0
    $ demon_love = 0

    $ shira2 = False
    $ shira4 = False
    $ shira5 = False

    $ friends = False
    $ charliekiss = False

    $ shira_endingopen = False

    scene bg black with dissolve

    jump introduction


label introduction:
    play music "music/track09.ogg" fadeout 1 fadein 1
    scene bg black with dissolve
    scene scene1a with dissolve
    mc "By hoof and claw and tooth of minx."
    mc "With heart of griffin and mind of sphinx."
    mc "The tower falls, the clock it chimes. "
    mc "Bury the past—let this power be mine."
    mc "Let this power be mine. "
    mc "Let this..."
    scene scene1b with dissolve
    mc "A-aahh..."
    blank "Each motion of my hand draws the light through the air, magic surging forward from my core. "
    blank "It seeps through my arms, tingles in the tips of my fingers and bleeds outward. "
    think "Is it...?"
    blank "It wells within me like a shadow, dark and static as it lifts each hair along my arms and the back of my neck. "
    blank "The pages beneath my hand flutter and send plumes of dust into the growing light. "
    blank "Arcane energy rises in me, an entity of its own, something hungry and wild howling through my being."
    blank "A wind that shakes my very bones. " with vpunch
    think "I...I've never felt anything like it. "
    think "It's working! It's actually working!"
    think "It-" with hpunch
    blank "But the beast rages against me, against my control, as the light begins to dance. "
    think "I'm...I'm not doing this...I.."
    scene bg white
    scene scene1c with dissolve
    blank "The lights blinding. Vivid. "
    scene bg white
    scene scene1c with dissolve
    think "It's too strong. I can't..."
    think "I can't control it!!"
    scene bg white
    scene scene1c with dissolve
    scene bg white
    scene scene1c with dissolve
    blank "My hands shake. My last thread of restraint begins to snap as it tears through me. "
    scene bg white
    scene scene1c with dissolve
    think "It's too strong!!!"
    scene bg white
    scene scene1c with dissolve
    scene bg white
    scene scene1c with dissolve
    mc "AUUGHHHHHHHH!!!!"
    scene bg white with dissolve
    blank "...."
    blank "..."
    blank ".."
    play music "music/track02.ogg" fadeout 1 fadein 1
    scene bg black with dissolve
    aureman_unknown "Miss? "
    aureman_unknown "...Miss, are you alright? "
    blank "A persistent tapping nudges my shoulder. "
    think "Ugh..."
    think "What...?"
    scene bg black with dissolve
    scene library_day with dissolve
    show aureman at m1 with dissolve
    aureman_unknown "Get up, please. "
    aureman_unknown "You aren't allowed to sleep in here. "
    $ auremanface = 'happy'
    show aureman at m2 with dissolve
    aureman_unknown "More to the point, you really aren't allowed to be in here at all, unless you have the right permission. "
    aureman_unknown "These are private grounds. "
    think "My head is killing me..."
    think "Have I been drinking? Where am I? "
    think "And who the hell is this old guy? "
    $ auremanface = 'neutral'
    show aureman at m1 with dissolve
    aureman_unknown "Don't forget your things. "
    blank "He saddles me with a bag across my shoulder like I'm a pack mule. "
    $ auremanface = 'happy'
    show aureman at m2 with dissolve
    aureman_unknown "Come along now. "
    blank "My feet move, one in front of the other, even as my eyes drift. "
    think "Okay...Okay, I might be hungover. Try not to look hungover. "
    $ auremanface = 'neutral'
    show aureman at m1 with dissolve
    aureman_unknown "My, you're a heavy sleeper, aren't you? "
    aureman_unknown "I have to say, I felt a little guilty waking you, but better I find you than someone else. "
    $ auremanface = 'annoyed'
    show aureman at m2 with dissolve
    aureman_unknown "They might not be so lenient. "
    think "Lenient? "
    aureman_unknown "For now, this is our little secret. "
    $ auremanface = 'happy'
    show aureman at m1 with dissolve
    aureman_unknown "No need to get the guard involved, if you ask me. "
    blank "He punctuates his good-natured laugh with friendly pat on the shoulder. "
    blank "Blinding light spills into my eyes as he opens a door with a creak and a shudder of magic. "
    scene bg white with dissolve
    aureman_unknown "Have a good day, child. And find better places to sleep!"
    scene city_day with dissolve
    think "Oh, damn, it's like the sun is pissing in my eyes. "
    blank "I squint at him as he shuffles off back inside the building. "
    think "Huh. "
    think "Weird. "
    think "I guess he was a Mage..."
    think "...Mage..."
    think "MY TRIAL!"
    think "OH GOD, I'M PROBABLY LATE!"
    think "DID THE SPELL WORK!?"
    blank "A thousand thoughts break through my mind at once, the word Mage the single flake of snow that set off an avalanche in my head."
    blank "Above the city stands the Academy; a proud building, ornate and ancient."
    blank "One of the firm pillars of the capital city, a proving ground for those who would pursue a magical career. "
    think "The career I want. "
    blank "I push myself in that direction, my legs feeling weak."
    think "I have to get there. "
    think "I can't miss this..."
    think "I can't..."
    blank "I run through the early morning streets, dodging people along the way. "
    think "None of this would have been necessary if they'd just accepted me when I showed up!"
    think "Three days I've waited around for a trial. An actual trial. With a real Mage or Magi. "
    think "I thought just proving I could harness magic would guarantee me a place, just to learn, but..."
    think "Ugh, this is all so stupid!"
    blank "Doubt nags at the back of my mind. "
    think "Of course they wouldn't accept just anyone. It's the most prestigious magic school in the kingdom. "
    blank "And if I thought I was good enough by my own merit, would I have done what I did last night? "
    blank "Would I have broken into the Sorcerer's Archives just to try and make myself stronger? "
    think "It's...it's not cheating, it's just being determined!"
    think "What if I didn't pass? What if they sent me home as a failure? "
    think "I couldn't risk that. I couldn't. "
    blank "My feet pound against the cobblestone, the building growing impossibly larger the closer I get. "
    think "Please don't let me be late..."
    think "On top of everything else that's happened..."
    blank "Barrier after barrier. I feel the magic sliding over my skin as I run past. "
    scene bg black with dissolve
    scene entrance_day with dissolve
    blank "The last barrier between me and my entrance exam. The large doors stand closed and unmanned. "
    think "These were open the last time I was here..."
    blank "I pull on the thick handle, but the door holds resolutely, its weight shuddering against my best attempts. "
    think "Let me in!"
    blank "The knocker is heavy as I rap it against the wood. "
    blank "I blink a few times before I notice it, letters appearing before my very eyes. "
    blank "The words appear to etch themselves into the door itself. "
    blank "YOU HAVE BUSINESS HERE. "
    blank "ENTER. "
    think "...O-oh, of course. It was just magicked. "
    think "Hah. Of course. I definitely knew that. "
    blank "I give a confident tug on the door...which stays stuck and nearly rips my arm off with it. "
    think "Are you kidding me!?"
    think "I'd love to enter, jerk off!!"
    think "LET. ME. IN!!"
    blank "I slam my palm against the wood. "
    blank "...Or I try. Instead, I go stumbling into thin air, falling over my own feet with all the grace of a hobbled cow. "
    blank "I fall straight through the door. "
    scene bg black with dissolve
    scene entrance_interior_day with dissolve
    blank "Annnnd slide right onto my face, against a rug that feels like it was made from boar hair. "
    mc "Haaaahhh!! Hah-hah-oww!!"
    think "Th-that burns. "
    think "My face is on fire. My face is LITERALLY on fire. "
    think "I massage my cheeks. Even the tears stinging in my eyes would be a relief. "
    think "Wait a second..."
    blank "I scramble to my feet, realizing exactly where I am. "
    think "Any, uh...any important Sorcerers around? Mages? "
    think "No?"
    blank "The foyer is vast and empty, the school's massive structure shrouded in a heavy silence. "
    blank "Only the hum of magic buzzes on the edge of my awareness. "
    mc "Phew..."
    think "Good. No one saw that. "
    blank "I clear my throat, seeming to have lost my voice. Probably from still being so groggy. "
    blank "Actually, that's a perfectly good explanation for all of this. I should be sharper than this. "
    blank "How am I going to pass the entrance test and become an Initiate if I can't even handle the damn DOOR?"
    blank "Trying to gather my wits, my eyes are drawn to a large clock on the wall. "
    think "Good. I still have a little time. "
    blank "I pick up the bag I dropped and toss it over my shoulder again. "
    think "I need to find somewhere to change..."
    think "I can't show up in my nightclothes. "
    scene bg black with dissolve
    scene hallway with dissolve
    blank "Wandering down a hallway, I try to keep my sense of direction. "
    blank "The building isn't just large, but convoluted in design, built to twist the senses around for those that aren't equipped to navigate it. "
    blank "I've heard enough stories of this place to know. "
    think "Leeeet's not think about my odds of finding a bathroom in this place. "
    think "I'd use a closet or something...if I could tell which of these doors were closets!!"
    think "Ugh. Please. "
    blank "And then, miracle of miracles, I see the standard open-entryway of a bathroom, a generic male symbol by the door. "
    scene bg black with dissolve
    scene toilet with dissolve
    blank "Another boy leaves, giving me a long stare as I walk past him. "
    blank "I nod to him as pleasantly as I can manage. "
    think "I bet I have carpet burn on my freakin' face. "
    blank "And I shouldn't be running around here in my nightclothes!"
    think "This is the kind of impression I'm going to give my peers..."
    blank "I toss my bag onto the counter and then glance up into the mirror. "
    scene bg white with vpunch
    scene scene2a with hpunch
    $ mc_clothes = 5
    mc "AAAAAAHHHHHHHHHHHHH!!!"
    blank "My hand clamps over my own mouth, muffling the horrible, high-pitched sound that comes out of it. "
    think "WHAT!?!"
    blank "My own shocked face stares back at me, but...but it's not mine!!"
    blank "I touch my cheek, watching as a more feminine hand rises to touch my face. "
    blank "I stare down at my palms. My chest. My thighs. "
    think "B-b-b-but how!?"
    mc "I... "
    think "Either I just now developed self-awareness after seventeen years of being alive, or something is really, really wrong!!!"
    think "M-m-maybe it's the mirror. A PRANK!"
    blank "I glance down at my own chest again, my chest now the opposite of flat and ruining my brief moment of insane hope. "
    think "But why is this happening!? Why..."
    scene scene1d with dissolve
    scene scene2a with dissolve
    think "The spell. "
    blank "The realization hits me like a brick. My new knees threaten to sway right out from under me. "
    mc "Oh nooooo. "
    think "I knew I lost control of it, but...but I just thought it didn't work!!"
    think "I didn't realize...how did I not realize!?"
    scene scene2b with dissolve
    blank "Still gaping at my own reflection, I pat myself down in shock. "
    think "It...It feels so real. "
    blank "My unhelpful minds informs me that's because it IS real. "
    blank "Stealing a furtive glance around, I cup my...my chest...and give them a little bounce. For science. "
    think "Woah..."
    think "No, don't get distracted!!"
    mc "I have to fix this!"
    blank "I screw up my face in determination...and am completely underwhelmed when nothing comes to mind. "
    think "My trial..."
    blank "It's all I can think about. "
    blank "Okay, not all, but it's ranking pretty high at the moment. "
    think "If I don't show up, there's no way I'll get admitted to the Academy. "
    blank "I stare into my face, set on a body just unfamiliar enough to be uncanny. "
    think "The trial...the trial has to come before everything. Even this. "
    think "But they're expecting a Shaun to show up! Not a.. a Sophie! "
    think "Okay...okay, I can fix this. I can fix this. "
    think "Less panic, more action. "
    scene bg black with dissolve
    scene toilet with dissolve
    blank "I wrangle my new body into my clothes...after doing a little inspection of things I'm not used to..."
    think "Ohh, that doesn't feel right..."
    think "Whatever. Ignore it."
    think "It'll have to do..."
    think "...This doesn't look convincing at all. "
    $ mc_gender = 2
    blank "I pull out the string that closes the waistband of my nightclothes and tie my hair up in it. "
    mc "I can pull this off, right? Just...act like this is how long you like to keep your hair. "
    think "And who can blame a guy for having a tiny waist? "
    think "Maybe I'm a vegetarian or something. They don't know. In fact, they'd be rude to ask!"
    blank "My mouth twitches into a frown, my poorly construed confidence crumbling easily. "
    think "...This is what you get for trying to cheat..."
    think "...Oh, whatever, I've got to go!"
    scene bg black with dissolve
    scene hallway with dissolve
    blank "Nervousness claws at my stomach as I make my way back to the main foyer. "
    think "As if things weren't hard enough already..."
    blank "I try to think past the fog of confusion clouding up my mind, completely thrown off-balance by all this. "
    scene bg black with dissolve
    scene entrance_interior_day with dissolve
    think "The trial is meant to take place in an arena within the school. An actual arena. "
    blank "My pulse picks up a faster beat at the thought. "
    think "But of course it's happening in an arena. Where else would it happen? "
    think "A back alley? "
    blank "Mocking my nerves doesn't do anything to actually quiet them. "
    think "Now...where did they say it was again? "
    blank "I follow the instructions that had been given to me, moving through the quiet hallways and toward the arena, ignoring the pulse in my throat. "
    scene bg black with dissolve
    scene arena with dissolve
    play music "music/track07.ogg" fadeout 1 fadein 1
    blank "The room is empty and dark. "
    think "Am I in the right place...?"
    blank "I step inside, staring across the expanse of the stadium."
    blank "The darkness is still unnaturally bright for how few torches line the walls. "
    blank "Where my sight should fail and fade into darkness, I can see clear across the room. "
    think ".....I wonder if this is where--"
    shira_unknown "Shaun. "
    blank "I spin around on my heel. "
    blank "The figure of a woman darkens the doorway, silhouetted by the halo of light at her back. "
    scene scene3a with dissolve
    blank "She steps closer, long and confident strides bringing her into view. "
    blank "I catch myself staring before I remember to bow. "
    think "Who is she...?"
    blank "I almost forget my manners, hastily coming up with something to say. "
    mc "Thank you for meeting with me. "
    blank "The words come out as a mumble as I try to keep my voice deep and pray she doesn't ask me too many questions. "
    blank "She returns the bow. "
    scene scene3b with dissolve
    shira "I am Magi Megan Shira, a representative and teacher at this Academy. "
    shira "I will be the one conducting your Trial of Initiation. "
    blank "A bead of sweat rolls down the back of my neck. "
    blank "I try to look as if I know exactly what that is, as if I've prepared for it my whole life. "
    blank "...And didn't just take some magic lessons from a crazy old Mage who wandered through town and smelled a little like mold. "
    shira "The trial is a trial by combat. "
    shira "I will warn you not to underestimate me simply because I'm a woman. You wouldn't be the first to make that mistake."
    think "Do I not look nervous enough for her liking? Does she want me to pee my pants, too? "
    shira "Your objective isn't to defeat me. What sort of Magi would I be if that could happen? "
    scene scene3a with dissolve
    blank "She smiles, the first human-like expression she's made since walking into the room, but her voice remains stiff. "
    blank "It's like she's speaking out of a manual. Then I realize how many times she's probably given these same instructions..."
    shira "But you will be expected to defend yourself. "
    shira "Though it's not your objective, you are allowed to attack. "
    shira "Any hits you manage to land against me will be taken into consideration in your favour. "
    shira "I won't hold it against you. If anything, I'd be very impressed. "
    shira "Do you have any questions? "
    blank "My thoughts are blank. Empty. Even if I had questions, I wouldn't know what they are. "
    blank "I shake my head. "
    shira "Very well, then. Shall we begin? "
    blank "The Magi steps further into the room. She moves delicately, each measured step taking her in a semi-circle around me. "
    think "I'm like her prey..."
    blank "I summon my will and my power into my hands, feeling the hot energy crackle between my fingertips."
    think "Simple defensive stuff. That's all I have to do..."
    blank "She stares me down, her face remarkably impassive, yet intent gleams in her eyes. "
    blank "I dig my heels into the ground, preparing myself for what's to come. "
    scene scene4a with dissolve
    blank "The lightening-quick motions of her hand summon a blast of power with remarkable speed. "
    menu:
        "Dodge":
            scene bg white with dissolve
            scene scene3b with hpunch
            blank "My instincts pull me away from the blast, knowing I don't have any time at all to summon a counter-spell."
            blank "The beam of ethereal magic barely glides past me, the aftershock ruffling my clothes and hair, but I stay on my feet. "
            blank "Magi Shira smirks. "
            shira "Rather good. Most new Initiates believe they have to only prove their magical prowess. "
            shira "They don't consider that physical skills are just as practical to a Magi's survival. "
            think "So I'm actually doing alright?"
            shira "...Of course, so are observational skills, and not getting distracted by your opponent's monologue. "
            blank "The bristle of magic at my back makes me gasp, as a shadow separates itself from the wall and breathes down my neck."
            menu:
                "Attack the shadow":
                    blank "I spin, my fingers flying through the air to summon a barrier between me and this creature. "
                    scene scene4b with vpunch
                    blank "But the tendrils of darkness snake around my wrists, interrupting the spell and causing me to thrash. "
                    shira "And very rarely is it wise to turn your back on your opponent. "
                    scene scene4c with vpunch
                    blank "The magic hums loudly as she summons it into her hands, building its power. I try to brace myself. Try to will a wall between us. "
                    blank "It's no use. "
                    blank "The arena flickers with a white light-- I can't see it coming, but I feel it. A heat from an arcane fire raging toward my back."
                    scene scene4d with hpunch
                    scene bg white with dissolve
                    jump aftertrial
                "Attack Magi Shira":

                    blank "I attack the puppeteer, not the puppet. "
                    scene scene4b with vpunch
                    blank "My hands weave together a spell, admittedly not a very powerful one, but quick. "
                    blank "Once light flickers and crackles within my control, I launch it toward Shira. "
                    scene scene3a with dissolve
                    blank "The tendrils of magic at my back recede as she quickly raises a defence against it. "
                    scene scene4e with dissolve
                    blank "The flame I threw at her simply flows into her hand like a toy."
                    blank "She laughs. "
                    shira "Not such a bad strategy..."
                    shira "But let's see some actual defensive spells. "
                    think "Huh? "
                    scene scene4f with dissolve
                    blank "She makes no pretence now, the fire dancing in her fingers, swirling into a ball that grows larger and larger. "
                    think "T-That's...how am I supposed to defend from that?!"
                    blank "My fingers fly together, muttering under my breath as I try to put together a barrier. "
                    scene scene4g
                    scene scene4f with dissolve
                    scene scene4g
                    scene scene4f with dissolve
                    scene scene4g
                    blank "The thin shield glistens in front of me, catching the light of Shira's power and reflecting it through the room. "
                    think "It...it won't hold. "
                    scene scene4f with dissolve
                    scene scene4g
                    think "I know it won't."
                    think "I know I can do better than this!!"
                    blank "But I expend the last of my magic into the barrier, bracing for the moment her spell strikes. "
                    scene scene4h with hpunch
                    blank "My eyes burn as she unleashes it. "
                    scene bg white with dissolve
                    jump aftertrial
        "Defend":

            scene scene4i with dissolve
            blank "I try to throw together a quick defensive spell as the light blinds me. "
            scene scene4j with dissolve
            scene scene4i
            scene scene4j with dissolve
            scene scene4i
            blank "I don't even get it fully summoned. "
            scene scene4k with vpunch
            blank "The spell hits me squarely in the chest, full-force. "
            blank "It knocks the breath right out of my lungs and my feet leave the ground, sending me spinning."
            scene bg white with dissolve
            jump aftertrial

label aftertrial:
    scene bg black with dissolve
    play music "music/track01.ogg" fadeout 1 fadein 1
    blank "......"
    blank "......"
    think "Nng...Ow..."
    scene scene5a with dissolve
    think "So that...that didn't work..."
    blank "My head throbs lamely. "
    $ achievement.grant("secretuncovered")
    blank "A gentle hand touches my shoulders, rousing me up from my crumpled state on the hard ground. "
    shira "Maybe I was a little overzealous. "
    scene scene5c with dissolve
    blank "When I open my eyes, my chin is tilted toward my chest...giving me a clear view of my ripped outer jacket and shirt, revealing far too much."
    think "Oh no!!"
    scene scene5b with dissolve
    blank "I jolt awake, my hands scrambling to cover myself up. "
    scene arena with dissolve
    show shira at m1 with dissolve
    shira "Are you alright? "
    mc "I-I'm fine!"
    $ shiraface = 'happy'
    $ shirapose = '2'
    show shira at m2 with dissolve
    shira "That's a relief. For a moment, I thought I may have seriously injured you. "
    $ shirapose = '1'
    show shira at m2 with dissolve
    shira "Here. "
    blank "With kinder motions than I would have expected from her, she guides me up into a sitting position. "
    shira "I'm glad you're unharmed."
    $ shiraface = 'neutral'
    show shira at m1 with dissolve
    shira "So the only question that remains is...who are you?"
    mc "I...um...wh-what? "
    shira "I was told I would be testing a young man named Shaun, who wished to become an Initiate here. "
    shira "So who are you? "
    mc "I- I am Shaun!!"
    $ shiraface = 'annoyed'
    show shira at m2 with dissolve
    blank "She peers at me closely, some of that strict, authoritarian gleam entering her eyes again. "
    $ shirapose = '3'
    show shira at m1 with dissolve
    shira "I will give you one chance to recant that. "
    mc "B-but it's true, I--!! "
    think "I-I have to tell her. She's not going to believe me otherwise. If I haven't already ruined my chances, that certainly will!"
    blank "I take a steadying breath. "
    mc "I really am Shaun, Magi Shira. But this...this isn't how I usually look. "
    mc "I was um...I was trying to utilize a spell when, when it must have backfired and..."
    blank "I gesture helplessly to myself. "
    mc "Yeah..."
    think "Eloquent..."
    blank "Her eyes never lose their investigative gleam, picking over me until I'm starting to get red in the face. "
    $ shirapose = '1'
    show shira at m2 with dissolve
    shira "And when did you conduct this spell? "
    mc "L-Last night. "
    blank "A thin eyebrow arches in my direction, spreading scepticism across her face. "
    $ shirapose = '3'
    show shira at m1 with dissolve
    shira "And what was the intention of this spell?"
    mc "......."
    think "She already knows, doesn't she? "
    think "At this point, I think I might be on the verge of getting arrested rather than admitted."
    mc "I...I had..."
    blank "My voice diminishes in my throat, sound extra pathetic with its new pitch. "
    mc "I first learned magic from a traveling mage, ma'am. He said I showed promise. "
    mc "He said I could pursue that here. "
    mc "I thought there was no way I would match up to city Mages who had grown up around this sort of magic, who had learned it all their lives..."
    mc "So I tried to magnify my own power, with...with the help of books. "
    $ shirapose = '1'
    show shira at m1 with dissolve
    shira "And what books would have shown you this? "
    mc "......."
    blank "A terse sigh leaves her lips, which have pursed into a thinner and thinner line throughout my explanation. "
    shira "It doesn't matter. However you laid eyes on such a spell is irrelevant. "
    shira "It's just as illegal that you performed it. "
    mc "Illegal!?"
    $ shiraface = 'neutral'
    show shira at m2 with dissolve
    shira "Yes. Only those who have passed the Trial of Sorcery may practice such a spell. "
    shira "Even I couldn't do so legally, much less one who has never even gained entrance into the Academy. "
    $ shirapose = '3'
    show shira at m1 with dissolve
    shira "That magic is meant for Sorcerers, only the most elite of magic users."
    $ shiraface = 'annoyed'
    show shira at m2 with dissolve
    shira "Do you understand what that means? "
    mc "That I...I'm going to prison? "
    blank "To my surprise, her eyes soften and, if I'm not mistaken, she almost laughs. "
    $ shiraface = 'neutral'
    show shira at m1 with dissolve
    shira "Though conventional, that...seems a bit extreme, I would think. "
    shira "It means that only five people alive at this very moment may legally perform that spell. "
    shira "Why do you think that's so? "
    mc "Uhhhm. B-because people running around accidentally changing genders all the time would get confusing? "
    blank "She opens her mouth and then closes it again, blinking at me. I wish I could learn that skill. "
    blank "Just close my damn mouth for ONCE. "
    blank "But it's not my fault! I blabber when I'm nervous!"
    $ shiraface = 'sad'
    show shira at m2 with dissolve
    shira "Well, I...I suppose you're right. "
    shira "But it's also because that spell is dangerous. You must indeed be talented if you survived it at all. "
    $ shiraface = 'neutral'
    show shira at m1 with dissolve
    shira "Most would not. "
    shira "Though you're still foolish in the ways of magic, if you thought consulting such a spell the eve before this trial was wise. "
    shira "You not only had this unfortunate side-effect, but you must have surely exhausted yourself. "
    shira "Controlling that amount of magic and preventing it from tearing you apart, despite a lack of formal training..."
    blank "She shakes her head, and though she isn't a woman who looks easily bewildered, I tend to have that effect on people. "
    $ shiraface = 'neutral'
    $ shirapose = '1'
    show shira at m2 with dissolve
    shira "It is impressive. Stupid. Very, very stupid. But impressive. "
    mc "Oh..."
    think "I didn't think I was doing anything particularly risky at the time..."
    think "If anything, I thought it was kind of clever. "
    think "Ugh. How embarrassing. I nearly got myself killed before I even made it to my trial. "
    $ shiraface = 'neutral'
    $ shirapose = '2'
    show shira at m1 with dissolve
    shira "Here. "
    blank "She helps pull me to my feet. "
    shira "I'll keep your secret. Ambition is a prerequisite for the path you've chosen, I'm sure you know that. "
    $ shiraface = 'sad'
    $ shirapose = '1'
    show shira at m2 with dissolve
    shira "I can't fault you for having it. "
    shira "But...you did not pass the test, as I'm sure you realized. "
    blank "My jaw twitches at the observation, fighting down the urge to plead and beg. "
    $ shiraface = 'neutral'
    $ shirapose = '3'
    show shira at m1 with dissolve
    shira "Defending yourself is a fundamental part of practicing magic even as an Initiate in the Academy. "
    shira "It is not a light study or a hobby. It is a practice that will take your life, if you're not prepared. "
    $ shirapose = '1'
    show shira at m2 with dissolve
    shira "Though we do what we can, there will always be those who are wounded or even killed in the Magi Wars. "
    mc "The Academy's test for graduation. "
    blank "She nods. "
    shira "Those who pass become Magi, and the strongest and most ambitious may then take the Trial of Sorcerers. "
    show shira at m1 with dissolve
    shira "Is that something you had your sights on? "
    blank "I nod reluctantly, now that the dream has already been snatched from my grip. "
    shira "We've lost many brilliant students to that Trial. "
    $ shiraface = 'sad'
    show shira at m2 with dissolve
    shira "No one has survived it in 18 years. It's claimed each one. "
    mc "Well, maybe you need a different trial..."
    blank "She scoffs, but nods. "
    shira "It does seem a reasonable solution, doesn't it? "
    shira "But the Sorcerers trial is a test of ability that a sorcerer must be able to call upon at any moment. "
    shira "Five live now, guarding the borders of our kingdom. We only have peace because they do not. "
    $ shiraface = 'neutral'
    show shira at m1 with dissolve
    shira "They must be the best of the best. We can't afford anything less. "
    shira "It's not a test we will put just anyone through. We must have hope that they can truly pass it. "
    mc "And I didn't even make the cut to be an Initiate, much less a Sorcerer..."
    blank "She hesitates for a moment, and then in a gesture that takes me by surprise, she rests a hand on my shoulder. "
    blank "It's not a great comfort, but I see a brief flicker of sympathy in her eyes."
    blank "I have to keep myself composed. I can't lose it in front of her."
    think "Hold it together, Shaun. I-It was a stupid test anyway."
    blank "I clear my throat as best I can, swallowing down bitter disappointment and childhood dreams along with it."
    blank "I guess I'm now officially a drama queen, after all. "
    blank "Speaking of..."
    mc "What about...?"
    blank "I make a vague gesture to the self that's not myself. "
    $ shiraface = 'annoyed'
    $ shirapose = '3'
    show shira at m2 with dissolve
    shira "That...that is a far more complex problem. "
    shira "We may yet find a solution for it, but any immediate counter spells would likely be reserved for Sorcerers. "
    $ shiraface = 'neutral'
    show shira at m1 with dissolve
    shira "It will take an equally strong magic to reverse the...ah, damage, outright. "
    blank "My stomach sinks. "
    think "How did this day fall apart so quickly? "
    think "I broke the law. I turned myself into a girl. And the worst part of it, I didn't even pass the exam!!!"
    think "That was the reason for all of it!"
    think "And if this was the price I had to pay to get it, I even would have paid it!!"
    blank "Feeling an embarrassing well of emotion starting to rise up in me, I bow hastily. "
    think "I have to get out of here before I make this even worse. "
    mc "I see. "
    mc "Thank you for seeing me, Magi Shira. "
    blank "I feel her eyes on my back as I leave, grabbing my bag from beside the door on my way out. "
    scene bg black with dissolve
    scene hallway with dissolve
    think "I can't believe this. "
    think "I...I really didn't make it. "
    think "How do I even go back home? What do I even go home to? "
    think "My whole life had revolved around this. "
    think "Not to mention, last time I was there, I wasn't a girl. "
    blank "I'm so preoccupied with my failure, that little problem keeps slipping my mind. "
    blank "Most people would probably be concerned with that first and foremost, but... "
    blank "This was everything to me. "
    $ warrenface = 'serious'
    show warren flip at m1 with dissolve
    warren_unknown "Miss, stop. "
    $ warrenpose = '2'
    show warren flip at m2 with dissolve
    warren_unknown "....Miss. "
    blank "I look around for a moment."
    think "Oh! Oh, right, he's talking to me..."
    think "Who is this...? "
    mc "Sir? "
    $ warrenpose = '3'
    show warren flip at m1 with dissolve
    warren_unknown "You are the young lady who just had a trial with Magi Shira."
    think "Is he asking me, or just making a bored observation?"
    mc "Uhm...Yes?"
    think "Does he know what I did!? Did she lie and turn me in already!?"
    think "But then why is he acting like I'm a girl...?"
    blank "He sighs so bitterly I can't help but wonder what I did to him. "
    $ warrenpose = '1'
    show warren flip at m2 with dissolve
    warren_unknown "She has requested that you wait. "
    show warren flip at m1 with dissolve
    warren_unknown "Stay here. And don't touch anything. "
    blank "With that, he turns to leave again. "
    hide warren with dissolve
    think "Who...was that? "
    blank "Not sure what's going on, I pace aimlessly in the hallway. "
    think "Maybe Shira thought of a way she can help with my little predicament... "
    think "At least I can get something out of this failure, maybe. "
    blank "I glance down at my chest. "
    think "Though I was kind of hoping to take these things for a spin..."
    blank "Footsteps snap me out of my thoughts. "
    $ shiraface = 'happy'
    $ shirapose = '2'
    show warren at l1
    show shira at r1
    with dissolve
    shira "After considering your case, I consulted with Master Mage Aureman about the possibility of taking on an apprentice. "
    mc "An apprentice...? "
    $ shiraface = 'neutral'
    show shira at r2 with dissolve
    shira "You did not pass the entry requirements, but given the circumstances, I believe that could be changed with practice. "
    $ shiraface = 'happy'
    show shira at r2 with dissolve
    shira "It's not uncommon for Magi to take on apprentices, to hone their skills and ready them for the entrance exam here. "
    warren_unknown "Particularly you."
    show warren at l2 with dissolve
    mc "Is this the Master Mage? "
    show warren at l1 with dissolve
    blank "The man gives me such a dark look I think the light in the room changes. "
    $ shiraface = 'annoyed'
    $ shirapose = '3'
    show shira at r1 with dissolve
    shira "No. This is Mage Warren, a fellow teacher of mine. "
    show warren at l2 with dissolve
    warren "And a far more practical one. Shira is too fond of taking in strays who have no chance. "
    think "No chance? He doesn't know anything about it!"
    blank "Shira cuts me off--before I can get myself prematurely expelled from an Academy I haven't even gotten into yet. "
    show shira at r2 with dissolve
    shira "And Mage Warren is too fond of immersing himself in conversations that have nothing to do with him. "
    show shira at r1 with dissolve
    shira "Shouldn't you be off failing your students somewhere? "
    think "They both seem so strict, even with each other. "
    think "Are all the teachers like that here? "
    blank "Despite being of equal rank, Mage Warren merely bristles at the remark. "
    blank "His scrutinizing stare eyes me down again before he sweeps off into the darkness of the Academy. "
    hide warren with dissolve
    $ shiraface = 'neutral'
    $ shirapose = '2'
    show shira at m2 with dissolve
    shira "I apologize for that. Mage Warren does not take on as many students as I do, and clearly has some opinions."
    mc "And he fails most of them...?"
    $ shirapose = '1'
    show shira at m1 with dissolve
    shira "I would say roughly half of his students may expect to pass. "
    shira "But his record is far better than mine. "
    blank "Doubt pools in the pit of my stomach. "
    $ shiraface = 'annoyed'
    show shira at m2 with dissolve
    shira "As you can see, Warren does not believe very much in chances. "
    shira "I however do. "
    $ shiraface = 'determined'
    show shira at m1 with dissolve
    shira "But not everyone will aspire to earning that chance. Very few are cut out for this school. "
    shira "Many students I take on are like yourself, disadvantaged from the start. "
    $ shiraface = 'neutral'
    show shira at m2 with dissolve
    shira "Warren is more comfortable teaching magically gifted children from well-off families, who may have personal tutors by the time they're 5. "
    mc "And even then, his passing rate is only 50/50...?"
    blank "She nods grimly. "
    shira "For their safety, yes. We refuse to foster delusions of grandeur here. "
    $ shiraface = 'happy'
    show shira at m1 with dissolve
    shira "You're getting a late start, but you're far from the first, and given what we know, I believe you have great promise. "
    shira "I am not saying this to be sentimental. It is merely a matter of fact. "
    blank "She keeps trying to emphasize how dangerous this is, how impossible. "
    blank "That only makes me want it all the more. "
    blank "Every assertion that I can't do it only sparks a flame insisting that I can. That I have to. "
    mc "I accept. "
    blank "I practically blurt the words, but they clearly don't come as a surprise. "
    blank "Shira only nods. "
    show shira at m2 with dissolve
    shira "I thought that might be the case. "
    shira "As for your...current condition. That should remain between us, I think, to avoid any trouble. "
    shira "Present yourself as a girl while in the school. "
    shira "Master Mage Aureman believes your name is Sophie. It should stay that way for the foreseeable future. "
    $ mc_name = "Shaun/Sophie"
    mc "Uhhhh...but...how do I--"
    $ shiraface = 'neutral'
    $ shirapose = '3'
    show shira at m2 with dissolve
    shira "Figure it out. That is your name from now on. "
    shira "Understand... Sophie? "
    mc "Ugh..."
    shira "Well?"
    $ mc_name = "Sophie"
    mc "Yes, I understand."
    shira "Good. "
    shira "I cannot always be there to hold your hand through this. "
    show shira at m1 with dissolve
    shira "Magic I can instruct you in. But your social life is your own to deal with. "
    blank "I close my gaping mouth and nod. "
    blank "I don't want to give her any reason to second-guess her decision to mentor me. "
    think "But Sophie? "
    think "That's my name now?"
    blank "It doesn't seem real. "
    blank "So caught up in my thoughts, I don't realize Magi Shira is leaving without me. "
    show shira at m1 with dissolve
    shira "Apprentices aren't allowed in the main area of the Academy...are you coming? "
    mc "Y-yes!"
    show shira at m2 with dissolve
    blank "I scramble to catch up with her. "
    shira "I will show you to the Apprentice Wing. "
    show shira at m1 with dissolve
    shira "You will wear a female school uniform for now, which will be in your room. "
    blank "I'm glad she's walking at a brisk pace ahead of me, her heels clacking against the floor. "
    blank "She doesn't see all the blood rapidly leaving my face. "
    scene bg black with dissolve
    scene library_day with dissolve
    show shira at m1 with dissolve
    shira "This is the apprentice library. Everything here contains basic spells and rituals that make up the foundation of magic. "
    shira "These are the spells that are safe for you to use and practice. With good sense, of course. "
    blank "She gives me a knowing look that makes me shrink a little further into my coat. "
    blank "If there's a spell to become an insignificant speck of guilt, I could have probably cast it perfectly. "
    scene bg black with dissolve
    scene hallway with dissolve
    play music "music/track03.ogg" fadeout 1 fadein 1
    show shira at m1 with dissolve
    shira "This way. "
    scene bg black with dissolve
    scene classroom with dissolve
    show shira at m1 with dissolve
    shira "This is what amounts to a classroom for Apprentices. "
    shira "Naturally there will be more emphasis on practical learning rather than sitting in a desk all day. "
    shira "I will mentor you and Charlie here. "
    mc "Charlie? Who's he?"
    $ shiraface = 'happy'
    $ shirapose = '2'
    show shira at m2 with dissolve
    shira "She is my other apprentice at the moment. "
    think "She...?"
    think "Great. I'm a guy with a girl's name, and she's a girl with a guy's name. "
    think "This isn't going to get confusing at all..."
    show shira at m1 with dissolve
    shira "You will both get a second attempt at the test, but that's all. Make good use of your time here. "
    mc "Yes, ma'am. "
    $ shiraface = 'neutral'
    $ shirapose = '1'
    show shira at m2 with dissolve
    shira "And what's your name again? "
    mc "Shau-- Sophie. "
    blank "I wince. Stupid force of habit. "
    $ shirapose = '3'
    show shira at m1 with dissolve
    shira "Learn that. Drill it into your head. "
    shira "Otherwise you'll compromise us both. Don't make me regret giving you this chance, Sophie. "
    blank "Being threatened with someone else's name really loses its emphasis, but I nod anyway. "
    blank "Being threatened with expulsion packs enough of a punch just on its own. "
    scene bg black with dissolve
    scene dormroom_day with dissolve
    show shira at m1 with dissolve
    shira "These are the apprentice dorms. "
    shira "Get changed now, before anyone sees you wearing those clothes. "
    think "Oh. I guess these are kind of boyish clothes, aren't they? "
    $ shirapose = '1'
    show shira at m2 with dissolve
    shira "Unforms will be in the wardrobe. I trust you can size it yourself? "
    menu:
        "Yes, I can manage it.":
            mc "I've been performing that kind of magic since I was young. "
            mc "It's pretty much required when you live outside of the city. "
            show shira at m1 with dissolve
            shira "Yes, I thought that might be a case. "
            shira "I'll leave you to change, then. I'll be outside the door. "
            hide shira with dissolve
            blank "The door closes and leaves me in silence. "
            blank "I look at the wardrobe, but instead sink down on the bed."
            think "Ugh. My head is still spinning. My hopes and dreams are having vertigo. "
            blank "Rubbing my palms against my temples, I take another glance down at myself. "
            blank "It's still a surprising view. "
            think "...Damn, would this be a nice body if it was on someone else. "
            think "But it's on me--or I'm in it--or whatever. "
            think "From the looks of things, I'm just going to have to get used to that..."
            think "But I have a chance. A real, honest chance to make it into the Academy!"
            blank "Hope swells in my unnaturally large and surprisingly heavy chest. "
            blank "I glance around the room, which is furnished simply, but so...so official looking. "
            blank "It might not be the official Initiate Dorms, but it's the closest I've ever been. "
            blank "I lay back and sigh happily. "
            think "I actually made it this far. I have someone on my side, someone who believes in me. "
            think "For everything that's gone wrong today, a lot has gone right. "
            think ".......And that person who believes in me is currently waiting on me. "
            think "Oh, dammit. "
            scene scene6a with dissolve
            blank "I peel myself up and strip off my clothes all in the same motion. "
            $ mc_gender = 1
            $ mc_clothes = 2
            think "Okay. Don't look. Don't look. Don't look. "
            blank "I looked. "
            think "Awww, jeez!! My skin has never been this smooth!!"
            think "And look at the size of these-"
            shira "Sophie, is everything alright in there? "
            mc "Y-Yes, everything's fine! One minute. "
            think "Okay, focus."
            think "Those are technically yours, don't get too fascinated. "
            blank "I pull out the standard uniform...and keep looking for the rest of it because what in three hells is this!?"
            think "There's hardly anything here on the bottom. "
            think "My hips aren't going to fit into this...are they? "
            think "And how does this work?!"
            blank "The bra looks like a muzzle you might put on some kind of irritable creature, but after tangling myself up a couple times... "
            scene scene6b with dissolve
            $ mc_clothes = 2
            think "Huh. The lift really does make a difference..."
            blank "I push my hands underneath the cups."
            think "Hmmm...."
            think "Solid 8.5/10. "
            think "...Is that a weird thing to say about your own wrong-gendered body? "
            think "........Probably. "
            think "Especially if you have to keep your eyes trained on the chest down. "
            think "My eyes still looks too familiar. Too me. That part is unsettling. "
            scene bg black with dissolve
            scene dormroom_day with dissolve
            $ mc_clothes = 8
            blank "The rest of the uniform comes on, as I cast a bit of magic to make it the right size. "
            think "And it fits! Phew! "
            think "I can admire all day, but I have a sinking feeling that masquerading as a girl is going to be a pain. "
            think "Though does it count as masquerading when I actually am one. Urgh, this makes my head hurt. "
            think "I don't even know the basic skills girls are born with. Like how to braid hair or win arguments through silence. "
            think "But the uniform leaves nothing to second-guessing. "
            think "No one is going to be mistaking me for a boy in this. "
            blank "I open the door to let Magi Shira back into the room. "
            $ charlieoutfit = 'uniform'
            show shira at r1 with dissolve
            show charlie at l1 with dissolve
            blank "But I'm taken by surprise when she's not standing there alone. "
        "Uhm, I'm not sure...":

            blank "I glance down at my hands, my magic still feeling weak from earlier. "
            mc "I think I'm still a little exhausted. "
            shira "Ah...of course..."
            show shira at m1 with dissolve
            shira "But you do know how to do this, yes? "
            mc "Y-Yes! I've done this sort of magic before.. "
            think "N-not with any kind of skill, but...she doesn't need to know that. "
            show shira at m2 with dissolve
            shira "Go ahead and change out of that, then. I'll help you with the fitting. "
            mc "Alright..."
            blank "I wait, but she doesn't leave. She just stands there, watching me with that same, sharp look. "
            mc "Um..."
            mc "I....."
            blank "Finally she blinks. "
            shira "Oh, of course. You're still new. "
            show shira at m1 with dissolve
            shira "There are some rituals that are better performed without bulky clothes on, but you wouldn't be used to that yet. "
            shira "I suppose I've gotten too lax about that sort of thing in my time. "
            think "Rituals were you don't wear clothes...? "
            think "What kind of school is this!?!"
            shira "I'll turn around and give you some privacy. "
            hide shira with dissolve
            think "It doesn't feel like privacy..."
            blank "But it doesn't really feel like my body, either, which makes it easier to strip down. "
            $ mc_gender = 1
            $ mc_clothes = 2
            blank "I try not to let on just how fascinated I am with it--really, I didn't know skin could be this silky. "
            blank "I pull out the uniform and underwear, putting it on first alongside some thin panties with a suspicious amount of lace. "
            think "I feel like I'm dressing up for a play or something. "
            think "A play titled Shaun's Life: A Series of Spectacular Failures. "
            scene scene6b with dissolve
            $ mc_clothes = 2
            blank "I shift awkwardly in my new underwear, inspecting it. "
            think "It's like something out of a magazine. "
            blank "Not that I look at those kind of magazines or anything..."
            mc "Um. Alright..."
            blank "Magi Shira spins around to face me, her gaze dragging up and down my body. "
            blank "I-Isn't this a little fast? And she is my teacher. "
            shira "Ah. That looks acceptable. "
            scene scene7a with dissolve
            shira "Here. "
            blank "Without warning, she brings her hands under my chest, causing my face to flush red. "
            shira "I'll fit it so it will hug a bit better in the front. "
            blank "Her hands push upward on my chest, and she hums, like she's knitting and not feeling up one of her students. "
            scene scene7b with dissolve
            think "!!!"
            shira "And the hem of the skirt, that should follow the curve of your hip. Like so. "
            blank "Her fingers trail down by my inner thigh, as she does so the unform recedes and bends to her magic. "
            scene bg black with dissolve
            scene dormroom_day with dissolve
            $ mc_clothes = 8
            blank "A moment later I am dressed again. "
            blank "Standing there with my new uniform, the fabric tugging tight over my chest and the skirt short enough to be uncomfortable. "
            show shira at r1 with dissolve
            shira "How does that feel? "
            mc "L-Like all I need now is a pole and some music. "
            $ charlieoutfit = 'uniform'
            show charlie at l1 with dissolve
            charlie_unknown "Ahahaa!!"

    think "!!?"
    think "Who's this and why is she in my room...?!"
    shira "Ah. Just in time for first introductions, I see. "
    show shira at r2 with dissolve
    shira "Charlie, this is a new apprentice of mine, Sophie. "
    blank "Charlie arches an eyebrow at me, looking a little more amused than I'm comfortable with. "
    shira "Sophie, this is the other apprentice I was telling you about. "
    think "Oh..."
    think "It didn't actually occur to me before, but..."
    think "I'm going to have to actually live with a girl while pretending to be one!?"
    think "I don't even speak the language!!"
    mc "H-Hi. "
    $ charlieface = 'blush'
    show charlie at l2 with dissolve
    charlie "Uh, hi. "
    $ charlieface = 'neutral'
    show charlie at l2 with dissolve
    charlie "You shy or something? "
    show shira at r1 with dissolve
    shira "Don't mind Charlie. She's too upfront for her own good. "
    blank "The girl cracks a mischievous smile, but says nothing. "
    shira "Play nicely, you two. I think you can both help each other in your studies. "
    shira "I'll leave you two to get to know each other. Charlie, make sure Sophie gets her bearings on how the school works. "
    shira "If you have any trouble, come find me. "
    shira "We'll resume our normal studies tomorrow. "
    hide shira with dissolve
    show charlie flip at m1 with dissolve
    blank "The one person who knows my situation vanishes. "
    think "Talk about sink or swim..."
    blank "To my surprise, Charlie thrusts out a hand at me. "
    charlie "Nice to meet you. "
    charlie "Call me Charlie. No nicknames. "
    mc "R-right. "
    mc "How long have you been training with Magi Shira, exactly...? "
    $ charliepose = '2'
    show charlie flip at m2 with dissolve
    charlie "Maybe a week. "
    charlie "Time goes by pretty quickly. She'll come back this afternoon. "
    mc "What for? "
    charlie "Eh. You'll find out. "
    blank "She grins and then plops down on my bed. "
    $ charliepose = '1'
    $ charlieface = 'neutral'
    show charlie flip at m1 with dissolve
    charlie "So I take it you're not from the capital? "
    mc "Do I have an accent or something...?"
    charlie "Nah. But you look about as nervous as a rabbit in a wolf's den, and I guess the capital can kinda seem that way. "
    charlie "I've seen newbies here before and they all kind of have that look."
    think "That's not exactly the problem, but I guess it's better than coming up with my own excuse. "
    charlie "You might as well not worry about it. "
    $ charlieface = 'flirty'
    show charlie flip at m2 with dissolve
    charlie "It's not like you'll have enough time away from the school for it to matter. "
    charlie "We're basically stuck here. "
    mc "Did you already have your initiation trial, too? "
    $ charliepose = '2'
    $ charlieface = 'sad'
    show charlie flip at m1 with dissolve
    charlie "Yeah, I mucked that up pretty bad."
    blank "She laughs and scratches the back of her head. "
    charlie "Get louder, hit harder. "
    $ charlieface = 'annoyed'
    show charlie flip at m2 with dissolve
    charlie "That was my philosophy. "
    charlie "Didn't really work out when she outsmarted me like I was just toddler throwing a tantrum."
    $ charliepose = '1'
    $ charlieface = 'neutral'
    show charlie flip at m1 with dissolve
    charlie "Real embarrassing. "
    mc "At least we get another chance. "
    charlie "Yeah. I think Shira's a real softie under that mask. "
    charlie "She acts tough as a teacher, but beneath that, she's pretty compassionate. "
    show charlie flip at m2 with dissolve
    charlie "Not that I'm an expert. "
    charlie "So how did you get into magic if you're not from around here? "
    menu:
        "Natural talent.":
            mc "I just had a knack for it. "
            mc "It runs in my family and I decided not to waste the potential. "
            $ charlieface = 'blush'
            show charlie flip at m1 with dissolve
            charlie "Hmm. You're pretty good, then? "
            mc "W-Well, I didn't pass, but..."
            think "Oh, come on, you're not even the right gender at the moment, you don't have to impress her!!"
            mc "I clear my throat. "
            mc "I think with a little polish on the techniques, I could be one of the best. "
            blank "Mentally, I slam my face into my hands. "
            think "Great job, tongue. "
            think "You can't even control your ego, much less your magic. "
            $ charliepose = '2'
            $ charlieface = 'neutral'
            show charlie flip at m1 with dissolve
            charlie "Yeah, we'll see, won't we? "
            mc "Is that a challenge? "
            charlie "...Nah. "
            blank "She sighs indifferently. "
            $ charlieface = 'sad'
            show charlie flip at m2 with dissolve
            charlie "I'm not much of the fight it out type. "
            mc "....Then why are you at a school where graduating depends on fighting? "
            blank "She shrugs. "
            $ charliepose = '1'
            $ charlieface = 'neutral'
            show charlie flip at m1 with dissolve
            charlie "One of life's many mysteries, isn't it? "
            charlie "I guess I am ambitious, but that doesn't mean I want to go smashing everything in my path. "
            charlie "I just want to be good at what I do. "
            charlie "Well talk to you in a bit. "
            mc "What?"
            hide charlie with dissolve
            jump night1
        "I knew a Mage growing up.":

            $ charlie_love += 1
            mc "He was sort of a family friend, I guess. He wandered through town once or twice. "
            mc "He didn't train me in a lot of combat, though.... "
            mc "We focused on practical things, I guess. Day to day things that help when you're not battling it out for survival. "
            mc "But he said I could come here and become a Mage, maybe even a Sorcerer. "
            $ charlieface = 'sad'
            show charlie flip at m1 with dissolve
            charlie "Mage? "
            mc "M-Magi!"
            think "S-Stupid gender-specific titles!"
            blank "She laughs. "
            $ charlieface = 'happy'
            show charlie flip at m2 with dissolve
            charlie "Do they just lump us all into one category where you're from? "
            mc "Uh, y-yeah, I guess we do. If you're a magic user, you're basically a Mage there. "
            $ charlieface = 'neutral'
            $ charliepose = '2'
            show charlie flip at m1 with dissolve
            charlie "Hmmm. That's a little weird. "
            think "It's also completely made-up, so please don't think too much about it..."
            mc "A-Anyway, I guess the idea got into me young. "
            charlie "The idea of being a sorcerer, too? "
            $ charlieface = 'sad'
            $ charliepose = '1'
            show charlie flip at m2 with dissolve
            charlie "That's a death sentence, you know. "
            mc "W-what? "
            $ charlieface = 'blush'
            show charlie flip at m1 with dissolve
            charlie "Becoming a sorcerer. Do you really want to?"
            menu:
                "Yes, even if it's a childish dream.":
                    charlie "A childish dream? "
                    charlie "Childish dreams are like wanting to be a doctor when you're afraid of blood or wanting to join a circus. "
                    charlie "Wanting to be a sorcerer is synonymous with wanting to be a corpse. "
                    mc "You don't think I can do it? "
                    $ charlieface = 'mad'
                    show charlie flip at m2 with dissolve
                    charlie "I think you could die!"
                    mc "So? "
                    charlie "So!?"
                    $ charliepose = '2'
                    show charlie flip at m1 with dissolve
                    charlie "People do DIE where you come from, right? "
                    charlie "You're not THAT sheltered. "
                    mc "Of course they do!"
                    mc "B-but that doesn't mean I'm not going to try!"
                    think "I'm not giving it up just because some girl I've just met doesn't think I can handle it. "
                    think "I've met plenty of nay-sayers in my time and none of them have set me back yet. "
                    $ charlieface = 'sad'
                    show charlie flip at m2 with dissolve
                    charlie "Whatever. "
                    charlie "You can try all you like. "
                    blank "She hops off the bed and strolls toward the door. "
                    mc "Where are you going? "
                    charlie "Wherever I want. But I'm not wasting my time on the dead girl. "
                    hide charlie with dissolve
                    think "The dead girl. "
                    think "Bah. I'm not going to die. "
                    think "....I'm not even a girl!"
                    jump night1
                "Yes, and I'll give anything to do it.":

                    $ charlie_love += 1
                    show charlie flip at m2 with dissolve
                    charlie "Even your life? "
                    mc "Even that. "
                    $ charliepose = '2'
                    $ charlieface = 'mad'
                    show charlie flip at m1 with dissolve
                    charlie "Why!? Why would it be worth that? "
                    mc "It's...it's not easy to explain. "
                    mc "I'm just not afraid of sacrifice. It's not because I'm so confident that I think I can't fail, it's just..."
                    mc "I have to try. "
                    think "I don't think I'm getting through to her. "
                    $ charlieface = 'sad'
                    show charlie flip at m2 with dissolve
                    charlie "It's your funeral, I guess. "
                    charlie "It's noble and everything, but...you seem really naive. "
                    mc "That's fine. "
                    charlie "...?"
                    mc "You won't change my mind. "
                    mc "You'll probably get the satisfaction of being proved right anyway. "
                    $ charliepose = '1'
                    $ charlieface = 'blush'
                    show charlie flip at m1 with dissolve
                    charlie "I'll get the satisfaction of seeing you die, you mean. "
                    charlie "Yeaaaah, that's not morbid at all. "
                    think "I REALLY didn't think about that before I said it. "
                    blank "Charlie gets up off the bed. "
                    charlie "Well, if you're a lost cause, I don't guess I'm going to waste my time. "
                    charlie "But...good luck, maybe? "
                    hide charlie with dissolve
                    think "...Wait, wasn't she supposed to show me around or something? "
                    think "And she just left!? "
                    think "...Was my first impression really that terrible!?"
                    jump night1


label night1:
    scene bg black with dissolve
    scene dormroom_day with dissolve
    play music "music/track06.ogg" fadeout 1 fadein 1
    think "She's left..."
    blank "For a few minutes, I sit awkwardly in my room. "
    blank "I put the things in my bag away, though it's not much and it doesn't take long. "
    think "All this male underwear looks really odd now.."
    think "Maybe I can burn it? Or would that look even wierder?"
    blank "Unsure, I stuff it underneath my mattress and toss the rest of my bag to the ground. "
    think "She thinks I'm going to fail. "
    think "What does it matter what she thinks? She's just some girl you talked to for five minutes. "
    think "It doesn't mean anything. "
    scene bg black with dissolve
    scene hallway with dissolve
    blank "Not sure what I'm meant to do, I wander around the Apprentice area that Magi Shira showed me. "
    think "I better get my bearings before I have to be somewhere on time. "
    think "I'm not sure if Charlie's going to be as much of a help as I'd hoped..."
    scene bg black with dissolve
    scene library_day with dissolve
    think "I guess I can try to get a head start on studying..."
    think "I can't get shown up on the first day. Charlie might never let me live it down. "
    think "And Magi Shira would get a bad impression. A worse impression, anyway. "
    blank "Thumbing through some of the books, I find mostly information I've already been told. "
    think "Spell Casting. The Tactician's Guide to Stealth. So You Think You Can Do Magic..."
    think "Ugh. "
    blank "It's practical stuff, but nothing complex that's really going to help me impress anybody. "
    blank "Irritated, I shove the book away. "
    think "Where's the harder section? "
    think "Magi Shira said these books would be more to an apprentice level, but I don't need just baby steps!"
    blank "But further inspection of the library reveals much the same. "
    blank "Informational texts, histories, and other dull subjects. "
    think "Maybe it's for the best..."
    think "The last time I went in a library to try and impress someone, I ended up as a girl. "
    think "I should have learned my lesson then and there. "
    think "But what am I supposed to do instead? "
    menu:
        "Explore the school.":
            play music "music/track01.ogg" fadeout 1 fadein 1
            think "Okay, I tried playing by the rules. "
            think "...For like 5 minutes, but still. I gave it my best attempt. "
            think "But I'm sure there are other places I can go, even if I'm not an Initiate. "
            scene bg black with dissolve
            scene hallway with dissolve
            blank "I leave the library behind, in pursuit of something a bit more interesting. "
            scene bg black with dissolve
            scene entrance_interior_day with dissolve
            think "This is where I came in. "
            blank "The open room is still just as empty as it was before. "
            think "Where is everyone? "
            think "Maybe classes are going on..."
            scene bg black with dissolve
            scene hallway with dissolve
            blank "Curious, I head down another hallway. "
            blank "The passageways reveal much the same. Hallways that look confusingly similar in appearance, doors that don't seem to have a way to open."
            blank "I can’t even find the place where I took my trial earlier."
            think "Shouldn’t there be some kind of dining hall or something?"
            think "Hrm…"
            blank "Knowing that as long as I can make it back to the foyer, I can get my bearings, I start wandering through less familiar territory."
            scene bg black with dissolve
            scene hallway_two with dissolve
            blank "From a distant doorway, with a high arch and an open entryway, a chorus of rhythmic muttering catches my attention."
            blank "The words rise and fall in a wave. A chorus of soft voices."
            think "Is that…?"
            blank "I move forward on my tiptoes, as if anyone might actually hear me over the droning chants."
            blank "I peek around the corner."
            scene bg black with dissolve
            scene classroom with dissolve
            think "Wait a second...that’s…"
            $ auremanface = 'neutral'
            show aureman at m1 with dissolve
            blank "Standing at the head of the class, a familiar old man leads the dictation, emphasizing his hand motions with each word."
            think "Oh, crap! I'd remember that beard anywhere!"
            think "That’s the guy who found me in the library!"
            think "What is he doing here?!!"
            think "The smart thing would be to hang back and try to avoid this guy at all costs."
            think "It’s a big school. It might be possible."
            think "But…"
            blank "Watching the students, I can’t help but wonder what they’re doing. My curiosity practically drags me toward the doorway. "
            think "This is an actual class."
            think "Initiates who were good enough to be accepted into the academy."
            blank "Suddenly, one of the student’s hands begin to glow with a soft purple."
            aureman_unknown "Excellent, excellent."
            blank "The professor's own hands are cloaked in green, the power flickering and shifting gently as it coils around like lazy smoke."
            blank "One by one, students lift up their hands to reveal a colour, different shades spilling between their fingers."
            $ auremanface = 'happy'
            show aureman at m2 with dissolve
            aureman_unknown "Very good."
            think "What are they doing?"
            aureman_unknown "Now. Who can guess as to why we’ve all performed the same ritual, but have ended up with different colours?"
            student "Because we each muttered the spell with our own accent and inflection?"
            aureman_unknown "Ah, very close, very close."
            aureman_unknown "Not quite though."
            $ auremanface = 'silly'
            show aureman at m1 with dissolve
            aureman_unknown "What about you?"
            blank "He looks right at me."
            blank "I nearly jump out of my skin, a whole classroom worth of eyes suddenly turning my way."
            blank "Stumbling back away from the door, I lift up my hands."
            mc "S-Sorry, I uh-- I was just lost, I didn’t mean to--"
            $ auremanface = 'neutral'
            show aureman at m2 with dissolve
            aureman_unknown "Nonsense. Sometimes getting lost is precisely how we end up where we’re meant to be."
            aureman_unknown "Please, come in, come in."
            blank "Face scalding like a frying pan, I force my feet to drag themselves one in front of the other and stand reluctantly before a whole classroom."
            mc "Um…"
            aureman_unknown "And you are?"
            mc "Sh-Sophie."
            aureman_unknown "Ah, Sophie, yes."
            mc "You’ve heard of me…?"
            show aureman at m1 with dissolve
            aureman_unknown "Mm. Magi Shira consulted me to ask permission to take you on as an apprentice."
            think "He must be Master Mage Aureman, then…"
            blank "At the word apprentice, a soft snicker rises from somewhere near the back of the class, sending a coil of anger twisting through my head."
            think "What’s so funny about it?!"
            think "I’ll be just as good as him one day--no, better--sitting in this exact same classroom!"
            blank "My fists clench at my sides."
            think "Man, if I wasn’t standing in front of a dozen witnesses, I would--"
            blank "The thought gets cut short."
            aureman "Here, Sophie. Inspect this and tell me why you think this magic is appearing green."
            scene scene8a with dissolve
            blank "He extends his hands."
            blank "I blink down at the hands extended to me."
            think "Uh…"
            think "I don’t really know anything about magical theory!!"
            think "I guess that’s what I should have been reading in the library, where I should have stayed."
            think "Is he doing this to punish me for eavesdropping? Lesson via public humiliation? "
            mc "Um…"
            scene scene8b with dissolve
            blank "Tentatively, I reach out to touch the flickering magic. It doesn’t change colour."
            blank "In fact, it doesn’t feel like anything at all."
            blank "It vibrates a little, calling out to my magic, but nothing else."
            blank "The whole class waits, watching me for an answer."
            blank "I’m guessing most of them have already formed some kind of guess, but no one is brave enough to say it and spare me from this…"
            think "Cowards."
            mc "Maybe it’s because..."
            menu:
                "Each person’s magic is unique.":
                    $ charlie_love += 1
                    blank "I blink in slow realization, a guess forming at the back of my mind."
                    mc "Because this is just your magic...and every person’s magic is different?"
                    aureman "Excellent!"
                    scene scene8a with dissolve
                    aureman "You took a risk by touching a spell you did not know, granted, but I’m sure you realized I wouldn’t have allowed it if it was dangerous."
                    blank "He turns back to the class."
                    aureman "As Sophie has determined, this is strictly a manifestation of my magic."
                    aureman "I used a ritual to summon it, but there’s no spell here, no real power at work."
                    aureman "As you all know, different spells and rituals can have different colours associated with them, or even no colour at all."
                    aureman "But our raw magic does have its natural colour."
                    aureman "Like your hair or eye colour, your magic is also unique to you."
                    aureman "You can look around the room and see it might be a similar shade to someone else’s, and that means your magic has similar properties."
                    student "Does personality have anything to do with it?"
                    think "If I had that baby-poop green colour, I’d be worried about my personality, too."
                    aureman "No, there’s no known correlation between personality and magic colours."
                    aureman "But know that sometimes being unskilled at a certain type of magic has less to do with your capabilities, and more to do with your magic type."
                    aureman "As we advance in this class, we will learn more about magic theory and specializations for different magic types. "
                    aureman "Here, Sophie. Would you like to try with the rest of us?"
                    blank "The green from his hands vanishes as he walks me through it."
                    scene scene8c with dissolve
                    blank "Summoning raw magic, without a ritual or spell, isn’t something I’d ever considered doing before…"
                    blank "Slowly, though, I feel it start to build."
                    blank "My fingers match his movements until--"
                    blank "Between my outstretched hands, a gold colour begins to grow and brighten, swelling with my own satisfaction."
                    think "It's working!"
                    think "Though maybe a little too much..."
                    scene scene8d with dissolve
                    blank "Soon, I have to squint against the intense light, a blinding contrast to the soft, earthy green in the professor’s hands."
                    blank "The golden edge of the magic remains, but the centre is so vivid, I can only see white there. "
                    blank "The soft pastels and dark, grungy shadows circling the hands of others looks nothing like this. "
                    blank "I close my hands and the raw magic vanishes."
                    scene classroom with dissolve
                    $ auremanface = 'neutral'
                    show aureman at m1 with dissolve
                    aureman "Fascinating..."
                    mc "...What?"
                    blank "The Masters gaze however remains on my hands with a transfixed stare, seeming to forget the class watching us."
                    aureman "In all my years, I’ve only seen such magic once before-"
                    charlie "Psst! Sophie!"
                    think "What?"
                    think "Charlie?"
                    $ charlieface = 'blush'
                    show charlie at l1 with dissolve
                    charlie "Uh, sorry Master Aureman, can I borrow her…?"
                    $ auremanface = 'silly'
                    show aureman at m2 with dissolve
                    aureman "Of course. I was the one taking up her time."
                    mc "--but what were you going to say?"
                    blank "My words go unanswered, as Charlie suddenly has me by the arm, wheeling me out of the classroom. "
                    blank "He nods at me politely, as if he's the one dismissing me, leaving me to be carted out of the classroom in confusion."
                    scene bg black with dissolve
                    scene hallway with dissolve
                    $ charlieface = 'annoyed'
                    show charlie flip at m2 with dissolve
                    charlie "What the hell were you doing in there?!"
                    blank "She keeps me by the arm without explanation, continuing her kidnapping."
                    mc "I...I don’t know, he just asked me to join!"
                    $ charliepose = '2'
                    show charlie flip at m1 with dissolve
                    charlie "You’re not even supposed to be in this part of the school."
                    mc "Then what are you doing here?"
                    charlie "Looking for you!"
                    $ charliepose = '1'
                    show charlie flip at m2 with dissolve
                    charlie "Listen, as far as Magi Shira probably cares, I’m responsible for you at the moment."
                    charlie "I can’t have you just running around doing whatever you want, that looks bad on me!"
                    mc "Then maybe you shouldn’t have left."
                    blank "She huffs."
                    $ charlieface = 'angry'
                    show charlie at m1 with dissolve
                    charlie "I didn’t think you’d run off into the Master Mage’s classroom of all things!"
                    charlie "You really don’t have any self-preservation skills, do you?"
                    blank "Thinking back over everything that’s happened to me in the last 24 hours…"
                    mc "Not a one."
                    blank "She sighs."
                    $ charlieface = 'sad'
                    $ charliepose = '2'
                    show charlie flip at m2 with dissolve
                    charlie "Alright. I’m sorry I left in a huff, then."
                    mc "Do you take back what you said?"
                    blank "A sly smirk curves over her mouth."
                    charlie "Not a word of it."
                    blank "She yanks me in a new direction. "
                    mc "Hey!"
                    $ charliepose = '1'
                    $ charlieface = 'sad'
                    show charlie flip at m1 with dissolve
                    charlie "Come on. We’re going to dinner before Shira notices we were missing."
                    mc "Aren’t we allowed to interact with the other students…?"
                    $ charlieface = 'neutral'
                    show charlie flip at m2 with dissolve
                    charlie "Trust me. Pretty soon, you’re going to be too busy to remember or care that there are other students."
                    charlie "And really...it's for the best that we don't. "
                    jump main1
                "Some magi are more powerful.":

                    $ shira2 = True
                    aureman "An interesting stance, but no-- it’s believed all magical users can grow to be powerful."
                    mc "But...that can’t be true."
                    mc "If everyone had the same potential, wouldn’t the school just train people until they were ready to pass the Sorcerer Trials?"
                    blank "And there goes my mouth again, cutting off my brain at the intersection of common sense. "
                    think "Trying to argue with the professor in front of the class...historically not a good idea. "
                    aureman "You talk about a subject you hardly understand."
                    aureman "The Sorcerer Trials-"
                    scene classroom with dissolve
                    $ auremanface = 'neutral'
                    show aureman flip at l2 with dissolve
                    shira "Sophie! What are you doing here?"
                    blank "Spinning on my heel, my heart jumps into my throat."
                    think "Oh crap."
                    show shira at r1 with dissolve
                    blank "Her scowl settles on me, and I physically feel the other students lean in, eager for the bloodshed."
                    think "Maybe they’ll get to see me be expelled, right here in front of everyone."
                    $ auremanface = 'happy'
                    show aureman flip at l1 with dissolve
                    aureman "No harm done, Magi Shira."
                    aureman "This is a school after all. I was simply helping another student learn."
                    $ shiraface = 'sad'
                    $ shirapose = '3'
                    show shira at r2 with dissolve
                    shira "Forgive the intrusion, Master Aureman. I will keep a sharper eye on this one."
                    blank "She roughly gestures me out of the classroom."
                    blank "Tail between my legs, I give Aureman a glance and shuffle out of the room."
                    scene bg black with dissolve
                    scene hallway with dissolve
                    $ shiraface = 'annoyed'
                    show shira at m2 with dissolve
                    shira "What were you thinking?"
                    shira "I tell you explicitly to stay in the Apprentice wing, and this is what you do?"
                    $ shiraface = 'sad'
                    show shira at m1 with dissolve
                    shira "Interrupt other teachers and make it appear as though you have no discipline?"
                    mc "I…"
                    think "Why did I do it?"
                    think "Just because I got bored?"
                    blank "But that wasn’t it, an indignant and obnoxiously prideful voice in the back of my head urges."
                    blank "And of course I end up saying it."
                    mc "I just wanted to see it."
                    $ shiraface = 'angry'
                    show shira at m2 with dissolve
                    shira "To see what, exactly?"
                    mc "Other people learning magic. An actual class."
                    mc "I wanted to see what that was like and...and what they were learning."
                    $ shiraface = 'annoyed'
                    show shira at m1 with dissolve
                    shira "You will begin plenty of that in your own time."
                    think "But I want it noooooow."
                    think "That’s essentially what I’m sounding like."
                    think "Great impression there, Shaun. Sophie. Whoever I am."
                    blank "But the closer we get to the Apprentice wing, the more Shira’s angry steps slow to a leisurely pace."
                    shira "I understand, you realize."
                    $ shiraface = 'sad'
                    show shira at m2 with dissolve
                    shira "I was like you once. Ambitious and hungry to learn. To prove myself."
                    shira "But you don’t go far if you don’t abide by the rules."
                    shira "I have every intention of doing what I can to help you, Sophie."
                    $ shiraface = 'neutral'
                    show shira at m1 with dissolve
                    shira "Just like mine, I want your dreams to be realized."
                    shira "But you have to trust me, and not just go your own way."
                    shira "Do you understand?"
                    blank "After a moment of looking scolded, I nod."
                    $ shirapose = '2'
                    show shira at m2 with dissolve
                    shira "And just so you know, I do think there was some truth to what you said-- about people's power being naturally different. "
                    shira "Some better than others. "
                    mc "You heard that...?"
                    show shira at m1 with dissolve
                    shira "I did. "
                    shira "But it's no matter now. It’s getting late and I bet you’re hungry."
                    mc "Starved, actually."
                    blank "Food had been the last thing on my mind all day, but at the mention of it, my stomach wails for my attention."
                    shira "Mmmhm."
                    $ shirapose = '1'
                    $ shiraface = 'determined'
                    show shira at m2 with dissolve
                    shira "One of those types, too, hm? At this point, I'm not surprised. "
                    mc "What type? "
                    shira "Able to ignore your most basic needs in pursuit of ambition."
                    blank "My cheeks darken, not sure if it’s a criticism or praise."
                    shira "Ah."
                    shira "There you are."
                    $ charlieface = 'blush'
                    show charlie at l2 with dissolve
                    charlie "What happened? "
                    shira "That's precisely the question I was thinking. "
                    $ shiraface = 'neutral'
                    show shira at r2 with dissolve
                    shira "You were supposed to be looking after her, Charlie. I entrusted her to your care because I thought you could handle it."
                    shira "So, as you asked, what happened?"
                    blank "Looking scandalized, Charlie’s mouth opens in an attempt to defend herself."
                    $ charliepose = '2'
                    show charlie at l1 with dissolve
                    charlie "I...I didn’t know what she was going to do!"
                    $ shirapose = '3'
                    show shira at r1 with dissolve
                    shira "Because you weren’t with her, when I told you to be."
                    mc "It’s not Charlie’s fault. I told her that she could leave."
                    mc "I wanted to sneak away by myself."
                    blank "Shira’s disapproving gaze lingers on me for a long moment."
                    $ shiraface = 'annoyed'
                    show shira at r2 with dissolve
                    shira "You’re new to this school, Sophie, and only here out of my benevolence. Remember that."
                    shira "Charlie, take Sophie to dinner."
                    $ shirapose = '1'
                    hide shira with dissolve
                    blank "She turns and departs from us, heels clicking sharply across the floor as her robes billow."
                    blank "We watch her go until she's completely out of ear-shot and I actually brace myself to be flat-out punched. "
                    $ charlieface = 'blush'
                    show charlie at l1 with dissolve
                    charlie "...You didn’t have to do that. I did bail on you."
                    think "Huh? "
                    think "I was expecting a stronger reaction than that..."
                    blank "I shrug."
                    mc "Doesn’t mean you’re responsible for what I did afterwards."
                    $ charlieface = 'neutral'
                    show charlie at l2 with dissolve
                    charlie "Damn right it doesn't."
                    charlie "But thanks anyway. I don’t like it when she’s angry."
                    charlie "She's strict enough as it is, we don't need to add any emotions into the mix. "
                    blank "I have my doubts that really describes Shira, considering the occasional flicker of kindness she's shown me, but I don’t argue."
                    blank "Charlie jerks her head toward an open door, the room behind it buzzing with noise."
                    $ charliepose = '2'
                    show charlie at l1 with dissolve
                    charlie "Come on, then. If we're stuck together, we might as well get dinner."
                    jump main1
        "Go back to my room.":


            blank "I heave a sigh."
            think "What else can I do?"
            blank "I trod back toward my room without feeling particularly certain about why. I know I’ll get just as bored when I’m there."
            think "I’ve been here 20 minutes, a place I’ve aspired to come to for years, and already I’ve lost interest."
            think "What does that say about my attention span?"
            scene bg black with dissolve
            scene dormroom_day with dissolve
            blank "I push open my door."
            $ charliepose = '2'
            show charlie at m1 with dissolve
            mc "What are you doing in here!?"
            blank "She glances up from where she had been peering into my bag."
            $ charlieface = 'blush'
            show charlie at m2 with dissolve
            charlie "Nothing. Just wondering where you ran off to."
            mc "And getting into my things!"
            blank "I pull my bag toward me defensively, as she holds up her hands and backs off."
            charlie "Chill out. It’s not like I took anything."
            blank "My heart is racing with worry, running laps with the questions buzzing around my mind. "
            think "How much did she see? What does she suspect? "
            $ charlieface = 'neutral'
            show charlie at m1 with dissolve
            charlie "You’ve got some cool clothes, though."
            mc "...What?"
            blank "Heat creeps up my neck and I peer into the bag, where I can see the heavy jacket that got ripped up during the fight."
            blank "I stuffed it on top, so hopefully it covered most of my clothes…"
            blank "If she saw anything more than that, she’ll know for sure that I’m not what I appear to be..."
            charlie "I thought you’d have mostly drab clothes."
            charlie "You know, like…"
            mc "Like a brown sack with holes cut in it?"
            $ charlieface = 'flirty'
            show charlie at m2 with dissolve
            charlie "Exactly."
            mc "I lived out in the country, not in a different time period…"
            mc "And you still haven’t told me why you’re messing around in my room!!"
            think "My voice sounds so squeaky when I get mad…"
            $ charliepose = '2'
            $ charlieface = 'neutral'
            show charlie at m1 with dissolve
            charlie "I came to find you."
            mc "Yeah, well, I’m not exactly gonna fit in this bag, am I?"
            blank "I shake it at her angrily."
            charlie "Pft. Not with that chest, you’re not."
            blank "Another wave of heat crawls up my neck."
            mc "I-I thought you weren’t wasting your time on me."
            show charlie at m2 with dissolve
            charlie "Just because you’re going to get yourself killed, doesn’t mean you need to starve yourself."
            charlie "I came by to take you to dinner."
            charlie "Unless you’re going to eat that jacket."
            mc "You didn’t have to come get me."
            charlie "Actually, I did."
            $ charliepose = '1'
            show charlie at m1 with dissolve
            charlie "Magi Shira did put me in charge of you, after all."
            think "That’s a little over-glorified…"
            charlie "And it’s not like you’d know where to go. So it was either let you starve in here, or come get you."
            charlie "And I hate eating alone anyway, so guess what?"
            charlie "You’re my new cafeteria buddy, death wish."
            charlie "So come on, let’s go get something to eat before my stomach thinks I’ve forgotten about it."
            blank "She grabs me by the arm and starts hauling me down the hallway."
            scene bg black with dissolve
            scene hallway with dissolve
            show charlie at m1 with dissolve
            mc "...Is everyone here as up-front as you are?"
            charlie "Nope. That’s just a perk of knowing me."
            charlie "The cafeteria’s just up ahead."
            jump main1

label main1:
    scene bg black with dissolve
    scene dininghall with dissolve
    play music "music/track08.ogg" fadeout 1 fadein 1
    blank "Here the school finally comes to life, looking more inhabited and friendly and less like the imposing, empty monolith it seemed to be."
    blank "Students sit around tables talking and laughing. In one corner, a group of teachers monitor the room."
    show charlie flip at m1 with dissolve
    charlie "Classes let out at different times to keep the dining hall from filling up too much at once."
    charlie "Since we don’t have a rigid class schedule, we can come in any time after 7. I think they stop serving food at 9, but who eats dinner at 9 anyway?"
    blank "We get our food and take a seat together near one corner of the room."
    think "I’m still not sure what to think about Charlie."
    think "Why the sudden change of heart?"
    think "I mean, I guess she is just trying to save her own skin…"
    think "And even if we’re not on the best of terms, I don’t want to mess with her."
    blank "We sit down together, which is a relief for my first-day anxiety. I wouldn’t have known where to sit otherwise."
    $ charlieface = 'annoyed'
    $ charliepose = '2'
    show charlie flip at m2 with dissolve
    charlie "Will you stop fiddling with the hem of your skirt?"
    charlie "It’s driving me nuts."
    mc "It’s driving ME nuts."
    blank "I don’t realize it, but I do keep tugging it down when I feel the fabric brush too high on my thigh."
    $ charliepose = '1'
    show charlie flip at m1 with dissolve
    mc "It doesn’t cover anything! What am I supposed to do?"
    $ charlieface = 'blush'
    show charlie flip at m1 with dissolve
    charlie "Wear cute panties."
    blank "I make my best attempt at drowning myself in my drink as Charlie just shrugs unhelpfully."
    think "I hope Magi Shira finds a way to fix this sooner rather than later..."
    blank "Dinner is amazing, though."
    blank "Not the food. I barely taste the food."
    blank "But there are actual Magi here, using spells casually."
    blank "Some students carry their trays without their hands. Others nab food off those same levitating, unguarded trays."
    blank "All the laughing and carrying on draws my eyes around the room, not wanting to miss anything."
    $ charlieface = 'neutral'
    show charlie flip at m2 with dissolve
    charlie "Are you going to actually eat?"
    mc "Oh. Right, sorry."
    blank "Distracted, I spear some vegetables onto my fork."
    charlie "You look like a little kid."
    mc "What?"
    blank "Glancing down at my chest, my brow furrows."
    think "How?"
    $ charliepose = '2'
    show charlie flip at m1 with dissolve
    charlie "Your face, I mean. Never seen this many magic users all in one place?"
    think "Oh."
    blank "I scoff under my breath."
    mc "Not counting myself, I’ve never seen more than three magic users in my whole life before today…"
    blank "She seems to consider that, and then pats my shoulder."
    $ charlieface = 'happy'
    show charlie flip at m2 with dissolve
    charlie "Don’t worry. You’ll get as used to and bored of it as the rest of us."
    blank "The cynicism doesn’t damper my mood any, but does remind me to actually keep eating."
    blank "Being used to home cooked meals all my life, having something not prepared by a familiar face is bizarre."
    blank "It’s not bad, but it is…I don’t know, it’s different."
    blank "I swallow down that first pang of homesickness with a bite of food."
    blank "Not having eaten all day, though, the meal doesn’t last long and still Charlie’s done before I am."
    blank "I follow her out of the dining hall."
    scene bg black with dissolve
    scene hallway with dissolve
    show charlie flip at m1 with dissolve
    mc "You walk too fast."
    blank "I can barely keep up."
    charlie "That’s the pace around here. Speed up, or you get left behind."
    blank "And that is the only option, I realize, as I stumble into stride with her."
    $ charlieface = 'neutral'
    show charlie flip at m2 with dissolve
    charlie "You’ll want to be in your dorm. Magi Shira will come around soon, once she's done with dinner."
    mc "For what?"
    blank "Charlie just gives me a wicked look."
    $ charlieface = 'flirty'
    $ charliepose = '2'
    show charlie flip at m1 with dissolve
    charlie "I told you, you’ll see."
    $ charliepose = '1'
    show charlie flip at m2 with dissolve
    charlie "I'm not going to ruin your surprise. "
    blank "She pats me on the shoulder with a look that I can only describe as friendly and ominous. "
    charlie "Have fun. "
    blank "That’s all the goodnight I get as she takes off toward her own room at that same relentless speed."
    scene bg black with dissolve
    scene dormroom_night with dissolve
    blank "Digging through my bag, I tuck a few clothes into the dresser--mostly with the intent of hiding them."
    blank "I want to squirrel them away for when I’m back to my old self."
    blank "Moving to the mirror, I check over myself again, pinching my cheeks and carding my fingers through the ends of my hair."
    blank "And tugging down that damn skirt again!"
    think "No one seems to suspect anything so far...not even Charlie."
    think "Maybe it's alright. Maybe I'm just overthinking things and nobody cares. "
    blank "A brisk knock interrupts me."
    shira "Sophie, may I come in?"
    mc "Uh, sure."
    $ shiraface = 'happy'
    show shira at m1 with dissolve
    shira "Good evening."
    shira "How are you adjusting?"
    mc "Uh...slowly, I think."
    mc "I’m not really sure what to do about clothes."
    $ shirapose = '2'
    show shira at m2 with dissolve
    shira "For now, rely on your uniform and school robes. I’ll arrange something soon to get you more suitable clothes."
    shira "If you wouldn't mind, take a place on the bed."
    blank "She gestures. "
    mc "What's going on exactly? "
    $ shirapose = '1'
    $ shiraface = 'neutral'
    show shira at m1 with dissolve
    shira "I'm going to perform a ritual on you. If you'll take off your clothes?"
    mc "What!?"
    blank "I bunch the bedcovers covers up around my chest, like she might try to get a peek."
    shira "...Well, you certainly are learning fast, aren't you? "
    $ shirapose = '3'
    show shira at m2 with dissolve
    shira "Perhaps I should explain first. "
    shira "Again, I do get into the habit of this until it all seems quite mundane. "
    blank "She at least offers an apologetic smile, but alarm bells are still echoing in my head. "
    think "I'm still not used to looking at my own boobs yet, let alone someone else!!"
    $ shirapose = '1'
    $ shiraface = 'happy'
    show shira at m1 with dissolve
    shira "Listen before you panic. "
    shira "One of the principle qualities of magic is that it has to be controlled. "
    shira "The better your focus, the more powerful and accurate your spellcasting can be, which is crucial to success here. "
    shira "But magic is chaotic energy by nature, and highly unpredictable. "
    mc "...And what does any of this have to do with me getting naked? "
    shira "Be patient. I'm getting there. "
    $ shiraface = 'neutral'
    show shira at m2 with dissolve
    shira "There are rituals that can help you focus control and reign in magic that would otherwise be unpredictable. "
    shira "It takes chaotic energy and processes it, making it easier to wield, which is helpful for those still learning. "
    shira "Unfortunately, it requires there be no barrier between the subject's skin and the caster's hand. "
    shira "I'll close my eyes, if you prefer. "
    mc "Uhm..."
    blank "The idea spins around my head. "
    think "If it's to make me stronger, well...I've already sacrificed a lot for that. "
    think "Really, what's a little more indecency and shame at this point? "
    mc "It doesn't really feel like my body, so..."
    think "It's not like she's looking at the real me naked..."
    $ shirapose = '3'
    show shira at m1 with dissolve
    shira "And still, I think you'd be a little more comfortable if I didn't look. How about you turn around for now? "
    $ mc_clothes = 2
    blank "Nervously, I strip off my outer layer of clothes as Magi Shira circles me, pacing slowly around the bed."
    blank "My breath hitches in my throat."
    think "Does she have to do this so...so...sensually?"
    blank "She reaches out, a soft hand grazing over the bare skin of my arm."
    scene scene9a with dissolve
    blank "Beneath it, I can feel the magic sinking in, a deep and warm tingle spreading through my veins."
    blank "Wherever it sweeps, heat follows, and then a drowsy numbness."
    think "Ohh…"
    blank "It’s a bit of a strange sensation at first."
    blank "She offers me a small smile."
    mc "Do I have to take off my underwear, too?"
    shira "No, there’s no need to touch every inch of your skin. Just enough to balance the energy."
    mc "There…"
    blank "Her voice has grown so soft, it almost lulls me to sleep by itself."
    scene scene9b with dissolve
    blank "Her fingers move over my collarbone, and then slide across the front of the bra."
    blank "My cheeks flush warmly as that tingle settles into places unexpected."
    think "I-Is that supposed to happen?"
    blank "My embarrassment keeps me from asking any questions, as her hands trail down and curve along my navel."
    blank "Warmth pools there after her touch, and tingles low between my legs."
    think "Unngh…"
    think "This can’t be normal..."
    blank "Desperately trying to distract myself from the strange, phantom sensation coiling in my belly, I do the thing I do best when nervous."
    blank "I run my mouth."
    mc "It’s a lucky thing the school gives us underwear, I guess."
    shira "They don’t."
    mc "...Wait, what?"
    scene scene9a with dissolve
    shira "Those are mine. I had them brought here with the uniform."
    shira "I knew you wouldn't have any, after all..."
    think "Th-th-these are her panties!?"
    shira "They’re clean, I promise. No need to look so traumatized."
    mc "That’s not really the problem!!"
    think "Has she forgotten that once upon a time, a.k.a. YESTERDAY, I was a guy?!"
    think "A complete, authentic, vaguely perverted guy."
    think "And despite the physical differences, I don’t think that has changed much!!"
    blank "I decide to just keep my mouth completely shut, as her hand wanders back up."
    blank "The fact that I can’t feel my toes doesn’t seem remotely important in the grand scheme of things."
    shira "Lie on the bed. This will probably start putting you to sleep soon."
    mc "Are you going to tuck me in a read me a bedtime story, too?"
    blank "The sarcasm isn’t appreciated."
    blank "Her fingers touch against my forehead, and the dizzying, warm sensation suddenly clouds over my senses."
    scene bg black with dissolve
    blank "I have no choice but to lay back. It’s either that or fall, as the feeling clouds over my senses."
    blank "I blink up into Magi Shira’s face, feeling so strange, as if I’m floating. Flying."
    blank "She says something, but I can’t comprehend it, just watching her glossy lips move."
    blank "Then she’s gone."
    blank "I spend the last of my energy pulling the covers over me."
    scene bg black with dissolve
    blank "Then nothing."
    scene dormroom_day with dissolve
    $ mc_clothes = 2
    think "Nng…"
    mc "Ahhhh."
    blank "A feeling of peaceful, drowsy wakefulness sweeps over me, as a bell chimes distantly in the school."
    blank "My body feels so light; I don’t want to move at all, knowing it'll shred the thin, comfortable veil of sleep still wrapped around my mind."
    blank "Whatever Magi Shira did last night...I highly recommend it..."
    charlie "As much as creeping on you is really stroking my ego here, we gotta go."
    blank "I jolt upward."
    mc "Charlie!?"
    $ charlieoutfit = 'robes'
    $ charlieface = 'annoyed'
    $ charliepose = '2'
    show charlie flip at m1 with dissolve
    charlie "Hello?"
    mc "Why are you here!?"
    charlie "I knew you’d be out of it and oversleep. Thought I might actually do you a favour so you won’t be late."
    charlie "You know...to make up for how honest I was yesterday."
    mc "...B-but how did you get in here?"
    mc "Didn’t Shira lock the door on the way out?"
    $ charlieface = 'neutral'
    $ charliepose = '1'

    show charlie flip at m2 with dissolve
    charlie "...This is a school of a magic, you know. Locks aren’t exactly the biggest hindrance."
    charlie "Get up!"
    blank "My feet remember what it’s like to move as I scramble up...and then realize how much skin I’m showing. "
    mc "Don't look!"
    blank "I stumble like a new-born calf toward the bathroom, my legs not yet catching up with the rest of my body."
    blank "I end up sprawled uselessly across the floor, staring up the ceiling until a pile of cloth falls over my face."
    scene bg black with dissolve
    charlie "There’s your robes, by the way."
    charlie "We’re practicing magic today, so you’ll want to show up in those."
    charlie "Better get ready quick, otherwise I’m bailing and heading to class on my own."
    charlie "I’d give you instructions to get there, but you’d probably get so lost we’d never see you again."
    charlie "Bye~"
    scene bg black with dissolve
    scene dormroom_day with dissolve
    mc "Auuuuuugh."
    think "Why does my only classmate have to be a jigsaw puzzle of cryptic intentions?"
    think "I can’t decide if she wants to befriend me or just wants the best seat possible as she tortures me."
    blank "But as I glare up at the ceiling, a firm determination settles over me."
    think "If she wants to test me, then fine. Let her."
    think "I’ll pass."
    blank "…"
    blank "I get ready in what must be record time."
    $ mc_clothes = 2
    blank "Even pulling what must be another pair of Magi Shira’s panties out of the drawer doesn’t slow me down."
    blank "I scrub down until my skin is pink, mouth set in a grim line as I refuse to let anything--anything at all--distract me."
    blank "Post-shower, I flick out a towel, magic sending a wave of heat through it as I scrub it into my hair to dry it."
    blank "...And dry it."
    blank "And dry it some more."
    think "How long does this take!?"
    think "Alright, forget it!"
    $ mc_clothes = 6
    blank "I wring out as much excess water as I can with my hands, then pull on my robes."
    blank "They feel heavy, denser."
    blank "Good for protection against most practice spells, I bet."
    blank "With an efficiency that would probably make the royal guard proud, I finish getting ready and head toward Charlie’s dorm."
    scene bg black with dissolve
    scene hallway with dissolve
    $ charlieoutfit = 'robes'
    show charlie flip at m1 with dissolve
    charlie "About time. Let’s go."
    think "About time? About time!? I’m practically out of breath!!"
    blank "But I try not to show it, following Charlie through the hallway."
    scene bg black with dissolve
    scene classroom with dissolve
    blank "...And then right to the same classroom that Magi Shira showed me yesterday."
    mc "How would this have been difficult to find!?"
    $ charlieface = 'flirty'
    show charlie at l2 with dissolve
    charlie "It wouldn’t have. I just wanted to get you out of your room faster."
    blank "She slides her hands into her pockets with a smug grin."
    charlie "You’re too easy."
    mc "And you’re...you’re…"
    $ shiraface = 'happy'
    $ shirapose = '2'
    show shira at r1 with dissolve
    shira "Here early."
    $ shirapose = '1'
    show shira at r2 with dissolve
    shira "Excellent."
    $ charlieface = 'neutral'
    show charlie at l1 with dissolve
    blank "Charlie’s smug look only intensifies as she turns toward Magi Shira, too."
    blank "I couldn’t hear the click-clack of her approaching heels over the sound of the steam whistling out my ears."
    blank "Standing straight and firm, Magi Shira observes us both."
    shira "Good, you look prepared, now follow me."
    scene bg black with dissolve
    scene hallway with dissolve
    $ shiraface = 'neutral'
    show charlie at l1 with dissolve
    show shira at r2 with dissolve
    shira "As these are our first lessons together as a group, we will be practicing in the arena."
    shira "It will be good for you both to get used to this place in case you pass your entrance test. "
    shira "As next year you will have to spend a lot more time in here, in battle."
    mc "Really?"
    shira "Yes, as you should know by now, the primary event that goes on in the school, is the Magi Wars tournament."
    scene bg black with dissolve
    scene arena with dissolve
    show shira at r2 with dissolve
    show charlie at l1 with dissolve
    shira "Here we are."
    shira "Charlie and I have been doing some basic drills before you joined us, Sophie."
    shira "And just as with Charlie, I always start my students out on defensive drills."
    $ shirapose = '3'
    show shira at r2 with dissolve
    shira "It’s paramount that you be able to protect yourself if you’re expected to go on to compete in the Magi Wars."
    blank "I nod in understanding."
    shira "Summon a defensive barrier."
    think "This is it. This is really it. My first magic lesson at the Academy!!"
    scene bg white with dissolve
    think "Focus, focus, focus. "
    scene scene10a with dissolve
    blank "I will my magic outward in an arc, forcing it to replenish over and over. "
    blank "Mine ripples with waves of power, while Charlie’s appears more like a grid work of connected, intense lines."
    think "Why does hers look so much different?"
    shira "You have good instincts, Sophie."
    shira "But unacceptable. "
    think "Unacceptable!?"
    shira "Instincts aren’t always enough."
    scene scene10a with vpunch
    blank "The blast of magic strikes before I can even react, launching me backwards."
    scene bg black with hpunch
    blank "It doesn’t have half of the power as it did when we actually sparred, but I still end up in a heap."
    scene arena with dissolve
    think "Tch…"
    think "W-why didn’t it work?"
    blank "I glance up, surprised, as Charlie extends a hand over me."
    blank "I take it and pull myself up with a wince."
    show charlie at l1 with dissolve
    think "So much for a good impression.."
    show shira at r2 with dissolve
    shira "A rookie mistake. You perform defensive spells as if you only read about their most basic properties in a text book."
    shira "Your magic fluctuated, and even then its pattern was predictable."
    shira "Striking at the right moment allowed me to knock you back as if you had no defence at all."
    show shira at r1 with dissolve
    shira "Notice how Charlie’s defences don’t have that flickering quality, as she's doing the spell correctly. "
    show charlie at l2 with dissolve
    blank "The praise causes the girl to flash a pleased grin at me, the webbed barrier throwing patterns of light over her face."
    show shira at r2 with dissolve
    shira "Structuring your defence makes it more solid, less prone to flickering."
    think "Magic is more complex than I had realized."
    shira "I will have you practicing this until you reach perfection! There is no room for laziness in my classroom. "
    show shira at r2 with dissolve
    shira "Now, again!"
    scene bg black with dissolve
    scene arena with dissolve
    blank "Charlie and I work as if we're training for the royal guard, rather that a simple Initiate Test. "
    think "Is she always like this!?"
    blank "Shira goes on about how the magic feels, about the slight movements and concentrations that are required to form a perfect shield in an instant."
    think "And this is just day one…"
    think "Jeez."
    blank "But for all its difficulty, I wouldn’t trade studying it for anything."
    blank "After a desperate hour of practice and shame, I finally get my shield to at least resemble the one Charlie had been practicing."
    think "I’m not going to let her show me up, not on the first day."
    $ shirapose = '3'
    show shira at r2 with dissolve
    show charlie at l2 with dissolve
    shira "We will change things up, now that you both understand the skill. "
    shira "Charlie, test Sophie’s defences yourself."
    show shira at r1 with dissolve
    shira "See how she fares against your assault."
    think "What!? I'm Charlie's punching bag all of a sudden!?"
    $ shiraface = 'determined'
    show shira at r2 with dissolve
    shira "Sophie, feel free to attack or defend. Simply win the fight with no severe harm."
    shira "You’re testing your abilities to attack and defend, not create a bloodbath with each other."
    think "Is it just my imagination, or does Charlie seem a little disappointed about that?"
    think "...Man, I've gotta watch my back with this one. "
    blank "I glance over at my new rival. "
    menu:
        "Good luck.":
            $ charlieface = 'annoyed'
            show charlie at l1 with dissolve
            charlie "Luck? "
            charlie "Don't even need it. "
        "Don't hold back.":

            $ charlie_love += 1
            charlie "Hold back? For you?"
            $ charlieface = 'happy'
            show charlie at l1 with dissolve
            charlie "Wouldn't dream of it. "
            blank "I smirk in return. "
            mc "Good. You won't be able to afford to. "
            blank "She scoffs playfully. "

    charlie "Hope you have a high pain tolerance and brought some bandages with you."
    $ charliepose = '2'
    $ charlieface = 'flirty'
    show charlie at l2 with dissolve
    charlie "It’s gonna be a bumpy ride, once I knock down that lump of a shield."
    mc "You talk a lot. Means you’re better at making threats than carrying them out."
    charlie "Good, keep underestimating me. I like it that way."
    charlie "Makes your expression all the better when I knock you on your--"
    shira "Ahem."
    think "Right. Back to business."
    $ charliepose = '1'
    show shira at r1 with dissolve
    shira "Let’s see what you’ve got, then."
    blank "We stand apart from each other, taking our respective places."
    blank "Charlie’s smile, infuriating as it is, stays in place as she stares me down."
    shira "When you’re ready…"
    shira "3, 2, 1..."
    shira "Begin!"
    scene bg black with dissolve
    scene scene11a with dissolve
    blank "Charlie’s spell breaks off from her hands, a stream of missiles striking the front of my barrier."
    blank "Her smile turns into a grimace at the resistance, before another series of basic attacks leave her fingertips."
    blank "I brace for them, willing the magic to make a solid, cohesive grid."
    think "Nnngh--"
    scene scene11b with vpunch
    blank "The strikes hit in close succession as I will all my power to reinforce the shield, until the last strike dissipates."
    blank "It hits so hard, my teeth chatter in response as the shock vibrates along my arm."
    blank "I fend each attack off, but drop the shield a moment later."
    blank "My wrists hurt to the bone."
    scene bg black with dissolve
    scene arena with dissolve
    play music "music/track12.ogg" fadeout 1 fadein 1
    show charlie at l2 with dissolve
    show shira at r2 with dissolve
    shira "Excellent job, Sophie."
    shira "As we get more specialized in shields, you’ll learn how to direct your magic to repel in smaller, more concentrated areas."
    shira "Covering your entire body with a defence isn’t economical. As you realized, you couldn’t hold it for very long."
    $ charlieface = 'flirty'
    show charlie at l1 with dissolve
    charlie "Mmm, you were having some performance issues there."
    mc "You didn’t get through!"
    $ charliepose = '2'
    show charlie at l2 with dissolve
    charlie "Sure I did. I just didn’t attack you after you dropped the shield because I didn’t want to mess up your pretty face."
    think "...Is that sarcasm or is my face actually pretty? "
    think "Oh, what does it matter!? Pay attention!!"
    shira "Being able to defend is necessary, but ultimately pointless if you can’t balance it with attacking."
    shira "Resume your places. Spar with each other in the same way you did with me when you first arrived."
    $ charliepose = '1'
    $ charlieface = 'neutral'
    show charlie at l1 with dissolve
    charlie "Oh, goody. And here I thought we were going to have to keep the sparring to the verbal variety."
    mc "You better hope you’re better at the physical kind."
    blank "We stand apart from each other again as I shake out my hands."
    think "Come on. I need all I can get right now."
    blank "For a moment I wait and watch, trying to judge what kind of fighting style Charlie’s going for--"
    blank "I don’t wait long."
    scene scene11c with vpunch
    blank "Her same basic force attack launches itself at my head only a second later."
    menu:
        "Shield.":
            blank "I dip below the wave of magic and raise my shield again."
            scene scene10b with hpunch
            think "I think I singed some of my hair… But it held."
            scene scene11d with dissolve
            blank "Swiftly sidestepping her second attack, I fire back one of my own."
            scene scene11e with hpunch
            blank "It catches her in the arm."
            shira "Excellent work, Sophie. Keep it up."
            shira "Charlie, you need some variety."
            shira "She knows what you’re doing, so change tactics."
            blank "But she doesn’t change anything, as I try to dance around the attacks and return fire."
            blank "Then I realize when she changes it up, she doesn’t move at all, the shield coming up to shatter my attack."
            scene scene11g with vpunch
            blank "It dissipates as she jumps through it, her fist a glowing red as it aims straight toward my temple."
            blank "I don’t think to do anything except shield."
            blank "Hastily raising a barrier, but knowing it will be too weak to protect me."
            blank "Closing my eyes against the expected pain."
            blank "But nothing happens."
            scene scene11h with dissolve
            blank "When I glance up again, her glowing fist of energy still hovers about an inch from my head."
            blank "But another barrier stands between the two of us, forcing her hand back."
            blank "It trembles a little."
            think "Is that…?"
            blank "Shira is watching us passively from the side, not seeming to have interfered."
            think "Then…"
            blank "Taking charge of this new power, it feels heavy and uncertain, like a newly discovered limb that’s always been asleep."
            blank "But with a powerful surge, I manage to push Charlie back, away from me."
            scene scene12b with dissolve
            blank "My magic surges over her, blasting her into the ground."
            shira "Impressive…"
            scene bg black with dissolve
            scene arena with dissolve
            $ shiraface = 'determined'
            show shira at r1 with dissolve
            blank "Shira has moved forward, to end the fight."
            $ shiraface = 'happy'
            show shira at r2 with dissolve
            shira "Where did you learn to do that, Sophie?"
            mc "Uh."
            mc "I didn’t. It just…"
            mc "It just kind of happened."
            $ shiraface = 'neutral'
            show shira at r1 with dissolve
            shira "Hmm."
            blank "Shira tilts her head at me, staring at me with such intent, I start to shrink beneath the gaze."
            think "Did I do something wrong?"
            scene scene12b with dissolve
            blank "Charlie punches the ground as she gets up."
            charlie "I want a rematch!!"
        "Fire back.":

            blank "I don’t know what compels me to do it."
            blank "My instincts tell me to shield."
            blank "The lesson tells me to defend myself."
            blank "And instead of heeding either of those impulses, a spark of wild energy ignites in my curled hand."
            mc "Rraagh!!!"
            scene scene11f with dissolve
            blank "I hurl it fiercely toward Charlie, "
            blank "The two magic's inter-mingling as we try to hit each other, neither of us shielding."
            blank "And to my astonishment, it rips through her assault like paper, burning it up and keeping its course toward her."
            think "What the!?"
            blank "She raises her hands to defend herself, but the shield is thin at best."
            blank "It doesn’t hold up, the strike catching her right in the stomach."
            blank "She lets out a startled cough, slumping over, but that doesn’t stop her from hurling another attack my way."
            blank "Her magic must have taken the brunt of my attack, because the hit didn’t slow her down any."
            scene scene11i with hpunch
            blank "Attack after attack."
            think "Oh, God."
            think "This is revenge, isn’t it?"
            blank "My defences get weaker and weaker, each attack illuminating a pattern across my shield that starts to look like cracked glass."
            blank "She storms toward me, one step, one attack at a time, before she pauses--drawing her power."
            blank "I clench my eyes, forcing every ounce of magic I have ahead of me, suspending it between my fingers."
            scene bg white with dissolve
            blank "The shield shatters between them."
            blank "I take a breathless hit to the chest."
            scene bg black with dissolve
            blank "And the shoulder."
            blank "And the knee."
            scene scene12a with dissolve
            blank "I roll over on the ground, trying to cover myself up as the punishing burns erupt over my body and burn red."
            $ mc_clothes = 2
            shira "Enough, Charlie."
            blank "Magi Shira steps between us abruptly, Charlie’s last attack pinging harmlessly off an unseen force."
            think "You couldn’t have called her off a little sooner!?"
            blank "I slump on the ground with a sigh, watching the steam rising off of my skin."
            think "Great…"
            shira "That first move was unexpected, Sophie."
            shira "Where did you learn to do that?"
            blank "I peel myself off the ground, massaging the newly tender skin on my chest without thinking much about it."
            mc "I just...it felt like it made sense. I felt like if my magic was stronger than hers, I could defend from it and attack all at once."
            scene bg black with dissolve
            scene arena with dissolve
            $ shiraface = 'neutral'
            $ shirapose = '3'
            show shira at r1 with dissolve
            shira "It’s a risky manoeuvre, but not an invalid one."
            shira "Though certainly not something I would have suggested for someone at your current skill level…"
            shira "The accuracy alone is difficult to master, and the technique a bit controversial…"
            shira "It takes a lot of energy to accomplish something like that."
            mc "Really? Maybe I really benefitted from that ritual last night."
            blank "Shira’s gaze lingers on me curiously."
            $ charlieface = 'annoyed'
            show charlie at l1 with dissolve
            charlie "You know I won right? Or should I proove it again?"

    scene bg black with dissolve
    scene arena with dissolve
    $ mc_clothes = 6
    show shira at r1 with dissolve
    shira "Now, now."
    shira "You’ve antagonized each other enough."
    shira "You’re both under my tutelage. You will be expected to work together."
    charlie "A little friendly rivalry never hurt anybody…"
    shira "Nevertheless, we’ll next do a team-building exercise, for the sake of you two not slaughtering each other."
    shira "But first, you should both know the appropriate spell to sort out your clothes."
    scene bg black with dissolve
    scene arena with dissolve
    blank "Both of us realise the state of our robes and quickly go about summoning the power to repair the damage."
    $ shirapose = '1'
    $ shiraface = 'happy'
    show shira at m1 with dissolve
    shira "Good, now instead of guarding yourself, you will practice guarding another person."
    shira "This techniques involves projecting your magic further and maintaining the same steady control and equal dispersion."
    shira "No weak spots, Sophie."
    blank "I nod."
    $ shirapose = '3'
    $ shiraface = 'neutral'
    show shira at m2 with dissolve
    shira "The stakes are always higher when other people are involved. We’re prone to get clumsy and to act rashly without thought."
    shira "These are impulses you can’t give into."
    shira "The stakes may be higher, but your odds are also better."
    hide shira with dissolve
    blank "We run through a series of drills, working on shifting our magic further from ourselves and relying less on the physical sensation of holding the shield in place."
    blank "It’s tricky…"
    blank "But I seem to pick it up faster than Charlie, whose shield keeps flickering out of existence about two feet from her."
    mc "Come oooon. This is the one thing I actually need you to be better than me at!"
    blank "Magi Shira ignores our complaints and bickering with a stony expression and an intense silence, until we both succumb to the look and refocus."
    shira "Alright, Sophie."
    shira "Cast a shield around Charlie."
    mc "Yes, ma'am. "
    mc "Succeed or bust."
    blank "Shira readies herself to attack and I don’t have any time at all to prepare."
    blank "My hands fly together, stumbling through the motions as fast as possible."
    scene bg white with dissolve
    blank "A white light flashes from my hands."
    blank "But as the white spots dissapear, instead of seeing a shield, I can see something very different."
    scene scene13a with dissolve
    think "……"
    think "Wh-...what…?"
    charlie "Uh…?"
    shira "Oh my..."
    blank "It takes her a long moment to realize, searching each of our faces with confusion. "
    $ charlieoutfit = 'underwear'
    charlie "SOPHIE, WHAT THE HELL DID YOU DO!?"
    menu:
        "I utilized the element of surprise.":
            $ charlie_love += 1
            think "And boy did I get a surprise."
            blank "Charlie stands there stunned, but I can’t help but stare."
            blank "She doesn’t even make an attempt to cover up, which just invites my stupid ogling."
            charlie "When you said succeed or bust…"
            mc "This really wasn’t the bust I had in mind, I swear."
            scene scene13b with dissolve
            blank "And though I’m fully braced to be punched in the mouth, Charlie just starts laughing."
            think "Talk about an ice-breaker…"
            think "If this is what team building exercises are like, I want to do more of them."
            charlie "How did you manage this!?"
            blank "I have no answer. "
            charlie "I knew I was doomed, but I didn't think you'd make me die half-naked. "
            blank "She glances down at herself. "
            charlie "Do you feel committed to the team spirit now?"
            blank "She gives a playful little shake, despite the colour that’s tinting her cheeks."
            think "If only she knew who she was really showing off to."
            mc "I think this is a good team strategy, don’t you? No one will see it coming."
            mc "It’s the perfect way to gain the upper hand."
            charlie "Well, aren’t you just a tactician all of a sudden? If I didn’t know better, I’d say you like it."
            think "I do like it."
            think "And I shouldn’t be liking this at all!"
            think "And Shira-- Oh, Gods, Magi Shira probably realizes just how terrible I am."
            think "Does this count as taking advantage of Charlie’s ignorance? Probably. It probably counts as a lot of things."
            think "Namely sexual harassment, but let’s not get too specific."
            blank "I try to look away, studying the ceiling or the patterns on the floor with intensity."
            blank "But none of those things have supple curves and a penchant for snarky, dry comments."
            charlie "Really, though, how did you manage to mess up THIS badly? Please tell me you meant for this to happen."
            charlie "I’m not even upset."
            charlie "I think I’m beyond a definable range of emotions at this point."
            charlie "You were supposed to defend me. Instead, you took away the only defence I had!!"
            mc "I’m not that terrible! I just...t-that’s just not how it’s supposed to work."
            charlie "What was your first clue…?"
            blank "She shakes her head."
            blank "Blushing, I glance down at my hands in bewilderment."
            think "Man, how did I even do that!? I might need this for...for future reference or something. Purely academically, of course."
            charlie "You didn’t even get rid of my clothes. I just can’t see them."
            blank "She rustles fabric that doesn’t appear to be there."
            shira "Sophie changed the properties of the robe, she didn't get rid of the robe itself."
            blank "Even Shira looks a bit flustered. And isn't she the one always going on about being used to seeing naked students or whatever? "
            blank "This is seriously the weirdest school. "
            blank "I'm gonna fit right in."
            charlie "Can you fix it or do I have to learn magic in my underwear from now on?"
            scene bg black with dissolve
            scene arena with dissolve
            $ shirapose = '1'
            $ charlieface = 'blush'
            $ charliepose = '2'
            show shira at r1 with dissolve
            show charlie at l1 with dissolve
            shira "Stand still a moment I should be able to clear a simple vanishing."
            think "I wouldn’t object."
            blank "To my mild disappointment, a few muttered words and Magi Shira has Charlie’s robe back intact."
            $ charlieoutfit = 'robes'
            $ charlieface = 'happy'
            $ charliepose = '1'
            show charlie at l2 with dissolve
            charlie "Alright, now show me how you did it!!"
            mc "It was an accident! Why do you need to know!?"
            charlie "Because fair’s fair!"
            mc "Nooo!!"
            mc "Why are you so much more docile with your clothes off!?"
            charlie "Alright, that’s it!" with vpunch
            blank "A fireball goes streaking past my head and nearly takes my nose and eyelashes with it."
            blank "Shira sighs."
            shira "Students, please avoid setting each other on fire."
            scene bg black with dissolve
            blank "We spend the rest of the afternoon trying to advance our defensive spells...and not turning anyone’s clothes invisible."
            blank "That’s the sad part. I can’t even recreate it if I try."
            blank "N-not that I did try or anything."
        "I’M SORRY!!!":

            mc "I really didn’t mean to do that!!"
            mc "It was a complete accident, I swear!"
            mc "I was just trying to summon a shield like we’d been doing, I...I didn’t even know this was possible!"
            blank "Charlie huffs, looking down at herself again."
            charlie "Mhm. Sure you didn’t. Because those two things are so easy to mix up."
            mc "It’s true!!"
            mc "I really didn’t know and I’m so, so sorry. I don’t want you to think I did it on purpose."
            charlie "Okay, okay. I was kidding, you know, it’s fine-"
            mc "It’s not!"
            mc "I’m not a creep, I swear! Please don’t think that about me!"
            blank "I practically fall to my knees."
            charlie "Uhhhhhh."
            charlie "The more times someone has to say they’re not a creep, the more likely they’re a creep."
            charlie "It grows exponentially like that. Why would I think you’re a creep anyway?"
            mc "But I just...I didn’t mean for it to..."
            charlie "You’re seriously freaking out about this. Chill out. You’re the one making it weird now."
            charlie "We’re all girls here, right?"
            blank "…"
            think "Uhhh."
            think "Well, this settles it. I’m going to hell."
            blank "My expression must say just how uncomfortable I am, because Charlie frowns at me all the more."
            think "Shouldn’t she be the one concerned about this!?"
            charlie "Magi Shira, can I get my robes back before Sophie bursts a blood vessel?"
            shira "I think that would be best."
            blank "She strides toward Charlie as if nothing is amiss."
            blank "Though given the ritual I went through last night, I’m guessing this isn’t all that unusual..."
            charlie "I can still feel the robes on me, they’re just...I just can’t see them."
            shira "I believe I can fix this."
            blank "With just a few waves of Shira’s hands, the colour bleeds back into the heavy fabric."
            $ charlieoutfit = 'robes'
            scene bg black with dissolve
            scene arena with dissolve
            $ charlieface = 'annoyed'
            show shira at r1 with dissolve
            show charlie at l1 with dissolve
            shira "There."
            shira "Now, can we resume training and keeping all our clothes on?"
            blank "She gives me a pointed look."
            think "It really was an accident, though!!"
            blank "I fall into place quickly and quietly, a little anxious about trying that spell again."
            blank "It doesn’t help that I can’t look at Charlie without my face finding a new shade of red."
            think "I really wish I hadn’t seen that…"
            think "I can’t get it out of my head."
            blank "We fall back into the routine once more, but it's not the same. An awkwardness settles over us."
            think "Charlie isn’t nearly as outgoing as she was initially. I think I might have actually managed to weird her out."
            think "Ugh, I can’t focus on any of that!"
            think "I have to get this right so it doesn’t happen again!"
            scene bg black with dissolve
            blank "We spend the rest of the session practicing those defensive spells, and much to my relief, I get better at them and Charlie remains clothed."
            blank "We spend hour after hour, drilling the defences into our heads."
            blank "There’s no such thing as a break with Magi Shira. If we’re not practicing magic, we’re reading about it."
            blank "We have 30 minute rest periods between practical lessons."
            blank "By the time we finish, I’m completely exhausted."
            blank "My legs hurt. My arms hurt."
            blank "Parts of my body I didn’t use hurt."

    scene bg black with dissolve
    scene dininghall with dissolve
    play music "music/track04.ogg" fadeout 1 fadein 1
    $ charlieoutfit = 'uniform'
    $ mc_clothes = 8
    $ charlieface = 'neutral'
    show charlie at l1 with dissolve
    blank "Reluctant and sore, Charlie and I change and drag ourselves into the dining hall at Magi Shira’s insistence."
    charlie "I’m too tired to look at food."
    charlie "I’d rather use my tray as a pillow."
    mc "Magi Shira said it’ll help us recover our magic faster. Come on-"
    mc "Oh!"
    show warren flip at r2 with dissolve
    blank "I glance up hastily, meeting a disapproving stare that chills my blood."
    mc "Uh.."
    think "Mage Warren."
    blank "I slammed right into him, yet I was the one who nearly stumbled backwards onto the floor."
    blank "Under those eyes, I suddenly feel like it’s a good idea to study our shoes instead."
    blank "My hand twitches to pull down my skirt, but Charlie slaps it away stealthily."
    $ warrenpose = '2'
    show warren flip at r1 with dissolve
    warren "I remember you from yesterday."
    warren "You’re Shira’s newest pet project."
    blank "Not a warm greeting."
    blank "I only met Warren briefly, but even in that amount of time, he left a certain...impression."
    blank "And he’s doing good at keeping it. His gaze drags over me, like a predator picking out a weak point."
    blank "He adjusts his robes with a huff."
    $ warrenpose = '3'
    show warren flip at r2 with dissolve
    warren "Be careful."
    think "Me!? If he’d been paying attention, this wouldn’t have happened either! Blame is a two-way street!"
    blank "Which are not the sort of things you say to a teacher at your new academy."
    blank "…And that's not the sort of helpful, practical sense my brain usually consults before opening my mouth."
    blank "I scoff, sorting between the number of stupid things I can say."
    blank "Charlie slams her foot against mine, and a smile curls over my face to try and hide the tears that just sprang into my eyes."
    mc "Y-yes, sir."
    blank "It’s all I can manage."
    blank "He makes little reply as he sweeps off."
    warren "Good."
    hide warren with dissolve
    blank "The terse word is muttered in parting, and then just as abruptly as I ran into him, he vanishes again."
    mc "Was that necessary?! You owe me a new pinkie toe!!"
    $ charliepose = '1'
    show charlie flip at m2 with dissolve
    charlie "Then you owe me your ass."
    charlie "You’ve barely been here 24 hours, but you get a look when you’re about to do something spectacularly stupid."
    $ charlieface = 'sad'
    show charlie flip at m1 with dissolve
    charlie "It’s like you turn your brain off."
    charlie "Besides, why would you want to make Mage Warren mad? He already has it out for us."
    mc "Oh. At least I’m not the only one he hates."
    mc "Why?"
    $ charliepose = '2'
    $ charlieface = 'annoyed'
    show charlie flip at m2 with dissolve
    charlie "Well, it’s less to do with us and more to do with Shira."
    blank "We move through the line, piling up our plates with food as Charlie drags me into the gossip."
    charlie "I don’t know where it comes from, really, but it’s like they have some kind of rivalry going on."
    mc "I noticed that when I showed up, too. He mentioned the fact that Magi Shira was taking on another apprentice."
    $ charlieface = 'blush'
    show charlie flip at m1 with dissolve
    charlie "I bet they’re together."
    mc "...You’ve lost me."
    charlie "I had a few lonely days to think about this theory too much, don’t judge."
    charlie "But isn’t it a nice disguise? Pretend you hate each other’s work so the boss doesn’t suspect you’re together."
    mc "Can teachers not be in relationships with each other?"
    blank "She shrugs."
    $ charliepose = '1'
    show charlie flip at m2 with dissolve
    charlie "How would I know? Like I said, it was just a theory."
    charlie "She seems too up-tight to admit she’s in a relationship. And from what I can tell, he’s worse than she is."
    charlie "But if it’s true, she still has good taste, don’t you think?"
    blank "…?"
    $ charlieface = 'flirty'
    show charlie flip at m1 with dissolve
    charlie "You know."
    blank "She smirks and nudges me in the side."
    blank "…"
    mc "I don’t."
    blank "My blank stare must finally convince her that I really am an idiot, because her expression falls."
    $ charliepose = '2'
    show charlie flip at m2 with dissolve
    charlie "He’s not exactly the worst looking guy around."
    charlie "Don’t you think so?"
    mc "Uhh."
    charlie "Total catch if you’re into the real strict disciplinarian types."
    blank "..."
    $ charlieface = 'happy'
    show charlie flip at m1 with dissolve
    charlie "What? Wouldn’t you bang him?"
    mc "N-no, that’s gross!!"
    blank "She laughs."
    charlie "What are you talking about, it’s gross?"
    mc "Because he’s...he’s a…"
    $ charlieface = 'neutral'
    show charlie flip at m2 with dissolve
    charlie "A teacher? That just adds to the fun."
    mc "What!?"
    mc "How often have you--"
    blank "Abruptly, Charlie starts laughing, clearly pleased with herself."
    $ charliepose = '1'
    show charlie flip at m1 with dissolve
    charlie "At this point, I’m just dragging reactions out of you."
    charlie "Are you still 12 or something that you can’t even talk about sex? He’s not gonna give you cooties."
    $ charliepose = '2'
    $ charlieface = 'blush'
    show charlie flip at m2 with dissolve
    charlie "I mean, I guess he won’t. I don’t know where he’s been."
    blank "She flicks me in the middle of my forehead."
    charlie "Poor, innocent Sophie."
    $ charliepose = '1'
    show charlie flip at m1 with dissolve
    charlie "Don't worry, I'll try not to give you a hard time."
    blank "Indignant, I’d love to prove to her just how innocent I’m NOT, but that would involve a lot of other weird confessions."
    blank "Instead, I slam my new tray of food down onto the table and eat sulkily."
    blank "Charlie doesn’t pay it any mind."
    charlie "I’m just saying, Magi Shira isn’t bad, but I wouldn’t have minded Mage Warren, either."
    blank "Peeking up from over my salad, Charlie pulls open a roll nonchalantly."
    $ charliepose = '2'
    $ charlieface = 'neutral'
    show charlie flip at m2 with dissolve
    charlie "But he always takes the kids that’ve had formal magical training for an age and a half. I bet the parents pay him under the table, too."
    mc "You haven’t, either? Even though you grew up here?"
    charlie "Nope."
    blank "That’s all she says about it, and finishes her food with record speed again."
    think "Guess she changed her mind about not having an appetite…"
    blank "I still pick around my tray, but all I can think about is sleep…and not the kind Charlie keeps going on about."
    think "Is that the sort of opinion I’m supposed to have about guys now?"
    think "Dom types? Teachers?"
    think "...Is this normal?"
    blank "If just don’t have any inclination for that sort of thing at all. Thinking about Mage Warren sexually is like thinking about having sex with a cactus."
    blank "But Charlie in her underwear, on the other hand..."
    blank "I guess there are some things that didn’t change along with my body."
    think "At least that’s familiar territory…"
    scene bg black with dissolve
    scene dormroom_night with dissolve
    blank "I collapse on my bed the moment I’m within reach."
    blank "It takes the last of my energy to wave my hand toward the door, forcing it to slide shut on rusty hinges."
    think "Ugh."
    blank "And every time I close my eyes, I get another glimpse of Charlie disrobed."
    think "Ughhhhhhh."
    think "I really hope I didn’t mess things up between us already. More than they already were…"
    think "Being a girl is the worst."
    think "Or maybe I'm just the worst at it. "
    blank "I thrash around on the bed briefly, trying to get comfortable."
    blank "She didn’t even seem bothered by it, so why can’t I get it out of my head?"
    blank "It’s going to be a new, awkward slide in my embarrassing moments film roll."
    blank "The one that always plays at night when I’m trying to go to sleep, but instead relive every remotely awkward thing I’ve ever done."
    blank "A sharp knock interrupts it."
    think "Oh. Right."
    show shira at m2 with dissolve
    shira "Good evening."
    shira "How was dinner?"
    mc "I wasn’t very hungry."
    blank "She nods."
    $ shirapose = '1'
    show shira at m1 with dissolve
    shira "That happens the first week or so, usually. You’ll be expending more magic here than you ever have before."
    shira "Your body will get used to it and eventually you won’t be so tired."
    blank "Aware of what’s coming, I strip off my clothes as she speaks."
    think "Hopefully just going with the flow will make this more normal than it really feels…"
    blank "She comes to stand in front of me, looking down at me with one of those rare smiles."
    blank "Charlie’s words seem to echo in my head. Magi Shira isn’t bad."
    think "Did she mean just as a teacher, or in the same way she was talking about Mage Warren?"
    think "Because if she was, we definitely agree on that…"
    blank "I try to banish that thought, as the warmth of her fingertips spread through me again."
    blank "But it does bring back that mortifying miscast spell from earlier."
    mc "Have you already visited Charlie?"
    $ shirapose = '2'
    show shira at m2 with dissolve
    shira "I have."
    mc "Did she say anything? About the...incident?"
    $ shirapose = '1'
    show shira at m1 with dissolve
    shira "She didn’t mention it, no."
    mc "Ugh, I felt like such an idiot. I really didn’t mean to do it on purpose…"
    show shira at m2 with dissolve
    shira "Believe me, I highly doubt you could have accomplished something that complex intentionally."
    mc "...Thanks for the vote of confidence."
    shira "Do you think this ritual helped you today?"
    mc "I don’t know…"
    show shira at m1 with dissolve
    shira "The effects can be hard to notice immediately."
    shira "Give it time."
    scene scene9a with dissolve
    $ mc_clothes = 2
    blank "The warmth builds in me once again, making the world seem distant and hazy."
    blank "All the exhaustion from the last day finally crashes down on me."
    blank "In hindsight, it’ll make sense, my body swaying forward without my consent."
    blank "In the moment, it feels like Shira’s boobs just jumped up and latched onto my face."
    think "Mmph!?"
    shira "Oops. Careful, Sophie."
    scene bg black with dissolve
    blank "Shira gently guides me back onto the bed, keeping her hand steady on my back as she guides me down onto the bed."
    blank "I can still taste fabric and sexual awkwardness."
    shira "Go to sleep."
    shira "You have another long day ahead of you tomorrow."
    mc "Mmmrh. I think I have a long life ahead of me."
    blank "I feel her brush a few strands of hair away from my face."
    shira "With the path you’ve chosen, let’s hope so."
    scene entrance_day with dissolve
    $ mc_clothes = 8
    blank "My first week at the school passes quickly."
    blank "It’s not the smoothest sailing, of course. With magic, Shira tells me, it never is."
    blank "The change of pace surprises me the most."
    blank "Back home, everything we learned was so practical. Day to day use."
    blank "Here, it’s all survival."
    blank "I’m finally getting a real dose of what Shira and Charlie have been telling me about."
    blank "We drill through attacks. Attack, after attack, after attack."
    blank "We utilize the elements in our environment, manipulate shadows to our will."
    blank "And to think I was excited when I learned how to reattach a button to a shirt..."
    blank "When I sit at the lunch hall each day, I look around at the faces there, trying to rationalize that some of them are going to get hurt."
    blank "Some of them might even die."
    blank "So why are they all here, too? There can’t be this many people who feel like I do, can there?"
    blank "Admittedly, I guess most of them are like Charlie. They’ll get promoted to Mage or Magi and that’ll be the end of it."
    blank "But there have to a few who want to press on, who want to become a Sorcerer despite the odds and the risks."
    blank "No matter how real it becomes, it never turns me away."
    blank "Charlie still thinks it’s insufferable so we don’t talk about it."
    blank "We don’t talk about much, really, outside of magic and Shira."
    blank "It’s like we’re in our own little ecosystem, staring into the shark tank while gasping for water."
    blank "I sigh as I slide my tray in beside hers, sinking down into my usual seat."
    scene bg black with dissolve
    scene dininghall with dissolve
    $ charlieoutfit = 'uniform'
    $ charliepose = '1'
    show charlie flip at m1 with dissolve
    charlie "Your eyebrows are growing back in."
    charlie "Told you they would."
    blank "I grimace at the reminder of a...very small, manageable fire I may have accidentally started."
    mc "It’s not like it was an important room! And I did it a favour, getting rid of those hideous curtains."
    $ charlieface = 'flirty'
    show charlie flip at m2 with dissolve
    charlie "Spoken like a true pyromaniac interior designer."
    blank "I take a bitter sip of my drink, though inwardly I am a little relieved my eyebrows are coming back in."
    blank "It’s only been a couple days since we worked with fire magic, which isn’t something I think Shira is going to let me do again for a long time."
    charlie "Let me see."
    blank "She rubs a thumb over them, where the ends were singed and brittle."
    mc "It’s not like I need them anyway. I’m not exactly winning any beauty contests here."
    mc "I’ve been noticing it for awhile now."
    $ charlieface = 'neutral'
    show charlie flip at m1 with dissolve
    charlie "Noticing what?"
    blank "I pick around my plate."
    think "Why am I rambling on about this?"
    think "It’s not Charlie’s problem. It’s barely even a problem at all!"
    blank "She jabs me sharply in the side."
    $ charliepose = '2'
    show charlie flip at m2 with dissolve
    charlie "Talk."
    mc "Ow! What are you, the mob?!"
    mc "I just meant..."
    mc "None of the girls here really look the way I look."
    think "Which kind of makes sense, all things considered, but...it still gets to me, irrational as I know it is."
    mc "It’s been bugging me forever."
    think "And by forever, I mean barely a week, but let’s not get specific."
    mc "But I guess there's not really a reason for it. Maybe all city kids just look...different. "
    $ charlieface = 'sad'
    show charlie flip at m1 with dissolve
    charlie "Pfft. Of course there's a reason. "
    blank "She waves her fingers. "
    $ charlieface = 'happy'
    show charlie flip at m1 with dissolve
    charlie "Magic. "
    blank "I scoff."
    charlie "I’m serious. You don’t do any of the basic makeup tricks, do you? I’ve never noticed any."
    mc "Makeup tricks?"
    charlie "You know...Slightly fuller eyebrows. Brightened eye colour. Skin with a natural glow. The works."
    mc "You can do all that through magic!?"
    $ charlieface = 'neutral'
    show charlie flip at m2 with dissolve
    charlie "...How do you not know this? Where have you been?"
    mc "Uh…"
    $ charliepose = '1'
    show charlie flip at m1 with dissolve
    charlie "You know, sometimes I can’t tell if it’s just weird where you’re from, or if you’re just...not a very typical girl."
    think "She’s onto me!! ...And I think she might have just called me ugly!!"
    think "One of those should take precedent over the other, but it still stings."
    blank "My heart kicks into overdrive for no reason."
    blank "I feel as if some undercover educational bouncer is going to burst from the throng of students with a righteous cry of, “IMPOSTER!!”"
    blank "Then he’ll probably wheel kick me in the face and out of the school."
    blank "Charlie is looking at me intently, as if she’s skinning me with her eyes and seeing what’s underneath."
    think "What do I say to get out of this one?"
    menu:
        "I don’t care about how I look.":
            show charlie flip at m2 with dissolve
            charlie "Says the blonde bombshell with a rack she could use as a cup holder."
            blank "She smirks."
            charlie "Preach to me a little more about your beauty problems, princess."
            mc "You were the one who said it was weird!"
            think "...And did she just call me hot? I mean, I know I’ve got the body down."
            think "My previous preferences certainly didn’t get reset."
            $ charliepose = '2'
            show charlie flip at m1 with dissolve
            charlie "It IS weird."
            charlie "Everyone’s so into that kind of thing. I figured it was cause you knew you didn’t need it."
            mc "Oh."
            mc "Uhm."
            blank "Not exactly used to talking about my appearance, and rarely ever in a positive way, my throat locks up against the attempt."
            mc "Do you do that kind of thing? The makeup stuff?"
            blank "She scoffs."
            $ charlieface = 'happy'
            show charlie flip at m2 with dissolve
            charlie "What do you think?"
            mc "...I think that’s a question that doesn’t have a right answer."
            $ charlieface = 'neutral'
            show charlie flip at m1 with dissolve
            charlie "Surprisingly diplomatic. Maybe you’re learning a thing or two here after all."
            mc "I don’t think avoiding trick questions is one of the areas of study, but I’ll be sure to tack it onto my future resume."
            $ charliepose = '1'
            show charlie flip at m2 with dissolve
            charlie "I don’t play the glamor game, no. I’m just not the type."
            blank "Looking at those big, brown eyes, I can see why."
            blank "Anything that looked faked about her just...wouldn’t be right."
            show charlie flip at m1 with dissolve
            charlie "But that doesn’t mean I don’t know how to do those kind of spells, and I aaaam a curious kitten."
            mc "Uh. Curious about what?"
            blank "She smirks at me devilishly and pushes her last helping of vegetables toward me."
            charlie "Eat up quick and maybe you'll find out."
            scene bg black with dissolve
            scene dormroom_day with dissolve
            mc "I changed my mind! I don’t want to do this!"
            $ charlieface = 'neutral'
            $ charliepose = '1'
            show charlie flip at m1 with dissolve
            charlie "Oh, don’t be such a baby."
            charlie "You’ll like it. I promise I’ll do a good job."
            blank "She crosses over her heart, looking at me with such a firm seriousness that I’m inclined to believe it."
            think "How did I get roped into this…?"
            blank "I grimace as I let Charlie cast spells over my face, praying she doesn’t accidentally transform my nose or remove my eyelids."
            blank "And the slightest chuckle sends ice water through my veins."
            mc "You’re going to make me look like a clown, aren’t you?"
            charlie "With that expression, you already do."
            charlie "Stop frowning so hard. You’ll pull something."
            blank "She tugs at the edge of my cheek, trying to convince my face to smile. "
            $ charliepose = '2'
            show charlie flip at m2 with dissolve
            charlie "It’s like you’re attempting your best Mage Warren impression. He’s a cutie and all, but it wouldn’t kill him to look happy."
            blank "A cold chill sweeps over my cheeks."
            mc "What was that? ...Am I going to sparkle after this?"
            charlie "I can make that happen if you want."
            mc "I don’t want it!"
            mc "Nothing about this feels right. I think I’d rather be strapped to an interrogation table."
            $ charlieface = 'sad'
            show charlie flip at m1 with dissolve
            charlie "Weren’t you the one complaining earlier about not looking like everyone else?"
            mc "And didn’t you say you didn’t like this kind of thing, either!?"
            charlie "Shhhh. Stop making sense and let me have my fun. It’s a Friday night and I have to be stuck in here."
            charlie "At least let me get to enjoy it."
            blank "I sit as still as I can, blinking rapidly as I feel a strange, heavy clutter on my eyelids."
            mc "I can see my eyelashes. I can see them sticking out of my face. Is that supposed to happen?"
            $ charlieface = 'flirty'
            show charlie flip at m2 with dissolve
            charlie "Don’t ask questions."
            blank "I blink compulsively. "
            think "This is worse than having hair in your eyes!"
            mc "How do you even know how to do all this, if you don’t do it?"
            charlie "I had some friends who were into this kind of thing, I guess. I picked it up from them."
            think "Charlie had friends?"
            blank "It’s weird, thinking about her talking to someone else. Here, she only really interacts with me."
            blank "She doesn’t strike me as the shy type, either, but when you’re not even an official student of the school and have no classes with anyone else…"
            blank "I guess it’s a friendship of necessity."
            mc "Where are they now?"
            blank "She shrugs."
            charlie "Where I left them, I guess."
            charlie "Now stop talking, I’m trying to plump your lips!! Unless you want a swollen tongue instead."
            blank "I fall silent, at the mercy of Charlie’s hand and having no idea what she’s doing to me."
            blank "But I have a feeling the threat wasn’t just because of the magic."
            blank "After about fifteen minutes of gruelling torture, Charlie seems to find some benevolence and lets me go."
            charlie "There. Check it out."
            blank "I brace myself for the catastrophe that is my face."
            mc "Woah........."
            blank "I touch my skin, my appearance just unfamiliar enough to remind me of someone else."
            blank "It’s a little unnerving, like Sophie has suddenly taken on a complete life of her own and is using my body like a host."
            think "But at least she can live an attractive life, I guess?"
            think "I’m not sure if I should like this as much as I do."
            $ charlieface = 'happy'
            show charlie flip at m2 with dissolve
            charlie "See?"
            charlie "There you go, you look like everyone else now. Glam'd out and ready to kill someone in 6-inch heels. "
            mc "I guess so..."
            charlie "Do you like it? Do you want me to show you the ropes?"
            blank "I shake my head adamantly."
            mc "No. Like I said, I don’t have any real interest in it. You were the one who wanted to try it."
            think "And I can’t imagine doing this on the daily. We’ve probably been at it 30 minutes and that was with someone who supposedly knew what she was doing."
            $ charlieface = 'neutral'
            show charlie flip at m1 with dissolve
            charlie "Hm. Interesting. Really thought you'd change your mind once you saw yourself in the mirror."
            mc "What, you think I’m vain?"
            charlie "No. Seraphim's breath, you always think the worst of me don't you? "
            $ charlieface = 'blush'
            show charlie flip at m2 with dissolve
            charlie "I thought you were struggling with your appearance or your identity or something."
            charlie "That’s what you made it sound like and I thought it would help. But let’s not pretend this wasn’t also for my own amusement."
            blank "Her fingers trail through my hair, mussing it up a bit as it falls over my shoulders."
            $ charlieface = 'neutral'
            show charlie flip at m1 with dissolve
            charlie "Ugh. I could totally pimp you out."
            mc "Yeah, I’m gonna hazard a guess here and say that’s against the rules."
        "I just never had a teacher.":

            $ charlie_love += 1
            charlie "Oh, right. You learned your magic from a guy, didn’t you?"
            mc "Yeah…uh, exactly."
            $ charlieface = 'blush'
            show charlie flip at m1 with dissolve
            charlie "Hmm. Well, I could show you, if you want."
            mc "Really? You do that sort of thing, too?"
            charlie "Not usually. Do my eyelashes look like I could sweep the floor with them? Or use my skin to strategically blind somebody?"
            charlie "You just pick up a few things, here and there. How you never managed it is beyond me."
            blank "She sighs again, as if I’m just the antithesis of all conventional wisdom."
            $ charliepose = '2'
            show charlie flip at m2 with dissolve
            charlie "Come on."
            blank "She pulls me away from the last of my tapioca pudding with an indignant whine."
            scene bg black with dissolve
            scene dormroom_day with dissolve
            $ charliepose = '1'
            mc "How long is this effect going to last…?"
            $ charlieface = 'neutral'
            show charlie flip at m2 with dissolve
            charlie "I can get rid of it when we’re done."
            think "But will she is the question. I have no idea what she’s doing to me."
            mc "Is this going to hurt…?"
            $ charlieface = 'annoyed'
            show charlie flip at m1 with dissolve
            charlie "Oh my God. Look, I’ll do it to my face first, alright?"
            $ charlieface = 'neutral'
            show charlie flip at m1 with dissolve
            charlie "That way you can see what I’m doing."
            blank "It’s fascinating, the way she alters her appearance bit by bit. Small things really do make a dramatic difference."
            think "I feel like an idiot for not realizing any of this, but how was I supposed to know?"
            think "I thought girls just naturally had really thick eyelashes!"
            blank "She pokes and prods at my face, sending an array of weird feelings through it: a tingling in the tip of my nose, a heat warming up my cheeks."
            charlie "Stop squirming."
            mc "It feels weird..."
            $ charlieface = 'flirty'
            show charlie flip at m1 with dissolve
            charlie "Well it looks sexy, so shut up."
            blank "I blush hotly under the compliment, trying not to focus on how close she is to me. "
            blank "I can count a few light freckles dotted across the bridge of her nose, ones I had never seen until now. "
            blank "And every now and then I catch her eye, and another wave of heat squirms bashfully under my skin."
            think "Of course. A girl calls me sexy and I’m not in the right body."
            think "Typical. Completely typical."
            $ charlieface = 'neutral'
            show charlie flip at m2 with dissolve
            charlie "Ta-daaa. But don’t get your hopes too high, that’s just the best I’ve got."
            mc "I’m scared to look."
            charlie "It’s a masterpiece."
            mc "...Did you make yourself look gorgeous and then draw a dick on my face?"
            charlie "…Now that you mention it, that’s a great idea. Come here."
            mc "No!!!"
            $ charlieface = 'annoyed'
            show charlie flip at m1 with dissolve
            charlie "Then just look in the mirror!"
            mc "Oh."
            mc "…Oh…"
            $ charlieface = 'neutral'
            show charlie flip at m1 with dissolve
            charlie "Well?"
            think "I probably shouldn’t like this. But…"
            think "I can’t stop looking at myself. And then there's /Charlie./"
            think "She looks...so different, the way she looks at me like she came straight out of a magazine."
            think "How do you just summon that gorgeous, sultry look on command?"
            charlie "You’re really leaving me in suspense, here."
            mc "Oh!"
            mc "S-Sorry, I…think it’s nice."
            blank "Her plain face has a certain endearing quality to it, cute and natural, though I’m not going to object to this, either."
            blank "I glance back into my mirror, looking at how much softer my jaw looks. "
            blank "How my eyes seem bigger. "
            $ charlieface = 'happy'
            show charlie flip at m2 with dissolve
            charlie "Already testing your angles? You really are a beauty queen."
            mc "I’m not!"
            $ charlieface = 'neutral'
            show charlie flip at m2 with dissolve
            charlie "Why are you so indignant about this? It’s just a bit of fun. You know how to have that, right?"
            blank "She pinches my cheek."
            charlie "This kind of magic makes me itch, though."
            blank "And layer by layer, I watch as her face returns to normal."

    blank "A sharp knock at the door interrupts us, and my mind immediately goes into panic mode."
    mc "Take it off!"
    $ charlieface = 'happy'
    $ charliepose = '2'
    show charlie flip at m1 with dissolve
    charlie "Is now really the time to be getting undressed? "
    mc "Charlie!"
    blank "The knock repeats."
    mc "O-One second!"
    blank "I grab her by the sleeve, as if me getting caught with makeup on my face is somehow scandalous."
    $ charlieface = 'annoyed'
    show charlie flip at m2 with dissolve
    charlie "Will you calm down!?"
    blank "She pulls away."
    $ charlieface = 'angry'
    show charlie flip at m1 with dissolve
    charlie "What’s the matter with you? We’re wearing makeup, not making out."
    mc "I don’t want anyone to see!"
    shira "Is everything alright?"
    mc "Everything’s fine!"
    $ charlieface = 'sad'
    $ charliepose = '1'
    show charlie flip at m1 with dissolve
    blank "I practically hiss through my teeth."
    mc "Get this off my face."
    blank "We both freeze suddenly, when we hear a second voice outside the door."
    mc "Who’s that?"
    blank "Exchanging a glance, the both of us creep slowly toward the door and press our ears to the wall."
    blank "I can’t hear the words, but the voice sounds familiar."
    mc "It sounds like Master Mage Aureman, doesn’t it?"
    blank "We both stare at the door intently, trying to overhear, but they speak too softly."
    mc "Now’s our chance!!"
    blank "She sighs as she starts to peel off the magic. It feels weird, like a thin layer of tape being slowly pulled off my skin."
    scene bg black with dissolve
    scene dormroom_day with dissolve
    show charlie flip at m1 with dissolve
    blank "I think 50 percent of my vision comes back, which is nice, no longer looking out through a canopy of shadowy, thick eyelashes."
    shira "Never mind, Sophie. I’ll return later."
    blank "We listen until the sound of Magi Shira’s footsteps trail away down the corridor, and I take a gasping sigh of relief."
    blank "Then get smacked upside the head."
    charlie "Seriously, what is your damage?"
    $ charlieface = 'sad'
    show charlie flip at m2 with dissolve
    charlie "You acted like we were trying to bury a body in here!"
    mc "Hey, I would have been way more composed if we were burying a body!"
    $ charliepose = '2'
    show charlie flip at m1 with dissolve
    charlie "So murder is cool, but wearing makeup is a no-no? "
    mc "I just…"
    mc "I want people here to take me seriously!"
    mc "No one will if I wear stuff like this. Magi Shira doesn’t."
    $ charlieface = 'neutral'
    show charlie flip at m2 with dissolve
    charlie "Sure she does! It’s just really subtle. Do you really think that flawless, wrinkle-free complexion is natural?"
    mc "It could be!"
    blank "She sighs, her hands going to her hips."
    think "Now I’ve done it."
    charlie "If you really think wearing makeup is going to affect your chances here somehow, maybe that says something more about your talent than it does about makeup."
    charlie "Something to think about."
    hide charlie with dissolve
    blank "She closes the door behind her as she leaves, leaving me gaping after her."
    blank "Usually I’d consider our banter...aggressively playful, I guess."
    blank "She’s only tried to set me on fire a couple of times. In terms of my previous relationships with girls, that’s a step in the right direction."
    blank "But the jab about my talent...."
    blank "She probably didn't mean it, but it digs into my skin like a barb I can’t get pry out, dripping a slow poison into my veins."
    blank "I’m not good enough now, I’m not delusional enough to think that."
    blank "But I can be. I’m sure that I can be."
    blank "The more I think on it, the more indignation rises in me."
    think "I'll show her!! Once I figure out how..."
    blank "I pace my room. "
    blank "Shira gave us some reading to do tonight, but I shove the thought away."
    blank "That’s not the kind of restless ambition I’m filled with."
    blank "It’s...more like the kind that got me into this mess to begin with, really."
    blank "…"
    think "So why don’t I use it to get out of it, too?"
    think "Shira said a counter-spell was something only sorcerers were likely to accomplish. If I could reverse it, then surely that would prove how powerful I can be!"
    think "Congratulating myself as a genius, I peek out of my room and slide toward the hallway."
    blank "I hope that whatever’s keeping Magi Shira lasts a long time."
    scene bg black with dissolve
    scene hallway with dissolve
    blank "I bypass our apprentice library completely. There won’t be anything of use in there."
    think "Those books are just coddling us."
    think "There has to be better resources somewhere else in the castle, probably on the higher floors."
    scene bg black with dissolve
    scene entrance_interior_day with dissolve
    play music "music/track03.ogg" fadeout 1 fadein 1
    think "The floors we’re not technically supposed to go to…"
    blank "My feet hesitate in front of the staircase, staring up into the dark."
    blank "For the first time in this plan, I feel doubt tug me back."
    think "Is this really worth it?"
    think "And what is Charlie going to think once I come clean about the whole mess?"
    blank "Not that her opinion should matter."
    blank "This is about what I want to do after school, not who I want to appease while I’m here."
    blank "But I still don’t move, don’t take that first step."
    think "Didn’t I say I’d do anything to succeed?"
    think "So what’s holding me back?"
    blank "A shadow moves down the corridor, stepping in front of a distant light."
    blank "I bolt toward the other side of the room, slinking behind a half-open door to an empty lecture hall."
    blank "I was so caught up in thoughts of getting caught, I forgot I wasn’t actually anywhere I wasn’t allowed to be…"
    blank "The voices drift by and I peek out from my hiding place."
    $ mc_clothes = 8
    $ auremanface = 'annoyed'
    $ warrenface = 'serious'
    show warren at l2 with dissolve
    show aureman at r1 with dissolve
    aureman "...I’m already aware of the situation, Warren."
    $ warrenpose = '2'
    show warren at l1 with dissolve
    $ warrenface = 'mad'
    warren "How? And don’t say your keen sense of intuition."
    $ auremanface = 'neutral'
    show aureman at r2 with dissolve
    aureman "By virtue of being in the right place at the right time. Not everything needs a supernatural explanation."
    $ warrenpose = '1'
    $ warrenface = 'neutral'
    show warren at l2 with dissolve
    warren "Then what are you planning to do about it?"
    $ auremanface = 'mad'
    show aureman at r1 with dissolve
    aureman "For the moment? Nothing."
    $ warrenpose = '3'
    $ warrenface = 'serious'
    show warren at l1 with dissolve
    warren "Nothing?"
    warren "A clear breach of magical law has taken place here and you’re just going to stand by idly-"
    $ auremanface = 'annoyed'
    show aureman at r2 with dissolve
    aureman "And what would you have me do, Warren? Round up a guard and march them through the halls?"
    blank "The old man gives a dry, croaky laugh."
    aureman "You’re too rigid. But I suppose I couldn’t expect that to change now, could I?"
    $ warrenpose = '1'
    show warren at l2 with dissolve
    warren "She has no place here and should be thrown out of the school."
    warren "Just like anyone who committed such a crime."
    $ warrenpose = '3'
    show warren at l1 with dissolve
    warren "That isn’t me being rigid, that’s me being pragmatic."
    think "...Throw who out of the school?"
    think "...T-They can’t be talking about me, can they?"
    think "Master Warren...how would he have known?"
    think "Oh, Gods."
    think "Aureman. He saw me in the library."
    think "The right place at the right time. He must have realized what I was doing and then…"
    blank "The Master Mage sighs wearily."
    show aureman at r1 with dissolve
    aureman "Perhaps you’re right."
    aureman "But for now, take no action. I will decide how to deal with this."
    think "They’re going to kick me out."
    think "I’m doomed."
    think "Hell, if Warren gets his way then I might even be arrested!"
    think "What am I supposed to do!?"
    menu:
        "Talk to Charlie about it.":
            play music "music/track01.ogg" fadeout 1 fadein 1
            blank "I wait until they’re out of sight and earshot, then book it toward my room."
            scene bg black with dissolve
            scene dormroom_night with dissolve
            mc "Charlie!!"
            $ charlieoutfit = 'pyjamas'
            $ charlieface = 'annoyed'
            show charlie flip at m1 with dissolve
            charlie "What the hell are you doing!? I thought you were Shira!!"
            blank "She goes to cover herself. "
            mc "Look, it’s not like I haven’t seen it before-- not to say it’s not impressive, I just-- UGH, that’s not the point! I have to talk to you!"
            $ charliepose = '2'
            show charlie flip at m2 with dissolve
            mc "It’s important. It’s really important, please."
            charlie "Okay, okay."
            $ charlieface = 'blush'
            show charlie flip at m1 with dissolve
            charlie "Get in here before you yell this super important information to the whole school."
            blank "She steps back, looking bewildered at how I keep going on."
            blank "Really, I can’t say that I blame her."
            think "I didn’t think this through. How am I supposed to even approach this subject?"
            think "I can’t tell her the truth."
            mc "Listen, I…"
            mc "I may have done something...bad..."
            $ charlieface = 'neutral'
            show charlie flip at m2 with dissolve
            charlie "Oh, boy. What’s on fire this time?"
            charlie "Or did you punch someone in the face, just to shake things up a little?"
            mc "Neither of those!!"
            mc "I-It involves getting into the academy."
            mc "I might’ve...done something slightly illegal."
            blank "Her face pales."
            $ charlieface = 'mad'
            show charlie flip at m1 with dissolve
            charlie "What?"
            mc "Look, does it matter what it is?"
            $ charliepose = '1'
            show charlie flip at m2 with dissolve
            charlie "Considering I don't know if you jay walked in front of the school or if you murdered somebody, yeah, I'd say it matters!"
            mc "I didn't murder anyone!"
            mc "The point is, I think the Master Mage and Mage Warren know, and I’m pretty sure Warren wants me expelled."
            mc "Please help me."
            $ charliepose = '2'
            show charlie flip at m1 with dissolve
            charlie "Help you?!"
            show charlie flip at m2 with dissolve
            charlie "Help you!?!"
            charlie "What do you possibly think I can do for you, Sophie!?"
            $ charlieface = 'angry'
            show charlie flip at m1 with dissolve
            charlie "Do you want to me spin a little time-travel magic and go back to tell you not to be an idiot!?"
            mc "...Is there such a thing?"
            show charlie flip at m2 with dissolve
            charlie "No, there isn’t!!"
            charlie "Just back up and tell me what you did."
            mc "I…"
            think "Well, I don’t have to tell her the spell went wrong. I can just tell her all the other ways I ruined my life."
            mc "I broke into one of the Sorcerer Archives."
            $ charlieface = 'annoyed'
            $ charliepose = '1'
            show charlie flip at m1 with dissolve
            charlie "...I’m sorry, did you just say you committed a class 3 magical offense?"
            mc "...There are classes?"
            blank "She punches me in the arm."
            charlie "Sophie, you idiot!"
            charlie "What…"
            $ charlieface = 'mad'
            show charlie flip at m2 with dissolve
            charlie "Why are you even here? Get out of the city!"
            mc "I’m not leaving! The only reason I did it was so I could come here!!"
            charlie "By busting into an archive and proving how much of a criminal you are?"
            charlie "Brilliant plan!"
            mc "I just wanted more power!"
            $ charliepose = '2'
            show charlie flip at m1 with dissolve
            charlie "Oh, yeah, said every totally well-meaning person ever."
            charlie "Listen...you need to leave."
            mc "I’m not leaving the school!"
            charlie "Not the school! I don’t care about the school, I don’t care where you go!"
            charlie "But you need to leave this room. I don’t…"
            $ charlieface = 'angry'
            show charlie flip at m2 with dissolve
            charlie "I’m not getting caught up in this. I won’t."
            blank "The words cut deeper than I expected them, my mouth falling open."
            blank "When I first pieced together what they were talking about, Charlie was the first one to come to my mind."
            blank "I don’t know why, but I thought…"
            blank "I thought she would help me."
            blank "Or that she would at least care!! I would have done the same for her."
            mc "...Aren’t we friends?"
            mc "We fight, but…"
            blank "Her expression flickers. "
            $ charlieface = 'sad'
            show charlie flip at m1 with dissolve
            charlie "We’re...we're not friends. We’re classmates."
            charlie "And you need to leave."
            blank "She’s backed up toward the corner, as if I’m a wild animal."
            mc "Charlie why are you acting this way!? I don’t understand!"
            mc "I really need your help!"
            blank "Unbidden, I feel my face heating up in desperation, and the sudden swell of emotion makes me want to get angry."
            mc "I didn’t do anything wrong!"
            blank "I wither a little beneath her glance."
            mc "Okay, okay, I didn’t do anything violent. But...why the hell are you treating me like this?"
            $ charliepose = '1'
            $ charlieface = 'annoyed'
            show charlie flip at m2 with dissolve
            charlie "Y-Your problems are not my problems!"
            mc "...I sure as hell hope not."
            mc "Because whatever your problems are, they make you a terrible person."
            blank "Emotion flickers across her face, a brief shattering of hurt before she draws herself up again."
            $ charliepose = '2'
            show charlie flip at m1 with dissolve
            charlie "You don’t know anything about it!"
            mc "Then explain it! I’ll leave your room if you just explain it!!"
            blank "She half turns around, then turns back, as if ready to get in my face. "
            blank "But she pulls herself back with whatever restraint she has left. "
            show charlie flip at m2 with dissolve
            charlie "You’re so..."
            blank "She sighs, with an expression so reluctant I might as well be making her cut off her own hand. "
            charlie "Whatever. Fine."
            charlie "Tomorrow."
            mc "Tomorrow?"
            $ charlieface = 'sad'
            $ charliepose = '1'
            show charlie flip at m1 with dissolve
            charlie "We’re going out. It’s a weekend anyway."
            charlie "Come here early."
            mc "But why can’t you just…"
            blank "She gives me such a reproachful look that I back up, my fist clenching and unclenching nervously."
            mc "Fine...."
            mc "Tomorrow."
            blank "Still wounded, I leave her room and close the door behind me."
            scene bg black with dissolve
            scene hallway with dissolve
            blank "I didn’t think about how loud we were being, but the hallway is deserted and quiet."
            think "I can’t believe she just turned me away."
            think "I wanted her help. I actually trusted her."
            think "So it wasn’t the most harmonious relationship, sure, but I thought we had an understanding…"
            think "And I still don’t know what to do about Mage Warren."
            blank "My stomach agrees with Charlie’s plan, I think. It wants to get the hell out of here."
            scene bg black with dissolve
            scene dormroom_night with dissolve
            blank "I spend about an hour of the night dry heaving over the toilet and bouncing between a number of possible mental illnesses."
            blank "Magi Shira doesn’t even come by like she normally does…"
            blank "I wonder what Charlie means by tomorrow. If I'll even be in the school long enough for tomorrow to matter. "
            blank "It takes me hours to fall asleep."
            scene bg black with dissolve
            scene dormroom_day with dissolve
            $ charlieoutfit = 'casual'
            $ mc_clothes = 2
            show charlie flip at m1 with dissolve
            charlie "Wake up."
            mc "Hrnnngh…"
            $ charliepose = '2'
            show charlie flip at m2 with dissolve
            charlie "We have to go early."
            think "Expulsion."
            blank "It’s the first word that pops into my head, jolting my head off the pillow."
            mc "What happened!?"
            $ charlieface = 'annoyed'
            show charlie flip at m1 with dissolve
            charlie "Nothing. What are you talking about? Are we going or not?"
            blank "It takes me a minute to remember everything that happened last night, piecing it together."
            mc "Oh. Right…"
            blank "Awkwardly, I shuffle out of bed under Charlie’s scrutiny."
            blank "She stands there stiff, discomfort etched into every limb."
            blank "It’s like she’s being held up by strings. Snap them, and all that tension falls apart into a mess."
            think "How is she the one stressing out about this?"
            think "I’m the one whose neck is on the chopping block!"
            blank "I get ready as quickly as I can, Charlie never leaving my room despite her demand that I leave her alone yesterday."
            scene bg black with dissolve
            scene entrance_interior_day with dissolve
            $ mc_clothes = 5
            $ mc_gender = 2
            $ charlieface = 'sad'
            show charlie flip at m1 with dissolve
            mc "Where are we going?"
            $ charliepose = '1'
            show charlie flip at m2 with dissolve
            charlie "Just follow me and don’t ask questions. Keep your eyes down."
            blank "For the first time in a week, we leave the school."
            scene bg black with dissolve
            scene city_day with dissolve
            blank "I don’t know anything about this place."
            blank "I barely had enough sense to get around the first few days I was here, wandering aimlessly with only the silhouette of the school as my reference point."
            blank "But Charlie moves with familiarity, skipping larger streets and choosing smaller alleys that avoid the crowds."
            blank "People cling to the shadows, sitting around on the street or piling up dirty clothes on the top of trash cans."
            blank "It doesn’t seem to bother her though."
            show charlie flip at m1 with dissolve
            charlie "Alright, listen. There are some basic rules you have to follow. "
            charlie "First, mind your own business. Don't get involved. "
            show charlie flip at m2 with dissolve
            charlie "Second, don't make any business. "
            show charlie flip at m1 with dissolve
            charlie "And third, if you see a guy in a red scarf with crossed eyes, always look in the LEFT eye. "
            mc "Wh-what?!"
            show charlie flip at m2 with dissolve
            charlie "ALWAYS THE LEFT. Got it? "
            mc "M-my left or his!?"
            blank "She heaves a sigh. "
            charlie "You're not gonna make it a day out here..."
            mc "Where even is 'here!?' What is this place?"
            show charlie flip at m1 with dissolve
            charlie "This is where I grew up."
            mc "...What?"
            blank "I glance around at the houses, but she shakes her head."
            charlie "Not there. Here."
            blank "She gestures around us, all around us, until the meaning finally sinks in."
            mc "You were homeless?"
            blank "She hesitates and shrugs."
            show charlie flip at m2 with dissolve
            charlie "N-not...really homeless, I guess."
            charlie "I just had a lot of homes. Different ones with different people in them."
            charlie "I’d stay with one over the summer, spend a week with someone else…"
            charlie "Spend time on the street, if somebody moved or lost their job…then get picked up somewhere else..."
            blank "She strolls down the street, glancing from house to house."
            show charlie flip at m1 with dissolve
            charlie "It sucked sometimes, but I had people."
            charlie "Until I didn’t."
            mc "What happened?"
            $ charliepose = '2'
            show charlie flip at m2 with dissolve
            charlie "They got old. They died. They moved. They vanished."
            charlie "The things that just happen to people when you live in a place like this."
            charlie "That sort of thing always happened, and someone always stepped in for me, but eventually I wasn’t a kid anymore."
            show charlie flip at m1 with dissolve
            charlie "I was someone who was expected to watch out for herself."
            charlie "I mean, I think I had a really great childhood, you know?"
            charlie "A bunch of moms. A bunch of dads."
            show charlie flip at m2 with dissolve
            charlie "More siblings than I probably even remember."
            charlie "It’s not really a sob story. But I’m not a kid anymore and there is nobody out here who’s going to look out for me now."
            charlie "So I’m just trying to make sure it doesn’t turn into one."
            mc "So you joined the Academy."
            $ charliepose = '1'
            show charlie flip at m1 with dissolve
            charlie "Where else was I going to go?"
            charlie "It was either that or be one of the women in the makeup."
            mc "Who?"
            charlie "It’s what I used to call the prostitutes when I was younger. I thought they looked nice."
            charlie "Fancy, you know?"
            show charlie flip at m2 with dissolve
            charlie "But you don’t wear make up around here unless you want to vanish or get taken advantage of."
            charlie "And eventually I knew better than to want to be one of them."
            mc "Why are you telling me all this?"
            show charlie flip at m1 with dissolve
            charlie "Because I want you to understand why I can’t get involved in whatever it is you’ve done."
            charlie "Because believe it or not, I actually do give some slight shit about what you think of me."
            charlie "And I need you to know I have a reason."
            show charlie flip at m2 with dissolve
            charlie "I can’t come back here. I don’t have anywhere to come back to."
            charlie "It’s this or nothing. It’s the only reason Shira took me in, I’m sure of it, and if I mess this up…"
            blank "Her voice has started shaking, thought trailing off into some emotion."
            charlie "You can hate me if you want. I wouldn’t blame you."
            charlie "But this is why."
            show charlie flip at m1 with dissolve
            charlie "Out here you learn not to make other people’s problems your problems, because you’ve got enough of your own."
            think "I get it."
            mc "I never meant to put you in this position."
            think "And if they find out that Magi Shira is lying to protect me…"
            think "To think, I should have been happy when I thought I was just messing up my life."
            blank "Charlie sighs."
            $ charlieface = 'blush'
            show charlie flip at m2 with dissolve
            charlie "I’m sorry, Sophie."
            mc "No, it’s nothing you have to apologize for. I’m the one who messed up."
            blank "I don’t know what to do from here."
            blank "We stand in the street together, listening to the drone of conversation. Dogs barking in the distance."
            blank "When I first got here, I was so overwhelmed by the city. All the sights and sounds."
            blank "Now it feels like it’s a million miles away, and the only place that exists is this tiny street."
            think "I really have been selfish."
            think "I thought it was a good thing. Ambitious. But all it’s done is ruin everything…"
            think "I have to make things right somehow."
            menu:
                "I won’t involve you.":
                    charlie "What?"
                    mc "Look, I didn’t tell you exactly what I did, and I really can’t, but-"
                    $ charlieface = 'mad'
                    show charlie flip at m1 with dissolve
                    charlie "Oh, thanks for the reciprocity. I’m over here spilling my guts and your mouth is sealed tighter than the archives."
                    charlie "Oh, never mind, apparently those aren’t very secure at all."
                    think "At least this attitude is familiar…"
                    mc "Look, you said you didn’t want to be involved, right?"
                    mc "Me not telling you, that’s keeping you uninvolved. But I feel like if I get better at magic, if I just prove myself…"
                    $ charlieface = 'angry'
                    show charlie flip at m2 with dissolve
                    charlie "Then what?"
                    charlie "Then you won’t get arrested? Just so you can graduate, achieve your dream, and then die in some stupid trial?"
                    $ charliepose = '2'
                    show charlie flip at m1 with dissolve
                    charlie "That’s what you still want, isn’t it?"
                    mc "Of course it is."
                    charlie "Ughh!!"
                    charlie "Don’t you understand how stupid that is, Sophie!?"
                    charlie "You’re throwing your life away. You have this one chance to make something out of yourself."
                    charlie "And if you actually do it, then you’re just going to die?"
                    charlie "All because you can’t be satisfied?"
                    mc "It’s not just about being satisfied, it’s...it’s more than that to me, okay?"
                    mc "I just have to do it!"
                    blank "Our voices lower as another couple strolls by, eyeing us, and briefly reminding me of where we are."
                    blank "Charlie sighs and crosses her arms moodily, not caring if our argument becomes a public spectacle."
                    $ charlieface = 'sad'
                    show charlie flip at m2 with dissolve
                    charlie "This is why I didn’t want to get involved with you in the first place, you know."
                    charlie "It’s easier to lose people when you don’t care about them."
                    $ charliepose = '1'
                    show charlie flip at m1 with dissolve
                    charlie "That’s another thing I learned out here."
                    charlie "I was just...never very good at following my own advice."
                    blank "Her eyes shift with uncertainty."
                    think "Does that mean she has started to care…?"
                    blank "But she shakes her head and I take that as a no. Rejection."
                    think "It’s not entirely undeserved, after everything I’ve done."
                    think "That’s it then."
                    think "I guess I’m on my own."
                    mc "I’m sorry I tried to get you involved, Charlie."
                    show charlie flip at m2 with dissolve
                    charlie "Yeah, well...it’s my fault, too."
                    charlie "I don’t have a hate switch in my head that I can flick and despise you immediately."
                    $ charlieface = 'blush'
                    show charlie flip at m1 with dissolve
                    charlie "I tried."
                    blank "She sighs heavily."
                    charlie "We’re still classmates. We’re still going to have to be around each other, and…"
                    charlie "I guess we can get along as much as we have to."
                    mc "Right."
                    blank "An awkward silence descends."
                    $ charlieface = 'neutral'
                    show charlie flip at m2 with dissolve
                    charlie "Umm. I’m gonna walk around for a little while, but I can walk you back to the school if you want."
                    mc "No, I better do some shopping while I’m out."
                    mc "I don’t think I packed enough clothes."
                    $ charliepose = '1'
                    show charlie flip at m1 with dissolve
                    charlie "Then I’ll take you to a good shopping district. You shouldn’t wander out here by yourself."
                    charlie "Come on…"
                    blank "In an awkward silence, Charlie leads me to a different part of the city."
                    blank "The shops are gathered together on narrow streets, one building blending into the next."
                    blank "I’ve never seen buildings crammed so close together before, even stacked on top each other."
                    blank "I’m still marvelling at the sight when Charlie slips away to be on her own."
                    blank "A sense of failure nestles in my stomach, a nauseating cocktail of guilt, remorse, and shame. Embarrassment for garnish. Stir well."
                    think "I really messed this up by being so selfish, didn’t I?"
                    think "...But that just means I have to make it better. Whatever that takes. "
                    blank "I run back into Charlie in front of the school, as if she was there waiting for me. "
                "Maybe we can help each other.":

                    $ friends = True
                    $ charlie_love += 1
                    $ charlieface = 'annoyed'
                    show charlie flip at m1 with dissolve
                    charlie "Have you not been listening to a word I’ve been saying…?"
                    $ charlieface = 'angry'
                    show charlie flip at m2 with dissolve
                    charlie "I can’t help you!"
                    $ charlieface = 'mad'
                    show charlie flip at m1 with dissolve
                    charlie "I’m not getting myself expelled by...by whatever idiotic plan you’re going to come up with!"
                    mc "That’s not what I’m talking about."
                    mc "Trust me, I don’t want you to get in trouble, either."
                    mc "I do care about what happens to you, you know…"
                    blank "She blinks at me in surprise."
                    mc "And I want to help you get in the Academy, too."
                    mc "So let’s train together. And I mean really, really train. Night and day."
                    $ charlieface = 'sad'
                    show charlie flip at m2 with dissolve
                    charlie "Why…?"
                    $ charliepose = '2'
                    show charlie flip at m1 with dissolve
                    charlie "So that I can get close to you and then you go can go die in some stupid trial?"
                    blank "She frowns at the ground, her face crumpling into a sadness I never expected to see there."
                    blank "The wind teases her hair and she tries to hide behind it, to keep me from seeing it, but it’s too late for that."
                    charlie "Why do you think I tried so hard just to be your rival when you first got here?"
                    charlie "I’ve already lost enough people. Good people."
                    charlie "I don’t want to go through it again."
                    scene scene14a with dissolve
                    blank "I don’t even remember moving. I don’t remember pulling her against me."
                    blank "It was an impulse, a feeling, and like most of my instincts, I don’t get a say in whether I do it or not."
                    blank "It just happens."
                    blank "And for a long second, I expect to be blasted across the city street and left to die."
                    blank "But she hesitates, tense in my arms, and then slumps into the grip."
                    blank "I’m briefly stunned."
                    scene scene14b with dissolve
                    blank "I’ve barely known her for more than a week, but I don’t think this would be okay for my actual gender."
                    blank "The touch is nice, though."
                    blank "Simple and comforting."
                    charlie "Why are you making it more and more difficult to dislike you?"
                    charlie "If you’re going to go die, I’d rather be spared the heartache of having been your friend."
                    mc "You’re not doing a very good job of it."
                    charlie "I can’t help it."
                    blank "She sulks against my shoulder, sounding more like a petulant child now."
                    mc "Then I guess you better really help me train."
                    charlie "...You’re awful."
                    blank "She punches me weakly in the arm, but it’s with a tentative smile."
                    charlie "Ugh."
                    scene bg black with dissolve
                    scene city_day with dissolve
                    $ charliepose = '1'
                    $ charlieface = 'blush'
                    show charlie flip at m1 with dissolve
                    blank "She wipes at her face. There’s an attempt to be discreet and I let her pretend that it was."
                    charlie "I kind of got a little emotional there, didn’t I?"
                    mc "Just an embarrassing bit."
                    $ charlieface = 'flirty'
                    show charlie flip at m2 with dissolve
                    charlie "Yuck."
                    show charlie flip at m1 with dissolve
                    charlie "Now I’m going to hate myself for the next six months."
                    mc "Hey, there’s no reason for that."
                    mc "I mean, unless you did it for nothing and you’re not going to accept my help."
                    blank "She rolls her eyes at me."
                    show charlie flip at m2 with dissolve
                    charlie "Have you ever thought of being a door-to-door saleswoman? I think you’d be really good at it."
                    mc "And I think you’d be a good lawyer, the way you keep deflecting."
                    charlie "Alright, alright."
                    $ charlieface = 'neutral'
                    show charlie flip at m1 with dissolve
                    charlie "I’m in."
                    charlie "But do you really think this will work?"
                    mc "It has to."
                    mc "Because I know I’m not letting you flunk out of here."
                    mc "And I don't know what they're going to do to me, but...maybe I can prove my worth."
                    $ charliepose = '2'
                    $ charlieface = 'sad'
                    show charlie flip at m2 with dissolve
                    charlie "But...but I can’t return the favour, I can’t make sure you don’t get expelled…"
                    mc "Nah, that doesn’t matter."
                    mc "I’ll handle that problem myself."
                    $ charlieface = 'blush'
                    $ charliepose = '1'
                    show charlie flip at m1 with dissolve
                    charlie "Guess it turns out I’m still not very good at making it on my own, am I..?"
                    charlie "And really, you should completely hate me for everything I’ve done."
                    charlie "I guess I’d still like to train with you and hang around, so I’m glad you don’t, but..."
                    mc "You have your reasons."
                    mc "You can’t risk helping me and getting expelled, too. Or worse."
                    mc "That’s totally understandable."
                    $ charlieface = 'sad'
                    show charlie flip at m2 with dissolve
                    charlie "I still don’t feel too great about some of that stuff I said. "
                    mc "I have a thick skin."
                    charlie "Pft. A country girl with thick skin?"
                    $ charlieface = 'flirty'
                    show charlie flip at m1 with dissolve
                    charlie "I’ll believe it when I see it."
                    blank "She prods me in the arm gently."
                    $ charlieface = 'neutral'
                    show charlie flip at m2 with dissolve
                    charlie "But I wouldn’t mind being proven wrong about you."
                    charlie "I really, really want you to surprise me."
                    think "Not just surprise her. She wants me to survive."
                    blank "A part of me stays uncertain. I don’t want Charlie to have to pay for my mistakes."
                    blank "But after the night I had, pacing my room and breaking out into cold sweats, suffering through the whole thing alone…"
                    blank "I’d like someone by my side in any way possible."
                    mc "If you’re sure you want to risk it..."
                    show charlie flip at m1 with dissolve
                    charlie "I’m not. But hey."
                    charlie "People have helped me and taken care of me my whole life."
                    charlie "What kind of person am I, if I don’t pay that forward?"
                    blank "She gives me a grin and takes my hand, her own touch a little rough and worn."
                    $ charliepose = '1'
                    show charlie flip at m2 with dissolve
                    charlie "Let’s go look around. I want to show you some of the old rooftops I used to play around on."
                    scene bg black with dissolve
                    scene entrance_day with dissolve
                    blank "We spend the day in the city together."
                    blank "Charlie knows every nook and cranny. She takes us to the best place for ice cream and shows me her favourite street performers."
                    blank "I even manage to buy some more girlish clothes while I’m out."
                    blank "Luckily, Charlie tends to have an opinion about everything even without being asked, so I got some easy advice and direction."
                    blank "When we finally go back to school, I’ve practically forgotten about all the very-real worries that are waiting for me."

            scene bg black with dissolve
            scene entrance_interior_day with dissolve
            show charlie at l1 with dissolve
            blank "When we enter, Magi Shira is standing just across the foyer, her hands folded as if she had been waiting for us."
            mc "It’s like she has some kind of sense."
            charlie "Yeah, that’s called magic, genius."
            blank "I nudge her gently in retribution, worry nettling my stomach."
            $ shiraoutfit = 'smart'
            show shira at r2 with dissolve
            think "What if this is it? What if she’s here to break the bad news?"
            blank "I look around for the guards that will probably escort me out."
            think "Oh, what am I saying?"
            think "I’m not even important enough to be escorted out."
            show shira at r1 with dissolve
            shira "Sophie, Charlie."
            blank "She nods to us politely and then passes us a piece of paper."
            think "I want to close my eyes. If I don’t look at it, maybe it won’t exist."
            show charlie at l2 with dissolve
            charlie "What’s this?"
            blank "Charlie leans in to see, peering at it."
            charlie "...Our Initiate Trial? "
            mc "Oh. Wait, what?!"
            show shira at r2 with dissolve
            shira "Shortly after the middle of the year, you'll be scheduled for a second attempt at your Trial. "
            shira "These are the dates that have been decided on. "
            mc "But that's so soon!"
            show shira at r1 with dissolve
            shira "You already showed enough potential to be considered Apprentices."
            shira "Your talents should have grown enough to qualify you for full-fledged membership into the school. "
            shira "All that remains is for that to be tested again. "
            mc "Will it be just like it was before...?"
            show shira at r2 with dissolve
            shira "Roughly, but you will not fight me. That would be rather unfair. "
            charlie "Then who's our opponent? "
            show shira at r1 with dissolve
            shira "Mage Warren. "
            show charlie at l1 with dissolve
            mc "Mage Warren!?!"
            mc "That's unfair, too!!"
            show shira at r1 with dissolve
            shira "I assure you, no matter his strong opinions, he won't sabotage you just to get at me. "
            shira "I wanted to let you know and think on it so you will have some time to prepare."
            shira "Enjoy your weekend."
            hide shira with dissolve
            mc "...Does this mean I’m not expelled?"
            charlie "Has anyone ever told you that you have a one-track mind?"
            mc "I’m anxious, alright!?"
            show charlie at l2 with dissolve
            charlie "Sorry, sorry. Here."
            blank "She pushes the paper toward me."
            mc "What?"
            charlie "I already know you’re going to obsess over this."
            mc "And you’re not?"
            show charlie at l2 with dissolve
            charlie "Pft. I might not be going to get myself slaughtered in the Sorcerer Trials, but I’m definitely not letting you show me up in our entrance exams."
            if friends:
                charlie "Besides, this fits in pretty nicely with our plans, doesn’t it?"
                show charlie at l1 with dissolve
                charlie "We we're going to train anyway, now we have even more reason."
                jump impendingtrial
            else:
                jump impendingtrial
        "Talk to Magi Shira about it.":

            play music "music/track12.ogg" fadeout 1 fadein 1
            $ shira4 = True
            blank "I wait until they’re out sight and earshot, then push myself out of the lecture hall."
            think "Shira."
            think "I have to find Magi Shira, I have to tell her.."
            scene bg black with dissolve
            scene hallway with dissolve
            $ shiraoutfit = 'robes'
            blank "My search is a desperately blind one. I go to her office, first."
            blank "Empty."
            scene bg black with dissolve
            scene dininghall with dissolve
            blank "The dining hall."
            blank "Empty."
            scene bg black with dissolve
            scene classroom with dissolve
            blank "Even our classroom, though there’s no reason she would be in it at this hour."
            think "Where is she?"
            think "What if she got fired?"
            think "What if she’s already being detained and questioned about her involvement in my stunt?"
            think "Oh no."
            think "Oh no, oh crap-"
            think "I’m so screwed. I’m so screwed!!"
            shira "Sophie?"
            show shira at m1 with dissolve
            blank "The voice cuts through my panic attack."
            blank "I nearly throw myself toward her, coming just short of grabbing her by the arms."
            mc "Magi Shira!"
            mc "What are you doing in here?"
            show shira at m2 with dissolve
            shira "I came back to your room for the nightly ritual, as usual, but you weren’t there."
            shira "I admit, I was a bit concerned."
            mc "I wasn’t sneaking off again."
            think "Okay, I was, but I didn’t. That’s an important distinction for me, but not one Shira needs to know about."
            mc "I was looking for you!"
            mc "I think I’m in trouble."
            show shira at m1 with dissolve
            shira "What sort of trouble?"
            mc "Um. The legal kind, maybe?"
            mc "Expulsion, at the very least."
            shira "Expulsion?"
            blank "She glances around the hallway and then steps further into the shadows of the classroom."
            blank "Her face is cast in half-shadows, making it difficult to see, but her eyes gleam with concern."
            show shira at m2 with dissolve
            shira "What’s happened, Sophie? What did you do?"
            mc "It’s nothing you don’t already know about, but…"
            mc "I think Mage Warren and Master Mage Aureman are onto me."
            mc "I overheard them talking…"
            show shira at m1 with dissolve
            shira "That’s strange. I told no one else your secret, I promise."
            shira "I would not have trusted it to anyone else."
            shira "What did they say?"
            mc "The Master Mage said he didn’t want to act on it, but Mage Warren was trying to convince him to issue an arrest.."
            mc "He said something like the law had been broken, and someone had to answer for it."
            show shira at m2 with dissolve
            shira "And you’re certain this was said about you?"
            mc "Well…"
            mc "I did run into the Master Mage once before. I saw him in the library after I’d cast the spell."
            mc "He also said he wouldn’t tell the guard anything about seeing me there."
            mc "I guess he recognized me and put together what I had done and why I’d done it after the fact."
            mc "But I don’t know how Mage Warren found out."
            show shira at m1 with dissolve
            shira "This is concerning…"
            blank "I nearly jump as a warm hand rises to cup my cheek."
            mc "Um…"
            show shira at m2 with dissolve
            shira "Sophie. You did the right thing by coming to tell me, but I don’t know if I’ll be able to protect you at this point."
            shira "But I’ll do what I can."
            show shira at m1 with dissolve
            shira "For now, I think it’s best we continue your studies tenfold."
            show shira at m2 with dissolve
            shira "The Master Mage is known to be benevolent, and if he sees the potential in you that I do, then he may be persuaded to make an exception."
            mc "But Mage Warren…"
            show shira at m1 with dissolve
            shira "Is subject to the will of Aureman."
            shira "He won’t act without his authority to do so, I can promise you that much."
            blank "I can’t explain how, but the assurance sets my rapidly beating heart on a softer pace."
            think "It's a slim chance, "
            show shira at m2 with dissolve
            shira "I hope I haven’t set you on the wrong path by allowing you to stay here…"
            mc "No, you didn’t do anything…"
            show shira at m1 with dissolve
            shira "Even so, I feel...guilty over it. I thought I would be able to protect you better this."
            shira "Ah."
            show shira at m2 with dissolve
            shira "I’m sorry, perhaps I’m overreacting."
            blank "Her gentle touch leaves my cheek."
            shira "It’s sometimes difficult to remember you’re a young man. I’m sure you don’t appreciate being coddled."
            show shira at m1 with dissolve
            shira "But perhaps I can still help you in a small way of my own."
            shira "Come out with me tomorrow."
            shira "There won’t be classes, as it’s Saturday, and I think getting you out of the school may be wise."
            shira "We can go to the shops and find you clothes that you can wear on the weekends."
            mc "We’re in the middle of a crisis and we’re going to go shopping?"
            shira "We’re going to reinforce the belief that you’re a girl. As far as we know, they may only be able to prove that you broke into the library."
            shira "If you used a spell is merely speculation unless they can prove it."
            shira "Getting ahead of any potential extra charges is important right now, if this matter should be investigated. "
            mc "...That's...pretty smart, actually. "
            shira "Well, they didn’t make me a teacher here for nothing."
            blank "She smiles at me warmly."
            shira "Come on. Let’s get you back to your room and get a decent night’s sleep in you."
            scene bg black with dissolve
            scene dormroom_night with dissolve
            show shira at m1 with dissolve
            shira "You’re still shaking a little."
            blank "I glance down at my hands, my fingers trembling beyond my control."
            mc "Oh.."
            think "I didn’t even notice."
            show shira at m2 with dissolve
            shira "It must have really scared you."
            $ mc_clothes = 2
            blank "She helps me slide out of my clothes, putting them aside."
            blank "As it turns out, once you get naked in front of someone once a day for about a week, it starts to lose its strangeness."
            blank "Even when that someone is your unreasonably hot teacher."
            blank "She begins the familiar ritual. Even the thought of it makes me calmer now, knowing the peace that follows it."
            blank "The ritual starts to muddle my mind quickly, layer after layer of consolation and peace spreading through me."
            blank "It muddles my inhibition."
            mc "Why are you so nice in private?"
            blank "I realize how the words sound, thick and strung together. If they were printed on a page, they’d be blurry."
            blank "But my tongue keeps forming them anyway."
            mc "Sometimes in class I think you might just throw me through the nearest window."
            mc "Especially that one time I was late."
            blank "She laughs softly."
            show shira at m1 with dissolve
            shira "I have to maintain high expectations for you. Anything else would be a disservice."
            shira "Besides, sometimes we have to pretend to be one thing, when we’re really the other."
            shira "Maybe it’s not fair, but that’s the way things are."
            blank "I blink up at her tiredly, as she drapes the covers over me."
            show shira at m2 with dissolve
            shira "Don’t worry about my contemporaries for the time being, I’ll be keeping an eye out for you."
            shira "I think a morning of sleeping in will do you good."
            shira "No need to keep a tight schedule. Come meet me in my office whenever you’re ready."
            scene bg black with dissolve
            blank "That I heard those instructions at all was a miracle."
            blank "I think I’m drooling on myself before she even leaves the room."
            blank "I really hope not."
            scene dormroom_day with dissolve
            show charlie at l1 with dissolve
            charlie "Rise and shine, pancakes."
            mc "Pancakes…?"
            show charlie at l2 with dissolve
            charlie "I’m kinda hungry, in case you couldn’t tell."
            charlie "Let’s go, before all the freshies eat up all the syrup."
            mc "Charlie, you’re a freshie, too…"
            charlie "Not technically."
            mc "Then the freshies outrank you."
            show charlie at l1 with dissolve
            charlie "Look, I’m just practicing senior seniority for when it finally happens, okay?"
            blank "I drag my pillow over my head to block out my oncoming headache."
            mc "It’s the weekend, Charlie. It rhymes with sleep in for a reason…"
            charlie "Oh, sure, she can play tongue twister, but she can’t drag herself out of bed for food."
            charlie "Suit yourself, though."
            charlie "I’m going to breakfast and you’re going to go hungry."
            charlie "I’m sure you won’t live to regret that."
            hide charlie with dissolve
            blank "It’s not until after she’s gone that I remember I have plans today anyway."
            blank "I might be falling asleep instantly every night, but I still haven’t gotten the hang of waking up that way."
            blank "I move through my morning routine like a robot doing its best human impression."
            blank "Acquire shampoo."
            blank "Apply shampoo to head."
            blank "Unknown substance detected. "
            blank "Acknowledge label that says body lotion."
            blank "Error Error Error Error."
            blank "By the time I finish un-greasing my hair, there’s knocking at my door."
            mc "Just a second!!"
            shira "I can come back later, if you want…"
            $ mc_clothes = 5
            mc "N-no, I’m ready."
            show shira at m1 with dissolve
            shira "Hi Sophie."
            blank "I brush off my dusty clothes as she walks in."
            shira "Once we get you some decent clothes, you won’t have to go around in this all the time."
            blank "She tugs meaningfully on the sleeve of my school jacket."
            mc "And you’re sure this will take some of the suspicion off of me?"
            show shira at m2 with dissolve
            shira "I’m sure it’s the best I can do for you, under the circumstances."
            shira "I’ve made Charlie busy for the rest of the day, so consider this a time where you can talk openly."
            shira "Come on."
            show shira at m1 with dissolve
            shira "Let’s go before the streets get crowded."
            scene bg black with dissolve
            scene entrance_day with dissolve
            blank "And just like that, Magi Shira has transformed again, out of the strict teacher persona and into someone nice and approachable."
            blank "It puts me at ease, strolling along like this together."
            blank "From a distant square, music drift through the streets and mingles with the sound of voices."
            blank "I nearly press myself against every window as we pass by, taking away a small slice of this crazy, vast city."
            blank "Toys spin and dance behind glass. Candy rotates on a display table. A man works a mound of dough, working it vigorously with hands white with flour."
            blank "In the next window, a posed, busty mannequin has been charmed to move, showing off a collar of expensive fur and waxy cleavage."
            blank "And I nearly trip over a vomit-covered homeless guy passed out in front of the store."
            think "...This is the best place ever!!!!!"
            blank "Magi Shira steers me delicately around the man."
            blank "She guides me into a shop and distracts me with the intimidating notion of picking out clothes."
            scene bg black with dissolve
            scene city_day with dissolve
            blank "Girl clothes."
            think "Ugh. Why is everything gendered?"
            think "Even the robes are gendered. Why!?"
            think "It’s just a fancy dress that we don’t call a dress!!"
            think "At least I can buy some underwear that actually belongs to me…"
            mc "I’ve never had to buy underwear that had lace on it before…"
            mc "I feel like I’m raiding someone’s panty drawer."
            show shira at m1 with dissolve
            shira "You don’t have to, you know. I could keep furnishing you some, if you’re more comfortable that way."
            shira "But you can’t expect me not to pick out things that I think are your colour."
            think "...So I’m either supposed to be comfortable digging through piles of underwear, or comfortable wearing my own teachers?"
            think "Women live the most confusing lives."
            mc "Uhm. Usually I just get the a bunch of identical ones, you know?"
            mc "Maybe I should do that?"
            blank "Shira gives me a look."
            show shira at m2 with dissolve
            shira "That seems rather sad."
            shira "The sorcerers don’t protect our borders just so we can wear bland, identical underwear everyday."
            show shira at m1 with dissolve
            shira "This is about authenticity, after all."
            shira "The more feminine, the better. "
            shira "Look, aren’t these cute?"
            blank "She brandishes a pair in my face until my cheeks overflow with heat and it starts filling up my vision, too."
            mc "Um..."
            show shira at m2 with dissolve
            shira "Ah, I’m sorry, Sophie."
            shira "I’m getting a little too lax around you."
            show shira at m1 with dissolve
            shira "Most of my contemporaries at the Academy are male, and with no one to really ever do this with…"
            shira "I got carried away in the moment. I won’t put you on the spot like that."
            blank "She sighs, slipping a few pairs into a bag for me, and wisely foregoing even asking my opinion."
            show shira at m2 with dissolve
            shira "If anyone from the Academy even caught me near this shop, I’d be mortified."
            mc "Why? Isn’t it obvious you have to buy underwear from somewhere?"
            shira "It is, but that doesn’t make a difference."
            show shira at m1 with dissolve
            shira "Why do you think that is?"
            mc "Because...you’re afraid people won’t take you seriously."
            blank "She nods."
            shira "Exactly. We will always have that working against us."
            show shira at m2 with dissolve
            shira "Err...I’m sorry, I suppose I misspoke. I will. You could still turn back."
            mc "I could, but then I lose my panty shopping privileges with you."
            blank "She smirks."
            show shira at m1 with dissolve
            shira "And why exactly would you be interested in going panty shopping with me, Miss. Sophie?"
            shira "Are we not here out of necessity?"
            mc "Of course…"
            blank "I grin under the heat of her eyes, finding the attitude so impossible to pin down."
            think "Is she flirting or just playing?"
            think "Or play-flirting?"
            think "Or flirting playfully?"
            think "Why do these all sound like they could be legitimately different things that women do with each other!?"
            hide shira with dissolve
            blank "At the nearest opportunity, I dive into a changing stall and out with a new outfit."
            think "Is she deliberately picking things that show off my cleavage or am I just inventing conspiracy theories now?"
            mc "How’s this?"
            mc "Shira…?"
            think "Oh."
            blank "I head toward the back of the store."
            scene scene15a with dissolve
            blank "A man shoves past me, suddenly crowding in on Shira."
            thief "Alright, lady."
            blank "He mutters beneath the rim of a thick moustache. Even from the back, I still catch the words."
            thief "You don’t need pretty clothes today. Give me your cash and I don’t have to bloody the ones you got on."
            blank "In his hand, I see a glint of metal. Something small, but clutched in his fist and pressed toward Shira."
            think "A knife?"
            think "Shira!!"
            menu:
                "Negotiate.":
                    mc "She doesn’t have any cash!"
                    thief "Stay out of this, kid!"
                    mc "I-It’s true! I-I was here buying for her, I swear!!"
                    mc "I’ll give you mine, but she won’t have anything to give you-"
                    scene bg white with hpunch
                    scene scene15b with dissolve
                    blank "The light nearly burns my eyes as I turn away, the pain searing."
                    blank "Glass shatters somewhere."
                    blank "I hear a scream from the counter."
                    blank "Slowly, with the first few hint of shadow and colour, the world blinks back into place."
                    think "Shira…?"
                    scene bg white with dissolve
                    scene scene16a with dissolve
                    blank "A small drop of crimson slides down from her nose and runs into the corner of her lip."
                    think "...Oh. "
                    think "That's...that's not an image I'll be able to forget soon. "
                    mc "Shira..?"
                    mc "Are you alright, did he hurt you?"
                    think "...Where did he even go?"
                    blank "I crane my head around, looking. Only then do I notice the boots."
                    think "Oh."
                    shira "I apologize."
                    shira "You should not have needed to see that."
                    blank "She wipes her nose with the heel of her palm, smearing the blood a little and looking all the more savage for it."
                    blank "Her gaze is transfixed on the spot where she blasted him."
                    scene bg black with dissolve
                    scene city_day with dissolve
                    show shira at m2 with dissolve
                    shira "What a fool. Attacking a robed mage."
                    blank "She scoffs under her breath, which would have quite the effect if she wasn’t covered head to toe in lacy things."
                    blank "Actually, it just adds to it."
                    think "I bet she would make a hell of a dominatrix…"
                    think "Wait, what the hell am I talking about!? We were almost robbed!!"
                    mc "U-Uh, Magi Shira?"
                    blank "Her gaze, still frosty with a cold anger, finally settles on me and thaws once more."
                    show shira at m1 with dissolve
                    shira "Yes, Sophie?"
                    mc "Y-You have a few..uhm…"
                    blank "I point, because I don't know how to tell her exactly what the problem is. "
                    show shira at m2 with dissolve
                    shira "Ah. Yes…"
                    blank "She blushes delicately."
                    show shira at m1 with dissolve
                    shira "No matter. What’s done is done."
                    blank "She steadfastly ignores the squawking of the indigent cashier, still blubbering about the mess"
                    mc "So he didn’t manage to hurt you?"
                    show shira at m2 with dissolve
                    shira "No. What sort of Magi would I be, if a lowlife like that man could?"
                    shira "And to think I once thought this a respectable place."
                    mc "Does that mean we’re not buying the clothes…?"
                    blank "She glances over me with a long look."
                    show shira at m1 with dissolve
                    shira "No, we will take them."
                    scene bg black with dissolve
                    scene city_day with dissolve
                    think "What a nightmare…"
                    think "Maybe it’s not the best place ever…"
                    show shira at m2 with dissolve
                    mc "Is everything alright?"
                    shira "Yes, it’s all sorted out now."
                    blank "She sighs and begins a brisk stride toward the school, a pace that I’ve come to recognize as her teacher walk."
                    mc "Are you sure?"
                    mc "You did what you had to do, Magi Shira-"
                    show shira at m1 with dissolve
                    shira "Naturally."
                    blank "She glances over just to ensure I’m looking when she arches that sceptical eyebrow at me."
                    shira "Remember for when you graduate, we are the power of this land."
                    shira "If I didn't think what I did was needed, why would I have done it?"
                    mc "I thought you might be feeling guilty. About using so much power against a civilian. "
                    show shira at m2 with dissolve
                    shira "He had a weapon and the lack of sense to try and use it."
                    shira "I used as much power as was necessary."
                    shira "What good is our strength if we don’t use it when needed?"
                    mc "I guess so."
                    think "She doesn't seem to have any remorse over killing someone."
                    think "Are all magic users like this, it seems like overkill to me."
                    blank "I follow her down a narrowing alley, though it soon branches into a road I find familiar and leading back to the academy."
                    blank "To safety, though not my own."
                    blank "That I could have gotten hurt barely crossed my mind. It was Shira that had scared me, much as she doesn’t need anyone looking out for her."
                    blank "She certainly handled it.."
                    show shira at m1 with dissolve
                    shira "You need to get more comfortable with using your power when the situation calls for it."
                    shira "You cannot fear it, Sophie."
                    show shira at m2 with dissolve
                    shira "Regardless of what you may have done with it in the past."
                    mc "I wasn’t-- I just didn’t want to hurt anybody."
                    shira "Of course. But sometimes that is what is neccessary, though perhaps..."
                    mc "Perhaps."
                    show shira at m1 with dissolve
                    shira "No, nothing, it doesn't matter."
                    show shira at m2 with dissolve
                    shira "I was planning on tell you and Charlie tonight, but the date of your Initiate Trial has been set. "
                    mc "...You mean my second chance at entrance to the Academy!? Already!?!"
                    show shira at m1 with dissolve
                    shira "It's just the date, Sophie. It's not quite as soon as you think. "
                    shira "You were very close to entrance already, if you gained an Apprenticeship. "
                    mc "But...I don't think I'm ready, I..."
                    blank "She finally sighs and stops, her hand lighting upon my shoulder."
                    show shira at m2 with dissolve
                    shira "Don't worry so much, Sophie. Trust in what you've learned, and what you will learn. "
                    shira "I'd like to go on to be your counsellor, rather than your mentor. "
                    shira "Besides, you still have some time to prepare, so devote yourself to that. "
                    mc "If they've set the trial date, does that mean they're not planning on...you know. "
                    show shira at m1 with dissolve
                    shira "Expelling you? Aresting you? "
                    show shira at m2 with dissolve
                    shira "I don't know. Charlie's date would be the same as yours, of course. "
                    shira "That may be the reason you were both informed. "
                    mc "So I'm still not in the clear. "
                    show shira at m1 with dissolve
                    shira "Defeat Mage Warren and maybe you will be. "
                    mc "Mage Warren!?"
                    shira "You certainly cannot fight me. I would be biased and intent on letting you pass. "
                    mc "And he'll be biased and make me lose!!"
                    show shira at m2 with dissolve
                    shira "He has more honour than you're giving him credit for. He would not deliberately sabotage you. "
                    shira "It will be a fair assessment. "
                    mc "I doubt that...."
                    think "Ughhh. "
                    show shira at m1 with dissolve
                    shira "I won't hear any of that defeatist attitude from you. "
                    shira "That you could have successfully used such a spell is so unlikely, I doubt they can prove it."
                    show shira at m2 with dissolve
                    shira "Breaking into the archive, well...perhaps I can speak to the Master Mage about that. "
                    shira "For now, we’re focusing on your future, not your past."
                    shira "Agreed?"
                    blank "I nod solemnly."
                    mc "Yes, ma’am."
                    show shira at m1 with dissolve
                    shira "Good."
                    blank "We step into the school’s shadow."
                    scene bg black with dissolve
                    scene entrance_day with dissolve
                    show shira at m2 with dissolve
                    shira "I will trust you and Charlie will practice every day, even outside of our usual classes."
                    show shira at m1 with dissolve
                    shira "With any luck, your skills will get you into the Academy and buy the Master Mage’s silence."
                    scene bg black with dissolve
                    scene classroom with dissolve
                "Attack.":

                    $ shira5 = True
                    blank "Power floods through my fingertips, kindled by anger."
                    scene scene15c with dissolve
                    blank "As my own power manifests, so to does Magi Shira's own power."
                    mc "What the…?!"
                    blank "With a surge of anger, the spell lets loose and catches the man right beneath his ribs."
                    blank "He stumbles backwards, sprawled helplessly across the floor and gasping for breath."
                    blank "I deny him that."
                    blank "I coil my magic around his neck, my fingers shaking with the effort to restrain myself."
                    shira "Stay down."
                    blank "Her own power slams into him then with an explosion of energy our magic intwines."
                    scene bg white with vpunch
                    scene scene16b with dissolve
                    blank "My hand lowers, my head swimming as I feel how much that drained my energy."
                    blank "I sway on my feet, but a sturdy arm catches me around the waist."
                    shira "Easy."
                    blank "She holds me against her side."
                    blank "I rub my head, but the feeling is already starting to pass."
                    mc "I’m sorry. I wasn't thinking."
                    shira "Sorry? You acted to save me."
                    shira "Granted, I was doing that myself, but I’m still quite grateful."
                    mc "Really?"
                    mc "You’re not mad?"
                    mc "I attacked a citizen with magic… And..."
                    shira "His fate was determined the moment he drew that blade, trust me your involvement only ensured a quicker passing."
                    think "Is she saying she was aiming to kill him as well."
                    think "And it wasn’t like I was thinking about what I was doing. I was practically blind with rage."
                    think "Magi Shira however was acting as she saw fit. "
                    shira "You attacked a criminal with magic."
                    shira "A person with intent to harm."
                    shira "What do we study magic for, if not for the advancement and betterment of society?"
                    mc "I suppose."
                    shira "You did the right thing. Don’t ever doubt that. I don't."
                    shira "And you even showed a talent for it."
                    mc "A talent…?"
                    shira "I think you are more suited to combative magic now, which you should be. "
                    shira "And just in time. "
                    scene bg black with dissolve
                    scene city_day with dissolve
                    show shira at m2 with dissolve
                    shira "Initially, I was planning on telling you and Charlie tonight, but I can give you a sneak-peek."
                    mc "A sneak-peek of what? "
                    shira "Your Initiate Trial. "
                    shira "They've set a date for your reassessment. "
                    mc "A date!?"
                    mc "I-Is it soon!?"
                    show shira at m1 with dissolve
                    shira "You still have a few weeks. With the rest of the school preparing for the Magi Wars, your reassessment must come before that. "
                    shira "Once that begins, we will be quite busy and you will be either in it or not."
                    mc "B-but I need more time!!"
                    shira "You shouldn't. If you were close enough to admittance to be an Apprentice, this time should be enough to refine your skills. "
                    mc "But..."
                    show shira at m2 with dissolve
                    shira "Are you turning down a challenge, Sophie?"
                    mc "N-no!"
                    mc "Not at all, I…"
                    show shira at m1 with dissolve
                    shira "I’m only teasing you."
                    blank "She links her arm in mine."
                    show shira at m2 with dissolve
                    shira "You don't need to worry. I believe you'll do just fine. "
                    shira "Show them what I already know."
                    blank "I smile under the praise, my head dipping down to try and shy from her intent gaze."
                    shira "I did appreciate what you did back there, you know."
                    show shira at m1 with dissolve
                    shira "You have more power than you know, when you need to call upon it, and better instincts than most."
                    think "Better instincts, is she really praising me for helping her to kill?"
                    shira "Together, you and I can do a great deal."
                    shira "Don’t you think so?"
                    blank "I nod."
                    blank "I don’t even know what I’m agreeing to, but I know she’s flattering me and it makes my face burn."
                    blank "The tips of her fingers card through the ends of my hair."
                    show shira at m2 with dissolve
                    shira "I’ll be here for you, Sophie."
                    shira "No matter what Mage Warren or the Master Mage try to do."
                    scene bg black with dissolve
                    scene classroom with dissolve

            blank "Magi Shira immediately puts us to work to train for our trial, much to Charlie’s shock."
            blank "She was just as horrified as I was, but she warms up to the idea pretty quickly."
            jump impendingtrial


label impendingtrial:
    scene bg black with dissolve
    scene classroom with dissolve
    play music "music/maintheme.ogg" fadeout 1 fadein 1
    $ mc_clothes = 8
    $ charlieoutfit = 'uniform'
    $ shiraoutfit = 'robes'
    blank "The promise of our pending trial sends Charlie and I on a training frenzy."
    blank "We spend so much time in the classroom, perfecting spells and learning magic theory, that my concerns about Aureman and Warren are briefly set aside."
    blank "Maybe they aren’t going to make a move so soon, or maybe they don’t have evidence."
    blank "Whatever the reason, neither of them seem to take any unusual interest in me in the next week or so."
    blank "And Charlie and I are advancing our skills more than ever. "
    show charlie at l1 with dissolve
    charlie "Come on, Sophie, you’ve gotta try this!!"
    blank "Her feet hover just a few inches off the ground, magic holding her suspended in the air."
    mc "Is that really practical?"
    $ shiraface = 'happy'
    show shira at r1 with dissolve
    shira "Impressive, maybe. Practical, no, I wouldn’t think so."
    charlie "But it does look cool."
    charlie "Admit it."
    $ charlieface = 'happy'
    show charlie at l2 with dissolve
    charlie "I’m literally flying."
    mc "You fly about as well as fish walk."
    mc "You’re hovering. There’s a difference."
    $ charlieface = 'neutral'
    show charlie at l1 with dissolve
    charlie "Well you’re not doing either, so I don’t want to hear it until you can get on my level."
    blank "Grumbling under my breath, I try to will myself upwards using the same spell Charlie used."
    blank "I squint my eyes closed, trying my best."
    mc "Any luck?"
    $ charlieface = 'flirty'
    show charlie at l2 with dissolve
    charlie "Nope. You just look constipated, or like you’re trying really hard to will yourself out of existence."
    mc "Ugh."
    mc "I can’t get the hang of this."
    scene bg black with dissolve
    scene classroom with dissolve
    $ charlieface = 'neutral'
    blank "We even fill our weekends with training."
    blank "Magi Shira smuggled us a couple more advanced books, which we use to practice on our own."
    blank "They’re nothing terribly hard, but they go a little beyond our usual curriculum, and we use them when we’re not in class with her."
    show charlie flip at m1 with dissolve
    charlie "You know what’s cool?"
    blank "She flips through a couple pages of the book."
    $ charliepose = '2'
    show charlie flip at m2 with dissolve
    charlie "Teleporting."
    mc "Let’s do it."
    show charlie flip at m1 with dissolve
    charlie "Uh. You know what’s also dangerous?"
    mc "Not pursuing your dreams and letting fear hold you back?"
    charlie "I don’t remember ordering a walking, talking self-help book."
    mc "Come on, you were the one who brought it up knowing full well I would totally try it."
    $ charliepose = '1'
    $ charlieface = 'flirty'
    show charlie flip at m2 with dissolve
    charlie "Maybe I just want to see you stuck in a wall somewhere."
    mc "Rude."
    mc "I’ll be great."
    $ charlieface = 'sad'
    show charlie flip at m1 with dissolve
    charlie "You’re going to get these books confiscated and probably send yourself to the medical wing."
    mc "You want to bet money on it?"
    charlie "Sure, just write me into your will."
    blank "I roll my eyes."
    $ charlieface = 'blush'
    show charlie flip at m2 with dissolve
    charlie "Really, though. I don’t want you to accidentally kill yourself. It’s pretty complicated stuff."
    charlie "It involves navigating a whole other plane of magic, and I don’t know what that means, but I know I can’t do it."
    mc "Look, it’s like baking a cake."
    mc "You just follow the steps to the letter, and there you go. Basic stuff."
    $ charliepose = '2'
    show charlie flip at m1 with dissolve
    charlie "...You’ve never actually baked a cake before, have you?"
    mc "Just give me the book!"
    think "Oh, jeez."
    think "This does look complicated."
    think "Even the instructions for how to centre your magic seem vague, at best."
    $ charliepose = '1'
    $ charlieface = 'neutral'
    show charlie flip at m2 with dissolve
    charlie "Just try it from one side of the room to the other."
    blank "I muster up my magic, letting it envelop my body until it reaches every part of me."
    think "Considering how similar this feels to levitating, I’m probably going to be terrible at this."
    charlie "Okay. Guide the magic inward."
    blank "I start chanting the words of the spell, standing as still as I possibly can. "
    show charlie flip at m1 with dissolve
    charlie "Allow your body to mingle with the magical planes around you. Whatever that means."
    charlie "And then…"
    scene bg black with dissolve
    blank "I close my eyes, envisioning an imaginary path between me and the place I want to go."
    blank "I inwardly push myself toward that spot, never moving my feet."
    blank "For about three solid minutes Charlie and I just stay like that, my eyes squeezed shut. "
    blank "…"
    blank "…"
    shira "Sophie!?"
    mc "What!?"
    scene scene17a with dissolve
    mc "Magi Shira!?!"
    mc "H-how did I-"
    mc "But-"
    mc "I-"
    mc "I- I can explain, I swear!"
    think "Once I figure out how to stop staring."
    shira "How did you get in here!?"
    menu:
        "...I teleported?":
            shira "Into my bedroom!?"
            mc "I-uh-I think I might have overshot my target just a bit."
            mc "Um. Which side of the school is this on again?"
            shira "Sophie, you know very well you aren’t meant to use that type of magic!"
            mc "But you gave us the book…"
            shira "For spells that bridge the gap between your current skills and more advanced magic's."
            shira "Not so you can jump right into skills far above your current abilities!"
            mc "...But I succeeded, didn’t I?"
            shira "I…"
            blank "Her scowl softens into an exasperated, if not fond roll of her eyes."
            blank "It’s a look I’ve seen a lot throughout my life."
            shira "I’m hesitant to call this a success."
            shira "You were lucky more than anything."
            think "You can say that again."
            shira "But you do seem to have an aptitude for pulling off spells that are quite dangerous, with only minor repercussions."
            mc "Is detention a minor repercussion?"
            shira "Detention?"
            mc "I..uhm…"
            blank "I point awkwardly."
            mc "You were changing…"
            shira "Oh."
            shira "Well, I do see you in this state each night before you go to sleep."
            shira "It seems only fair, I suppose."
            blank "For once, I’m incredibly glad I’m not a boy."
            blank "There’s no way I could hide a male reaction to this."
            shira "You are either incredibly gifted or incredibly lucky, I’ll admit that much."
            shira "No more teleporting, Sophie, but this will be another secret for us to share."
            blank "She gives me a small, coy smile."
            shira "Now, if you could let me change?"
        "Fate?":

            shira "...You teleported, didn’t you?"
            mc "Accidentally."
            shira "No one accidentally teleports, it’s very deliberate magic!"
            mc "Well...I didn’t exactly stick the landing is what I mean."
            mc "I didn’t mean to um...intrude…"
            blank "And she doesn’t keep getting dressed, apparently too intent on lecturing me to care that I’m getting the best possible reward for misbehaviour."
            shira "That’s dangerous magic, Sophie!"
            mc "I realize that now."
            mc "I could have dropped in on Mage Aureman changing or something."
            shira "Be serious."
            blank "She scowls, and it dawns on me that I’m not dealing with the Jekyll of her personalities."
            blank "She’s actually upset."
            mc "I really didn’t mean to see…"
            shira "This is about you continuously being irresponsible with magic, not about what you saw."
            shira "I have better priorities than to think that this is the worst of my problems!"
            shira "Go back to the classroom and continue your training."
            shira "I’ll want a paper come Monday morning about historical instances of teleportation gone wrong."
            shira "Now leave me to change."
            shira "And walk back!"

    blank "I take one last look and then bolt out of there, my heart racing."
    scene bg black with dissolve
    scene classroom with dissolve
    $ charliepose = '1'
    $ charlieface = 'mad'
    show charlie flip at m1 with dissolve
    charlie "What happened to you!?"
    $ charlieface = 'sad'
    show charlie flip at m2 with dissolve
    charlie "I thought for sure you accidentally launched yourself into the sky or something!"
    mc "Oh Gods, it was worse."
    blank "I slump down against the wall."
    $ charliepose = '2'
    show charlie flip at m1 with dissolve
    charlie "What?"
    mc "I accidentally teleported...right into Magi Shira’s bedroom."
    $ charlieface = 'neutral'
    show charlie flip at m2 with dissolve
    charlie "You didn’t. Seriously? Was she in there?"
    mc "Of course she was. You think the universe actually likes me enough to let me get away with something like that?"
    mc "It’s even worse."
    charlie "How could it get worse?!"
    charlie "Was she with Mage Warren? Did you collapse on top of her? "
    mc "What? No!! She was...changing clothes."
    charlie "... "
    $ charlieface = 'happy'
    show charlie flip at m1 with dissolve
    charlie "Bahahahah!!!"
    $ charlieface = 'flirty'
    $ charliepose = '1'
    show charlie flip at m2 with dissolve
    charlie "Ahhh, Sophie the pervert!!"
    charlie "What did she say!? Tell me everything."
    blank "She hits me in the arm until I recount my every embarrassing second to Charlie, who devours my embarrassment like an emotional vampire."
    $ charlieface = 'neutral'
    show charlie flip at m1 with dissolve
    charlie "You know, for as much as you worry about getting expelled...you’re really not trying to avoid it."
    mc "Because you suggested it--!!"
    scene bg black with dissolve
    blank "It becomes a game, to find some questionably dangerous spell and see if I’ll try it or not."
    blank "In my defence, I say no most of the time."
    blank "If I’ve learned anything at school so far, besides how to unintentionally set my own hair on fire, it’s how to set limits for myself."
    blank "...Until I get challenged."
    blank "Then all bets are off."
    blank "Our classroom courses remain steady, though."
    if friends:
        blank "And Charlie and I have stayed close, practicing magic and hanging out together daily."

    scene library_day with dissolve
    $ charlieoutfit = 'smart'
    $ mc_clothes = 7
    $ charlieface = 'mad'
    show charlie flip at m1 with dissolve
    charlie "When I agreed to training, you didn’t tell me I was trading away every Saturday for the rest of my life."
    charlie "I need a break from school."
    blank "She presses her face into the book, until she takes a breath of dust and sneezes."
    $ charlieface = 'blush'
    show charlie flip at m2 with dissolve
    charlie "Ughhhhhh."
    blank "I sigh, resting my chin on my palm as I glance over the upside-down words."
    mc "I’m burnt out, too."
    mc "But we have to keep going."
    charlie "Only if I get first pick of what we do."
    blank "I shrug indifferently, and Charlie slowly thumbs through the heavy pages. "
    blank "I think she’s hoping she’ll forget how to read so we don’t have to do anything."
    blank "I watch as the words drift past, one page at a time."
    charlie "Hmmm."
    blank "She finally taps her chin, a sure sign that she's found something devious. "
    mc "What’s in store for me today? Controlling animals? Turning invisible? ...Changing my gender?"
    $ charlieface = 'neutral'
    $ charliepose = '2'
    show charlie flip at m1 with dissolve
    charlie "Pft. Pretty sure that’s not possible."
    think "You’d be surprised…"
    blank "She pulls out a piece of paper that's been tucked into the back pages of the book."
    mc "What’s that? A note?"
    $ charliepose = '1'
    show charlie flip at m2 with dissolve
    charlie "No. It looks like it was from another text book or something."
    blank "She squints down at it."
    show charlie flip at m1 with dissolve
    charlie "Look how yellow it is. It must be pretty old, but you can still make out the writing."
    blank "The paper slides toward me under her palm."
    mc "Oh, no."
    mc "No, no, no, I am not getting involved in whatever that is."
    mc "Random, old rituals shoved into the back of textbooks, that’s just asking for trouble--"
    think "I learned my lesson the first time."
    charlie "Oh, don’t be so paranoid, Sophie."
    $ charlieface = 'flirty'
    show charlie flip at m2 with dissolve
    charlie "What’s the worst that could happen?"
    think "Oh, I don’t know, maybe a dude could suddenly grows boobs and have a high pitched voice and have to call himself Sophie for the rest of his life?"
    think "At least Charlie wouldn’t have to change her name."
    mc "I..hear bad stuff can happen if you don’t know what you’re doing."
    $ charlieface = 'neutral'
    show charlie flip at m1 with dissolve
    charlie "I bet it’s nothing. Someone’s old homework assignment or something."
    blank "She pushes it toward me suddenly, smirking."
    charlie "Just try it."
    menu:
        "Not happening.":
            play music "music/track07.ogg" fadeout 1 fadein 1
            charlie "Fine, I’ll do it."
            mc "What?"
            $ charlieface = 'annoyed'
            show charlie flip at m2 with dissolve
            charlie "If you’re not going to do it, then I will."
            mc "No! Charlie, come on-"
            blank "But she grabs the paper again, starting to chant softly under her breath as her hands move in a steady rhythm."
            blank "I recognize the gestures, though the order is complicated and the instructions for the vocalization seems so strange. Almost call and response."
            mc "Uhm, Charlie."
            $ charlieface = 'neutral'
            show charlie flip at m1 with dissolve
            charlie "I’m trying to focus!"
            mc "Charlie, seriously, something’s happening.."
            blank "Beneath the book, a pink glow emanates, spilling the colour across the table."
            blank "But it gets to a point and pauses, Charlie’s expression screwed up in deep concentration."
            think "She isn’t strong enough…"
            blank "Forcing down my reluctance, I slide in next to her. Joining hands we combine our powers."
            scene bg white with dissolve
            blank "The glow forms a large circle over the table."
            blank "Two, actually, side by side, with smaller circles growing within them…"
            think "Uh."
            think "Maybe I’m just a pervert, but it’s kind of starting to look like…"
            scene scene18a with dissolve
            eri_unknown "Ahhhhaaaa~~"
            mc "What the!?"
            blank "Charlie practically flips backwards out of her seat."
            charlie "What is that!?"
            eri_unknown "It’s been such a long time..."
            think "What...what on Earth did we do?"
            think "What is this thing?!"
            eri_unknown "So you’re the one who summoned me, mmh?"
            eri_unknown "How lucky."
            blank "She blinks down at Charlie, a smile curving over her mouth and showing a few sharp, white teeth."
            charlie "I d-d-didn’t mean to, sorry, now go back where you came from!"
            charlie "S-seriously, shoo!"
            eri_unknown "Hmm, how about no? I want to stay here. You asked for me, didn’t you?"
            charlie "I don’t even know what you are!!"
            blank "Charlie gives me a bewildered look, but I just shrug helplessly."
            think "I don’t know, either. All I know is that she’s a girl. Definitely a girl."
            eri_unknown "You mean you really don’t know?"
            scene library_day with dissolve
            show charlie at l1 with dissolve
            show eri at r1 with dissolve
            blank "She slides off the table toward Charlie, pinning her in suddenly against the bookcase."
            charlie "Ahhhh!! Sophie, get it off me!"
            show eri at r2 with dissolve
            eri_unknown "Shhhh."
            blank "She presses a tapered fingertip to Charlie’s lips, pressing her mouth against the shell of her ear."
            eri_unknown "I’m just giving you some context clues."
            show charlie at l2 with dissolve
            charlie "Sophie, it’s gonna eat me!!!"
            show eri at r1 with dissolve
            eri_unknown "Hmmm, I could definitely do that, if you want--"
            blank "She starts to drop down to her knees."
            mc "A succubus!!"
            blank "Both of them turn toward me, blinking."
            mc "That’s what you are."
            mc "You’re a type of demon."
            show eri at r2 with dissolve
            succubus "Bingo!"
            succubus "Do you want a prize, too?"
            blank "She starts to crawl my way, and unlike Charlie, I don’t have the sense to back away."
        "...Fine.":

            play music "music/track07.ogg" fadeout 1 fadein 1
            $ demon_love += 1
            charlie "Ha. You didn’t even put up a fight. You’re curious, too."
            blank "I glance down at the paper, trying to read through the instructions."
            think "This looks complicated."
            $ charlieface = 'neutral'
            show charlie flip at m2 with dissolve
            charlie "It all looks complicated. Just try it."
            charlie "What’s the worst that could happen?"
            blank "I have a few ideas, but I decide not to say them."
            blank "Instead, I focus on the ritual, muttering the words under my breath and ignoring Charlie’s criticisms of my technique."
            think "If she thinks she knows better, why doesn’t she do it!?"
            blank "But I must be getting somewhere, a tingling rising in my hands as light begins to creep across the table in front of us."
            think "Something’s happening…"
            charlie "I think you’re doing it, Sophie!"
            think "That would be encouraging, if I had any idea what “it” is."
            think "For all I know, I’m turning this table into an explosive."
            think "That’ll be interesting to explain…"
            blank "The light grows brighter, my magic beginning to fray as its limits are tested."
            blank "I’m giving it everything I have, but it’s just not enough."
            blank "Suddenly, Charlie’s at my elbow, mimicking my gestures and words."
            blank "She gives me a quick wink out of the corner of her eye as we lean over the paper, haphazardly performing the ritual together."
            scene bg white with dissolve
            blank "The pink coloured light spills across the table into two circles."
            blank "And then two smaller circles appear within those."
            blank "Wait are second…"
            think "Are those…?"
            blank "It looks like something you’d find on the wall of a middle school bathroom stall, and if I didn’t know better…"
            scene scene18a with dissolve
            think "!!??"
            think "What is that!?"
            blank "Charlie lets out a yelp."
            eri_unknown "Ohhh~ A threesome?"
            think "Sh-she just appeared out of thin air!?"
            charlie "Where did you come from!?"
            eri_unknown "From your naughtiest dreams, of course."
            eri_unknown "And what can I do for the two of you?"
            mc "What?"
            eri_unknown "How many ways do I need to ask?"
            eri_unknown "How can I be of pleasure? Do you want me to be a cookie or the cream?"
            charlie "...Okay, Sophie, you did this, so this crazy slut is definitely your problem."
            mc "You helped!"
            eri_unknown "Is that right?"
            blank "She leans toward me, my feet stumbling back."
            eri_unknown "So you’re the one I should be calling Master?"
            eri_unknown "Or do you prefer Mistress?"
            blank "She winks at me, the colour rising into my face."
            think "Does she know…?"
            think "B-but how?"
            think "Who even is she!?"
            eri_unknown "Cat got your tongue?"
            eri_unknown "Awwww."
            scene scene19a with dissolve
            eri_unknown "I’ll fight the cat for it."
            blank "Her pink tongue glides along her teeth, a surprising strength pinning me down beneath her."
            blank "Alarm bells ring in my head."
            think "System overload."
            think "Terminating all brain function."
            charlie "Hey! Get off of her--you--sleazy--!!"
            blank "Charlie emphasizes every word with a smack of the book we had been using, the woman ducking her head against it."
            scene scene19b with dissolve
            eri_unknown "Hey!!"
            eri_unknown "Knock it off, brat!!"
            eri_unknown "I’m trying to work here!"
            blank "Suddenly, the answer pops into my brain, making me feel like an idiot for not realizing it sooner."
            mc "You’re a succubus!"
            succubus "Ahhh, so you’re not complete idiots after all."
            succubus "I knew you had it in you."
            blank "Her fingers run over my chest as I squirm beneath the touch."
            succubus "That and more."
            charlie "I’m gonna be sick."
            succubus "Uh, you’re kind of ruining the mood here."
            succubus "You summoned me for a purpose and I’m here to serve."
            blank "She winks."
            succubus "It’s been a long time since I’ve gotten any lady action."
            charlie "Subtlety isn’t exactly your style, is it? Porn has more convincing dialogue."
            succubus "But does it have the benefit of being in the flesh?"
            blank "She takes my hands and guides them to her hips."
            succubus "I’m all real and right here for the taking."
            charlie "Sophie, get up and help me put this demon-nympho back wherever she came from!"
            succubus "You won’t do that to me, will you?"
            succubus "I see what you really want."
            blank "She purrs lowly, lidded eyes staring right through me as she leans in a little closer."
            blank "She presses her mouth against my ear in a breathy whisper."
            succubus "You won’t turn me away. You won’t make me go back there without a little fun first."
            blank "She glances up."
            succubus "But if your friend is getting a little jealous, I’ll let her join in, too."

    scene bg black with dissolve
    scene library_day with dissolve
    $ eriface = 'flirty'
    $ eripose = '2'
    show charlie at l1 with dissolve
    show eri at r1 with dissolve
    succubus "So what do you want me to do for you?"
    succubus "You did summon me after all."
    blank "She gives a breathy moan."
    $ eripose = '1'
    $ eriface = 'excited'
    show eri at r2 with dissolve
    succubus "I’m at your beck and call."
    $ charlieface = 'sad'
    $ charliepose = '2'
    show charlie at l2 with dissolve
    charlie "Alright, this is some dime store novel trash and I’m not having it-"
    succubus "What did you call me!?"
    charlie "I’m just saying, isn’t this a little over the top!?"
    charlie "I get you’re supposed to be a sex demon and everything, but you’re coming on a little strong."
    $ eriface = 'happy'
    show eri at r1 with dissolve
    succubus "I won’t be the only one coming~"
    $ charliepose = '1'
    show charlie at l1 with dissolve
    charlie "Oh, God."
    charlie "That’s it."
    blank "She reaches for the paper."
    charlie "How do we put it back?"
    $ eriface = 'sad'
    show eri at r2 with dissolve
    succubus "Hey, no!!"
    blank "The demon snatches the paper away, crumpling it against her chest protectively."
    succubus "I haven’t even got to do anything yet!"
    mc "Hang on a second, Charlie, I think we’re moving a little fast here."
    $ charliepose = '2'
    show charlie at l2 with dissolve
    charlie "We’re the ones moving fast!?"
    charlie "Sophie, I think we just found some pervo Mage’s secret fap material and I don’t know about you, but it’s kind of gross."
    charlie "Also probably illegal."
    think "As if that’s anything new to my life."
    $ eriface = 'annoyed'
    show eri at r1 with dissolve
    succubus "So, do I get any say in this?"
    $ charlieface = 'mad'
    show charlie at l1 with dissolve
    charlie "No."
    mc "Charlie, she obviously has feelings."
    blank "The demon slides a hand low along her pelvis."
    succubus "Oh, I most certainly do. So many feelings~"
    show charlie at l2 with dissolve
    charlie "I’m gonna be sick."
    $ eriface = 'happy'
    show eri at r2 with dissolve
    succubus "If you didn’t want me, you shouldn’t have helped summon me."
    charlie "I didn’t know what I was doing!"
    $ charlieface = 'sad'
    show charlie at l1 with dissolve
    charlie "Sophie, help me get rid of this!!"
    mc "Shh!"
    charlie "What?"
    blank "Click. Click. Click."
    blank "Magi Shira’s signature approach."
    show charlie at l2 with dissolve
    charlie "Oh no."
    mc "You have to hide!!"
    blank "The demon just gives me a confused scowl as Magi Shira opens the door."
    $ eriface = 'determined'
    $ shiraface = 'neutral'
    $ shirapose = '3'
    show shira at m1 with dissolve
    shira "Sophie, Charlie."
    shira "How goes the studying?"
    blank "Sweat pours down my neck as she looks up at us."
    mc "U-uh-uhm."
    mc "We, uh…"
    blank "Shira’s face flickers in confusion, eyes narrowing suspiciously."
    $ shiraface = 'annoyed'
    show shira at m2 with dissolve
    shira "Is something the matter?"
    blank "The demon lets out a sultry laugh."
    $ eriface = 'happy'
    show eri at r1 with dissolve
    succubus "Your faces!"
    $ eriface = 'neutral'
    show eri at r2 with dissolve
    succubus "Watch, loves."
    blank "She saunters toward Magi Shira, who stares through her, still looking straight toward us."
    $ eriface = 'flirty'
    show eri at r1 with dissolve
    eri "Nice to meet you. I’m Eri."
    blank "She extends a hand, which goes entirely unnoticed."
    eri "Oops, looks like she’s not in a talkative mood."
    blank "Her hands feign twisting Shira’s boobs."
    eri "It’s a pity she can’t see me, I’d like to get a handful of these bad girls."
    blank "Shira steps forward suddenly, Eri appears to magically slide to one side."
    $ shiraface = 'neutral'
    show shira at m1 with dissolve
    shira "Speak up. What's wrong?"
    mc "N-Nothing. I just...we were taking a little break."
    blank "I rub the back of my neck, trying to cover up our silence."
    blank "She studies us suspiciously."
    $ shiraface = 'happy'
    $ shirapose = '1'
    show shira at m2 with dissolve
    shira "It is the weekend after all, you don’t need to extend yourself too much...."
    shira "I brought some more books with the Master Mage’s approval, in case you wanted to look through them."
    blank "Eri peers over her shoulder."
    $ eriface = 'sad'
    $ eripose = '3'
    show eri at r1 with dissolve
    eri "Looks boring."
    $ eriface = 'excited'
    $ eripose = '2'
    show eri at r2 with dissolve
    eri "Where’s the romance? The erotica?"
    blank "The way her face is deepening into a scarlet colour, I think Charlie’s about to have an aneurysm."
    blank "Shira gives us another long, wondering look."
    show shira at m1 with dissolve
    shira "Well, if everything’s alright, I suppose I’ll go…"
    charlie "Y-yes, we’re fine."
    mc "Goodbye!"
    blank "Too cheery."
    hide shira with dissolve
    blank "But Shira just blinks at us and leaves, shaking her head as she goes."
    blank "I feel like I’ve been underwater for five minutes, finally taking a deep breath."
    charlie "She can’t see you?"
    $ eriface = 'determined'
    show eri at r1 with dissolve
    eri "Of course not, sweetling. You summoned me, so you have exclusive rights to this eye candy."
    blank "She shimmies slowly."
    $ eripose = '1'
    show eri at r2 with dissolve
    eri "I’m just for your viewing pleasure~"
    blank "I slump down into my chair with a heavy sigh."
    think "How many close calls can I really have with expulsion? Or is this sort of thing just everyday nonsense in a school that teaches magic?"
    think "I really haven’t figured it out yet, but I haven’t heard of any other students opening up portals to hell."
    show charlie at l1 with dissolve
    charlie "She can’t stay, Sophie."
    eri "Hmph."
    show eri at r1 with dissolve
    eri "She’s so mean. A real sadist if you ask me."
    eri "I can be that way, too, if that’s what you’re into."
    mc "I’m not INTO anything.."
    $ eriface = 'neutral'
    $ eripose = '3'
    show eri at r2 with dissolve
    eri "Ohh. Unexplored desires. My favourite."
    mc "We do have a small problem…"
    $ charlieface = 'neutral'
    show charlie at l2 with dissolve
    charlie "Just a small one?"
    mc "I don’t see a way here to un-summon her. It’s just the summoning ritual…"
    blank "She looks over the paper like maybe it was written in invisible ink, but no."
    blank "There’s just no way."
    mc "Which one of us said what’s the worst that could happen?"
    $ charlieface = 'blush'
    show charlie at l1 with dissolve
    charlie "I’m not taking the heat for this."
    mc "All things considered, it could have been worse, right?"
    mc "We could have summoned some powerful demon hell-bent on destroying the school or something."
    mc "But Eri looks nice enough."
    $ eriface = 'flirty'
    show eri at r1 with dissolve
    eri "Ohh, the sweet, innocent angle, hm? That’s how you like to play?"
    $ eriface = 'excited'
    $ eripose = '2'
    show eri at r2 with dissolve
    eri "Oh, s-senpai, notice me~"
    charlie "…"
    charlie "That sounds so completely wrong with you looking like that."
    mc "…"
    blank "Eri scratches the back of her head."
    $ eriface = 'determined'
    $ eripose = '1'
    show eri at r1 with dissolve
    eri "Alright, alright, I’m not very good at that one. I’m working on it!"
    blank "I sigh."
    mc "All my power was spent summoning her. There’s no way I’m going to be able to keep practicing."
    mc "I guess we might as well go to dinner."
    $ charlieface = 'mad'
    show charlie at l2 with dissolve
    charlie "With that!?"
    mc "No one said she had to come."
    $ eriface = 'neutral'
    show eri at r2 with dissolve
    eri "I want to come! All night~"
    mc "Look at it this way, maybe she can help us with our trials somehow..."
    blank "But she’s not listening. Instead, Charlie groans and storms out of the library."
    hide charlie with dissolve
    eri "In my immodest professional opinion...she really needs to get laid."
    scene bg black with dissolve
    scene dininghall with dissolve
    $ charlieface = 'neutral'
    $ charliepose = '1'
    $ eripose = '3'
    show charlie at l2 with dissolve
    show eri at r2 with dissolve
    eri "Nnnn, that looks so good..."
    blank "Eri eyes my plate like a puppy begging for scraps."
    $ charlieface = 'sad'
    show charlie at l1 with dissolve
    charlie "I can’t believe you’re letting her sit with us."
    mc "How am I supposed to stop her, exactly?"
    $ charlieface = 'angry'
    show charlie at l2 with dissolve
    charlie "You could ask! She said we're her masters, so can’t we just...tell her to go away?"
    mc "Is that how it works, Eri?"
    $ eriface = 'happy'
    show eri at r1 with dissolve
    eri "Nope."
    blank "I give Charlie a look."
    mc "See?"
    $ eriface = 'flirty'
    show eri at r2 with dissolve
    eri "So why don’t you losers sit with your classmates?"
    eri "Some of these people are really attractive.."
    mc "We don’t really know anyone. Those are all Initiates of the Academy."
    mc "We’re just Apprentices."
    blank "Eri bursts out laughing."
    $ charlieface = 'mad'
    show charlie at l1 with dissolve
    charlie "It’s not funny! We’re just as good as anyone else here!"
    blank "I’ve never seen Charlie get so worked up before."
    eri "Darling, if you were just as good, you’d be sitting with them. Besides, that’s not what’s funny."
    eri "You two are so determined to send me away, when I could help you."
    eri "I mean, I am a demon. Don’t you think I might have some insight into magic?"
    $ charlieface = 'annoyed'
    show charlie at l2 with dissolve
    charlie "I think you’re wicked and probably here for no good."
    blank "Eri’s look sours."
    mc "Then you should watch your tongue, shouldn’t you?"
    $ eriface = 'determined'
    show eri at r1 with dissolve
    eri "And to think I thought about introducing that tongue to mine."
    eri "Hmph. Now that’s never going to happen."
    charlie "Woah. Sophie, look."
    blank "She kicks me gently under the table, turning my attention toward the teacher’s table."
    show warren flip at m1 with dissolve
    blank "He stares right at us as he strides past. Worry knots itself in my stomach."
    think "…"
    blank "He passes by so close his robes nearly brush my arm."
    hide warren flip with dissolve
    mc "Could he see her?!"
    blank "Eri laughs again."
    mc "You think he was looking at me?"
    blank "She tugs on a piece of my hair."
    $ eripose = '1'
    $ eriface = 'flirty'
    show eri at r2 with dissolve
    $ charliepose = '2'
    $ charlieface = 'neutral'
    show charlie at l2 with dissolve
    eri "He was definitely checking you out. Must be those cherubic cheeks of yours."
    eri "And I don’t mean the ones on your face."
    blank "Annnnd there goes my appetite."
    mc "I’m pretty sure he was looking at me for an entirely different reason."
    think "Though at this point, I’d probably prefer if he was checking me out."
    blank "A gaggle of students swarms up behind us, talking loudly with each other."
    mc "I’ll tell you later."
    blank "I stab at my tray with a fork."
    think "Well, since I can’t find a way to get rid of her, I guess I have two friends now."
    scene bg black with dissolve
    scene dormroom_night with dissolve
    mc "Why am I the one who gets stuck with her?"
    $ charlieface = 'flirty'
    show charlie at l2 with dissolve
    show eri at r2 with dissolve
    charlie "You can handle her better than I can. It just makes sense. "
    blank "Eri sighs, almost a little sadly. "
    blank "Even Charlie looks a bit remorseful, as we squabble over her like a kid neither parent wants in the divorce. "
    $ eriface = 'happy'
    $ eripose = '1'
    show eri at r1 with dissolve
    eri "It's fine...."
    eri "I can just go outside...in the dark...by myself..."
    $ charlieface = 'mad'
    show charlie at l1 with dissolve
    charlie "Don't be dramatic. "
    blank "Eri just heaves another equally dramatic sigh. "
    charlie "...Alright, I'm sorry! At least don't mope around forever. "
    $ eriface = 'flirty'
    show eri at r2 with dissolve
    eri "Make it up to me!!"
    mc "How...?"
    eri "I think you know how~"
    $ charlieface = 'angry'
    show charlie at l2 with dissolve
    charlie "No!"
    eri "Not even a little teasing!? What kind of boarding school is this!?"
    eri "Here, I'll get us started. "
    scene bg white with dissolve
    blank "A blinding puff of white smoke suddenly fills the room. "
    scene scene20a with dissolve
    $ mc_clothes = 2
    charlie "...WHAT DID YOU DO!?"
    blank "Eri laughs delightedly. "
    eri "It's just some fun!!"
    blank "I stare between both of them, my jaw hanging open. "
    charlie "Sophie!"
    mc "R-r-right, sorry!!"
    blank "I clench my eyes shut. "
    mc "I didn't see anything!!"
    think "I saw everything. "
    eri "See~ Isn't this better~"
    eri "Everyone just needs to unknot their panties for a second!"
    blank "She slides behind me, hands on my shoulders suddenly as she starts to massage them. "
    mc "How do you like it, hm? "
    menu:
        "Give me my clothes back!!":
            eri "Are all people around here so dull or is it just you two...? "
            charlie "I'm getting out of here before she starts touching herself. "
        "That feels good...":

            $ demon_love += 1
            eri "See? Nothing like a little nudity to work out the stresses of life. "
            eri "You should join us~"
            blank "She croons at Charlie, who looks a little uncertain. "
            charlie "Are you really going along with this?"
            mc "Uhm."
            blank "She lifts her hands up. "
            charlie "Hey, whatever you get up to at night is totally your business. "
            charlie "But leave me out of it. "
            blank "She gives us both a look as she leaves. "

    scene bg black with dissolve
    scene dormroom_night with dissolve
    show eri at m2 with dissolve
    mc "Great..."
    think "Now I'm alone with her. "
    blank "Eri takes a running start toward my bed, but then spins on her heel to face me."
    $ eriface = 'flirty'
    $ eripose = '2'
    show eri at m1 with dissolve
    eri "Ahhh~ Why don’t you come join me, Sophie?"
    eri "We’ll have a good time~"
    eri "That other girl is obnoxious."
    mc "Charlie? She’s not really that bad, you’re just...not exactly her speed."
    $ eriface = 'sad'
    show eri at m2 with dissolve
    eri "What a pity."
    eri "I thought you humans would be more into sex, you know? You live such short lives."
    $ eripose = '3'
    show eri at m1 with dissolve
    eri "Especially your kind."
    mc "My kind?!"
    $ eriface = 'flirty'
    show eri at m2 with dissolve
    eri "Magi."
    eri "Always looking for some reason to get themselves killed, aren’t they?"
    mc "I changed my mind. You and Charlie are exactly the same."
    $ eriface = 'excited'
    show eri at m1 with dissolve
    eri "Oooh, let’s have a threesome then!!"
    mc "We’re not having a threesome."
    $ eriface = 'determined'
    show eri at m2 with dissolve
    eri "Ugh. Well, what am I supposed to do then?"
    mc "I don’t know. Sleep?"
    $ eriface = 'neutral'
    show eri at m1 with dissolve
    eri "Evil doesn’t sleep."
    mc "Uhh…?"
    $ eriface = 'sad'
    show eri at m2 with dissolve
    eri "...It was a joke. Never mind. But really, I don’t sleep."
    mc "Does that mean you have to watch me sleep?"
    blank "She snorts."
    eri "I don’t know if you’ve noticed, but I’m not actually glued to your side."
    $ eriface = 'flirty'
    show eri at m1 with dissolve
    eri "I can entertain myself for the night."
    eri "Maybe in your bathroom, trying to be quiet but unable to help myself…"
    $ eriface = 'excited'
    show eri at m2 with dissolve
    eri "Ugggnnn...Sophie, please...."
    blank "She moans loudly, falling back onto the bed with a giggle."
    think "It’s going to be a long year…"
    scene bg black with dissolve
    scene dormroom_night with dissolve
    play music "music/track08.ogg" fadeout 1 fadein 1
    blank "I convince Eri to leave my room for the night."
    blank "I think she went to spy on the other students and hope that some of their nights are more sweatier and heated than mine."
    blank "But if she stays around, they might just end up that way."
    blank "I know she’s a demon, but…"
    blank "Ugh, I shouldn’t find her attractive."
    show shira at m1 with dissolve
    shira "Good evening, Sophie."
    blank "Pity Eri didn’t stay for this. I think she would have liked it."
    if shira4:
        mc "Has Mage Warren or Master Mage Aureman mentioned anything to you yet?"
        shira "Nothing."
        show shira at m2 with dissolve
        shira "I think the Master Mage is more than willing to overlook the transgression, and Mage Warren will be convinced if he sees your talent."
        shira "Try not to worry too much. Now relax."
        scene scene9a with dissolve
        blank "Her hand slides over my skin as she puts me to sleep."
        blank "If she hadn’t, I don’t think I would have managed it myself."

    scene bg black with dissolve
    blank "…"
    think "Zzzzzzz…"
    eri "Psst."
    blank "…"
    eri "Psssssssssssssssssssssst!!"
    mc "You just spat on me…"
    mc "What do you want?"
    blank "I roll over irritably, glancing up into strangely coloured eyes."
    eri "Do you need me to help wake you up?"
    blank "A hand slides between my thighs."
    $ erioutfit = 'sexy'
    mc "WHAT ARE YOU DOING!?"
    blank "I flail backwards, slipping off the bed."
    scene dormroom_day with hpunch
    $ eriface = 'flirty'
    show eri at m2 with dissolve
    mc "And what are you wearing?"
    eri "This little thing? I thought you might like it."
    eri "No need to be dramatic. All you had to do was say no."
    mc "Will you just tell me why you woke me up!?"
    $ eriface = 'sad'
    $ eripose = '2'
    show eri at m1 with dissolve
    eri "......I'm bored. "
    $ eriface = 'flirty'
    show eri at m2 with dissolve
    eri "Play with me~"
    blank "She crawls off the bed too, and onto me with a gleam in her eyes. "
    blank "I squirm helplessly."
    mc "I have school!!"
    $ eriface = 'annoyed'
    $ eripose = '3'
    show eri at m1 with dissolve
    eri "It’s a Sunday. There’s no school on Sunday, even in the demon world."
    mc "...There are schools in the demon world?"
    $ eriface = 'happy'
    show eri at m2 with dissolve
    eri "No. Ergo, no schools on Sunday. Aha~"
    blank "It’s too early for this. My head is already starting to spin."
    mc "Whatever!! The point is, I have to train."
    mc "There’s a trial we’re trying to prepare for and we’re spending every day working up to it."
    $ eriface = 'determined'
    show eri at m1 with dissolve
    eri "Yeah, you mentioned that yesterday and I didn’t really care."
    eri "Oh, and oops!! I don’t care today, either."
    $ eriface = 'excited'
    show eri at m1 with dissolve
    eri "Play with me!"
    mc "Nooo, Eri. I have studying to do."
    $ eriface = 'sad'
    show eri at m2 with dissolve
    eri "Ughhh. How did I get summoned by the two most boring, prudish people on the planet?"
    blank "She follows me toward the bathroom, sliding between me and the doorway."
    $ eriface = 'flirty'
    show eri at m1 with dissolve
    eri "...It’s not like I haven’t figured it out, you know."
    mc "What are you talking about now?"
    $ eriface = 'happy'
    show eri at m2 with dissolve
    eri "Your little secret."
    mc "What?"
    think "How could she…?"
    think "She couldn’t. There’s no way."
    mc "You’re bluffing. And not well."
    mc "Can you move out of the way?"
    $ eriface = 'neutral'
    show eri at m1 with dissolve
    eri "Alright, alright."
    eri "Whatever you say, Shaun."
    hide eri with dissolve
    blank "I spin around, but she’s already vanished."
    scene bg black with dissolve
    scene classroom with dissolve
    $ charlieface = 'neutral'
    $ charliepose = '1'
    $ charlieoutfit = 'uniform'
    $ mc_clothes = 8
    $ erioutfit = 'demon'
    show charlie at l1 with dissolve
    blank "When I walk in, Charlie’s feet are hovering a couple inches off the ground."
    mc "Practicing levitation again?"
    show charlie at l2 with dissolve
    charlie "Magi Shira says it’s good for control. Plus it’s one of the things I’m actually better at than you."
    charlie "It comes with a certain sense of pride."
    mc "Pft. Sure."
    mc "Um...have you seen Eri this morning?"
    mc "She uh, ran off while I was getting ready..."
    $ charlieface = 'mad'
    show charlie at l1 with dissolve
    charlie "Keeping track of your demon wife is your problem, not mine."
    mc "She’s not my demon wife!"
    $ eriface = 'flirty'
    show eri at r2 with dissolve
    eri "I’m not!?"
    $ eriface = 'mad'
    show eri at r1 with dissolve
    eri "Now I’m just insulted."
    blank "Charlie sighs."
    $ charlieface = 'sad'
    show charlie at l2 with dissolve
    charlie "Speak of the devil…"
    think "She better not say anything to Charlie."
    blank "I try to give her a stern glare, but she just smiles at me with those sharp little teeth."
    $ eriface = 'flirty'
    show eri at r2 with dissolve
    eri "You look tense, Sophie, darling."
    eri "How about a deep massage to work some of that out of your system?"
    mc "I’m here to train. Can you at least let us do that in peace?"
    blank "I fall in beside Charlie, starting to focus my magic on levitating, too."
    blank "The fact that I’ve never actually done this successfully only makes me more determined."
    blank "I go through the steps again, Charlie trying to offer her best advice."
    blank "I even try jumping to get a head start, but my feet return stubbornly to the ground. "
    $ eriface = 'sad'
    show eri at r1 with dissolve
    eri "No, no, no!!"
    eri "You’re doing it all wrong."
    $ eriface = 'annoyed'
    $ eripose = '1'
    show eri at r2 with dissolve
    eri "You’re trying to drag yourself up, like your magic is a string you’re tying yourself to."
    eri "You gotta push upward from the centre."
    blank "She pokes me hard in the chest, which doesn’t help my concentration."
    $ eriface = 'sad'
    show eri at r1 with dissolve
    eri "Come on."
    eri "Like you’re filling your boobs with helium. Only it’s magic instead."
    think "This can’t be serious advice..."
    blank "Despite the ridiculous instructions, I try it."
    blank "Slowly, bit by bit, I feel the magic align through my body, balanced from head to toe."
    blank "It feels right, suddenly. Possible."
    blank "My feet slowly start to leave the ground."
    mc "I’m doing it!"
    mc "Yess!!"
    blank "In a wave of excitement, I kick off from the ground a little more, triumphant."
    mc "Look!"
    $ charlieface = 'blush'
    show charlie at l1 with dissolve
    charlie "Uhm, that’s great and all, but..."
    scene scene21a with dissolve
    charlie "You realize you’re wearing a skirt, right?"
    mc "...DON’T LOOK!!"
    eri "Don’t move so fast! You’ve gotta take it slow and sensual."
    eri "Pull up your top now, just a bit. Let’s see some under-boob."
    think "Why the under-boob? That's like the least exciting part of the boob. "
    charlie "Are you actually capable of thinking of anything else?"
    mc "Thi-this isn’t what I meant to show off!!"
    mc "You're both perverts, turn around!!"
    blank "I pinwheel my arms like it’ll keep me afloat as I panic."
    scene bg black with dissolve
    scene classroom with dissolve
    blank "…" with vpunch
    mc "O-ow."
    think "So much for control."
    show charlie at l1 with dissolve
    show eri at r1 with dissolve
    if friends:
        charlie "Sophie!?"
        show charlie at l2 with dissolve
        charlie "Are you okay??"
        charlie "Did you hit your head?"
        mc "N-no...but I think I broke my butt."
        blank "She snorts."
        $ charlieface = 'happy'
        show charlie at l1 with dissolve
        charlie "Well, as long as that’s all you broke."
        $ eriface = 'neutral'
        show eri at r2 with dissolve
        eri "Why don’t you kiss it and make it better?"
        blank "Charlie’s cheeks heat up as she glowers at Eri, but then she glances down at me."

    blank "Two different sets of hands reach down to help me up and I take them both."
    $ eriface = 'neutral'
    $ charlieface = 'neutral'
    show charlie at l1 with dissolve
    show eri at r2 with dissolve
    mc "Thanks…"
    mc "How did you know how to do that, Eri?"
    blank "She shrugs."
    $ eripose = '1'
    show eri at r2 with dissolve
    eri "Instinct, I guess."
    eri "Demons use magic, too, you know. We just don’t have to learn it."
    $ charlieface = 'annoyed'
    show charlie at l2 with dissolve
    charlie "It’s not like it’s the same thing."
    $ charlieface = 'sad'
    show charlie at l2 with dissolve
    charlie "Demons use dark magic. All the better to destroy things and hurt people with."
    $ eriface = 'sad'
    show eri at r1 with dissolve
    eri "Is that what they teach you?"
    blank "She scoffs."
    $ eriface = 'annoyed'
    $ eripose = '2'
    show eri at r2 with dissolve
    eri "There’s no difference between what you do and what I do, except that I’m better at it."
    blank "I immediately step between them, because I know where the line is and Eri just pole vaulted it over."
    mc "Alright, enough."
    mc "Eri, you did help me out."
    mc "Do you think you could help us train for our trial?"
    $ charlieface = 'angry'
    $ charliepose = '2'
    show charlie at l1 with dissolve
    charlie "What!?"
    $ eriface = 'happy'
    $ eripose = '3'
    show eri at r1 with dissolve
    eri "Oooh, I don’t know. You haven’t been very nice."
    eri "What’s in it for me?"
    mc "Uhm."
    blank "I glance at Charlie for help, but she doesn't look very keen on the idea."
    mc "I’ll…"
    menu:
        "Let you make out with me.":
            $ demon_love += 1
            $ eriface = 'excited'
            show eri at r2 with dissolve
            eri "I’m in!"
            $ charlieface = 'mad'
            show charlie at l2 with dissolve
            charlie "You’ll what!?"
            mc "...It’s just a bit of tongue action. What could it hurt?"
            show charlie at l1 with dissolve
            charlie "Isn’t that what we said when we summoned her in the first place?"
            charlie "She’s a demon. Soul-sucking is probably a hobby."
            $ eriface = 'happy'
            show eri at r1 with dissolve
            eri "Aha, now you’re just embellishing my talents. Please, I’m too modest for such flattery~"
            blank "Charlie seethes."
            show charlie at l2 with dissolve
            charlie "You and modest are antonyms."
            $ eriface = 'neutral'
            show eri at r2 with dissolve
            eri "Sophie already made the arrangement, so a deal’s a deal."
            eri "Consider me one of your new teachers. I’m sure you’ll be an eager and willing pupil…"
            blank "She gives me a sly look."
            $ eripose = '1'
            show eri at r1 with dissolve
            eri "I’ll be waiting to collect my reward."
        "Stop trying to send you home.":

            charlie "So you’re just going to keep her around forever. Like a pet."
            mc "You can leave whenever you want, can’t you, Eri? I just don’t know how to make you leave."
            $ eriface = 'determined'
            show eri at r2 with dissolve
            eri "That’s right."
            eri "This is my impromptu vacation, so good luck getting rid of me."
            $ charlieface = 'mad'
            show charlie at l2 with dissolve
            charlie "Ugh."
            charlie "This is the worst idea."
            mc "Trust me, if there is such a thing as the “worst idea,” I’ve probably already come up with it and tried it myself."
            $ eripose = '2'
            show eri at r1 with dissolve
            eri "I’m not all that fussed about it, but I guess training you would give me something to do."
            blank "She shrugs indifferently."
            $ eriface = 'neutral'
            show eri at r2 with dissolve
            eri "Aren’t you glad you have two hot teachers now?"
            eri "I don’t know how you kids live with all this roiling sexual tension."
            $ eripose = '1'
            show eri at r1 with dissolve
            eri "I think your first lesson should be on how to unwind and explore your sexuality a little bit…"
            blank "Charlie and I shout in unison."
            mc "Not that kind of teacher!!"

    scene bg black with dissolve
    scene dormroom_night with dissolve
    blank "After a day of trying to get Eri to focus on something other than sex, Charlie and I are both exhausted."
    blank "It’s a good excuse to break away from Charlie for the time being. "
    blank "I have some questions for the demon girl trailing after me."
    show eri at m2 with dissolve
    mc "So. Explain."
    eri "Well, when two people are both reasonably attracted to each other, sometimes they-"
    mc "About this morning! How did you know my name?"
    $ eriface = 'flirty'
    $ eripose = '2'
    show eri at m1 with dissolve
    eri "Oh~ You think I don’t know a manly stud when I see one?"
    blank "Just the words make my skin crawl uncomfortably now."
    eri "I’m teasing. But the magic still lingers on you, you know."
    $ eriface = 'determined'
    show eri at m2 with dissolve
    eri "Like uhm. Residual energy, I think you’d call it."
    mc "And that residual energy just happened to spell out my name?"
    $ eripose = '3'
    show eri at m1 with dissolve
    eri "Nah. I found that in your bag, on a letter from someone."
    mc "You went through my things!?"
    blank "She shrugs."
    $ eriface = 'neutral'
    show eri at m2 with dissolve
    eri "It’s not my fault you’re a heavy sleeper, and really, do you expect a demon to be the most well-behaved person you’ve ever met?"
    blank "With a sigh, I slump down onto my bed."
    mc "Whatever. I’m too tired to deal with you right now, but don’t tell anyone what you found out."
    mc "And when Magi Shira comes in I want you to leave. I can't focus with you around. "
    blank "She holds up her hands in defence."
    $ eripose = '1'
    show eri at m1 with dissolve
    eri "Alright, alright."
    eri "No need to get testy; your secret’s safe with me. Cross my horny little heart."
    blank "A knock on the door interrupts my groan."
    show eri at m2 with dissolve
    eri "Looks like this is my exit. See you~"
    play music "music/track04.ogg" fadeout 1 fadein 1
    hide eri with dissolve
    if shira4 == True and shira5 == True:
        show shira at m1 with dissolve
        shira "Sophie.."
        blank "With Eri’s exit, she seems to drag all the joy out of the room with her."
        jump shira34
    else:

        think "I can’t believe Eri figured it out.."
        think "I should have been more cautious."
        blank "For a moment, I almost want to turn Magi Shira away tonight. I feel like there’s not enough time to sort through everything in my head."
        blank "But maybe it’s better to lock it all away completely…"
        jump endings1


label shira34:
    blank "Shira’s expression makes me do a double-take, to make sure it really is her."
    mc "Magi Shira...is something wrong?"
    blank "She looks so uncharacteristically crestfallen."
    blank "That stern, no-nonsense demeanour is gone, and even the gentler, kinder side of her personality hadn’t prepared me for this."
    $ shiraface = 'sad'
    $ shirapose = '1'
    show shira at m2 with dissolve
    shira "...Is it that obvious?"
    mc "I guess so… You look upset."
    blank "She sighs, and without invitation sits down on the edge of my bed."
    $ shirapose = '3'
    show shira at m1 with dissolve
    shira "I’ve been led to believe that Mage Warren might take action against me, as well."
    mc "What!? He can’t do that!!"
    blank "She holds up a hand to silence my outrage."
    $ shirapose = '1'
    show shira at m2 with dissolve
    shira "If there’s a formal investigation, it would have happened anyway. I would have to be on leave while they sort out the particulars of the case."
    shira "But…"
    $ shiraface = 'neutral'
    show shira at m1 with dissolve
    shira "The Master Mage has made certain adjustments that makes me think my position here at the Academy is no longer secure."
    shira "He’s even taken on an apprentice of his own."
    mc "I don’t understand what that means…"
    blank "She smiles thinly."
    show shira at m2 with dissolve
    shira "It means he’s training my replacement."
    blank "My heart sinks."
    mc "M-Magi Shira, I…"
    menu:
        "What if I turn myself in?":
            $ shiraface = 'sad'
            show shira at m1 with dissolve
            shira "That won’t help. It would only be an affirmation of both our guilt."
            shira "We can’t do anything but continue on our present course, and hope for the best."
            think "Why did I let this happen…?"
            think "If I had just come clean from the beginning...if I had just been honest about my abilities from the start, I…"
            think "I just never imagined anyone else getting wrapped up in what I’d done."
            blank "Shira lifts a hand to touch my cheek, startling me from my thoughts."
            $ shirapose = '2'
            show shira at m2 with dissolve
            shira "Don’t be upset on my behalf."
            shira "I just hope I can fulfil the promises I made to you."
            blank "My heart clenches."
            think "Why?"
            think "Why does she care so much about me?"
            mc "I’ll train harder than ever."
            mc "I promise."
            blank "She smiles in return, even if the happiness doesn’t reach her eyes."
            $ shiraface = 'happy'
            $ shirapose = '1'
            show shira at m1 with dissolve
            shira "I know you will."
            blank "She gently helps me strip off my clothes, the action so familiar and yet somehow so intimate this time."
            blank "I blush beneath her gaze as she runs her hands slowly along my skin."
            blank "And now I wish I could put her to sleep in return, just for the chance to touch her like that."
            blank "She gazes down at me through lidded eyes."
            $ shiraface = 'determined'
            show shira at m2 with dissolve
            shira "It’s strange how close two people get when they share a common secret, isn’t it?"
            blank "I open my mouth to reply, but my eyes close instead."
            blank "Darkness settles over me faster than it ever has before."
            jump endings1
        "I won’t let them do that to you!":

            mc "They can’t!"
            mc "We’ll find a way to stop it somehow, I promise."
            think "Charlie. Eri."
            think "Master Mage Aureman."
            think "Something has to give. There has to be a way."
            blank "She smiles sadly, and her hand brushes against my cheek even as my mind races through each option."
            $ shirapose = '2'
            $ shiraface = 'sad'
            show shira at m1 with dissolve
            shira "I wish it was as easy as you make it sound."
            blank "Without meaning to, I slump down against her shoulder a bit."
            mc "It doesn’t need to be easy. It just needs to be possible…"
            blank "She sighs softly, a sound I take for agreement."
            show shira at m2 with dissolve
            shira "What if I told you there might be a way?"
            blank "I glance up into her face."
            shira "But I would need your complete trust and your confidence."
            $ shirapose = '3'
            $ shiraface = 'determined'
            show shira at m1 with dissolve
            shira "Can I get those from you?"
            blank "I nod quietly."
            mc "You’ve done so much for me. You already have them."
            blank "She ruffles my hair affectionately, murmuring softly."
            $ shiraface = 'happy'
            show shira at m2 with dissolve
            shira "Good girl."
            shira "Come with me now."
            mc "Where are we going?"
            show shira at m1 with dissolve
            shira "To fix this."

    scene bg black with dissolve
    scene hallway with dissolve
    $ mc_clothes = 6
    think "I trail after Shira, a bundle of nerves and confusion as she leads me through the school."
    think "I wish I knew what we’re about to do or how we’re going to do it....."
    think "It’s not like Shira, to do something without first explaining it. Or maybe I’m just used to her being a teacher and not an accomplice…"
    think "Who’s in control anymore?"
    think "It isn’t me. I don’t think it’s really been me for a long time."
    $ shiraface = 'determined'
    $ shirapose = '3'
    show shira at m2 with dissolve
    shira "His office is just down this hallway."
    mc "What do you need me to do?"
    blank "She presses a finger to her lips, dropping her voice to a low whisper."
    $ shirapose = '1'
    show shira at m1 with dissolve
    shira "I’ll show you."
    blank "She beckons me close."
    shira "You may have caught on, but I specialize in magic manipulation."
    mc "Like the ritual we do each night?"
    blank "She nods."
    show shira at m2 with dissolve
    shira "Yes, that’s a form of it. With the right power, I can even put a dampening field around someone else’s magic."
    shira "I can render it useless."
    $ shirapose = '3'
    show shira at m1 with dissolve
    shira "That’s what we’re going to do, just long enough for me to get in there and put Mage Warren to sleep."
    think "We're attacking Mage Warren...?"
    mc "B-But why are we putting him to sleep?"
    $ shiraface = 'neutral'
    show shira at m2 with dissolve
    shira "So he won’t fight back."
    blank "Doubt crawls in my stomach, but she puts a hand on my shoulder."
    $ shirapose = '1'
    show shira at m1 with dissolve
    shira "If we were going to kill him, would we be putting him to sleep first?"
    shira "What I’m going to do takes time, and it’s better if he’s not fighting me."
    shira "I’m going to change his memories."
    $ shirapose = '2'
    show shira at m2 with dissolve
    shira "But I can’t control him by myself. I’ll need your help."
    think "This is insane."
    blank "I stare at her in disbelief, trying to get a grip on what exactly we’re doing."
    mc "I thought only sorcerers would have access to magic like that…"
    $ shirapose = '1'
    show shira at m1 with dissolve
    shira "Once you study magic for long enough, you come across things by accident."
    shira "The knowledge itself isn’t illegal. Using it...well, I suppose that is."
    show shira at m2 with dissolve
    shira "But that’s a crime we can both be guilty of."
    blank "Her hands clasp around mine suddenly, her eyes searching my face."
    shira "Do you want to do this?"
    show shira at m1 with dissolve
    if shira2 == True and shira4 == True and shira5 == True:
        $ shira_endingopen = True
    shira "I need an answer."
    menu:
        "I want to do it." if shira_endingopen == True and persistent.completed == True:
            blank "A strange thrill creeps through me at the question, a sudden rush."
            blank "It’s the same feeling I felt when I broke into the library that night, finding that book…"
            blank "That thrill of discovery, of knowing power was just at the tips of my fingers if only I was brave enough to grasp it."
            blank "I nod."
            mc "I want to."
            blank "Her expression warms suddenly, her hand squeezing mine."
            $ shiraface = 'shy'
            show shira at m2 with dissolve
            shira "I knew I could count on you. You and I, we’re just alike."
            shira "Come here."
            blank "Together, we kneel down in front of Mage Warren’s office, just outside the door."
            mc "What if someone comes along and sees us?"
            $ shiraface = 'happy'
            show shira at m1 with dissolve
            shira "He’s always the last to leave. He’ll still be in there, working or something similar, but we have time."
            shira "Now follow my lead. Just like we do in class, alright?"
            mc "Got it."
            blank "If I was actually half a certain as I sounded, maybe we’d have a chance between the two of us."
            $ shiraface = 'determined'
            $ shirapose = '3'
            show shira at m2 with dissolve
            shira "Come on. This way."
            blank "We need to make a dampening field with our magic, a cage that’ll reign in his powers."
            shira "Between the two of us I think that’s possible. I can do the ritual, I just need your energy."
            blank "Shira starts the ritual as I stand by, staring anxiously at the door."
            think "What if he knows?"
            think "What if he comes barrelling out, ready to fight?"
            mc "How long is this going to take?"
            blank "She hushes me sharply, concentrating."
            think "Ugh…"
            think "Come on…"
            blank "The feeling slides through me, warm and strange, a deep tugging that pulls at something unnameable inside me."
            blank "I shudder against the feeling."
            $ shiraface = 'determined'
            show shira at m1 with dissolve
            shira "Don’t fight it."
            blank "A muffled noise comes from inside the room."
            shira "Now!"
            jump shiraend
        "I can't do it.":

            think "I…"
            mc "I can’t do this."
            mc "I’m sorry--"
            blank "I break away from her suddenly, my feet pounding through the hallway as I run back toward my room."
            scene bg black with dissolve
            scene dormroom_night with dissolve
            blank "My breath rushes in frightened gasps, legs wobbling uncertainly beneath me."
            think "This was a mistake."
            think "It was all a mistake."
            think "I shouldn’t have come here."
            think "I shouldn’t have tried that spell."
            think "Maybe I shouldn’t even be running away right now, my courage buckling...but I am."
            think "...I did everything wrong."
            scene bg black with dissolve
            blank "I stay in my room, but I don’t sleep."
            blank "The darkness crashes in on me like a wave, smothering me."
            blank "Waiting for someone to knock on the door and take me away to my fate."
            blank "I spend the night just trying to breathe, and when the sun comes up outside the window, it’s almost a relief."
            scene bg black with dissolve
            scene classroom with dissolve
            blank "School resumes."
            blank "No one came for me."
            blank "Normalcy (or as close as I ever get to it) feels ridiculous, when I’m constantly looking over my shoulder."
            blank "But Charlie chats away about the latest rumours, and Eri has settled between us like a problematic child we have joint custody over."
            blank "It’s strange, the way it all goes back to the way it was before."
            blank "Shira is stricter than ever, though."
            blank "No more kind words or knowing glances. She regards me with a firm disdain that burns every time I think about it."
            blank "She trains us harder than ever, too."
            blank "Even with the robes, I get a new limited edition scrape or burn every day, working myself to the bone."
            blank "I’m cut off from knowing what’s happening inside the school, or if Shira is going to lose her job."
            blank "When she comes by at night, she barely speaks, and I think she puts me to sleep faster than before."
            think "I must have really hurt her…"
            blank "But the trial looms impossibly close, and brings with it its own set of anxieties."
            blank "I already said I would do it, and I plan to."
            blank "I want to prove myself-- if to no one else, than at least to me."
            blank "I want to see what I’m made of."
            jump endings1


label shiraend:
    scene bg black with dissolve
    scene office with dissolve
    play music "music/goodend.ogg" fadeout 1 fadein 1
    $ shiraface = 'neutral'
    $ shirapose = '1'
    show shira at r2 with dissolve
    show warren at m1 with dissolve
    warren "You…"
    shira "Shhh. No need to speak."
    shira "This doesn’t have to be painful, Warren."
    blank "My body feels strange, like it’s on fire from the inside."
    blank "She strides up to him, her hand brushing against his temple as she grins."
    shira "All you have to do is go to sleep."
    $ shiraface = 'determined'
    $ shirapose = '2'
    show shira at r1 with dissolve
    shira "Isn’t that right, Sophie?"
    warren "I knew you were up to something--I knew--"
    blank "He struggles against her touch, and begins to chant a spell."
    scene scene22d with dissolve
    blank "As his shield appears, Shira lets lose a powerful blast of energy, shattering the still forming bubble."
    blank "My skin tingles as the strike is let loose."
    blank "He hits the floor with a thud, the light of his eyes is dimmed."
    warren "What are you..."
    shira "Shhhh."
    blank "Her hand slides down his cheek."
    blank "His eyes start to droop."
    warren "Tch...where did you..get this power...?"
    shira "Tsk tsk. No questions."
    scene scene22a with dissolve
    blank "He falls backwards onto the ground, with a heavy thud, and Magi Shira practically pounces on him."
    blank "The fire in my chest suddenly releases, my own eyes heavy. I nearly follow suit and collapse, too."
    blank "I manage to slump against his desk and keep myself upright."
    mc "You can alter his memory now?"
    shira "…"
    mc "Magi Shira?"
    shira "I’m glad you let me help you, Sophie."
    shira "A symbiotic relationship is truly a beautiful thing, isn’t it?"
    shira "I told you I would protect you and I have. I hope you won’t hate me for doing that."
    mc "...W-what are you talking about?"
    mc "What are you doing to him?"
    scene scene22b with dissolve
    shira "The same thing I’ve done to you and Charlie every night-- taking his power."
    shira "Didn’t you ever wonder why it was so exhausting? Why you had to fall asleep afterwards?"
    shira "And with that illegal ritual you performed, you had extraordinary amounts of power all for the taking. You never even noticed a difference, did you?"
    mc "But…"
    shira "Don’t worry, Sophie. I was never out to harm you."
    shira "You and I...we’re like-minded."
    shira "We don’t let anything stand in the way of what we want."
    shira "If I was the one trying to expel you, then you’d be here, trying to circumvent me, wouldn’t you?"
    shira "I don’t hold it against you. If anything I admire it."
    blank "She glances over her shoulder toward me. Mage Warren’s face has gone pale and slack."
    blank "Her eyes flutter."
    shira "Almost there…"
    blank "My stomach twists."
    mc "...What’ll happen to him?"
    shira "The same thing that happens to all things, when you take away what gives them power."
    shira "He’ll die."
    mc "Y-you’re capable of that?"
    blank "I don’t mean magically. Morally. I’m in a wordless awe."
    shira "Remember when I said that sometimes we have to pretend to be one thing, when really we’re something else?"
    shira "It’s all a part of getting what you want."
    shira "I know how to play the game, Sophie. And so do you."
    think "She’s going to kill him. ...And one of my problems will be gone."
    blank "The thought manifests before I can stop it, watching with transfixed eyes as the subtle twitches of Mage Warren’s face fall still."
    scene scene22c with dissolve
    blank "Shira lets out a low, shaky breath, the magic around her fading as her new power settles."
    blank "And he's gone. "
    blank "She stands to face me, but I can hardly pull my eyes away from Mage Warren. "
    think "She killed him...she really killed him..."
    blank "I lift my eyes to her, wanting to be horrified. I guess I am, but...with myself. "
    scene bg black with dissolve
    scene office with dissolve
    $ shiraface = 'blush'
    $ shirapose = '2'
    show shira at m2 with dissolve
    shira "I knew you would stay."
    shira "I can always count on you."
    blank "Her hand brushes my cheek again, though I feel numb all over."
    $ shirapose = '1'
    show shira at m1 with dissolve
    shira "It’ll take some getting used to, all this."
    mc "B-But...they’ll know. The Master Mage--"
    $ shiraface = 'happy'
    show shira at m2 with dissolve
    shira "Is our next target, now that I have the power to defeat him."
    shira "How about it, Sophie?"
    $ shirapose = '3'
    show shira at m1 with dissolve
    shira "Do you want to be a sorcerer?"
    shira "No Academy, no trial. Just us, looking out for each other’s interests."
    $ shirapose = '1'
    show shira at m2 with dissolve
    shira "It’s what we were made to do."
    shira "I have only one stipulation."
    mc "…?"
    $ shiraface = 'blush'
    show shira at m1 with dissolve
    shira "I get to keep you just like this."
    shira "Her fingers catch beneath my chin and draw me in."
    scene scene23a with dissolve
    blank "The lingering kiss, is all I want and I enjoy it deeply."
    blank "With the same tactics, I help her again."
    scene scene24a with dissolve
    blank "Before I know it we are in another battle."
    blank "We subdue the Master Mage."
    blank "He was already asleep when we found him, but he put up far more of a fight than Mage Warren."
    blank "Beneath that wrinkled, good-mannered face, there was a warrior in him."
    blank "It didn't save him."
    blank "With Mage Warren’s power, Shira outmatches him easily, and he becomes her--our--second victim."
    blank "Eri stumbled upon what we’ve done, but she just regards me warily."
    blank "It’s not her business. It’s not even her world."
    blank "She doesn’t care so much about the lives of mortals."
    scene bg black with dissolve
    blank "Together, Magi Shira and I construct an alibi. We were together, practicing, at the time of the attack."
    blank "Shira is the only thing that keeps me calm during the interrogations."
    blank "And then a stroke of luck."
    blank "In the investigation that follows, they discover demonic energy lingering in the school."
    blank "It serves as a good enough explanation for them, as the school is briefly put on lockdown to deal with the situation."
    blank "But out of the chaos and confusion, a scene of mourning and suspicion, Magi Shira becomes the new Master."
    blank "One small rung on the ladder we’re going to climb together."
    blank "And every night, with the same ritual, I help her get a little closer to her goal."
    scene endingimage3 with dissolve
    $ achievement.grant("blackmagician")
    blank "Ending #3 - The Black Magician"
    jump credits


label endings1:
    scene bg black with dissolve
    scene dininghall with dissolve
    play music "music/track09.ogg" fadeout 1 fadein 1
    $ mc_clothes = 6
    $ charlieoutfit = 'robes'
    $ erioutfit = 'demon'
    $ charlieface = 'neutral'
    $ charliepose = '1'
    $ eriface = 'neutral'
    $ eripose = '1'
    show charlie at l1 with dissolve
    show eri at r2 with dissolve
    charlie "I can’t believe the trial's almost here."
    mc "I’m not ready. We’re going to make idiots out of ourselves, just watch..."
    blank "Eri sniffs."
    $ eriface = 'sad'
    show eri at r1 with dissolve
    eri "You train all day. If you’re not ready now, you’re never going to be."
    blank "Charlie launches a piece of food in her direction, apparently forgetting we’re the only ones who can see her."
    mc "Knock it off you two."
    mc "I’m trying to have an anxiety attack in peace."
    $ eriface = 'annoyed'
    show eri at r2 with dissolve
    eri "Seriously? It’s been weeks."
    eri "And as someone who doesn’t actually need to go to school, this has been the most monotonous and chaste weeks of my life."
    eri "I really thought one of you would give in to me by now."
    $ charlieface = 'mad'
    show charlie at l2 with dissolve
    charlie "Not happening."
    $ eriface = 'flirty'
    $ eripose = '2'
    show eri at r1 with dissolve
    eri "I really am a catch, even as succubae go."
    eri "Why don’t either of you believe me?"
    blank "I completely believe her, but I don’t voice as much."
    blank "If anything, I think we’ve become desensitized. I don’t even react when she brushes her foot against my leg teasingly."
    $ charliepose = '2'
    $ charlieface = 'neutral'
    show charlie at l1 with dissolve
    charlie "I say we go through the drills again. Basic assault and defence. Some element manipulation."
    blank "We’ve come pretty far from where we started."
    blank "Blocking spells without a full shield. Attacking within mere seconds."
    blank "It’s becoming second-nature to me, but it doesn’t feel very advanced. I know I’m still in the rudimentary concepts of magic."
    $ eriface = 'excited'
    $ eripose = '3'
    show eri at r2 with dissolve
    eri "Sophie, your girlfriend is talking to you."
    $ charliepose = '2'
    $ charlieface = 'annoyed'
    show charlie at l2 with dissolve
    charlie "I'm not her girlfriend!"
    $ eripose = '1'
    show eri at r1 with dissolve
    eri "Not for lack of wanting, I think. "
    blank "Charlie goes pale, my attention finally sliding to the two of them. "
    think "Um...?"
    $ charlieface = 'neutral'
    show charlie at l1 with dissolve
    charlie "Sophie, I’m curious...do you know if demons are immune to stab wounds?"
    eri "I was just trying to be helpful."
    mc "Okay, enough."
    blank "My appetite completely gone, I toss my food in the closest bin and head out."
    $ charlieface = 'sad'
    show charlie at l2 with dissolve
    charlie "Wait!"
    charlie "Okay. You’re stressed, I get it. We’re all stressed."
    $ eriface = 'neutral'
    show eri at r2 with dissolve
    eri "I’m not stressed. I’m patented stress relief. See?"
    blank "She squeezes her chest."
    $ eriface = 'determined'
    show eri at r1 with dissolve
    eri "Stress relief balls!"
    blank "Charlie presses on like Eri didn’t say anything at all."
    charlie "Let’s go work some of that out in training, alright?"
    $ eriface = 'sad'
    show eri at r2 with dissolve
    eri "But I’m tiiiiiired of training."
    charlie "No one asked you!"
    scene bg black with dissolve
    scene arena with dissolve
    show charlie flip at m1 with dissolve
    blank "Charlie takes me by the arm and drags me toward the arena."
    blank "We just did this for seven hours earlier, and eating didn’t exactly put me in a more magical mood."
    mc "Well, what do you want to do?"
    $ charlieface = 'blush'
    show charlie flip at m2 with dissolve
    charlie "If you’re going to sound so defeated, I don’t want to do anything at all."
    blank "I shake my head."
    mc "I always get like this a few days before something big happens."
    mc "This is just the defeated stage. Give it a few another day and I’ll hit the manic stage and be trying something ridiculous."
    $ charlieface = 'neutral'
    show charlie flip at m1 with dissolve
    charlie "Well, we’re going to get through that."
    charlie "Aren’t you the one always pushing through with stubborn determination?"
    charlie "Find some of that sitting around and let’s go."
    blank "She takes a few strides from me, standing opposite me as Eri stands in the middle."
    blank "It’s a familiar set-up, our private demon friend playing ref while Charlie and I practice spells on each other."
    blank "I take a breath, trying to get into the mind-set and push through another wave of exhaustion. "
    scene scene25a with dissolve
    blank "Charlie launches a barrage of attacks immediately, but they ping uselessly off my summoned shields."
    blank "I spin the shields into a frontal attack, sending the wall of magic pushing toward Charlie."
    blank "She bolts out of the way and uses my temporary weakness to her advantage."
    blank "Firing black shards of energy at me, bypassing my shield completely."
    menu:
        "Avoid Them.":
            scene scene25b with dissolve
            blank "I drop down beneath it at the last second."
            blank "I spin back around, launching another series of attacks."
            blank "Charlie counters them in kind, with attacks of her own."
        "Return Fire.":

            $ demon_love += 1
            scene scene25c with dissolve
            blank "I focus what little energy I have into a beam of golden light."
            blank "But several slithers still make it through my onslaught"
            blank "Hitting my sides, sending me stumbling as my skin burns."
            think "Nnng…"
            scene scene25d with dissolve
            blank "I manage to keep my balance though and continue the onslaught of golden light, overcoming Charlie's power."

    blank "Frustration growing, my teeth clench hard."
    think "I have to be better than this. I have to."
    scene scene25e with dissolve
    blank "I put everything I have into it."
    blank "My magic becomes a single beam, flickering gold, illuminating Eri’s nervous expression."
    blank "It happens quick."
    blank "Charlie’s spell falters as she loses control, her assault breaking."
    blank "The full force of my magic catches her in the chest and sends her spinning."
    scene bg black with dissolve
    scene arena with dissolve
    $ eripose = '3'
    $ eriface = 'flirty'
    show eri at m2 with dissolve
    eri "We have a winner!!"
    blank "An eruption of glitter briefly blinds me, courtesy of Eri as she rains it over me."
    eri "Congrats, Sophie. I knew you had it in you. How about a victory romp?"
    mc "I’m already going to have to take a bath for hours to get all this off me…"
    show eri at m1 with dissolve
    eri "Shower sex is always an option~"
    mc "Will you knock it off?"
    blank "Only then do I realize I’m not being yelled at. No one’s in my face, demanding a rematch."
    blank "Charlie hasn’t moved from where she landed."
    mc "...Charlie?"
    blank "Eri and I both stand immobilized for a second, as I process what happened."
    mc "Charlie!!"
    scene scene12b with dissolve
    blank "I run over to her, Eri trailing after me."
    blank "I slip my hand beneath her head to ease her up, but it comes away bloody."
    think "Oh no."
    think "Oh no, no, no--"
    blank "Her eyes roll as she tries to open them, mouth moving."
    charlie "Sophie--"
    mc "Hang on. Don’t move, okay?"
    mc "Just...just stay there, I’ll get Magi Shira."
    mc "It’ll be okay."
    blank "I shout back at Eri as I bolt out of the room."
    mc "Stay with her!!"
    scene bg black with dissolve
    scene hallway with dissolve
    blank "It’s surreal, watching them take Charlie to the medical wing."
    blank "Magi Shira did what she could to patch up Charlie on the spot, but she has been asleep ever since."
    $ shiraface = 'neutral'
    $ shirapose = '3'
    show shira at r2 with dissolve
    shira "Go back to your room, Sophie."
    shira "I’ll let you know if anything changes."
    hide shira with dissolve
    blank "With a brisk pace, she follows the medics back out of the classroom."
    $ eriface = 'sad'
    show eri at m2 with dissolve
    eri "It’s not really your fault, you know."
    mc "Sorry, Eri, I just...I can’t hear that right now."
    blank "She nods, and trails after me quietly as we head toward my room."
    scene bg black with dissolve
    scene dormroom_night with dissolve
    play music "music/track01.ogg" fadeout 1 fadein 1
    blank "I stare at the place between my feet, watching as the little sparkles catch the light."
    blank "I keep replaying that moment in my head, over and over."
    think "All I’d wanted to do was win."
    think "It was the only thing I could think about, the only thing I could see."
    think "It clouded every sense. It always does this."
    blank "I run my hands through my hair, another wave of regret washing over me."
    think "Why am I like this?"
    think "Why am I always like this?"
    show eri at m1 with dissolve
    blank "Eri sits down on the bed beside me, and nuzzles against my shoulder."
    blank "For the first time, it feels completely chaste."
    mc "I did this to her."
    show eri at m2 with dissolve
    eri "Yeah. You did."
    eri "But…"
    mc "No buts. I did it. That’s all there is to it."
    show eri at m1 with dissolve
    eri "Fine. That’s all there is."
    eri "So what are you going to do now?"
    show eri at m2 with dissolve
    eri "Are you going to stay in here and mope or are you going to do something about it?"
    menu:
        "There’s nothing I can do…":
            show eri at m1 with dissolve
            eri "How defeatist."
            blank "We sit in silence for a few moments more, her words slowly nagging at me."
            think "Charlie’s up there all by herself. What if she wakes up?"
            think "What if she’s mad at me, and I can’t even apologize?"
            think "..."
            think "Oh, fine."
            blank "Angrily, I push myself off the bed, ignoring the feeling of Eri’s smirk following me."
        "Like what?":

            $ charlie_love += 1
            $ demon_love += 1
            show eri at m1 with dissolve
            eri "Like go to her!"
            mc "I’m not supposed to…"
            think "But when has that ever stopped me before?"
            mc "Even if I did, I...what could I do for her? I’m the reason she’s in there in the first place."
            show eri at m2 with dissolve
            eri "I’m not the best person you could go to for sentimental advice, but even I know an apology in person goes a long way."
            eri "It’s like looking at boobs."
            show eri at m1 with dissolve
            eri "A picture is great and all, but there’s just something special about seeing them in person."
            mc "You’re right..."
            eri "I know. I’m a boob expert."
            mc "Not about that! About the apology, about the fact that I shouldn’t just be sitting here chewing my nails off!"
            mc "I need to see her."
            show eri at m2 with dissolve
            eri "I think she likes you, you know. "
            blank "My feet freeze on the spot. "
            mc "What? "
            show eri at m1 with dissolve
            eri "I'm a demon, not Cupid. I COULD be wrong, but when does that ever happen? "
            eri "Just...it's a feeling I get. She doesn't like me. "
            mc "So?"
            eri "So? It's because she thinks I'm competition. "
            blank "Now that Eri’s put the idea in my brain, I can’t shake it."
            blank "I have to make sure she’s okay, I have to see it for myself."

    mc "Aren’t you tagging along, too?"
    $ eriface = 'happy'
    show eri at m2 with dissolve
    eri "I think I’ll sit this one out. I’ll just be enjoying the comforts of your bed."
    eri "Close the door on your way out~?"
    hide eri with dissolve
    blank "It’s not like anyone could see her."
    blank "But I close the door anyway, heading through the dark and silent school."
    scene scene26a with dissolve
    blank "I slip inside quietly."
    blank "The room is mostly empty, except the small silhouette of Charlie beneath the covers."
    blank "I can hear her breathing, soft and regular."
    think "Maybe she’s still unconscious…"
    think "There’s no one with her, that could be a good sign."
    think "Maybe she’s expected to be fine…"
    blank "Begging that none of the healers come in, I creep toward Charlie’s bed."
    blank "The sense of purpose I had found vanishes again, seeing her still face. Not peaceful, just...absent."
    blank "But then, slowly, it starts to shift."
    blank "My breath catches in my throat as she grimaces, squinting up at me."
    scene scene26c with dissolve
    charlie "Sophie…?"
    mc "Hey."
    blank "She closes her eyes again, grimacing against the attempt at talking."
    mc "Maybe I should get help. Hold on-"
    charlie "Wait."
    blank "She grabs my wrist before I can leave, pulling me close."
    charlie "Don’t think I don’t know you’re not supposed to be here."
    blank "She smiles."
    charlie "Places where you’re not supposed to go are always your favourite."
    charlie "Are you okay?"
    blank "She reaches a hand up, her fingertips gliding against my cheek."
    mc "Me…?"
    mc "I’m the one who should be asking you that."
    blank "She starts to shake her head, but grimaces."
    charlie "No. The whole time...what little I could actually think, I just thought...what if this was how I left you?"
    charlie "I wasn’t afraid of dying. I was just afraid that you’d blame yourself."
    charlie "All that guilt..."
    charlie "It wasn’t your fault, but I know that wouldn’t have mattered."
    charlie "But I didn’t die, so I guess there’s no sense in worrying about it."
    blank "I swallow thickly."
    charlie "Don’t look so glum, Sophie."
    charlie "I’m still around to torture you."
    menu:
        "Good.":
            blank "She grins and hits me playfully on the arm."
            charlie "Right. Good."
        "You don’t torture me.":

            $ charlie_love += 1
            charlie "Maybe I just need to try harder, then?"
            mc "No, that’s not...that isn’t what I meant."
            charlie "I think I know what you meant."
            blank "Her fingers brush along my knuckles slowly."
            charlie "Is that my blood under your nails?"
            blank "My hand twitches in her grip at the realization, but she holds to it fast, her gaze shifting."
            charlie "Stay. It’s alright."

    charlie "I guess my thick skull finally paid off."
    blank "I scoff quietly under my breath."
    if charlie_love >= 6:
        $ charliekiss = True
        play music "music/track02.ogg" fadeout 1 fadein 1
        mc "I can’t stop thinking about what you said, about the Sorcerer Trials and how I’m just...throwing it all away for half a chance."
        mc "I don’t want to put you through what I almost went through."
        charlie "But you have to."
        mc "What?"
        charlie "Don’t you think I’ve figured it out?"
        charlie "It’s just who you are, isn’t it?"
        mc "You don’t know anything about who I am…"
        blank "Her expression falls a bit, and I realize it probably sounded a lot harsher than I meant."
        mc "I mean- y-you do, it’s just, I-"
        mc "I haven’t been entirely honest with you…"
        blank "The truth sits stuck on my tongue."
        mc "Um…"
        charlie "Come on. I could be bleeding into my brain or something here, you better tell me fast."
        mc "Okay, now you’re just trying to make me feel bad."
        blank "She grins guiltily."
        mc "Charlie, I...my name isn’t Sophie."
        charlie "…What?"
        blank "I desperately want to pull my hand back from hers, afraid of how she’ll react."
        blank "But I have to tell her. She deserves to know the truth."
        mc "It’s Shaun."
        blank "The first wave of confusion fills her face."
        mc "I...well, you know I’m not the best at decision making under stressful circumstances…"
        charlie "I’ve caught on, yeah..."
        mc "Before I was supposed to face Magi Shira in my trial, I used a spell I shouldn’t have used and it...it turned me into this."
        mc "Into a girl."
        blank "Her expression stays unreadable, looking over me slowly."
        charlie "So you’re telling me…"
        charlie "That you found a spell that made you go from flat-chested to a D-cup, and you didn’t share?"
        blank "…"
        mc "Uh."
        mc "What?"
        mc "Oh. Right. Why am I even telling you this now, you have a head injury--"
        charlie "Hey, I’m not an invalid."
        charlie "Look, I...I have to admit, I didn’t see this coming. Like, you’re not really the greatest at pretending you’re a girl, but I thought you were just...you know, you."
        charlie "Not that it makes much of a difference."
        mc "Then you’re just...okay with it? With everything?"
        charlie "Okay might be a strong word. I would have liked some warning before I let you get a sneak peak at the goods."
        mc "Now you’re starting to sound like Eri."
        charlie "Heaven forbid."
        blank "She looks at our clasped hands again, sighing softly."
        charlie "If you’re Shaun, then fine. You’re Shaun, I guess."
        blank "I shrug."
        mc "No. It’s-- I like being Sophie for you."
        mc "You’re friends with her."
        charlie "I’m friends with YOU."
        charlie "Whatever your name or your gender is, that doesn’t really make a difference."
        charlie "Just...try not to lie to me next time?"
        mc "Next time?"
        mc "If I ever accidentally turn myself into a cat, I’ll be sure to let you know immediately."
        blank "She grins at me, and it makes my heart swell a little bit."
        blank "I didn’t think she’d be this understanding. I don’t think I would have been this understanding."
        blank "But Charlie is something else."
        charlie "Hey."
        blank "She nudges my arm gently."
        charlie "You have a trial to pass. And, uh, just in case I am bleeding into my brain-- and for luck--"
        scene scene26b with dissolve
        think "What!!?"
        think "Where did this come from!?"
        blank "The feeling of her lips tingle against mine, softer than I expected of someone who could speak so bluntly."
        think "She must have really hit her head…"
        blank "Her hands hold me in place, but I don't struggle."
        mc "Charlie…"
        charlie "Don’t ruin it. Whatever you’re about to say, just don’t."
        charlie "It doesn’t have to mean anything."
        charlie "You don’t have to feel anything at all, okay?"
        charlie "I just wanted to do it. Just once."
        charlie "...Maybe twice."
        charlie "Her lips meet mine again, and this time I respond in kind."
        think "...I’m a man of many vices, okay!?"
        think "It’s a perfectly reasonable reaction when a girl is practically throwing herself at you!"
        think "And it is Charlie."
        think "Much as I’ve been focused on my own troubles and drama, she’s been with me through it all, in her own way."
        blank "She pulls back finally."
        charlie "There. Now go get some sleep."
        mc "But--"
        charlie "Sleep!"
        scene bg black with dissolve
        scene dormroom_night with dissolve
        blank "Her voice chases me out of the room, my thoughts still spinning as I go."
        show eri at m1 with dissolve
        eri "Well? How did it go?"
        mc "...Bizarrely."
        mc "She kissed me."
        blank "Her eyes light up, like I just connected a wire in her brain."
        eri "Really!?"
        $ eriface = 'excited'
        $ eripose = '2'
        show eri at m2 with dissolve
        eri "Did you two do it in the hospital bed!?"
        mc "No!!"
        eri "One step at a time, I suppose. So she kissed a girl."
        mc "And I liked it."
        mc "I told her the truth."
        $ eripose = '1'
        $ eriface = 'neutral'
        show eri at m1 with dissolve
        eri "And she still kissed you?"
        mc "She did."
        blank "I sit down on the bed slowly, still taking in what happened."
        $ eriface = 'flirty'
        show eri at m2 with dissolve
        eri "Hm. She must be into some interesting kinks…"
        mc "Alright, I don’t know why I thought I could talk to you about this."
        mc "I’m going to sleep."
        mc "Why don’t you go stay with Charlie?"
        eri "I don’t have the best bedside manner. I’ll just go spy on who’s cheating on who tonight."
        $ eriface = 'neutral'
        $ eripose = '3'
        show eri at m1 with dissolve
        eri "The gossip never stops, you know~"
        mc "Oh, did Magi Shira come by tonight?"
        eri "No. She never did."
        think "I wonder if my incident with Charlie just furthered Mage Warren’s case against me…"
        think "I don’t know."
        blank "I lay down to sleep on my own, my thoughts about that kiss still spinning."

    scene bg black with dissolve
    centered "..."
    centered "..."
    scene bg black with dissolve
    scene dormroom_day with dissolve
    show shira at m2 with dissolve
    shira "Sophie."
    mc "How is she?"
    blank "I bounce to my feet before I’m even awake, Magi Shira sighing and taking me by the shoulder to balance me."
    shira "Charlie’s recovering fine."
    $ shiraface = 'determined'
    $ shirapose = '1'
    show shira at m1 with dissolve
    shira "We have a few last days to finish lessons, and then…"
    blank "I nod."
    mc "I’m ready."
    scene bg black with dissolve
    scene classroom with dissolve
    blank "We run through the same drills again, the ones we’ve been perfecting for weeks."
    blank "But it feels so basic."
    blank "I’m terrified it won’t be enough…"
    blank "For the next three days, I try to focus on training."
    blank "But my thoughts keep wandering back to Charlie…"
    blank "I didn’t know they would keep her for so long."
    blank "Despite being someone who regularly makes it a sport of driving me crazy, Eri might be the only thing that keeps me sane."
    blank "At least she’s company, a distraction from all the thoughts swirling around my head."
    blank "Failure. Worry. Guilt."
    blank "I end up training alone after our usual classroom hours, missing Charlie’s help."
    blank "Two days. Only two days left and then..."
    show eri at m1 with dissolve
    eri "It’s just a single fight, though, isn’t it? It doesn’t really mean anything…"
    mc "It means everything!"
    mc "It’s my only second chance into getting into the Academy as an official student and not some charity chase..."
    show eri at m2 with dissolve
    eri "It’s not like the Academy is that great."
    mc "Getting into the Academy is everything. Without that, I’m nothing."
    eri "Don’t put it like that."
    show eri at m1 with dissolve
    eri "You’re still hot. That means something."
    eri "And if it doesn’t go well, then we can say forget the magic and I’ll show you how to sleep your way to the top!"
    mc "...Thanks, Eri."
    mc "No problem!"
    think "I have to forcibly remind myself that she’s trying to help."
    scene bg black with dissolve
    scene dormroom_night with dissolve
    $ shiraface = 'neutral'
    show shira flip at l1 with dissolve
    shira "Are you ready, Sophie?"
    blank "I nearly jump out of my skin."
    think "Hopefully she didn’t hear me talking to myself."
    $ mc_clothes = 2
    mc "I nod and strip down for the ritual, my face burning under the scrutiny of Eri’s interested gaze."
    show eri at r2 with dissolve
    eri "Oooh. What’s this?"
    blank "I try my best to ignore her as the demon pulls stealthily at the side of my bra."
    shira "You look unusually warm, Sophie."
    $ shiraface = 'sad'
    show shira flip at l2 with dissolve
    shira "Are you certain you’re alright?"
    blank "Her hand goes to my forehead, eyes scrutinizing."
    mc "I-I’m fine."
    $ eriface = 'flirty'
    show eri at r1 with dissolve
    shira "If you say so. I don’t want you falling ill before your trial. It wouldn’t be fair."
    scene scene9a with dissolve
    blank "She begins the ritual as usual, pouring relaxation through my veins like a cool water."
    if demon_love >= 3:
        play music "music/track01.ogg" fadeout 1 fadein 1
        blank "Eri’s forehead creases slightly as she stares at me."
        think "I wonder if she’s jealous?"
        think "I sent her away all these nights, when she could have been getting this free show.."
        blank "My mind drifts along with my body, hearing my own pulse thrumming in my veins."
        blank "I sigh as her hand reaches my thighs, slides along the side of my leg and traces a finger down the slope of my knee."
        blank "By the time she repeats the motion, I’m already asleep."
        scene bg black with dissolve
        centered "..."
        centered "..."
        scene bg black with dissolve
        scene dormroom_night with dissolve
        eri "Psst!!"
        eri "Hey!!!"
        mc "Nngh.."
        eri "Wake up, dammit!!"
        mc "What?"
        $ eriface = 'annoyed'
        show eri at m1 with dissolve
        mc "What time is it…?"
        eri "It’s wake-the-hell-up ‘o clock!"
        $ eriface = 'mad'
        show eri at m2 with dissolve
        eri "Do you have any idea what just happened?"
        mc "You ruined my sleep?"
        mc "Ow!! What was that for!?" with vpunch
        $ eriface = 'annoyed'
        show eri at m1 with dissolve
        eri "For waking you up!"
        mc "Well congrats, you succeeded!"
        blank "I rub my cheek irritably, glaring at Eri with a scowl that physically hurts my face."
        mc "What do you want?"
        $ eriface = 'angry'
        $ eripose = '2'
        show eri at m2 with dissolve
        eri "I want to look out for you! What Magi Shira just did...why did she do it?"
        mc "It’s just a ritual to balance magic energy. Which is...naturally chaotic or something."
        mc "I don’t remember, we started doing this ages ago, but it has a purpose."
        $ eriface = 'annoyed'
        show eri at m1 with dissolve
        eri "Yeah, the purpose being to squeeze all the magic out of you like you’re a ripe orange for her dark magic OJ!"
        mc "....What?"
        $ eripose = '1'
        show eri at m2 with dissolve
        eri "What she’s doing isn’t balancing your energy or whatever new age crap you’re rambling about."
        eri "She’s putting you to sleep because she’s rapidly draining your magic."
        eri "Trust me, I know what that looks like, and her magic levels went through the roof."
        show eri at m1 with dissolve
        eri "Your aura’s barely visible right now."
        mc "But…"
        think "No, that can’t be right. Magi Shira has been helping us this whole time."
        eri "I know what I saw, Sophie."
        $ eripose = '3'
        show eri at m2 with dissolve
        eri "Why do you think you always feel so tired afterward? If it was supposed to make you more powerful, wouldn’t you feel more powerful, too?"
        mc "But Magi Shira, she…"
        eri "Is really, really bad news."
        show eri at m1 with dissolve
        eri "This is a pretty common technique for Dark Mages, and definitely forbidden."
        eri "Demons do it all the time. Predator and prey."
        eri "Like, it’s kind of hot coming from a human, but I guess you're kind of cool and I don’t want anything to happen to you."
        mc "Charlie…"
        blank "I try to lurch forward suddenly."
        mc "She could be up there doing it to Charlie!"
        blank "A warm hand grabs my shoulder and pushes me back."
        $ eripose = '1'
        show eri at m2 with dissolve
        eri "Even if she is, that’s fine. Charlie doesn’t need her magic right now anyway, right?"
        eri "She’s all cuddled up in medical."
        $ eriface = 'mad'
        show eri at m1 with dissolve
        eri "It’s not like Shira’s going to kill either of you; she needs you alive if she’s going to make you her personal magic milking cows."
        mc "Do you have to put it like that?"
        show eri at m2 with dissolve
        eri "There was a lot of touching in inappropriate places. I call it like I see it."
        mc "Still...I need to tell her."
        blank "I blink toward the doorway, willing my body to move, but it’s like my limbs are cemented to the bed."
        $ eriface = 'annoyed'
        show eri at m1 with dissolve
        eri "As if you’re going to get anywhere after that."
        eri "You have to sleep and recover your magic."
        eri "But I can be your message girl, I guess."
        $ eriface = 'flirty'
        show eri at m2 with dissolve
        eri "I do like seeing the medical magi in all those short robes."
        mc "Alright..."
        blank "It feels like I'm dreaming as Eri leaves."
        hide eri with dissolve
        think "Magi Shira was taking magic from me this whole time...?"
        think "She seemed so intent on helping me. On seeing me achieve my dream."
        think "And her own…"
        think "Didn’t she mention something about that, when we first met?"
        think "She said we were similar somehow. Ambitious."
        blank "My fingers curl slowly into the covers."
        think "I am ambitious, I’ll freely admit to that. But I’m not ruthless. I’m not a monster."
        blank "Shira’s ritual has still taken the life out of me, though."
        blank "Even if the school was burning down, I’d barely have enough energy to get myself outside."
        blank "I guess I can trust Eri to tell Charlie.."
        blank "The light starts to fade again. My eyelids slide shut."
        think "Shira..."
        scene bg black with dissolve
        scene hallway with dissolve
        $ mc_clothes = 8
        $ charlieoutfit = 'uniform'
        blank "The next morning, I get ready in a hurry, throwing my robe on."
        think "What am I going to do?!"
        think "I have to see Charlie. First thing, before class--"
        think "I have to--"
        $ charlieface = 'sad'
        $ charliepose = '1'
        show charlie flip at m1 with dissolve
        mc "CHARLIE!?"
        blank "I grab onto her elbow before she can fall."
        mc "Where did you come from!?"
        $ charliepose = '2'
        show charlie flip at m2 with dissolve
        charlie "...Medical?"
        mc "S-sorry, I didn’t see you."
        mc "Don’t let me give you another head injury."
        charlie "I might seriously kill you if you manage to pull that off."
        blank "She looks into my face, eyes swimming with just as much silent urgency as my own."
        blank "She glances around furtively before she starts to whisper."
        $ charlieface = 'mad'
        show charlie flip at m1 with dissolve
        charlie "Eri told me last night."
        mc "You’re starting to learn her tricks. I feel like I summoned you just by thinking about you."
        mc "Where is she?"
        $ charlieface = 'sad'
        show charlie flip at m2 with dissolve
        charlie "Watching Magi Shira, to make sure she doesn’t do anything else suspicious."
        mc "I wish we’d let her see this before…"
        charlie "What are we supposed to do?"
        blank "I’ve been thinking about this all morning, turning the possibilities over in my mind."
        menu:
            "Confront Shira." if charlie_love >= 6:
                jump confrontshiraend
            "Tell someone.":

                jump tellsomeoneend
            "There’s nothing we can do.":

                jump donothingend
    else:

        blank "I sigh softly, trying not to show too much enjoyment as her hands trail down my stomach and Eri gives a delighted squeal."
        eri "Looks like someone’s having a good time~"
        blank "I wish I could tell her to buzz off without Shira thinking I’m a maniac."
        blank "But even that annoyance washes away under the heat and rhythm of Shira’s hands."
        blank "My eyes start to slide closed."
        eri "You enjoy it, Sophie~"
        blank "She winks at me and laughs."
        blank "Then the two of them fade."
        scene bg black with dissolve
        charlie "Guess who’s back!?" with vpunch
        scene bg black with dissolve
        scene dormroom_day with dissolve
        play music "music/badend.ogg" fadeout 1 fadein 1
        $ charliepose = '1'
        $ charlieface = 'neutral'
        show charlie at l1 with dissolve
        mc "Charlie?"
        blank "My head spins, still trying to wake up from where I’m plastered to the mattress."
        mc "How are you? Are you okay?"
        blank "Each sleepy question comes out like it’s wrapped in cobwebs, sticky and muffled."
        charlie "I’m fine. Clean bill of health."
        $ eriface = 'flirty'
        show eri at r2 with dissolve
        eri "Such a shame."
        eri "I liked it when you couldn’t run away."
        $ charlieface = 'blush'
        show charlie at l2 with dissolve
        charlie "I see you still haven’t taken out the trash…"
        mc "Charlie!"
        blank "She sighs."
        $ charlieface = 'sad'
        show charlie at l1 with dissolve
        charlie "Sorry."
        charlie "Anyway, you know what I came back here for!"
        mc "...To learn magic?"
        $ eripose = '2'
        show eri at r1 with dissolve
        eri "Ohh, to teach sex ed!?"
        charlie "...To cheer for you at your trial, idiot!"
        mc "Oh. Right."
        $ charliepose = '2'
        show charlie at l2 with dissolve
        charlie "You don’t even sound excited. I thought this thing was everything to you."
        charlie "I’m the one who hit my head, why are you having the personality changes?"
        blank "She pokes me in the temple."
        mc "Sorry. I’m still sleepy."
        charlie "That’s such a drag. I’m so hyped now that I’m out of the medical wing, but I guess sitting in a hospital bed for days will do that to you."
        charlie "How long was I even in there?"
        $ eripose = '1'
        show eri at r2 with dissolve
        eri "You still are. This is just a coma dream."
        $ charlieface = 'mad'
        show charlie at l2 with dissolve
        charlie "If you’re here, it’s a coma nightmare."
        blank "But Charlie playfully swats at Eri, who dances away."
        $ eriface = 'happy'
        show eri at r1 with dissolve
        eri "Look at you, trying to grab a handful of the girls."
        blank "She puts her hands over her boobs, feigning a scandalized expression."
        mc "I probably shouldn’t be here for their hate-flirting.."
        mc "I gotta train."
        blank "Charlie helps pry me out of bed."
        $ charliepose = '1'
        show charlie at l1 with dissolve
        charlie "This day has to count for everything. It’s my last chance against Mage Warren, a strange mix of promise of helplessness."
        blank "If I’m not good enough now, nothing I can do in a day will likely change it."
        blank "But at the same time, it seems pointless not to practice."
        blank "I ignore the strange, paradoxical feelings. I get ready with my audience of Charlie and Eri, then we all head to class."
        scene bg black with dissolve
        scene classroom with dissolve
        $ shiraface = 'neutral'
        $ shirapose = '3'
        show shira at m2 with dissolve
        shira "Charlie, you won’t be taking the trial just yet, due to the head injury."
        shira "Sophie, your Initiate Trial is still on schedule for tomorrow."
        $ shirapose = '1'
        $ shiraface = 'sad'
        show shira at m1 with dissolve
        shira "You must prepare. Mage Warren will not show mercy."
        think "Mage Warren…ugh…"
        shira "I see that look. But in the interest of fairness, he will be the one surveying my students."
        $ shiraface = 'neutral'
        show shira at m2 with dissolve
        shira "And I will do the same for him."
        shira "Regardless of what you think of it, it is an even trade."
        shira "Now, no more wasting time."
        $ shirapose = '3'
        show shira at m1 with dissolve
        shira "Let’s begin."
        hide shira with dissolve
        blank "My last day of class before I square off against Mage Warren."
        blank "I deflect spells. I conserve magic. I time my assaults."
        blank "The technique is there, but the power…"
        blank "Shira deflects easily, over and over."
        blank "She even calls class to an early end, insisting that I have to rest up if I want my strength up tomorrow."
        think "Ugh."
        think "What if I really am just...weak?"
        think "What if I was never meant to do this?"
        think "I thought that spell would help things, but maybe my power is never going to be more than it is."
        think "If there was a way to strengthen your own magic, I guess everyone would do it."
        blank "Charlie remains optimistic, tries to assure me that Magi Shira would be far tougher than Mage Warren is going to be."
        blank "That’s how you prepare somebody for a challenge. Make the practice more intense than the test."
        scene bg black with dissolve
        scene dormroom_night with dissolve
        blank "My usual nightly ritual with Magi Shira goes by as per normal."
        blank "I’ve never been more thankful for an arrangement in my whole life."
        blank "But even as the last few strands of consciousness fray inside my mind, I worry about not having enough time to worry."
        blank "The joys of panicking."
        scene bg black with dissolve
        scene arena with dissolve
        blank "This morning didn’t feel real. None of it feels real."
        blank "I’m walking through a dream I don’t recognize, right up to the moment my foot steps inside the Academy’s arena."
        blank "It hits me like a wave, reality crashing into my face."
        think "This is it."
        think "This is the day you become an Initiate, right?"
        blank "My fists clench at my sides, steeling myself for the trial."
        think "Optimism. Optimism. Optimism."
        think "What would Charlie say if she was here?"
        $ charliepose = '1'
        $ charlieface = 'neutral'
        show charlie at m1 with dissolve
        charlie "Good luck!!"
        think "It’s almost like she really is…"
        charlie "Hey!! Spacey!"
        $ charlieface = 'flirty'
        show charlie at m2 with dissolve
        charlie "Don’t ignore me. You’re gonna do great."
        blank "She wraps me up in a brief hug."
        $ charliepose = '2'
        show charlie at m1 with dissolve
        charlie "Get ‘em for me, okay?"
        hide charlie with dissolve
        blank "I nod to her, and she gives me a slight nudge before walking off to the observation seat."
        blank "I see Master Mage Aureman and Magi Shira among them."
        scene scene27a with dissolve
        warren "Are you ready to begin?"
        blank "The answer lodges in my throat, which makes no difference. Mage Warren doesn’t wait for one."
        blank "He takes a few steps back before facing me again."
        charlie "You got this, Sophie!!"
        blank "An irritable scowl flickers across his unmerciful features."
        blank "I swallow the lump in my throat."
        think "Alright..here it goes.."
        blank "Time before the match begin, counts down."
        blank "3...2...1..."
        scene scene27b with hpunch
        blank "Mage Warren’s magic slices through the air like the blade of a sharp, abrupt sword."
        blank "If I defend, it’s out of instinct rather than realization."
        blank "I stumble back, pulling up my defences as he advances on me."
        blank "Another strike. Another."
        blank "My magic flares gold, time and time again, as his magic crashes into it."
        blank "My next shield dissolves weakly."
        blank "Panic floods my system, but there’s nothing I can do."
        scene bg white with hpunch
        blank "His magic fills my vision. "
        scene bg black with dissolve
        think "…?"
        think "Nng…?"
        think "What happened?"
        scene dormroom_night with dissolve
        $ mc_clothes = 8
        $ charlieface = 'sad'
        $ charliepose = '2'
        show charlie at l2 with dissolve
        blank "She frowns down at me."
        charlie "Hey.."
        mc "The trial!!"
        blank "I jolt upwards, but her hand settles on my shoulder."
        $ charliepose = '1'
        show charlie at l1 with dissolve
        charlie "It’s over, remember?"
        $ eriface = 'sad'
        show eri at r1 with dissolve
        eri "I was kind of disappointed."
        eri "I thought it was supposed to be a fight, but no one even took their shirt off."
        charlie "Eri!"
        blank "Charlie scowls at her. They both feel a million miles away from me."
        mc "I lost.."
        charlie "..Y-yeah. You actually fainted, afterwards."
        blank "Heat crawls up my neck."
        $ eripose = '1'
        $ eriface = 'annoyed'
        show eri at r2 with dissolve
        eri "That Warren guy is just a jerk."
        eri "It’s probably because he doesn’t know how to handle his gross man-feelings about how cute Sophie is."
        eri "He didn’t even give her a chance."
        $ charliepose = '2'
        show charlie at l2 with dissolve
        charlie "The Master Mage ruled it a fair match."
        charlie "You saw the flaw in his attack. You could have countered it."
        charlie "You tried to."
        charlie "You just…"
        mc "I wasn’t strong enough."
        blank "My gaze falls to the floor."
        blank "In some ways, I think I did better against Magi Shira."
        blank "At least then I had no training to rely on, there could be some scepticism about my potential."
        mc "What.."
        mc "What happens now..?"
        show charlie at l1 with dissolve
        charlie "Uhm…"
        blank "She shifts nervously."
        show charlie at l2 with dissolve
        charlie "You need to be out of the school."
        blank "The words cause my stomach to clench. Like someone punched me good and hard, right on the naval."
        blank "Right there on the floor, she has all my things already packed up for me. Ready to go."
        mc "Oh.."
        mc "Right…"
        $ charliepose = '2'
        $ charlieface = 'sad'
        show charlie at l1 with dissolve
        charlie "Sophie, I…"
        blank "She reaches out to touch me, but the emotions hit me all at once."
        mc "It’s fine!"
        blank "The anger comes in a burst, as I push past Charlie and her patronizing."
        blank "I grab the bag and run."
        hide charlie with dissolve
        charlie "Sophie!"
        scene bg black with vpunch
        scene entrance_day with dissolve
        blank "I don't even see the school fly by. "
        blank "The fresh air is the only thing that brings me back to my senses, the hundreds of paths stretching out before my feet."
        blank "And the only one I want to walk is at my back..."
        blank "I stare out at the city, which once had so much potential for me. I looked out at it and just saw row after row of possibilities."
        blank "Now it’s just hard, jagged lines of sharp disappointment."
        blank "I stand there. And stand there."
        blank "It slowly comes over me that I don’t know where to go."
        blank "My hands start to shake."
        scene bg black with dissolve
        scene city_night with dissolve
        eri "Out here pouting?"
        mc "Eri.."
        blank "I sigh."
        eri "Quite the dramatic exit."
        scene scene28a with dissolve
        eri "If you’d lost a shoe and stumbled a little, I think that’s the only way you could have made it better."
        mc "Don’t mock me. Not now. "
        blank "She pouts and comes to stand by my side, her fingers entwining with mine."
        eri "Oh, you’ll have to grow a thicker skin than that."
        blank "She laughs softly, humming."
        eri "I have plans for you, my dear."
        mc "What?"
        eri "Believe me when I say I didn’t sabotage you."
        eri "I just...helped, by not helping."
        blank "She smiles slowly, magic tingling in the palm of my hand and spreading through me."
        eri "I even kind of wanted you to succeed, you know. It's been fun hanging around, even with a couple of prudes. "
        eri "But since you have no ambitions or plan now, you really can’t complain if I put you to a better use, can you?"
        mc "What are you doing!?"
        mc "Eri…knock it off, it’s not funny."
        blank "But I don’t think she’s joking."
        think "I don’t understand. She’s never been like this before..."
        mc "Eri, what’s happening!?"
        eri "Probably what you expect, isn’t it?"
        eri "Humans do have such lowly opinion of demons. You think we’re all so terrible."
        eri "Self-fulfilling prophecy and all that."
        mc "Stop!"
        scene scene28b with dissolve
        blank "I try to pull away, but it’s like an electric current has spread through my hands, tensing every muscle."
        blank "She pinches my cheek with her free hand."
        eri "Don’t you worry your pretty little head over it, Sophie."
        eri "You and me? We’re going to be together forever."
        eri "A permanent cuddle partner, isn’t that nice? Just the two of us, always..."
        mc "What do you mean--"
        mc "Eri!!"
        blank "My vision starts to blur."
        mc "Eri what are you doing!?!"
        mc "ERI!!!"
        $ achievement.grant("demonslave")
        scene endingimage2 with dissolve
        blank "Ending #2 - Enslaved by a Demon."
        jump credits

label confrontshiraend:
    $ charlieface = 'annoyed'
    show charlie flip at m1 with dissolve
    charlie "Confront her!?"
    mc "We don’t have to let her keep doing this to us!"
    $ charlieface = 'sad'
    show charlie flip at m2 with dissolve
    charlie "And that’s all? She’s practicing some seriously messed up magic, Sophie."
    mc "Do you think anyone in the Academy is going to believe that?"
    mc "She’s one of them."
    mc "They might even know about it themselves. What if Mage Warren does it to his students, too?"
    mc "What if that’s the whole system!?"
    $ charliepose = '1'
    show charlie at l2 with dissolve
    charlie "You’re getting into some conspiracy theory nonsense, but…"
    $ eriface = 'neutral'
    show eri at r2 with dissolve
    eri "Maybe I can be of some help?"
    mc "DON’T DO THAT!!!"
    blank "My heart pounds against my chest, threatening to burst free."
    blank "I thought we were done for."
    mc "Aren’t you supposed to be watching Shira?"
    show eri at r1 with dissolve
    eri "Mm. Once she got her clothes on, I lost interest."
    mc "Is that what you call being helpful?"
    $ eriface = 'annoyed'
    show eri at r2 with dissolve
    eri "Well, fine. If you’re so busy being rude, I guess you don’t want to hear about the counter spell."
    $ eriface = 'flirty'
    show charlie at l1 with dissolve
    charlie "A counter spell?"
    $ eriface = 'happy'
    show eri at r1 with dissolve
    eri "A way to stop it, darling."
    $ charlieface = 'angry'
    show charlie at l2 with dissolve
    charlie "I know what a counter spell is!!"
    eri "I can teach it to you, but neither of you are as strong as she is. It would likely take the both of you to pull it off."
    eri "And you’ll get a nice little power boost, too."
    mc "That could be what we need to pass our trials!"
    $ charlieface = 'mad'
    show charlie at l1 with dissolve
    charlie "How can you even think about that in a time like this!? Really, it’s like you have blinders on."
    charlie "Besides, it’s what YOU need to pass."
    charlie "I can’t take it yet."
    blank "She taps the side of her head, and my spirit falls a little."
    mc "Oh. Right…"
    $ charlieface = 'neutral'
    $ charliepose = '1'
    show charlie at l2 with dissolve
    charlie "If they let me sit in, I’ll be the best cheerleader I can manage, but right now we really need to focus on this Shira business."
    mc "So we both have to be there to pull it off.."
    $ charlieface = 'blush'
    show charlie at l1 with dissolve
    charlie "We can practice it after class, and then sleep together tonight."
    $ eriface = 'neutral'
    show eri at r2 with dissolve
    eri "Oh, oh!! Invite me!"
    charlie "Not like that!!"
    blank "She frowns."
    $ eriface = 'sad'
    show eri at r1 with dissolve
    eri "Then what’s the point?"
    mc "Are you going to class?"
    $ charlieface = 'neutral'
    show charlie at l2 with dissolve
    charlie "I can sit in and watch you, but I’m not doing anything hands-on for a few days."
    charlie "I just wanted to get out of the damn medical ward…"
    charlie "Almost lost my mind in there."
    $ eriface = 'flirty'
    show eri at r2 with dissolve
    eri "I could have kept you company, all you had to do was ask~"
    blank "She gives me a look, but it’s not quite the same soul-burning hatred I think it used to be."
    blank "Instead, she just sighs."
    show charlie at l1 with dissolve
    charlie "Let’s go to class."
    scene bg black with dissolve
    scene classroom with dissolve
    play music "music/track06.ogg" fadeout 1 fadein 1
    $ shiraface = 'neutral'
    $ shirapose = '3'
    show shira at m1 with dissolve
    blank "It’s ridiculous, looking at her and trying to see her as a Dark Magi."
    blank "She has red hair, for crying out loud."
    think "Would Shira really do something like that, after everything she’s done for me?"
    blank "I run through the drills with Shira again, who pushes me harder and harder every time."
    blank "Spells and counter spells, even giving me advice as to what Mage Warren may try during our time together."
    blank "I don’t let my distraction bother me."
    blank "Whatever Magi Shira might be, right now she’s beneficial to me."
    blank "…"
    blank "Another ordinary day of learning magic."
    blank "Magi Shira gives me a subtle smile at the end of our lesson, but doesn’t break her strict attitude in public."
    $ shirapose = '1'
    show shira at m2 with dissolve
    shira "Good luck tomorrow, Sophie. I expect you’ll do well."
    shira "The same goes for you Charlie, when you finally have your trial."
    show shira at m1 with dissolve
    shira "I’ll see you both tonight."
    blank "With a curt nod she finally strides from the room, leaving me exhausted, my hands tingling from using such concentrated magic for so long."
    hide shira with dissolve
    $ charlieface = 'neutral'
    $ charliepose = '1'
    show charlie at l1 with dissolve
    charlie "You did do really well, you know…"
    charlie "Compared to when we first started, I don’t think there’s anyway you’ll lose."
    mc "Unless I never make it to the trial."
    show charlie at l2 with dissolve
    charlie "We can do this!"
    mc "Maybe we should just wait until after..?"
    charlie "Bad idea."
    $ charlieface = 'sad'
    show charlie at l1 with dissolve
    charlie "She’s taking our energy. You’d be even stronger if she didn’t tamper with you the night before, and you know she will."
    charlie "You have to do something about it tonight."
    $ eriface = 'excited'
    show eri at r1 with dissolve
    eri "So listen up, kids, I’m in charge now!"
    think "Ugh...this is the longest school day ever."
    scene bg black with dissolve
    scene classroom with dissolve
    $ eriface = 'neutral'
    $ charlieface = 'neutral'
    show eri at r1 with dissolve
    show charlie at l1 with dissolve
    blank "Eri sits us around in a triangle and decides to use me as her explanation mannequin."
    eri "When she touches you, she’s pulling magic from all over your body."
    eri "It runs through you like blood, and follows the basic pathways of the circulatory system."
    blank "Her fingers trail over my chest, under the stern look of Charlie’s glare."
    mc "Like, uh...everywhere?"
    blank "Charlie slaps me on the arm."
    charlie "Don’t get her started."
    show eri at r2 with dissolve
    eri "But your magic is strongest at your core, like your heart."
    eri "If you counter the spell while she’s taking your magic from your core, then boom!"
    eri "Maximum damage!"
    eri "Okay, have you got it?"
    show eri at r1 with dissolve
    eri "Remember, timing is everything!"
    eri "She has to be pulling magic from your very core, that’s where it’s strongest, and where you can counter it!"
    eri "But if you wait too long, it’s like putting off an orgasm until it fizzles out because you get tired, instead of building up."
    blank "Charlie and I exchange glances."
    show charlie at l2 with dissolve
    charlie "Can we get that in not-sex lingo?"
    show eri at r1 with dissolve
    eri "Amateurs."
    eri "If she drains too much of your magic, you won’t be able to counter it."
    show eri at r2 with dissolve
    eri "So make sure you do it at the right time."
    eri "You should be able to feel it."
    mc "Can’t you just tell us when to use it?"
    show eri at r1 with dissolve
    eri "I can’t feel it like you can. It wouldn’t be precise."
    eri "Whichever one isn’t being put to sleep, you’ll have to help by giving the other one magic to fuel the ritual."
    eri "I’m guessing you know how to do that?"
    blank "We both nod."
    eri "Good~"
    show charlie at l1 with dissolve
    charlie "But isn’t that really similar to what Magi Shira is doing in the first place?"
    show eri at r2 with dissolve
    eri "Consent is key~"
    eri "Now, as for the actual ritual part--"
    eri "Which one of you have ever been to a sex shop? It’s relevant, trust me!!"
    blank "Charlie and I both groan. "
    scene bg black with dissolve
    scene dormroom_night with dissolve
    blank "Neither of us ate much at dinner."
    blank "We watched Magi Shira from across the hall, talking with the other Mages and Magi."
    blank "The reality of what we were about to do was sinking in the whole time."
    blank "I was actually relieved to see my dorm room."
    $ mc_clothes = 2
    $ charlieoutfit = 'underwear'
    $ charlieface = 'neutral'
    show charlie at l1 with dissolve
    charlie "Are you ready?"
    charlie "No, but I never am until it’s already happening."
    blank "We sit together on the bed, Charlie’s arm linked with mine."
    scene scene29a with dissolve
    charlie "This...doesn’t look very natural, does it?"
    mc "Not especially."
    mc "We should probably lay down together, act like we’re already almost asleep."
    mc "She might be less likely to send you back to your room."
    blank "Charlie nods, lying down in bed and waiting for me."
    charlie "Well? "
    blank "I fight down the urge to go brush my teeth a second time. "
    mc "R-right, sure. "
    blank "I lay on the smallest sliver of the edge of the bed. If Magi Shira walked in, she'd think I was practicing levitating. "
    charlie "Get over here. "
    blank "She drags me to her suddenly. "
    blank "Magi Shira has been at the forefront of my thoughts all day, but even she has to take a backseat when I see Charlie like that."
    blank "It makes all the awkward, primal parts of my brain wake up."
    think "Not now!!"
    blank "Charlie lifts an eyebrow at me, grinning like she knows exactly what I'm thinking. "
    blank "I glance down at her cleavage in a triple-take, like my eyes chose the worst time to have a seizure. "
    if charliekiss:
        charlie "It’s alright."
        blank "She grins at me quietly, reaching over to slide her fingers over my arm."
        mc "You know, technically I am the guy here."
        mc "I should be the one making moves."
        blank "She shrugs."
        charlie "Maybe you’re just as bad at being a guy as you are at being a girl."
        blank "Her teasing grin makes my insides feel like slush, a bead of sweat rolling down my neck."
        charlie "I tried really hard not to like you, you know."
        charlie "Like really hard."
        blank "I can’t help but laugh."
        mc "I’m just that irresistible."
        charlie "Okay, NOW you sound like a guy."

    eri "She’s coming!!"
    eri "--And maybe one of you are, too… Where’s my invite to the party?"
    eri "Why did I get put on watch duty, while you two get to fondle each other!?"
    mc "We’re just lying in the same bed, Eri, there’s nothing--"
    blank "A sharp knock sounds at the door, Charlie and I sharing a final, wide-eyed look as Magi Shira enters."
    scene bg black with dissolve
    scene dormroom_night with dissolve
    $ shiraface = 'neutral'
    $ shirapose = '1'
    $ charlieface = 'sad'
    show shira at r1 with dissolve
    show charlie at l1 with dissolve
    shira "Oh, Charlie."
    shira "I didn’t expect you in here as well…"
    blank "Charlie gives an impressively sleepy stretch."
    charlie "We’re a little nervous about the trials tomorrow."
    $ charlieface = 'blush'
    show charlie at l2 with dissolve
    charlie "Or I am, anyway…"
    charlie "I asked Sophie if I could sleep over."
    shira "I see."
    $ shirapose = '3'
    show shira at r2 with dissolve
    shira "No need to move. At least being asleep, I won’t have to worry about you getting up to anything inappropriate."
    shira "I’ll have this done quickly."
    think "This is it."
    blank "My heart pounds against my chest, feeling her fingers start to brush along the lengths of my arms."
    think "So I’m the one who’s going to have to do it."
    blank "I stare up at her, fighting off the first wave of tiredness that pulls through me."
    blank "If I focus, if I really focus, I can even feel it."
    blank "The pulse of magic being drawn, so slowly and carefully from me."
    blank "Charlie’s fingers clasp subtly on the inside of my elbow, silently willing me to stay awake."
    blank "I have to wait for the right time…"
    blank "I try to find it, try to centre and focus on my core like Eri showed me."
    scene scene30a with dissolve
    blank "Magi Shira’s hand glides across my collar bone, spreads a heat through my chest."
    menu:
        "Now!":
            play music "music/badend.ogg" fadeout 1 fadein 1
            blank "I push back against her, using the same channel she opened up between us to draw my magic back in."
            scene scene30b with vpunch
            blank "My fingers grab Shira by the neck, the only visible patch of skin, fighting hard to turn the tide of the magic."
            blank "At my side, Charlie curls against me, her magic bleeding into my skin like ink through paper."
            shira "--What are you doing!?"
            blank "Her face contorts in rage, and I feel her efforts redouble."
            eri "Focus, Sophie!!"
            blank "I’m drawing from Charlie as much as I can, the strength of our combined magic flickering against her power."
            blank "She’s paralyzed above us, caught in current of the spell."
            blank "But my eyes start to slide shut."
            eri "No-n-no no!!!"
            scene scene30b with hpunch
            shira "How dare you try to defy me!!"
            shira "I tried to help you!!"
            blank "A sharp slap hits across my face, but I can barely feel it."
            blank "The room starts to blur."
            blank "I feel Charlie move, but in the next second she’s gone. Something crashes across the corner of the room."
            shira "You selfish brat."
            shira "After everything I’ve done for you."
            shira "This is what you pull?"
            blank "The words start to fade, my eyelids heavy."
            mc "A-ahh--"
            blank "But it doesn’t stop."
            blank "Her hand doesn’t move the way it used to, staying firm over my chest."
            blank "I thrash against the grip, a wordless scream rising up out of my lips."
            blank "It’s like she’s pulling out my heart."
            blank "Patches of colour dance in front of my eyes, bringing Shira's face into flickering focus. "
            scene scene30c with hpunch
            blank "The rage in her eyes swallows me up. "
            eri "Sophie!!"
            eri "Sophie, no!! Wake up, wake up!"
            scene bg black with dissolve
            blank "Then nothing."
            $ achievement.grant("darkdeath")
            scene endingimage6
            blank "Ending #6 - A Dark Death."
            jump credits
        "Wait…":

            blank "Her hand dips lower. She moves across to the other arm."
            blank "Charlie’s practically pinching me as my eyelids start to droop, the fog beginning to cloud up my mind."
            think "Dammit…"
            think "I can’t go to sleep, I can’t…"
            think "But it would feel so good to just give in…"
            blank "There's nothing harder than trying to claw my way through it, pulling myself up and away from the beckoning dark. "
            blank "Her hand returns to the centre of my collar bone, dipping down along my chest."
            blank "It follows the curve of my chest, bringing with it that flush of familiar heat."
            think "She looks so casual…"
            think "Like she’s not doing anything wrong at all."
            blank "I wonder if she’s done this to all her students. If this is why so many of them have failed."
            think "She’s just been using them…"
            blank "Her palm glides across my heart, the spell settling deep, burrowing inside as if digging for more to take."
            menu:
                "Now!":
                    play music "music/goodend.ogg" fadeout 1 fadein 1
                    blank "I feel it shudder through me, as she pulls magic from my core. Just like Eri said."
                    blank "I push back with the bulk of my magic, hurling it at her like I would an attack."
                    blank "Her whole body shudders in surprise, but I grab her wrist, keeping her hand on my chest."
                    mc "Y-you won’t get away with this. N-Not anymore."
                    scene scene30d with dissolve
                    blank "Charlie curls against my side, pouring her magic into me like ink bleeding through paper."
                    blank "I use it to counteract Shira’s strength, which is rapidly fading."
                    shira "No!!"
                    shira "S-Stop it! You don’t know what you’re doing!"
                    mc "I know exactly what I’m doing. And I know what you’ve been doing, too!"
                    blank "I suddenly feel so alive, electricity running through my veins."
                    think "Is this what it feels like for her every time?"
                    blank "And the more I drain her, the easier it gets, though she won’t stop fighting and struggling."
                    shira "Nnng--"
                    shira "Enough!!"
                    shira "You have no right to do this to me! You’re a student! You--you don't understand what you're doing!!"
                    blank "She tries to thrash against me, but Charlie grabs onto her too, holding her there by a handful of hair. "
                    charlie "Stop fighting it!!"
                    blank "She refuses, trying to claw at my face."
                    blank "But without magic, she’s weak and tired, her movements sluggish."
                    shira "I--"
                    shira "I won’t--"
                    shira "S-Sophie we can--we can come to an arrangement--"
                    shira "I’ll make you a student here-- I’ll graduate you--"
                    shira "We could do great things together--"
                    shira "S-Sophie…"
                    scene scene31a with dissolve
                    blank "She wobbles and then falls down, still and motionless across the bed."
                    blank "I gasp, my body shaking with a newfound power."
                    blank "Charlie sits up slowly as a stillness and silence fills the room."
                    charlie "I-Is it over…?"
                    mc "...I think so."
                    blank "Charlie's hands clamp over her mouth, her eyes wide."
                    blank "I keep staring at Shira, waiting for her to move. Waiting for something. Anything. "
                    eri "She wasn’t going to sleep, though, she was fighting back. You had to hold on."
                    eri "Mortality isn’t such a big deal, I don’t see why humans make such a fuss..."
                    eri "People die in this place all the time anyway."
                    eri "They probably run a crematorium in the basement, we can just stick her down there.."
                    charlie "Eri, you’re not helping!!"
                    mc "I killed her…"
                    charlie "W-We killed her."
                    mc "I’m the one who cast the spell!"
                    charlie "Yeah, and I’m the one who helped you!"
                    charlie "We both did it."
                    scene bg black with dissolve
                    scene hallway with dissolve
                    blank "Head reeling, it feels like a phantom limb knocking on the Master Mage’s door. Not mine."
                    blank "I’m not even afraid. I don’t know if I’m feeling anything at all."
                    blank "It’s like Shira’s magic did work, putting me into the deepest dream."
                    $ auremanpose = '1'
                    show aureman at m1 with dissolve
                    aureman "Yes?"
                    mc "We...need to tell you something that happened."
                    scene bg black with dissolve
                    scene hallway with dissolve
                    show aureman at r1 with dissolve
                    show warren at l1 with dissolve
                    aureman "We suspected Magi Shira was dabbling in the dark arts."
                    warren "I had been forming my own case against her and preparing to act on it."
                    show aureman at r2 with dissolve
                    aureman "We had no idea she was taking power from students, however."
                    aureman "That she would involve them was beyond even my darkest thoughts."
                    show warren at l2 with dissolve
                    warren "I told you."
                    blank "The Master Mage holds up his old hand."
                    show aureman at r1 with dissolve
                    aureman "And you were right, Mage Warren. You had your suspicions, and I had my own evidence, but I needed concrete proof."
                    mc "You mean…you’ve been suspicious of Magi Shira this whole time?"
                    mc "Not...not anything else?"
                    blank "The two blink at me blankly."
                    warren "What are you talking about? "
                    mc "I uh...I may have overheard you talking about removing someone from the school. "
                    show warren at l1 with dissolve
                    warren "And why would that have anything at all to do with you? "
                    blank "I glance to the Master Mage guiltily, his face finally lighting with realization. "
                    aureman "Ah."
                    show aureman at r2 with dissolve
                    aureman "If this is about me finding you in the library, Sophie, then no. I had no intentions of doing anything about that."
                    show warren at l2 with dissolve
                    warren "What is she talking about?"
                    aureman "Nothing, nothing."
                    show aureman at r1 with dissolve
                    aureman "Just a harmless encounter, nothing to be concerned about."
                    blank "His eyes twinkle with a knowing mischief, the first bright look he’s had since we woke him up to tell him we killed our teacher."
                    blank "Not the easiest news to take to someone who’s basically your principal."
                    show aureman at r2 with dissolve
                    aureman "For now, we have a far more pressing matter in resolving this situation."
                    mc "Does this mean we won’t be able to join the Academy?"
                    blank "Mage Warren bristles."
                    warren "A trial will be necessary, to deem you innocent or guilty of using forbidding magic."
                    warren "The counter-spell you used drains magical energy. It is, in the strictest sense, forbidden."
                    mc "Protecting yourself is forbidden!?"
                    aureman "Magi Shira’s power now flows through your veins and probably Charlie's as well, does it not?"
                    blank "She must have felt it, too. Ever since Shira’s death, I’ve felt stronger."
                    blank "Our guilty expressions must answer for us, as Aureman presses on."
                    $ auremanface = 'happy'
                    show aureman at r1 with dissolve
                    aureman "We will have to hold a trial, but no matter how intimidating Mage Warren makes it sound, I assure you it is a formality."
                    aureman "I will be most curious to see you grow from here, twice strengthened. "
                    scene bg black with dissolve
                    blank "Charlie and I room together after the Shira incident, and Mage Warren is forced to take over our education."
                    blank "Despite being even more strict that Shira, he does seem genuinely remorseful that he didn’t act sooner."
                    blank "And without her interference, and with her added power, my lessons are even more productive."
                    blank "My old dorm room is cleared out and closed off for now, leaving me to bunk with Charlie."
                    blank "They could have given me a completely different room, but I prefer it this way."
                    blank "At least for now, after everything that has happened. "
                    scene dormroom_night with dissolve
                    $ mc_clothes = 7
                    $ charlieoutfit = 'smart'
                    show charlie at l1 with dissolve
                    charlie "What do you think they’ll do with your old dorm?"
                    show eri at r2 with dissolve
                    eri "I guess they’ll put some newbie in there who doesn’t know a teacher died in that room."
                    charlie "Eri!!"
                    $ eriface = 'flirty'
                    show eri at r1 with dissolve
                    eri "I’m just being practical! Cuddle with me if you want to shut me up~"
                    charlie "There’s no such thing as just cuddling with you."
                    charlie "Don’t think I didn’t know you were feeling me up last time!!"
                    blank "It’s been an interesting few days, the three of us piled in a room together…"
                    blank "I’m still unpacking my stuff, moving it into Charlie’s space and trying not to get in her way."
                    blank "She doesn't seem to mind the intrusion. "
                    $ charlieface = 'blush'
                    show charlie at l2 with dissolve
                    charlie "What’s that?"
                    blank "She kneels down suddenly, coming back up with something clutched in her hand."
                    blank "I recognize the paper with a jolt. "
                    blank "I snatch it away."
                    mc "T-that’s nothing, just a...silly...uh.."
                    $ charlieface = 'mad'
                    show charlie at l1 with dissolve
                    charlie "Hey!!"
                    charlie "Come on, I was reading that."
                    charlie "I won’t make fun."
                    $ charlieface = 'blush'
                    show charlie at l2 with dissolve
                    charlie "I mean, unless it’s seriously embarrassing, then I’ll make fun."
                    charlie "But lovingly."
                    charlie "Come onnnn."
                    blank "She whines as she reaches for it again, my hands keeping it instinctively close to my chest."
                    blank "Finally, though, I let her fingers tug it away."
                    blank "She skims over it, my face heating."
                    $ charlieface = 'neutral'
                    show charlie at l1 with dissolve
                    charlie "...What is this? Who’s Darren?"
                    $ eriface = 'excited'
                    show eri at r2 with dissolve
                    eri "Maybe an old boyfriend writing Sophie love letters~"
                    blank "Charlie's eyes widen. "
                    $ charliepose = '2'
                    show charlie at l2 with dissolve
                    charlie "Really?"
                    mc "What?!"
                    mc "He's my brother!!"
                    $ charliepose = '1'
                    $ charlieface = 'sad'
                    show charlie at l1 with dissolve
                    charlie "You never mentioned a brother..."
                    blank "Her eyes skim over the letter again, my heart clenching. "
                    blank "I haven't read that letter in so long, but I still can't bring myself to throw it away. "
                    mc "He went here. "
                    show charlie at l2 with dissolve
                    charlie "He's a Mage? "
                    blank "I hesitate, glancing into Charlie's face as the realization slowly dawns. "
                    charlie "O-Oh. "
                    mc "He was a Mage. He made it that far. "
                    mc "One of the best, even. They called him the Golden Mage when he went here. He was the top of his class. "
                    mc "They said he did better than anyone in the Magi Wars. "
                    $ charlieface = 'blush'
                    show charlie at l1 with dissolve
                    charlie "Then he...?"
                    blank "I shift from foot to foot, studying his scratchy handwriting. "
                    mc "He took the Sorcerer's Trial. We promised each other we'd become Sorcerers. "
                    mc "It was the last promise we made before he left.."
                    mc "The Academy sent representatives to tell my mom and I that he was gone. And that was it. "
                    mc "This letter is the last thing I have from him. "
                    $ charliepose = '2'
                    show charlie at l2 with dissolve
                    charlie "I'm sorry, Sophie. I didn't know that's what this was.."
                    blank "She hands it back to me, as I take the faded paper in my hands. "
                    blank "I fold it back carefully again. "
                    $ eriface = 'neutral'
                    show eri at r1 with dissolve
                    eri "And you uh...didn't learn anything from that? "
                    charlie "Eri!!"
                    mc "It's fine. I know where she's coming from. It's why I don't bring it up a lot. "
                    blank "My hands clench. "
                    mc "I just...I made a promise. And at any point he could have turned back, he could have accepted being a Mage and went on with a brilliant career. "
                    mc "But he knew the risks, and he still took the trial. "
                    mc "So will I. I have to. I told him that I would. "
                    show eri at r2 with dissolve
                    eri "But is it reeeaaally breaking a promise if the person you made it to is dead? "
                    eri "I mean, was there any fine print? Did you sign something? There are ways out of this. "
                    blank "I think Charlie might tackle her, but I can only chuckle. "
                    mc "I think what Eri's trying to say is that she doesn't want to see me die in the Trials, too. "
                    blank "The demon girl gives a tiny nod. "
                    mc "I'm not going to. I'm going to beat the Trials. "
                    mc "And once I'm powerful, once I'm a sorcerer, I'm going to change everything. "
                    blank "My fingers tighten around the edges of the letter. "
                    mc "I'm going to make sure no one ever has to die in the Trials again. "
                    scene bg black with dissolve
                    blank "Clinging to that notion has pulled me through a lot. "
                    blank "I helps pull me through now, but Charlie helps more than anything. "
                    blank "She and I keep each other sane when the guilt starts to creep in and we question what we should have done differently."
                    blank "Nothing, she insists."
                    blank "We did the only thing we could. We defended ourselves, and maybe we stopped someone from doing something more dangerous."
                    blank "She’s pretty good at making me see the brighter side of things."
                    blank "Our trial comes quickly, seated by some of the most politically powerful Mages in the kingdom."
                    blank "And among them is even a sorcerer, serving as judge."
                    blank "I would have probably fangirled a little, if I wasn’t busy peeing my pants over possible murder charges."
                    blank "We stand hand in hand again, waiting for the judgement."
                    blank "The judge stands, peering down at us from beneath a heavy brow. "
                    blank "Anxiety bubbles in my stomach. "
                    scene scene32a with dissolve
                    $ mc_clothes = 6
                    judge "The council has reached a verdict. "
                    blank "This is it. "
                    blank "Charlie's fingers feel slippery in my grip, her body a line of tension at my side. "
                    blank "We might as well be staring down our executioner. "
                    judge "The Council of Sorcery hereby proclaims you...innocent of all charges."
                    blank "Charlie throws herself onto me with glee. "
                    blank "Relief comes crashing in so hard my eyes water. That and the fact that she's crushing the air out of me and jumping on my toes. "
                    charlie "We did it! We did it!!"
                    charlie "We...didn’t go to jail!"
                    blank "The sorcerer clears his throat slightly amid our celebrations."
                    judge "The council has ruled that you acted in self-defence. The deceased, Magi Shira, will be used as an example, a warning to all who would practice dark and forbidden magic."
                    judge "It is also the Academy’s decision, based on the input of Mage Warren, that you shall both be permitted entrance into the Academy for the following year."
                    blank "……………"
                    mc "WHAT!?!?"
                    charlie "We got admitted!?!"
                    mc "B-but our trial--"
                    blank "I'm hushed sharply, Charlie still bouncing up and down even as she clamps a hand over my mouth."
                    judge "The progress you have made in training, and the additional power absorbed from Magi Shira, has more than qualified you for admittance."
                    judge "Further, you have done a service to our noble school."
                    judge "You will both be joining the next class and participate in the Magi Wars."
                    think "The Magi Wars…"
                    think "Is this really happening?"
                    blank "Charlie and I exchange glances, trying to contain ourselves as we give a hasty thank you as the trial comes to a sudden close."
                    scene bg black with dissolve
                    scene hallway with dissolve
                    $ charlieoutfit = 'uniform'
                    $ mc_clothes = 8
                    blank "A day later and the news still hasn't fully sunk in."
                    $ charlieface = 'neutral'
                    show charlie flip at m1 with dissolve
                    mc "I can’t believe it!!"
                    mc "We actually made it in!!"
                    blank "The excitement and disbelief practically radiates off Charlie, and I’m not doing so great at containing myself either."
                    if charliekiss:
                        blank "Which still doesn’t prepare me for the sudden embrace of Charlie."
                        scene scene33a with dissolve
                        $ achievement.grant("lovingembrace")
                        blank "I feel the immediate tension drain out of her shoulders, her body listing toward mine."
                        blank "It might not be me, really, but...it’s still her."
                        charlie "Sophie.."
                        blank "She smiles against the kiss, our fingers entwining again."
                        charlie "You know this is going to make being rivals awkward."
                        mc "Shhh."
                        blank "I press another brief peck of my lips against her mouth."
                        mc "Then just enjoy it while you can, and after that we can pretend it never happened."
                        charlie "Sounds like a plan."
                        blank "Not a plan I want to follow, but I have no idea what’s going to happen after this."
                        blank "How our lives are going to change…"

                    mc "Holy…"
                    scene bg black with dissolve
                    scene hallway with dissolve
                    $ charlieoutfit = 'robes'
                    $ mc_clothes = 6
                    show charlie flip at m1 with dissolve
                    mc "The Magi Wars.."
                    blank "I can’t stop saying it."
                    charlie "Let’s try not to think too much about it."
                    mc "Right."

                    show charlie flip at m2 with dissolve
                    charlie "Right."
                    blank "We exchange a long glance, before we burst out laughing."
                    mc "You know what this means, don’t you?"
                    charlie "Dinner’s on you?"
                    mc "Dinner? Who has time for dinner!?"
                    mc "We have to train!!"

                    show charlie flip at m1 with dissolve
                    charlie "No! No more training!!"
                    charlie "I just want one day--"
                    mc "You’ve been in medical, you’ve had plenty of days--"
                    blank "Our bickering resumes as normal. "
                    scene bg black with dissolve
                    blank "I don’t know what’s in store for me and Charlie."
                    blank "I know we’ll face it head on, and that we’ll face it together."
                    blank "If we’ve come this far, and done so much...it actually gives me hope that I might achieve it one day."
                    blank "Sorceress Sophie…"
                    blank "That kind of has a ring to it, doesn’t it?"
                    blank "But first things first."
                    blank "The Magi Wars."
                    scene endingimage1
                    $ persistent.completed = True
                    $ achievement.grant("graduation")
                    scene endingimage1 with dissolve
                    blank "Ending #1 - Graduation Day."
                    jump credits
                "Wait…":

                    play music "music/badend.ogg" fadeout 1 fadein 1
                    blank "I don’t know if that’s it."
                    think "Eri said I would know, didn’t she?"
                    scene scene30b with dissolve
                    blank "Her eyes widen, though, as Shira’s touch starts to tease along my stomach, skipping my navel."
                    think "Oh…"
                    blank "My eyes start to slide shut."
                    think "No."
                    think "No, no, no…"
                    blank "The warm feeling is lifting me up, pulling me away from this reality-- how can anyone who makes me feel this way be bad?"
                    think "N-no."
                    blank "I try to fight against the sleep, desperation rising as I use the counter-spell."
                    eri "What are you doing!?"
                    blank "Shira’s face contorts into rage as she realizes what’s happening."
                    blank "I push back against her, using the same channel she opened up between us to draw my magic back in."
                    eri "Sophie, no!!" with vpunch
                    blank "My fingers grab Shira by the neck, the only visible patch of skin, fighting hard to turn the tide of the magic."
                    blank "At my side, Charlie curls against me, her magic bleeding into my skin like ink through paper."
                    scene scene30c with dissolve
                    shira "--What are you doing, Sophie--!?"
                    blank "Her face contorts in rage, and I feel her efforts redouble."
                    think "Focus!!"
                    blank "Charlie is giving as much as she can, the strength of our combined magic flickering against Shira's power."
                    blank "Shira’s paralyzed above us, caught in current of the spell."
                    blank "But my eyes start to slide shut."
                    think "No-n-no no!!!"
                    shira "How dare you try to defy me!!"
                    shira "I tried to help you!!"
                    blank "A sharp slap hits across my face, but I can barely feel it."
                    blank "The room starts to blur."
                    blank "I feel Charlie move, but in the next second she’s gone. Something crashes across the corner of the room."
                    shira "You selfish brat."
                    shira "After everything I’ve done for you."
                    shira "This is what you pull?"
                    blank "The words start to fade, my eyelids heavy."
                    scene bg black with dissolve
                    mc "A-ahh--"
                    blank "But it doesn’t stop."
                    blank "Her hand doesn’t move the way it used to, staying firm over my chest."
                    blank "I thrash against the grip, a wordless scream rising up out of my lips."
                    blank "It’s like she’s pulling out my heart."
                    eri "Sophie!!"
                    blank "Then nothing."
                    scene endingimage7 with dissolve
                    $ achievement.grant("drainedtodeath")
                    blank "ending #7 - Drained to Death."
                    jump credits


label tellsomeoneend:
    mc "We have to let someone what’s happening."
    mc "She can’t do this to us, they won’t let her get away with it."
    show charlie flip at m1 with dissolve
    charlie "And who’s this someone you have in mind, exactly?"
    mc "Um…"
    mc "Master Aureman?"
    $ charlieface = 'mad'
    show charlie flip at m2 with dissolve
    charlie "What if he already knows?"
    mc "He doesn’t seem like the type…"
    charlie "Neither does Magi Shira!!"
    charlie "I…"
    blank "Charlie shakes her head, though."
    $ charlieface = 'sad'
    show charlie flip at m1 with dissolve
    charlie "No, you’re right."
    charlie "This isn’t something we can handle on our own."
    scene bg black with dissolve
    scene hallway with dissolve
    think "He wasn’t in his classroom, so he must be here.."
    $ auremanpose = '2'
    $ auremanface = 'neutral'
    show aureman at m1 with dissolve
    aureman "Ah, Sophie. Charlie. What can I do for you?"
    mc "We need to talk to you, sir…"
    scene bg black with dissolve
    scene classroom with dissolve
    blank "We sit the Master Mage down and explain to him what Shira has been doing every night."
    blank "The longer we talk, the more severe his expression grows."
    $ auremanface = 'mad'
    show aureman at m1 with dissolve
    aureman "It’s as we feared…"
    mc "What?"
    $ auremanface = 'annoyed'
    show aureman at m2 with dissolve
    aureman "Mage Warren and I have suspected Magi Shira of corruption."
    aureman "I discovered her research into magical manipulation had bypassed the realms of the ethical, but I had no idea she was subjecting her own students to it…"
    show aureman at m1 with dissolve
    aureman "Mage Warren was right."
    aureman "I should have acted sooner."
    mc "Wait...you and Mage Warren argued about this?"
    aureman "We did. Why?"
    mc "You uh...did you also happen to argue about me at all?"
    $ auremanface = 'neutral'
    show aureman at m2 with dissolve
    aureman "You? What reason would we have to argue about you, Sophie?"
    think "...THEY WERE TALKING ABOUT SHIRA THE WHOLE TIME!?"
    blank "I could smack myself."
    mc "N-n-no reason! I just didn’t know…"
    blank "He blinks at me curiously, but then stands, brushing my nonsense aside."
    $ auremanface = 'annoyed'
    show aureman at m1 with dissolve
    aureman "In any case, neither Mage Warren or I can stand for this to happen in our school."
    aureman "We will deal with this ourselves."
    blank "Charlie and I exchange glances, wordlessly wondering what that means."
    scene bg black with dissolve
    scene entrance_interior_day with dissolve
    play music "music/badend.ogg" fadeout 1 fadein 1
    show shira at r1 with dissolve
    show aureman flip at l1 with dissolve
    blank "Before we can reach Mage Warren, a familiar figure seems to materialize in front of us."
    blank "My blood turns to ice water. "
    shira "There you are."
    show shira at r2 with dissolve
    shira "I was looking for my students. They’re not in any trouble, are they, Master Mage?"
    aureman "No, they’re not."
    show aureman flip at l2 with dissolve
    aureman "However, I will need to borrow them."
    blank "He moves in front of us quietly."
    blank "I see Shira’s expression flicker, a subtle realization that something isn’t right."
    blank "Charlie’s hand curls around mine, the atmosphere of the room changing slowly."
    shira "For what purpose?"
    $ auremanface = 'mad'
    show aureman flip at m1 with dissolve
    aureman "To keep them away from you, Magi Shira."
    blank "Her expression remains unreadable in the long, silent seconds that follow."
    blank "And then she smiles, a knife-sharp grin that borders on manic."
    shira "So someone figured it out."
    $ shiraface = 'determined'
    show shira at r1 with dissolve
    shira "You brats."
    shira "How dare you go against me, when I was nothing but kind to you."
    shira "I gave you this pathetic chance--"
    show aureman flip at l2 with dissolve
    aureman "Enough, Shira!"
    blank "The Master Mage hurls a powerful wave of magic toward Shira, the breeze of it ruffling in our hair and the ground trembling."
    blank "To our shock, Shira blocks it."
    scene scene34a with dissolve
    blank "It shatters around her, staining the walls with scorch marks."
    shira "I’ve been absorbing the energy of students for years."
    scene scene34b with dissolve
    shira "Do you really think you can beat me so easily?"
    blank "A flick of her wrist sends the Master Mage sprawling, where he lands inelegantly on the steps."
    mc "No!!"
    blank "A severe glance turns toward us, her gaze narrowing."
    think "This can’t be happening…"
    blank "I stand there staring at the woman I thought was my mentor, maybe even a friend in her own way."
    charlie "Sophie, look out!!"
    blank "Charlie tackles me suddenly."
    scene bg black with hpunch
    blank "The world goes spinning."
    blank "I land a few feet away, the attack missing me completely."
    blank "But Charlie.."
    scene scene35a with dissolve
    mc "Charlie!!"
    blank "I crawl toward her, her breaths shaking in her throat."
    mc "H-hold on. Hold on, it’s okay--"
    mc "It’s okay--"
    blank "Her expression tenses, those pretty brown eyes staring into my face and filled with such terror and confusion."
    mc "I'm here. I've got you, Charlie, just hang on."
    blank "She gives a strangled scream as the pain registers. "
    blank "Footsteps pound around us, voices rising. "
    blank "I can't focus on anything but Charlie. "
    charlie "Sophie..."
    blank "A dark emptiness creeps into her eyes."
    mc "Charlie!!!"
    scene bg black with dissolve
    $ mc_clothes = 6
    blank "The battle brought the attention of many in the school."
    blank "Students and teachers alike swarmed down the stairs to confront Shira."
    blank "Knowing she had no chance, she fled into the city."
    blank "They never caught her."
    blank "I stayed only long enough for Charlie’s burial. A last goodbye."
    blank "She had no family to return to. Instead, they placed her in a plot of land behind the school. "
    blank "A small grave. "
    blank "And so I went home."
    blank "The Master Mage offered me a chance to take my trial, but I declined."
    blank "I’ve given it up. I don’t want to be a great sorcerer anymore. I don’t even care that much about being a boy."
    blank "What I want now is truly impossible: I want things to go back to the way they were."
    blank "I want Charlie."
    blank "I want to redo that day over and over, to do every thing differently. "
    blank "But she’s gone, and maybe I am, too."
    scene bg white with dissolve
    centered "Two years later"
    scene bg black with dissolve
    scene scene36a with dissolve
    $ mc_clothes = 6
    blank "I’ve been protecting my village, using what little magic I learned while at the Academy."
    blank "With no living family of my own, I assumed the role of a family relative."
    blank "No one questioned it."
    blank "Life is mundane, even for someone who does nothing but odd jobs."
    blank "I hunt down people who owe taxes, enrich crops to grow extra bountiful harvests, shoo off vermin with spells."
    blank "It’s not quite as exciting as the life I’d envisioned."
    blank "Twice, I've been contacted by the Academy. They want me to return. "
    blank "And on the anniversary of Charlie's death, someone sends me flowers. I suspect it's the Master Mage. "
    blank "I feel like I should be over it. That Charlie should be long buried by now. "
    blank "But it's something about this body. About Sophie. It keeps her real for me. "
    blank "Charlie was the one person Sophie knew. Her whole identity was built up while Charlie was alive. "
    blank "Without her, nothing feels right. "
    blank "The people in this town are concerned about me, I think. "
    blank "The strange magic girl that wanders around and doesn't speak to anyone. "
    blank "But that's simply how life is now. What life became in the After-Charlie chapters of my story. "
    blank "They're good people, and they do what they can to take care of me. "
    blank "I do another round of patrols, walking through the small streets and around the too-familiar houses."
    blank "And then I see a familiar face."
    blank "In a town this tiny, every face is familiar, but this one-- this one is something out of a nightmare."
    scene bg black with dissolve
    scene village with dissolve
    $ shiraoutfit = 'darkrobes'
    $ shiraface = 'annoyed'
    $ shirapose = '3'
    show shira at m1 with dissolve
    shira "So glad to see you’re doing well, Sophie."
    shira "Small-town life agrees with you."
    blank "The world comes to a halt. I should have been thrown off my feet by how quickly it all stutters to a stop. "
    mc "Y-you…"
    think "Where did she come from?"
    think "Why is she here?"
    blank "A hundred questions blossom into fears."
    $ shiraface = 'determined'
    $ shirapose = '1'
    show shira at m2 with dissolve
    shira "You look surprised. Did you really think I’d let a betrayal go that easily?"
    shira "Or that I’d actually be caught?"
    shira "You’ll be happy to know that I’m doing well, too. In fact...I’ve never been better."
    blank "I don’t even see the blast. It’s invisible, but it cuts through me like a knife."
    blank "Sharp and precise, I don’t even lose my balance."
    blank "It’s not until my hand goes to my stomach that I feel the blood gushing. The same kind of spell she used against Charlie. "
    blank "My knee wobbles and I fall, unable to summon my magic through the shock."
    shira "Don’t worry, Sophie. "
    shira "I’m not going to kill you quick."
    shira "We're just getting started in this little reunion. "
    blank "Her fingers curl into my hair, pulling me up to look at her. "
    shira "You made a feeble attempt at ruining my life. I'm only here to return the favour."
    shira "Bleed out here for a time, and enjoy the front row seat of the destruction of your quaint little hometown."
    scene scene36b with dissolve
    mc "N-no--"
    blank "But I can’t move, Shira’s magic securing binding around my wrists that sears white-hot into my flesh."
    mc "Shira, don't!!"
    mc "Shira!!!!"
    blank "I stare at the place where she disappears. And then it starts. The screaming and the smoke. "
    scene endingimage4 with dissolve
    $ achievement.grant("retribution")
    blank "Ending #4 - Retribution Cometh."
    jump credits


label donothingend:
    charlie "What!?"
    show charlie flip at m1 with dissolve
    charlie "You’re going to let her do this to us?"
    mc "And possibly get into the Academy?"
    mc "Yes!"
    charlie "You’re not going to get in if you don’t have all of your power, Sophie!"
    $ charlieface = 'angry'
    show charlie flip at m2 with dissolve
    charlie "I didn’t know you were this selfish.."
    blank "My heart sinks a little."
    mc "No, that’s...that’s not completely it."
    $ charlieface = 'mad'
    show charlie flip at m1 with dissolve
    charlie "Oh, I’m sure."
    mc "Look, it’s not just getting into the Academy."
    mc "What if the other mentors do the same thing? Maybe she and Mage Warren are working together."
    mc "Maybe the Master Mage knows."
    mc "We don’t know how far this goes…"
    charlie "Ugh."
    blank "Charlie kicks irritably at the floor, but I don’t hear her coming up with any better suggestions."
    charlie "I guess so."
    $ charliepose = '1'
    $ charlieface = 'sad'
    show charlie flip at m2 with dissolve
    charlie "In a place like this, I wouldn’t be surprised."
    blank "I sigh."
    think "At least she’s not mad at me."
    mc "So it’s just another average day, right?"
    $ charliepose = '2'
    show charlie flip at m1 with dissolve
    charlie "Right…"
    blank "We both exchange glances, knowing that neither of us really feel that way."
    blank "The thought of going to class actually makes my stomach hurt, but there’s no way to get out of it."
    blank "We’ll have to face her eventually, one way or another."
    scene bg black with dissolve
    scene classroom with dissolve
    blank "We go about our lessons in typical form, with Shira instructing Charlie and I sternly."
    blank "But even she seems to sense something is off."
    blank "We’re quieter now, and my best attempt at off-setting that silence falls flat and hollow."
    think "I figured that’s how my jokes usually sound, so what’s there to be suspicious of!?"
    blank "Still, we suffer through hours of awkward instruction, trying not to think too much about why we’re not doing as good as we could."
    blank "Because of her."
    blank "And what does she even want with our power? What benefit does it give her?"
    blank "When she finally dismisses us, after hours of that torturous awkwardness, Charlie and I practically run to dinner."
    blank "Eri tags along."
    scene bg black with dissolve
    scene dininghall with dissolve
    play music "music/badend.ogg" fadeout 1 fadein 1
    show charlie at l1 with dissolve
    $ eriface = 'sad'
    $ eripose = '3'
    show eri at r1 with dissolve
    eri "So you really aren’t going to do anything?"
    mc "No...We’ll get used to it."
    charlie "Get used to it?!"
    $ charlieface = 'angry'
    show charlie at l2 with dissolve
    charlie "We’re going to fail because of this woman! And tonight, when she comes into my dorm, I…"
    blank "Charlie grimaces."
    $ charlieface = 'mad'
    show charlie at l1 with dissolve
    charlie "I don’t know how we’re going to play this off, Sophie."
    blank "Eri twirls one of our butter knives between her fingers."
    $ eriface = 'annoyed'
    show eri at r2 with dissolve
    eri "Yes, what could you possibly do?"
    blank "Charlie growls."
    $ charlieface = 'angry'
    show charlie at l2 with dissolve
    charlie "We’re not killing our teacher, Eri, but thanks for the advice!"
    mc "Keep your voice down. Other people can’t see her."
    blank "Charlie knows that, but get her angry enough, and she’d probably yell at Eri in front of an audience."
    blank "I can’t focus on those two right now, though."
    think "What are we going to do?"
    mc "Maybe we should sleep together tonight."
    $ eriface = 'excited'
    $ eripose = '2'
    show eri at r1 with dissolve
    eri "YESSSS, FINALLY!"
    mc "Dammit, Eri, not like thaaaaat."
    eri "Why do you hurt me like this?"
    $ charlieface = 'sad'
    $ charliepose = '1'
    show charlie at l1 with dissolve
    charlie "What DO you mean, sleep together?"
    mc "Just...so we don’t have to be alone, when she does it."
    mc "I don’t know, I thought it might make you feel better about it, if we can’t avoid it."
    show charlie at l2 with dissolve
    charlie "Or maybe we can just tell her we don’t want it?"
    charlie "Isn’t that an idea?"
    show eri at r2 with dissolve
    eri "Yeah, I’m sure the dark wizard lady is totally gonna be fine with that and not suspicious at all when you pull the same thing tomorrow night."
    eri "And the night after that. And the one after that. And the one-"
    charlie "Okay, I get it!"
    charlie "Fine."
    show charlie at l2 with dissolve
    charlie "Then I guess we’ll just have to stick together."
    mc "Yeah."
    think "Others have made it through, right?"
    think "They wouldn’t let Magi Shira still teach if all of her students failed."
    think "I-It’s just an extra challenge. A small, extra hurdle of getting past my dark magi teacher."
    think "Totally simple."
    think "……Why couldn’t I have wanted to be a farmer or something?"
    scene bg black with dissolve
    scene dormroom_night with dissolve
    $ mc_clothes = 2
    $ charlieoutfit = 'underwear'
    show charlie at l1 with dissolve
    charlie "Okay, let’s just try to act natural."
    blank "She’s probably not aware, but me trying to lay in bed with a girl in her underwear is the opposite of natural."
    blank "They’re antonyms in the thesaurus."
    mc "Haha. Yeah. Natural."
    blank "I hurl a pillow at her, but it misses."
    show charlie at l2 with dissolve
    charlie "Stop!!"
    blank "Charlie hisses as she swats my arm down, and in the next second the door opens."
    show shira at r1 with dissolve
    shira "Oh."
    show shira at r2 with dissolve
    shira "Sophie, I wasn’t expecting you to have company…"
    blank "She eyes us with confusion."
    shira "Is there something wrong with your dorm, Charlie?"
    show charlie at l1 with dissolve
    charlie "N-no, I just decided to sleep in here tonight."
    blank "Shira approaches us slowly, looking us both over with an empty gaze."
    shira "You weren’t acting right in class, either."
    shira "I know there’s something the matter, there’s no use in trying to hide it."
    $ shiraface = 'determined'
    show shira at r1 with dissolve
    shira "This school has a way of wringing the truth out of people, I’m afraid."
    think "Is it torture?"
    think "At this rate, I wouldn’t be surprised."
    charlie "N-nothing’s wrong!"
    blank "It’s the most unconvincing thing I’ve ever heard, and a heavy silence follows."
    blank "An oppressive silence. It weighs over the whole room, as if threatening to break us all in two."
    blank "Someone has to say something."
    blank "Someone…"
    blank "Me."
    blank "The words bubble up under the pressure, like a pot brought to a boil."
    mc "W-We know what you’ve been doing."
    mc "We know it’s a spell to drain magic instead of enhance it or control it."
    shira "Tch...what?"
    $ shiraface = 'sad'
    show shira at r2 with dissolve
    shira "Where did you hear such a thing?"
    blank "Her voice grows raspy when she’s alarmed, I realize. Soft and urgent."
    shira "Admittedly, I do take some of your energy by necessity."
    $ shirapose = '3'
    show shira at r1 with dissolve
    shira "Excess energy is detrimental to honing more intricate skills."
    blank "Behind her, Eri shakes her head, her hand like a sock puppet flapping its jaws."
    blank "But Magi Shira prattles on, her voice stern and certain."
    think "How many years has she been doing this? How many students failed because of it?"
    blank "An anger starts to rise in me, but what can I do?"
    menu:
        "Attack Magi Shira":
            shira "I’m impressed, but sadly, not surprised."
            blank "with a wave of her hand, Charlie flies across the room, into an unmoving heap."
            shira "This is the second time you’ve done this to poor Charlie. Someone might think you have a vendetta. "
            mc "Ch-Charlie!!"
            blank "I go running."
            blank "Blood. A pool of it stretches out away from her body--."
            scene bg black with vpunch
            $ mc_clothes = 6
            blank "Something hits the back of my head hard."
            blank "The pain rattles around in my skull for a moment, with all the fear, trying to keep me awake."
            blank "It doesn't. "
            blank "My time in the medical ward was a blur."
            blank "My hands were constantly tied to the bed, and a magical dampening field was kept around me at all times."
            blank "I was treated like a criminal."
            blank "I finally found out why."
            scene scene32b with dissolve
            blank "They hauled me here in front of these people, calling me a murderer."
            blank "I still remember what happened, though. Despite the drug-induced haze I lived in at the medical ward, I remember. "
            blank "It played through my head over and over again. Charlie's face. The moment the spell hit. The blood. "
            judge "You are being tried for the murder of your fellow apprentice. How do you plea?"
            mc "Not guilty!!"
            mc "It wasn’t me--it was Magi Shira!!"
            judge "Magi Shira claims to be the one who stopped you, though unfortunately too late."
            judge "She was the one who called this emergency meeting of the council. Why would she do that, if it would only lead to incriminating herself?"
            mc "Because she’s trying to frame me!!"
            mc "She was taking our power! She has been this entire time!"
            mc "Every night before we’d go to sleep, she’d use a ritual to take some of our magic!"
            mc "I..I tried to stop her, but.."
            blank "I stare into the eyes of a dozen unmoved faces."
            judge "Curious. Magi Shira claims this is exactly what you were doing when you killed Charlie."
            judge "Would you describe yourself as ambitious, Apprentice Sophie?"
            mc "...-Y-yes, but not a murderer, not--"
            judge "I believe we have another testimony here."
            blank "To my surprise, the Master Mage speaks up."
            aureman "This girl was found in the Archives Library in the days before she joined this Academy."
            aureman "I saw her myself. She had broken in."
            judge "And you did not report this immediately?"
            aureman "I did not. From what I had seen, there was no harm done. She was sleeping when I entered."
            aureman "I had never thought her capable of something like this.."
            blank "The Council stares down at me."
            think "No."
            think "No, no, no…"
            mc "I didn’t! It was Shira! It was Magi Shira, she killed Charlie!"
            blank "Tears spring into my eyes just at the sound of the name."
            blank "I haven’t even cried over her yet."
            blank "I couldn’t."
            blank "It was all too surreal, like I’d find her down in her dorm later, once I was out of this mess."
            blank "Just another zany situation I’d gotten myself into."
            blank "But no.."
            blank "She isn’t coming back. She isn’t going to be able to help me."
            blank "I can hardly breathe."
            mc "I didn’t……"
            blank "But the trial presses on without me."
            blank "They’ve already decided on my guilt. It’s clear from the language, from their tone."
            judge "Master Mage, this was an act of gross negligence on your part. How do you intend to compensate for your actions?"
            aureman "I will be stepping down as Master Mage."
            aureman "I have grown too complacent in old age, it seems."
            aureman "I would have never thought of one of our own capable of this…"
            judge "And who will you be electing in your stead?"
            blank "My heart sinks."
            blank "As his eyes turn to Shira."
            scene endingimage5 with dissolve
            $ achievement.grant("convicted")
            blank "Ending #5 - Wrongfully Convicted."
            jump credits
        "Do nothing.":

            blank "Nothing."
            blank "There’s nothing I can do to stop this."
            blank "I hang my head."
            eri "Sophie, look out!!"
            blank "I glance up, surprised--"
            blank "The knife glints from where she pulls it from the folds of her robes."
            blank "Charlie screams. Or maybe it’s me."
            scene bg black with hpunch
            blank "The pain flares, one wound after the other as she stabs downward. I try to summon my magic, but it’s too late."
            blank "In my attempt to get away, I fumble onto the floor and collapse on the other side of the bed."
            blank "I hear a scuffle from above."
            think "Charlie…"
            blank "The blood streams out of my neck, gushes with every weak beat of my heart."
            blank "Panic ensures, my hands clawing at the wound, trying to close it, to undo it. "
            blank "My hands are coated in red, slippery and warm. "
            blank "I’m dying…"
            blank "It’s such a surreal thought, amid the panic."
            blank "I draw a breath that rattles and clenches in my chest, the taste of blood thick."
            blank "Even the sound of the fight above me starts to fade."
            blank "Everything becomes a blind panic."
            blank "Pure, thoughtless fear."
            blank "I can’t see or hear or think."
            blank "Fighting, clawing does nothing."
            blank "My strength is going..."
            scene endingimage8 with dissolve
            $ achievement.grant("bloodyend")
            blank "ending #8 - A Bloody End."
            jump credits
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
