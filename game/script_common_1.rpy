label common_1:
    scene bg_black

    $renpy.pause(3.0, hard = True)

    play sound sound_face_hit_1

    ch_narrator "짝!"

    ch_boy "(TV나 전단지를 보면 종종 그런 장면들이 있다.)"

    ch_boy "(엄마, 아빠, 그리고 아이가 행복하게 웃으며 즐거운 시간을 보내고 있는 모습.)"

    play sound sound_face_hit_2

    ch_narrator "퍽!"

    ch_boy "(그런 사진이나 광고를 보고 있으면 정말 마음이 따뜻해져서 기분이 좋았다.)"

    play sound sound_face_hit_1

    ch_narrator "짝!"

    ch_boy "(하지만 나는 항상 궁금했다.)"

    ch_boy "(어째서 그 사람들은 그렇게 즐겁게 웃을 수 있는 것일까?)"

    play sound sound_face_hit_3

    ch_narrator "쿵!"

    ch_boy "(나는... 항상...)"

    play sound sound_face_hit_2

    ch_narrator "퍽!"

    ch_mother "너는 왜 이모양이니?!"

    # show bg here with fade
    play music bgm_boat_floating

    ch_narrator "배를 감싸안은 채 쓰러져 있는 [ch_boy]의 어머니로 보이는 여자는 많은 X 표시가 보이는 시험지를 펄럭이며 화를 내고 있다."

    ch_mother "아직 구구단도 제대로 못 외운단 말이니! 정말 답답하구나, 이래서 커서 뭐가 되려고 그러니!"    

    ch_boy "어... 엄마... 너무 어려워요..."

    ch_mother "지금 말대꾸 하는거니?! 그리고 그게 뭐 어쨌다고 그러는거니! 옆집 성호는 벌써 초등학생이 풀 문제를 푼다고 하더라! 너 같은 열등한 아이가 내 아들이라니..."

    ch_narrator "[ch_boy]은 뭐라 대꾸 할 말을 찾지 못하고 고개를 떨구고 눈을 감았다."
    
    ch_narrator "그리고 생각했다."

    ch_narrator "(그래, 조금만 참으면 돼. 항상 그래왔잖아? 조금만 더.)"
    
    ch_narrator "(끝나면 밖에 나가서 소리내어 조금 울고 들어오자. 그리고 어두워지면 돌아와서 자면 되는거야.)"

    ch_narrator "하지만 그 날은 [ch_boy]의 생각과는 조금 달랐다."

    ch_mother "더 이상은 안되겠어. 이젠 못 참아! 당장 너를 [ch_babyTrader]에게 데려가야 겠어."

    play sound sound_shock

    ch_narrator "갑자기 가슴을 큰 망치로 두드려 맞은 것 같은 느낌이 들었다. 가슴이 저리고 머리가 어지러웠다. [ch_boy]은 지금 빨리 어머니의 마음을 돌리지 않으면 안될 것 같은 느낌이 들었다."
    
    ch_narrator "떨리는 손으로 어머니의 치맛자락을 잡고 그는 입을 떼었다."

    ch_boy "어... 엄마, 무... 무슨소리를 하시는 거예요? 지금 농담 하시는 것 맞죠?"

    ch_mother "이것 놔라! 지아비도 없이 엄마 혼자서 힘들게 널 키웠으면 보람이라도 있어야지! 너 같이 쓸모없는 아이는 필요 없다!"

    ch_boy "제... 제발요... 뭐든지 할게요 엄마... 공부 열심히 할게요 엄마... 말도 잘 들을게요 엄마... 제발 절 버리지 마세요..."

    ch_narrator "어느새 [ch_boy]의 얼굴은 눈물과 콧물로 범벅이 되었다."

    ch_narrator "[ch_boy]은 [ch_babyTrader]에 대해 유치원에서 아이들이 이야기 하는 것을 들은 적이 있다. 갑자기 유치원에 더 이상 나오지 않는 아이들이 몇 있었는데 [ch_babyTrader]에게 팔려갔다는 소문이었다."

    ch_narrator "그 아이들은 대부분 시끄럽거나 문제를 일으키고 선생님들이 가르치는 내용에 대해 흥미를 보이지 않는 아이들이었다. [ch_boy]은 설마 어머니에게서 [ch_babyTrader]이라는 말을 들을 줄은 몰랐다."

    ch_mother "시끄러워! 될성 싶은 나무는 떡잎부터 알아본다 했어! 너는 이미 싹수가 노랗구나!"

    ch_narrator "어머니는 [ch_boy]의 손을 강제로 잡고 문 밖을 나섰다. 그는 저항하려 했으나 어린 아이의 힘으로는 어쩔 도리가 없었다. 마치 바닥에 끌리는 자루처럼 어머니에게 이끌려갔다."

    stop music fadeout 1.0
    jump common_2