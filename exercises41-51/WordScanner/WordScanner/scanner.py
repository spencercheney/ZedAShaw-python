class scanner(object):

    #converts a string to a number or returns a null value
    def convert_numbers(self, s):
        try:
            return int(s)
        except ValueError:
            return None
    
    def scan(self, sentence):
        directions = ['north', 'south', 'east', 'west', 'down', 'up', 'left', 'right', 'back']
        verbs = ['go', 'stop', 'kill', 'eat']
        stop = ['the', 'in', 'of', 'from', 'at', 'it']
        nouns = ['door', 'bear', 'princess', 'cabinet']

        lex_sentence = []

        words = sentence.split()

        for wordI in range(len(words)):         #iterate through the list of words

            found_word = False

            for directionI in range(len(directions)):               #search through list of direction words for each word
                if words[wordI] == directions[directionI]:
                    lex = ('direction', words[wordI])
                    found_word = True

            for verbI in range(len(verbs)):                         #search through the list of verbs
                if words[wordI] == verbs[verbI]:
                    lex = ('verb', words[wordI])
                    found_word = True
            
            for stopI in range(len(stop)):                          #search through the list of stop words
                if words[wordI] == stop[stopI]:
                    lex = ('stop', words[wordI])
                    found_word = True

            for nounI in range(len(nouns)):                         #search through the list of nouns
                if words[wordI] == nouns[nounI]:
                    lex = ('noun', words[wordI])
                    found_word = True

            check_number = self.convert_numbers(words[wordI])       #check to see if it's a number
            if check_number:                                        #if it is make a tuple
                lex = ('number', check_number)
                found_word = True

            if not found_word:                                      #if the word isn't a number and isn't in any 
                lex = ('error', words[wordI])                       #of the list make a tuple with 'error' as the first item

            lex_sentence.append(lex)

        return lex_sentence
            


lexicon = scanner()