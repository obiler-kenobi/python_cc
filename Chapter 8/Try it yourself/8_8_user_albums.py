def make_album(artist_name, album_title, number_of_songs=None):
    """Return a dictionary of album"""
    album = {'artist_name': artist_name, 'album_title': album_title}

    if number_of_songs:
        album['number_of_songs'] = number_of_songs
    return album

while True:
    print("\nPlease tell me your favorite album:")
    print("(enter 'q' at any time to quit)")
    artist = input("Artist Name: ")
    if artist == 'q':
        break
     
    album_name = input("Album Name: ")
    if album_name == 'q':
        break
     
    number_of_songs = input("Number of songs: ")
    if number_of_songs == 'q':
         break

    album = make_album(artist, album_name, number_of_songs)
    print(album)