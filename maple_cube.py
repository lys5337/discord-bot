import numpy as np
wapon_1 = [
    'STR:+12%','DEX:+12%','INT:+12%','LUK:+12%',
    '공격력:+12%','마력+12%',
    '크리티컬 확률:+12%','데미지:+12%','올스탯:+9%',
    '캐릭터 기준 10레벨 당 공격력:+1','캐릭터 기준 10레벨 당 마력:+1',
    '몬스터 방어력 무시:+35%','몬스터 방어력 무시:+40%',
    '보스 몬스터 공격 시 데미지:+30%','보스 몬스터 공격 시 데미지:+35%','보스 몬스터 공격 시 데미지:+40%'
]
wapon_2 = [
    'STR : +9%','DEX : +9%','INT : +9%','LUK : +9%',
    '공격력 : +9%','마력 : +9%',
    '크리티컬 확률 : +9%','데미지 : +9%','올스탯 : +6%',
    '몬스터 방어율 무시 : +30%','보스 몬스터 공격 시 데미지 : +30%',
    'STR : +12%','DEX : +12%','INT : +12%','LUK : +12%',
    '공격력 : +12%','마력 : +12%',
    '크리티컬 확률 : +12%','데미지 : +12%','올스탯 : +9%',
    '캐릭터 기준 10레벨 당 공격력 : +1','캐릭터 기준 10레벨 당 마력 : +1',
    '몬스터 방어율 무시 : +35%','몬스터 방어율 무시 : +40%',
    '보스 몬스터 공격 시 데미지 : +30%','보스 몬스터 공격 시 데미지 : +35%','보스 몬스터 공격 시 데미지 : +40%'
]
wapon_3 = [
    'STR : +9%','DEX : +9%','INT : +9%','LUK : +9%',
    '공격력 : +9%','마력 : +9%',
    '크리티컬 확률 : +9%','데미지 : +9%','올스탯 : +6%',
    '몬스터 방어율 무시 : +30%','보스 몬스터 공격 시 데미지 : +30%',
    'STR : +12%','DEX : +12%','INT : +12%','LUK : +12%',
    '공격력 : +12%','마력 : +12%',
    '크리티컬 확률 : +12%','데미지 : +12%','올스탯 : +9%',
    '캐릭터 기준 10레벨 당 공격력 : +1','캐릭터 기준 10레벨 당 마력 : +1',
    '몬스터 방어율 무시 : +35%','몬스터 방어율 무시 : +40%',
    '보스 몬스터 공격 시 데미지 : +30%','보스 몬스터 공격 시 데미지 : +35%','보스 몬스터 공격 시 데미지 : +40%'
]

wapon_op_1 = np.random.choice(wapon_1, 1, p = 
[0.097562,0.097562,0.097562,0.097562,0.048780,0.048780,0.048780,0.048780,0.073172,0.048780,0.048780,0.048780,0.048780,0.048780,0.048780,0.048780])
wapon_op_2 = np.random.choice(wapon_2, 1, p = 
[0.104651,0.104651,0.104651,0.104651,0.062791,0.062791,0.083721,0.062791,0.083721,0.062791,0.062791,
0.009756,0.009756,0.009756,0.009756,0.004878,0.004878,0.004878,0.004878,0.007317,0.004878,0.004878,0.004878,0.004878,0.004878,0.004878,0.004878])
wapon_op_3 = np.random.choice(wapon_2, 1, p = 
[0.115116,0.115116,0.115116,0.115116,0.069070,0.069070,0.092093,0.069070,0.092093,0.069070,0.069070,
0.000975,0.000975,0.000975,0.000975,0.000488,0.000488,0.000488,0.000488,0.000732,0.000488,0.000488,0.000488,0.000488,0.000488,0.000488,0.000488])