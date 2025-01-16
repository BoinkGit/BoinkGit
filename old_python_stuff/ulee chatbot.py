# ulee chatbot
from random import randint
from pyautogui import prompt, alert
chatList = []
triggers = {'hello':'hi','bye':'you could\'ve just pressed the x button',
            'ultrakill':'yo i love that game!','raisin':'ugh i hate those things'}
def chat(chatlen = 20):
    text = ''
    for i in range(chatlen):
        x = i - chatlen
        if abs(x) < len(chatList)+1:
            if x % 2 == 1:
                text += f'\nUlee: {chatList[x]}'
            else: text += f'\nYou: {chatList[x]}'
    yourMsg = prompt(text,'texts')
    chatList.append(yourMsg)
    x2 = 0
    for i in triggers:
        x2 += 1
        if i in yourMsg.lower():
            chatList.append(triggers[i])
            if i is 'bye':
                text += f'\nYou: {chatList[-2]}' + f'\nUlee: {chatList[-1]}'
                alert(text,'texts','')
                quit()
            break
        elif x2 == len(triggers):
            chatList.append('what?'); break
while True:
    chat()
