class Song(object):
    
    #where you put your variables
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print line

happy_bday = Song(["Happy Birthday to you",
                   "Happy Birthday to you",
                   "Happy Birthday dear fri-end",
                   "Happy Birthday to you"])

bulls_on_parade = Song(["They rally around the family",
                        "With pokets full of shells"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()