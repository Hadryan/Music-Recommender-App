import csv


class Song:
    def __init__(self, id, title, artist,danceability, decade, uri, genre):
        self.id = id
        self.title = title
        self.artist = artist
        self.danceability = danceability
        self.decade = decade
        self.uri = uri
        self.genre = genre

#
def MusicList():
    list = []
    with open('MusicDBNew.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        count = 0
        for row in csv_reader:
           # print(row[0])
            if count != 0:
                s = Song(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
                list.append(s)
            count += 1
    #print(count)
    return list

