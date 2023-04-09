from replit import clear
from art import logo
#HINT: You can call clear() to clear the output in the console.

print(logo)
print("Welcome to the secret auction program.")


bidders = {}

def find_the_highest(all_bidders):
	highest_bid = 0
	
	for bidder in bidders:
		if bidders[bidder] > highest_bid:
			highest_bid = bidders[bidder]
			winner = bidder
	
	print(f"The winner is {winner} with a bid of ${highest_bid}")


	
should_continue = True
while should_continue:
	get_name = input("What is your name?: ")
	get_bid = int(input("What is your bid?: $"))
	bidders[get_name] = get_bid
	ask_continue = input("Are there any other bidders? Type 'yes' or 'no'\n").lower()

	if ask_continue == "no":
		should_continue = False
		find_the_highest(bidders)
	elif ask_continue == "yes":
		clear()
	

