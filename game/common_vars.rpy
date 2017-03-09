init 0:
    # language
    $gui.language = "korean-with-spaces"

    # path
    $path_image_bg = "bg/"
    $path_image_sgc = "scg/"
    $path_audio_bgm = "sound/bgm/"
    $path_audio_sound = "sound/effect/"
    
    # character
    define ch_narrator = Character(None)
    # 그냥 베이비 트레이더라고 할까
    define ch_babyTrader = Character("아이 상인", color = "#0f60e2")
    define ch_mother = Character("엄마", color = "#0f60e2")
    define ch_boy = Character("소년", color = "#0f60e2")
    define ch_main = Character("민호", color = "#0f60e2")

    # image
    image bg_prologue = path_image_bg + "bg_test.png"
    image bg_black = "#000000"

    # standing cg
    image scg_babyTrader normal:
        im.FactorScale(path_image_sgc + "scg_test.png", 0.9)

    # bgms
    define audio.bgm_strange_ways = path_audio_bgm + "Strange_Ways.mp3" # prologue
    define audio.bgm_blakey_s_burnout = path_audio_bgm + "Blakey_s_Burnout.mp3" # baby trader jazz
    define audio.bgm_boat_floating = path_audio_bgm + "Boat_Floating.mp3" # mother hits boy
    define audio.bgm_back_of_the_room_hang = path_audio_bgm + "Back_of_the_Room_Hang.mp3" # after sale

    
    # sound effects
    define audio.sound_door_bell = path_audio_sound + "Door_Bell.mp3"
    define audio.sound_door_close = path_audio_sound + "Door_Close.mp3"
    define audio.sound_light_switch = path_audio_sound + "Light_Switch.mp3"
    define audio.sound_walk_on_hollow_wood = path_audio_sound + "Walk_On_Hollow_Wood.mp3"
    define audio.sound_beep_alert = path_audio_sound + "Beep_Alert.mp3"
    define audio.sound_shock = path_audio_sound + "Shock.mp3"
    define audio.sound_face_hit_1 = path_audio_sound + "Face_Hit_1.mp3"
    define audio.sound_face_hit_2 = path_audio_sound + "Face_Hit_2.mp3"
    define audio.sound_face_hit_3 = path_audio_sound + "Face_Hit_3.mp3"
    