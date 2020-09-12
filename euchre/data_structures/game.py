class Game:
    """
    	- Features
		○ Players - list (crucially ordered!)
		○ Index_of_active_player
		○ Deck
	- Functions
		○ Start()
			§ Choose_dealer()
			§ Play the rounds (a round is a point scored)
				§ Shuffle the deck
				§ Deal out the cards
				§ Decide trump
					□ Phase 1 - pick up or put down
					□ Phase 2 - call randomly
				§ Play_tricks
					Determine the trick taker
					Increase the team trick counts
					Check if any team has scored
				§ Determine who scores
				§ Update score
				§ Check for 10 points
    """