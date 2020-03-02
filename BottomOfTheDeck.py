import json
import requests
import sys

#My imported modules, including adding file paths
sys.path.insert(0, "../DeckOfCards")

#This just takes the top card and moves it to the
#bottom after saying what card it is.
def main():
    r = requests.get('http://localhost:5000/shuffle')
    print(r.json().get('message'))
    for i in range(104):
        r = requests.get('http://localhost:5000/draw')
        card = r.json()
        print(card[0] + " of " + card[1])
        x = requests.post('http://localhost:5000/return',
            {'face': card[0], 'suit': card[1]})

if __name__ == '__main__':
    main()
