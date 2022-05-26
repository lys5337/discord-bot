import numpy as np

class redcube:
    wapon_result = []
    emblem_result = []
    sub_wapon_result = []
    force_and_soul_result = []
    shield_result = []
    cap_result = []
    top_result = []
    onepiece_result = []
    bottom_result = []
    shoes_result = []
    gloves_result = []
    cloak_result = []
    belt_result = []
    shoulder_result = []
    face_result = []
    eyes_result = []
    earring_result = []
    ring_result = []
    necklace_result = []
    heart_result = []

    #무기_레드 
    wapon_1 = [
        'STR:+12%','DEX:+12%','INT:+12%','LUK:+12%',
        '공격력:+12%','마력+12%',
        '크확:+12%','데미지:+12%','올스탯:+9%',
        '렙당 공격력:+1','렙당 마력:+1',
        '방무:+35%','방무:+40%',
        '보공:+30%','보공:+35%','보공:+40%'
    ]
    wapon_2 = [
        'STR : +9%','DEX : +9%','INT : +9%','LUK : +9%',
        '공격력 : +9%','마력 : +9%',
        '크확 : +9%','데미지 : +9%','올스탯 : +6%',
        '방무 : +30%','보공 : +30%',
        'STR : +12%','DEX : +12%','INT : +12%','LUK : +12%',
        '공격력 : +12%','마력 : +12%',
        '크확 : +12%','데미지 : +12%','올스탯 : +9%',
        '렙당 공격력 : +1','렙당 마력 : +1',
        '방무 : +35%','방무 : +40%',
        '보공 : +30%','보공 : +35%','보공 : +40%'
    ]
    wapon_3 = [
        'STR : +9%','DEX : +9%','INT : +9%','LUK : +9%',
        '공격력 : +9%','마력 : +9%',
        '크확 : +9%','데미지 : +9%','올스탯 : +6%',
        '방무 : +30%','보공 : +30%',
        'STR : +12%','DEX : +12%','INT : +12%','LUK : +12%',
        '공격력 : +12%','마력 : +12%',
        '크확 : +12%','데미지 : +12%','올스탯 : +9%',
        '렙당 공격력 : +1','렙당 마력 : +1',
        '방무 : +35%','방무 : +40%',
        '보공 : +30%','보공 : +35%','보공 : +40%'
    ]
    #엠블렘_레드 
    emblem_1 = [
        'STR : +12%','DEX : +12%','INT : +12%','LUK : +12%',
        '공격력 : +12%','마력 : +12%',
        '크리티컬 확률 : +12%','데미지 : +12%','올스탯 : +9%',
        '캐릭터 기준 10레벨 당 공격력 : +1','캐릭터 기준 10레벨 당 마력 : +1',
        '몬스터 방어율 무시 : +35%','몬스터 방어율 무시 : +40%'
    ]
    emblem_2 = [
        'STR : +9%','DEX : +9%','INT : +9%','LUK : +9%',
        '공격력 : +9%','마력 : +9%',
        '크리티컬 확률 : +9%','데미지 : +9%','올스탯 : +6%',
        '몬스터 방어율 무시 : +30%',
        'STR : +12%','DEX : +12%','INT : +12%','LUK : +12%',
        '공격력 : +12%','마력 : +12%',
        '크리티컬 확률 : +12%','데미지 : +12%','올스탯 : +9%',
        '캐릭터 기준 10레벨 당 공격력 : +1','캐릭터 기준 10레벨 당 마력 : +1',
        '몬스터 방어율 무시 : +35%','몬스터 방어율 무시 : +40%'
    ]
    emblem_3 = [
        'STR : +9%','DEX : +9%','INT : +9%','LUK : +9%',
        '공격력 : +9%','마력 : +9%',
        '크리티컬 확률 : +9%','데미지 : +9%','올스탯 : +6%',
        '몬스터 방어율 무시 : +30%',
        'STR : +12%','DEX : +12%','INT : +12%','LUK : +12%',
        '공격력 : +12%','마력 : +12%',
        '크리티컬 확률 : +12%','데미지 : +12%','올스탯 : +9%',
        '캐릭터 기준 10레벨 당 공격력 : +1','캐릭터 기준 10레벨 당 마력 : +1',
        '몬스터 방어율 무시 : +35%','몬스터 방어율 무시 : +40%'
    ]
    #보조무기_레드 
    sub_wapon_1 = []
    sub_wapon_2 = []
    sub_wapon_3 = []
    #포스실드_소울링_레드 
    force_and_soul_1 = []
    force_and_soul_2 = []
    force_and_soul_3 = []
    #방패_레드 
    shield_1 = []
    shield_2 = []
    shield_3 = []
    #모자_레드 
    cap_1 = []
    cap_2 = []
    cap_3 = []
    #상의_레드 
    top_1 = []
    top_2 = []
    top_3 = []
    #한벌옷_레드 
    onepiece_1 = []
    onepiece_2 = []
    onepiece_3 = []
    #하의_레드 
    bottom_1 = []
    bottom_2 = []
    bottom_3 = []
    #신발_레드 
    shoes_1 = []
    shoes_2 = []
    shoes_3 = []
    #장갑_레드 
    gloves_1 = []
    gloves_2 = []
    gloves_3 = []
    #망토_레드 
    cloak_1 = []
    cloak_2 = []
    cloak_3 = []
    #벨트_레드 
    belt_1 = []
    belt_2 = []
    belt_3 = []
    #어깨_레드 
    shoulder_1 = []
    shoulder_2 = []
    shoulder_3 = []
    #얼굴장식_레드 
    face_1 = []
    face_2 = []
    face_3 = []
    #눈장식_레드 
    eyes_1 = []
    eyes_2 = []
    eyes_3 = []
    #귀고리_레드 
    earring_1 = []
    earring_2 = []
    earring_3 = []
    #반지_레드 
    ring_1 = []
    ring_2 = []
    ring_3 = []
    #목걸이_레드 
    necklace_1 = []
    necklace_2 = []
    necklace_3 = []
    #기계심장_레드 
    heart_1 = []
    heart_2 = []
    heart_3 = []

    def wapon (a, b):
        if a == b:
            return
        else: 
            wapon_op_1 = np.random.choice(redcube.wapon_1, 1, p = 
            [0.097562,0.097562,0.097562,0.097562,0.048780,0.048780,0.048780,0.048780,0.073172,0.048780,0.048780,0.048780,0.048780,0.048780,0.048780,0.048780])
            wapon_op_2 = np.random.choice(redcube.wapon_2, 1, p = 
            [0.104651,0.104651,0.104651,0.104651,0.062791,0.062791,0.083721,0.062791,0.083721,0.062791,0.062791,
            0.009756,0.009756,0.009756,0.009756,0.004878,0.004878,0.004878,0.004878,0.007317,0.004878,0.004878,0.004878,0.004878,0.004878,0.004878,0.004878])
            wapon_op_3 = np.random.choice(redcube.wapon_3, 1, p = 
            [0.115116,0.115116,0.115116,0.115116,0.069070,0.069070,0.092093,0.069070,0.092093,0.069070,0.069070,
            0.000975,0.000975,0.000975,0.000975,0.000488,0.000488,0.000488,0.000488,0.000732,0.000488,0.000488,0.000488,0.000488,0.000488,0.000488,0.000488])
            
            redcube.wapon_result.append(str(wapon_op_1) + ' ' + str(wapon_op_2) + ' ' + str(wapon_op_3))
        redcube.wapon (a+1, b)

    def emblem (a, b):
        if a == b:
            emblem_op_1 = np.random.choice(redcube.emblem_1, 1, p = 
            [0.114286,0.114286,0.114286,0.114286,0.057143,0.057143,0.057143,0.057143,0.085714,0.057143,0.057143,0.057143,0.057143])
            emblem_op_2 = np.random.choice(redcube.emblem_2, 1, p = 
            [0.112500,0.112500,0.112500,0.112500,0.067500,0.067500,0.090000,0.067500,0.090000,0.067501,0.011429,0.011429,0.011429,0.011429,
            0.005714,0.005714,0.005714,0.005714,0.008571,0.005714,0.005714,0.005714,0.005714])
            emblem_op_3 = np.random.choice(redcube.emblem_3, 1, p = [])
            return
        redcube.emblem (a+1, b)

    def sub_wapon (a, b):
        if a == b:
            sub_wapon_op_1 = np.random.choice(redcube.sub_wapon_1, 1, p = [])
            sub_wapon_op_2 = np.random.choice(redcube.sub_wapon_2, 1, p = [])
            sub_wapon_op_3 = np.random.choice(redcube.sub_wapon_3, 1, p = [])

            return
        redcube.sub_wapon (a+1, b)

    def force_and_soul (a, b):
        if a == b:
            force_and_soul_op_1 = np.random.choice(redcube.force_and_soul_1, 1, p = [])
            force_and_soul_op_2 = np.random.choice(redcube.force_and_soul_2, 1, p = [])
            force_and_soul_op_3 = np.random.choice(redcube.force_and_soul_3, 1, p = [])
            return
        redcube.force_and_soul (a+1, b)

    def shield (a, b):
        if a == b:
            shield_op_1 = np.random.choice(redcube.shield_1, 1, p = [])
            shield_op_2 = np.random.choice(redcube.shield_2, 1, p = [])
            shield_op_3 = np.random.choice(redcube.shield_3, 1, p = [])
            return
        redcube.shield (a+1, b)

    def cap (a, b):
        if a == b:
            cap_op_1 = np.random.choice(redcube.cap_1, 1, p = [])
            cap_op_2 = np.random.choice(redcube.cap_2, 1, p = [])
            cap_op_3 = np.random.choice(redcube.cap_3, 1, p = [])
            return
        redcube.cap (a+1, b)

    def top (a, b):
        if a == b:
            top_op_1 = np.random.choice(redcube.top_1, 1, p = [])
            top_op_2 = np.random.choice(redcube.top_2, 1, p = [])
            top_op_3 = np.random.choice(redcube.top_3, 1, p = [])
            return
        redcube.top (a+1, b)

    def onepiece (a, b):
        if a == b:
            onepiece_op_1 = np.random.choice(redcube.onepiece_1, 1, p = [])
            onepiece_op_2 = np.random.choice(redcube.onepiece_2, 1, p = [])
            onepiece_op_3 = np.random.choice(redcube.onepiece_3, 1, p = [])
            return
        redcube.onepiece (a+1, b)

    def bottom (a, b):
        if a == b:
            bottom_op_1 = np.random.choice(redcube.bottom_1, 1, p = [])
            bottom_op_2 = np.random.choice(redcube.bottom_2, 1, p = [])
            bottom_op_3 = np.random.choice(redcube.bottom_3, 1, p = [])
            return
        redcube.bottom (a+1, b)

    def shoes (a, b):
        if a == b:
            shoes_op_1 = np.random.choice(redcube.shoes_1, 1, p = [])
            shoes_op_2 = np.random.choice(redcube.shoes_2, 1, p = [])
            shoes_op_3 = np.random.choice(redcube.shoes_3, 1, p = [])
            return
        redcube.shoes (a+1, b)

    def gloves (a, b):
        if a == b:
            gloves_op_1 = np.random.choice(redcube.gloves_1, 1, p = [])
            gloves_op_2 = np.random.choice(redcube.gloves_2, 1, p = [])
            gloves_op_3 = np.random.choice(redcube.gloves_3, 1, p = [])
            return
        redcube.gloves (a+1, b)

    def cloak (a, b):
        if a == b:
            cloak_op_1 = np.random.choice(redcube.cloak_1, 1, p = [])
            cloak_op_2 = np.random.choice(redcube.cloak_2, 1, p = [])
            cloak_op_3 = np.random.choice(redcube.cloak_3, 1, p = [])
            return
        redcube.cloak (a+1, b)

    def belt (a, b):
        if a == b:
            belt_op_1 = np.random.choice(redcube.belt_1, 1, p = [])
            belt_op_2 = np.random.choice(redcube.belt_2, 1, p = [])
            belt_op_3 = np.random.choice(redcube.belt_3, 1, p = [])
            return
        redcube.belt (a+1, b)

    def shoulder (a, b):
        if a == b:
            shoulder_op_1 = np.random.choice(redcube.shoulder_1, 1, p = [])
            shoulder_op_2 = np.random.choice(redcube.shoulder_2, 1, p = [])
            shoulder_op_3 = np.random.choice(redcube.shoulder_3, 1, p = [])
            return
        redcube.shoulder (a+1, b)

    def face (a, b):
        if a == b:
            face_op_1 = np.random.choice(redcube.face_1, 1, p = [])
            face_op_2 = np.random.choice(redcube.face_2, 1, p = [])
            face_op_3 = np.random.choice(redcube.face_3, 1, p = [])
            return
        redcube.face (a+1, b)

    def eyes (a, b):
        if a == b:
            eyes_op_1 = np.random.choice(redcube.eyes_1, 1, p = [])
            eyes_op_2 = np.random.choice(redcube.eyes_2, 1, p = [])
            eyes_op_3 = np.random.choice(redcube.eyes_3, 1, p = [])
            return
        redcube.eyes (a+1, b)

    def earring (a, b):
        if a == b:
            earring_op_1 = np.random.choice(redcube.earring_1, 1, p = [])
            earring_op_2 = np.random.choice(redcube.earring_2, 1, p = [])
            earring_op_3 = np.random.choice(redcube.earring_3, 1, p = [])
            return
        redcube.earring (a+1, b)

    def ring (a, b):
        if a == b:
            ring_op_1 = np.random.choice(redcube.ring_1, 1, p = [])
            ring_op_1 = np.random.choice(redcube.ring_2, 1, p = [])
            ring_op_1 = np.random.choice(redcube.ring_3, 1, p = [])
            return
        redcube.ring (a+1, b)

    def necklace (a, b):
        if a == b:
            necklace_op_1 = np.random.choice(redcube.necklace_1, 1, p = [])
            necklace_op_2 = np.random.choice(redcube.necklace_2, 1, p = [])
            necklace_op_3 = np.random.choice(redcube.necklace_3, 1, p = [])
            return
        redcube.necklace (a+1, b)

    def heart (a, b):
        if a == b:
            heart_op_1 = np.random.choice(redcube.heart_1, 1, p = [])
            heart_op_2 = np.random.choice(redcube.heart_2, 1, p = [])
            heart_op_3 = np.random.choice(redcube.heart_3, 1, p = [])
            return
        redcube.heart (a+1, b)

class blackcube:
    wapon_result = []
    emblem_result = []
    sub_wapon_result = []
    force_and_soul_result = []
    shield_result = []
    cap_result = []
    top_result = []
    onepiece_result = []
    bottom_result = []
    shoes_result = []
    gloves_result = []
    cloak_result = []
    belt_result = []
    shoulder_result = []
    face_result = []
    eyes_result = []
    earring_result = []
    ring_result = []
    necklace_result = []
    heart_result = []

    wapon_1 = []
    wapon_2 = []
    wapon_3 = []
    emblem_1 = []
    emblem_2 = []
    emblem_3 = []
    sub_wapon_1 = []
    sub_wapon_2 = []
    sub_wapon_3 = []
    force_and_soul_1 = []
    force_and_soul_2 = []
    force_and_soul_3 = []
    shield_1 = []
    shield_2 = []
    shield_3 = []
    cap_1 = []
    cap_2 = []
    cap_3 = []
    top_1 = []
    top_2 = []
    top_3 = []
    onepiece_1 = []
    onepiece_2 = []
    onepiece_3 = []
    bottom_1 = []
    bottom_2 = []
    bottom_3 = []
    shoes_1 = []
    shoes_2 = []
    shoes_3 = []
    gloves_1 = []
    gloves_2 = []
    gloves_3 = []
    cloak_1 = []
    cloak_2 = []
    cloak_3 = []
    belt_1 = []
    belt_2 = []
    belt_3 = []
    shoulder_1 = []
    shoulder_2 = []
    shoulder_3 = []
    face_1 = []
    face_2 = []
    face_3 = []
    eyes_1 = []
    eyes_2 = []
    eyes_3 = []
    earring_1 = []
    earring_2 = []
    earring_3 = []
    ring_1 = []
    ring_2 = []
    ring_3 = []
    necklace_1 = []
    necklace_2 = []
    necklace_3 = []
    heart_1 = []
    heart_2 = []
    heart_3 = []


    def wapon (a, b):
        if a == b:
            return
        else: 
            wapon_op_1 = np.random.choice(blackcube.wapon_1, 1, p = [])
            wapon_op_2 = np.random.choice(blackcube.wapon_2, 1, p = [])
            wapon_op_3 = np.random.choice(blackcube.wapon_3, 1, p = [])
            
            blackcube.wapon_result.append(str(wapon_op_1) + ' ' + str(wapon_op_2) + ' ' + str(wapon_op_3))
        blackcube.wapon (a+1, b)

    def emblem (a, b):
        if a == b:
            emblem_op_1 = np.random.choice(blackcube.emblem_1, 1, p = [])
            emblem_op_2 = np.random.choice(blackcube.emblem_2, 1, p = [])
            emblem_op_3 = np.random.choice(blackcube.emblem_3, 1, p = [])
            return
        blackcube.emblem (a+1, b)

    def sub_wapon (a, b):
        if a == b:
            sub_wapon_op_1 = np.random.choice(blackcube.sub_wapon_1, 1, p = [])
            sub_wapon_op_2 = np.random.choice(blackcube.sub_wapon_2, 1, p = [])
            sub_wapon_op_3 = np.random.choice(blackcube.sub_wapon_3, 1, p = [])

            return
        blackcube.sub_wapon (a+1, b)

    def force_and_soul (a, b):
        if a == b:
            force_and_soul_op_1 = np.random.choice(blackcube.force_and_soul_1, 1, p = [])
            force_and_soul_op_2 = np.random.choice(blackcube.force_and_soul_2, 1, p = [])
            force_and_soul_op_3 = np.random.choice(blackcube.force_and_soul_3, 1, p = [])
            return
        blackcube.force_and_soul (a+1, b)

    def shield (a, b):
        if a == b:
            shield_op_1 = np.random.choice(blackcube.shield_1, 1, p = [])
            shield_op_2 = np.random.choice(blackcube.shield_2, 1, p = [])
            shield_op_3 = np.random.choice(blackcube.shield_3, 1, p = [])
            return
        blackcube.shield (a+1, b)

    def cap (a, b):
        if a == b:
            cap_op_1 = np.random.choice(blackcube.cap_1, 1, p = [])
            cap_op_2 = np.random.choice(blackcube.cap_2, 1, p = [])
            cap_op_3 = np.random.choice(blackcube.cap_3, 1, p = [])
            return
        blackcube.cap (a+1, b)

    def top (a, b):
        if a == b:
            top_op_1 = np.random.choice(blackcube.top_1, 1, p = [])
            top_op_2 = np.random.choice(blackcube.top_2, 1, p = [])
            top_op_3 = np.random.choice(blackcube.top_3, 1, p = [])
            return
        blackcube.top (a+1, b)

    def onepiece (a, b):
        if a == b:
            onepiece_op_1 = np.random.choice(blackcube.onepiece_1, 1, p = [])
            onepiece_op_2 = np.random.choice(blackcube.onepiece_2, 1, p = [])
            onepiece_op_3 = np.random.choice(blackcube.onepiece_3, 1, p = [])
            return
        blackcube.onepiece (a+1, b)

    def bottom (a, b):
        if a == b:
            bottom_op_1 = np.random.choice(blackcube.bottom_1, 1, p = [])
            bottom_op_2 = np.random.choice(blackcube.bottom_2, 1, p = [])
            bottom_op_3 = np.random.choice(blackcube.bottom_3, 1, p = [])
            return
        blackcube.bottom (a+1, b)

    def shoes (a, b):
        if a == b:
            shoes_op_1 = np.random.choice(blackcube.shoes_1, 1, p = [])
            shoes_op_2 = np.random.choice(blackcube.shoes_2, 1, p = [])
            shoes_op_3 = np.random.choice(blackcube.shoes_3, 1, p = [])
            return
        blackcube.shoes (a+1, b)

    def gloves (a, b):
        if a == b:
            gloves_op_1 = np.random.choice(blackcube.gloves_1, 1, p = [])
            gloves_op_2 = np.random.choice(blackcube.gloves_2, 1, p = [])
            gloves_op_3 = np.random.choice(blackcube.gloves_3, 1, p = [])
            return
        blackcube.gloves (a+1, b)

    def cloak (a, b):
        if a == b:
            cloak_op_1 = np.random.choice(blackcube.cloak_1, 1, p = [])
            cloak_op_2 = np.random.choice(blackcube.cloak_2, 1, p = [])
            cloak_op_3 = np.random.choice(blackcube.cloak_3, 1, p = [])
            return
        blackcube.cloak (a+1, b)

    def belt (a, b):
        if a == b:
            belt_op_1 = np.random.choice(blackcube.belt_1, 1, p = [])
            belt_op_2 = np.random.choice(blackcube.belt_2, 1, p = [])
            belt_op_3 = np.random.choice(blackcube.belt_3, 1, p = [])
            return
        blackcube.belt (a+1, b)

    def shoulder (a, b):
        if a == b:
            shoulder_op_1 = np.random.choice(blackcube.shoulder_1, 1, p = [])
            shoulder_op_2 = np.random.choice(blackcube.shoulder_2, 1, p = [])
            shoulder_op_3 = np.random.choice(blackcube.shoulder_3, 1, p = [])
            return
        blackcube.shoulder (a+1, b)

    def face (a, b):
        if a == b:
            face_op_1 = np.random.choice(blackcube.face_1, 1, p = [])
            face_op_2 = np.random.choice(blackcube.face_2, 1, p = [])
            face_op_3 = np.random.choice(blackcube.face_3, 1, p = [])
            return
        blackcube.face (a+1, b)

    def eyes (a, b):
        if a == b:
            eyes_op_1 = np.random.choice(blackcube.eyes_1, 1, p = [])
            eyes_op_2 = np.random.choice(blackcube.eyes_2, 1, p = [])
            eyes_op_3 = np.random.choice(blackcube.eyes_3, 1, p = [])
            return
        blackcube.eyes (a+1, b)

    def earring (a, b):
        if a == b:
            earring_op_1 = np.random.choice(blackcube.earring_1, 1, p = [])
            earring_op_2 = np.random.choice(blackcube.earring_2, 1, p = [])
            earring_op_3 = np.random.choice(blackcube.earring_3, 1, p = [])
            return
        blackcube.earring (a+1, b)

    def ring (a, b):
        if a == b:
            ring_op_1 = np.random.choice(blackcube.ring_1, 1, p = [])
            ring_op_1 = np.random.choice(blackcube.ring_2, 1, p = [])
            ring_op_1 = np.random.choice(blackcube.ring_3, 1, p = [])
            return
        blackcube.ring (a+1, b)

    def necklace (a, b):
        if a == b:
            necklace_op_1 = np.random.choice(blackcube.necklace_1, 1, p = [])
            necklace_op_2 = np.random.choice(blackcube.necklace_2, 1, p = [])
            necklace_op_3 = np.random.choice(blackcube.necklace_3, 1, p = [])
            return
        blackcube.necklace (a+1, b)

    def heart (a, b):
        if a == b:
            heart_op_1 = np.random.choice(blackcube.heart_1, 1, p = [])
            heart_op_2 = np.random.choice(blackcube.heart_2, 1, p = [])
            heart_op_3 = np.random.choice(blackcube.heart_3, 1, p = [])
            return
        blackcube.heart (a+1, b)

class additional:
    wapon_result = []
    emblem_result = []
    sub_wapon_result = []
    force_and_soul_result = []
    shield_result = []
    cap_result = []
    top_result = []
    onepiece_result = []
    bottom_result = []
    shoes_result = []
    gloves_result = []
    cloak_result = []
    belt_result = []
    shoulder_result = []
    face_result = []
    eyes_result = []
    earring_result = []
    ring_result = []
    necklace_result = []
    heart_result = []

    wapon_1 = []
    wapon_2 = []
    wapon_3 = []
    emblem_1 = []
    emblem_2 = []
    emblem_3 = []
    sub_wapon_1 = []
    sub_wapon_2 = []
    sub_wapon_3 = []
    force_and_soul_1 = []
    force_and_soul_2 = []
    force_and_soul_3 = []
    shield_1 = []
    shield_2 = []
    shield_3 = []
    cap_1 = []
    cap_2 = []
    cap_3 = []
    top_1 = []
    top_2 = []
    top_3 = []
    onepiece_1 = []
    onepiece_2 = []
    onepiece_3 = []
    bottom_1 = []
    bottom_2 = []
    bottom_3 = []
    shoes_1 = []
    shoes_2 = []
    shoes_3 = []
    gloves_1 = []
    gloves_2 = []
    gloves_3 = []
    cloak_1 = []
    cloak_2 = []
    cloak_3 = []
    belt_1 = []
    belt_2 = []
    belt_3 = []
    shoulder_1 = []
    shoulder_2 = []
    shoulder_3 = []
    face_1 = []
    face_2 = []
    face_3 = []
    eyes_1 = []
    eyes_2 = []
    eyes_3 = []
    earring_1 = []
    earring_2 = []
    earring_3 = []
    ring_1 = []
    ring_2 = []
    ring_3 = []
    necklace_1 = []
    necklace_2 = []
    necklace_3 = []
    heart_1 = []
    heart_2 = []
    heart_3 = []


    def wapon (a, b):
        if a == b:
            return
        else: 
            wapon_op_1 = np.random.choice(additional.wapon_1, 1, p = [])
            wapon_op_2 = np.random.choice(additional.wapon_2, 1, p = [])
            wapon_op_3 = np.random.choice(additional.wapon_3, 1, p = [])
            
            additional.wapon_result.append(str(wapon_op_1) + ' ' + str(wapon_op_2) + ' ' + str(wapon_op_3))
        additional.wapon (a+1, b)

    def emblem (a, b):
        if a == b:
            emblem_op_1 = np.random.choice(additional.emblem_1, 1, p = [])
            emblem_op_2 = np.random.choice(additional.emblem_2, 1, p = [])
            emblem_op_3 = np.random.choice(additional.emblem_3, 1, p = [])
            return
        additional.emblem (a+1, b)

    def sub_wapon (a, b):
        if a == b:
            sub_wapon_op_1 = np.random.choice(additional.sub_wapon_1, 1, p = [])
            sub_wapon_op_2 = np.random.choice(additional.sub_wapon_2, 1, p = [])
            sub_wapon_op_3 = np.random.choice(additional.sub_wapon_3, 1, p = [])

            return
        additional.sub_wapon (a+1, b)

    def force_and_soul (a, b):
        if a == b:
            force_and_soul_op_1 = np.random.choice(additional.force_and_soul_1, 1, p = [])
            force_and_soul_op_2 = np.random.choice(additional.force_and_soul_2, 1, p = [])
            force_and_soul_op_3 = np.random.choice(additional.force_and_soul_3, 1, p = [])
            return
        additional.force_and_soul (a+1, b)

    def shield (a, b):
        if a == b:
            shield_op_1 = np.random.choice(additional.shield_1, 1, p = [])
            shield_op_2 = np.random.choice(additional.shield_2, 1, p = [])
            shield_op_3 = np.random.choice(additional.shield_3, 1, p = [])
            return
        additional.shield (a+1, b)

    def cap (a, b):
        if a == b:
            cap_op_1 = np.random.choice(additional.cap_1, 1, p = [])
            cap_op_2 = np.random.choice(additional.cap_2, 1, p = [])
            cap_op_3 = np.random.choice(additional.cap_3, 1, p = [])
            return
        additional.cap (a+1, b)

    def top (a, b):
        if a == b:
            top_op_1 = np.random.choice(additional.top_1, 1, p = [])
            top_op_2 = np.random.choice(additional.top_2, 1, p = [])
            top_op_3 = np.random.choice(additional.top_3, 1, p = [])
            return
        additional.top (a+1, b)

    def onepiece (a, b):
        if a == b:
            onepiece_op_1 = np.random.choice(additional.onepiece_1, 1, p = [])
            onepiece_op_2 = np.random.choice(additional.onepiece_2, 1, p = [])
            onepiece_op_3 = np.random.choice(additional.onepiece_3, 1, p = [])
            return
        additional.onepiece (a+1, b)

    def bottom (a, b):
        if a == b:
            bottom_op_1 = np.random.choice(additional.bottom_1, 1, p = [])
            bottom_op_2 = np.random.choice(additional.bottom_2, 1, p = [])
            bottom_op_3 = np.random.choice(additional.bottom_3, 1, p = [])
            return
        additional.bottom (a+1, b)

    def shoes (a, b):
        if a == b:
            shoes_op_1 = np.random.choice(additional.shoes_1, 1, p = [])
            shoes_op_2 = np.random.choice(additional.shoes_2, 1, p = [])
            shoes_op_3 = np.random.choice(additional.shoes_3, 1, p = [])
            return
        additional.shoes (a+1, b)

    def gloves (a, b):
        if a == b:
            gloves_op_1 = np.random.choice(additional.gloves_1, 1, p = [])
            gloves_op_2 = np.random.choice(additional.gloves_2, 1, p = [])
            gloves_op_3 = np.random.choice(additional.gloves_3, 1, p = [])
            return
        additional.gloves (a+1, b)

    def cloak (a, b):
        if a == b:
            cloak_op_1 = np.random.choice(additional.cloak_1, 1, p = [])
            cloak_op_2 = np.random.choice(additional.cloak_2, 1, p = [])
            cloak_op_3 = np.random.choice(additional.cloak_3, 1, p = [])
            return
        additional.cloak (a+1, b)

    def belt (a, b):
        if a == b:
            belt_op_1 = np.random.choice(additional.belt_1, 1, p = [])
            belt_op_2 = np.random.choice(additional.belt_2, 1, p = [])
            belt_op_3 = np.random.choice(additional.belt_3, 1, p = [])
            return
        additional.belt (a+1, b)

    def shoulder (a, b):
        if a == b:
            shoulder_op_1 = np.random.choice(additional.shoulder_1, 1, p = [])
            shoulder_op_2 = np.random.choice(additional.shoulder_2, 1, p = [])
            shoulder_op_3 = np.random.choice(additional.shoulder_3, 1, p = [])
            return
        additional.shoulder (a+1, b)

    def face (a, b):
        if a == b:
            face_op_1 = np.random.choice(additional.face_1, 1, p = [])
            face_op_2 = np.random.choice(additional.face_2, 1, p = [])
            face_op_3 = np.random.choice(additional.face_3, 1, p = [])
            return
        additional.face (a+1, b)

    def eyes (a, b):
        if a == b:
            eyes_op_1 = np.random.choice(additional.eyes_1, 1, p = [])
            eyes_op_2 = np.random.choice(additional.eyes_2, 1, p = [])
            eyes_op_3 = np.random.choice(additional.eyes_3, 1, p = [])
            return
        additional.eyes (a+1, b)

    def earring (a, b):
        if a == b:
            earring_op_1 = np.random.choice(additional.earring_1, 1, p = [])
            earring_op_2 = np.random.choice(additional.earring_2, 1, p = [])
            earring_op_3 = np.random.choice(additional.earring_3, 1, p = [])
            return
        additional.earring (a+1, b)

    def ring (a, b):
        if a == b:
            ring_op_1 = np.random.choice(additional.ring_1, 1, p = [])
            ring_op_1 = np.random.choice(additional.ring_2, 1, p = [])
            ring_op_1 = np.random.choice(additional.ring_3, 1, p = [])
            return
        additional.ring (a+1, b)

    def necklace (a, b):
        if a == b:
            necklace_op_1 = np.random.choice(additional.necklace_1, 1, p = [])
            necklace_op_2 = np.random.choice(additional.necklace_2, 1, p = [])
            necklace_op_3 = np.random.choice(additional.necklace_3, 1, p = [])
            return
        additional.necklace (a+1, b)

    def heart (a, b):
        if a == b:
            heart_op_1 = np.random.choice(additional.heart_1, 1, p = [])
            heart_op_2 = np.random.choice(additional.heart_2, 1, p = [])
            heart_op_3 = np.random.choice(additional.heart_3, 1, p = [])
            return
        additional.heart (a+1, b)