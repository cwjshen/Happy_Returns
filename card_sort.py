from collections import deque

# For this problem, can I assume that there are no duplicate cards or any potential cycles in the trip?
# Multiple journey paths?

class Boarding_Card():
	def __init__(self, src, dest, mode, travel_num, seat_num):
		self.src = src
		self.dest = dest
		self.mode = mode
		self.travel_num = travel_num
		self.seat_num = seat_num

test = Boarding_Card("NY", "SF", "air", "SK455", "45B")


def sort_cards(list_of_cards):
	
	solution = []
	starting_card = list_of_cards[0]
	solution.append(starting_card)
	del list_of_cards[0]

	while list_of_cards:		
		for i in range(len(list_of_cards)):			
			curr = solution[-1]
			if list_of_cards[i].src == curr.dest:				
				solution.append(list_of_cards[i])
				del list_of_cards[i]
		for i in range(len(list_of_cards)):
			curr = solution[0]
			if list_of_cards[i].dest == curr.src:
				solution.insert(0, list_of_cards[i])
				del list_of_cards[i]				

	for card in solution:
		print 'Src: ', card.src, 'Dest: ', card.dest, 'Mode: ', card.mode, 'Travel No.: ', card.travel_num, 'Seat No.: ', card.seat_num 
	return solution

# All that needs to be done is a little string output and formatting to get desired list as per the spec


def main():
	card1 = Boarding_Card("NY", "SF", "air", "A455", "45B")
	card2 = Boarding_Card("BOS", "NY", "bus", "B235", "23C")
	card3 = Boarding_Card("SF", "LA", "air", "A500", "10A")

	list_of_cards = [card1, card2, card3]
	sort_cards(list_of_cards)

main()