#!/usr/bin/env python
#  -*- encoding: utf-8 -*-
import Base

#####
# Comparisons of the Poker Hands and their respective result
#####
# This are the unit tests according to the Challenge
list_tests = ['TC TH 5C 5H KH ', '9C 9H 5C 5H AC ',
			  'TS TD KC JC 7C ', 'JS JC AS KC TD ',
			  '7H 7C QC JS TS ', '7D 7C JS TS 6D ',
			  '5S 5D 8C 7S 6H ', '7D 7S 5S 5D JS ',
			  'AS AD KD 7C 3D ', 'AD AH KD 7C 4S ',
			  'TS JS QS KS AS ', 'AC AH AS AS KS ',
			  'TS JS QS KS AS ', 'TC JS QC KS AC ',
			  'TS JS QS KS AS ', 'QH QS QC AS 8H ',
			  'AC AH AS AS KS ', 'TC JS QC KS AC ',
			  'AC AH AS AS KS ', 'QH QS QC AS 8H ',
			  'TC JS QC KS AC ', 'QH QS QC AS 8H ',
			  '7H 8H 9H TH JH ', 'JH JC JS JD TH ',
			  '7H 8H 9H TH JH ', '4H 5H 9H TH JH ',
			  '7H 8H 9H TH JH ', '7C 8S 9H TH JH ',
			  '7H 8H 9H TH JH ', 'TS TH TD JH JD ',
			  '7H 8H 9H TH JH ', 'JH JD TH TC 4C ',
			  'JH JC JS JD TH ', '4H 5H 9H TH JH ',
			  'JH JC JS JD TH ', '7C 8S 9H TH JH ',
			  'JH JC JS JD TH ', 'TS TH TD JH JD ',
			  'JH JC JS JD TH ', 'JH JD TH TC 4C ',
			  '4H 5H 9H TH JH ', '7C 8S 9H TH JH ',
			  '4H 5H 9H TH JH ', 'TS TH TD JH JD ',
			  '4H 5H 9H TH JH ', 'JH JD TH TC 4C ',
			  '7C 8S 9H TH JH ', 'TS TH TD JH JD ',
			  '7C 8S 9H TH JH ', 'JH JD TH TC 4C ',
			  'TS TH TD JH JD ', 'JH JD TH TC 4C ']
i = 0
# Processing the quantity of unit tests of the Poker Hands
while i < len(list_tests):
	if i%2 == 0:
		list_hands = [list_tests[i], list_tests[i+1]]
		print(list_hands)
		peso_hands = Base.PokerHand.calc_value(list_hands)
		print(Base.PokerHand.who_win(peso_hands))
	i+=1
