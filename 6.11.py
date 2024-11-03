


cities={'HeFei':{'country':'China',
                 'population':985.3,
                 'fact':'境内有巢湖'},
        'New York':{'country':'USA',
                    'population':834,
                    'fact':'The economic center of USA'},
        'Tokyo':{'country':'Japan',
                 'population':1410,
                 'fact':'世界の2次元の中心です'}
        }

if __name__=='__main__':
    for city,content in cities.items():
        print(city)
        for _ in content.items():
            print(f'{_[0]}->{_[1]}')
