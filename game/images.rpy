




define slowfade1 = Fade(2.0, 1.0, 3.0, color='#ffffff')
define blood = Fade(0.1, 0.0, 0.8, color='#de0000')
define quickwhite = Fade(0.1, 0.0, 0.8, color='#ffffff')





image bg black = "#000"
image bg white = "#FFF"










define mc = DynamicCharacter("mc_name", window_background="ui/dialogbox.png", color="#0096ff", what_font="PoetsenOne-Regular.ttf", show_two_window = True, image="maincharacter", ctc = anim.Blink("ui/ctc.png"))
define think = Character(" ", window_background="ui/dialogbox.png", color="#0096ff", what_font="PoetsenOne-Regular.ttf", show_two_window = True, image="female_shadow", ctc = anim.Blink("ui/ctc.png"))
define blank = Character(" ", window_background="ui/dialogbox.png", color="#0096ff", what_font="PoetsenOne-Regular.ttf", show_two_window = True, ctc = anim.Blink("ui/ctc.png"))





define aureman = Character("Master Aureman", window_background="ui/dialogbox.png", color="#0096ff", what_font="PoetsenOne-Regular.ttf", show_two_window = True, outlines=[(3, "#000", 0, 0)], ctc = anim.Blink("ui/ctc.png"))
define charlie = Character("Charlie", window_background="ui/dialogbox.png", color="#0096ff", what_font="PoetsenOne-Regular.ttf", show_two_window = True, outlines=[(3, "#000", 0, 0)], ctc = anim.Blink("ui/ctc.png"))
define eri = Character("Eri", window_background="ui/dialogbox.png", color="#0096ff", what_font="PoetsenOne-Regular.ttf", show_two_window = True, outlines=[(3, "#000", 0, 0)], ctc = anim.Blink("ui/ctc.png"))
define succubus = Character("Succubus Demon", window_background="ui/dialogbox.png", color="#0096ff", what_font="PoetsenOne-Regular.ttf", show_two_window = True, outlines=[(3, "#000", 0, 0)], ctc = anim.Blink("ui/ctc.png"))
define warren = Character("Mage Warren", window_background="ui/dialogbox.png", color="#0096ff", what_font="PoetsenOne-Regular.ttf", show_two_window = True, outlines=[(3, "#000", 0, 0)], ctc = anim.Blink("ui/ctc.png"))
define shira = Character("Magi Shira", window_background="ui/dialogbox.png", color="#0096ff", what_font="PoetsenOne-Regular.ttf", show_two_window = True, outlines=[(3, "#000", 0, 0)], ctc = anim.Blink("ui/ctc.png"))

define aureman_unknown = Character("Unknown", window_background="ui/dialogbox.png", color="#0096ff", what_font="PoetsenOne-Regular.ttf", show_two_window = True, outlines=[(3, "#000", 0, 0)], ctc = anim.Blink("ui/ctc.png"))
define charlie_unknown = Character("Unknown", window_background="ui/dialogbox.png", color="#0096ff", what_font="PoetsenOne-Regular.ttf", show_two_window = True, outlines=[(3, "#000", 0, 0)], ctc = anim.Blink("ui/ctc.png"))
define eri_unknown = Character("Demon", window_background="ui/dialogbox.png", color="#0096ff", what_font="PoetsenOne-Regular.ttf", show_two_window = True, outlines=[(3, "#000", 0, 0)], ctc = anim.Blink("ui/ctc.png"))
define warren_unknown = Character("Unknown", window_background="ui/dialogbox.png", color="#0096ff", what_font="PoetsenOne-Regular.ttf", show_two_window = True, outlines=[(3, "#000", 0, 0)], ctc = anim.Blink("ui/ctc.png"))
define shira_unknown = Character("Unknown", window_background="ui/dialogbox.png", color="#0096ff", what_font="PoetsenOne-Regular.ttf", show_two_window = True, outlines=[(3, "#000", 0, 0)], ctc = anim.Blink("ui/ctc.png"))

define judge = Character("Judge", window_background="ui/dialogbox.png", color="#0096ff", what_font="PoetsenOne-Regular.ttf", show_two_window = True, outlines=[(3, "#000", 0, 0)], ctc = anim.Blink("ui/ctc.png"))
define student = Character("Student", window_background="ui/dialogbox.png", color="#0096ff", what_font="PoetsenOne-Regular.ttf", show_two_window = True, outlines=[(3, "#000", 0, 0)], ctc = anim.Blink("ui/ctc.png"))
define thief = Character("Thief", window_background="ui/dialogbox.png", color="#0096ff", what_font="PoetsenOne-Regular.ttf", show_two_window = True, outlines=[(3, "#000", 0, 0)], ctc = anim.Blink("ui/ctc.png"))



init:
    $ charlieface = 'neutral'
    $ charliepose = '1'
    $ charlieoutfit = 'casual'

    $ shiraface = 'neutral'
    $ shirapose = '1'
    $ shiraoutfit = 'robes'

    $ eriface = 'neutral'
    $ eripose = '1'
    $ erioutfit = 'demon'

    $ warrenface = 'neutral'
    $ warrenpose = '1'

    $ auremanface = 'neutral'
    $ auremanpose = '2'



image charlie:
    LiveComposite(
        (514,955),
        (0,0), ("chars/charlie/pose%s %s.png"%(charliepose,charlieoutfit)), 
        (0,0), ("chars/charlie/face %s.png"%(charlieface)), 
        (0,0), ("chars/charlie/base hair.png"), 
        )

image charlie flip:
    xzoom -1
    LiveComposite(
        (514,955),
        (0,0), ("chars/charlie/pose%s %s.png"%(charliepose,charlieoutfit)), 
        (0,0), ("chars/charlie/face %s.png"%(charlieface)), 
        (0,0), ("chars/charlie/base hair.png"), 
        )




image shira:
    LiveComposite(
        (682,1000),
        (0,0), ("chars/shira/pose%s %s.png"%(shirapose,shiraoutfit)), 
        (0,0), ("chars/shira/face %s.png"%(shiraface)), 
        )

image shira flip:
    xzoom -1
    LiveComposite(
        (682,1000),
        (0,0), ("chars/shira/pose%s %s.png"%(shirapose,shiraoutfit)), 
        (0,0), ("chars/shira/face %s.png"%(shiraface)), 
        )



image eri:
    LiveComposite(
        (502,980),
        (0,0), ("chars/eri/pose%s %s.png"%(eripose,erioutfit)), 
        (0,0), ("chars/eri/face %s.png"%(eriface)), 
        )

image eri flip:
    xzoom -1
    LiveComposite(
        (502,980),
        (0,0), ("chars/eri/pose%s %s.png"%(eripose,erioutfit)), 
        (0,0), ("chars/eri/face %s.png"%(eriface)), 
        )




image warren:
    LiveComposite(
        (688,1000),
        (0,0), ("chars/warren/pose%s robes.png"%(warrenpose)), 
        (0,0), ("chars/warren/face %s.png"%(warrenface)), 
        )

image warren flip:
    xzoom -1
    LiveComposite(
        (688,1000),
        (0,0), ("chars/warren/pose%s robes.png"%(warrenpose)), 
        (0,0), ("chars/warren/face %s.png"%(warrenface)),  
        )




image aureman:
    LiveComposite(
        (744,1150),
        (0,0), ("chars/aureman/pose%s %s.png"%(auremanpose,auremanface)), 
        )

image aureman flip:
    xzoom -1
    LiveComposite(
        (744,1150),
        (0,0), ("chars/aureman/pose%s %s.png"%(auremanpose,auremanface)), 
        )







image side maincharacter:
    ConditionSwitch(
        "mc_gender == 1", ImageReference ("female_mc_pose1"),
        "mc_gender == 2", ImageReference ("female_mc_pose2"),
        )


image female_mc_pose1:
    contains:
        ConditionSwitch(
            "mc_clothes == 0", "images/chars/mc/f_blank.png",
            "mc_clothes == 1", "images/chars/mc/mc_longhair_night_neutral.png",
            "mc_clothes == 2", "images/chars/mc/mc_longhair_pinkundies_neutral.png",
            "mc_clothes == 3", "images/chars/mc/mc_longhair_blackundies_neutral.png",
            "mc_clothes == 4", "images/chars/mc/mc_longhair_whiteundies_neutral.png",
            "mc_clothes == 5", "images/chars/mc/mc_longhair_casual_neutral.png",
            "mc_clothes == 6", "images/chars/mc/mc_longhair_robes_neutral.png",
            "mc_clothes == 7", "images/chars/mc/mc_longhair_smart_neutral.png",
            "mc_clothes == 8", "images/chars/mc/mc_longhair_uniform_neutral.png",
            )

image female_mc_pose2:
    contains:
        ConditionSwitch(
            "mc_clothes == 0", "images/chars/mc/f_blank.png",
            "mc_clothes == 1", "images/chars/mc/mc_ponytail_night_neutral.png",
            "mc_clothes == 2", "images/chars/mc/mc_ponytail_pinkundies_neutral.png",
            "mc_clothes == 3", "images/chars/mc/mc_ponytail_blackundies_neutral.png",
            "mc_clothes == 4", "images/chars/mc/mc_ponytail_whiteundies_neutral.png",
            "mc_clothes == 5", "images/chars/mc/mc_ponytail_casual_neutral.png",
            "mc_clothes == 6", "images/chars/mc/mc_ponytail_robes_neutral.png",
            "mc_clothes == 7", "images/chars/mc/mc_ponytail_smart_neutral.png",
            "mc_clothes == 8", "images/chars/mc/mc_ponytail_uniform_neutral.png",
            )


image side female_shadow:
    ConditionSwitch(
        "mc_gender == 1", ImageReference ("fshadow_long"),
        "mc_gender == 2", ImageReference ("fshadow_pony"),
        )


image fshadow_long:
    contains:
        ConditionSwitch(
            "mc_clothes == 0", "images/chars/mc/shadow/f_blank.png",
            "mc_clothes == 1", "images/chars/mc/shadow/mc_longhair_night_neutral.png",
            "mc_clothes == 2", "images/chars/mc/shadow/mc_longhair_pinkundies_neutral.png",
            "mc_clothes == 3", "images/chars/mc/shadow/mc_longhair_blackundies_neutral.png",
            "mc_clothes == 4", "images/chars/mc/shadow/mc_longhair_whiteundies_neutral.png",
            "mc_clothes == 5", "images/chars/mc/shadow/mc_longhair_casual_neutral.png",
            "mc_clothes == 6", "images/chars/mc/shadow/mc_longhair_robes_neutral.png",
            "mc_clothes == 7", "images/chars/mc/shadow/mc_longhair_smart_neutral.png",
            "mc_clothes == 8", "images/chars/mc/shadow/mc_longhair_uniform_neutral.png",
            )

image fshadow_pony:
    contains:
        ConditionSwitch(
            "mc_clothes == 0", "images/chars/mc/shadow/f_blank.png",
            "mc_clothes == 1", "images/chars/mc/shadow/mc_ponytail_night_neutral.png",
            "mc_clothes == 2", "images/chars/mc/shadow/mc_ponytail_pinkundies_neutral.png",
            "mc_clothes == 3", "images/chars/mc/shadow/mc_ponytail_blackundies_neutral.png",
            "mc_clothes == 4", "images/chars/mc/shadow/mc_ponytail_whiteundies_neutral.png",
            "mc_clothes == 5", "images/chars/mc/shadow/mc_ponytail_casual_neutral.png",
            "mc_clothes == 6", "images/chars/mc/shadow/mc_ponytail_robes_neutral.png",
            "mc_clothes == 7", "images/chars/mc/shadow/mc_ponytail_smart_neutral.png",
            "mc_clothes == 8", "images/chars/mc/shadow/mc_ponytail_uniform_neutral.png",
            )







image credits 1 = "#1f0511"
image cred = Text(credits_s, font="SourceSansPro-Italic.ttf", text_align=0.5)
image thanks = Text("{size=80}THANKS FOR PLAYING!", font="Lobster 1.4.otf", text_align=0.5)





transform ending_dissolve:
    xalign 0.5 yalign 0.5 alpha 0.0
    linear 3.0 alpha 1.0
    on hide:
        linear 3.0 alpha 0.0

screen ending:
    text "The End" font "Lobster 1.4.otf" size 50 at ending_dissolve





init:

    image plogo = "images/ui/plogo.png"
    image plogo1 = "images/ui/plogo1.png"
    image menufade = "ui/title/background.png"

label splashscreen:

    $ renpy.pause(0)

    scene black
    with Pause(0.5)
    show plogo
    with dissolve
    $ renpy.pause(1, hard=True)
    show plogo1
    with dissolve
    $ renpy.pause(1, hard=True)
    show menufade at alphadissolve
    with Pause(2.0)
    return





transform logoexpand:
    xalign 0.5 yalign 0.5
    linear 1.0 zoom 1.5 alpha 0.0 xalign 0.5 yalign 0.5





transform alphadissolve:
    subpixel True
    alpha 0.0
    linear 1.0 alpha 1.0
    on hide:
        linear 1.0 alpha 0.0

transform alphadissolvewait:
    subpixel True
    alpha 0.0
    0.5
    linear 0.5 alpha 1.0
    on hide:
        linear 0.5 alpha 0.0

transform alphadissolvefast:
    subpixel True
    alpha 0.0
    linear 0.5 alpha 1.0
    on hide:
        linear 0.5 alpha 0.0

transform zoom_fade_in:
    subpixel True
    alpha 0.01
    zoom 1.2
    easein 0.7 alpha 1.0 zoom 1.0

transform slidein:
    subpixel True
    xalign 0.42 yalign 2.5 xalign 0.52
    easein 0.42 yalign 0.5
    on hide:
        easeout 0.5 yalign 2.5

transform slidein2:
    subpixel True
    xalign 0.5 yalign 2.5 xalign 0.52
    easein 0.5 yalign 0.62
    on hide:
        easeout 0.5 yalign 2.5





transform text_fade_in:
    alpha 0.01
    easein 0.7 alpha 1.0

transform text_slide:
    xalign 0.3
    easein 0.7 xalign 0.4

transform choice_slide:
    alpha 0.01 xalign 0.0
    easein 0.7 alpha 1.0 xalign 0.02





transform left:
    xalign 0.2
    yalign 1.0

transform right:
    xalign 0.8
    yalign 1.0

transform center:
    xalign 0.5
    yalign 1.0

transform middleleft:
    xalign 0.4
    yalign 1.0

transform middleright:
    xalign 0.6
    yalign 1.0


init -1:
    transform r1:
        on show:
            xalign 0.9 yalign 1.0 xoffset 0
            easein .5 xoffset 20 xalign 0.9
        on replace:
            easein .5 xalign 0.9 xoffset 20
        on hide:
            easeout .5 alpha 0 xoffset 0

    transform r2:
        on show:
            xalign 0.9 yalign 1.0 xoffset 0
            easein .5 xoffset 40 xalign 0.9
        on replace:
            easein .5 xalign 0.9 xoffset -20
        on hide:
            easeout .5 alpha 0 xoffset 0

    transform l1:
        on show:
            xalign 0.1 yalign 1.0 xoffset 0
            easein .5 xoffset -20 xalign 0.1
        on replace:
            easein .5 xalign 0.1 xoffset -20
        on hide:
            easeout -0.5 alpha 0 xoffset 0

    transform l2:
        on show:
            xalign 0.1 yalign 1.0 xoffset 0
            easein .5 xoffset 40 xalign 0.1
        on replace:
            easein .5 xalign 0.1 xoffset 20
        on hide:
            easeout .5 alpha 0 xoffset 0

    transform m1:
        on show:
            xalign 0.5 yalign 1.0 xoffset 0
            easein .5 xoffset 20 xalign 0.5
        on replace:
            easein .5 xalign 0.5 xoffset 20
        on hide:

            easeout .5 alpha 0 xoffset 0

    transform m2:
        on show:
            xalign 0.5 yalign 1.0 xoffset 0
            easein .5 xoffset 40 xalign 0.5
        on replace:
            easein .5 xalign 0.5 xoffset -20
        on hide:
            easeout .5 alpha 0 xoffset 0




init -1:


    $ show_quick_menu = True

    transform fd:
        on show:
            easein .3 alpha 1.0
        on replace:
            easein .3 alpha 1.0
        on hide:
            easein .3 alpha 0.0

    transform tcenter:
        on show:
            xalign .5 yalign 1.0
            easein .5 alpha 1.0 xoffset 0
        on replace:
            easein .5 xalign .5 xoffset 0
        on hide:
            easeout .5 alpha 0 xalign .5 xoffset 0


    transform rtl:
        on show:
            xalign 1.0 yalign 1.0 xoffset 0
            easein .5 alpha 1.0 xoffset -45
        on replace:
            easein .5 xalign 1.0 xoffset -45
        on hide:
            easeout .5 alpha 0 xoffset 0


    transform rtr:
        on show:
            xalign 1.0 yalign 1.0 xoffset 0
            easein .5 xoffset 45 xalign 1.0
        on replace:
            easein .5 xalign 1.0 xoffset 45
        on hide:

            easeout .5 alpha 0 xoffset 0

    transform ltr:
        on show:
            xalign 0.0 yalign 1.0 xoffset 0
            easein .5 alpha 1.0 xoffset 45
        on replace:
            easein .5 xalign 0.0 xoffset 45
        on hide:
            easeout .5 alpha 0 xoffset 0

    transform ltl:
        on show:
            xalign 0.0 yalign 1.0 xoffset 0
            easein .5 alpha 1.0 xoffset -45
        on replace:
            easein .5 xalign 0.0 xoffset -45
        on hide:
            easeout .5 alpha 0 xoffset 0

    transform ctl:
        on show:
            xalign .5 yalign 1.0 xoffset 0
            easein .5 alpha 1.0 xoffset -100
        on replace:
            easein .5 xalign .5 xoffset -100
        on hide:
            easeout .5 alpha 0 xalign .5

    transform ctr:
        on show:
            xalign .5 yalign 1.0 xoffset 0
            easein .5 alpha 1.0 xoffset 100
        on replace:
            easein .5 xalign .5 xoffset 100
        on hide:
            easeout .5 alpha 0 xalign .5 xoffset 0
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
