


def make_car(manufacturer:str,style:str,**info):
    if info is None:
        return {'manufacturer':manufacturer,'style':style}
    else:
        temp={'manufacturer':manufacturer,'style':style}
        for key,value in info.items():
            temp[key]=value
        return temp
    
if  __name__=='__main__':
    car_info=make_car('subaru','outback',color='blue',tow_package=True)
    for _ in car_info.items():
        print(f'{_[0]}->{_[1]}')
    print(car_info)