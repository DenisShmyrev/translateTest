init python:


    g = Gallery()



    g.hover_border ="ui/gallery/gallery_hover.png"
    g.locked_button = "ui/gallery/gallery_locked.png"



    g.button("scene1")
    g.unlock_image("scene1a")
    g.unlock_image("scene1b")
    g.unlock_image("scene1c")
    g.unlock_image("scene1d")

    g.button("scene2")
    g.unlock_image("scene2a")
    g.unlock_image("scene2b")
    g.unlock_image("scene6a")
    g.unlock_image("scene6b")

    g.button("scene3")
    g.unlock_image("scene3a")
    g.unlock_image("scene3b")
    g.unlock_image("scene4a")
    g.unlock_image("scene4b")
    g.unlock_image("scene4c")
    g.unlock_image("scene4d")

    g.button("scene4")
    g.unlock_image("scene4e")
    g.unlock_image("scene4f")
    g.unlock_image("scene4g")
    g.unlock_image("scene4h")
    g.unlock_image("scene4i")
    g.unlock_image("scene4j")
    g.unlock_image("scene4k")

    g.button("scene5")
    g.unlock_image("scene5a")
    g.unlock_image("scene5b")
    g.unlock_image("scene5c")

    g.button("scene6")
    g.unlock_image("scene7a")
    g.unlock_image("scene7b")
    g.unlock_image("scene9a")
    g.unlock_image("scene9b")

    g.button("scene7")
    g.unlock_image("scene8a")
    g.unlock_image("scene8b")
    g.unlock_image("scene8c")
    g.unlock_image("scene8d")

    g.button("scene8")
    g.unlock_image("scene10a")
    g.unlock_image("scene10b")
    g.unlock_image("scene11a")
    g.unlock_image("scene11b")
    g.unlock_image("scene11c")
    g.unlock_image("scene11d")
    g.unlock_image("scene11e")

    g.button("scene9")
    g.unlock_image("scene11f")
    g.unlock_image("scene11g")
    g.unlock_image("scene11h")
    g.unlock_image("scene11i")

    g.button("scene10")
    g.unlock_image("scene12a")
    g.unlock_image("scene12b")
    g.unlock_image("scene12c")

    g.button("scene11")
    g.unlock_image("scene13a")
    g.unlock_image("scene13b")

    g.button("scene12")
    g.unlock_image("scene14a")
    g.unlock_image("scene14b")

    g.button("scene13")
    g.unlock_image("scene15a")
    g.unlock_image("scene15b")
    g.unlock_image("scene15c")

    g.button("scene14")
    g.unlock_image("scene16a")
    g.unlock_image("scene16b")

    g.button("scene15")
    g.unlock_image("scene17a")

    g.button("scene16")
    g.unlock_image("scene18a")

    g.button("scene17")
    g.unlock_image("scene19a")
    g.unlock_image("scene19b")

    g.button("scene18")
    g.unlock_image("scene20a")

    g.button("scene19")
    g.unlock_image("scene21a")

    g.button("scene20")
    g.unlock_image("scene22d")
    g.unlock_image("scene22b")
    g.unlock_image("scene22a")
    g.unlock_image("scene22c")

    g.button("scene21")
    g.unlock_image("scene23a")

    g.button("scene22")
    g.unlock_image("scene24a")

    g.button("scene23")
    g.unlock_image("scene25a")
    g.unlock_image("scene25b")
    g.unlock_image("scene25c")
    g.unlock_image("scene25d")
    g.unlock_image("scene25e")

    g.button("scene24")
    g.unlock_image("scene26a")
    g.unlock_image("scene26c")
    g.unlock_image("scene26b")

    g.button("scene25")
    g.unlock_image("scene27a")
    g.unlock_image("scene27b")

    g.button("scene26")
    g.unlock_image("scene28a")
    g.unlock_image("scene28b")

    g.button("scene27")
    g.unlock_image("scene29a")

    g.button("scene28")
    g.unlock_image("scene30a")
    g.unlock_image("scene30b")
    g.unlock_image("scene30c")
    g.unlock_image("scene30d")

    g.button("scene29")
    g.unlock_image("scene31a")

    g.button("scene30")
    g.unlock_image("scene32a")
    g.unlock_image("scene32b")

    g.button("scene31")
    g.unlock_image("scene33a")

    g.button("scene32")
    g.unlock_image("scene34a")

    g.button("scene33")
    g.unlock_image("scene34b")

    g.button("scene34")
    g.unlock_image("scene35a")

    g.button("scene35")
    g.unlock_image("scene36a")
    g.unlock_image("scene36b")

    g.button("scene36")
    g.unlock_image("endingimage1")
    g.unlock_image("endingimage2")
    g.unlock_image("endingimage3")
    g.unlock_image("endingimage4")
    g.unlock_image("endingimage5")
    g.unlock_image("endingimage6")
    g.unlock_image("endingimage7")
    g.unlock_image("endingimage8")


    g.transition = dissolve


screen gallery() tag main_menu_screen:
    modal True

    window:
        style "mm_root"
        add "ui/title/background.png"
        add "ui/gallery/gallery_bg.png"

        vbox:
            spacing 40
            xalign 0.31
            yalign 0.68

            imagebutton auto "ui/title/mainmenu_%s.png" action [Hide("gallery", transition=dissolve), Hide("gallery_page"), Play("sound", "se/open.ogg")] hovered Play("sound", "se/select.ogg") focus_mask True
            add "ui/title/gallery_hover.png"
            imagebutton auto "ui/title/settings_%s.png" action [Show("preferences", transition=dissolve), Show("preferences_1"), Hide("gallery_page"), Play("sound", "se/open.ogg")] hovered Play("sound", "se/select.ogg") focus_mask True

screen gallery_page_1() tag gallery_page:



    add "ui/gallery/page_1_title.png" xalign 0.61 yalign 0.15

    hbox:
        xalign 0.62 yalign 0.86
        spacing 30
        add "ui/navarrowleft_idle.png"
        add "ui/navbutton2_hover.png" yalign 0.5
        imagebutton auto "ui/navbutton2_%s.png" action [Show("gallery_page_2", transition=dissolve), Play("sound", "se/open.ogg")] hovered Play("sound", "se/select.ogg") focus_mask True yalign 0.5
        imagebutton auto "ui/navbutton2_%s.png" action [Show("gallery_page_3", transition=dissolve), Play("sound", "se/open.ogg")] hovered Play("sound", "se/select.ogg") focus_mask True yalign 0.5
        imagebutton auto "ui/navbutton2_%s.png" action [Show("gallery_page_4", transition=dissolve), Play("sound", "se/open.ogg")] hovered Play("sound", "se/select.ogg") focus_mask True yalign 0.5
        imagebutton auto "ui/navarrowright_%s.png" action [Show('gallery_page_2', transition=dissolve), Play("sound", "se/open.ogg")] hovered Play("sound", "se/select.ogg") focus_mask True

    grid 3 3:
        xalign 0.625
        yalign 0.48
        spacing 28


        add g.make_button("scene1", "ui/gallery/gallery_1.png", xalign=0.5, yalign=0.5, xpadding=0, ypadding=0, background=None)
        add g.make_button("scene2", "ui/gallery/gallery_2.png", xalign=0.5, yalign=0.5, xpadding=0, ypadding=0, background=None)
        add g.make_button("scene3", "ui/gallery/gallery_3.png", xalign=0.5, yalign=0.5, xpadding=0, ypadding=0, background=None)

        add g.make_button("scene4", "ui/gallery/gallery_4.png", xalign=0.5, yalign=0.5, xpadding=0, ypadding=0, background=None)
        add g.make_button("scene5", "ui/gallery/gallery_5.png", xalign=0.5, yalign=0.5, xpadding=0, ypadding=0, background=None)
        add g.make_button("scene6", "ui/gallery/gallery_6.png", xalign=0.5, yalign=0.5, xpadding=0, ypadding=0, background=None)

        add g.make_button("scene7", "ui/gallery/gallery_7.png", xalign=0.5, yalign=0.5, xpadding=0, ypadding=0, background=None)
        add g.make_button("scene8", "ui/gallery/gallery_8.png", xalign=0.5, yalign=0.5, xpadding=0, ypadding=0, background=None)
        add g.make_button("scene9", "ui/gallery/gallery_9.png", xalign=0.5, yalign=0.5, xpadding=0, ypadding=0, background=None)

screen gallery_page_2() tag gallery_page:



    add "ui/gallery/page_2_title.png" xalign 0.61 yalign 0.15

    hbox:
        xalign 0.62 yalign 0.86
        spacing 30
        imagebutton auto "ui/navarrowleft_%s.png" action [Show("gallery_page_1", transition=dissolve), Play("sound", "se/open.ogg")] hovered Play("sound", "se/select.ogg") focus_mask True yalign 0.5
        imagebutton auto "ui/navbutton2_%s.png" action [Show("gallery_page_1", transition=dissolve), Play("sound", "se/open.ogg")] hovered Play("sound", "se/select.ogg") focus_mask True yalign 0.5
        add "ui/navbutton2_hover.png" yalign 0.5
        imagebutton auto "ui/navbutton2_%s.png" action [Show("gallery_page_3", transition=dissolve), Play("sound", "se/open.ogg")] hovered Play("sound", "se/select.ogg") focus_mask True yalign 0.5
        imagebutton auto "ui/navbutton2_%s.png" action [Show("gallery_page_4", transition=dissolve), Play("sound", "se/open.ogg")] hovered Play("sound", "se/select.ogg") focus_mask True yalign 0.5
        imagebutton auto "ui/navarrowright_%s.png" action [Show('gallery_page_3', transition=dissolve), Play("sound", "se/open.ogg")] hovered Play("sound", "se/select.ogg") focus_mask True

    grid 3 3:
        xalign 0.625
        yalign 0.48
        spacing 28


        add g.make_button("scene10", "ui/gallery/gallery_10.png", xalign=0.5, yalign=0.5, xpadding=0, ypadding=0, background=None)
        add g.make_button("scene11", "ui/gallery/gallery_11.png", xalign=0.5, yalign=0.5, xpadding=0, ypadding=0, background=None)
        add g.make_button("scene12", "ui/gallery/gallery_12.png", xalign=0.5, yalign=0.5, xpadding=0, ypadding=0, background=None)

        add g.make_button("scene13", "ui/gallery/gallery_13.png", xalign=0.5, yalign=0.5, xpadding=0, ypadding=0, background=None)
        add g.make_button("scene14", "ui/gallery/gallery_14.png", xalign=0.5, yalign=0.5, xpadding=0, ypadding=0, background=None)
        add g.make_button("scene15", "ui/gallery/gallery_15.png", xalign=0.5, yalign=0.5, xpadding=0, ypadding=0, background=None)

        add g.make_button("scene16", "ui/gallery/gallery_16.png", xalign=0.5, yalign=0.5, xpadding=0, ypadding=0, background=None)
        add g.make_button("scene17", "ui/gallery/gallery_17.png", xalign=0.5, yalign=0.5, xpadding=0, ypadding=0, background=None)
        add g.make_button("scene18", "ui/gallery/gallery_18.png", xalign=0.5, yalign=0.5, xpadding=0, ypadding=0, background=None)

screen gallery_page_3() tag gallery_page:



    add "ui/gallery/page_3_title.png" xalign 0.61 yalign 0.15

    hbox:
        xalign 0.62 yalign 0.86
        spacing 30
        imagebutton auto "ui/navarrowleft_%s.png" action [Show("gallery_page_2", transition=dissolve), Play("sound", "se/open.ogg")] hovered Play("sound", "se/select.ogg") focus_mask True yalign 0.5
        imagebutton auto "ui/navbutton2_%s.png" action [Show("gallery_page_1", transition=dissolve), Play("sound", "se/open.ogg")] hovered Play("sound", "se/select.ogg") focus_mask True yalign 0.5
        imagebutton auto "ui/navbutton2_%s.png" action [Show("gallery_page_2", transition=dissolve), Play("sound", "se/open.ogg")] hovered Play("sound", "se/select.ogg") focus_mask True yalign 0.5
        add "ui/navbutton2_hover.png" yalign 0.5
        imagebutton auto "ui/navbutton2_%s.png" action [Show("gallery_page_4", transition=dissolve), Play("sound", "se/open.ogg")] hovered Play("sound", "se/select.ogg") focus_mask True yalign 0.5
        imagebutton auto "ui/navarrowright_%s.png" action [Show('gallery_page_4', transition=dissolve), Play("sound", "se/open.ogg")] hovered Play("sound", "se/select.ogg") focus_mask True


    grid 3 3:
        xalign 0.625
        yalign 0.48
        spacing 28


        add g.make_button("scene19", "ui/gallery/gallery_19.png", xalign=0.5, yalign=0.5, xpadding=0, ypadding=0, background=None)
        add g.make_button("scene20", "ui/gallery/gallery_20.png", xalign=0.5, yalign=0.5, xpadding=0, ypadding=0, background=None)
        add g.make_button("scene21", "ui/gallery/gallery_21.png", xalign=0.5, yalign=0.5, xpadding=0, ypadding=0, background=None)

        add g.make_button("scene22", "ui/gallery/gallery_22.png", xalign=0.5, yalign=0.5, xpadding=0, ypadding=0, background=None)
        add g.make_button("scene23", "ui/gallery/gallery_23.png", xalign=0.5, yalign=0.5, xpadding=0, ypadding=0, background=None)
        add g.make_button("scene24", "ui/gallery/gallery_24.png", xalign=0.5, yalign=0.5, xpadding=0, ypadding=0, background=None)

        add g.make_button("scene25", "ui/gallery/gallery_25.png", xalign=0.5, yalign=0.5, xpadding=0, ypadding=0, background=None)
        add g.make_button("scene26", "ui/gallery/gallery_26.png", xalign=0.5, yalign=0.5, xpadding=0, ypadding=0, background=None)
        add g.make_button("scene27", "ui/gallery/gallery_27.png", xalign=0.5, yalign=0.5, xpadding=0, ypadding=0, background=None)



screen gallery_page_4() tag gallery_page:



    add "ui/gallery/page_4_title.png" xalign 0.61 yalign 0.15

    hbox:
        xalign 0.62 yalign 0.86
        spacing 30
        imagebutton auto "ui/navarrowleft_%s.png" action [Show("gallery_page_3", transition=dissolve), Play("sound", "se/open.ogg")] hovered Play("sound", "se/select.ogg") focus_mask True yalign 0.5
        imagebutton auto "ui/navbutton2_%s.png" action [Show("gallery_page_1", transition=dissolve), Play("sound", "se/open.ogg")] hovered Play("sound", "se/select.ogg") focus_mask True yalign 0.5
        imagebutton auto "ui/navbutton2_%s.png" action [Show("gallery_page_2", transition=dissolve), Play("sound", "se/open.ogg")] hovered Play("sound", "se/select.ogg") focus_mask True yalign 0.5
        imagebutton auto "ui/navbutton2_%s.png" action [Show("gallery_page_3", transition=dissolve), Play("sound", "se/open.ogg")] hovered Play("sound", "se/select.ogg") focus_mask True yalign 0.5
        add "ui/navbutton2_hover.png" yalign 0.5
        add "ui/navarrowright_idle.png"

    grid 3 3:
        xalign 0.625
        yalign 0.48
        spacing 28


        add g.make_button("scene28", "ui/gallery/gallery_28.png", xalign=0.5, yalign=0.5, xpadding=0, ypadding=0, background=None)
        add g.make_button("scene29", "ui/gallery/gallery_29.png", xalign=0.5, yalign=0.5, xpadding=0, ypadding=0, background=None)
        add g.make_button("scene30", "ui/gallery/gallery_30.png", xalign=0.5, yalign=0.5, xpadding=0, ypadding=0, background=None)

        add g.make_button("scene31", "ui/gallery/gallery_31.png", xalign=0.5, yalign=0.5, xpadding=0, ypadding=0, background=None)
        add g.make_button("scene32", "ui/gallery/gallery_32.png", xalign=0.5, yalign=0.5, xpadding=0, ypadding=0, background=None)
        add g.make_button("scene33", "ui/gallery/gallery_33.png", xalign=0.5, yalign=0.5, xpadding=0, ypadding=0, background=None)

        add g.make_button("scene34", "ui/gallery/gallery_34.png", xalign=0.5, yalign=0.5, xpadding=0, ypadding=0, background=None)
        add g.make_button("scene35", "ui/gallery/gallery_35.png", xalign=0.5, yalign=0.5, xpadding=0, ypadding=0, background=None)
        add g.make_button("scene36", "ui/gallery/gallery_36.png", xalign=0.5, yalign=0.5, xpadding=0, ypadding=0, background=None)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
