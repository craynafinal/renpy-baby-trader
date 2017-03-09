init 0:
    # language configuration
    $gui.language = "korean-with-spaces"

    # path configuration
    $path_image_bg = "bg/"
    $path_image_sgc = "scg/"
    
    # character definitions
    define ch_narrator = Character(None)
    # 그냥 베이비 트레이더라고 할까
    define ch_babyTrader = Character("아이 상인", color = "#0f60e2")
    define ch_mother = Character("엄마", color = "#0f60e2")
    define ch_boy = Character("소년", color = "#0f60e2")
    define ch_main = Character("민호", color = "#0f60e2")

    # image definitions
    image bg_prologue = path_image_bg + "bg_test.png"
    image bg_black = "#000000"

    # standing cg definitions
    image scg_babyTrader normal:
        im.FactorScale(path_image_sgc + "scg_test.png", 0.9)