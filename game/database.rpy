



screen database() tag main_menu_screen:
    modal True

    window:
        style "mm_root"
        add "ui/title/background.png"
        add "ui/database/database_bg.png"

        grid 2 3:
            spacing 40
            xalign 0.61
            yalign 0.6
            imagebutton auto "ui/database/charlie_%s.png" action [Show("database_charlie"), Play("sound", "se/open.ogg")] hovered Play("sound", "se/select.ogg") focus_mask True
            imagebutton auto "ui/database/magiwarren_%s.png" action [Show("database_warren"), Play("sound", "se/open.ogg")] hovered Play("sound", "se/select.ogg") focus_mask True
            imagebutton auto "ui/database/magishira_%s.png" action [Show("database_shira"), Play("sound", "se/open.ogg")] hovered Play("sound", "se/select.ogg") focus_mask True
            imagebutton auto "ui/database/masteraureman_%s.png" action [Show("database_aureman"), Play("sound", "se/open.ogg")] hovered Play("sound", "se/select.ogg") focus_mask True
            imagebutton auto "ui/database/protagonist_%s.png" action [Show("database_protagonist"), Play("sound", "se/open.ogg")] hovered Play("sound", "se/select.ogg") focus_mask True
            imagebutton auto "ui/database/succubuseri_%s.png" action [Show("database_eri"), Play("sound", "se/open.ogg")] hovered Play("sound", "se/select.ogg") focus_mask True

        vbox:
            spacing 7
            xalign 0.31
            yalign 0.71

            imagebutton auto "ui/title/mainmenu_%s.png" action [Hide("database", transition=dissolve), Play("sound", "se/open.ogg")] hovered Play("sound", "se/select.ogg") focus_mask True
            add "ui/title/database_hover.png"
            imagebutton auto "ui/title/gallery_%s.png" action [Show("gallery", transition=dissolve), Show("gallery_page_1"), Play("sound", "se/open.ogg")] hovered Play("sound", "se/select.ogg") focus_mask True
            imagebutton auto "ui/title/settings_%s.png" action [Show("preferences", transition=dissolve), Show("preferences_1"), Play("sound", "se/open.ogg")] hovered Play("sound", "se/select.ogg") focus_mask True

screen database_protagonist():
    modal True
    window at database_popup:
        xysize (1920,1080)
        left_margin 0
        left_padding 0
        right_padding 0
        top_padding 0
        background "ui/database/popup_bg.png"

        imagebutton auto "ui/database/close_%s.png" action [Hide("database_protagonist"), Play("sound", "se/close.ogg")] hovered Play("sound", "se/select.ogg") focus_mask True xalign 0.86 yalign 0.07

        add "ui/database/main/protagonist_title.png" xalign 0.5 yalign 0.15
        add "ui/database/main/protagonist_pic.png" xalign 0.2 yalign 0.6

        if persistent.introcomplete:
            text "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum." style "database_text"
        else:
            text "\n\nNo Data to Display at present.\n\n\n\n\nComplete more of the game to unlock\nthis characters bio information." style "database_text"

screen database_charlie():
    modal True
    window at database_popup:
        xysize (1920,1080)
        left_margin 0
        left_padding 0
        right_padding 0
        top_padding 0
        background "ui/database/popup_bg.png"

        imagebutton auto "ui/database/close_%s.png" action [Hide("database_charlie"), Play("sound", "se/close.ogg")] hovered Play("sound", "se/select.ogg") focus_mask True xalign 0.86 yalign 0.07

        add "ui/database/main/charlie_title.png" xalign 0.5 yalign 0.15
        add "ui/database/main/charlie_pic.png" xalign 0.2 yalign 0.6

        if persistent.charliemet:
            text "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum." style "database_text"
        else:
            text "\n\nNo Data to Display at present.\n\n\n\n\nComplete more of the game to unlock\nthis characters bio information." style "database_text"

screen database_shira():
    modal True
    window at database_popup:
        xysize (1920,1080)
        left_margin 0
        left_padding 0
        right_padding 0
        top_padding 0
        background "ui/database/popup_bg.png"

        imagebutton auto "ui/database/close_%s.png" action [Hide("database_shira"), Play("sound", "se/close.ogg")] hovered Play("sound", "se/select.ogg") focus_mask True xalign 0.86 yalign 0.07

        add "ui/database/main/shira_title.png" xalign 0.5 yalign 0.15
        add "ui/database/main/shira_pic.png" xalign 0.2 yalign 0.6

        if persistent.shiramet:
            text "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum." style "database_text"
        else:
            text "\n\nNo Data to Display at present.\n\n\n\n\nComplete more of the game to unlock\nthis characters bio information." style "database_text"



screen database_warren():
    modal True
    window at database_popup:
        xysize (1920,1080)
        left_margin 0
        left_padding 0
        right_padding 0
        top_padding 0
        background "ui/database/popup_bg.png"

        imagebutton auto "ui/database/close_%s.png" action [Hide("database_warren"), Play("sound", "se/close.ogg")] hovered Play("sound", "se/select.ogg") focus_mask True xalign 0.86 yalign 0.07

        add "ui/database/main/warren_title.png" xalign 0.5 yalign 0.15
        add "ui/database/main/warren_pic.png" xalign 0.2 yalign 0.6

        if persistent.warrenmet:
            text "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum." style "database_text"
        else:
            text "\n\nNo Data to Display at present.\n\n\n\n\nComplete more of the game to unlock\nthis characters bio information." style "database_text"




screen database_aureman():
    modal True
    window at database_popup:
        xysize (1920,1080)
        left_margin 0
        left_padding 0
        right_padding 0
        top_padding 0
        background "ui/database/popup_bg.png"

        imagebutton auto "ui/database/close_%s.png" action [Hide("database_aureman"), Play("sound", "se/close.ogg")] hovered Play("sound", "se/select.ogg") focus_mask True xalign 0.86 yalign 0.07

        add "ui/database/main/aureman_title.png" xalign 0.5 yalign 0.15
        add "ui/database/main/aureman_pic.png" xalign 0.2 yalign 0.6

        if persistent.auremanmet:
            text "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum." style "database_text"
        else:
            text "\n\nNo Data to Display at present.\n\n\n\n\nComplete more of the game to unlock\nthis characters bio information." style "database_text"


screen database_eri():
    modal True
    window at database_popup:
        xysize (1920,1080)
        left_margin 0
        left_padding 0
        right_padding 0
        top_padding 0
        background "ui/database/popup_bg.png"

        imagebutton auto "ui/database/close_%s.png" action [Hide("database_eri"), Play("sound", "se/close.ogg")] hovered Play("sound", "se/select.ogg") focus_mask True xalign 0.86 yalign 0.07

        add "ui/database/main/eri_title.png" xalign 0.5 yalign 0.15
        add "ui/database/main/eri_pic.png" xalign 0.2 yalign 0.6

        if persistent.erimet:
            text "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum." style "database_text"
        else:
            text "\n\nNo Data to Display at present.\n\n\n\n\nComplete more of the game to unlock\nthis characters bio information." style "database_text"





transform database_popup:
    ycenter 2.0 xcenter 0.5
    ease 0.6 ycenter 0.5
    on hide:
        ease 0.6 ycenter 2.0

style database_text:
    xpos 800
    ypos 300
    xysize (800,800)
    color "#FFF"
    outlines [(2, "#000", 0, 0)]
    font "PoetsenOne-Regular.ttf"
    size 34
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
