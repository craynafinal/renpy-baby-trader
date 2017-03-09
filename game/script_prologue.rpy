label prologue:

    #play music "sound/bgm/bgm_rain.ogg" fadein 4.0
    scene bg_black

    $renpy.pause(1.0, hard = True)

    ch_babyTrader "저의 가게에 어서 오십시오."

    hide bg_black
    scene bg_prologue with fade
    show scg_babyTrader normal with dissolve

    ch_babyTrader "사람들은 저를 [ch_babyTrader]이라고 부르지요."

    ch_babyTrader "혹시 자신의 아이가 맘에 들지 않습니까? 말썽을 부리거나 다른 아이들에 비해 열등한 아이를 갖고 계십니까?"

    ch_babyTrader "아이가 학습 속도가 느리거나 말을 듣지 않아서 장차 미래가 불안하신가요?"

    ch_babyTrader "그런 고객님께 제가 아주 좋은 제안을 드리려고 합니다."

    ch_babyTrader "제 이름에서 벌써 눈치채신 분도 계시겠지만 저는 아이들을 사고 파는 나부랭이지요, 후후훗..."

    ch_babyTrader "고객님의 실망스러운 아이를 제게 데려오시면 좋은 가격에 매입해드립니다."

    ch_babyTrader "골칫거리 아이를 처리하고 돈까지 받을 수 있다니..."

    ch_babyTrader "이것이야 말로 일석이조, 꿩먹고 알먹기, 도랑치고 가재잡고, 누이좋고 매부좋고, 님도 보고 뽕도..."
    
    ch_babyTrader "이런이런, 제가 너무 흥분을 한 것 같군요, 후후훗..."

    ch_babyTrader "이런, 아이를 제게 판매 하셨으니 이제는 다른 아이가 필요 하시겠군요."
    
    ch_babyTrader "물론 고객님께 딱 맞는 아름답고 똑똑한 아이를 말입니다."

    ch_babyTrader "저의 인벤토리에는 고객님들을 기다리고 있는 최상급의 훌륭한 아기 상품들이 넘쳐나지요."

    ch_babyTrader "의사가 될 아이가 필요하신가요? 변호사나 판사, 연예인, 정치인, 혹은 사장님은 어떻습니까?"

    ch_babyTrader "하지만 역시 아이의 직업만으로는 여러분의 욕망을 전부 채워드릴 수 없겠지요."

    ch_babyTrader "앞으로 잘생겨질 아이, 몸매 좋아질 아이, 효도할 아이, 착하고 사랑받을 아이 등 수많은 옵션을 추가하실 수 있지요."

    ch_babyTrader "어이쿠, 잊을뻔 했군요. 아이를 판매해주신 분들께는 특별 할인 혜택을 드리고 있으니 참고해주시기 바랍니다."

    ch_babyTrader "고객님의 행복과 만족을 저 [ch_babyTrader]이 책임지겠습니다."

    ch_babyTrader "그럼 조만간 뵙도록 하겠습니다, 후후훗..."

    hide scg_babyTrader
    hide bg_prologue
    with dissolve
    
    jump common_1

