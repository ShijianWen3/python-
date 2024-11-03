


try:
    with open('10.8_cats.txt') as file:
        contents=file.readlines()
        print('cats\' names:')
        for _ in contents:
            print(_.strip())
    with open('10.8_dogs.txt') as file:
        contents=file.readlines()
        print('dogs\' names:')
        for _ in contents:
            print(_.strip())
except FileNotFoundError:
    print('FileNotFoundError:有文件无法找到')