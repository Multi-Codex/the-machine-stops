image splash_sayori_background:
    alpha 0
    2.35
    "mod_assets/splashes/menu_bg_sayori.png"
    xtile 50 subpixel True
    crop_relative True
    yoffset -119.5
    crop (0.0,0.0,1.0,0.41)
    matrixcolor BrightnessMatrix(0.12)
    parallel:
        ease 0.25 alpha 1.0

    block:
        xoffset 0
        linear 80 xoffset -1280
        repeat

image splash_sayori_1:



    contains:
        truecenter
        subpixel True
        Solid("#0050ab")
        crop_relative True
        xanchor 0.0
        xoffset -640
        
        crop (0.0,0.0,0.0,0.070)
        parallel:
            ease 1 crop (0.0,0.0,1.1, 0.070)
        parallel:
            1
            easein_quint 1 zoom 15

    contains:
        0.15
        truecenter
        subpixel True
        Solid("#0075ce")
        crop_relative True
        xanchor 0.0
        xoffset -640
        
        crop (0.0,0.0,0.0,0.070)
        parallel:
            ease 1 crop (0.0,0.0,1.1, 0.070)
        parallel:
            1
            easein_quint 1 zoom 15


    contains:
        0.3
        truecenter
        subpixel True
        Solid("#00a2ff")
        crop_relative True
        xanchor 0.0
        xoffset -640
        crop (0.0,0.0,0.0,0.070)
        parallel:
            ease 1 crop (0.0,0.0,1.1, 0.070)
        parallel:
            1
            easein_quint 1 zoom 15

    contains:
        0.6
        subpixel True
        Solid("#89c0ff")
        crop_relative True
        xanchor 0.0
        yoffset -300
        crop (0.0,0.0,1.0, 0.195)
        ease 2 yoffset -30

    contains:
        0.6
        subpixel True
        Solid("#89c0ff")
        crop_relative True
        xanchor 0.0
        yoffset 900
        crop (0.0,0.0,1.0, 0.195)
        ease 2 yoffset 600

image splash_sayori_2:


    contains:
        2.95
        matrixcolor BrightnessMatrix(-0.25)
        "mod_assets/splashes/menu_art_s_blue.png"
        subpixel True
        truecenter
        
        alpha 0
        yoffset 300
        xoffset 370

        parallel:
            easein_quint 3 alpha 1.0 
        parallel:
            0.1
            ease 3 xoffset 415
            ease 3 xoffset 425
            ease 3 xoffset 427
            ease 3 xoffset 419
            repeat
        parallel:
            0.1
            ease 3 yoffset 305
            ease 3 yoffset 295
            ease 3 yoffset 301
            ease 3 yoffset 299
            repeat
        parallel:
            ease 10 rotate 2.5
            ease 10 rotate 0
            repeat
        parallel:
            ease 10 zoom 1.02
            ease 10 zoom 0.98
            repeat

    contains:
        2.9
        matrixcolor BrightnessMatrix(-0.1)
        "mod_assets/splashes/menu_art_s_blue.png"
        subpixel True
        truecenter
        
        alpha 0
        yoffset 300
        xoffset 370

        parallel:
            easein_quint 3 alpha 1.0 
        parallel:
            0.1
            ease 3 xoffset 390
            ease 3 xoffset 400
            repeat
        parallel:
            0.1
            ease 3 yoffset 308
            ease 3 yoffset 291
            repeat
        parallel:
            ease 10 rotate -2.5
            ease 10 rotate 0
            repeat
        parallel:
            ease 5 zoom 1.02
            ease 5 zoom 0.98
            repeat

    contains:
        1.75
        "mod_assets/splashes/menu_art_s_blue.png"
        subpixel True
        truecenter
        xoffset -600
        alpha 0
        yoffset 300
        easein_quint 1.75 xoffset 370 alpha 1
        parallel:
            ease 3 xoffset 365
            ease 3 xoffset 375
            ease 3 xoffset 371
            ease 3 xoffset 368 
            repeat
        parallel:
            ease 3 yoffset 305
            ease 3 yoffset 295
            ease 3 yoffset 301
            ease 3 yoffset 297 
            repeat
        parallel:
            ease 3 zoom 1.02
            ease 3 zoom 0.98
            repeat




    contains:
        2.20
        'sayori_name_blue'
        alpha 0
        subpixel True truecenter
        easein_quint 2 alpha 1 rotate 3 yoffset -15 zoom 1.1
        block:
            ease 3 zoom 1.14
            ease 3 zoom 1.1
            repeat

    contains:
        2.30
        'sayori_name_blue_2'
        alpha 0
        subpixel True truecenter
        easein_quint 2 alpha 1 rotate -3 yoffset 45 zoom 1.1
        block:
            ease 3 zoom 1.14
            ease 3 zoom 1.1
            repeat   

    contains:
        2.20
        Solid("#ffffff")
        easeout 0.75 alpha 0
        time 2.20
        alpha 1
        linear 0.5 alpha 0

    contains:
        2.25
        truecenter
        subpixel True
        yoffset 250
        xoffset 200
        ParticleBurst("gui/menu_particle.png", explodeTime=0, numParticles=40, particleTime=2.0, particleXSpeed=3, particleYSpeed=3).sm
        particle_fadeout



image sayori_name_blue:  
    
    truecenter subpixel True
    yoffset 0
    xoffset -375
    
    Text("Day 1", size=50, slow_cps=0,  color="fff", insensitive_outlines=[(4, "#0085eb", 0, 0), (2, "#0085eb", 2, 2)], outlines=[(4, text_outline_color, 0, 0), (2, text_outline_color, 2, 2)])

image sayori_name_blue_2:  
    
    truecenter subpixel True
    yoffset 30
    xoffset -375
    
    Text("Ohayou!", size=50, slow_cps=0,  color="fff", insensitive_outlines=[(4, "#0085eb", 0, 0), (2, "#0085eb", 2, 2)], outlines=[(4, text_outline_color, 0, 0), (2, text_outline_color, 2, 2)])






# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


image splash_yuri_background:
    alpha 0
    2.35
    "mod_assets/splashes/menu_bg_yuri.png"
    xtile 50 subpixel True
    crop_relative True
    yoffset -119.5
    crop (0.0,0.0,1.0,0.41)
    matrixcolor BrightnessMatrix(0.12)
    parallel:
        ease 0.25 alpha 1.0

    block:
        xoffset 0
        linear 80 xoffset -1280
        repeat

image splash_yuri_1:



    contains:
        truecenter
        subpixel True
        Solid("#b833ff") 
        crop_relative True
        xanchor 0.0
        xoffset -640
        
        crop (0.0,0.0,0.0,0.070)
        parallel:
            ease 1 crop (0.0,0.0,1.1, 0.070)
        parallel:
            1
            easein_quint 1 zoom 15

    contains:
        0.15
        truecenter
        subpixel True
        Solid("#8a0afa")
        crop_relative True
        xanchor 0.0
        xoffset -640
        
        crop (0.0,0.0,0.0,0.070)
        parallel:
            ease 1 crop (0.0,0.0,1.1, 0.070)
        parallel:
            1
            easein_quint 1 zoom 15


    contains:
        0.3
        truecenter
        subpixel True
        Solid("#9962de")
        crop_relative True
        xanchor 0.0
        xoffset -640
        crop (0.0,0.0,0.0,0.070)
        parallel:
            ease 1 crop (0.0,0.0,1.1, 0.070)
        parallel:
            1
            easein_quint 1 zoom 15

    contains:
        0.6
        subpixel True
        Solid("#BF8DFE")
        crop_relative True
        xanchor 0.0
        yoffset -300
        crop (0.0,0.0,1.0, 0.195)
        ease 2 yoffset -30

    contains:
        0.6
        subpixel True
        Solid("#BF8DFE")
        crop_relative True
        xanchor 0.0
        yoffset 900
        crop (0.0,0.0,1.0, 0.195)
        ease 2 yoffset 600

image splash_yuri_2:


    contains:
        2.95
        matrixcolor BrightnessMatrix(-0.25)
        "mod_assets/splashes/menu_art_y_purple.png"
        subpixel True
        truecenter
        
        alpha 0
        yoffset 300
        xoffset 370

        parallel:
            easein_quint 3 alpha 1.0 
        parallel:
            0.1
            ease 3 xoffset 415
            ease 3 xoffset 425
            ease 3 xoffset 427
            ease 3 
            repeat
        parallel:
            0.1
            ease 3 yoffset 305
            ease 3 yoffset 295
            ease 3 yoffset 301
            ease 3 yoffset 299
            repeat
        parallel:
            ease 10 rotate 2.5
            ease 10 rotate 0
            repeat
        parallel:
            ease 10 zoom 1.02
            ease 10 zoom 0.98
            repeat

    contains:
        2.9
        matrixcolor BrightnessMatrix(-0.1)
        "mod_assets/splashes/menu_art_y_purple.png"
        subpixel True
        truecenter
        
        alpha 0
        yoffset 300
        xoffset 370

        parallel:
            easein_quint 3 alpha 1.0 
        parallel:
            0.1
            ease 3 xoffset 390
            ease 3 xoffset 400
            repeat
        parallel:
            0.1
            ease 3 yoffset 308
            ease 3 yoffset 291
            repeat
        parallel:
            ease 10 rotate -2.5
            ease 10 rotate 0
            repeat
        parallel:
            ease 5 zoom 1.02
            ease 5 zoom 0.98
            repeat

    contains:
        1.75
        "mod_assets/splashes/menu_art_y_purple.png"
        subpixel True
        truecenter
        xoffset -600
        alpha 0
        yoffset 300
        easein_quint 1.75 xoffset 370 alpha 1
        parallel:
            ease 3 xoffset 365
            ease 3 xoffset 375
            ease 3 xoffset 371
            ease 3 xoffset 368 
            repeat
        parallel:
            ease 3 yoffset 305
            ease 3 yoffset 295
            ease 3 yoffset 301
            ease 3 yoffset 297 
            repeat
        parallel:
            ease 3 zoom 1.02
            ease 3 zoom 0.98
            repeat




    contains:
        2.20
        'yuri_name_purple'
        alpha 0
        subpixel True truecenter
        easein_quint 2 alpha 1 rotate 3 yoffset -15 zoom 1.1
        block:
            ease 3 zoom 1.14
            ease 3 zoom 1.1
            repeat

    contains:
        2.30
        'yuri_name_purple_2'
        alpha 0
        subpixel True truecenter
        easein_quint 2 alpha 1 rotate -3 yoffset 45 zoom 1.1
        block:
            ease 3 zoom 1.14
            ease 3 zoom 1.1
            repeat   

    contains:
        2.20
        Solid("#ffffff")
        easeout 0.75 alpha 0
        time 2.20
        alpha 1
        linear 0.5 alpha 0

    contains:
        2.25
        truecenter
        subpixel True
        yoffset 250
        xoffset 200
        ParticleBurst("gui/menu_particle.png", explodeTime=0, numParticles=40, particleTime=2.0, particleXSpeed=3, particleYSpeed=3).sm
        particle_fadeout



image yuri_name_purple:  
    
    truecenter subpixel True
    yoffset 0
    xoffset -375
    
    Text("Day 2", size=50, slow_cps=0,  color="#fff", insensitive_outlines=[(4, "#9962de", 0, 0), (2, "#9962de", 2, 2)], outlines=[(4, text_outline_color, 0, 0), (2, text_outline_color, 2, 2)])

image yuri_name_purple_2:  
    
    truecenter subpixel True
    yoffset 30
    xoffset -375
    
    Text("Silver Lining", size=50, slow_cps=0,  color="fff", insensitive_outlines=[(4, "#9962de", 0, 0), (2, "#9962de", 2, 2)], outlines=[(4, text_outline_color, 0, 0), (2, text_outline_color, 2, 2)])





# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------




image splash_monika_background:
    alpha 0
    2.35
    "mod_assets/splashes/menu_bg_monika.png"
    xtile 50 subpixel True
    crop_relative True
    yoffset -119.5
    crop (0.0,0.0,1.0,0.41)
    matrixcolor BrightnessMatrix(0.12)
    parallel:
        ease 0.25 alpha 1.0

    block:
        xoffset 0
        linear 80 xoffset 1280
        repeat

image splash_monika_1:



    contains:
        truecenter
        subpixel True
        Solid("#268E1E") 
        crop_relative True
        xanchor 1
        xoffset -640
        
        crop (0.0,0.0,0.0,0.070)
        parallel:
            ease 1 crop (0.0,0.0,1.1, 0.070)
        parallel:
            1
            easein_quint 1 zoom 15

    contains:
        0.15
        truecenter
        subpixel True
        Solid("#35BB2A")
        crop_relative True
        xanchor 1
        xoffset -640
        
        crop (0.0,0.0,0.0,0.070)
        parallel:
            ease 1 crop (0.0,0.0,1.1, 0.070)
        parallel:
            1
            easein_quint 1 zoom 15


    contains:
        0.3
        truecenter
        subpixel True
        Solid("#6BD562")
        crop_relative True
        xanchor 1
        xoffset -640
        crop (0.0,0.0,0.0,0.070)
        parallel:
            ease 1 crop (0.0,0.0,1.1, 0.070)
        parallel:
            1
            easein_quint 1 zoom 15

    contains:
        0.6
        subpixel True
        Solid("#6FE865")
        crop_relative True
        xanchor 0.0
        yoffset -300
        crop (0.0,0.0,1.0, 0.195)
        ease 2 yoffset -30

    contains:
        0.6
        subpixel True
        Solid("#6FE865")
        crop_relative True
        xanchor 0.0
        yoffset 900
        crop (0.0,0.0,1.0, 0.195)
        ease 2 yoffset 600

image splash_monika_2:


    contains:
        2.95
        matrixcolor BrightnessMatrix(-0.35)
        "mod_assets/splashes/menu_art_m_green.png"
        subpixel True
        truecenter
        
        alpha 0
        yoffset 300
        xoffset -290

        parallel:
            easein_quint 3 alpha 1.0 
        parallel:
            0.1
            ease 3 xoffset -325
            ease 3 xoffset -330
            ease 3 xoffset -320
            ease 3 xoffset -335
            repeat
        parallel:
            0.1
            ease 3 yoffset 305
            ease 3 yoffset 295
            ease 3 yoffset 301
            ease 3 yoffset 299
            repeat
        parallel:
            ease 10 rotate 2.5
            ease 10 rotate 0
            repeat
        parallel:
            ease 10 zoom 1.02
            ease 10 zoom 0.98
            repeat

    contains:
        2.9
        matrixcolor BrightnessMatrix(-0.2)
        "mod_assets/splashes/menu_art_m_green.png"
        subpixel True
        truecenter
        
        alpha 0
        yoffset 300
        xoffset -290

        parallel:
            easein_quint 3 alpha 1.0 
        parallel:
            0.1
            ease 5 xoffset -310
            ease 3 xoffset -300
            ease 4 xoffset -295
            ease 3 xoffset -305
            repeat
        parallel:
            0.1
            ease 3 yoffset 308
            ease 3 yoffset 291
            repeat
        parallel:
            ease 10 rotate -2.5
            ease 10 rotate 0
            repeat
        parallel:
            ease 5 zoom 1.02
            ease 5 zoom 0.98
            repeat

    contains:
        1.75
        matrixcolor BrightnessMatrix(-0.1)
        "mod_assets/splashes/menu_art_m_green.png"
        subpixel True
        truecenter
        xoffset 800
        alpha 0
        yoffset 300
        easein_quint 1.75 xoffset -290 alpha 1
        parallel:
            ease 3 xoffset -285
            ease 3 xoffset -295
            ease 3 xoffset -300
            ease 3 xoffset -290
            repeat
        parallel:
            ease 3 yoffset 305
            ease 3 yoffset 295
            ease 3 yoffset 301
            ease 3 yoffset 297 
            repeat
        parallel:
            ease 6 zoom 1.02
            ease 4 zoom 0.98
            repeat




    contains:
        2.20
        'monika_name_green'
        alpha 0
        subpixel True truecenter
        easein_quint 2 alpha 1 rotate -3 yoffset -15 zoom 1.1
        block:
            ease 3 zoom 1.14
            ease 3 zoom 1.1
            repeat

    contains:
        2.30
        'monika_name_green_2'
        alpha 0
        subpixel True truecenter
        easein_quint 2 alpha 1 rotate 3 yoffset 45 zoom 1.1
        block:
            ease 3 zoom 1.14
            ease 3 zoom 1.1
            repeat   

    contains:
        2.20
        Solid("#ffffff")
        easeout 0.75 alpha 0
        time 2.20
        alpha 1
        linear 0.5 alpha 0

    contains:
        2.25
        truecenter
        subpixel True
        yoffset 250
        xoffset 915
        ParticleBurst("gui/menu_particle.png", explodeTime=0, numParticles=40, particleTime=2.0, particleXSpeed=3, particleYSpeed=3).sm
        particle_fadeout



image monika_name_green:  
    
    truecenter subpixel True
    yoffset 0
    xoffset 375
    
    Text("Day 3", size=50, slow_cps=0,  color="#fff", insensitive_outlines=[(4, "#45AA3C", 0, 0), (2, "#45AA3C", 2, 2)], outlines=[(4, text_outline_color, 0, 0), (2, text_outline_color, 2, 2)])

image monika_name_green_2:  
    
    truecenter subpixel True
    yoffset 30
    xoffset 375
    
    Text("Reconcile", size=50, slow_cps=0,  color="fff", insensitive_outlines=[(4, "#45AA3C", 0, 0), (2, "#45AA3C", 2, 2)], outlines=[(4, text_outline_color, 0, 0), (2, text_outline_color, 2, 2)])

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------





image splash_natsuki_background:
    alpha 0
    2.35
    "mod_assets/splashes/menu_bg_natsuki.png"
    xtile 50 subpixel True
    crop_relative True
    yoffset -119.5
    crop (0.0,0.0,1.0,0.41)
    matrixcolor BrightnessMatrix(0.12)
    parallel:
        ease 0.25 alpha 1.0

    block:
        xoffset 0
        linear 80 xoffset 1280
        repeat

image splash_natsuki_1:



    contains:
        truecenter
        subpixel True
        Solid("#F85BFF") 
        crop_relative True
        xanchor 1
        xoffset -640
        
        crop (0.0,0.0,0.0,0.070)
        parallel:
            ease 1 crop (0.0,0.0,1.1, 0.070)
        parallel:
            1
            easein_quint 1 zoom 15

    contains:
        0.15
        truecenter
        subpixel True
        Solid("#F526FF")
        crop_relative True
        xanchor 1
        xoffset -640
        
        crop (0.0,0.0,0.0,0.070)
        parallel:
            ease 1 crop (0.0,0.0,1.1, 0.070)
        parallel:
            1
            easein_quint 1 zoom 15


    contains:
        0.3
        truecenter
        subpixel True
        Solid("#FA94FF")
        crop_relative True
        xanchor 1
        xoffset -640
        crop (0.0,0.0,0.0,0.070)
        parallel:
            ease 1 crop (0.0,0.0,1.1, 0.070)
        parallel:
            1
            easein_quint 1 zoom 15

    contains:
        0.6
        subpixel True
        Solid("#FBA1FF")
        crop_relative True
        xanchor 0.0
        yoffset -300
        crop (0.0,0.0,1.0, 0.195)
        ease 2 yoffset -30

    contains:
        0.6
        subpixel True
        Solid("#FBA1FF")
        crop_relative True
        xanchor 0.0
        yoffset 900
        crop (0.0,0.0,1.0, 0.195)
        ease 2 yoffset 600

image splash_natsuki_2:


    contains:
        2.95
        matrixcolor BrightnessMatrix(-0.25)
        "mod_assets/splashes/menu_art_n_pink.png"
        subpixel True
        truecenter
        
        alpha 0
        yoffset 300
        xoffset -290

        parallel:
            easein_quint 3 alpha 1.0 
        parallel:
            0.1
            ease 3 xoffset -325
            ease 3 xoffset -330
            ease 3 xoffset -320
            ease 3 xoffset -335
            repeat
        parallel:
            0.1
            ease 3 yoffset 305
            ease 3 yoffset 295
            ease 3 yoffset 301
            ease 3 yoffset 299
            repeat
        parallel:
            ease 10 rotate 2.5
            ease 10 rotate 0
            repeat
        parallel:
            ease 10 zoom 1.02
            ease 10 zoom 0.98
            repeat

    contains:
        2.9
        matrixcolor BrightnessMatrix(-0.1)
        "mod_assets/splashes/menu_art_n_pink.png"
        subpixel True
        truecenter
        
        alpha 0
        yoffset 300
        xoffset -290

        parallel:
            easein_quint 3 alpha 1.0 
        parallel:
            0.1
            ease 5 xoffset -310
            ease 3 xoffset -300
            ease 4 xoffset -295
            ease 3 xoffset -305
            repeat
        parallel:
            0.1
            ease 3 yoffset 308
            ease 3 yoffset 291
            repeat
        parallel:
            ease 10 rotate -2.5
            ease 10 rotate 0
            repeat
        parallel:
            ease 5 zoom 1.02
            ease 5 zoom 0.98
            repeat

    contains:
        1.75

        "mod_assets/splashes/menu_art_n_pink.png"
        subpixel True
        truecenter
        xoffset 800
        alpha 0
        yoffset 300
        easein_quint 1.75 xoffset -290 alpha 1
        parallel:
            ease 3 xoffset -285
            ease 3 xoffset -295
            ease 3 xoffset -300
            ease 3 xoffset -290
            repeat
        parallel:
            ease 3 yoffset 305
            ease 3 yoffset 295
            ease 3 yoffset 301
            ease 3 yoffset 297 
            repeat
        parallel:
            ease 6 zoom 1.02
            ease 4 zoom 0.98
            repeat




    contains:
        2.20
        'natsuki_name_pink'
        alpha 0
        subpixel True truecenter
        easein_quint 2 alpha 1 rotate -3 yoffset -15 zoom 1.1
        block:
            ease 3 zoom 1.14
            ease 3 zoom 1.1
            repeat

    contains:
        2.30
        'natsuki_name_pink_2'
        alpha 0
        subpixel True truecenter
        easein_quint 2 alpha 1 rotate 3 yoffset 45 zoom 1.1
        block:
            ease 3 zoom 1.14
            ease 3 zoom 1.1
            repeat   

    contains:
        2.20
        Solid("#ffffff")
        easeout 0.75 alpha 0
        time 2.20
        alpha 1
        linear 0.5 alpha 0

    contains:
        2.25
        truecenter
        subpixel True
        yoffset 250
        xoffset 915
        ParticleBurst("gui/menu_particle.png", explodeTime=0, numParticles=40, particleTime=2.0, particleXSpeed=3, particleYSpeed=3).sm
        particle_fadeout



image natsuki_name_pink:  
    
    truecenter subpixel True
    yoffset 0
    xoffset 375
    
    Text("Tuesday", size=50, slow_cps=0,  color="#fff", insensitive_outlines=[(4, "#F870FF", 0, 0), (2, "#F870FF", 2, 2)], outlines=[(4, text_outline_color, 0, 0), (2, text_outline_color, 2, 2)])

image natsuki_name_pink_2:  
    
    truecenter subpixel True
    yoffset 30
    xoffset 375
    
    Text("Day 1", size=50, slow_cps=0,  color="fff", insensitive_outlines=[(4, "#F870FF", 0, 0), (2, "#F870FF", 2, 2)], outlines=[(4, text_outline_color, 0, 0), (2, text_outline_color, 2, 2)])




# This is what you should put in the script for it to work and show.

    # menu:
        # "Sayori":
            
            # show splash_sayori_1
            # show splash_sayori_background
            # show splash_sayori_2
            # pause 
            # hide splash_sayori_1
            # hide splash_sayori_background
            # hide splash_sayori_2
            
        # "Yuri":
            # show splash_yuri_1
            # show splash_yuri_background
            # show splash_yuri_2
            # pause
            # hide splash_yuri_1
            # hide splash_yuri_background
            # hide splash_yuri_2
    
        # "Monika":
            # show splash_monika_1
            # show splash_monika_background
            # show splash_monika_2
            # pause
            # hide splash_monika_1
            # hide splash_monika_background
            # hide splash_monika_2

        # "Natsuki":
            # show splash_natsuki_1
            # show splash_natsuki_background
            # show splash_natsuki_2
            # pause 
            # hide splash_natsuki_1
            # hide splash_natsuki_background
            # hide splash_natsuki_2







