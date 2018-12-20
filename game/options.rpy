








init -1 python hide:





    config.developer = False
    config.autoreload = False



    config.screen_width = 1920
    config.screen_height = 1080




    config.window_title = u"HSR: Magi Trials"



    config.name = "HSR Magi Trials"
    config.version = "1.3"

    config.quit_action = Quit(confirm=True)










    theme.threeD(
        
        

        
        widget = "#898989",

        
        widget_hover = "#464646",

        
        widget_text = "#FFF",

        
        
        widget_selected = "#FFF",

        
        disabled = "#898989",

        
        disabled_text = "#FFF",

        
        label = "#FFF",

        
        frame = "#252525",

        
        
        
        mm_root = "#393939",

        
        
        
        gm_root = "#393939",

        
        
        rounded_window = False,

        
        
        
        )










    style.window.background = "ui/dialogbox.png"












    style.window.left_padding = 300
    style.window.right_padding = 400
    style.window.top_padding = 100





    style.window.yminimum = 339



























    style.default.font = "Lobster 1.4.otf"



    style.default.size = 42











    config.has_sound = True



    config.has_music = True



    config.has_voice = False

















    config.main_menu_music = "music/maintheme.ogg"












    config.help = "README.html"



    config.window_icon = "ui/icon.ico"





    config.enter_transition = None


    config.exit_transition = None


    config.intra_transition = None


    config.main_game_transition = None


    config.game_main_transition = None


    config.end_splash_transition = None


    config.end_game_transition = None


    config.after_load_transition = None


    config.window_show_transition = None


    config.window_hide_transition = None


    config.adv_nvl_transition = dissolve


    config.nvl_adv_transition = dissolve


    config.enter_yesno_transition = None


    config.exit_yesno_transition = None


    config.enter_replay_transition = None


    config.exit_replay_transition = None


    config.say_attribute_transition = None





python early:
    config.save_directory = "HSR-Magi-Trials"

init -1 python hide:









    config.default_fullscreen = False



    config.default_text_cps = 10



    config.default_afm_time = 10




    style.default.color = "#FFF"
    style.default.outlines = [(2, "#000", 0, 0)]


    style.say_label.size = 72
    style.say_label.bold = False
    style.say_label.drop_shadow = (1,1)


    config.thumbnail_width = 192
    config.thumbnail_height = 108


    style.say_label.size = 70
    style.say_label.bold = False
    style.say_label.font = "PoetsenOne-Regular.ttf"
    style.say_label.outlines = [(2, "#FFF", 0, 0)]
    style.say_label.drop_shadow = (4,4)

    style.say_who_window.background = None
    style.say_who_window.xanchor = 0.0
    style.say_who_window.xpos = 0
    style.say_who_window.ypos = 830



init python:




    build.directory_name = "HSR-Magi-Trials-1.3"




    build.executable_name = "MagiTrials"



    build.include_update = False





























    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)
    build.classify("**.rpy", None)
    build.classify("**.psd", None)
    build.classify('game/ep2/**', None)
    build.classify('game/ep3/**', None)
    build.classify('game/ep4/**', None)



    build.classify('game/**.rpyb', 'archive')
    build.classify('game/**.rpyc', 'archive')
    build.classify('game/**.ttf', 'archive')
    build.classify('game/**.otf', 'archive')
    build.classify('game/**.ico', 'archive')
    build.classify('game/**.icns', 'archive')
    build.classify('game/**.png', 'archive')
    build.classify('game/**.jpg', 'archive')
    build.classify('game/**.ogg', 'archive')
    build.classify('game/**.ogv', 'archive')




    build.documentation('*.html')
    build.documentation('*.txt')
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
