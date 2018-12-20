
label credits:
    $ credits_speed = 50
    show cred at Move((0.75, 2.8), (0.75, 0.0), credits_speed, repeat=False, bounce=False, xanchor="center", yanchor="bottom")
    show thanks:
        yanchor 0.10 ypos 0.10
        xanchor 0.95 xpos 0.95
    with dissolve
    with Pause(5)
    hide thanks
    with dissolve
    with Pause(credits_speed - 1)
    $ renpy.pause(3)
    show bg black
    with dissolve
    with Pause(2)
    return

init python:
    credits = ('Original Concept', 'A.J.Tilley'), ('Coding & Design', 'A.J.Tilley'), ('Background Art', 'Alexey Yakovlev'), ('Sprites and CG Scenes', 'Enrique Bolatre'), ('Lead Script Writer', 'Kayzda'), ('GUI Design', 'A.J.Tilley & Johnathan X'),
    credits_s = "{size=40}Developed by\n{size=60}Dharker Studios Limited\n{size=40}DharkerStudio.com{/size}\n\n"
    c1 = ''
    for c in credits:
        if not c1==c[0]:
            credits_s += "\n{size=60}" + c[0] + "\n"
        credits_s += "{size=40}" + c[1] + "\n"
        c1=c[0]
    credits_s += "\n{size=60}Original Musical Score\n{size=40}Produced by Sam L. Jones.\n"
    credits_s += "\n\n"
    credits_s += "\n{size=40}Game Created in Renpy\n{size=40}www.renpy.org"
    credits_s += "\n\n"
    credits_s += "\n{size=50}Special Thanks to all our\nKickstarter Backers...\n\nWithout you this game\nwould not have been possible.\n"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
