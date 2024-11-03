# from collections import OrderedDict as Dict


# dic = Dict()
# dic['import']='导入模块'
# dic['for']='可用于遍历'
# dic['while']='用于循环'
# dic['break']='跳出循环'
# for key,value in dic.items():
#     print(f'{key}->{value}')

import random

class Die:
    def __init__(self,sides:int=6) -> None:
        self.sides=sides

    def roll_die(self):
        num=random.randint(1,self.sides)
        print(num)

if __name__=='__main__':
    die_6=Die()
    die_10=Die(10)
    die_20=Die(20)
    for _ in range(10):
        die_6.roll_die()
    for _ in range(10):
        die_10.roll_die()
    print('-'*10)
    for _ in range(10):
        die_20.roll_die()