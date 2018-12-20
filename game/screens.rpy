











screen say(who, what, side_image=None, two_window=False):


    use quick_menu


    if not two_window:


        window:
            id "window"

            has vbox:
                style "say_vbox"

            if who:
                text who id "who"

            text what id "what"

    else:



        window:
            id "window"

            has vbox:
                style "say_vbox"

            text what id "what"

        if who:
            window:
                style "say_who_window"

                text who:
                    id "who"



    if side_image:
        add side_image
    else:
        add SideImage() xalign 0.01 yalign 1.0 zoom 0.4







transform choice_pop:
    subpixel True
    alpha 0.0 zoom 1.1
    ease 0.4 alpha 1.0 zoom 1.0

screen choice(items):

    window at choice_pop:
        style "menu_window"
        xalign 0.5
        yalign 0.5

        has vbox:
            style "menu"
            spacing 2

        for caption, action, chosen in items:

            if action:

                button:
                    action [action, Play("sound", "se/open.ogg")] hovered Play("sound", "se/select.ogg")
                    style "menu_choice_button"

                    text caption style "menu_choice"

            else:
                text caption style "menu_caption"

init -2:
    $ config.narrator_menu = True

    style menu_window is default

    style menu_choice is button_text clear:
        size 40
        color "#FFF"


    style menu_choice_button is button:
        ypadding 10
        background Frame("ui/choice_button.png", 12, 12)
        hover_background Frame("ui/choice_button_hover.png", 12, 12)
        xminimum int(config.screen_width * 0.75)
        xmaximum int(config.screen_width * 0.75)








screen input(prompt):

    window style "input_window":
        has vbox

        text prompt style "input_prompt"
        input id "input" style "input_text"

    use quick_menu







screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox:
            style "nvl_vbox"


        for who, what, who_id, what_id, window_id in dialogue:
            window:
                id window_id

                has hbox:
                    spacing 10

                if who is not None:
                    text who id who_id

                text what id what_id


        if items:

            vbox:
                id "menu"

                for caption, action, chosen in items:

                    if action:

                        button:
                            style "nvl_menu_choice_button"
                            action action

                            text caption style "nvl_menu_choice"

                    else:

                        text caption style "nvl_dialogue"

    add SideImage() xalign 0.0 yalign 1.0

    use quick_menu







screen main_menu():


    window:
        style "mm_root"
        add "ui/title/background.png"
        add "ui/title/mm_base.png"

        vbox:
            spacing 10
            xalign 0.61
            yalign 0.72

            imagebutton auto "ui/title/start_%s.png" action [Start(), Play("sound", "se/open.ogg")] hovered Play("sound", "se/select.ogg") focus_mask True
            imagebutton auto "ui/title/load_%s.png" action [Show("load"), Play("sound", "se/open.ogg")] hovered Play("sound", "se/select.ogg") focus_mask True
            imagebutton auto "ui/title/quit_%s.png" action [Quit(confirm=True), Play("sound", "se/open.ogg")] hovered Play("sound", "se/select.ogg") focus_mask True

        vbox:
            spacing 40
            xalign 0.31
            yalign 0.68

            add "ui/title/mainmenu_hover.png"
            imagebutton auto "ui/title/gallery_%s.png" action [Show("gallery", transition=dissolve), Show("gallery_page_1"), Play("sound", "se/open.ogg")] hovered Play("sound", "se/select.ogg") focus_mask True
            imagebutton auto "ui/title/settings_%s.png" action [Show("preferences", transition=dissolve), Show("preferences_1"), Play("sound", "se/open.ogg")] hovered Play("sound", "se/select.ogg") focus_mask True

init -2:


    style mm_button:
        size_group "mm"








transform zoom_fade_in:
    subpixel True
    alpha 0.01
    zoom 1.2
    easein 0.7 alpha 1.0 zoom 1.0

screen navigation tag menu:
    modal True


    frame at zoom_fade_in:
        xalign 0.46 yalign 0.5
        add "ui/nav_back.png" xalign 0.5 yalign 0.5 zoom 1.5

        hbox:
            xalign 0.5 yalign 0.5
            imagebutton auto "ui/navmenu/return_%s.png" action [Return(), Play("sound", "se/open.ogg")] hovered Play("sound", "se/select.ogg") focus_mask True
            null width 20
            imagebutton auto "ui/navmenu/save_%s.png" action [Show('save'), Play("sound", "se/open.ogg")] hovered Play("sound", "se/select.ogg") focus_mask True
            null width 20
            imagebutton auto "ui/navmenu/load_%s.png" action [Show('load'), Play("sound", "se/open.ogg")] hovered Play("sound", "se/select.ogg") focus_mask True
            null width 20
            imagebutton auto "ui/navmenu/quit_%s.png" action [MainMenu(), Play("sound", "se/alert.ogg")] hovered Play("sound", "se/select.ogg") focus_mask True

init -2:


    style gm_nav_button:
        size_group "gm_nav"













screen file_picker():

    hbox:
        xalign 0.5 yalign 0.5
        imagebutton auto "ui/navarrowleft_%s.png" action [FilePagePrevious(), Play("sound", "se/open.ogg")] hovered Play("sound", "se/select.ogg") focus_mask True
        null width 1200
        imagebutton auto "ui/navarrowright_%s.png" action [FilePageNext(max=8), Play("sound", "se/open.ogg")] hovered Play("sound", "se/select.ogg") focus_mask True

    hbox:
        xalign 0.5
        yalign 0.85
        style_group "file_picker_nav"

        textbutton _("Auto"):
            action [FilePage("auto"), Play("sound", "se/open.ogg")] hovered Play("sound", "se/select.ogg")

        textbutton _("Quick"):
            action [FilePage("quick"), Play("sound", "se/open.ogg")] hovered Play("sound", "se/select.ogg")

        for i in range(1, 9):
            textbutton str(i):
                action [FilePage(i), Play("sound", "se/open.ogg")] hovered Play("sound", "se/select.ogg")

    $ columns = 3
    $ rows = 2


    grid columns rows:
        xfill True
        yfill True
        xysize (1000,500)
        xalign 0.515
        yalign 0.55
        style_group "file_picker"


        for i in range(1, columns * rows + 1):


            button:
                action [FileAction(i), Play("sound", "se/open.ogg")] hovered Play("sound", "se/select.ogg")

                has vbox:
                    xalign 0.5


                add FileScreenshot(i)

                $ file_name = FileSlotName(i, columns * rows)
                $ file_time = FileTime(i, empty=_("Empty Slot."))
                $ save_name = FileSaveName(i)



                text "[file_name]. [file_time!t]\n[save_name!t]" text_align 0.5

                key "save_delete" action FileDelete(i)


screen save():
    modal True
    window at database_popup:
        xysize (1920,1080)
        left_margin 0
        left_padding 0
        right_padding 0
        top_padding 0
        background "ui/database/popup_bg.png"
        imagebutton auto "ui/database/close_%s.png" action [Hide("save"), Play("sound", "se/close.ogg")] hovered Play("sound", "se/select.ogg") focus_mask True xalign 0.86 yalign 0.07

        add "ui/save_title.png" xalign 0.5 yalign 0.15

        use file_picker

screen load():
    modal True
    window at database_popup:
        xysize (1920,1080)
        left_margin 0
        left_padding 0
        right_padding 0
        top_padding 0
        background "ui/database/popup_bg.png"
        imagebutton auto "ui/database/close_%s.png" action [Hide("load"), Play("sound", "se/close.ogg")] hovered Play("sound", "se/select.ogg") focus_mask True xalign 0.86 yalign 0.07

        add "ui/load_title.png" xalign 0.5 yalign 0.15

        use file_picker

init -2:
    style file_picker_frame is menu_frame
    style file_picker_nav_button is small_button:
        background None
    style file_picker_nav_button_text is small_button_text:
        font "Lobster 1.4.otf"
        size 50
        hover_color "#91d05a"
        selected_color "#91d05a"
    style file_picker_button is large_button:
        background Frame("ui/save_thumb.png", 25, 25)
        hover_background Frame("ui/save_thumb_hover.png", 25, 25)
        top_padding 30
        xysize (300,150)
        focus_mask True



    style file_picker_text is large_button_text:
        font "Lobster 1.4.otf"
        size 28
        xalign 0.5

style small_window is default:
    xysize (928,675)
    background "ui/small_window.png"

style close_button is default:
    focus_mask True
    xpos 837
    ypos 20

transform popup:
    subpixel True
    ycenter 1.5 xalign 0.5
    ease 0.5 ycenter 0.5
    on hide:
        ease 0.5 ycenter 1.5








screen preferences() tag main_menu_screen:
    modal True

    window:
        style "mm_root"
        add "ui/title/background.png"
        add "ui/settings/settings_bg.png"

        vbox:
            spacing 40
            xalign 0.31
            yalign 0.68

            imagebutton auto "ui/title/mainmenu_%s.png" action [Hide("preferences", transition=dissolve), Hide('preferences_screen'), Play("sound", "se/open.ogg")] hovered Play("sound", "se/select.ogg") focus_mask True
            imagebutton auto "ui/title/gallery_%s.png" action [Show("gallery", transition=dissolve), Show("gallery_page_1"), Hide('preferences_screen'), Play("sound", "se/open.ogg")] hovered Play("sound", "se/select.ogg") focus_mask True
            add "ui/title/settings_hover.png"

screen preferences_1() tag preferences_screen:


    hbox:
        xalign 0.62 yalign 0.86
        spacing 30
        add "ui/navarrowleft_idle.png"
        add "ui/navbutton_hover.png" yalign 0.5
        imagebutton auto "ui/navbutton_%s.png" action [Show("preferences_2", transition=dissolve), Play("sound", "se/open.ogg")] hovered Play("sound", "se/select.ogg") focus_mask True yalign 0.5
        imagebutton auto "ui/navbutton_%s.png" action [Show("preferences_3", transition=dissolve), Play("sound", "se/open.ogg")] hovered Play("sound", "se/select.ogg") focus_mask True yalign 0.5
        imagebutton auto "ui/navarrowright_%s.png" action [Show('preferences_2', transition=dissolve), Play("sound", "se/open.ogg")] hovered Play("sound", "se/select.ogg") focus_mask True


    vbox:
        xalign 0.62
        ypos 250

        add "ui/settings/display_title.png" xalign 0.5
        hbox:
            spacing 10
            xalign 0.5
            imagebutton auto "ui/settings/windowed_%s.png" action [Preference("display", 0.71145833333), Play("sound", "se/open.ogg")] hovered Play("sound", "se/select.ogg")
            imagebutton auto "ui/settings/fullscreen_%s.png" action [Preference("display", "fullscreen"), Play("sound", "se/open.ogg")] hovered Play("sound", "se/select.ogg")

        null height 40

        add "ui/settings/transitions_title.png" xalign 0.5
        hbox:
            spacing 10
            xalign 0.5
            imagebutton auto "ui/settings/all_%s.png" action [Preference("transitions", "all"), Play("sound", "se/open.ogg")] hovered Play("sound", "se/select.ogg")
            imagebutton auto "ui/settings/none_%s.png" action [Preference("transitions", "none"), Play("sound", "se/open.ogg")] hovered Play("sound", "se/select.ogg")

        null height 40

        frame:
            style_group "pref"
            has vbox

            add "ui/settings/textspeed_title.png" xalign 0.5
            bar value Preference("text speed") xalign 0.5

screen preferences_2() tag preferences_screen:


    hbox:
        xalign 0.62 yalign 0.86
        spacing 30
        imagebutton auto "ui/navarrowleft_%s.png" action [Show("preferences_1", transition=dissolve), Play("sound", "se/open.ogg")] hovered Play("sound", "se/select.ogg") focus_mask True yalign 0.5
        imagebutton auto "ui/navbutton_%s.png" action [Show("preferences_1", transition=dissolve), Play("sound", "se/open.ogg")] hovered Play("sound", "se/select.ogg") focus_mask True yalign 0.5
        add "ui/navbutton_hover.png" yalign 0.5
        imagebutton auto "ui/navbutton_%s.png" action [Show("preferences_3", transition=dissolve), Play("sound", "se/open.ogg")] hovered Play("sound", "se/select.ogg") focus_mask True yalign 0.5
        imagebutton auto "ui/navarrowright_%s.png" action [Show('preferences_3', transition=dissolve), Play("sound", "se/open.ogg")] hovered Play("sound", "se/select.ogg") focus_mask True

    vbox:
        xalign 0.62
        ypos 250
        add "ui/settings/skip_title.png" xalign 0.5
        hbox:
            xalign 0.5
            spacing 10
            imagebutton auto "ui/settings/seenmessages_%s.png" action [Preference("skip", "seen"), Play("sound", "se/open.ogg")] hovered Play("sound", "se/select.ogg")
            imagebutton auto "ui/settings/allmessages_%s.png" action [Preference("skip", "all"), Play("sound", "se/open.ogg")] hovered Play("sound", "se/select.ogg")

        null height 40

        add "ui/settings/afterchoices_title.png" xalign 0.5
        hbox:
            xalign 0.5
            spacing 10
            imagebutton auto "ui/settings/stopskipping_%s.png" action [Preference("after choices", "stop"), Play("sound", "se/open.ogg")] hovered Play("sound", "se/select.ogg")
            imagebutton auto "ui/settings/keepskipping_%s.png" action [Preference("after choices", "skip"), Play("sound", "se/open.ogg")] hovered Play("sound", "se/select.ogg")

        null height 40

        frame:
            style_group "pref"
            has vbox

            add "ui/settings/autoforward_title.png" xalign 0.5
            bar value Preference("auto-forward time") xalign 0.5

            if config.has_voice:
                textbutton _("Wait for Voice") action Preference("wait for voice", "toggle")

screen preferences_3() tag preferences_screen:


    hbox:
        xalign 0.62 yalign 0.86
        spacing 30
        imagebutton auto "ui/navarrowleft_%s.png" action [Show("preferences_2", transition=dissolve), Play("sound", "se/open.ogg")] hovered Play("sound", "se/select.ogg") focus_mask True yalign 0.5
        imagebutton auto "ui/navbutton_%s.png" action [Show("preferences_1", transition=dissolve), Play("sound", "se/open.ogg")] hovered Play("sound", "se/select.ogg") focus_mask True yalign 0.5
        imagebutton auto "ui/navbutton_%s.png" action [Show("preferences_2", transition=dissolve), Play("sound", "se/open.ogg")] hovered Play("sound", "se/select.ogg") focus_mask True yalign 0.5
        add "ui/navbutton_hover.png" yalign 0.5
        add "ui/navarrowright_idle.png"

    vbox:
        xalign 0.62
        ypos 250
        frame:
            style_group "pref"
            has vbox

            add "ui/settings/musicvolume_title.png" xalign 0.5
            bar value Preference("music volume") xalign 0.5

        null height 40

        frame:
            style_group "pref"
            has vbox

            add "ui/settings/soundvolume_title.png" xalign 0.5
            bar value Preference("sound volume") xalign 0.5

            if config.sample_sound:
                textbutton _("Test"):
                    action Play("sound", config.sample_sound)
                    style "soundtest_button"

        if config.has_voice:
            frame:
                style_group "pref"
                has vbox

                label _("Voice Volume")
                bar value Preference("voice volume")

                textbutton _("Voice Sustain") action Preference("voice sustain", "toggle")
                if config.sample_voice:
                    textbutton _("Test"):
                        action Play("voice", config.sample_voice)
                        style "soundtest_button"

init -2:
    style pref_frame:
        background None







    style pref_button:
        size_group "pref"
        xalign 1.0

    style pref_slider:
        xysize (444,83)
        xalign 1.0
        left_bar "ui/bar_full.png"
        right_bar "ui/bar_empty.png"
        thumb "ui/bar_thumb.png"
        left_gutter 40
        right_gutter 40
        thumb_offset 9

    style soundtest_button:
        xalign 1.0








screen yesno_prompt(message, yes_action, no_action):

    modal True

    window at popup:
        background "ui/alert_window.png"
        xysize (1034,466)
        style_group "yesno"
        left_margin 0
        bottom_margin 0
        xpadding 0
        ypadding 0

        label _(message):
            xalign 0.5
            yalign 0.3

        hbox:
            yalign 0.8
            xalign 0.5
            spacing 150

            imagebutton auto "ui/yes_%s.png" action [yes_action, Play("sound", "se/open.ogg")] hovered Play("sound", "se/select.ogg")
            imagebutton auto "ui/no_%s.png" action [no_action, Play("sound", "se/open.ogg")] hovered Play("sound", "se/select.ogg")


    key "game_menu" action no_action

init -2:
    style yesno_button:
        size_group "yesno"
        background None

    style yesno_button_text is yesno_button:
        font "Lobster 1.4.otf"
        size 70
        hover_color "#0096ff"

    style yesno_label_text:
        text_align 0.5
        font "Lobster 1.4.otf"
        size 40
        layout "subtitle"








transform quick_menu_pop:
    alpha 0.0 yzoom 0.0
    linear 0.5 alpha 1.0 yzoom 1.0
    on hide:
        linear 0.5 alpha 0.0 yzoom 0.0

screen quick_menu():

    default tt = Tooltip("")

    if buttonpop:
        imagebutton auto "ui/quickmenu/home_%s.png" action [Hide('quick_menu_pop'), ToggleVariable('buttonpop', False)] hovered tt.Action("HIDE QUICK MENU") xalign 0.985 ypos 30
    else:
        imagebutton auto "ui/quickmenu/home_%s.png" action [Show('quick_menu_pop'), ToggleVariable('buttonpop', True)] hovered tt.Action("EXPAND QUICK MENU") xalign 0.985 ypos 30

    text tt.value xalign 0.93 ypos 42 text_align 1.0 color "#FFF" size 32 font "PoetsenOne-Regular.ttf"

screen quick_menu_pop():

    default tt = Tooltip("")

    text tt.value xalign 0.93 ypos 42 text_align 1.0 color "#FFF" size 32 font "PoetsenOne-Regular.ttf"

    vbox at quick_menu_pop:

        xalign 0.985
        ypos 125
        spacing 10
        imagebutton auto "ui/quickmenu/menu_%s.png" action [ShowMenu('navigation')] hovered tt.Action("NAVIGATION MENU")
        imagebutton auto "ui/quickmenu/skip_%s.png" action [Skip()] hovered tt.Action("SKIP")
        imagebutton auto "ui/quickmenu/auto_%s.png" action [Preference("auto-forward", "toggle")] hovered tt.Action("AUTO-FORWARD")
        imagebutton auto "ui/quickmenu/quicksave_%s.png" action QuickSave() hovered tt.Action("QUICK SAVE")
        imagebutton auto "ui/quickmenu/quickload_%s.png" action QuickLoad() hovered tt.Action("QUICK LOAD")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
