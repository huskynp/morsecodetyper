
MORSE_CODE_VALS = {'.-': 'a', '-...': 'b', '-.-.': 'c', '-..': 'd', '.': 'e', '..-.': 'f', '--.': 'g', 
'....': 'h', '..': 'i', '.---': 'j', '-.-': 'k', '.-..': 'l', '--': 'm', '-.': 'n', '---': 'o', '.--.': 'p', 
'--.-':'q', '.-.': 'r', '...': 's', '-': 't', '..-': 'u', '...-': 'v', '.--': 'w', '-..-': 'x', '-.--': 'y', '--..': 'z', 
'-----': '0', '.----': '1', '..---': '2', '...--': '3', '....-': '4', '.....': '5', '-....': '6', '--...': '7', '---..': '8', '----.': '9'}
END_LETTER_IDENTIFIER = '/'
SHIFT_IDENTIFIER=","
UNIQUE_SHIFTS = {'1':'!','2':'@','3':'#','4':'$','5':'%','6':'^','7':'&','8':'&','9':'(','0':')'}

class MorseIdentifier():
    def __init__(self):
        self.sequence = ""
        self.letters = ""

    def translateMorse(self,morse):
        lines = morse.split('///')
        i = 1
        for line in lines:
            words = [word for word in line.split('//') if word != '']
            for word in words:
                letters = word.split('/')
                for letter in letters:
                    shift = False
                    if SHIFT_IDENTIFIER in letter: 
                        shift = True
                        letter = letter.replace(SHIFT_IDENTIFIER, '')
                    if letter in MORSE_CODE_VALS.keys():
                        val = MORSE_CODE_VALS[letter]
                        if shift and val not in UNIQUE_SHIFTS.keys(): val = val.upper()
                        elif shift and val in UNIQUE_SHIFTS.keys(): val = UNIQUE_SHIFTS[val]
                        self.letters += val
                        self.sequence += letter + '/'
                self.letters += ' '*line.count('//')
                #self.sequence += '//'*line.count('//')
            if(i < len(lines)): 
                self.letters += '\n'*morse.count('///')
            #self.sequence += '///'*morse.count('///')
            i+=1
        

        res = self.sequence
        tot = self.letters

        print(self.sequence, len(self.letters)) #debug
        self.sequence = ''
        self.letters = ''

        return res,tot

    def add(self,key, isTypeOn = False):
        self.sequence += key

if __name__ == "__main__":
    morse = MorseIdentifier()
    while 1:
        text = input('Morse: ').strip().lower()
        if text.lower() == 'quit': break
        morse.translateMorse(text)