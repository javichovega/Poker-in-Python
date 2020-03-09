#!/usr/bin/env python
#  -*- encoding: utf-8 -*-
import Values as valor
import random
import numpy as np

class PokerHand:
    def __init__(self):
		# Data Upload
		# Length of the Labels of each card
        self.len_value = len(valor.values)
		# Length of the Types of deck
        self.len_suit = len(valor.suit)
    
    def generate_hand(self):
        # Generation of Poker Hand
        hand = ""
        for n in range(valor.valor):
			      # Random number between 1 and 13 (self.len_value)
			      m = random.randint(1, self.len_value)
			      # Random number between 1 and 4 (self.len_suit)
			      n = random.randint(1, self.len_suit)
				  # Creation of one value of the Poker Hand
			      hand = hand + (valor.valores[m-1] + valor.suit[n-1] + valor.separador)
        return hand

    def calc_value(hands):
        # Calculation the value of Poker Hands
        # Where the value of the type of the Poker Hand is save
        peso = []
        # Where the sum of each card value of the Poker Hand is save
        peso_aux = []
        i = 0
        # Processing the quantity of Poker Hands
        while i < len(hands):
			      # Generation a dictionary with all the values equal to 0, from Label of each card
			      cards = dict.fromkeys(valor.valores, 0)
			      # Generation a dictionary with all the values equal to 0, from Type of deck
			      palos = dict.fromkeys(valor.suit, 0)
			      # Where the value of each Poker Hand is save
			      suma_aux = 0
			      # Where the value of of the card in each Poker Hand is save
			      order = []
			      # Processing the Poker Hand
			      for n in range(len(hands[i])):
				      # The position corresponding to the label of the card in the Poker Hand
				      if n%3 == 0:
						       # If the label of the card appear in "cards"
						       if hands[i][n] in cards:
							       # Aggregate 1 to the corresponding label
							       cards[hands[i][n]] = cards[hands[i][n]] + 1
						       # Saving the corresponding value of the Label of each card
						       order.append(valor.values.get(hands[i][n]))
						       # Aggregating  the corresponding value of the Label of each card
						       suma_aux = suma_aux + (valor.values.get(hands[i][n]))
				      # The position corresponding to space in blank
				      elif n%3 == 2:
						       suma_aux = suma_aux
				      # The position corresponding to the deck of the card in the Poker Hand
				      else: # n%3 == 1
						       # If the deck of the card appear in "palos"
						       if hands[i][n] in palos:
							       # Aggregate 1 to the corresponding deck
							       palos[hands[i][n]] = palos[hands[i][n]] + 1

			      # Sorting the values of cards of the Poker Hand
			      order.sort(reverse=True)
			      # If the value of the first position minus 4 is equal to the last value,
			      #  then we have a sequence and "ordenado" is "True"
			      ordenado = ((order[0]-4) == order[valor.valor - 1])
			      # Filtering only the cards with values equal or major to 1
			      cartas = list(filter(lambda x: x > 0, cards.values()))
			      # If the maximum value of "palos" is equal to 5 and is in order, then we have a...
			      if (max(palos.values()) == 5 and ordenado):
				      # If first value of "order" is equal to 13,
				      #  then we have a Royal Flush (Royal Straight Flush)
				      if (order[0] == 13):
						       suma = 110
				      # If first value of "order" is different to 13,
				      #  then we have a Straight Flush
				      else:
						       suma = 105
			      # If the maximum value of "palos" is equal to 5 and is not in order,
			      #  then we have a Flush
			      elif (max(palos.values()) == 5 and not(ordenado)):
				      suma = 90
			      # If the maximum value of "palos" is equal or major to 2 and is in order,
			      #  then we have a Straight
			      elif (max(palos.values()) >= 2 and ordenado):
				      suma = 85
			      # If the maximum value of "cartas" is equal to 4,
			      #  then we have a Four of a Kind
			      elif max(cartas) == 4:
				      suma = 100
			      # If the maximum value of "cartas" is equal to 3, then we have a...
			      elif max(cartas) == 3:
				      # If lenght of "cartas" is equal to 2,
				      #  then we have a Full House
				      if len(cartas) == 2:
						       suma = 95
				      # If lenght of "cartas" is different to 2,
				      #  then we have a Three of a Kind
				      else:
						       suma = 80
			      # If the maximum value of "cartas" is equal to 2, then we have a...
			      elif max(cartas) == 2:
				      # If lenght of "cartas" is equal to 3,
				      #  then we have a Two Pair
				      if len(cartas) == 3:
						       suma = 75
				      # If lenght of "cartas" is different to 3,
				      #  then we have a One Pair
				      else:
						       suma = 70
			      # None of above,
			      #  then we have a High Card
			      else:
				      suma = suma_aux
			      # Save the value of "suma", corresponding to the value of the type of the Poker Hand
			      peso.append(suma)
			      # Save the value of "suma_aux", corresponding to the value of the Poker Hand
			      peso_aux.append(suma_aux)
			      i+=1
        # Sorting the values of each type of Poker Hand
        aux = sorted(peso)
		# If the first value is equal to last value
        if aux[0] == aux[i-1]:
			      peso = peso_aux
        return peso
    
    def who_win(hands):
        # Which Poker Hands win ?
		# Transformation of the Poker Hands
        array = np.array(hands)
		# Which is the maximum value of the Poker Hands ?
        indice = np.where(array == max(array))[0]
		# If the length of "indice" is 1 and the position corresponds to the first hand
        if (len(indice) == 1 and indice[0] == 0):
			      return "WIN"
		# If the length of "indice" is major to 1 and the position corresponds to the first hand
        elif (len(indice) > 1 and indice[0] == 0):
			      return "TIE"
		# If the length of "indice" is major to 1 and the position not corresponds to the first hand
        else:
			      return "LOSS"
