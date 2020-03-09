#!/usr/bin/env python
#  -*- encoding: utf-8 -*-
import Base

#####
# Generation and visualization of Poker Hands
#####
# Number of Poker Hands to creating
numero = 2
# Where the Poker Hands are save
list_hands = []
i = 1
c = Base.PokerHand() # Data Upload
while i <= numero:
	a = Base.PokerHand.generate_hand(c)
	list_hands.append(a)
	print("Poker Hand", i, ":", a, "\n")
	i+=1


#####
# Calculation of the value of each Poker Hand
#####
# Where the value of the Poker Hands are save
peso_hands = Base.PokerHand.calc_value(list_hands)


#####
# Comparisons of the Poker Hands and their respective result
#####
print("You have the Poker Hand 1 !!!\n")
print("Your Poker Hand:", Base.PokerHand.who_win(peso_hands))
