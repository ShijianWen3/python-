


def make_album(singer_name:str,album_name:str,songs_num:int=None):
    if songs_num is None:
        return {'singer':singer_name,'album':album_name}
    else:
        return {'singer':singer_name,'album':album_name,'number':songs_num}


if __name__=="__main__":
    album_1=make_album('wen','World')
    album_2=make_album('shi','Hello')
    album_3=make_album('jian','Change',3)
    print(album_1)
    print(album_2)
    print(album_3)
    