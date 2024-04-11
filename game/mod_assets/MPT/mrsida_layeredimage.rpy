layeredimage ida:
    at Flatten
    
    #####
    # If you're using Autofocus, uncomment the lines below and comment/remove the 'at Flatten' above
    #####
    #at AutofocusDisplayable(name="ida")
    #
    #group autofocus_coloring:
    #    attribute day default null
    #    attribute dawn null
    #    attribute sunset null
    #    attribute evening null
    #    attribute night null

    always "mod_assets/MPT/MrsIda/facebase.png"

    group outfit:
        attribute casual default null
        attribute yutaka null
    
    group eyes_color:
        attribute blue default null
        attribute green null
    
    group nose:
        attribute na default null
        attribute nb:
            "mod_assets/MPT/MrsIda/nose_b.png"        # sweat drop

    group mouth:
        attribute ma default:
            "mod_assets/MPT/MrsIda/mouth_a.png"       # smiling
        attribute mb:
            "mod_assets/MPT/MrsIda/mouth_b.png"       # talking + happy
        attribute mc:
            "mod_assets/MPT/MrsIda/mouth_c.png"       # talking + very happy
        attribute md:
            "mod_assets/MPT/MrsIda/mouth_d.png"       # closed
        attribute me:
            "mod_assets/MPT/MrsIda/mouth_e.png"       # closed + bit opened
        attribute mf:
            "mod_assets/MPT/MrsIda/mouth_f.png"       # showing teeth (angry?)
        attribute mg:
            "mod_assets/MPT/MrsIda/mouth_g.png"       # wide open (yelling / embarassed)

    group eyes:
        attribute ea default if_any(["blue"]):
            "mod_assets/MPT/MrsIda/eyes_a_blue.png" # neutral
        attribute ea default if_any(["green"]):
            "mod_assets/MPT/MrsIda/eyes_a_green.png"
        attribute eb:
            "mod_assets/MPT/MrsIda/eyes_b.png"        # closed
        attribute ec:
            "mod_assets/MPT/MrsIda/eyes_c.png"        # closed + happy
        attribute ed if_any(["blue"]):
            "mod_assets/MPT/MrsIda/eyes_d_blue.png" # crazy
        attribute ed if_any(["green"]):
            "mod_assets/MPT/MrsIda/eyes_d_green.png"

    group eyebrows:
        attribute ba default:
            "mod_assets/MPT/MrsIda/eyebrows_a.png"    # neutral
        attribute bb:
            "mod_assets/MPT/MrsIda/eyebrows_b.png"    # serious
        attribute bc:
            "mod_assets/MPT/MrsIda/eyebrows_c.png"    # raised eyebrow *vine boom*
        attribute bd:
            "mod_assets/MPT/MrsIda/eyebrows_d.png"    # surprised
        attribute be:
            "mod_assets/MPT/MrsIda/eyebrows_e.png"    # worried
        attribute bf:
            "mod_assets/MPT/MrsIda/eyebrows_f.png"    # anger

    group left:
        attribute ldown default if_any(["casual"]):
            "mod_assets/MPT/MrsIda/outfits/casual_ldown.png"
        attribute ldown default if_any(["yutaka"]):
            "mod_assets/MPT/MrsIda/outfits/yutaka_ldown.png"

        attribute lup if_any(["casual"]):
            "mod_assets/MPT/MrsIda/outfits/casual_lup.png"
        attribute lup if_any(["yutaka"]):
            "mod_assets/MPT/MrsIda/outfits/yutaka_lup.png"
    
    group right:
        attribute rdown default if_any(["casual"]):
            "mod_assets/MPT/MrsIda/outfits/casual_rdown.png"
        attribute rdown default if_any(["yutaka"]):
            "mod_assets/MPT/MrsIda/outfits/yutaka_rdown.png"

        attribute rhold if_any(["casual"]):
            "mod_assets/MPT/MrsIda/outfits/casual_rhold.png"
        attribute rhold if_any(["yutaka"]):
            "mod_assets/MPT/MrsIda/outfits/yutaka_rhold.png"
    
    