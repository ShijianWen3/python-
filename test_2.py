#对9.13的测试函数
"""来自9.13的函数"""

import random

class Die:
    def __init__(self,sides:int=6) -> None:
        self.sides=sides
        self.current_num=None

    def roll_die(self):
        num=random.randint(1,self.sides)
        self.current_num=num
        print(num)
        return num

def test_Die():
    die=Die(10)
    num=die.roll_die()
    assert num == die.current_num