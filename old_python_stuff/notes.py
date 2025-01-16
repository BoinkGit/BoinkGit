from winsound import Beep as b
megaloChorus = '2220700605040245 1120700605040245 8820700605040245 7720700605040245'
megaloVerse1 = '4044040402020004 0440506054245004 0440506070907002 0202729090909'
tones = [37, 262, 294, 330, 349, 392, 415, 440, 494, 523]
songs = {'1':megaloChorus,'2':megaloVerse1}
def numTones(num='0'):
    letters = ['𝄽','C','D','E','F','G','G♯','A','B','C2']
    notes = []
    letNotes = []
    for i in num:
        try:
            notes.append(tones[int(i)])
            letNotes.append(letters[int(i)])
        except: None
    print(letNotes)
    for i in notes:
        b(i,200)
while True:
    if input('var or yours\n\t') == 'yours':
        a = input()
        if a == '': break
        else: numTones(a)
    else:
        a = input('1 = megaloChorus\n2 = megaloVerse1\n')
        if a == 'loop':
            while True:
                numTones(megaloChorus)
                numTones(megaloVerse1)
        numTones(songs[a])
