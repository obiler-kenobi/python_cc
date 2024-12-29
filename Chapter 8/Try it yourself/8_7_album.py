def make_album(artist_name, album_title, number_of_songs=None):
    """Return a dictionary of album"""
    album = {'artist_name': artist_name, 'album_title': album_title}

    if number_of_songs:
        album['number_of_songs'] = number_of_songs
    return album

parokya = make_album('parokya ni edgar','buruguduystunstugudunstuy')
print(parokya)

kamikazee = make_album('kamikazee', 'romantico')
print(kamikazee)

malone = make_album('post malone', 'beerbongs & bentleys')
print(malone)

twice = make_album('twice','dive',number_of_songs=10)
print(twice)