#对8.14的测试函数
"""来自8.14的函数"""
def make_car(manufacturer:str,style:str,**info):
    if info is None:
        return {'manufacturer':manufacturer,'style':style}
    else:
        temp={'manufacturer':manufacturer,'style':style}
        for key,value in info.items():
            temp[key]=value
        return temp
    
def test_make_car():
    feedback=make_car('subaru','outback',color='blue',tow_package=True)
    assert feedback=={'manufacturer': 'subaru',
                       'style': 'outback',
                         'color': 'blue', 
                         'tow_package': True}
