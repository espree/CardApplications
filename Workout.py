#Python modules imported
import json
import requests
import sys

#My imported modules, including adding file paths
sys.path.insert(0, "../DeckOfCards")

#Driver program for conducting a deck of cards workout
class DeckOfCardsWorkout:
    def start_new_workout(self):
        r = requests.get('http://localhost:5000/shuffle')
        print(r.json().get('message'))

    def next_workout(self):
        r = requests.get('http://localhost:5000/draw')
        card = r.json()
        if (card[1] == "Clubs"):
            print(card[0] + " second body planks.")
        elif (card[1] == "Diamonds"):
            print(card[0] + " dumbbell presses.")
        elif (card[1] == "Hearts"):
            print(card[0] + " jumping jacks")
        elif (card[1] == "Spades"):
            print(card[0] + " body squats")
        elif (card[1] == "cards"):
            print(card[0] + " " + card[1] + " remaining")
        else:
            print("Invalid output")

#Driver method
def main():
    workout = DeckOfCardsWorkout()
    workout.start_new_workout()

    #Because there are 52 cards and I do not intend on returning cards,
    #this is a magic value, and the 53 loop should return no cards
    #remaining message
    for i in range(53):
        workout.next_workout()

if __name__ == '__main__':
    main()
