import random
import lyricsgenius
import statistics
genius = lyricsgenius.Genius(
    "776-QCS4FRVa1Ozb9gbYA-oOusUbGuK_Ykng7D-kAB1xkPSYO5S82EGZxlLGa3BX")

names = ['White Christmas', 'The Chipmunk Song', 'Rudolph, The Red Nosed Reindeer', 'I Saw Mommy Kissing Santa Claus', 'Jingle Bell Rock', 'The Christmas Song', 'Snoopys Christmas', 'Here Comes Santa Claus', 'Little Drummer Boy', 'Donde Esta Santa Claus', 'Rockin Around The Christmas Tree', 'Youre All I Want For Christmas', 'Babys First Christmas', 'Santa Claus Is Coming To Town', 'Home For The Holidays', 'Santa Claus Is Coming To Town', 'Do They Know Its Christmas', 'Happy Christmas (War is Over)', 'May You Always', 'Grandma Got Run Over By A Reindeer', 'Jingle Bell Rock', 'Jingle Bells', 'Frosty the Snowman', 'Merry Christmas Darling', 'Little St. Nick', 'Please Come Home For Christmas', 'Its Beginning to Look A Lot Like Christmas', 'Feliz Navidad', 'Santa Baby', 'Do You Hear What I Hear', 'Blue Christmas', 'Run Rudolph Run', '(Sleep in Heavenly Peace) Silent Night', 'Nuttin for Christmas', 'Wonderful Christmastime', 'Step Into Christmas', 'The Christmas Waltz', 'All I Want For Christmas is My Two Front Teeth', 'Please Come Home For Christmas', 'Amen', 'Monsters Holiday', 'Holly Jolly Christmas', 'Give Love on Christmas Day', 'Dominick, The Italian Christmas Donkey', 'White Christmas', 'Its Christmas Everywhere', 'Gee Whiz, Its Christmas', 'Christmas Dragnet', 'Sleigh Ride - (Instrumental)', 'Pretty Paper', 'Christmas (Baby Please Come Home)',
         'If It Doesnt Snow on Christmas', 'What Christmas Means To Me', 'Marshmallow World', 'Winter Wonderland', 'Merry, Merry Christmas Baby', 'Frosty the Snowman', 'Christmas Auld Lang Syne', 'Jingle Bells (Instrumental)', 'Silver Bells', 'Merry Christmas All', 'Rudolph, The Red Nosed Reindeer', 'Santa Claus is Coming To Town', 'Have Yourself A Merry Little Christmas', 'Sleigh Ride', 'The Most Wonderful Time of The Year', 'Peace on Earth/Little Drummer Boy', 'Winter Wonderland', 'Happy Holidays', 'Kissin By The Mistletoe', 'The Man With All The Toys', 'The Twelve Days of Christmas', 'Here Comes Santa Claus', 'We Need A Little Christmas', 'Last Christmas', 'Silent Night', 'We Wish You The Merriest', 'White Christmas', 'Santa Claus Is Watching You', 'This Christmas', 'A Christmas Long Ago', 'Let It Snow, Let It Snow, Let It Snow', 'Sleigh Ride', 'Mistletoe and Holly', 'Its Christmas Once Again', 'Twas The Night Before Christmas', 'This Time of Year', 'Parade of The Wooden Soldiers', 'Rockin Around The Christmas Tree', 'Chrissy, The Christmas Mouse', 'Marshmallow World', 'Christmas Serenade', 'Christmas Aint Christmas', 'Youre My Christmas Present', 'I Saw Mommy Kissing Santa Claus', 'I Believe in Father Christmas', 'Someday At Christmas', 'Merry Christmas Baby', 'Santa Claus Is Coming To Town', 'Bells of St. Mary']

new_lyrics = []
song = []


def sing_me_a_song(lyrics):
    for i in range(0, 51):
        word = []
        for j in range(0, 97):
            word.append(lyrics[j][i])
        song.append(word[random.randint(0, 96)])
        song.append(statistics.mode(word))

    song1 = ' '.join(song)
    return print(song1)


def add_song(songs):
    lyrics = []
    for i in songs['hits']:
        url = i['result']['url']
        song_lyrics = genius.lyrics(url)
        lyrics.append(song_lyrics)
        song = (lyrics[0].split(' ' and '\n'))

    for i in range(len(song)):
        while 'Verse' in song[i]:
            song.pop(i)
            song.append('')
        while 'Chorus' in song[i]:
            song.pop(i)
            song.append('')
        while 'Intro' in song[i]:
            song.pop(i)
            song.append('')
        while 'Instrumental' in song[i]:
            song.pop(i)
            song.append('')
    stringsong = ''
    for i in range(len(song)):
        stringsong += song[i] + ' '
    array = stringsong.split()
    new_lyrics.append(array)
    return


def run():
    for i in range(len(names)):
        bump = genius.search_songs(names[i])
        print(names[i])
        print(str(int((i/len(names))*100))+'%')
        add_song(bump)
    print(new_lyrics)
    sing_me_a_song(new_lyrics)
    return


run()
