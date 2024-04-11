## definitions.rpy

# This file defines important stuff for DDLC and your mod!

# This variable declares if the mod is a demo or not.
# Leftover from DDLC.
define persistent.demo = False

# This variable declares whether the mod is in the 'steamapps' folder.
define persistent.steam = ("steamapps" in config.basedir.lower())

# This variable declares whether Developer Mode is on or off in the mod.
define config.developer = False

# This python statement starts singleton to make sure only one copy of the mod
# is running.
python early:
    import singleton
    me = singleton.SingleInstance()

init -3 python:
    ## Dynamic Super Position (DSP)
    # DSP is a feature in where the game upscales the positions of assets 
    # with higher resolutions (1080p).
    # This is just simple division from Adobe, implemented in Python.
    def dsp(orig_val):
        ceil = not isinstance(orig_val, float)
        dsp_scale = config.screen_width / 1280.0
        if ceil: return math.ceil(orig_val * dsp_scale)
        else: return orig_val * dsp_scale

    ## Dynamic Super Resolution
    # DSR is a feature in where the game upscales asset sizes to higher
    # resolutions (1080p) and sends back a modified transform.
    # (Recommend that you just make higher res assets than upscale lower res ones)
    class DSR:
        def __call__(self, path):
            img_bounds = renpy.image_size(path)
            return Transform(path, size=(dsp(img_bounds[0]), dsp(img_bounds[1])))

    dsr = DSR()

# This init python statement sets up the functions, keymaps and channels
# for the game.
init python:
    # These variable declarations adjusts the mapping for certain actions in-game.
    config.keymap['game_menu'].remove('mouseup_3')
    config.keymap['hide_windows'].append('mouseup_3')
    config.keymap['self_voicing'] = []
    config.keymap['clipboard_voicing'] = []
    config.keymap['toggle_skip'] = []

    # This variable declaration registers the music poem channel for the poem sharing music.
    renpy.music.register_channel("music_poem", mixer="music", tight=True)
    
    # This function gets the postition of the music playing in a given channel.
    def get_pos(channel='music'):
        pos = renpy.music.get_pos(channel=channel)
        if pos: return pos
        return 0

    # This function deletes all the saves made in the mod.
    def delete_all_saves():
        for savegame in renpy.list_saved_games(fast=True):
            renpy.unlink_save(savegame)

    # This function deletes a given character name from the characters folder.
    def delete_character(name):
        if renpy.android:
            try: os.remove(os.environ['ANDROID_PUBLIC'] + "/characters/" + name + ".chr")
            except: pass
        else:
            try: os.remove(config.basedir + "/characters/" + name + ".chr")
            except: pass

    # These functions restores all the character CHR files to the characters folder 
    # given the playthrough number in the mod and list of characters to restore.
    def restore_character(names):
        if not isinstance(names, list):
            raise Exception("'names' parameter must be a list. Example: [\"monika\", \"sayori\"].")

        for x in names:
            if renpy.android:
                try: renpy.file(os.environ['ANDROID_PUBLIC'] + "/characters/" + x + ".chr")
                except: open(os.environ['ANDROID_PUBLIC'] + "/characters/" + x + ".chr", "wb").write(renpy.file("chrs/" + x + ".chr").read())
            else:
                try: renpy.file(config.basedir + "/characters/" + x + ".chr")
                except: open(config.basedir + "/characters/" + x + ".chr", "wb").write(renpy.file("chrs/" + x + ".chr").read())

    def restore_all_characters():
        if persistent.playthrough == 0:
            restore_character(["monika", "sayori", "natsuki", "yuri"])
        elif persistent.playthrough == 1 or persistent.playthrough == 2:
            restore_character(["monika", "natsuki", "yuri"])
        elif persistent.playthrough == 3:
            restore_character(["monika"])
        else:
            restore_character(["sayori", "natsuki", "yuri"])
    
    # This function is obsolete as all characters now restores only
    # relevant characters to the characters folder.
    def restore_relevant_characters():
        restore_all_characters()

    # This function pauses the time for a certain amount of time or indefinite.
    def pause(time=None):
        global _windows_hidden

        if not time:
            _windows_hidden = True
            renpy.ui.saybehavior(afm=" ")
            renpy.ui.interact(mouse='pause', type='pause', roll_forward=None)
            _windows_hidden = False
            return
        if time <= 0: return
        _windows_hidden = True
        renpy.pause(time)
        _windows_hidden = False

## Music
# This section declares the music available to be played in the mod.
# Syntax:
#   audio. - This tells Ren'Py this is a audio variable.
#   t1 - This tells Ren'Py the label of the music/sound file being declared.
#   <loop 22.073> - This tells Ren'Py to loop the music/sound to this position when the song completes.
#   "bgm/1.ogg" - This tells Ren'Py the path of the music/sound file to use.
# Example: 
#   define audio.t2 = "bgm/2.ogg"

define audio.t1 = "<loop 22.073>bgm/1.ogg" # Doki Doki Literature Club! - Main Theme
define audio.t2 = "<loop 4.499>bgm/2.ogg" # Ohayou Sayori! - Sayori Theme
define audio.t2g = "bgm/2g.ogg"
define audio.t2g2 = "<from 4.499 loop 4.499>bgm/2.ogg"
define audio.t2g3 = "<loop 4.492>bgm/2g2.ogg"
define audio.t3 = "<loop 4.618>bgm/3.ogg" # Main Theme - In Game 
define audio.t3g = "<to 15.255>bgm/3g.ogg"
define audio.t3g2 = "<from 15.255 loop 4.618>bgm/3.ogg"
define audio.t3g3 = "<loop 4.618>bgm/3g2.ogg"
define audio.t3m = "<loop 4.618>bgm/3.ogg"
define audio.t4 = "<loop 19.451>bgm/4.ogg" # Dreams of Love and Literature - Poem Game Theme
define audio.t4g = "<loop 1.000>bgm/4g.ogg"
define audio.t5 = "<loop 4.444>bgm/5.ogg" # Okay Everyone! - Sharing Poems Theme

define audio.tmonika = "<loop 4.444>bgm/5_monika.ogg" # Okay Everyone! (Monika)
define audio.tsayori = "<loop 4.444>bgm/5_sayori.ogg" # Okay Everyone! (Sayori)
define audio.tnatsuki = "<loop 4.444>bgm/5_natsuki.ogg" # Okay Everyone! (Natsuki)
define audio.tyuri = "<loop 4.444>bgm/5_yuri.ogg" # Okay Everyone! (Yuri)

define audio.t5b = "<loop 4.444>bgm/5.ogg"
define audio.t5c = "<loop 4.444>bgm/5.ogg"
define audio.t6 = "<loop 10.893>bgm/6.ogg" # Play With Me - Yuri/Natsuki Theme
define audio.t6g = "<loop 10.893>bgm/6g.ogg"
define audio.t6r = "<to 39.817 loop 0>bgm/6r.ogg"
define audio.t6s = "<loop 43.572>bgm/6s.ogg"
define audio.t7 = "<loop 2.291>bgm/7.ogg" # Poem Panic - Argument Theme
define audio.t7a = "<loop 4.316 to 12.453>bgm/7.ogg"
define audio.t7g = "<loop 31.880>bgm/7g.ogg"
define audio.t8 = "<loop 9.938>bgm/8.ogg" # Daijoubu! - Argument Resolved Theme
define audio.t9 = "<loop 3.172>bgm/9.ogg" # My Feelings - Emotional Theme
define audio.t9g = "<loop 1.532>bgm/9g.ogg" # My Feelings but 207% Speed
define audio.t10 = "<loop 5.861>bgm/10.ogg" # My Confession - Sayori Confession Theme
define audio.t10y = "<loop 0>bgm/10-yuri.ogg"
define audio.td = "<loop 36.782>bgm/d.ogg"

define audio.m1 = "<loop 0>bgm/m1.ogg" # Just Monika. - Just Monika.
define audio.mend = "<loop 6.424>bgm/monika-end.ogg" # I Still Love You - Monika Post-Delete Theme

#Custom Music
define audio.t11 = "mod_assets/custom_music/Love_In_Glacier.ogg"
define audio.casual = "mod_assets/custom_music/Casual.wav"
define audio.iris = "mod_assets/custom_music/Iris.mp3"
define audio.chasecars = "mod_assets/custom_music/chasingcars.mp3"
define audio.midroom = "mod_assets/custom_music/midroom.mp3"
define audio.surround = "mod_assets/custom_music/surrounded.mp3"

##EM:R Music

define audio.motionpicturesoundtrack1 = "<from 0 to 199.592 loop 39.184>mod_assets/custom_music/motionpicturesoundtrack.ogg"
define audio.yawa = "<from 0 to 210.010 loop 105.696>mod_assets/custom_music/youandwhosearmy.ogg"
define audio.setmyselfonfire = "<from 0 to 146.213 loop 12.346>mod_assets/custom_music/setmyselfonfire.ogg"
define audio.truelovewaits = "<from 0 to 261.176 loop 7.059>mod_assets/custom_music/truelovewaits.ogg"

## WIP
#define audio.houseofcards = "<loop 0>mod_assets/custom_music/houseofcards.ogg"

## BONUS
define audio.trulovwaits = "<loop 0>mod_assets/custom_music/trulovwaits.ogg"
define audio.creep = "<loop 0>mod_assets/custom_music/creep xD.ogg"


#Custom SFX
define audio.newhov= "mod_assets/custom_music/hover.ogg"
define audio.newsel= "mod_assets/custom_music/select.ogg"
define audio.glitch4 = "mod_assets/custom_music/heavg.mp3"
define audio.transmoni = "mod_assets/custom_music/transition_m.ogg"
define audio.transnat = "mod_assets/custom_music/transition_n.ogg"
define audio.transsayo = "mod_assets/custom_music/transition_s.ogg"
define audio.transyuri = "mod_assets/custom_music/transition_y.ogg"
define audio.alarm = "mod_assets/custom_music/alarmnat.ogg"

define audio.ghostmenu = "<loop 0>bgm/ghostmenu.ogg"
define audio.g1 = "<loop 0>bgm/g1.ogg"
define audio.g2 = "<loop 0>bgm/g2.ogg"
define audio.hb = "<loop 0>bgm/heartbeat.ogg"

define audio.closet_open = "sfx/closet-open.ogg"
define audio.closet_close = "sfx/closet-close.ogg"
define audio.page_turn = "sfx/pageflip.ogg"
define audio.fall = "sfx/fall.ogg"

## Backgrounds
# This section declares the backgrounds available to be shown in the mod.
# To define a new color background, declare a new image statement like in this example:
#     image blue = "X" where X is your color hex i.e. '#158353'
# To define a new background, declare a new image statement like this instead:
#     image bg bathroom = "mod_assets/bathroom.png" 

image black = "#000000"
image dark = "#000000e4"
image darkred = "#110000c8"
image white = "#ffffff"
image splash = "bg/splash.png"
image end:
    truecenter
    "gui/end.png"

image bg residential_day = "bg/residential.png" # Start of DDLC BG
image bg class_day = "bg/class.png" # The classroom BG
image bg corridor = "bg/corridor.png" # The hallway BG
image bg club_day = "bg/club.png" # The club BG
image bg club_day2: # Glitched Club BG
    choice:
        "bg club_day"
    choice:
        "bg club_day"
    choice:
        "bg club_day"
    choice:
        "bg club_day"
    choice:
        "bg club_day"
    choice:
        "bg/club-skill.png"

image bg closet = "bg/closet.png" # The closet BG
image bg bedroom = "bg/bedroom.png" # MC's Room BG
image bg sayori_bedroom = "bg/sayori_bedroom.png" # Sayori's Room BG
image bg house = "bg/house.png" # Sayori's House BG
image bg kitchen = "bg/kitchen.png" # MC's Kitchen BG

image bg notebook = "bg/notebook.png" # Poem Game Notebook Scene
image bg notebook-glitch = "bg/notebook-glitch.png" # Glitched Poem Game BG

#Custom BGs
image bg void = "mod_assets/custom_bg/void.png" #The Void/Digital Prison
image bg yuri = "mod_assets/custom_bg/yurijump.png" #Yuri Jumpscare
image bg school = "mod_assets/custom_bg/schoolfront.png" #Front of School
image bg void1 = "mod_assets/custom_bg/void1.png" #Another Void BG
image bg bednight = "mod_assets/custom_bg/bedroom_night.png" #MC Bedroom Night

image bg black = "mod_assets/custom_bg/black.jpg"
image bg eye = "mod_assets/custom_bg/theeye.jpg" #eye jumpscare
image bg eye1 = "mod_assets/custom_bg/eye1.jpg"
image bg eye2 = "mod_assets/custom_bg/eye2.jpg"
image bg natcup1 = "mod_assets/custom_bg/natcup1.png"
image bg act1 = "mod_assets/custom_bg/actone.png"
image bg act2 = "mod_assets/custom_bg/acttwo.png"
image bg mallcg = "mod_assets/custom_bg/mall1.png"

#Credits
image bg credits1 = "mod_assets/credits/1.png"
image bg credits2 = "mod_assets/credits/2.png"
image bg credits3 = "mod_assets/credits/3.png"
image bg credits4 = "mod_assets/credits/4.png"
image bg credits5 = "mod_assets/credits/5.png"
image bg credits6 = "mod_assets/credits/6.png"
image bg credits7 = "mod_assets/credits/7.png"
image bg credits8 = "mod_assets/credits/8.png"
image bg credits9 = "mod_assets/credits/9.png"
image bg credits10 = "mod_assets/credits/10.png"
image bg credits11 = "mod_assets/credits/11.png"
image bg credits12 = "mod_assets/credits/12.png"
image bg credits13 = "mod_assets/credits/13.png"
image bg credits14 = "mod_assets/credits/14.png"
image bg credits15 = "mod_assets/credits/15.png"


# This image shows a glitched screen during Act 2 poem sharing with Yuri.
image bg glitch = LiveTile("bg/glitch.jpg")

# This image transform shows a glitched scene effect
# during Act 3 when we delete Monika.
image glitch_color:
    ytile 3
    zoom 2.5
    parallel:
        "bg/glitch-red.png"
        0.1
        "bg/glitch-green.png"
        0.1
        "bg/glitch-blue.png"
        0.1
        repeat
    parallel:
        yoffset 720
        linear 0.5 yoffset 0
        repeat
    parallel:
        choice:
            xoffset 0
        choice:
            xoffset 10
        choice:
            xoffset 20
        choice:
            xoffset 35
        choice:
            xoffset -10
        choice:
            xoffset -20
        choice:
            xoffset -30
        0.01
        repeat
    parallel:
        alpha 0.6
        linear 0.15 alpha 0.1
        0.2
        alpha 0.6
        linear 0.15 alpha 0.1
        0.2
        alpha 0.7
        linear 0.45 alpha 0

# This image transform shows another glitched scene effect
# during Act 3 when we delete Monika.
image glitch_color2:
    ytile 3
    zoom 2.5
    parallel:
        "bg/glitch-red.png"
        0.1
        "bg/glitch-green.png"
        0.1
        "bg/glitch-blue.png"
        0.1
        repeat
    parallel:
        yoffset 720
        linear 0.5 yoffset 0
        repeat
    parallel:
        choice:
            xoffset 0
        choice:
            xoffset 10
        choice:
            xoffset 20
        choice:
            xoffset 35
        choice:
            xoffset -10
        choice:
            xoffset -20
        choice:
            xoffset -30
        0.01
        repeat
    parallel:
        alpha 0.7
        linear 0.45 alpha 0

transform t51: #Leftmost of 5 characters
    tcommon(140)
transform t52:
    tcommon(390)
transform t53:
    tcommon(640)
transform t54:
    tcommon(890)
transform t55:
    tcommon(1140)

transform f51: #Leftmost of 5 characters
    fcommon(140)
transform f52:
    fcommon(390)
transform f53:
    fcommon(640)
transform f54:
    fcommon(890)
transform f55:
    fcommon(1140)

transform h51: #Leftmost of 5 characters
    hcommon(140)
transform h52:
    hcommon(390)
transform h53:
    hcommon(640)
transform h54:
    hcommon(890)
transform h55:
    hcommon(1140)

# Characters
# This is where the characters bodies and faces are defined in the mod.
# They are defined by a left half, a right half and their head.
# To define a new image, declare a new image statement like in this example:
#     image sayori 1ca = Composite((960, 960), (0, 0), "mod_assets/sayori/1cl.png", (0, 0), "mod_assets/sayori/1cr.png", (0, 0), "sayori/a.png")

# Sayori's Character Definitions

image sayori 1 = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/a.png")
image sayori 1a = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/a.png")
image sayori 1b = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/b.png")
image sayori 1c = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/c.png")
image sayori 1d = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/d.png")
image sayori 1e = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/e.png")
image sayori 1f = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/f.png")
image sayori 1g = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/g.png")
image sayori 1h = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/h.png")
image sayori 1i = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/i.png")
image sayori 1j = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/j.png")
image sayori 1k = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/k.png")
image sayori 1l = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/l.png")
image sayori 1m = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/m.png")
image sayori 1n = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/n.png")
image sayori 1o = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/o.png")
image sayori 1p = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/p.png")
image sayori 1q = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/q.png")
image sayori 1r = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/r.png")
image sayori 1s = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/s.png")
image sayori 1t = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/t.png")
image sayori 1u = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/u.png")
image sayori 1v = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/v.png")
image sayori 1w = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/w.png")
image sayori 1x = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/x.png")
image sayori 1y = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/y.png")

image sayori 2 = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/a.png")
image sayori 2a = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/a.png")
image sayori 2b = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/b.png")
image sayori 2c = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/c.png")
image sayori 2d = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/d.png")
image sayori 2e = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/e.png")
image sayori 2f = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/f.png")
image sayori 2g = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/g.png")
image sayori 2h = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/h.png")
image sayori 2i = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/i.png")
image sayori 2j = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/j.png")
image sayori 2k = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/k.png")
image sayori 2l = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/l.png")
image sayori 2m = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/m.png")
image sayori 2n = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/n.png")
image sayori 2o = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/o.png")
image sayori 2p = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/p.png")
image sayori 2q = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/q.png")
image sayori 2r = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/r.png")
image sayori 2s = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/s.png")
image sayori 2t = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/t.png")
image sayori 2u = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/u.png")
image sayori 2v = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/v.png")
image sayori 2w = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/w.png")
image sayori 2x = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/x.png")
image sayori 2y = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/y.png")

image sayori 3 = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/a.png")
image sayori 3a = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/a.png")
image sayori 3b = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/b.png")
image sayori 3c = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/c.png")
image sayori 3d = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/d.png")
image sayori 3e = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/e.png")
image sayori 3f = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/f.png")
image sayori 3g = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/g.png")
image sayori 3h = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/h.png")
image sayori 3i = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/i.png")
image sayori 3j = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/j.png")
image sayori 3k = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/k.png")
image sayori 3l = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/l.png")
image sayori 3m = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/m.png")
image sayori 3n = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/n.png")
image sayori 3o = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/o.png")
image sayori 3p = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/p.png")
image sayori 3q = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/q.png")
image sayori 3r = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/r.png")
image sayori 3s = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/s.png")
image sayori 3t = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/t.png")
image sayori 3u = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/u.png")
image sayori 3v = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/v.png")
image sayori 3w = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/w.png")
image sayori 3x = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/x.png")
image sayori 3y = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/y.png")

image sayori 4 = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/a.png")
image sayori 4a = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/a.png")
image sayori 4b = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/b.png")
image sayori 4c = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/c.png")
image sayori 4d = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/d.png")
image sayori 4e = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/e.png")
image sayori 4f = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/f.png")
image sayori 4g = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/g.png")
image sayori 4h = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/h.png")
image sayori 4i = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/i.png")
image sayori 4j = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/j.png")
image sayori 4k = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/k.png")
image sayori 4l = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/l.png")
image sayori 4m = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/m.png")
image sayori 4n = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/n.png")
image sayori 4o = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/o.png")
image sayori 4p = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/p.png")
image sayori 4q = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/q.png")
image sayori 4r = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/r.png")
image sayori 4s = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/s.png")
image sayori 4t = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/t.png")
image sayori 4u = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/u.png")
image sayori 4v = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/v.png")
image sayori 4w = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/w.png")
image sayori 4x = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/x.png")
image sayori 4y = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/y.png")

image sayori 5 = im.Composite((960, 960), (0, 0), "sayori/3a.png")
image sayori 5a = im.Composite((960, 960), (0, 0), "sayori/3a.png")
image sayori 5b = im.Composite((960, 960), (0, 0), "sayori/3b.png")
image sayori 5c = im.Composite((960, 960), (0, 0), "sayori/3c.png")
image sayori 5d = im.Composite((960, 960), (0, 0), "sayori/3d.png")

# Sayori in her Casual Outfit [Day 4]
image sayori 1ba = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/a.png")
image sayori 1bb = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/b.png")
image sayori 1bc = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/c.png")
image sayori 1bd = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/d.png")
image sayori 1be = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/e.png")
image sayori 1bf = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/f.png")
image sayori 1bg = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/g.png")
image sayori 1bh = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/h.png")
image sayori 1bi = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/i.png")
image sayori 1bj = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/j.png")
image sayori 1bk = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/k.png")
image sayori 1bl = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/l.png")
image sayori 1bm = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/m.png")
image sayori 1bn = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/n.png")
image sayori 1bo = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/o.png")
image sayori 1bp = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/p.png")
image sayori 1bq = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/q.png")
image sayori 1br = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/r.png")
image sayori 1bs = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/s.png")
image sayori 1bt = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/t.png")
image sayori 1bu = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/u.png")
image sayori 1bv = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/v.png")
image sayori 1bw = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/w.png")
image sayori 1bx = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/x.png")
image sayori 1by = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/y.png")

image sayori 2ba = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/a.png")
image sayori 2bb = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/b.png")
image sayori 2bc = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/c.png")
image sayori 2bd = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/d.png")
image sayori 2be = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/e.png")
image sayori 2bf = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/f.png")
image sayori 2bg = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/g.png")
image sayori 2bh = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/h.png")
image sayori 2bi = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/i.png")
image sayori 2bj = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/j.png")
image sayori 2bk = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/k.png")
image sayori 2bl = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/l.png")
image sayori 2bm = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/m.png")
image sayori 2bn = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/n.png")
image sayori 2bo = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/o.png")
image sayori 2bp = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/p.png")
image sayori 2bq = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/q.png")
image sayori 2br = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/r.png")
image sayori 2bs = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/s.png")
image sayori 2bt = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/t.png")
image sayori 2bu = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/u.png")
image sayori 2bv = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/v.png")
image sayori 2bw = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/w.png")
image sayori 2bx = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/x.png")
image sayori 2by = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/y.png")

image sayori 3ba = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/a.png")
image sayori 3bb = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/b.png")
image sayori 3bc = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/c.png")
image sayori 3bd = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/d.png")
image sayori 3be = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/e.png")
image sayori 3bf = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/f.png")
image sayori 3bg = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/g.png")
image sayori 3bh = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/h.png")
image sayori 3bi = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/i.png")
image sayori 3bj = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/j.png")
image sayori 3bk = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/k.png")
image sayori 3bl = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/l.png")
image sayori 3bm = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/m.png")
image sayori 3bn = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/n.png")
image sayori 3bo = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/o.png")
image sayori 3bp = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/p.png")
image sayori 3bq = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/q.png")
image sayori 3br = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/r.png")
image sayori 3bs = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/s.png")
image sayori 3bt = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/t.png")
image sayori 3bu = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/u.png")
image sayori 3bv = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/v.png")
image sayori 3bw = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/w.png")
image sayori 3bx = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/x.png")
image sayori 3by = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/y.png")

image sayori 4ba = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/a.png")
image sayori 4bb = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/b.png")
image sayori 4bc = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/c.png")
image sayori 4bd = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/d.png")
image sayori 4be = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/e.png")
image sayori 4bf = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/f.png")
image sayori 4bg = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/g.png")
image sayori 4bh = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/h.png")
image sayori 4bi = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/i.png")
image sayori 4bj = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/j.png")
image sayori 4bk = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/k.png")
image sayori 4bl = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/l.png")
image sayori 4bm = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/m.png")
image sayori 4bn = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/n.png")
image sayori 4bo = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/o.png")
image sayori 4bp = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/p.png")
image sayori 4bq = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/q.png")
image sayori 4br = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/r.png")
image sayori 4bs = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/s.png")
image sayori 4bt = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/t.png")
image sayori 4bu = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/u.png")
image sayori 4bv = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/v.png")
image sayori 4bw = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/w.png")
image sayori 4bx = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/x.png")
image sayori 4by = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/y.png")

#Sayori depressed expressions by JohnRDVSMarston

image sayori 41a = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/41a.png")
image sayori 41b = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/41b.png")
image sayori 41c = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/41c.png")
image sayori 41d = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/41d.png")
image sayori 41e = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/41e.png")
image sayori 41f = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/41f.png")
image sayori 41g = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/41g.png")
image sayori 41h = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/41h.png")
image sayori 41i = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/41i.png")

image sayori 42a = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/42a.png")
image sayori 42b = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/42b.png")
image sayori 42c = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/42c.png")
image sayori 42d = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/42d.png")
image sayori 42e = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/42e.png")
image sayori 42f = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/42f.png")
image sayori 42g = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/42g.png")
image sayori 42h = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/42h.png")
image sayori 42i = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/42i.png")

image sayori 43a = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/43a.png")
image sayori 43b = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/43b.png")
image sayori 43c = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/43c.png")
image sayori 43d = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/43d.png")
image sayori 43e = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/43e.png")
image sayori 43f = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/43f.png")
image sayori 43g = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/43g.png")
image sayori 43h = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/43h.png")
image sayori 43i = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/43i.png")

image sayori 44a = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/44a.png")
image sayori 44b = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/44b.png")
image sayori 44c = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/44c.png")
image sayori 44d = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/44d.png")
image sayori 44e = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/44e.png")
image sayori 44f = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/44f.png")
image sayori 44g = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/44g.png")
image sayori 44h = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/44h.png")
image sayori 44i = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/44i.png")

image sayori 45a = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/45a.png")
image sayori 45b = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/45b.png")
image sayori 45c = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/45c.png")
image sayori 45d = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/45d.png")
image sayori 45e = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/45e.png")
image sayori 45f = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/45f.png")
image sayori 45g = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/45g.png")
image sayori 45h = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/45h.png")
image sayori 45i = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/45i.png")

image sayori 46a = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/46a.png")
image sayori 46b = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/46b.png")
image sayori 46c = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/46c.png")
image sayori 46d = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/46d.png")
image sayori 46e = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/46e.png")
image sayori 46f = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/46f.png")
image sayori 46g = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/46g.png")
image sayori 46h = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/46h.png")
image sayori 46i = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/46i.png")

image sayori 47a = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/47a.png")
image sayori 47b = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/47b.png")
image sayori 47c = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/47c.png")
image sayori 47d = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/47d.png")
image sayori 47e = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/47e.png")
image sayori 47f = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/47f.png")
image sayori 47g = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/47g.png")
image sayori 47h = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/47h.png")
image sayori 47i = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/47i.png")

image sayori 48a = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/48a.png")
image sayori 48b = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/48b.png")
image sayori 48c = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/48c.png")
image sayori 48d = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/48d.png")
image sayori 48e = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/48e.png")
image sayori 48f = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/48f.png")
image sayori 48g = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/48g.png")
image sayori 48h = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/48h.png")
image sayori 48i = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/48i.png")

image sayori 41abow = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/41a.png",  (0, 0), "sayori/bow.png")
image sayori 41bbow = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/41b.png",  (0, 0), "sayori/bow.png")
image sayori 41cbow = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/41c.png",  (0, 0), "sayori/bow.png")
image sayori 41dbow = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/41d.png",  (0, 0), "sayori/bow.png")
image sayori 41ebow = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/41e.png",  (0, 0), "sayori/bow.png")
image sayori 41fbow = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/41f.png",  (0, 0), "sayori/bow.png")
image sayori 41gbow = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/41g.png",  (0, 0), "sayori/bow.png")
image sayori 41hbow = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/41h.png",  (0, 0), "sayori/bow.png")
image sayori 41ibow = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/41i.png",  (0, 0), "sayori/bow.png")

image sayori 42abow = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/42a.png",  (0, 0), "sayori/bow.png")
image sayori 42bbow = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/42b.png",  (0, 0), "sayori/bow.png")
image sayori 42cbow = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/42c.png",  (0, 0), "sayori/bow.png")
image sayori 42dbow = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/42d.png",  (0, 0), "sayori/bow.png")
image sayori 42ebow = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/42e.png",  (0, 0), "sayori/bow.png")
image sayori 42fbow = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/42f.png",  (0, 0), "sayori/bow.png")
image sayori 42gbow = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/42g.png",  (0, 0), "sayori/bow.png")
image sayori 42hbow = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/42h.png",  (0, 0), "sayori/bow.png")
image sayori 42ibow = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/42i.png",  (0, 0), "sayori/bow.png")

image sayori 43abow = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/43a.png",  (0, 0), "sayori/bow.png")
image sayori 43bbow = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/43b.png",  (0, 0), "sayori/bow.png")
image sayori 43cbow = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/43c.png",  (0, 0), "sayori/bow.png")
image sayori 43dbow = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/43d.png",  (0, 0), "sayori/bow.png")
image sayori 43ebow = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/43e.png",  (0, 0), "sayori/bow.png")
image sayori 43fbow = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/43f.png",  (0, 0), "sayori/bow.png")
image sayori 43gbow = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/43g.png",  (0, 0), "sayori/bow.png")
image sayori 43hbow = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/43h.png",  (0, 0), "sayori/bow.png")
image sayori 43ibow = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/43i.png",  (0, 0), "sayori/bow.png")

image sayori 44abow = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/44a.png",  (0, 0), "sayori/bow.png")
image sayori 44bbow = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/44b.png",  (0, 0), "sayori/bow.png")
image sayori 44cbow = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/44c.png",  (0, 0), "sayori/bow.png")
image sayori 44dbow = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/44d.png",  (0, 0), "sayori/bow.png")
image sayori 44ebow = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/44e.png",  (0, 0), "sayori/bow.png")
image sayori 44fbow = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/44f.png",  (0, 0), "sayori/bow.png")
image sayori 44gbow = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/44g.png",  (0, 0), "sayori/bow.png")
image sayori 44hbow = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/44h.png",  (0, 0), "sayori/bow.png")
image sayori 44ibow = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/44i.png",  (0, 0), "sayori/bow.png")

image sayori 45abow = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/45a.png",  (0, 0), "sayori/bow.png")
image sayori 45bbow = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/45b.png",  (0, 0), "sayori/bow.png")
image sayori 45cbow = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/45c.png",  (0, 0), "sayori/bow.png")
image sayori 45dbow = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/45d.png",  (0, 0), "sayori/bow.png")
image sayori 45ebow = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/45e.png",  (0, 0), "sayori/bow.png")
image sayori 45fbow = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/45f.png",  (0, 0), "sayori/bow.png")
image sayori 45gbow = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/45g.png",  (0, 0), "sayori/bow.png")
image sayori 45hbow = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/45h.png",  (0, 0), "sayori/bow.png")
image sayori 45ibow = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/45i.png",  (0, 0), "sayori/bow.png")

image sayori 46abow = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/46a.png",  (0, 0), "sayori/bow.png")
image sayori 46bbow = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/46b.png",  (0, 0), "sayori/bow.png")
image sayori 46cbow = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/46c.png",  (0, 0), "sayori/bow.png")
image sayori 46dbow = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/46d.png",  (0, 0), "sayori/bow.png")
image sayori 46ebow = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/46e.png",  (0, 0), "sayori/bow.png")
image sayori 46fbow = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/46f.png",  (0, 0), "sayori/bow.png")
image sayori 46gbow = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/46g.png",  (0, 0), "sayori/bow.png")
image sayori 46hbow = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/46h.png",  (0, 0), "sayori/bow.png")
image sayori 46ibow = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/46i.png",  (0, 0), "sayori/bow.png")

image sayori 47abow = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/47a.png",  (0, 0), "sayori/bow.png")
image sayori 47bbow = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/47b.png",  (0, 0), "sayori/bow.png")
image sayori 47cbow = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/47c.png",  (0, 0), "sayori/bow.png")
image sayori 47dbow = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/47d.png",  (0, 0), "sayori/bow.png")
image sayori 47ebow = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/47e.png",  (0, 0), "sayori/bow.png")
image sayori 47fbow = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/47f.png",  (0, 0), "sayori/bow.png")
image sayori 47gbow = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/47g.png",  (0, 0), "sayori/bow.png")
image sayori 47hbow = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/47h.png",  (0, 0), "sayori/bow.png")
image sayori 47ibow = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/47i.png",  (0, 0), "sayori/bow.png")

image sayori 48abow = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/48a.png",  (0, 0), "sayori/bow.png")
image sayori 48bbow = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/48b.png",  (0, 0), "sayori/bow.png")
image sayori 48cbow = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/48c.png",  (0, 0), "sayori/bow.png")
image sayori 48dbow = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/48d.png",  (0, 0), "sayori/bow.png")
image sayori 48ebow = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/48e.png",  (0, 0), "sayori/bow.png")
image sayori 48fbow = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/48f.png",  (0, 0), "sayori/bow.png")
image sayori 48gbow = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/48g.png",  (0, 0), "sayori/bow.png")
image sayori 48hbow = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/48h.png",  (0, 0), "sayori/bow.png")
image sayori 48ibow = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/48i.png",  (0, 0), "sayori/bow.png")

image sayori 4b1a = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/41a.png")
image sayori 4b1b = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/41b.png")
image sayori 4b1c = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/41c.png")
image sayori 4b1d = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/41d.png")
image sayori 4b1e = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/41e.png")
image sayori 4b1f = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/41f.png")
image sayori 4b1g = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/41g.png")
image sayori 4b1h = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/41h.png")
image sayori 4b1i = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/41i.png")

image sayori 4b2a = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/42a.png")
image sayori 4b2b = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/42b.png")
image sayori 4b2c = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/42c.png")
image sayori 4b2d = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/42d.png")
image sayori 4b2e = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/42e.png")
image sayori 4b2f = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/42f.png")
image sayori 4b2g = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/42g.png")
image sayori 4b2h = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/42h.png")
image sayori 4b2i = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/42i.png")

image sayori 4b3a = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/43a.png")
image sayori 4b3b = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/43b.png")
image sayori 4b3c = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/43c.png")
image sayori 4b3d = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/43d.png")
image sayori 4b3e = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/43e.png")
image sayori 4b3f = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/43f.png")
image sayori 4b3g = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/43g.png")
image sayori 4b3h = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/43h.png")
image sayori 4b3i = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/43i.png")

image sayori 4b4a = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/44a.png")
image sayori 4b4b = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/44b.png")
image sayori 4b4c = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/44c.png")
image sayori 4b4d = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/44d.png")
image sayori 4b4e = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/44e.png")
image sayori 4b4f = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/44f.png")
image sayori 4b4g = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/44g.png")
image sayori 4b4h = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/44h.png")
image sayori 4b4i = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/44i.png")

image sayori 4b5a = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/45a.png")
image sayori 4b5b = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/45b.png")
image sayori 4b5c = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/45c.png")
image sayori 4b5d = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/45d.png")
image sayori 4b5e = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/45e.png")
image sayori 4b5f = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/45f.png")
image sayori 4b5g = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/45g.png")
image sayori 4b5h = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/45h.png")
image sayori 4b5i = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/45i.png")

image sayori 4b6a = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/46a.png")
image sayori 4b6b = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/46b.png")
image sayori 4b6c = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/46c.png")
image sayori 4b6d = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/46d.png")
image sayori 4b6e = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/46e.png")
image sayori 4b6f = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/46f.png")
image sayori 4b6g = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/46g.png")
image sayori 4b6h = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/46h.png")
image sayori 4b6i = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/46i.png")

image sayori 4b7a = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/47a.png")
image sayori 4b7b = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/47b.png")
image sayori 4b7c = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/47c.png")
image sayori 4b7d = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/47d.png")
image sayori 4b7e = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/47e.png")
image sayori 4b7f = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/47f.png")
image sayori 4b7g = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/47g.png")
image sayori 4b7h = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/47h.png")
image sayori 4b7i = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/47i.png")

image sayori 4b8a = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/48a.png")
image sayori 4b8b = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/48b.png")
image sayori 4b8c = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/48c.png")
image sayori 4b8d = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/48d.png")
image sayori 4b8e = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/48e.png")
image sayori 4b8f = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/48f.png")
image sayori 4b8g = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/48g.png")
image sayori 4b8h = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/48h.png")
image sayori 4b8i = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/48i.png")

image sayori 4b1abow = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/41a.png",  (0, 0), "sayori/bow.png")
image sayori 4b1bbow = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/41b.png",  (0, 0), "sayori/bow.png")
image sayori 4b1cbow = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/41c.png",  (0, 0), "sayori/bow.png")
image sayori 4b1dbow = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/41d.png",  (0, 0), "sayori/bow.png")
image sayori 4b1ebow = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/41e.png",  (0, 0), "sayori/bow.png")
image sayori 4b1fbow = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/41f.png",  (0, 0), "sayori/bow.png")
image sayori 4b1gbow = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/41g.png",  (0, 0), "sayori/bow.png")
image sayori 4b1hbow = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/41h.png",  (0, 0), "sayori/bow.png")
image sayori 4b1ibow = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/41i.png",  (0, 0), "sayori/bow.png")

image sayori 4b2abow = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/42a.png",  (0, 0), "sayori/bow.png")
image sayori 4b2bbow = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/42b.png",  (0, 0), "sayori/bow.png")
image sayori 4b2cbow = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/42c.png",  (0, 0), "sayori/bow.png")
image sayori 4b2dbow = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/42d.png",  (0, 0), "sayori/bow.png")
image sayori 4b2ebow = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/42e.png",  (0, 0), "sayori/bow.png")
image sayori 4b2fbow = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/42f.png",  (0, 0), "sayori/bow.png")
image sayori 4b2gbow = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/42g.png",  (0, 0), "sayori/bow.png")
image sayori 4b2hbow = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/42h.png",  (0, 0), "sayori/bow.png")
image sayori 4b2ibow = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/42i.png",  (0, 0), "sayori/bow.png")

image sayori 4b3abow = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/43a.png",  (0, 0), "sayori/bow.png")
image sayori 4b3bbow = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/43b.png",  (0, 0), "sayori/bow.png")
image sayori 4b3cbow = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/43c.png",  (0, 0), "sayori/bow.png")
image sayori 4b3dbow = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/43d.png",  (0, 0), "sayori/bow.png")
image sayori 4b3ebow = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/43e.png",  (0, 0), "sayori/bow.png")
image sayori 4b3fbow = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/43f.png",  (0, 0), "sayori/bow.png")
image sayori 4b3gbow = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/43g.png",  (0, 0), "sayori/bow.png")
image sayori 4b3hbow = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/43h.png",  (0, 0), "sayori/bow.png")
image sayori 4b3ibow = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/43i.png",  (0, 0), "sayori/bow.png")

image sayori 4b4abow = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/44a.png",  (0, 0), "sayori/bow.png")
image sayori 4b4bbow = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/44b.png",  (0, 0), "sayori/bow.png")
image sayori 4b4cbow = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/44c.png",  (0, 0), "sayori/bow.png")
image sayori 4b4dbow = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/44d.png",  (0, 0), "sayori/bow.png")
image sayori 4b4ebow = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/44e.png",  (0, 0), "sayori/bow.png")
image sayori 4b4fbow = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/44f.png",  (0, 0), "sayori/bow.png")
image sayori 4b4gbow = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/44g.png",  (0, 0), "sayori/bow.png")
image sayori 4b4hbow = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/44h.png",  (0, 0), "sayori/bow.png")
image sayori 4b4ibow = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/44i.png",  (0, 0), "sayori/bow.png")

image sayori 4b5abow = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/45a.png",  (0, 0), "sayori/bow.png")
image sayori 4b5bbow = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/45b.png",  (0, 0), "sayori/bow.png")
image sayori 4b5cbow = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/45c.png",  (0, 0), "sayori/bow.png")
image sayori 4b5dbow = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/45d.png",  (0, 0), "sayori/bow.png")
image sayori 4b5ebow = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/45e.png",  (0, 0), "sayori/bow.png")
image sayori 4b5fbow = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/45f.png",  (0, 0), "sayori/bow.png")
image sayori 4b5gbow = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/45g.png",  (0, 0), "sayori/bow.png")
image sayori 4b5hbow = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/45h.png",  (0, 0), "sayori/bow.png")
image sayori 4b5ibow = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/45i.png",  (0, 0), "sayori/bow.png")

image sayori 4b6abow = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/46a.png",  (0, 0), "sayori/bow.png")
image sayori 4b6bbow = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/46b.png",  (0, 0), "sayori/bow.png")
image sayori 4b6cbow = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/46c.png",  (0, 0), "sayori/bow.png")
image sayori 4b6dbow = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/46d.png",  (0, 0), "sayori/bow.png")
image sayori 4b6ebow = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/46e.png",  (0, 0), "sayori/bow.png")
image sayori 4b6fbow = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/46f.png",  (0, 0), "sayori/bow.png")
image sayori 4b6gbow = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/46g.png",  (0, 0), "sayori/bow.png")
image sayori 4b6hbow = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/46h.png",  (0, 0), "sayori/bow.png")
image sayori 4b6ibow = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/46i.png",  (0, 0), "sayori/bow.png")

image sayori 4b7abow = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/47a.png",  (0, 0), "sayori/bow.png")
image sayori 4b7bbow = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/47b.png",  (0, 0), "sayori/bow.png")
image sayori 4b7cbow = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/47c.png",  (0, 0), "sayori/bow.png")
image sayori 4b7dbow = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/47d.png",  (0, 0), "sayori/bow.png")
image sayori 4b7ebow = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/47e.png",  (0, 0), "sayori/bow.png")
image sayori 4b7fbow = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/47f.png",  (0, 0), "sayori/bow.png")
image sayori 4b7gbow = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/47g.png",  (0, 0), "sayori/bow.png")
image sayori 4b7hbow = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/47h.png",  (0, 0), "sayori/bow.png")
image sayori 4b7ibow = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/47i.png",  (0, 0), "sayori/bow.png")

image sayori 4b8abow = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/48a.png",  (0, 0), "sayori/bow.png")
image sayori 4b8bbow = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/48b.png",  (0, 0), "sayori/bow.png")
image sayori 4b8cbow = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/48c.png",  (0, 0), "sayori/bow.png")
image sayori 4b8dbow = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/48d.png",  (0, 0), "sayori/bow.png")
image sayori 4b8ebow = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/48e.png",  (0, 0), "sayori/bow.png")
image sayori 4b8fbow = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/48f.png",  (0, 0), "sayori/bow.png")
image sayori 4b8gbow = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/48g.png",  (0, 0), "sayori/bow.png")
image sayori 4b8hbow = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/48h.png",  (0, 0), "sayori/bow.png")
image sayori 4b8ibow = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/48i.png",  (0, 0), "sayori/bow.png")

image sayori 4p1a = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/41a.png")
image sayori 4p1b = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/41b.png")
image sayori 4p1c = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/41c.png")
image sayori 4p1d = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/41d.png")
image sayori 4p1e = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/41e.png")
image sayori 4p1f = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/41f.png")
image sayori 4p1g = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/41g.png")
image sayori 4p1h = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/41h.png")
image sayori 4p1i = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/41i.png")

image sayori 4p2a = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/42a.png")
image sayori 4p2b = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/42b.png")
image sayori 4p2c = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/42c.png")
image sayori 4p2d = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/42d.png")
image sayori 4p2e = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/42e.png")
image sayori 4p2f = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/42f.png")
image sayori 4p2g = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/42g.png")
image sayori 4p2h = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/42h.png")
image sayori 4p2i = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/42i.png")

image sayori 4p3a = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/43a.png")
image sayori 4p3b = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/43b.png")
image sayori 4p3c = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/43c.png")
image sayori 4p3d = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/43d.png")
image sayori 4p3e = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/43e.png")
image sayori 4p3f = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/43f.png")
image sayori 4p3g = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/43g.png")
image sayori 4p3h = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/43h.png")
image sayori 4p3i = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/43i.png")

image sayori 4p4a = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/44a.png")
image sayori 4p4b = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/44b.png")
image sayori 4p4c = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/44c.png")
image sayori 4p4d = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/44d.png")
image sayori 4p4e = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/44e.png")
image sayori 4p4f = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/44f.png")
image sayori 4p4g = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/44g.png")
image sayori 4p4h = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/44h.png")
image sayori 4p4i = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/44i.png")

image sayori 4p5a = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/45a.png")
image sayori 4p5b = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/45b.png")
image sayori 4p5c = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/45c.png")
image sayori 4p5d = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/45d.png")
image sayori 4p5e = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/45e.png")
image sayori 4p5f = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/45f.png")
image sayori 4p5g = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/45g.png")
image sayori 4p5h = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/45h.png")
image sayori 4p5i = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/45i.png")

image sayori 4p6a = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/46a.png")
image sayori 4p6b = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/46b.png")
image sayori 4p6c = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/46c.png")
image sayori 4p6d = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/46d.png")
image sayori 4p6e = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/46e.png")
image sayori 4p6f = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/46f.png")
image sayori 4p6g = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/46g.png")
image sayori 4p6h = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/46h.png")
image sayori 4p6i = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/46i.png")

image sayori 4p7a = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/47a.png")
image sayori 4p7b = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/47b.png")
image sayori 4p7c = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/47c.png")
image sayori 4p7d = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/47d.png")
image sayori 4p7e = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/47e.png")
image sayori 4p7f = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/47f.png")
image sayori 4p7g = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/47g.png")
image sayori 4p7h = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/47h.png")
image sayori 4p7i = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/47i.png")

image sayori 4p8a = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/48a.png")
image sayori 4p8b = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/48b.png")
image sayori 4p8c = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/48c.png")
image sayori 4p8d = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/48d.png")
image sayori 4p8e = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/48e.png")
image sayori 4p8f = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/48f.png")
image sayori 4p8g = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/48g.png")
image sayori 4p8h = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/48h.png")
image sayori 4p8i = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/48i.png")

image sayori 4p1abow = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/41a.png",  (0, 0), "sayori/bow.png")
image sayori 4p1bbow = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/41b.png",  (0, 0), "sayori/bow.png")
image sayori 4p1cbow = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/41c.png",  (0, 0), "sayori/bow.png")
image sayori 4p1dbow = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/41d.png",  (0, 0), "sayori/bow.png")
image sayori 4p1ebow = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/41e.png",  (0, 0), "sayori/bow.png")
image sayori 4p1fbow = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/41f.png",  (0, 0), "sayori/bow.png")
image sayori 4p1gbow = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/41g.png",  (0, 0), "sayori/bow.png")
image sayori 4p1hbow = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/41h.png",  (0, 0), "sayori/bow.png")
image sayori 4p1ibow = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/41i.png",  (0, 0), "sayori/bow.png")

image sayori 4p2abow = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/42a.png",  (0, 0), "sayori/bow.png")
image sayori 4p2bbow = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/42b.png",  (0, 0), "sayori/bow.png")
image sayori 4p2cbow = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/42c.png",  (0, 0), "sayori/bow.png")
image sayori 4p2dbow = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/42d.png",  (0, 0), "sayori/bow.png")
image sayori 4p2ebow = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/42e.png",  (0, 0), "sayori/bow.png")
image sayori 4p2fbow = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/42f.png",  (0, 0), "sayori/bow.png")
image sayori 4p2gbow = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/42g.png",  (0, 0), "sayori/bow.png")
image sayori 4p2hbow = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/42h.png",  (0, 0), "sayori/bow.png")
image sayori 4p2ibow = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/42i.png",  (0, 0), "sayori/bow.png")

image sayori 4p3abow = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/43a.png",  (0, 0), "sayori/bow.png")
image sayori 4p3bbow = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/43b.png",  (0, 0), "sayori/bow.png")
image sayori 4p3cbow = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/43c.png",  (0, 0), "sayori/bow.png")
image sayori 4p3dbow = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/43d.png",  (0, 0), "sayori/bow.png")
image sayori 4p3ebow = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/43e.png",  (0, 0), "sayori/bow.png")
image sayori 4p3fbow = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/43f.png",  (0, 0), "sayori/bow.png")
image sayori 4p3gbow = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/43g.png",  (0, 0), "sayori/bow.png")
image sayori 4p3hbow = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/43h.png",  (0, 0), "sayori/bow.png")
image sayori 4p3ibow = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/43i.png",  (0, 0), "sayori/bow.png")

image sayori 4p4abow = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/44a.png",  (0, 0), "sayori/bow.png")
image sayori 4p4bbow = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/44b.png",  (0, 0), "sayori/bow.png")
image sayori 4p4cbow = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/44c.png",  (0, 0), "sayori/bow.png")
image sayori 4p4dbow = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/44d.png",  (0, 0), "sayori/bow.png")
image sayori 4p4ebow = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/44e.png",  (0, 0), "sayori/bow.png")
image sayori 4p4fbow = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/44f.png",  (0, 0), "sayori/bow.png")
image sayori 4p4gbow = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/44g.png",  (0, 0), "sayori/bow.png")
image sayori 4p4hbow = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/44h.png",  (0, 0), "sayori/bow.png")
image sayori 4p4ibow = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/44i.png",  (0, 0), "sayori/bow.png")

image sayori 4p5abow = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/45a.png",  (0, 0), "sayori/bow.png")
image sayori 4p5bbow = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/45b.png",  (0, 0), "sayori/bow.png")
image sayori 4p5cbow = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/45c.png",  (0, 0), "sayori/bow.png")
image sayori 4p5dbow = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/45d.png",  (0, 0), "sayori/bow.png")
image sayori 4p5ebow = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/45e.png",  (0, 0), "sayori/bow.png")
image sayori 4p5fbow = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/45f.png",  (0, 0), "sayori/bow.png")
image sayori 4p5gbow = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/45g.png",  (0, 0), "sayori/bow.png")
image sayori 4p5hbow = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/45h.png",  (0, 0), "sayori/bow.png")
image sayori 4p5ibow = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/45i.png",  (0, 0), "sayori/bow.png")

image sayori 4p6abow = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/46a.png",  (0, 0), "sayori/bow.png")
image sayori 4p6bbow = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/46b.png",  (0, 0), "sayori/bow.png")
image sayori 4p6cbow = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/46c.png",  (0, 0), "sayori/bow.png")
image sayori 4p6dbow = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/46d.png",  (0, 0), "sayori/bow.png")
image sayori 4p6ebow = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/46e.png",  (0, 0), "sayori/bow.png")
image sayori 4p6fbow = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/46f.png",  (0, 0), "sayori/bow.png")
image sayori 4p6gbow = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/46g.png",  (0, 0), "sayori/bow.png")
image sayori 4p6hbow = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/46h.png",  (0, 0), "sayori/bow.png")
image sayori 4p6ibow = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/46i.png",  (0, 0), "sayori/bow.png")

image sayori 4p7abow = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/47a.png",  (0, 0), "sayori/bow.png")
image sayori 4p7bbow = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/47b.png",  (0, 0), "sayori/bow.png")
image sayori 4p7cbow = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/47c.png",  (0, 0), "sayori/bow.png")
image sayori 4p7dbow = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/47d.png",  (0, 0), "sayori/bow.png")
image sayori 4p7ebow = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/47e.png",  (0, 0), "sayori/bow.png")
image sayori 4p7fbow = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/47f.png",  (0, 0), "sayori/bow.png")
image sayori 4p7gbow = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/47g.png",  (0, 0), "sayori/bow.png")
image sayori 4p7hbow = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/47h.png",  (0, 0), "sayori/bow.png")
image sayori 4p7ibow = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/47i.png",  (0, 0), "sayori/bow.png")

image sayori 4p8abow = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/48a.png",  (0, 0), "sayori/bow.png")
image sayori 4p8bbow = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/48b.png",  (0, 0), "sayori/bow.png")
image sayori 4p8cbow = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/48c.png",  (0, 0), "sayori/bow.png")
image sayori 4p8dbow = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/48d.png",  (0, 0), "sayori/bow.png")
image sayori 4p8ebow = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/48e.png",  (0, 0), "sayori/bow.png")
image sayori 4p8fbow = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/48f.png",  (0, 0), "sayori/bow.png")
image sayori 4p8gbow = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/48g.png",  (0, 0), "sayori/bow.png")
image sayori 4p8hbow = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/48h.png",  (0, 0), "sayori/bow.png")
image sayori 4p8ibow = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/48i.png",  (0, 0), "sayori/bow.png")

image sayori 4Scream = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/4Scream.png")
image sayori 4Screambow = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/4Scream.png",  (0, 0), "sayori/bow.png")
image sayori 4bScream = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/4Scream.png")
image sayori 4bScreambow = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/4Scream.png",  (0, 0), "sayori/bow.png")
image sayori 4pScream = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/4Scream.png")
image sayori 4pScreambow = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/4Scream.png",  (0, 0), "sayori/bow.png")

#Sayori with long hair from EMR

image sayori 1emr = im.Composite((960, 960), (0, 0), "mod_assets/sayori_hair_epilogue.png", (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/a.png", (0, 0), "mod_assets/sayori_ptsd.png")
image sayori 1aemr = im.Composite((960, 960), (0, 0), "mod_assets/sayori_hair_epilogue.png", (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/a.png", (0, 0), "mod_assets/sayori_ptsd.png")
image sayori 1bemr = im.Composite((960, 960), (0, 0), "mod_assets/sayori_hair_epilogue.png", (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/b.png", (0, 0), "mod_assets/sayori_ptsd.png")
image sayori 1cemr = im.Composite((960, 960), (0, 0), "mod_assets/sayori_hair_epilogue.png", (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/c.png", (0, 0), "mod_assets/sayori_ptsd.png")
image sayori 1demr = im.Composite((960, 960), (0, 0), "mod_assets/sayori_hair_epilogue.png", (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/d.png", (0, 0), "mod_assets/sayori_ptsd.png")
image sayori 1eemr = im.Composite((960, 960), (0, 0), "mod_assets/sayori_hair_epilogue.png", (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/e.png", (0, 0), "mod_assets/sayori_ptsd.png")
image sayori 1femr = im.Composite((960, 960), (0, 0), "mod_assets/sayori_hair_epilogue.png", (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/f.png", (0, 0), "mod_assets/sayori_ptsd.png")
image sayori 1gemr = im.Composite((960, 960), (0, 0), "mod_assets/sayori_hair_epilogue.png", (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/g.png", (0, 0), "mod_assets/sayori_ptsd.png")
image sayori 1hemr = im.Composite((960, 960), (0, 0), "mod_assets/sayori_hair_epilogue.png", (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/h.png", (0, 0), "mod_assets/sayori_ptsd.png")
image sayori 1iemr = im.Composite((960, 960), (0, 0), "mod_assets/sayori_hair_epilogue.png", (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/i.png", (0, 0), "mod_assets/sayori_ptsd.png")
image sayori 1jemr = im.Composite((960, 960), (0, 0), "mod_assets/sayori_hair_epilogue.png", (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/j.png", (0, 0), "mod_assets/sayori_ptsd.png")
image sayori 1kemr = im.Composite((960, 960), (0, 0), "mod_assets/sayori_hair_epilogue.png", (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/k.png", (0, 0), "mod_assets/sayori_ptsd.png")
image sayori 1lemr = im.Composite((960, 960), (0, 0), "mod_assets/sayori_hair_epilogue.png", (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/l.png", (0, 0), "mod_assets/sayori_ptsd.png")
image sayori 1memr = im.Composite((960, 960), (0, 0), "mod_assets/sayori_hair_epilogue.png", (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/m.png", (0, 0), "mod_assets/sayori_ptsd.png")
image sayori 1nemr = im.Composite((960, 960), (0, 0), "mod_assets/sayori_hair_epilogue.png", (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/n.png", (0, 0), "mod_assets/sayori_ptsd.png")
image sayori 1oemr = im.Composite((960, 960), (0, 0), "mod_assets/sayori_hair_epilogue.png", (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/o.png", (0, 0), "mod_assets/sayori_ptsd.png")
image sayori 1pemr = im.Composite((960, 960), (0, 0), "mod_assets/sayori_hair_epilogue.png", (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/p.png", (0, 0), "mod_assets/sayori_ptsd.png")
image sayori 1qemr = im.Composite((960, 960), (0, 0), "mod_assets/sayori_hair_epilogue.png", (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/q.png", (0, 0), "mod_assets/sayori_ptsd.png")
image sayori 1remr = im.Composite((960, 960), (0, 0), "mod_assets/sayori_hair_epilogue.png", (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/r.png", (0, 0), "mod_assets/sayori_ptsd.png")
image sayori 1semr = im.Composite((960, 960), (0, 0), "mod_assets/sayori_hair_epilogue.png", (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/s.png", (0, 0), "mod_assets/sayori_ptsd.png")
image sayori 1temr = im.Composite((960, 960), (0, 0), "mod_assets/sayori_hair_epilogue.png", (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/t.png", (0, 0), "mod_assets/sayori_ptsd.png")
image sayori 1uemr = im.Composite((960, 960), (0, 0), "mod_assets/sayori_hair_epilogue.png", (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/u.png", (0, 0), "mod_assets/sayori_ptsd.png")
image sayori 1vemr = im.Composite((960, 960), (0, 0), "mod_assets/sayori_hair_epilogue.png", (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/v.png", (0, 0), "mod_assets/sayori_ptsd.png")
image sayori 1wemr = im.Composite((960, 960), (0, 0), "mod_assets/sayori_hair_epilogue.png", (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/w.png", (0, 0), "mod_assets/sayori_ptsd.png")
image sayori 1xemr = im.Composite((960, 960), (0, 0), "mod_assets/sayori_hair_epilogue.png", (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/x.png", (0, 0), "mod_assets/sayori_ptsd.png")
image sayori 1yemr = im.Composite((960, 960), (0, 0), "mod_assets/sayori_hair_epilogue.png", (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/y.png", (0, 0), "mod_assets/sayori_ptsd.png")

image sayori 2emr = im.Composite((960, 960), (0, 0), "mod_assets/sayori_hair_epilogue.png", (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/a.png", (0, 0), "mod_assets/sayori_ptsd.png")
image sayori 2aemr = im.Composite((960, 960), (0, 0), "mod_assets/sayori_hair_epilogue.png", (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/a.png", (0, 0), "mod_assets/sayori_ptsd.png")
image sayori 2bemr = im.Composite((960, 960), (0, 0), "mod_assets/sayori_hair_epilogue.png", (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/b.png", (0, 0), "mod_assets/sayori_ptsd.png")
image sayori 2cemr = im.Composite((960, 960), (0, 0), "mod_assets/sayori_hair_epilogue.png", (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/c.png", (0, 0), "mod_assets/sayori_ptsd.png")
image sayori 2demr = im.Composite((960, 960), (0, 0), "mod_assets/sayori_hair_epilogue.png", (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/d.png", (0, 0), "mod_assets/sayori_ptsd.png")
image sayori 2eemr = im.Composite((960, 960), (0, 0), "mod_assets/sayori_hair_epilogue.png", (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/e.png", (0, 0), "mod_assets/sayori_ptsd.png")
image sayori 2femr = im.Composite((960, 960), (0, 0), "mod_assets/sayori_hair_epilogue.png", (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/f.png", (0, 0), "mod_assets/sayori_ptsd.png")
image sayori 2gemr = im.Composite((960, 960), (0, 0), "mod_assets/sayori_hair_epilogue.png", (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/g.png", (0, 0), "mod_assets/sayori_ptsd.png")
image sayori 2hemr = im.Composite((960, 960), (0, 0), "mod_assets/sayori_hair_epilogue.png", (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/h.png", (0, 0), "mod_assets/sayori_ptsd.png")
image sayori 2iemr = im.Composite((960, 960), (0, 0), "mod_assets/sayori_hair_epilogue.png", (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/i.png", (0, 0), "mod_assets/sayori_ptsd.png")
image sayori 2jemr = im.Composite((960, 960), (0, 0), "mod_assets/sayori_hair_epilogue.png", (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/j.png", (0, 0), "mod_assets/sayori_ptsd.png")
image sayori 2kemr = im.Composite((960, 960), (0, 0), "mod_assets/sayori_hair_epilogue.png", (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/k.png", (0, 0), "mod_assets/sayori_ptsd.png")
image sayori 2lemr = im.Composite((960, 960), (0, 0), "mod_assets/sayori_hair_epilogue.png", (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/l.png", (0, 0), "mod_assets/sayori_ptsd.png")
image sayori 2memr = im.Composite((960, 960), (0, 0), "mod_assets/sayori_hair_epilogue.png", (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/m.png", (0, 0), "mod_assets/sayori_ptsd.png")
image sayori 2nemr = im.Composite((960, 960), (0, 0), "mod_assets/sayori_hair_epilogue.png", (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/n.png", (0, 0), "mod_assets/sayori_ptsd.png")
image sayori 2oemr = im.Composite((960, 960), (0, 0), "mod_assets/sayori_hair_epilogue.png", (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/o.png", (0, 0), "mod_assets/sayori_ptsd.png")
image sayori 2pemr = im.Composite((960, 960), (0, 0), "mod_assets/sayori_hair_epilogue.png", (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/p.png", (0, 0), "mod_assets/sayori_ptsd.png")
image sayori 2qemr = im.Composite((960, 960), (0, 0), "mod_assets/sayori_hair_epilogue.png", (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/q.png", (0, 0), "mod_assets/sayori_ptsd.png")
image sayori 2remr = im.Composite((960, 960), (0, 0), "mod_assets/sayori_hair_epilogue.png", (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/r.png", (0, 0), "mod_assets/sayori_ptsd.png")
image sayori 2semr = im.Composite((960, 960), (0, 0), "mod_assets/sayori_hair_epilogue.png", (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/s.png", (0, 0), "mod_assets/sayori_ptsd.png")
image sayori 2temr = im.Composite((960, 960), (0, 0), "mod_assets/sayori_hair_epilogue.png", (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/t.png", (0, 0), "mod_assets/sayori_ptsd.png")
image sayori 2uemr = im.Composite((960, 960), (0, 0), "mod_assets/sayori_hair_epilogue.png", (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/u.png", (0, 0), "mod_assets/sayori_ptsd.png")
image sayori 2vemr = im.Composite((960, 960), (0, 0), "mod_assets/sayori_hair_epilogue.png", (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/v.png", (0, 0), "mod_assets/sayori_ptsd.png")
image sayori 2wemr = im.Composite((960, 960), (0, 0), "mod_assets/sayori_hair_epilogue.png", (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/w.png", (0, 0), "mod_assets/sayori_ptsd.png")
image sayori 2xemr = im.Composite((960, 960), (0, 0), "mod_assets/sayori_hair_epilogue.png", (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/x.png", (0, 0), "mod_assets/sayori_ptsd.png")
image sayori 2yemr = im.Composite((960, 960), (0, 0), "mod_assets/sayori_hair_epilogue.png", (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/y.png", (0, 0), "mod_assets/sayori_ptsd.png")

image sayori 3emr = im.Composite((960, 960), (0, 0), "mod_assets/sayori_hair_epilogue.png", (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/a.png", (0, 0), "mod_assets/sayori_ptsd.png")
image sayori 3aemr = im.Composite((960, 960), (0, 0), "mod_assets/sayori_hair_epilogue.png", (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/a.png", (0, 0), "mod_assets/sayori_ptsd.png")
image sayori 3bemr = im.Composite((960, 960), (0, 0), "mod_assets/sayori_hair_epilogue.png", (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/b.png", (0, 0), "mod_assets/sayori_ptsd.png")
image sayori 3cemr = im.Composite((960, 960), (0, 0), "mod_assets/sayori_hair_epilogue.png", (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/c.png", (0, 0), "mod_assets/sayori_ptsd.png")
image sayori 3demr = im.Composite((960, 960), (0, 0), "mod_assets/sayori_hair_epilogue.png", (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/d.png", (0, 0), "mod_assets/sayori_ptsd.png")
image sayori 3eemr = im.Composite((960, 960), (0, 0), "mod_assets/sayori_hair_epilogue.png", (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/e.png", (0, 0), "mod_assets/sayori_ptsd.png")
image sayori 3femr = im.Composite((960, 960), (0, 0), "mod_assets/sayori_hair_epilogue.png", (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/f.png", (0, 0), "mod_assets/sayori_ptsd.png")
image sayori 3gemr = im.Composite((960, 960), (0, 0), "mod_assets/sayori_hair_epilogue.png", (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/g.png", (0, 0), "mod_assets/sayori_ptsd.png")
image sayori 3hemr = im.Composite((960, 960), (0, 0), "mod_assets/sayori_hair_epilogue.png", (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/h.png", (0, 0), "mod_assets/sayori_ptsd.png")
image sayori 3iemr = im.Composite((960, 960), (0, 0), "mod_assets/sayori_hair_epilogue.png", (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/i.png", (0, 0), "mod_assets/sayori_ptsd.png")
image sayori 3jemr = im.Composite((960, 960), (0, 0), "mod_assets/sayori_hair_epilogue.png", (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/j.png", (0, 0), "mod_assets/sayori_ptsd.png")
image sayori 3kemr = im.Composite((960, 960), (0, 0), "mod_assets/sayori_hair_epilogue.png", (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/k.png", (0, 0), "mod_assets/sayori_ptsd.png")
image sayori 3lemr = im.Composite((960, 960), (0, 0), "mod_assets/sayori_hair_epilogue.png", (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/l.png", (0, 0), "mod_assets/sayori_ptsd.png")
image sayori 3memr = im.Composite((960, 960), (0, 0), "mod_assets/sayori_hair_epilogue.png", (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/m.png", (0, 0), "mod_assets/sayori_ptsd.png")
image sayori 3nemr = im.Composite((960, 960), (0, 0), "mod_assets/sayori_hair_epilogue.png", (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/n.png", (0, 0), "mod_assets/sayori_ptsd.png")
image sayori 3oemr = im.Composite((960, 960), (0, 0), "mod_assets/sayori_hair_epilogue.png", (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/o.png", (0, 0), "mod_assets/sayori_ptsd.png")
image sayori 3pemr = im.Composite((960, 960), (0, 0), "mod_assets/sayori_hair_epilogue.png", (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/p.png", (0, 0), "mod_assets/sayori_ptsd.png")
image sayori 3qemr = im.Composite((960, 960), (0, 0), "mod_assets/sayori_hair_epilogue.png", (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/q.png", (0, 0), "mod_assets/sayori_ptsd.png")
image sayori 3remr = im.Composite((960, 960), (0, 0), "mod_assets/sayori_hair_epilogue.png", (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/r.png", (0, 0), "mod_assets/sayori_ptsd.png")
image sayori 3semr = im.Composite((960, 960), (0, 0), "mod_assets/sayori_hair_epilogue.png", (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/s.png", (0, 0), "mod_assets/sayori_ptsd.png")
image sayori 3temr = im.Composite((960, 960), (0, 0), "mod_assets/sayori_hair_epilogue.png", (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/t.png", (0, 0), "mod_assets/sayori_ptsd.png")
image sayori 3uemr = im.Composite((960, 960), (0, 0), "mod_assets/sayori_hair_epilogue.png", (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/u.png", (0, 0), "mod_assets/sayori_ptsd.png")
image sayori 3vemr = im.Composite((960, 960), (0, 0), "mod_assets/sayori_hair_epilogue.png", (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/v.png", (0, 0), "mod_assets/sayori_ptsd.png")
image sayori 3wemr = im.Composite((960, 960), (0, 0), "mod_assets/sayori_hair_epilogue.png", (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/w.png", (0, 0), "mod_assets/sayori_ptsd.png")
image sayori 3xemr = im.Composite((960, 960), (0, 0), "mod_assets/sayori_hair_epilogue.png", (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/x.png", (0, 0), "mod_assets/sayori_ptsd.png")
image sayori 3yemr = im.Composite((960, 960), (0, 0), "mod_assets/sayori_hair_epilogue.png", (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/y.png", (0, 0), "mod_assets/sayori_ptsd.png")

image sayori 4emr = im.Composite((960, 960), (0, 0), "mod_assets/sayori_hair_epilogue.png", (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/a.png", (0, 0), "mod_assets/sayori_ptsd.png")
image sayori 4aemr = im.Composite((960, 960), (0, 0), "mod_assets/sayori_hair_epilogue.png", (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/a.png", (0, 0), "mod_assets/sayori_ptsd.png")
image sayori 4bemr = im.Composite((960, 960), (0, 0), "mod_assets/sayori_hair_epilogue.png", (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/b.png", (0, 0), "mod_assets/sayori_ptsd.png")
image sayori 4cemr = im.Composite((960, 960), (0, 0), "mod_assets/sayori_hair_epilogue.png", (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/c.png", (0, 0), "mod_assets/sayori_ptsd.png")
image sayori 4demr = im.Composite((960, 960), (0, 0), "mod_assets/sayori_hair_epilogue.png", (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/d.png", (0, 0), "mod_assets/sayori_ptsd.png")
image sayori 4eemr = im.Composite((960, 960), (0, 0), "mod_assets/sayori_hair_epilogue.png", (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/e.png", (0, 0), "mod_assets/sayori_ptsd.png")
image sayori 4femr = im.Composite((960, 960), (0, 0), "mod_assets/sayori_hair_epilogue.png", (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/f.png", (0, 0), "mod_assets/sayori_ptsd.png")
image sayori 4gemr = im.Composite((960, 960), (0, 0), "mod_assets/sayori_hair_epilogue.png", (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/g.png", (0, 0), "mod_assets/sayori_ptsd.png")
image sayori 4hemr = im.Composite((960, 960), (0, 0), "mod_assets/sayori_hair_epilogue.png", (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/h.png", (0, 0), "mod_assets/sayori_ptsd.png")
image sayori 4iemr = im.Composite((960, 960), (0, 0), "mod_assets/sayori_hair_epilogue.png", (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/i.png", (0, 0), "mod_assets/sayori_ptsd.png")
image sayori 4jemr = im.Composite((960, 960), (0, 0), "mod_assets/sayori_hair_epilogue.png", (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/j.png", (0, 0), "mod_assets/sayori_ptsd.png")
image sayori 4kemr = im.Composite((960, 960), (0, 0), "mod_assets/sayori_hair_epilogue.png", (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/k.png", (0, 0), "mod_assets/sayori_ptsd.png")
image sayori 4lemr = im.Composite((960, 960), (0, 0), "mod_assets/sayori_hair_epilogue.png", (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/l.png", (0, 0), "mod_assets/sayori_ptsd.png")
image sayori 4memr = im.Composite((960, 960), (0, 0), "mod_assets/sayori_hair_epilogue.png", (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/m.png", (0, 0), "mod_assets/sayori_ptsd.png")
image sayori 4nemr = im.Composite((960, 960), (0, 0), "mod_assets/sayori_hair_epilogue.png", (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/n.png", (0, 0), "mod_assets/sayori_ptsd.png")
image sayori 4oemr = im.Composite((960, 960), (0, 0), "mod_assets/sayori_hair_epilogue.png", (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/o.png", (0, 0), "mod_assets/sayori_ptsd.png")
image sayori 4pemr = im.Composite((960, 960), (0, 0), "mod_assets/sayori_hair_epilogue.png", (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/p.png", (0, 0), "mod_assets/sayori_ptsd.png")
image sayori 4qemr = im.Composite((960, 960), (0, 0), "mod_assets/sayori_hair_epilogue.png", (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/q.png", (0, 0), "mod_assets/sayori_ptsd.png")
image sayori 4remr = im.Composite((960, 960), (0, 0), "mod_assets/sayori_hair_epilogue.png", (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/r.png", (0, 0), "mod_assets/sayori_ptsd.png")
image sayori 4semr = im.Composite((960, 960), (0, 0), "mod_assets/sayori_hair_epilogue.png", (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/s.png", (0, 0), "mod_assets/sayori_ptsd.png")
image sayori 4temr = im.Composite((960, 960), (0, 0), "mod_assets/sayori_hair_epilogue.png", (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/t.png", (0, 0), "mod_assets/sayori_ptsd.png")
image sayori 4uemr = im.Composite((960, 960), (0, 0), "mod_assets/sayori_hair_epilogue.png", (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/u.png", (0, 0), "mod_assets/sayori_ptsd.png")
image sayori 4vemr = im.Composite((960, 960), (0, 0), "mod_assets/sayori_hair_epilogue.png", (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/v.png", (0, 0), "mod_assets/sayori_ptsd.png")
image sayori 4wemr = im.Composite((960, 960), (0, 0), "mod_assets/sayori_hair_epilogue.png", (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/w.png", (0, 0), "mod_assets/sayori_ptsd.png")
image sayori 4xemr = im.Composite((960, 960), (0, 0), "mod_assets/sayori_hair_epilogue.png", (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/x.png", (0, 0), "mod_assets/sayori_ptsd.png")
image sayori 4yemr = im.Composite((960, 960), (0, 0), "mod_assets/sayori_hair_epilogue.png", (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/y.png", (0, 0), "mod_assets/sayori_ptsd.png")

image sayori 5emr = im.Composite((960, 960), (-40, 0), "mod_assets/sayori_hair_edit.png", (0, 0), "sayori/3a.png")
image sayori 5aemr = im.Composite((960, 960), (-40, 0), "mod_assets/sayori_hair_edit.png", (0, 0), "sayori/3a.png")
image sayori 5bemr = im.Composite((960, 960), (-40, 0), "mod_assets/sayori_hair_edit.png", (0, 0), "sayori/3b.png")
image sayori 5cemr = im.Composite((960, 960), (-40, 0), "mod_assets/sayori_hair_edit.png", (0, 0), "sayori/3c.png")
image sayori 5demr = im.Composite((960, 960), (-40, 0), "mod_assets/sayori_hair_edit.png", (0, 0), "sayori/3d.png")

# Sayori in her Casual Outfit [Day 4]
image sayori 1baemr = im.Composite((960, 960), (0, 0), "mod_assets/sayori_hair_epilogue.png", (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/a.png", (0, 0), "mod_assets/sayori_ptsd.png")
image sayori 1bbemr = im.Composite((960, 960), (0, 0), "mod_assets/sayori_hair_epilogue.png", (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/b.png", (0, 0), "mod_assets/sayori_ptsd.png")
image sayori 1bcemr = im.Composite((960, 960), (0, 0), "mod_assets/sayori_hair_epilogue.png", (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/c.png", (0, 0), "mod_assets/sayori_ptsd.png")
image sayori 1bdemr = im.Composite((960, 960), (0, 0), "mod_assets/sayori_hair_epilogue.png", (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/d.png", (0, 0), "mod_assets/sayori_ptsd.png")
image sayori 1beemr = im.Composite((960, 960), (0, 0), "mod_assets/sayori_hair_epilogue.png", (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/e.png", (0, 0), "mod_assets/sayori_ptsd.png")
image sayori 1bfemr = im.Composite((960, 960), (0, 0), "mod_assets/sayori_hair_epilogue.png", (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/f.png", (0, 0), "mod_assets/sayori_ptsd.png")
image sayori 1bgemr = im.Composite((960, 960), (0, 0), "mod_assets/sayori_hair_epilogue.png", (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/g.png", (0, 0), "mod_assets/sayori_ptsd.png")
image sayori 1bhemr = im.Composite((960, 960), (0, 0), "mod_assets/sayori_hair_epilogue.png", (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/h.png", (0, 0), "mod_assets/sayori_ptsd.png")
image sayori 1biemr = im.Composite((960, 960), (0, 0), "mod_assets/sayori_hair_epilogue.png", (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/i.png", (0, 0), "mod_assets/sayori_ptsd.png")
image sayori 1bjemr = im.Composite((960, 960), (0, 0), "mod_assets/sayori_hair_epilogue.png", (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/j.png", (0, 0), "mod_assets/sayori_ptsd.png")
image sayori 1bkemr = im.Composite((960, 960), (0, 0), "mod_assets/sayori_hair_epilogue.png", (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/k.png", (0, 0), "mod_assets/sayori_ptsd.png")
image sayori 1blemr = im.Composite((960, 960), (0, 0), "mod_assets/sayori_hair_epilogue.png", (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/l.png", (0, 0), "mod_assets/sayori_ptsd.png")
image sayori 1bmemr = im.Composite((960, 960), (0, 0), "mod_assets/sayori_hair_epilogue.png", (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/m.png", (0, 0), "mod_assets/sayori_ptsd.png")
image sayori 1bnemr = im.Composite((960, 960), (0, 0), "mod_assets/sayori_hair_epilogue.png", (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/n.png", (0, 0), "mod_assets/sayori_ptsd.png")
image sayori 1boemr = im.Composite((960, 960), (0, 0), "mod_assets/sayori_hair_epilogue.png", (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/o.png", (0, 0), "mod_assets/sayori_ptsd.png")
image sayori 1bpemr = im.Composite((960, 960), (0, 0), "mod_assets/sayori_hair_epilogue.png", (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/p.png", (0, 0), "mod_assets/sayori_ptsd.png")
image sayori 1bqemr = im.Composite((960, 960), (0, 0), "mod_assets/sayori_hair_epilogue.png", (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/q.png", (0, 0), "mod_assets/sayori_ptsd.png")
image sayori 1bremr = im.Composite((960, 960), (0, 0), "mod_assets/sayori_hair_epilogue.png", (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/r.png", (0, 0), "mod_assets/sayori_ptsd.png")
image sayori 1bsemr = im.Composite((960, 960), (0, 0), "mod_assets/sayori_hair_epilogue.png", (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/s.png", (0, 0), "mod_assets/sayori_ptsd.png")
image sayori 1btemr = im.Composite((960, 960), (0, 0), "mod_assets/sayori_hair_epilogue.png", (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/t.png", (0, 0), "mod_assets/sayori_ptsd.png")
image sayori 1buemr = im.Composite((960, 960), (0, 0), "mod_assets/sayori_hair_epilogue.png", (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/u.png", (0, 0), "mod_assets/sayori_ptsd.png")
image sayori 1bvemr = im.Composite((960, 960), (0, 0), "mod_assets/sayori_hair_epilogue.png", (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/v.png", (0, 0), "mod_assets/sayori_ptsd.png")
image sayori 1bwemr = im.Composite((960, 960), (0, 0), "mod_assets/sayori_hair_epilogue.png", (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/w.png", (0, 0), "mod_assets/sayori_ptsd.png")
image sayori 1bxemr = im.Composite((960, 960), (0, 0), "mod_assets/sayori_hair_epilogue.png", (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/x.png", (0, 0), "mod_assets/sayori_ptsd.png")
image sayori 1byemr = im.Composite((960, 960), (0, 0), "mod_assets/sayori_hair_epilogue.png", (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/y.png", (0, 0), "mod_assets/sayori_ptsd.png")

image sayori 2baemr = im.Composite((960, 960), (0, 0), "mod_assets/sayori_hair_epilogue.png", (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/a.png", (0, 0), "mod_assets/sayori_ptsd.png")
image sayori 2bbemr = im.Composite((960, 960), (0, 0), "mod_assets/sayori_hair_epilogue.png", (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/b.png", (0, 0), "mod_assets/sayori_ptsd.png")
image sayori 2bcemr = im.Composite((960, 960), (0, 0), "mod_assets/sayori_hair_epilogue.png", (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/c.png", (0, 0), "mod_assets/sayori_ptsd.png")
image sayori 2bdemr = im.Composite((960, 960), (0, 0), "mod_assets/sayori_hair_epilogue.png", (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/d.png", (0, 0), "mod_assets/sayori_ptsd.png")
image sayori 2beemr = im.Composite((960, 960), (0, 0), "mod_assets/sayori_hair_epilogue.png", (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/e.png", (0, 0), "mod_assets/sayori_ptsd.png")
image sayori 2bfemr = im.Composite((960, 960), (0, 0), "mod_assets/sayori_hair_epilogue.png", (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/f.png", (0, 0), "mod_assets/sayori_ptsd.png")
image sayori 2bgemr = im.Composite((960, 960), (0, 0), "mod_assets/sayori_hair_epilogue.png", (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/g.png", (0, 0), "mod_assets/sayori_ptsd.png")
image sayori 2bhemr = im.Composite((960, 960), (0, 0), "mod_assets/sayori_hair_epilogue.png", (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/h.png", (0, 0), "mod_assets/sayori_ptsd.png")
image sayori 2biemr = im.Composite((960, 960), (0, 0), "mod_assets/sayori_hair_epilogue.png", (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/i.png", (0, 0), "mod_assets/sayori_ptsd.png")
image sayori 2bjemr = im.Composite((960, 960), (0, 0), "mod_assets/sayori_hair_epilogue.png", (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/j.png", (0, 0), "mod_assets/sayori_ptsd.png")
image sayori 2bkemr = im.Composite((960, 960), (0, 0), "mod_assets/sayori_hair_epilogue.png", (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/k.png", (0, 0), "mod_assets/sayori_ptsd.png")
image sayori 2blemr = im.Composite((960, 960), (0, 0), "mod_assets/sayori_hair_epilogue.png", (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/l.png", (0, 0), "mod_assets/sayori_ptsd.png")
image sayori 2bmemr = im.Composite((960, 960), (0, 0), "mod_assets/sayori_hair_epilogue.png", (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/m.png", (0, 0), "mod_assets/sayori_ptsd.png")
image sayori 2bnemr = im.Composite((960, 960), (0, 0), "mod_assets/sayori_hair_epilogue.png", (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/n.png", (0, 0), "mod_assets/sayori_ptsd.png")
image sayori 2boemr = im.Composite((960, 960), (0, 0), "mod_assets/sayori_hair_epilogue.png", (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/o.png", (0, 0), "mod_assets/sayori_ptsd.png")
image sayori 2bpemr = im.Composite((960, 960), (0, 0), "mod_assets/sayori_hair_epilogue.png", (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/p.png", (0, 0), "mod_assets/sayori_ptsd.png")
image sayori 2bqemr = im.Composite((960, 960), (0, 0), "mod_assets/sayori_hair_epilogue.png", (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/q.png", (0, 0), "mod_assets/sayori_ptsd.png")
image sayori 2bremr = im.Composite((960, 960), (0, 0), "mod_assets/sayori_hair_epilogue.png", (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/r.png", (0, 0), "mod_assets/sayori_ptsd.png")
image sayori 2bsemr = im.Composite((960, 960), (0, 0), "mod_assets/sayori_hair_epilogue.png", (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/s.png", (0, 0), "mod_assets/sayori_ptsd.png")
image sayori 2btemr = im.Composite((960, 960), (0, 0), "mod_assets/sayori_hair_epilogue.png", (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/t.png", (0, 0), "mod_assets/sayori_ptsd.png")
image sayori 2buemr = im.Composite((960, 960), (0, 0), "mod_assets/sayori_hair_epilogue.png", (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/u.png", (0, 0), "mod_assets/sayori_ptsd.png")
image sayori 2bvemr = im.Composite((960, 960), (0, 0), "mod_assets/sayori_hair_epilogue.png", (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/v.png", (0, 0), "mod_assets/sayori_ptsd.png")
image sayori 2bwemr = im.Composite((960, 960), (0, 0), "mod_assets/sayori_hair_epilogue.png", (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/w.png", (0, 0), "mod_assets/sayori_ptsd.png")
image sayori 2bxemr = im.Composite((960, 960), (0, 0), "mod_assets/sayori_hair_epilogue.png", (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/x.png", (0, 0), "mod_assets/sayori_ptsd.png")
image sayori 2byemr = im.Composite((960, 960), (0, 0), "mod_assets/sayori_hair_epilogue.png", (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/y.png", (0, 0), "mod_assets/sayori_ptsd.png")

image sayori 3baemr = im.Composite((960, 960), (0, 0), "mod_assets/sayori_hair_epilogue.png", (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/a.png", (0, 0), "mod_assets/sayori_ptsd.png")
image sayori 3bbemr = im.Composite((960, 960), (0, 0), "mod_assets/sayori_hair_epilogue.png", (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/b.png", (0, 0), "mod_assets/sayori_ptsd.png")
image sayori 3bcemr = im.Composite((960, 960), (0, 0), "mod_assets/sayori_hair_epilogue.png", (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/c.png", (0, 0), "mod_assets/sayori_ptsd.png")
image sayori 3bdemr = im.Composite((960, 960), (0, 0), "mod_assets/sayori_hair_epilogue.png", (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/d.png", (0, 0), "mod_assets/sayori_ptsd.png")
image sayori 3beemr = im.Composite((960, 960), (0, 0), "mod_assets/sayori_hair_epilogue.png", (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/e.png", (0, 0), "mod_assets/sayori_ptsd.png")
image sayori 3bfemr = im.Composite((960, 960), (0, 0), "mod_assets/sayori_hair_epilogue.png", (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/f.png", (0, 0), "mod_assets/sayori_ptsd.png")
image sayori 3bgemr = im.Composite((960, 960), (0, 0), "mod_assets/sayori_hair_epilogue.png", (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/g.png", (0, 0), "mod_assets/sayori_ptsd.png")
image sayori 3bhemr = im.Composite((960, 960), (0, 0), "mod_assets/sayori_hair_epilogue.png", (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/h.png", (0, 0), "mod_assets/sayori_ptsd.png")
image sayori 3biemr = im.Composite((960, 960), (0, 0), "mod_assets/sayori_hair_epilogue.png", (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/i.png", (0, 0), "mod_assets/sayori_ptsd.png")
image sayori 3bjemr = im.Composite((960, 960), (0, 0), "mod_assets/sayori_hair_epilogue.png", (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/j.png", (0, 0), "mod_assets/sayori_ptsd.png")
image sayori 3bkemr = im.Composite((960, 960), (0, 0), "mod_assets/sayori_hair_epilogue.png", (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/k.png", (0, 0), "mod_assets/sayori_ptsd.png")
image sayori 3blemr = im.Composite((960, 960), (0, 0), "mod_assets/sayori_hair_epilogue.png", (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/l.png", (0, 0), "mod_assets/sayori_ptsd.png")
image sayori 3bmemr = im.Composite((960, 960), (0, 0), "mod_assets/sayori_hair_epilogue.png", (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/m.png", (0, 0), "mod_assets/sayori_ptsd.png")
image sayori 3bnemr = im.Composite((960, 960), (0, 0), "mod_assets/sayori_hair_epilogue.png", (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/n.png", (0, 0), "mod_assets/sayori_ptsd.png")
image sayori 3boemr = im.Composite((960, 960), (0, 0), "mod_assets/sayori_hair_epilogue.png", (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/o.png", (0, 0), "mod_assets/sayori_ptsd.png")
image sayori 3bpemr = im.Composite((960, 960), (0, 0), "mod_assets/sayori_hair_epilogue.png", (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/p.png", (0, 0), "mod_assets/sayori_ptsd.png")
image sayori 3bqemr = im.Composite((960, 960), (0, 0), "mod_assets/sayori_hair_epilogue.png", (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/q.png", (0, 0), "mod_assets/sayori_ptsd.png")
image sayori 3bremr = im.Composite((960, 960), (0, 0), "mod_assets/sayori_hair_epilogue.png", (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/r.png", (0, 0), "mod_assets/sayori_ptsd.png")
image sayori 3bsemr = im.Composite((960, 960), (0, 0), "mod_assets/sayori_hair_epilogue.png", (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/s.png", (0, 0), "mod_assets/sayori_ptsd.png")
image sayori 3btemr = im.Composite((960, 960), (0, 0), "mod_assets/sayori_hair_epilogue.png", (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/t.png", (0, 0), "mod_assets/sayori_ptsd.png")
image sayori 3buemr = im.Composite((960, 960), (0, 0), "mod_assets/sayori_hair_epilogue.png", (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/u.png", (0, 0), "mod_assets/sayori_ptsd.png")
image sayori 3bvemr = im.Composite((960, 960), (0, 0), "mod_assets/sayori_hair_epilogue.png", (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/v.png", (0, 0), "mod_assets/sayori_ptsd.png")
image sayori 3bwemr = im.Composite((960, 960), (0, 0), "mod_assets/sayori_hair_epilogue.png", (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/w.png", (0, 0), "mod_assets/sayori_ptsd.png")
image sayori 3bxemr = im.Composite((960, 960), (0, 0), "mod_assets/sayori_hair_epilogue.png", (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/x.png", (0, 0), "mod_assets/sayori_ptsd.png")
image sayori 3byemr = im.Composite((960, 960), (0, 0), "mod_assets/sayori_hair_epilogue.png", (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/y.png", (0, 0), "mod_assets/sayori_ptsd.png")

image sayori 4baemr = im.Composite((960, 960), (0, 0), "mod_assets/sayori_hair_epilogue.png", (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/a.png", (0, 0), "mod_assets/sayori_ptsd.png")
image sayori 4bbemr = im.Composite((960, 960), (0, 0), "mod_assets/sayori_hair_epilogue.png", (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/b.png", (0, 0), "mod_assets/sayori_ptsd.png")
image sayori 4bcemr = im.Composite((960, 960), (0, 0), "mod_assets/sayori_hair_epilogue.png", (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/c.png", (0, 0), "mod_assets/sayori_ptsd.png")
image sayori 4bdemr = im.Composite((960, 960), (0, 0), "mod_assets/sayori_hair_epilogue.png", (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/d.png", (0, 0), "mod_assets/sayori_ptsd.png")
image sayori 4beemr = im.Composite((960, 960), (0, 0), "mod_assets/sayori_hair_epilogue.png", (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/e.png", (0, 0), "mod_assets/sayori_ptsd.png")
image sayori 4bfemr = im.Composite((960, 960), (0, 0), "mod_assets/sayori_hair_epilogue.png", (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/f.png", (0, 0), "mod_assets/sayori_ptsd.png")
image sayori 4bgemr = im.Composite((960, 960), (0, 0), "mod_assets/sayori_hair_epilogue.png", (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/g.png", (0, 0), "mod_assets/sayori_ptsd.png")
image sayori 4bhemr = im.Composite((960, 960), (0, 0), "mod_assets/sayori_hair_epilogue.png", (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/h.png", (0, 0), "mod_assets/sayori_ptsd.png")
image sayori 4biemr = im.Composite((960, 960), (0, 0), "mod_assets/sayori_hair_epilogue.png", (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/i.png", (0, 0), "mod_assets/sayori_ptsd.png")
image sayori 4bjemr = im.Composite((960, 960), (0, 0), "mod_assets/sayori_hair_epilogue.png", (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/j.png", (0, 0), "mod_assets/sayori_ptsd.png")
image sayori 4bkemr = im.Composite((960, 960), (0, 0), "mod_assets/sayori_hair_epilogue.png", (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/k.png", (0, 0), "mod_assets/sayori_ptsd.png")
image sayori 4blemr = im.Composite((960, 960), (0, 0), "mod_assets/sayori_hair_epilogue.png", (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/l.png", (0, 0), "mod_assets/sayori_ptsd.png")
image sayori 4bmemr = im.Composite((960, 960), (0, 0), "mod_assets/sayori_hair_epilogue.png", (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/m.png", (0, 0), "mod_assets/sayori_ptsd.png")
image sayori 4bnemr = im.Composite((960, 960), (0, 0), "mod_assets/sayori_hair_epilogue.png", (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/n.png", (0, 0), "mod_assets/sayori_ptsd.png")
image sayori 4boemr = im.Composite((960, 960), (0, 0), "mod_assets/sayori_hair_epilogue.png", (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/o.png", (0, 0), "mod_assets/sayori_ptsd.png")
image sayori 4bpemr = im.Composite((960, 960), (0, 0), "mod_assets/sayori_hair_epilogue.png", (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/p.png", (0, 0), "mod_assets/sayori_ptsd.png")
image sayori 4bqemr = im.Composite((960, 960), (0, 0), "mod_assets/sayori_hair_epilogue.png", (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/q.png", (0, 0), "mod_assets/sayori_ptsd.png")
image sayori 4bremr = im.Composite((960, 960), (0, 0), "mod_assets/sayori_hair_epilogue.png", (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/r.png", (0, 0), "mod_assets/sayori_ptsd.png")
image sayori 4bsemr = im.Composite((960, 960), (0, 0), "mod_assets/sayori_hair_epilogue.png", (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/s.png", (0, 0), "mod_assets/sayori_ptsd.png")
image sayori 4btemr = im.Composite((960, 960), (0, 0), "mod_assets/sayori_hair_epilogue.png", (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/t.png", (0, 0), "mod_assets/sayori_ptsd.png")
image sayori 4buemr = im.Composite((960, 960), (0, 0), "mod_assets/sayori_hair_epilogue.png", (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/u.png", (0, 0), "mod_assets/sayori_ptsd.png")
image sayori 4bvemr = im.Composite((960, 960), (0, 0), "mod_assets/sayori_hair_epilogue.png", (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/v.png", (0, 0), "mod_assets/sayori_ptsd.png")
image sayori 4bwemr = im.Composite((960, 960), (0, 0), "mod_assets/sayori_hair_epilogue.png", (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/w.png", (0, 0), "mod_assets/sayori_ptsd.png")
image sayori 4bxemr = im.Composite((960, 960), (0, 0), "mod_assets/sayori_hair_epilogue.png", (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/x.png", (0, 0), "mod_assets/sayori_ptsd.png")
image sayori 4byemr = im.Composite((960, 960), (0, 0), "mod_assets/sayori_hair_epilogue.png", (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/y.png", (0, 0), "mod_assets/sayori_ptsd.png")

#Sayori depressed expressions by JohnRDVSMarston WITH EMR HAIR

image sayori 41aemr = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/41a.png")
image sayori 41bemr = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/41b.png")
image sayori 41cemr = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/41c.png")
image sayori 41demr = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/41d.png")
image sayori 41eemr = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/41e.png")
image sayori 41femr = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/41f.png")
image sayori 41gemr = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/41g.png")
image sayori 41hemr = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/41h.png")
image sayori 41iemr = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/41i.png")

image sayori 42aemr = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/42a.png")
image sayori 42bemr = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/42b.png")
image sayori 42cemr = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/42c.png")
image sayori 42demr = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/42d.png")
image sayori 42eemr = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/42e.png")
image sayori 42femr = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/42f.png")
image sayori 42gemr = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/42g.png")
image sayori 42hemr = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/42h.png")
image sayori 42iemr = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/42i.png")

image sayori 43aemr = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/43a.png")
image sayori 43bemr = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/43b.png")
image sayori 43cemr = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/43c.png")
image sayori 43demr = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/43d.png")
image sayori 43eemr = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/43e.png")
image sayori 43femr = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/43f.png")
image sayori 43gemr = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/43g.png")
image sayori 43hemr = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/43h.png")
image sayori 43iemr = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/43i.png")

image sayori 44aemr = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/44a.png")
image sayori 44bemr = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/44b.png")
image sayori 44cemr = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/44c.png")
image sayori 44demr = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/44d.png")
image sayori 44eemr = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/44e.png")
image sayori 44femr = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/44f.png")
image sayori 44gemr = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/44g.png")
image sayori 44hemr = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/44h.png")
image sayori 44iemr = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/44i.png")

image sayori 45aemr = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/45a.png")
image sayori 45bemr = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/45b.png")
image sayori 45cemr = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/45c.png")
image sayori 45demr = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/45d.png")
image sayori 45eemr = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/45e.png")
image sayori 45femr = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/45f.png")
image sayori 45gemr = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/45g.png")
image sayori 45hemr = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/45h.png")
image sayori 45iemr = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/45i.png")

image sayori 46aemr = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/46a.png")
image sayori 46bemr = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/46b.png")
image sayori 46cemr = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/46c.png")
image sayori 46demr = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/46d.png")
image sayori 46eemr = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/46e.png")
image sayori 46femr = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/46f.png")
image sayori 46gemr = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/46g.png")
image sayori 46hemr = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/46h.png")
image sayori 46iemr = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/46i.png")

image sayori 47aemr = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/47a.png")
image sayori 47bemr = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/47b.png")
image sayori 47cemr = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/47c.png")
image sayori 47demr = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/47d.png")
image sayori 47eemr = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/47e.png")
image sayori 47femr = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/47f.png")
image sayori 47gemr = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/47g.png")
image sayori 47hemr = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/47h.png")
image sayori 47iemr = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/47i.png")

image sayori 48aemr = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/48a.png")
image sayori 48bemr = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/48b.png")
image sayori 48cemr = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/48c.png")
image sayori 48demr = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/48d.png")
image sayori 48eemr = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/48e.png")
image sayori 48femr = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/48f.png")
image sayori 48gemr = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/48g.png")
image sayori 48hemr = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/48h.png")
image sayori 48iemr = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/48i.png")

image sayori 41abowemr = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/41a.png",  (0, 0), "sayori/bow.png")
image sayori 41bbowemr = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/41b.png",  (0, 0), "sayori/bow.png")
image sayori 41cbowemr = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/41c.png",  (0, 0), "sayori/bow.png")
image sayori 41dbowemr = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/41d.png",  (0, 0), "sayori/bow.png")
image sayori 41ebowemr = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/41e.png",  (0, 0), "sayori/bow.png")
image sayori 41fbowemr = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/41f.png",  (0, 0), "sayori/bow.png")
image sayori 41gbowemr = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/41g.png",  (0, 0), "sayori/bow.png")
image sayori 41hbowemr = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/41h.png",  (0, 0), "sayori/bow.png")
image sayori 41ibowemr = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/41i.png",  (0, 0), "sayori/bow.png")

image sayori 42abowemr = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/42a.png",  (0, 0), "sayori/bow.png")
image sayori 42bbowemr = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/42b.png",  (0, 0), "sayori/bow.png")
image sayori 42cbowemr = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/42c.png",  (0, 0), "sayori/bow.png")
image sayori 42dbowemr = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/42d.png",  (0, 0), "sayori/bow.png")
image sayori 42ebowemr = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/42e.png",  (0, 0), "sayori/bow.png")
image sayori 42fbowemr = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/42f.png",  (0, 0), "sayori/bow.png")
image sayori 42gbowemr = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/42g.png",  (0, 0), "sayori/bow.png")
image sayori 42hbowemr = im.Composite((960, 960),(0, 0), "mod_assets/sayori_hair_edit.png", (0, 0), "sayori/4.png", (0, 0), "sayori/42h.png",  (0, 0), "sayori/bow.png", (0, 0), "mod_assets/sayori_ptsd.png")
image sayori 42ibowemr = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/42i.png",  (0, 0), "sayori/bow.png")

image sayori 43abowemr = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/43a.png",  (0, 0), "sayori/bow.png")
image sayori 43bbowemr = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/43b.png",  (0, 0), "sayori/bow.png")
image sayori 43cbowemr = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/43c.png",  (0, 0), "sayori/bow.png")
image sayori 43dbowemr = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/43d.png",  (0, 0), "sayori/bow.png")
image sayori 43ebowemr = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/43e.png",  (0, 0), "sayori/bow.png")
image sayori 43fbowemr = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/43f.png",  (0, 0), "sayori/bow.png")
image sayori 43gbowemr = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/43g.png",  (0, 0), "sayori/bow.png")
image sayori 43hbowemr = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/43h.png",  (0, 0), "sayori/bow.png")
image sayori 43ibowemr = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/43i.png",  (0, 0), "sayori/bow.png")

image sayori 44abowemr = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/44a.png",  (0, 0), "sayori/bow.png")
image sayori 44bbowemr = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/44b.png",  (0, 0), "sayori/bow.png")
image sayori 44cbowemr = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/44c.png",  (0, 0), "sayori/bow.png")
image sayori 44dbowemr = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/44d.png",  (0, 0), "sayori/bow.png")
image sayori 44ebowemr = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/44e.png",  (0, 0), "sayori/bow.png")
image sayori 44fbowemr = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/44f.png",  (0, 0), "sayori/bow.png")
image sayori 44gbowemr = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/44g.png",  (0, 0), "sayori/bow.png")
image sayori 44hbowemr = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/44h.png",  (0, 0), "sayori/bow.png")
image sayori 44ibowemr = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/44i.png",  (0, 0), "sayori/bow.png")

image sayori 45abowemr = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/45a.png",  (0, 0), "sayori/bow.png")
image sayori 45bbowemr = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/45b.png",  (0, 0), "sayori/bow.png")
image sayori 45cbowemr = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/45c.png",  (0, 0), "sayori/bow.png")
image sayori 45dbowemr = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/45d.png",  (0, 0), "sayori/bow.png")
image sayori 45ebowemr = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/45e.png",  (0, 0), "sayori/bow.png")
image sayori 45fbowemr = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/45f.png",  (0, 0), "sayori/bow.png")
image sayori 45gbowemr = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/45g.png",  (0, 0), "sayori/bow.png")
image sayori 45hbowemr = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/45h.png",  (0, 0), "sayori/bow.png")
image sayori 45ibowemr = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/45i.png",  (0, 0), "sayori/bow.png")

image sayori 46abowemr = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/46a.png",  (0, 0), "sayori/bow.png")
image sayori 46bbowemr = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/46b.png",  (0, 0), "sayori/bow.png")
image sayori 46cbowemr = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/46c.png",  (0, 0), "sayori/bow.png")
image sayori 46dbowemr = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/46d.png",  (0, 0), "sayori/bow.png")
image sayori 46ebowemr = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/46e.png",  (0, 0), "sayori/bow.png")
image sayori 46fbowemr = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/46f.png",  (0, 0), "sayori/bow.png")
image sayori 46gbowemr = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/46g.png",  (0, 0), "sayori/bow.png")
image sayori 46hbowemr = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/46h.png",  (0, 0), "sayori/bow.png")
image sayori 46ibowemr = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/46i.png",  (0, 0), "sayori/bow.png")

image sayori 47abowemr = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/47a.png",  (0, 0), "sayori/bow.png")
image sayori 47bbowemr = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/47b.png",  (0, 0), "sayori/bow.png")
image sayori 47cbowemr = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/47c.png",  (0, 0), "sayori/bow.png")
image sayori 47dbowemr = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/47d.png",  (0, 0), "sayori/bow.png")
image sayori 47ebowemr = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/47e.png",  (0, 0), "sayori/bow.png")
image sayori 47fbowemr = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/47f.png",  (0, 0), "sayori/bow.png")
image sayori 47gbowemr = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/47g.png",  (0, 0), "sayori/bow.png")
image sayori 47hbowemr = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/47h.png",  (0, 0), "sayori/bow.png")
image sayori 47ibowemr = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/47i.png",  (0, 0), "sayori/bow.png")

image sayori 48abowemr = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/48a.png",  (0, 0), "sayori/bow.png")
image sayori 48bbowemr = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/48b.png",  (0, 0), "sayori/bow.png")
image sayori 48cbowemr = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/48c.png",  (0, 0), "sayori/bow.png")
image sayori 48dbowemr = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/48d.png",  (0, 0), "sayori/bow.png")
image sayori 48ebowemr = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/48e.png",  (0, 0), "sayori/bow.png")
image sayori 48fbowemr = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/48f.png",  (0, 0), "sayori/bow.png")
image sayori 48gbowemr = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/48g.png",  (0, 0), "sayori/bow.png")
image sayori 48hbowemr = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/48h.png",  (0, 0), "sayori/bow.png")
image sayori 48ibowemr = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/48i.png",  (0, 0), "sayori/bow.png")

image sayori 4b1aemr = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/41a.png")
image sayori 4b1bemr = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/41b.png")
image sayori 4b1cemr = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/41c.png")
image sayori 4b1demr = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/41d.png")
image sayori 4b1eemr = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/41e.png")
image sayori 4b1femr = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/41f.png")
image sayori 4b1gemr = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/41g.png")
image sayori 4b1hemr = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/41h.png")
image sayori 4b1iemr = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/41i.png")

image sayori 4b2aemr = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/42a.png")
image sayori 4b2bemr = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/42b.png")
image sayori 4b2cemr = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/42c.png")
image sayori 4b2demr = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/42d.png")
image sayori 4b2eemr = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/42e.png")
image sayori 4b2femr = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/42f.png")
image sayori 4b2gemr = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/42g.png")
image sayori 4b2hemr = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/42h.png")
image sayori 4b2iemr = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/42i.png")

image sayori 4b3aemr = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/43a.png")
image sayori 4b3bemr = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/43b.png")
image sayori 4b3cemr = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/43c.png")
image sayori 4b3demr = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/43d.png")
image sayori 4b3eemr = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/43e.png")
image sayori 4b3femr = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/43f.png")
image sayori 4b3gemr = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/43g.png")
image sayori 4b3hemr = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/43h.png")
image sayori 4b3i = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/43i.png")

image sayori 4b4aemr = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/44a.png")
image sayori 4b4bemr = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/44b.png")
image sayori 4b4cemr = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/44c.png")
image sayori 4b4demr = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/44d.png")
image sayori 4b4eemr = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/44e.png")
image sayori 4b4femr = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/44f.png")
image sayori 4b4gemr = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/44g.png")
image sayori 4b4hemr = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/44h.png")
image sayori 4b4iemr = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/44i.png")

image sayori 4b5aemr = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/45a.png")
image sayori 4b5bemr = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/45b.png")
image sayori 4b5cemr = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/45c.png")
image sayori 4b5demr = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/45d.png")
image sayori 4b5eemr = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/45e.png")
image sayori 4b5femr = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/45f.png")
image sayori 4b5gemr = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/45g.png")
image sayori 4b5hemr = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/45h.png")
image sayori 4b5iemr = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/45i.png")

image sayori 4b6aemr = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/46a.png")
image sayori 4b6bemr = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/46b.png")
image sayori 4b6cemr = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/46c.png")
image sayori 4b6demr = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/46d.png")
image sayori 4b6eemr = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/46e.png")
image sayori 4b6femr = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/46f.png")
image sayori 4b6gemr = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/46g.png")
image sayori 4b6hemr = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/46h.png")
image sayori 4b6iemr = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/46i.png")

image sayori 4b7aemr = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/47a.png")
image sayori 4b7bemr = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/47b.png")
image sayori 4b7cemr = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/47c.png")
image sayori 4b7demr = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/47d.png")
image sayori 4b7eemr = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/47e.png")
image sayori 4b7femr = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/47f.png")
image sayori 4b7gemr = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/47g.png")
image sayori 4b7hemr = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/47h.png")
image sayori 4b7iemr = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/47i.png")

image sayori 4b8aemr = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/48a.png")
image sayori 4b8bemr = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/48b.png")
image sayori 4b8cemr = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/48c.png")
image sayori 4b8demr = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/48d.png")
image sayori 4b8eemr = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/48e.png")
image sayori 4b8femr = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/48f.png")
image sayori 4b8gemr = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/48g.png")
image sayori 4b8hemr = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/48h.png")
image sayori 4b8iemr = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/48i.png")

image sayori 4b1abowemr = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/41a.png",  (0, 0), "sayori/bow.png")
image sayori 4b1bbowemr = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/41b.png",  (0, 0), "sayori/bow.png")
image sayori 4b1cbowemr = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/41c.png",  (0, 0), "sayori/bow.png")
image sayori 4b1dbowemr = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/41d.png",  (0, 0), "sayori/bow.png")
image sayori 4b1ebowemr = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/41e.png",  (0, 0), "sayori/bow.png")
image sayori 4b1fbowemr = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/41f.png",  (0, 0), "sayori/bow.png")
image sayori 4b1gbowemr = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/41g.png",  (0, 0), "sayori/bow.png")
image sayori 4b1hbowemr = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/41h.png",  (0, 0), "sayori/bow.png")
image sayori 4b1ibowemr = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/41i.png",  (0, 0), "sayori/bow.png")

image sayori 4b2abowemr = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/42a.png",  (0, 0), "sayori/bow.png")
image sayori 4b2bbowemr = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/42b.png",  (0, 0), "sayori/bow.png")
image sayori 4b2cbowemr = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/42c.png",  (0, 0), "sayori/bow.png")
image sayori 4b2dbowemr = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/42d.png",  (0, 0), "sayori/bow.png")
image sayori 4b2ebowemr = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/42e.png",  (0, 0), "sayori/bow.png")
image sayori 4b2fbowemr = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/42f.png",  (0, 0), "sayori/bow.png")
image sayori 4b2gbowemr = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/42g.png",  (0, 0), "sayori/bow.png")
image sayori 4b2hbowemr = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/42h.png",  (0, 0), "sayori/bow.png")
image sayori 4b2ibowemr = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/42i.png",  (0, 0), "sayori/bow.png")

image sayori 4b3abowemr = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/43a.png",  (0, 0), "sayori/bow.png")
image sayori 4b3bbowemr = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/43b.png",  (0, 0), "sayori/bow.png")
image sayori 4b3cbowemr = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/43c.png",  (0, 0), "sayori/bow.png")
image sayori 4b3dbowemr = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/43d.png",  (0, 0), "sayori/bow.png")
image sayori 4b3ebowemr = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/43e.png",  (0, 0), "sayori/bow.png")
image sayori 4b3fbowemr = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/43f.png",  (0, 0), "sayori/bow.png")
image sayori 4b3gbowemr = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/43g.png",  (0, 0), "sayori/bow.png")
image sayori 4b3hbowemr = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/43h.png",  (0, 0), "sayori/bow.png")
image sayori 4b3ibowemr = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/43i.png",  (0, 0), "sayori/bow.png")

image sayori 4b4abowemr = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/44a.png",  (0, 0), "sayori/bow.png")
image sayori 4b4bbowemr = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/44b.png",  (0, 0), "sayori/bow.png")
image sayori 4b4cbowemr = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/44c.png",  (0, 0), "sayori/bow.png")
image sayori 4b4dbowemr = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/44d.png",  (0, 0), "sayori/bow.png")
image sayori 4b4ebowemr = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/44e.png",  (0, 0), "sayori/bow.png")
image sayori 4b4fbowemr = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/44f.png",  (0, 0), "sayori/bow.png")
image sayori 4b4gbowemr = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/44g.png",  (0, 0), "sayori/bow.png")
image sayori 4b4hbowemr = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/44h.png",  (0, 0), "sayori/bow.png")
image sayori 4b4ibowemr = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/44i.png",  (0, 0), "sayori/bow.png")

image sayori 4b5abowemr = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/45a.png",  (0, 0), "sayori/bow.png")
image sayori 4b5bbowemr = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/45b.png",  (0, 0), "sayori/bow.png")
image sayori 4b5cbowemr = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/45c.png",  (0, 0), "sayori/bow.png")
image sayori 4b5dbowemr = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/45d.png",  (0, 0), "sayori/bow.png")
image sayori 4b5ebowemr = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/45e.png",  (0, 0), "sayori/bow.png")
image sayori 4b5fbowemr = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/45f.png",  (0, 0), "sayori/bow.png")
image sayori 4b5gbowemr = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/45g.png",  (0, 0), "sayori/bow.png")
image sayori 4b5hbowemr = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/45h.png",  (0, 0), "sayori/bow.png")
image sayori 4b5ibowemr = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/45i.png",  (0, 0), "sayori/bow.png")

image sayori 4b6abowemr = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/46a.png",  (0, 0), "sayori/bow.png")
image sayori 4b6bbowemr = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/46b.png",  (0, 0), "sayori/bow.png")
image sayori 4b6cbowemr = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/46c.png",  (0, 0), "sayori/bow.png")
image sayori 4b6dbowemr = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/46d.png",  (0, 0), "sayori/bow.png")
image sayori 4b6ebowemr = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/46e.png",  (0, 0), "sayori/bow.png")
image sayori 4b6fbowemr = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/46f.png",  (0, 0), "sayori/bow.png")
image sayori 4b6gbowemr = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/46g.png",  (0, 0), "sayori/bow.png")
image sayori 4b6hbowemr = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/46h.png",  (0, 0), "sayori/bow.png")
image sayori 4b6ibowemr = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/46i.png",  (0, 0), "sayori/bow.png")

image sayori 4b7abowemr = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/47a.png",  (0, 0), "sayori/bow.png")
image sayori 4b7bbowemr = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/47b.png",  (0, 0), "sayori/bow.png")
image sayori 4b7cbowemr = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/47c.png",  (0, 0), "sayori/bow.png")
image sayori 4b7dbowemr = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/47d.png",  (0, 0), "sayori/bow.png")
image sayori 4b7ebowemr = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/47e.png",  (0, 0), "sayori/bow.png")
image sayori 4b7fbowemr = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/47f.png",  (0, 0), "sayori/bow.png")
image sayori 4b7gbowemr = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/47g.png",  (0, 0), "sayori/bow.png")
image sayori 4b7hbowemr = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/47h.png",  (0, 0), "sayori/bow.png")
image sayori 4b7ibowemr = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/47i.png",  (0, 0), "sayori/bow.png")

image sayori 4b8abowemr = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/48a.png",  (0, 0), "sayori/bow.png")
image sayori 4b8bbowemr = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/48b.png",  (0, 0), "sayori/bow.png")
image sayori 4b8cbowemr = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/48c.png",  (0, 0), "sayori/bow.png")
image sayori 4b8dbowemr = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/48d.png",  (0, 0), "sayori/bow.png")
image sayori 4b8ebowemr = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/48e.png",  (0, 0), "sayori/bow.png")
image sayori 4b8fbowemr = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/48f.png",  (0, 0), "sayori/bow.png")
image sayori 4b8gbowemr = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/48g.png",  (0, 0), "sayori/bow.png")
image sayori 4b8hbowemr = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/48h.png",  (0, 0), "sayori/bow.png")
image sayori 4b8ibowemr = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/48i.png",  (0, 0), "sayori/bow.png")

image sayori 4p1aemr = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/41a.png")
image sayori 4p1bemr = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/41b.png")
image sayori 4p1cemr = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/41c.png")
image sayori 4p1demr = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/41d.png")
image sayori 4p1eemr = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/41e.png")
image sayori 4p1femr = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/41f.png")
image sayori 4p1gemr = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/41g.png")
image sayori 4p1hemr = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/41h.png")
image sayori 4p1iemr = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/41i.png")

image sayori 4p2aemr = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/42a.png")
image sayori 4p2bemr = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/42b.png")
image sayori 4p2cemr = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/42c.png")
image sayori 4p2demr = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/42d.png")
image sayori 4p2eemr = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/42e.png")
image sayori 4p2femr = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/42f.png")
image sayori 4p2gemr = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/42g.png")
image sayori 4p2hemr = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/42h.png")
image sayori 4p2iemr = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/42i.png")

image sayori 4p3aemr = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/43a.png")
image sayori 4p3bemr = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/43b.png")
image sayori 4p3cemr = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/43c.png")
image sayori 4p3demr = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/43d.png")
image sayori 4p3eemr = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/43e.png")
image sayori 4p3femr = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/43f.png")
image sayori 4p3gemr = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/43g.png")
image sayori 4p3hemr = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/43h.png")
image sayori 4p3iemr = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/43i.png")

image sayori 4p4aemr = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/44a.png")
image sayori 4p4bemr = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/44b.png")
image sayori 4p4cemr = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/44c.png")
image sayori 4p4demr = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/44d.png")
image sayori 4p4eemr = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/44e.png")
image sayori 4p4femr = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/44f.png")
image sayori 4p4gemr = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/44g.png")
image sayori 4p4hemr = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/44h.png")
image sayori 4p4iemr = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/44i.png")

image sayori 4p5aemr = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/45a.png")
image sayori 4p5bemr = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/45b.png")
image sayori 4p5cemr = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/45c.png")
image sayori 4p5demr = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/45d.png")
image sayori 4p5eemr = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/45e.png")
image sayori 4p5femr = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/45f.png")
image sayori 4p5gemr = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/45g.png")
image sayori 4p5hemr = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/45h.png")
image sayori 4p5iemr = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/45i.png")

image sayori 4p6aemr = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/46a.png")
image sayori 4p6bemr = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/46b.png")
image sayori 4p6cemr = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/46c.png")
image sayori 4p6demr = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/46d.png")
image sayori 4p6eemr = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/46e.png")
image sayori 4p6femr = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/46f.png")
image sayori 4p6gemr = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/46g.png")
image sayori 4p6hemr = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/46h.png")
image sayori 4p6iemr = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/46i.png")

image sayori 4p7aemr = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/47a.png")
image sayori 4p7bemr = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/47b.png")
image sayori 4p7cemr = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/47c.png")
image sayori 4p7demr = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/47d.png")
image sayori 4p7eemr = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/47e.png")
image sayori 4p7femr = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/47f.png")
image sayori 4p7gemr = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/47g.png")
image sayori 4p7hemr = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/47h.png")
image sayori 4p7iemr = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/47i.png")

image sayori 4p8aemr = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/48a.png")
image sayori 4p8bemr = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/48b.png")
image sayori 4p8cemr = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/48c.png")
image sayori 4p8demr = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/48d.png")
image sayori 4p8eemr = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/48e.png")
image sayori 4p8femr = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/48f.png")
image sayori 4p8gemr = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/48g.png")
image sayori 4p8hemr = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/48h.png")
image sayori 4p8iemr = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/48i.png")

image sayori 4p1abowemr = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/41a.png",  (0, 0), "sayori/bow.png")
image sayori 4p1bbowemr = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/41b.png",  (0, 0), "sayori/bow.png")
image sayori 4p1cbowemr = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/41c.png",  (0, 0), "sayori/bow.png")
image sayori 4p1dbowemr = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/41d.png",  (0, 0), "sayori/bow.png")
image sayori 4p1ebowemr = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/41e.png",  (0, 0), "sayori/bow.png")
image sayori 4p1fbowemr = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/41f.png",  (0, 0), "sayori/bow.png")
image sayori 4p1gbowemr = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/41g.png",  (0, 0), "sayori/bow.png")
image sayori 4p1hbowemr = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/41h.png",  (0, 0), "sayori/bow.png")
image sayori 4p1ibowemr = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/41i.png",  (0, 0), "sayori/bow.png")

image sayori 4p2abowemr = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/42a.png",  (0, 0), "sayori/bow.png")
image sayori 4p2bbowemr = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/42b.png",  (0, 0), "sayori/bow.png")
image sayori 4p2cbowemr = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/42c.png",  (0, 0), "sayori/bow.png")
image sayori 4p2dbowemr = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/42d.png",  (0, 0), "sayori/bow.png")
image sayori 4p2ebowemr = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/42e.png",  (0, 0), "sayori/bow.png")
image sayori 4p2fbowemr = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/42f.png",  (0, 0), "sayori/bow.png")
image sayori 4p2gbowemr = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/42g.png",  (0, 0), "sayori/bow.png")
image sayori 4p2hbowemr = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/42h.png",  (0, 0), "sayori/bow.png")
image sayori 4p2ibowemr = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/42i.png",  (0, 0), "sayori/bow.png")

image sayori 4p3abowemr = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/43a.png",  (0, 0), "sayori/bow.png")
image sayori 4p3bbowemr = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/43b.png",  (0, 0), "sayori/bow.png")
image sayori 4p3cbowemr = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/43c.png",  (0, 0), "sayori/bow.png")
image sayori 4p3dbowemr = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/43d.png",  (0, 0), "sayori/bow.png")
image sayori 4p3ebowemr = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/43e.png",  (0, 0), "sayori/bow.png")
image sayori 4p3fbowemr = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/43f.png",  (0, 0), "sayori/bow.png")
image sayori 4p3gbowemr = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/43g.png",  (0, 0), "sayori/bow.png")
image sayori 4p3hbowemr = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/43h.png",  (0, 0), "sayori/bow.png")
image sayori 4p3ibowemr = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/43i.png",  (0, 0), "sayori/bow.png")

image sayori 4p4abowemr = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/44a.png",  (0, 0), "sayori/bow.png")
image sayori 4p4bbowemr = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/44b.png",  (0, 0), "sayori/bow.png")
image sayori 4p4cbowemr = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/44c.png",  (0, 0), "sayori/bow.png")
image sayori 4p4dbowemr = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/44d.png",  (0, 0), "sayori/bow.png")
image sayori 4p4ebowemr = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/44e.png",  (0, 0), "sayori/bow.png")
image sayori 4p4fbowemr = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/44f.png",  (0, 0), "sayori/bow.png")
image sayori 4p4gbowemr = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/44g.png",  (0, 0), "sayori/bow.png")
image sayori 4p4hbowemr = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/44h.png",  (0, 0), "sayori/bow.png")
image sayori 4p4ibowemr = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/44i.png",  (0, 0), "sayori/bow.png")

image sayori 4p5abowemr = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/45a.png",  (0, 0), "sayori/bow.png")
image sayori 4p5bbowemr = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/45b.png",  (0, 0), "sayori/bow.png")
image sayori 4p5cbowemr = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/45c.png",  (0, 0), "sayori/bow.png")
image sayori 4p5dbowemr = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/45d.png",  (0, 0), "sayori/bow.png")
image sayori 4p5ebowemr = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/45e.png",  (0, 0), "sayori/bow.png")
image sayori 4p5fbowemr = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/45f.png",  (0, 0), "sayori/bow.png")
image sayori 4p5gbowemr = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/45g.png",  (0, 0), "sayori/bow.png")
image sayori 4p5hbowemr = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/45h.png",  (0, 0), "sayori/bow.png")
image sayori 4p5ibowemr = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/45i.png",  (0, 0), "sayori/bow.png")

image sayori 4p6abowemr = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/46a.png",  (0, 0), "sayori/bow.png")
image sayori 4p6bbowemr = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/46b.png",  (0, 0), "sayori/bow.png")
image sayori 4p6cbowemr = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/46c.png",  (0, 0), "sayori/bow.png")
image sayori 4p6dbowemr = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/46d.png",  (0, 0), "sayori/bow.png")
image sayori 4p6ebowemr = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/46e.png",  (0, 0), "sayori/bow.png")
image sayori 4p6fbowemr = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/46f.png",  (0, 0), "sayori/bow.png")
image sayori 4p6gbowemr = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/46g.png",  (0, 0), "sayori/bow.png")
image sayori 4p6hbowemr = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/46h.png",  (0, 0), "sayori/bow.png")
image sayori 4p6ibowemr = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/46i.png",  (0, 0), "sayori/bow.png")

image sayori 4p7abowemr = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/47a.png",  (0, 0), "sayori/bow.png")
image sayori 4p7bbowemr = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/47b.png",  (0, 0), "sayori/bow.png")
image sayori 4p7cbowemr = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/47c.png",  (0, 0), "sayori/bow.png")
image sayori 4p7dbowemr = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/47d.png",  (0, 0), "sayori/bow.png")
image sayori 4p7ebowemr = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/47e.png",  (0, 0), "sayori/bow.png")
image sayori 4p7fbowemr = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/47f.png",  (0, 0), "sayori/bow.png")
image sayori 4p7gbowemr = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/47g.png",  (0, 0), "sayori/bow.png")
image sayori 4p7hbowemr = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/47h.png",  (0, 0), "sayori/bow.png")
image sayori 4p7ibowemr = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/47i.png",  (0, 0), "sayori/bow.png")

image sayori 4p8abowemr = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/48a.png",  (0, 0), "sayori/bow.png")
image sayori 4p8bbowemr = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/48b.png",  (0, 0), "sayori/bow.png")
image sayori 4p8cbowemr = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/48c.png",  (0, 0), "sayori/bow.png")
image sayori 4p8dbowemr = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/48d.png",  (0, 0), "sayori/bow.png")
image sayori 4p8ebowemr = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/48e.png",  (0, 0), "sayori/bow.png")
image sayori 4p8fbowemr = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/48f.png",  (0, 0), "sayori/bow.png")
image sayori 4p8gbowemr = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/48g.png",  (0, 0), "sayori/bow.png")
image sayori 4p8hbowemr = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/48h.png",  (0, 0), "sayori/bow.png")
image sayori 4p8ibowemr = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/48i.png",  (0, 0), "sayori/bow.png")

image sayori 4Screamemr = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/4Scream.png")
image sayori 4Screambowemr = im.Composite((960, 960), (0, 0), "sayori/4.png", (0, 0), "sayori/4Scream.png",  (0, 0), "sayori/bow.png")
image sayori 4bScreamemr = im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/4Scream.png")
image sayori 4bScreambow emr= im.Composite((960, 960), (0, 0), "sayori/4b.png", (0, 0), "sayori/4Scream.png",  (0, 0), "sayori/bow.png")
image sayori 4pScreamemr = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/4Scream.png")
image sayori 4pScreambowemr = im.Composite((960, 960), (0, 0), "sayori/4p.png", (0, 0), "sayori/4Scream.png",  (0, 0), "sayori/bow.png")

# This image shows a glitched Sayori sprite during Act 2.
image sayori glitch:
    "sayori/glitch1.png"
    pause 0.01666
    "sayori/glitch2.png"
    pause 0.01666
    repeat

# Natsuki's Character Definitions
image natsuki 11 = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/1t.png")
image natsuki 1a = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/a.png")
image natsuki 1b = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/b.png")
image natsuki 1c = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/c.png")
image natsuki 1d = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/d.png")
image natsuki 1e = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/e.png")
image natsuki 1f = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/f.png")
image natsuki 1g = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/g.png")
image natsuki 1h = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/h.png")
image natsuki 1i = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/i.png")
image natsuki 1j = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/j.png")
image natsuki 1k = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/k.png")
image natsuki 1l = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/l.png")
image natsuki 1m = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/m.png")
image natsuki 1n = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/n.png")
image natsuki 1o = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/o.png")
image natsuki 1p = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/p.png")
image natsuki 1q = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/q.png")
image natsuki 1r = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/r.png")
image natsuki 1s = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/s.png")
image natsuki 1t = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/t.png")
image natsuki 1u = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/u.png")
image natsuki 1v = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/v.png")
image natsuki 1w = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/w.png")
image natsuki 1x = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/x.png")
image natsuki 1y = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/y.png")
image natsuki 1z = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/z.png")

image natsuki 21 = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/1t.png")
image natsuki 2a = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/a.png")
image natsuki 2b = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/b.png")
image natsuki 2c = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/c.png")
image natsuki 2d = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/d.png")
image natsuki 2e = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/e.png")
image natsuki 2f = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/f.png")
image natsuki 2g = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/g.png")
image natsuki 2h = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/h.png")
image natsuki 2i = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/i.png")
image natsuki 2j = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/j.png")
image natsuki 2k = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/k.png")
image natsuki 2l = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/l.png")
image natsuki 2m = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/m.png")
image natsuki 2n = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/n.png")
image natsuki 2o = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/o.png")
image natsuki 2p = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/p.png")
image natsuki 2q = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/q.png")
image natsuki 2r = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/r.png")
image natsuki 2s = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/s.png")
image natsuki 2t = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/t.png")
image natsuki 2u = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/u.png")
image natsuki 2v = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/v.png")
image natsuki 2w = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/w.png")
image natsuki 2x = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/x.png")
image natsuki 2y = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/y.png")
image natsuki 2z = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/z.png")

image natsuki 31 = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/1t.png")
image natsuki 3a = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/a.png")
image natsuki 3b = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/b.png")
image natsuki 3c = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/c.png")
image natsuki 3d = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/d.png")
image natsuki 3e = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/e.png")
image natsuki 3f = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/f.png")
image natsuki 3g = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/g.png")
image natsuki 3h = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/h.png")
image natsuki 3i = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/i.png")
image natsuki 3j = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/j.png")
image natsuki 3k = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/k.png")
image natsuki 3l = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/l.png")
image natsuki 3m = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/m.png")
image natsuki 3n = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/n.png")
image natsuki 3o = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/o.png")
image natsuki 3p = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/p.png")
image natsuki 3q = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/q.png")
image natsuki 3r = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/r.png")
image natsuki 3s = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/s.png")
image natsuki 3t = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/t.png")
image natsuki 3u = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/u.png")
image natsuki 3v = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/v.png")
image natsuki 3w = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/w.png")
image natsuki 3x = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/x.png")
image natsuki 3y = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/y.png")
image natsuki 3z = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/z.png")

image natsuki 41 = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/1t.png")
image natsuki 4a = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/a.png")
image natsuki 4b = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/b.png")
image natsuki 4c = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/c.png")
image natsuki 4d = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/d.png")
image natsuki 4e = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/e.png")
image natsuki 4f = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/f.png")
image natsuki 4g = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/g.png")
image natsuki 4h = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/h.png")
image natsuki 4i = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/i.png")
image natsuki 4j = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/j.png")
image natsuki 4k = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/k.png")
image natsuki 4l = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/l.png")
image natsuki 4m = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/m.png")
image natsuki 4n = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/n.png")
image natsuki 4o = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/o.png")
image natsuki 4p = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/p.png")
image natsuki 4q = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/q.png")
image natsuki 4r = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/r.png")
image natsuki 4s = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/s.png")
image natsuki 4t = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/t.png")
image natsuki 4u = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/u.png")
image natsuki 4v = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/v.png")
image natsuki 4w = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/w.png")
image natsuki 4x = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/x.png")
image natsuki 4y = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/y.png")
image natsuki 4z = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/z.png")

image natsuki 12 = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/2t.png")
image natsuki 12a = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/2ta.png")
image natsuki 12b = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/2tb.png")
image natsuki 12c = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/2tc.png")
image natsuki 12d = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/2td.png")
image natsuki 12e = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/2te.png")
image natsuki 12f = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/2tf.png")
image natsuki 12g = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/2tg.png")
image natsuki 12h = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/2th.png")
image natsuki 12i = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/2ti.png")

image natsuki 42 = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/2t.png")
image natsuki 42a = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/2ta.png")
image natsuki 42b = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/2tb.png")
image natsuki 42c = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/2tc.png")
image natsuki 42d = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/2td.png")
image natsuki 42e = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/2te.png")
image natsuki 42f = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/2tf.png")
image natsuki 42g = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/2tg.png")
image natsuki 42h = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/2th.png")
image natsuki 42i = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/2ti.png")

image natsuki 51 = im.Composite((960, 960), (18, 22), "natsuki/1t.png", (0, 0), "natsuki/3.png")
image natsuki 5a = im.Composite((960, 960), (18, 22), "natsuki/a.png", (0, 0), "natsuki/3.png")
image natsuki 5b = im.Composite((960, 960), (18, 22), "natsuki/b.png", (0, 0), "natsuki/3.png")
image natsuki 5c = im.Composite((960, 960), (18, 22), "natsuki/c.png", (0, 0), "natsuki/3.png")
image natsuki 5d = im.Composite((960, 960), (18, 22), "natsuki/d.png", (0, 0), "natsuki/3.png")
image natsuki 5e = im.Composite((960, 960), (18, 22), "natsuki/e.png", (0, 0), "natsuki/3.png")
image natsuki 5f = im.Composite((960, 960), (18, 22), "natsuki/f.png", (0, 0), "natsuki/3.png")
image natsuki 5g = im.Composite((960, 960), (18, 22), "natsuki/g.png", (0, 0), "natsuki/3.png")
image natsuki 5h = im.Composite((960, 960), (18, 22), "natsuki/h.png", (0, 0), "natsuki/3.png")
image natsuki 5i = im.Composite((960, 960), (18, 22), "natsuki/i.png", (0, 0), "natsuki/3.png")
image natsuki 5j = im.Composite((960, 960), (18, 22), "natsuki/j.png", (0, 0), "natsuki/3.png")
image natsuki 5k = im.Composite((960, 960), (18, 22), "natsuki/k.png", (0, 0), "natsuki/3.png")
image natsuki 5l = im.Composite((960, 960), (18, 22), "natsuki/l.png", (0, 0), "natsuki/3.png")
image natsuki 5m = im.Composite((960, 960), (18, 22), "natsuki/m.png", (0, 0), "natsuki/3.png")
image natsuki 5n = im.Composite((960, 960), (18, 22), "natsuki/n.png", (0, 0), "natsuki/3.png")
image natsuki 5o = im.Composite((960, 960), (18, 22), "natsuki/o.png", (0, 0), "natsuki/3.png")
image natsuki 5p = im.Composite((960, 960), (18, 22), "natsuki/p.png", (0, 0), "natsuki/3.png")
image natsuki 5q = im.Composite((960, 960), (18, 22), "natsuki/q.png", (0, 0), "natsuki/3.png")
image natsuki 5r = im.Composite((960, 960), (18, 22), "natsuki/r.png", (0, 0), "natsuki/3.png")
image natsuki 5s = im.Composite((960, 960), (18, 22), "natsuki/s.png", (0, 0), "natsuki/3.png")
image natsuki 5t = im.Composite((960, 960), (18, 22), "natsuki/t.png", (0, 0), "natsuki/3.png")
image natsuki 5u = im.Composite((960, 960), (18, 22), "natsuki/u.png", (0, 0), "natsuki/3.png")
image natsuki 5v = im.Composite((960, 960), (18, 22), "natsuki/v.png", (0, 0), "natsuki/3.png")
image natsuki 5w = im.Composite((960, 960), (18, 22), "natsuki/w.png", (0, 0), "natsuki/3.png")
image natsuki 5x = im.Composite((960, 960), (18, 22), "natsuki/x.png", (0, 0), "natsuki/3.png")
image natsuki 5y = im.Composite((960, 960), (18, 22), "natsuki/y.png", (0, 0), "natsuki/3.png")
image natsuki 5z = im.Composite((960, 960), (18, 22), "natsuki/z.png", (0, 0), "natsuki/3.png")

# Natsuki in her casual outfit [Day 4 - Natsuki Route]
image natsuki 1ba = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/a.png")
image natsuki 1bb = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/b.png")
image natsuki 1bc = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/c.png")
image natsuki 1bd = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/d.png")
image natsuki 1be = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/e.png")
image natsuki 1bf = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/f.png")
image natsuki 1bg = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/g.png")
image natsuki 1bh = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/h.png")
image natsuki 1bi = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/i.png")
image natsuki 1bj = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/j.png")
image natsuki 1bk = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/k.png")
image natsuki 1bl = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/l.png")
image natsuki 1bm = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/m.png")
image natsuki 1bn = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/n.png")
image natsuki 1bo = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/o.png")
image natsuki 1bp = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/p.png")
image natsuki 1bq = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/q.png")
image natsuki 1br = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/r.png")
image natsuki 1bs = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/s.png")
image natsuki 1bt = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/t.png")
image natsuki 1bu = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/u.png")
image natsuki 1bv = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/v.png")
image natsuki 1bw = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/w.png")
image natsuki 1bx = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/x.png")
image natsuki 1by = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/y.png")
image natsuki 1bz = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/z.png")

image natsuki 2ba = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/a.png")
image natsuki 2bb = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/b.png")
image natsuki 2bc = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/c.png")
image natsuki 2bd = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/d.png")
image natsuki 2be = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/e.png")
image natsuki 2bf = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/f.png")
image natsuki 2bg = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/g.png")
image natsuki 2bh = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/h.png")
image natsuki 2bi = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/i.png")
image natsuki 2bj = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/j.png")
image natsuki 2bk = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/k.png")
image natsuki 2bl = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/l.png")
image natsuki 2bm = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/m.png")
image natsuki 2bn = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/n.png")
image natsuki 2bo = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/o.png")
image natsuki 2bp = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/p.png")
image natsuki 2bq = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/q.png")
image natsuki 2br = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/r.png")
image natsuki 2bs = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/s.png")
image natsuki 2bt = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/t.png")
image natsuki 2bu = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/u.png")
image natsuki 2bv = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/v.png")
image natsuki 2bw = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/w.png")
image natsuki 2bx = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/x.png")
image natsuki 2by = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/y.png")
image natsuki 2bz = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/z.png")

image natsuki 3ba = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/a.png")
image natsuki 3bb = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/b.png")
image natsuki 3bc = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/c.png")
image natsuki 3bd = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/d.png")
image natsuki 3be = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/e.png")
image natsuki 3bf = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/f.png")
image natsuki 3bg = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/g.png")
image natsuki 3bh = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/h.png")
image natsuki 3bi = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/i.png")
image natsuki 3bj = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/j.png")
image natsuki 3bk = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/k.png")
image natsuki 3bl = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/l.png")
image natsuki 3bm = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/m.png")
image natsuki 3bn = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/n.png")
image natsuki 3bo = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/o.png")
image natsuki 3bp = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/p.png")
image natsuki 3bq = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/q.png")
image natsuki 3br = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/r.png")
image natsuki 3bs = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/s.png")
image natsuki 3bt = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/t.png")
image natsuki 3bu = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/u.png")
image natsuki 3bv = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/v.png")
image natsuki 3bw = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/w.png")
image natsuki 3bx = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/x.png")
image natsuki 3by = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/y.png")
image natsuki 3bz = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/z.png")

image natsuki 4ba = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/a.png")
image natsuki 4bb = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/b.png")
image natsuki 4bc = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/c.png")
image natsuki 4bd = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/d.png")
image natsuki 4be = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/e.png")
image natsuki 4bf = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/f.png")
image natsuki 4bg = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/g.png")
image natsuki 4bh = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/h.png")
image natsuki 4bi = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/i.png")
image natsuki 4bj = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/j.png")
image natsuki 4bk = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/k.png")
image natsuki 4bl = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/l.png")
image natsuki 4bm = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/m.png")
image natsuki 4bn = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/n.png")
image natsuki 4bo = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/o.png")
image natsuki 4bp = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/p.png")
image natsuki 4bq = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/q.png")
image natsuki 4br = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/r.png")
image natsuki 4bs = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/s.png")
image natsuki 4bt = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/t.png")
image natsuki 4bu = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/u.png")
image natsuki 4bv = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/v.png")
image natsuki 4bw = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/w.png")
image natsuki 4bx = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/x.png")
image natsuki 4by = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/y.png")
image natsuki 4bz = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/z.png")

image natsuki 12ba = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/2bta.png")
image natsuki 12bb = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/2btb.png")
image natsuki 12bc = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/2btc.png")
image natsuki 12bd = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/2btd.png")
image natsuki 12be = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/2bte.png")
image natsuki 12bf = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/2btf.png")
image natsuki 12bg = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/2btg.png")
image natsuki 12bh = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/2bth.png")
image natsuki 12bi = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/2bti.png")

image natsuki 42ba = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/2bta.png")
image natsuki 42bb = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/2btb.png")
image natsuki 42bc = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/2btc.png")
image natsuki 42bd = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/2btd.png")
image natsuki 42be = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/2bte.png")
image natsuki 42bf = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/2btf.png")
image natsuki 42bg = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/2btg.png")
image natsuki 42bh = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/2bth.png")
image natsuki 42bi = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/2bti.png")

image natsuki 5ba = im.Composite((960, 960), (18, 22), "natsuki/a.png", (0, 0), "natsuki/3b.png")
image natsuki 5bb = im.Composite((960, 960), (18, 22), "natsuki/b.png", (0, 0), "natsuki/3b.png")
image natsuki 5bc = im.Composite((960, 960), (18, 22), "natsuki/c.png", (0, 0), "natsuki/3b.png")
image natsuki 5bd = im.Composite((960, 960), (18, 22), "natsuki/d.png", (0, 0), "natsuki/3b.png")
image natsuki 5be = im.Composite((960, 960), (18, 22), "natsuki/e.png", (0, 0), "natsuki/3b.png")
image natsuki 5bf = im.Composite((960, 960), (18, 22), "natsuki/f.png", (0, 0), "natsuki/3b.png")
image natsuki 5bg = im.Composite((960, 960), (18, 22), "natsuki/g.png", (0, 0), "natsuki/3b.png")
image natsuki 5bh = im.Composite((960, 960), (18, 22), "natsuki/h.png", (0, 0), "natsuki/3b.png")
image natsuki 5bi = im.Composite((960, 960), (18, 22), "natsuki/i.png", (0, 0), "natsuki/3b.png")
image natsuki 5bj = im.Composite((960, 960), (18, 22), "natsuki/j.png", (0, 0), "natsuki/3b.png")
image natsuki 5bk = im.Composite((960, 960), (18, 22), "natsuki/k.png", (0, 0), "natsuki/3b.png")
image natsuki 5bl = im.Composite((960, 960), (18, 22), "natsuki/l.png", (0, 0), "natsuki/3b.png")
image natsuki 5bm = im.Composite((960, 960), (18, 22), "natsuki/m.png", (0, 0), "natsuki/3b.png")
image natsuki 5bn = im.Composite((960, 960), (18, 22), "natsuki/n.png", (0, 0), "natsuki/3b.png")
image natsuki 5bo = im.Composite((960, 960), (18, 22), "natsuki/o.png", (0, 0), "natsuki/3b.png")
image natsuki 5bp = im.Composite((960, 960), (18, 22), "natsuki/p.png", (0, 0), "natsuki/3b.png")
image natsuki 5bq = im.Composite((960, 960), (18, 22), "natsuki/q.png", (0, 0), "natsuki/3b.png")
image natsuki 5br = im.Composite((960, 960), (18, 22), "natsuki/r.png", (0, 0), "natsuki/3b.png")
image natsuki 5bs = im.Composite((960, 960), (18, 22), "natsuki/s.png", (0, 0), "natsuki/3b.png")
image natsuki 5bt = im.Composite((960, 960), (18, 22), "natsuki/t.png", (0, 0), "natsuki/3b.png")
image natsuki 5bu = im.Composite((960, 960), (18, 22), "natsuki/u.png", (0, 0), "natsuki/3b.png")
image natsuki 5bv = im.Composite((960, 960), (18, 22), "natsuki/v.png", (0, 0), "natsuki/3b.png")
image natsuki 5bw = im.Composite((960, 960), (18, 22), "natsuki/w.png", (0, 0), "natsuki/3b.png")
image natsuki 5bx = im.Composite((960, 960), (18, 22), "natsuki/x.png", (0, 0), "natsuki/3b.png")
image natsuki 5by = im.Composite((960, 960), (18, 22), "natsuki/y.png", (0, 0), "natsuki/3b.png")
image natsuki 5bz = im.Composite((960, 960), (18, 22), "natsuki/z.png", (0, 0), "natsuki/3b.png")

# These image definitions are left-overs of certain Natsuki expressions 
# found in the original 1.0 release of DDLC.
image natsuki 1 = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/1t.png")
image natsuki 2 = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/1t.png")
image natsuki 3 = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/1t.png")
image natsuki 4 = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/1t.png")
image natsuki 5 = im.Composite((960, 960), (18, 22), "natsuki/1t.png", (0, 0), "natsuki/3.png")

# This image shows the realistic mouth on Natsuki on a random playthrough
# of Act 2.
image natsuki mouth = im.Composite((960, 960), (0, 0), "natsuki/0.png", (390, 340), "n_rects_mouth", (480, 334), "n_rects_mouth")

# This image shows black rectangles on Natsuki on a random playthrough
# of Act 2.
image n_rects_mouth:
    RectCluster(Solid("#000"), 4, 15, 5).sm
    size (20, 25)

# This image transform makes the realistic mouth move on Natsuki's face
# on a random playthrough of Act 2.
image n_moving_mouth:
    "images/natsuki/mouth.png"
    pos (615, 305)
    xanchor 0.5 yanchor 0.5
    parallel:
        choice:
            ease 0.10 yzoom 0.2
        choice:
            ease 0.05 yzoom 0.2
        choice:
            ease 0.075 yzoom 0.2
        pass
        choice:
            0.02
        choice:
            0.04
        choice:
            0.06
        choice:
            0.08
        pass
        choice:
            ease 0.10 yzoom 1
        choice:
            ease 0.05 yzoom 1
        choice:
            ease 0.075 yzoom 1
        pass
        choice:
            0.02
        choice:
            0.04
        choice:
            0.06
        choice:
            0.08
        repeat
    parallel:
        choice:
            0.2
        choice:
            0.4
        choice:
            0.6
        ease 0.2 xzoom 0.4
        ease 0.2 xzoom 0.8
        repeat

# These images show the Natsuki ghost sprite shown in the poemgame of 
# Act 2.
image natsuki_ghost_blood:
    "#00000000"
    "natsuki/ghost_blood.png" with ImageDissolve("images/menu/wipedown.png", 80.0, ramplen=4, alpha=True)
    pos (620,320) zoom 0.80

image natsuki ghost_base:
    "natsuki/ghost1.png"
image natsuki ghost1:
    "natsuki 11"
    "natsuki ghost_base" with Dissolve(20.0, alpha=True)
image natsuki ghost2 = Image("natsuki/ghost2.png")
image natsuki ghost3 = Image("natsuki/ghost3.png")
image natsuki ghost4:
    "natsuki ghost3"
    parallel:
        easeout 0.25 zoom 4.5 yoffset 1200
    parallel:
        ease 0.025 xoffset -20
        ease 0.025 xoffset 20
        repeat
    0.25
    "black"

# This image makes Natsuki's sprite glitch up for a bit before
# returning to normal.
image natsuki glitch1:
    "natsuki/glitch1.png"
    zoom 1.25
    block:
        yoffset 300 xoffset 100 ytile 2
        linear 0.15 yoffset 200
        repeat
    time 0.75
    yoffset 0 zoom 1 xoffset 0 ytile 1
    "natsuki 4e"

image natsuki scream = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/scream.png")
image natsuki vomit = "natsuki/vomit.png"

# These images declare alterative eyes for Natsuki on a random playthrough of
# Act 2.
image n_blackeyes = "images/natsuki/blackeyes.png"
image n_eye = "images/natsuki/eye.png"

# Yuri's Character Definitions
# Note: Sprites with a 'y' in the middle are Yuri's Yandere Sprites.
image yuri 1 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/a.png")
image yuri 2 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/a.png")
image yuri 3 = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/a.png")
image yuri 4 = im.Composite((960, 960), (0, 0), "yuri/3.png", (0, 0), "yuri/a2.png")

image yuri 1a = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/a.png")
image yuri 1b = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/b.png")
image yuri 1c = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/c.png")
image yuri 1d = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/d.png")
image yuri 1e = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/e.png")
image yuri 1f = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/f.png")
image yuri 1g = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/g.png")
image yuri 1h = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/h.png")
image yuri 1i = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/i.png")
image yuri 1j = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/j.png")
image yuri 1k = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/k.png")
image yuri 1l = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/l.png")
image yuri 1m = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/m.png")
image yuri 1n = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/n.png")
image yuri 1o = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/o.png")
image yuri 1p = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/p.png")
image yuri 1q = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/q.png")
image yuri 1r = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/r.png")
image yuri 1s = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/s.png")
image yuri 1t = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/t.png")
image yuri 1u = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/u.png")
image yuri 1v = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/v.png")
image yuri 1w = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/w.png")

image yuri 1y1 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/y1.png")
image yuri 1y2 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/y2.png")
image yuri 1y3 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/y3.png")
image yuri 1y4 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/y4.png")
image yuri 1y5 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/y5.png")
image yuri 1y6 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/y6.png")
image yuri 1y7 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/y7.png")

image yuri 2a = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/a.png")
image yuri 2b = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/b.png")
image yuri 2c = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/c.png")
image yuri 2d = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/d.png")
image yuri 2e = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/e.png")
image yuri 2f = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/f.png")
image yuri 2g = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/g.png")
image yuri 2h = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/h.png")
image yuri 2i = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/i.png")
image yuri 2j = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/j.png")
image yuri 2k = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/k.png")
image yuri 2l = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/l.png")
image yuri 2m = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/m.png")
image yuri 2n = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/n.png")
image yuri 2o = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/o.png")
image yuri 2p = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/p.png")
image yuri 2q = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/q.png")
image yuri 2r = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/r.png")
image yuri 2s = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/s.png")
image yuri 2t = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/t.png")
image yuri 2u = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/u.png")
image yuri 2v = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/v.png")
image yuri 2w = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/w.png")

image yuri 2y1 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y1.png")
image yuri 2y2 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y2.png")
image yuri 2y3 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y3.png")
image yuri 2y4 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y4.png")
image yuri 2y5 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y5.png")
image yuri 2y6 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y6.png")
image yuri 2y7 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y7.png")

image yuri 3a = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/a.png")
image yuri 3b = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/b.png")
image yuri 3c = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/c.png")
image yuri 3d = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/d.png")
image yuri 3e = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/e.png")
image yuri 3f = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/f.png")
image yuri 3g = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/g.png")
image yuri 3h = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/h.png")
image yuri 3i = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/i.png")
image yuri 3j = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/j.png")
image yuri 3k = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/k.png")
image yuri 3l = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/l.png")
image yuri 3m = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/m.png")
image yuri 3n = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/n.png")
image yuri 3o = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/o.png")
image yuri 3p = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/p.png")
image yuri 3q = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/q.png")
image yuri 3r = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/r.png")
image yuri 3s = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/s.png")
image yuri 3t = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/t.png")
image yuri 3u = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/u.png")
image yuri 3v = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/v.png")
image yuri 3w = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/w.png")

image yuri 3y1 = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y1.png")
image yuri 3y2 = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y2.png")
image yuri 3y3 = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y3.png")
image yuri 3y4 = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y4.png")
image yuri 3y5 = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y5.png")
image yuri 3y6 = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y6.png")
image yuri 3y7 = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y7.png")

image yuri 4a = im.Composite((960, 960), (0, 0), "yuri/3.png", (0, 0), "yuri/a2.png")
image yuri 4b = im.Composite((960, 960), (0, 0), "yuri/3.png", (0, 0), "yuri/b2.png")
image yuri 4c = im.Composite((960, 960), (0, 0), "yuri/3.png", (0, 0), "yuri/c2.png")
image yuri 4d = im.Composite((960, 960), (0, 0), "yuri/3.png", (0, 0), "yuri/d2.png")
image yuri 4e = im.Composite((960, 960), (0, 0), "yuri/3.png", (0, 0), "yuri/e2.png")

# Yuri in her casual outfit [Day 4 - Yuri Route]
image yuri 1ba = im.Composite((960, 960), (0, 0), "yuri/a.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bb = im.Composite((960, 960), (0, 0), "yuri/b.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bc = im.Composite((960, 960), (0, 0), "yuri/c.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bd = im.Composite((960, 960), (0, 0), "yuri/d.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1be = im.Composite((960, 960), (0, 0), "yuri/e.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bf = im.Composite((960, 960), (0, 0), "yuri/f.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bg = im.Composite((960, 960), (0, 0), "yuri/g.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bh = im.Composite((960, 960), (0, 0), "yuri/h.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bi = im.Composite((960, 960), (0, 0), "yuri/i.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bj = im.Composite((960, 960), (0, 0), "yuri/j.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bk = im.Composite((960, 960), (0, 0), "yuri/k.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bl = im.Composite((960, 960), (0, 0), "yuri/l.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bm = im.Composite((960, 960), (0, 0), "yuri/m.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bn = im.Composite((960, 960), (0, 0), "yuri/n.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bo = im.Composite((960, 960), (0, 0), "yuri/o.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bp = im.Composite((960, 960), (0, 0), "yuri/p.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bq = im.Composite((960, 960), (0, 0), "yuri/q.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1br = im.Composite((960, 960), (0, 0), "yuri/r.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bs = im.Composite((960, 960), (0, 0), "yuri/s.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bt = im.Composite((960, 960), (0, 0), "yuri/t.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bu = im.Composite((960, 960), (0, 0), "yuri/u.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bv = im.Composite((960, 960), (0, 0), "yuri/v.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bw = im.Composite((960, 960), (0, 0), "yuri/w.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")

image yuri 2ba = im.Composite((960, 960), (0, 0), "yuri/a.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bb = im.Composite((960, 960), (0, 0), "yuri/b.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bc = im.Composite((960, 960), (0, 0), "yuri/c.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bd = im.Composite((960, 960), (0, 0), "yuri/d.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2be = im.Composite((960, 960), (0, 0), "yuri/e.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bf = im.Composite((960, 960), (0, 0), "yuri/f.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bg = im.Composite((960, 960), (0, 0), "yuri/g.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bh = im.Composite((960, 960), (0, 0), "yuri/h.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bi = im.Composite((960, 960), (0, 0), "yuri/i.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bj = im.Composite((960, 960), (0, 0), "yuri/j.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bk = im.Composite((960, 960), (0, 0), "yuri/k.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bl = im.Composite((960, 960), (0, 0), "yuri/l.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bm = im.Composite((960, 960), (0, 0), "yuri/m.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bn = im.Composite((960, 960), (0, 0), "yuri/n.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bo = im.Composite((960, 960), (0, 0), "yuri/o.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bp = im.Composite((960, 960), (0, 0), "yuri/p.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bq = im.Composite((960, 960), (0, 0), "yuri/q.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2br = im.Composite((960, 960), (0, 0), "yuri/r.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bs = im.Composite((960, 960), (0, 0), "yuri/s.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bt = im.Composite((960, 960), (0, 0), "yuri/t.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bu = im.Composite((960, 960), (0, 0), "yuri/u.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bv = im.Composite((960, 960), (0, 0), "yuri/v.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bw = im.Composite((960, 960), (0, 0), "yuri/w.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")

image yuri 3ba = im.Composite((960, 960), (0, 0), "yuri/a.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bb = im.Composite((960, 960), (0, 0), "yuri/b.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bc = im.Composite((960, 960), (0, 0), "yuri/c.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bd = im.Composite((960, 960), (0, 0), "yuri/d.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3be = im.Composite((960, 960), (0, 0), "yuri/e.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bf = im.Composite((960, 960), (0, 0), "yuri/f.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bg = im.Composite((960, 960), (0, 0), "yuri/g.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bh = im.Composite((960, 960), (0, 0), "yuri/h.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bi = im.Composite((960, 960), (0, 0), "yuri/i.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bj = im.Composite((960, 960), (0, 0), "yuri/j.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bk = im.Composite((960, 960), (0, 0), "yuri/k.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bl = im.Composite((960, 960), (0, 0), "yuri/l.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bm = im.Composite((960, 960), (0, 0), "yuri/m.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bn = im.Composite((960, 960), (0, 0), "yuri/n.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bo = im.Composite((960, 960), (0, 0), "yuri/o.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bp = im.Composite((960, 960), (0, 0), "yuri/p.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bq = im.Composite((960, 960), (0, 0), "yuri/q.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3br = im.Composite((960, 960), (0, 0), "yuri/r.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bs = im.Composite((960, 960), (0, 0), "yuri/s.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bt = im.Composite((960, 960), (0, 0), "yuri/t.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bu = im.Composite((960, 960), (0, 0), "yuri/u.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bv = im.Composite((960, 960), (0, 0), "yuri/v.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bw = im.Composite((960, 960), (0, 0), "yuri/w.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")

image yuri 4ba = im.Composite((960, 960), (0, 0), "yuri/a2.png", (0, 0), "yuri/3b.png")
image yuri 4bb = im.Composite((960, 960), (0, 0), "yuri/b2.png", (0, 0), "yuri/3b.png")
image yuri 4bc = im.Composite((960, 960), (0, 0), "yuri/c2.png", (0, 0), "yuri/3b.png")
image yuri 4bd = im.Composite((960, 960), (0, 0), "yuri/d2.png", (0, 0), "yuri/3b.png")
image yuri 4be = im.Composite((960, 960), (0, 0), "yuri/e2.png", (0, 0), "yuri/3b.png")

# This image shows the looping Yuri glitched head in Act 2.
image y_glitch_head:
    "images/yuri/za.png"
    0.15
    "images/yuri/zb.png"
    0.15
    "images/yuri/zc.png"
    0.15
    "images/yuri/zd.png"
    0.15
    repeat

# These images shows Yuri stabbing herself at the end of Act 2 in six stages.
image yuri stab_1 = "yuri/stab/1.png"
image yuri stab_2 = "yuri/stab/2.png"
image yuri stab_3 = "yuri/stab/3.png"
image yuri stab_4 = "yuri/stab/4.png"
image yuri stab_5 = "yuri/stab/5.png"
image yuri stab_6 = im.Composite((960,960), (0, 0), "yuri/stab/6-mask.png", (0, 0), "yuri stab_6_eyes", (0, 0), "yuri/stab/6.png")

# This image transform animates Yuri's eyes on her 6th stabbing in Act 2.
image yuri stab_6_eyes:
    "yuri/stab/6-eyes.png"
    subpixel True
    parallel:
        choice:
            xoffset 0.5
        choice:
            xoffset 0
        choice:
            xoffset -0.5
        0.2
        repeat
    parallel:
        choice:
            yoffset 0.5
        choice:
            yoffset 0
        choice:
            yoffset -0.5
        0.2
        repeat
    parallel:
        2.05
        easeout 1.0 yoffset -15
        linear 10 yoffset -15

# These images shows Yuri with a offcenter right eye moving slowing away
# from her face.
image yuri oneeye = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/oneeye.png", (0, 0), "yuri oneeye2")
image yuri oneeye2:
    "yuri/oneeye2.png"
    subpixel True
    pause 5.0
    linear 60 xoffset -50 yoffset 20

# These images show a glitched Yuri during Act 2.
image yuri glitch:
    "yuri/glitch1.png"
    pause 0.1
    "yuri/glitch2.png"
    pause 0.1
    "yuri/glitch3.png"
    pause 0.1
    "yuri/glitch4.png"
    pause 0.1
    "yuri/glitch5.png"
    pause 0.1
    repeat
image yuri glitch2:
    "yuri/0a.png"
    pause 0.1
    "yuri/0b.png"
    pause 0.5
    "yuri/0a.png"
    pause 0.3
    "yuri/0b.png"
    pause 0.3
    "yuri 1"

# These image declarations show Yuri's moving eyes in Act 2.
image yuri eyes = im.Composite((1280, 720), (0, 0), "yuri/eyes1.png", (0, 0), "yuripupils")

# This image shows the base of Yuri's sprite as her eyes move.
image yuri eyes_base = "yuri/eyes1.png"

# This image shows Yuri's realistic moving eyes during Act 2.
image yuripupils:
    "yuri/eyes2.png"
    yuripupils_move

image yuri cuts = "yuri/cuts.png"

# This image shows another glitched Yuri from Act 2. 
image yuri dragon:
    "yuri 3"
    0.25
    parallel:
        "yuri/dragon1.png"
        0.01
        "yuri/dragon2.png"
        0.01
        repeat
    parallel:
        0.01
        choice:
            xoffset -1
            xoffset -2
            xoffset -5
            xoffset -6
            xoffset -9
            xoffset -10
        0.01
        xoffset 0
        repeat
    time 0.55
    xoffset 0
    "yuri 3"

#YURI CG SPRITE

image cg_yuri 1 = im.Composite((1500, 1075), (0, 0), "mod_assets/cg_yuri/b/1.png", (0, 0), "mod_assets/cg_yuri/a.png")
image cg_yuri 2 = im.Composite((1500, 1125), (0, 0), "mod_assets/cg_yuri/b/2.png", (0, 0),  "mod_assets/cg_yuri/a.png")
image cg_yuri 3 = im.Composite((1500, 1125), (0, 0), "mod_assets/cg_yuri/b/3.png", (0, 0), "mod_assets/cg_yuri/a.png")

image cg_yuri 1a = im.Composite((1500, 1125), (0, 0), "mod_assets/cg_yuri/b/1.png", (0, 0), "mod_assets/cg_yuri/a.png")
image cg_yuri 1b = im.Composite((1500, 1125), (0, 0), "mod_assets/cg_yuri/b/1.png", (0, 0), "mod_assets/cg_yuri/b.png")
image cg_yuri 1c = im.Composite((1500, 1125), (0, 0), "mod_assets/cg_yuri/b/1.png", (0, 0), "mod_assets/cg_yuri/c.png")
image cg_yuri 1d = im.Composite((1500, 1125), (0, 0), "mod_assets/cg_yuri/b/1.png", (0, 0), "mod_assets/cg_yuri/d.png")
image cg_yuri 1e = im.Composite((1500, 1125), (0, 0), "mod_assets/cg_yuri/b/1.png", (0, 0), "mod_assets/cg_yuri/e.png")
image cg_yuri 1f = im.Composite((1500, 1125), (0, 0), "mod_assets/cg_yuri/b/1.png", (0, 0), "mod_assets/cg_yuri/f.png")
image cg_yuri 1g = im.Composite((1500, 1125), (0, 0), "mod_assets/cg_yuri/b/1.png", (0, 0), "mod_assets/cg_yuri/g.png")
image cg_yuri 1h = im.Composite((1500, 1125), (0, 0), "mod_assets/cg_yuri/b/1.png", (0, 0), "mod_assets/cg_yuri/h.png")
image cg_yuri 1i = im.Composite((1500, 1125), (0, 0), "mod_assets/cg_yuri/b/1.png", (0, 0), "mod_assets/cg_yuri/i.png")
image cg_yuri 1j = im.Composite((1500, 1125), (0, 0), "mod_assets/cg_yuri/b/1.png", (0, 0), "mod_assets/cg_yuri/j.png")
image cg_yuri 1k = im.Composite((1500, 1125), (0, 0), "mod_assets/cg_yuri/b/1.png", (0, 0), "mod_assets/cg_yuri/k.png")
image cg_yuri 1l = im.Composite((1500, 1125), (0, 0), "mod_assets/cg_yuri/b/1.png", (0, 0), "mod_assets/cg_yuri/l.png")
image cg_yuri 1m = im.Composite((1500, 1125), (0, 0), "mod_assets/cg_yuri/b/1.png", (0, 0), "mod_assets/cg_yuri/m.png")
image cg_yuri 1n = im.Composite((1500, 1125), (0, 0), "mod_assets/cg_yuri/b/1.png", (0, 0), "mod_assets/cg_yuri/n.png")

image cg_yuri 2a = im.Composite((1500, 1125), (0, 0), "mod_assets/cg_yuri/b/2.png", (0, 0), "mod_assets/cg_yuri/a.png")
image cg_yuri 2b = im.Composite((1500, 1125), (0, 0), "mod_assets/cg_yuri/b/2.png", (0, 0), "mod_assets/cg_yuri/b.png")
image cg_yuri 2c = im.Composite((1500, 1125), (0, 0), "mod_assets/cg_yuri/b/2.png", (0, 0), "mod_assets/cg_yuri/c.png")
image cg_yuri 2d = im.Composite((1500, 1125), (0, 0), "mod_assets/cg_yuri/b/2.png", (0, 0), "mod_assets/cg_yuri/d.png")
image cg_yuri 2e = im.Composite((1500, 1125), (0, 0), "mod_assets/cg_yuri/b/2.png", (0, 0), "mod_assets/cg_yuri/e.png")
image cg_yuri 2f = im.Composite((1500, 1125), (0, 0), "mod_assets/cg_yuri/b/2.png", (0, 0), "mod_assets/cg_yuri/f.png")
image cg_yuri 2g = im.Composite((1500, 1125), (0, 0), "mod_assets/cg_yuri/b/2.png", (0, 0), "mod_assets/cg_yuri/g.png")
image cg_yuri 2h = im.Composite((1500, 1125), (0, 0), "mod_assets/cg_yuri/b/2.png", (0, 0), "mod_assets/cg_yuri/h.png")
image cg_yuri 2i = im.Composite((1500, 1125), (0, 0), "mod_assets/cg_yuri/b/2.png", (0, 0), "mod_assets/cg_yuri/i.png")
image cg_yuri 2j = im.Composite((1500, 1125), (0, 0), "mod_assets/cg_yuri/b/2.png", (0, 0), "mod_assets/cg_yuri/j.png")
image cg_yuri 2k = im.Composite((1500, 1125), (0, 0), "mod_assets/cg_yuri/b/2.png", (0, 0), "mod_assets/cg_yuri/k.png")
image cg_yuri 2l = im.Composite((1500, 1125), (0, 0), "mod_assets/cg_yuri/b/2.png", (0, 0), "mod_assets/cg_yuri/l.png")
image cg_yuri 2m = im.Composite((1500, 1125), (0, 0), "mod_assets/cg_yuri/b/2.png", (0, 0), "mod_assets/cg_yuri/m.png")
image cg_yuri 2n = im.Composite((1500, 1125), (0, 0), "mod_assets/cg_yuri/b/2.png", (0, 0), "mod_assets/cg_yuri/n.png")

image cg_yuri 3a = im.Composite((1500, 1125), (0, 0), "mod_assets/cg_yuri/b/1.png", (0, 0), "mod_assets/cg_yuri/a.png")
image cg_yuri 3b = im.Composite((1500, 1125), (0, 0), "mod_assets/cg_yuri/b/1.png", (0, 0), "mod_assets/cg_yuri/b.png")
image cg_yuri 3c = im.Composite((1500, 1125), (0, 0), "mod_assets/cg_yuri/b/1.png", (0, 0), "mod_assets/cg_yuri/c.png")
image cg_yuri 3d = im.Composite((1500, 1125), (0, 0), "mod_assets/cg_yuri/b/1.png", (0, 0), "mod_assets/cg_yuri/d.png")
image cg_yuri 3e = im.Composite((1500, 1125), (0, 0), "mod_assets/cg_yuri/b/1.png", (0, 0), "mod_assets/cg_yuri/e.png")
image cg_yuri 3f = im.Composite((1500, 1125), (0, 0), "mod_assets/cg_yuri/b/1.png", (0, 0), "mod_assets/cg_yuri/f.png")
image cg_yuri 3g = im.Composite((1500, 1125), (0, 0), "mod_assets/cg_yuri/b/1.png", (0, 0), "mod_assets/cg_yuri/g.png")
image cg_yuri 3h = im.Composite((1500, 1125), (0, 0), "mod_assets/cg_yuri/b/1.png", (0, 0), "mod_assets/cg_yuri/h.png")
image cg_yuri 3i = im.Composite((1500, 1125), (0, 0), "mod_assets/cg_yuri/b/1.png", (0, 0), "mod_assets/cg_yuri/i.png")
image cg_yuri 3j = im.Composite((1500, 1125), (0, 0), "mod_assets/cg_yuri/b/1.png", (0, 0), "mod_assets/cg_yuri/j.png")
image cg_yuri 3k = im.Composite((1500, 1125), (0, 0), "mod_assets/cg_yuri/b/1.png", (0, 0), "mod_assets/cg_yuri/k.png")
image cg_yuri 3l = im.Composite((1500, 1125), (0, 0), "mod_assets/cg_yuri/b/1.png", (0, 0), "mod_assets/cg_yuri/l.png")
image cg_yuri 3m = im.Composite((1500, 1125), (0, 0), "mod_assets/cg_yuri/b/1.png", (0, 0), "mod_assets/cg_yuri/m.png")
image cg_yuri 3n = im.Composite((1500, 1125), (0, 0), "mod_assets/cg_yuri/b/1.png", (0, 0), "mod_assets/cg_yuri/n.png")

# Monika's Character Definitions
image monika 1 = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/a.png")
image monika 2 = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/a.png")
image monika 3 = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/a.png")
image monika 4 = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/a.png")
image monika 5 = im.Composite((960, 960), (0, 0), "monika/3a.png")

image monika 1a = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/a.png")
image monika 1b = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/b.png")
image monika 1c = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/c.png")
image monika 1d = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/d.png")
image monika 1e = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/e.png")
image monika 1f = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/f.png")
image monika 1g = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/g.png")
image monika 1h = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/h.png")
image monika 1i = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/i.png")
image monika 1j = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/j.png")
image monika 1k = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/k.png")
image monika 1l = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/l.png")
image monika 1m = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/m.png")
image monika 1n = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/n.png")
image monika 1o = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/o.png")
image monika 1p = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/p.png")
image monika 1q = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/q.png")
image monika 1r = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/r.png")

image monika 2a = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/a.png")
image monika 2b = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/b.png")
image monika 2c = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/c.png")
image monika 2d = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/d.png")
image monika 2e = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/e.png")
image monika 2f = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/f.png")
image monika 2g = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/g.png")
image monika 2h = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/h.png")
image monika 2i = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/i.png")
image monika 2j = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/j.png")
image monika 2k = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/k.png")
image monika 2l = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/l.png")
image monika 2m = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/m.png")
image monika 2n = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/n.png")
image monika 2o = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/o.png")
image monika 2p = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/p.png")
image monika 2q = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/q.png")
image monika 2r = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/r.png")

image monika 3a = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/a.png")
image monika 3b = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/b.png")
image monika 3c = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/c.png")
image monika 3d = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/d.png")
image monika 3e = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/e.png")
image monika 3f = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/f.png")
image monika 3g = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/g.png")
image monika 3h = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/h.png")
image monika 3i = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/i.png")
image monika 3j = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/j.png")
image monika 3k = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/k.png")
image monika 3l = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/l.png")
image monika 3m = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/m.png")
image monika 3n = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/n.png")
image monika 3o = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/o.png")
image monika 3p = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/p.png")
image monika 3q = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/q.png")
image monika 3r = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/r.png")

image monika 4a = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/a.png")
image monika 4b = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/b.png")
image monika 4c = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/c.png")
image monika 4d = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/d.png")
image monika 4e = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/e.png")
image monika 4f = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/f.png")
image monika 4g = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/g.png")
image monika 4h = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/h.png")
image monika 4i = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/i.png")
image monika 4j = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/j.png")
image monika 4k = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/k.png")
image monika 4l = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/l.png")
image monika 4m = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/m.png")
image monika 4n = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/n.png")
image monika 4o = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/o.png")
image monika 4p = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/p.png")
image monika 4q = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/q.png")
image monika 4r = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/r.png")

image monika 5a = im.Composite((960, 960), (0, 0), "monika/3a.png")
image monika 5b = im.Composite((960, 960), (0, 0), "monika/3b.png")

image libitina 1a = im.Composite((960, 960), (0, 0), "mod_assets/gov.sdc.libitina/Poses/1.png", (0, 0), "mod_assets/gov.sdc.libitina/Expressions/Pose 1/a.png")
image libitina 1b = im.Composite((960, 960), (0, 0), "mod_assets/gov.sdc.libitina/Poses/1.png", (0, 0), "mod_assets/gov.sdc.libitina/Expressions/Pose 1/b.png")
image libitina 1c = im.Composite((960, 960), (0, 0), "mod_assets/gov.sdc.libitina/Poses/1.png", (0, 0), "mod_assets/gov.sdc.libitina/Expressions/Pose 1/c.png")
image libitina 1d = im.Composite((960, 960), (0, 0), "mod_assets/gov.sdc.libitina/Poses/1.png", (0, 0), "mod_assets/gov.sdc.libitina/Expressions/Pose 1/d.png")
image libitina 1e = im.Composite((960, 960), (0, 0), "mod_assets/gov.sdc.libitina/Poses/1.png", (0, 0), "mod_assets/gov.sdc.libitina/Expressions/Pose 1/e.png")
image libitina 1f = im.Composite((960, 960), (0, 0), "mod_assets/gov.sdc.libitina/Poses/1.png", (0, 0), "mod_assets/gov.sdc.libitina/Expressions/Pose 1/f.png")
image libitina 1g = im.Composite((960, 960), (0, 0), "mod_assets/gov.sdc.libitina/Poses/1.png", (0, 0), "mod_assets/gov.sdc.libitina/Expressions/Pose 1/g.png")
image libitina 1h = im.Composite((960, 960), (0, 0), "mod_assets/gov.sdc.libitina/Poses/1.png", (0, 0), "mod_assets/gov.sdc.libitina/Expressions/Pose 1/h.png")
image libitina 1i = im.Composite((960, 960), (0, 0), "mod_assets/gov.sdc.libitina/Poses/1.png", (0, 0), "mod_assets/gov.sdc.libitina/Expressions/Pose 1/i.png")
image libitina 1j = im.Composite((960, 960), (0, 0), "mod_assets/gov.sdc.libitina/Poses/1.png", (0, 0), "mod_assets/gov.sdc.libitina/Expressions/Pose 1/j.png")
image libitina 1k = im.Composite((960, 960), (0, 0), "mod_assets/gov.sdc.libitina/Poses/1.png", (0, 0), "mod_assets/gov.sdc.libitina/Expressions/Pose 1/k.png")
image libitina 1l = im.Composite((960, 960), (0, 0), "mod_assets/gov.sdc.libitina/Poses/1.png", (0, 0), "mod_assets/gov.sdc.libitina/Expressions/Pose 1/l.png")
image libitina 1m = im.Composite((960, 960), (0, 0), "mod_assets/gov.sdc.libitina/Poses/1.png", (0, 0), "mod_assets/gov.sdc.libitina/Expressions/Pose 1/m.png")
image libitina 1n = im.Composite((960, 960), (0, 0), "mod_assets/gov.sdc.libitina/Poses/1.png", (0, 0), "mod_assets/gov.sdc.libitina/Expressions/Pose 1/n.png")
image libitina 1o = im.Composite((960, 960), (0, 0), "mod_assets/gov.sdc.libitina/Poses/1.png", (0, 0), "mod_assets/gov.sdc.libitina/Expressions/Pose 1/o.png")
image libitina 1p = im.Composite((960, 960), (0, 0), "mod_assets/gov.sdc.libitina/Poses/1.png", (0, 0), "mod_assets/gov.sdc.libitina/Expressions/Pose 1/p.png")
image libitina 1q = im.Composite((960, 960), (0, 0), "mod_assets/gov.sdc.libitina/Poses/1.png", (0, 0), "mod_assets/gov.sdc.libitina/Expressions/Pose 1/q.png")
image libitina 1r = im.Composite((960, 960), (0, 0), "mod_assets/gov.sdc.libitina/Poses/1.png", (0, 0), "mod_assets/gov.sdc.libitina/Expressions/Pose 1/r.png")
image libitina 1s = im.Composite((960, 960), (0, 0), "mod_assets/gov.sdc.libitina/Poses/1.png", (0, 0), "mod_assets/gov.sdc.libitina/Expressions/Pose 1/s.png")
image libitina 1t = im.Composite((960, 960), (0, 0), "mod_assets/gov.sdc.libitina/Poses/1.png", (0, 0), "mod_assets/gov.sdc.libitina/Expressions/Pose 1/t.png")
image libitina 1u = im.Composite((960, 960), (0, 0), "mod_assets/gov.sdc.libitina/Poses/1.png", (0, 0), "mod_assets/gov.sdc.libitina/Expressions/Pose 1/u.png")
image libitina 1v = im.Composite((960, 960), (0, 0), "mod_assets/gov.sdc.libitina/Poses/1.png", (0, 0), "mod_assets/gov.sdc.libitina/Expressions/Pose 1/v.png")
image libitina 1w = im.Composite((960, 960), (0, 0), "mod_assets/gov.sdc.libitina/Poses/1.png", (0, 0), "mod_assets/gov.sdc.libitina/Expressions/Pose 1/w.png")
image libitina 1x = im.Composite((960, 960), (0, 0), "mod_assets/gov.sdc.libitina/Poses/1.png", (0, 0), "mod_assets/gov.sdc.libitina/Expressions/Pose 1/x.png")

## Pose 2
image libitina 2a = im.Composite((960, 960), (0, 0), "mod_assets/gov.sdc.libitina/Poses/2.png", (0, 0), "mod_assets/gov.sdc.libitina/Expressions/Pose 2/a.png")
image libitina 2b = im.Composite((960, 960), (0, 0), "mod_assets/gov.sdc.libitina/Poses/2.png", (0, 0), "mod_assets/gov.sdc.libitina/Expressions/Pose 2/b.png")
image libitina 2c = im.Composite((960, 960), (0, 0), "mod_assets/gov.sdc.libitina/Poses/2.png", (0, 0), "mod_assets/gov.sdc.libitina/Expressions/Pose 2/c.png")
image libitina 2d = im.Composite((960, 960), (0, 0), "mod_assets/gov.sdc.libitina/Poses/2.png", (0, 0), "mod_assets/gov.sdc.libitina/Expressions/Pose 2/d.png")
image libitina 2e = im.Composite((960, 960), (0, 0), "mod_assets/gov.sdc.libitina/Poses/2.png", (0, 0), "mod_assets/gov.sdc.libitina/Expressions/Pose 2/e.png")
image libitina 2f = im.Composite((960, 960), (0, 0), "mod_assets/gov.sdc.libitina/Poses/2.png", (0, 0), "mod_assets/gov.sdc.libitina/Expressions/Pose 2/f.png")
image libitina 2g = im.Composite((960, 960), (0, 0), "mod_assets/gov.sdc.libitina/Poses/2.png", (0, 0), "mod_assets/gov.sdc.libitina/Expressions/Pose 2/g.png")
image libitina 2h = im.Composite((960, 960), (0, 0), "mod_assets/gov.sdc.libitina/Poses/2.png", (0, 0), "mod_assets/gov.sdc.libitina/Expressions/Pose 2/h.png")
image libitina 2i = im.Composite((960, 960), (0, 0), "mod_assets/gov.sdc.libitina/Poses/2.png", (0, 0), "mod_assets/gov.sdc.libitina/Expressions/Pose 2/i.png")
image libitina 2j = im.Composite((960, 960), (0, 0), "mod_assets/gov.sdc.libitina/Poses/2.png", (0, 0), "mod_assets/gov.sdc.libitina/Expressions/Pose 2/j.png")
image libitina 2k = im.Composite((960, 960), (0, 0), "mod_assets/gov.sdc.libitina/Poses/2.png", (0, 0), "mod_assets/gov.sdc.libitina/Expressions/Pose 2/k.png")
image libitina 2l = im.Composite((960, 960), (0, 0), "mod_assets/gov.sdc.libitina/Poses/2.png", (0, 0), "mod_assets/gov.sdc.libitina/Expressions/Pose 2/l.png")
image libitina 2m = im.Composite((960, 960), (0, 0), "mod_assets/gov.sdc.libitina/Poses/2.png", (0, 0), "mod_assets/gov.sdc.libitina/Expressions/Pose 2/m.png")
image libitina 2n = im.Composite((960, 960), (0, 0), "mod_assets/gov.sdc.libitina/Poses/2.png", (0, 0), "mod_assets/gov.sdc.libitina/Expressions/Pose 2/n.png")
image libitina 2o = im.Composite((960, 960), (0, 0), "mod_assets/gov.sdc.libitina/Poses/2.png", (0, 0), "mod_assets/gov.sdc.libitina/Expressions/Pose 2/o.png")
image libitina 2p = im.Composite((960, 960), (0, 0), "mod_assets/gov.sdc.libitina/Poses/2.png", (0, 0), "mod_assets/gov.sdc.libitina/Expressions/Pose 2/p.png")
image libitina 2q = im.Composite((960, 960), (0, 0), "mod_assets/gov.sdc.libitina/Poses/2.png", (0, 0), "mod_assets/gov.sdc.libitina/Expressions/Pose 2/q.png")
image libitina 2r = im.Composite((960, 960), (0, 0), "mod_assets/gov.sdc.libitina/Poses/2.png", (0, 0), "mod_assets/gov.sdc.libitina/Expressions/Pose 2/r.png")
image libitina 2s = im.Composite((960, 960), (0, 0), "mod_assets/gov.sdc.libitina/Poses/2.png", (0, 0), "mod_assets/gov.sdc.libitina/Expressions/Pose 2/s.png")
image libitina 2t = im.Composite((960, 960), (0, 0), "mod_assets/gov.sdc.libitina/Poses/2.png", (0, 0), "mod_assets/gov.sdc.libitina/Expressions/Pose 2/t.png")
image libitina 2u = im.Composite((960, 960), (0, 0), "mod_assets/gov.sdc.libitina/Poses/2.png", (0, 0), "mod_assets/gov.sdc.libitina/Expressions/Pose 2/u.png")
image libitina 2v = im.Composite((960, 960), (0, 0), "mod_assets/gov.sdc.libitina/Poses/2.png", (0, 0), "mod_assets/gov.sdc.libitina/Expressions/Pose 2/v.png")
image libitina 2w = im.Composite((960, 960), (0, 0), "mod_assets/gov.sdc.libitina/Poses/2.png", (0, 0), "mod_assets/gov.sdc.libitina/Expressions/Pose 2/w.png")
image libitina 2x = im.Composite((960, 960), (0, 0), "mod_assets/gov.sdc.libitina/Poses/2.png", (0, 0), "mod_assets/gov.sdc.libitina/Expressions/Pose 2/x.png")

## Yandere Look for Pose 2
image libitina 2yb = im.Composite((960, 960), (0, 0), "mod_assets/gov.sdc.libitina/Poses/2.png", (0, 0), "mod_assets/gov.sdc.libitina/Expressions/Pose 3/b.png")

## Pose 3
image libitina 3a = im.Composite((960, 960), (0, 0), "mod_assets/gov.sdc.libitina/Poses/3.png", (0, 0), "mod_assets/gov.sdc.libitina/Expressions/Pose 3/a2.png")
image libitina 3a2 = im.Composite((960, 960), (0, 0), "mod_assets/gov.sdc.libitina/Poses/3.png", (0, 0), "mod_assets/gov.sdc.libitina/Expressions/Pose 3/a.png")
image libitina 3b = im.Composite((960, 960), (0, 0), "mod_assets/gov.sdc.libitina/Poses/3.png", (0, 0), "mod_assets/gov.sdc.libitina/Expressions/Pose 3/b.png")
image libitina 3b2 = im.Composite((960, 960), (0, 0), "mod_assets/gov.sdc.libitina/Poses/3.png", (0, 0), "mod_assets/gov.sdc.libitina/Expressions/Pose 3/b2.png")
image libitina 3c = im.Composite((960, 960), (0, 0), "mod_assets/gov.sdc.libitina/Poses/3.png", (0, 0), "mod_assets/gov.sdc.libitina/Expressions/Pose 3/c.png")
image libitina 3c2 = im.Composite((960, 960), (0, 0), "mod_assets/gov.sdc.libitina/Poses/3.png", (0, 0), "mod_assets/gov.sdc.libitina/Expressions/Pose 3/c2.png")
image libitina 3d = im.Composite((960, 960), (0, 0), "mod_assets/gov.sdc.libitina/Poses/3.png", (0, 0), "mod_assets/gov.sdc.libitina/Expressions/Pose 3/d.png")
image libitina 3e = im.Composite((960, 960), (0, 0), "mod_assets/gov.sdc.libitina/Poses/3.png", (0, 0), "mod_assets/gov.sdc.libitina/Expressions/Pose 3/floating rl eyes.png", (0, 0), "mod_assets/gov.sdc.libitina/Expressions/Pose 3/e.png")
image libitina 3f = im.Composite((960, 960), (0, 0), "mod_assets/gov.sdc.libitina/Poses/3.png", (0, 0), "mod_assets/gov.sdc.libitina/Expressions/Pose 3/floating rl eyes.png", (0, 0), "mod_assets/gov.sdc.libitina/Expressions/Pose 3/f.png")

#swimsuit
image libitina 1sa = im.Composite((960, 960), (0, 0), "mod_assets/gov.sdc.libitina/Poses/s1.png", (0, 0), "mod_assets/gov.sdc.libitina/Expressions/Pose 1/a.png")
image libitina 1sb = im.Composite((960, 960), (0, 0), "mod_assets/gov.sdc.libitina/Poses/s1.png", (0, 0), "mod_assets/gov.sdc.libitina/Expressions/Pose 1/b.png")
image libitina 1sc = im.Composite((960, 960), (0, 0), "mod_assets/gov.sdc.libitina/Poses/s1.png", (0, 0), "mod_assets/gov.sdc.libitina/Expressions/Pose 1/c.png")
image libitina 1sd = im.Composite((960, 960), (0, 0), "mod_assets/gov.sdc.libitina/Poses/s1.png", (0, 0), "mod_assets/gov.sdc.libitina/Expressions/Pose 1/d.png")
image libitina 1se = im.Composite((960, 960), (0, 0), "mod_assets/gov.sdc.libitina/Poses/s1.png", (0, 0), "mod_assets/gov.sdc.libitina/Expressions/Pose 1/e.png")
image libitina 1sf = im.Composite((960, 960), (0, 0), "mod_assets/gov.sdc.libitina/Poses/s1.png", (0, 0), "mod_assets/gov.sdc.libitina/Expressions/Pose 1/f.png")
image libitina 1sg = im.Composite((960, 960), (0, 0), "mod_assets/gov.sdc.libitina/Poses/s1.png", (0, 0), "mod_assets/gov.sdc.libitina/Expressions/Pose 1/g.png")
image libitina 1sh = im.Composite((960, 960), (0, 0), "mod_assets/gov.sdc.libitina/Poses/s1.png", (0, 0), "mod_assets/gov.sdc.libitina/Expressions/Pose 1/h.png")
image libitina 1si = im.Composite((960, 960), (0, 0), "mod_assets/gov.sdc.libitina/Poses/s1.png", (0, 0), "mod_assets/gov.sdc.libitina/Expressions/Pose 1/i.png")
image libitina 1sj = im.Composite((960, 960), (0, 0), "mod_assets/gov.sdc.libitina/Poses/s1.png", (0, 0), "mod_assets/gov.sdc.libitina/Expressions/Pose 1/j.png")
image libitina 1sk = im.Composite((960, 960), (0, 0), "mod_assets/gov.sdc.libitina/Poses/s1.png", (0, 0), "mod_assets/gov.sdc.libitina/Expressions/Pose 1/k.png")
image libitina 1sl = im.Composite((960, 960), (0, 0), "mod_assets/gov.sdc.libitina/Poses/s1.png", (0, 0), "mod_assets/gov.sdc.libitina/Expressions/Pose 1/l.png")
image libitina 1sm = im.Composite((960, 960), (0, 0), "mod_assets/gov.sdc.libitina/Poses/s1.png", (0, 0), "mod_assets/gov.sdc.libitina/Expressions/Pose 1/m.png")
image libitina 1sn = im.Composite((960, 960), (0, 0), "mod_assets/gov.sdc.libitina/Poses/s1.png", (0, 0), "mod_assets/gov.sdc.libitina/Expressions/Pose 1/n.png")
image libitina 1so = im.Composite((960, 960), (0, 0), "mod_assets/gov.sdc.libitina/Poses/s1.png", (0, 0), "mod_assets/gov.sdc.libitina/Expressions/Pose 1/o.png")
image libitina 1sp = im.Composite((960, 960), (0, 0), "mod_assets/gov.sdc.libitina/Poses/s1.png", (0, 0), "mod_assets/gov.sdc.libitina/Expressions/Pose 1/p.png")
image libitina 1sq = im.Composite((960, 960), (0, 0), "mod_assets/gov.sdc.libitina/Poses/s1.png", (0, 0), "mod_assets/gov.sdc.libitina/Expressions/Pose 1/q.png")
image libitina 1sr = im.Composite((960, 960), (0, 0), "mod_assets/gov.sdc.libitina/Poses/s1.png", (0, 0), "mod_assets/gov.sdc.libitina/Expressions/Pose 1/r.png")
image libitina 1ss = im.Composite((960, 960), (0, 0), "mod_assets/gov.sdc.libitina/Poses/s1.png", (0, 0), "mod_assets/gov.sdc.libitina/Expressions/Pose 1/s.png")
image libitina 1st = im.Composite((960, 960), (0, 0), "mod_assets/gov.sdc.libitina/Poses/s1.png", (0, 0), "mod_assets/gov.sdc.libitina/Expressions/Pose 1/t.png")
image libitina 1su = im.Composite((960, 960), (0, 0), "mod_assets/gov.sdc.libitina/Poses/s1.png", (0, 0), "mod_assets/gov.sdc.libitina/Expressions/Pose 1/u.png")
image libitina 1sv = im.Composite((960, 960), (0, 0), "mod_assets/gov.sdc.libitina/Poses/s1.png", (0, 0), "mod_assets/gov.sdc.libitina/Expressions/Pose 1/v.png")
image libitina 1sw = im.Composite((960, 960), (0, 0), "mod_assets/gov.sdc.libitina/Poses/s1.png", (0, 0), "mod_assets/gov.sdc.libitina/Expressions/Pose 1/w.png")
image libitina 1sx = im.Composite((960, 960), (0, 0), "mod_assets/gov.sdc.libitina/Poses/s1.png", (0, 0), "mod_assets/gov.sdc.libitina/Expressions/Pose 1/x.png")

## Pose 2
image libitina 2sa = im.Composite((960, 960), (0, 0), "mod_assets/gov.sdc.libitina/Poses/s2.png", (0, 0), "mod_assets/gov.sdc.libitina/Expressions/Pose 2/a.png")
image libitina 2sb = im.Composite((960, 960), (0, 0), "mod_assets/gov.sdc.libitina/Poses/s2.png", (0, 0), "mod_assets/gov.sdc.libitina/Expressions/Pose 2/b.png")
image libitina 2sc = im.Composite((960, 960), (0, 0), "mod_assets/gov.sdc.libitina/Poses/s2.png", (0, 0), "mod_assets/gov.sdc.libitina/Expressions/Pose 2/c.png")
image libitina 2sd = im.Composite((960, 960), (0, 0), "mod_assets/gov.sdc.libitina/Poses/s2.png", (0, 0), "mod_assets/gov.sdc.libitina/Expressions/Pose 2/d.png")
image libitina 2se = im.Composite((960, 960), (0, 0), "mod_assets/gov.sdc.libitina/Poses/s2.png", (0, 0), "mod_assets/gov.sdc.libitina/Expressions/Pose 2/e.png")
image libitina 2sf = im.Composite((960, 960), (0, 0), "mod_assets/gov.sdc.libitina/Poses/s2.png", (0, 0), "mod_assets/gov.sdc.libitina/Expressions/Pose 2/f.png")
image libitina 2sg = im.Composite((960, 960), (0, 0), "mod_assets/gov.sdc.libitina/Poses/s2.png", (0, 0), "mod_assets/gov.sdc.libitina/Expressions/Pose 2/g.png")
image libitina 2sh = im.Composite((960, 960), (0, 0), "mod_assets/gov.sdc.libitina/Poses/s2.png", (0, 0), "mod_assets/gov.sdc.libitina/Expressions/Pose 2/h.png")
image libitina 2si = im.Composite((960, 960), (0, 0), "mod_assets/gov.sdc.libitina/Poses/s2.png", (0, 0), "mod_assets/gov.sdc.libitina/Expressions/Pose 2/i.png")
image libitina 2sj = im.Composite((960, 960), (0, 0), "mod_assets/gov.sdc.libitina/Poses/s2.png", (0, 0), "mod_assets/gov.sdc.libitina/Expressions/Pose 2/j.png")
image libitina 2sk = im.Composite((960, 960), (0, 0), "mod_assets/gov.sdc.libitina/Poses/s2.png", (0, 0), "mod_assets/gov.sdc.libitina/Expressions/Pose 2/k.png")
image libitina 2sl = im.Composite((960, 960), (0, 0), "mod_assets/gov.sdc.libitina/Poses/s2.png", (0, 0), "mod_assets/gov.sdc.libitina/Expressions/Pose 2/l.png")
image libitina 2sm = im.Composite((960, 960), (0, 0), "mod_assets/gov.sdc.libitina/Poses/s2.png", (0, 0), "mod_assets/gov.sdc.libitina/Expressions/Pose 2/m.png")
image libitina 2sn = im.Composite((960, 960), (0, 0), "mod_assets/gov.sdc.libitina/Poses/s2.png", (0, 0), "mod_assets/gov.sdc.libitina/Expressions/Pose 2/n.png")
image libitina 2so = im.Composite((960, 960), (0, 0), "mod_assets/gov.sdc.libitina/Poses/s2.png", (0, 0), "mod_assets/gov.sdc.libitina/Expressions/Pose 2/o.png")
image libitina 2sp = im.Composite((960, 960), (0, 0), "mod_assets/gov.sdc.libitina/Poses/s2.png", (0, 0), "mod_assets/gov.sdc.libitina/Expressions/Pose 2/p.png")
image libitina 2sq = im.Composite((960, 960), (0, 0), "mod_assets/gov.sdc.libitina/Poses/s2.png", (0, 0), "mod_assets/gov.sdc.libitina/Expressions/Pose 2/q.png")
image libitina 2sr = im.Composite((960, 960), (0, 0), "mod_assets/gov.sdc.libitina/Poses/s2.png", (0, 0), "mod_assets/gov.sdc.libitina/Expressions/Pose 2/r.png")
image libitina 2ss = im.Composite((960, 960), (0, 0), "mod_assets/gov.sdc.libitina/Poses/s2.png", (0, 0), "mod_assets/gov.sdc.libitina/Expressions/Pose 2/s.png")
image libitina 2st = im.Composite((960, 960), (0, 0), "mod_assets/gov.sdc.libitina/Poses/s2.png", (0, 0), "mod_assets/gov.sdc.libitina/Expressions/Pose 2/t.png")
image libitina 2su = im.Composite((960, 960), (0, 0), "mod_assets/gov.sdc.libitina/Poses/s2.png", (0, 0), "mod_assets/gov.sdc.libitina/Expressions/Pose 2/u.png")
image libitina 2sv = im.Composite((960, 960), (0, 0), "mod_assets/gov.sdc.libitina/Poses/s2.png", (0, 0), "mod_assets/gov.sdc.libitina/Expressions/Pose 2/v.png")
image libitina 2sw = im.Composite((960, 960), (0, 0), "mod_assets/gov.sdc.libitina/Poses/s2.png", (0, 0), "mod_assets/gov.sdc.libitina/Expressions/Pose 2/w.png")
image libitina 2sx = im.Composite((960, 960), (0, 0), "mod_assets/gov.sdc.libitina/Poses/s2.png", (0, 0), "mod_assets/gov.sdc.libitina/Expressions/Pose 2/x.png")

## Yandere Look for Pose 2
image libitina 2syb = im.Composite((960, 960), (0, 0), "mod_assets/gov.sdc.libitina/Poses/s2.png", (0, 0), "mod_assets/gov.sdc.libitina/Expressions/Pose 3/b.png")

## Pose 3
image libitina 3sa = im.Composite((960, 960), (0, 0), "mod_assets/gov.sdc.libitina/Poses/s3.png", (0, 0), "mod_assets/gov.sdc.libitina/Expressions/Pose 3/a2.png")
image libitina 3sa2 = im.Composite((960, 960), (0, 0), "mod_assets/gov.sdc.libitina/Poses/s3.png", (0, 0), "mod_assets/gov.sdc.libitina/Expressions/Pose 3/a.png")
image libitina 3sb = im.Composite((960, 960), (0, 0), "mod_assets/gov.sdc.libitina/Poses/s3.png", (0, 0), "mod_assets/gov.sdc.libitina/Expressions/Pose 3/b.png")
image libitina 3sb2 = im.Composite((960, 960), (0, 0), "mod_assets/gov.sdc.libitina/Poses/s3.png", (0, 0), "mod_assets/gov.sdc.libitina/Expressions/Pose 3/b2.png")
image libitina 3sc = im.Composite((960, 960), (0, 0), "mod_assets/gov.sdc.libitina/Poses/s3.png", (0, 0), "mod_assets/gov.sdc.libitina/Expressions/Pose 3/c.png")
image libitina 3sc2 = im.Composite((960, 960), (0, 0), "mod_assets/gov.sdc.libitina/Poses/s3.png", (0, 0), "mod_assets/gov.sdc.libitina/Expressions/Pose 3/c2.png")
image libitina 3sd = im.Composite((960, 960), (0, 0), "mod_assets/gov.sdc.libitina/Poses/s3.png", (0, 0), "mod_assets/gov.sdc.libitina/Expressions/Pose 3/d.png")
image libitina 3se = im.Composite((960, 960), (0, 0), "mod_assets/gov.sdc.libitina/Poses/s3.png", (0, 0), "mod_assets/gov.sdc.libitina/Expressions/Pose 3/floating rl eyes.png", (0, 0), "mod_assets/gov.sdc.libitina/Expressions/Pose 3/e.png")
image libitina 3sf = im.Composite((960, 960), (0, 0), "mod_assets/gov.sdc.libitina/Poses/s3.png", (0, 0), "mod_assets/gov.sdc.libitina/Expressions/Pose 3/floating rl eyes.png", (0, 0), "mod_assets/gov.sdc.libitina/Expressions/Pose 3/f.png")

# This image transform shows a glitched Monika during a special poem.
image monika g1:
    "monika/g1.png"
    xoffset 35 yoffset 55
    parallel:
        zoom 1.00
        linear 0.10 zoom 1.03
        repeat
    parallel:
        xoffset 35
        0.20
        xoffset 0
        0.05
        xoffset -10
        0.05
        xoffset 0
        0.05
        xoffset -80
        0.05
        repeat
    time 1.25
    xoffset 0 yoffset 0 zoom 1.00
    "monika 3"

# This image transform shows Monika being glitched as she is 
# deleted in Act 3.
image monika g2:
    block:
        choice:
            "monika/g2.png"
        choice:
            "monika/g3.png"
        choice:
            "monika/g4.png"
    block:
        choice:
            pause 0.05
        choice:
            pause 0.1
        choice:
            pause 0.15
        choice:
            pause 0.2
    repeat

## Character Variables
# This is where the characters are declared in the mod.
# To define a new character with assets, declare a character variable like in this example:
#   define e = DynamicCharacter('e_name', image='eileen', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
# To define a new character without assets, declare a character variable like this instead:
#   define en = Character('Eileen & Nat', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")

define narrator = Character(ctc="ctc", ctc_position="fixed")
define mc = DynamicCharacter('player', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed", window_background=Image("mod_assets/mc_name.png", xalign=0.5, yalign=1.0))
define s = DynamicCharacter('s_name', image='sayori', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed", window_background=Image("mod_assets/s_name.png", xalign=0.5, yalign=1.0))
define m = DynamicCharacter('m_name', image='monika', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed", window_background=Image("mod_assets/m_name.png", xalign=0.5, yalign=1.0))
define n = DynamicCharacter('n_name', image='natsuki', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed", window_background=Image("mod_assets/n_name.png", xalign=0.5, yalign=1.0))
define y = DynamicCharacter('y_name', image='yuri', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed", window_background=Image("mod_assets/y_name.png", xalign=0.5, yalign=1.0))
define k = DynamicCharacter('k_name', image='kotonoha', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed", window_background=Image("mod_assets/k_name.png", xalign=0.5, yalign=1.0))
define ny = Character('Nat & Yuri', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define a = DynamicCharacter('a_name', image='???', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define d = DynamicCharacter('d_name', image='doctor', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define co = DynamicCharacter('co_name', image='codex', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define cgy = DynamicCharacter('cgy_name', image='cg_yuri', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define l = DynamicCharacter('l_name', image='libitina', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define ida = DynamicCharacter('i_name', image='ida', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
# This variable determines whether to allow the player to dismiss pauses.
# By default this is set by config.developer which is normally set to false
# once you packaged your mod.
define _dismiss_pause = config.developer

## [BETA] Pronoun Variables
# This section adds the feature to use player pronouns within the game text easily.
# To use this feature, simply ask the user for their pronoun and use it here.
# For capitalization, use heC, himC, areC and hesC
default persistent.he = ""
default persistent.him = ""
default persistent.are = ""
default persistent.hes = ""
default he = persistent.he
default him = persistent.him
default are = persistent.are
default hes = persistent.hes
default he_capital = he.capitalize()
default him_capital = him.capitalize()
default are_capital = are.capitalize()
default hes_capital = hes.capitalize()

## Extra Settings Variables
# This section controls whether the mod is censored or is in let's play mode.
default persistent.uncensored_mode = False
default persistent.lets_play = False

## Variables
# This section declares variables when the mod runs for the first time on all saves.
# To make a new persistent variable, make a new variable with the 'persistent.' in it's name
# like in this example:
#   default persistent.monika = 1
# To make a non-persistent variable, make a new variable like this instead:
#   default cookies = False
# To make sure a variable is set to a given condition use 'define' rather than 'default'.

default persistent.playername = ""
default player = persistent.playername
default persistent.playthrough = 0
default persistent.yuri_kill = 0
default persistent.seen_eyes = None
default persistent.seen_sticker = None
default persistent.ghost_menu = None
default persistent.seen_ghost_menu = None
default seen_eyes_this_chapter = False
default persistent.anticheat = 0
default persistent.clear = [False, False, False, False, False, False, False, False, False, False]
default persistent.special_poems = None
default persistent.clearall = None
default persistent.menu_bg_m = None
default persistent.first_load = None
default persistent.first_poem = None
default persistent.seen_colors_poem = None
default persistent.monika_back = None

default in_sayori_kill = None
default in_yuri_kill = None
default anticheat = 0
define config.mouse = None
default allow_skipping = True
default basedir = config.basedir
default chapter = 0
default currentpos = 0
default faint_effect = None

# Default Name Variables
# To define a default name make a character name variable like in this example:
#   default e_name = "Eileen"

default s_name = "Sayori"
default m_name = "Monika"
default n_name = "Natsuki"
default y_name = "Yuri"
default a_name = "???"
default v_name = "Voice"
default p_name = "The Programmer"
default d_name = "Doctor"
default k_name = "Kotonoha"
default co_name = "Codex"


# Poem Variables
# This section records how much each character likes your poem in-game.
# Syntax:
#   -1 - Bad
#   0 - Neutral
#   1 - Good
# To add a new poem person, make a poem array like in this example:
#   default e_poemappeal = [0, 0, 0]

default n_poemappeal = [0, 0, 0]
default s_poemappeal = [0, 0, 0]
default y_poemappeal = [0, 0, 0]
default m_poemappeal = [0, 0, 0]

# This variable keeps tracks on which person won the poem session after each day.
default poemwinner = ['sayori', 'sayori', 'sayori']

# These variables keep track on who has read your poem during poem sharing
default s_readpoem = False
default n_readpoem = False
default y_readpoem = False
default m_readpoem = False

# This variable keeps track on how many people have read your poem.
default poemsread = 0

# These variables store the appeal a character has to your poem
default n_appeal = 0
default s_appeal = 0
default y_appeal = 0
default m_appeal = 0

# These variables control if we have seen Natsuki's or Yuri's exclusive scenes
default n_exclusivewatched = False
default y_exclusivewatched = False

# These variables track whether we gave Yuri our poem in Act 2 and if she
# ran away during Act 2 poem sharing.
default y_gave = False
default y_ranaway = False

# These variables track whether we read Natsuki's or Yuri's 3rd poem in poem sharing.
default n_read3 = False
default y_read3 = False

# This variable tracks which person we sided with in Day 2 of the game.
default ch1_choice = "sayori"

# This variable tracks if we gave Natsuki our poem first during poem sharing.
default n_poemearly = False

# These variables track whether we tried to help Monika or Sayori during Day 3's ending.
default help_sayori = None
default help_monika = None

# These variables track which route Day 4 will play and who is their name.
default ch4_scene = "yuri"
default ch4_name = "Yuri"

# This variable tracks whether we accepted Sayori's confession or not.
default sayori_confess = True

# This variable tracks whether we read Natsuki's 3rd poem in Act 2.
default natsuki_23 = None

transform saul_ok:
        subpixel True align (0.5, 0.515)        

        parallel:
            ease_quad 2.0 xoffset -120.0
            easeout_quad 1.5 xoffset 190.0
        parallel:
            ease_quad 3.5 zoom 1.5 yoffset 200.0
        
        zoom 2.0 offset (-300.0, 300.0)
        easeout_expo 2.37 zoom 1.8 offset (-220.0, 220.0)
        easein_quint 1.63 zoom 0.8 offset (0.0, 0.0)
        ease_expo 4.7 zoom 2.2 offset (-200.0, 350.0)

        offset (120.0, 200.0) zoom 1.5

        parallel:
            ease_quad 2.0 xoffset -120.0
            easeout_quad 1.3 xoffset 0.0
        parallel:
            ease_quad 3.2 zoom 0.8 yoffset 0.0
        
        yanchor 1.0 ypos 1.03