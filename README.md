# Blackjack
## Christian Tropeano

## Why and How
I decided to make the card game Blackjack because it is my favorite card game to play and I feel like this game can be used in order to keep my programming skills up-to-par when I have down time (using data structures like a stack for the cards and algorithms for shuffling the cards, etc). Right now, it is only a text-based version of the game; eventually, a version of the game with a GUI will be implemented.
I made this game using Python, as it is a language that I feel comfortable using. I used *insert libraries here*.

## How to Launch and Use Program 
*Insert how to download here*  
After you successully downloaded the program, you will be prompted with the option to  
Type either 'p' or 'play' to play the game  
Type either 'r' or 'rules' to view the rules of the game  
Type either 'q' or 'quit' to exit the application  

If you decide to play the game, then the game will commence and you will be dealt two cards and the dealer will be dealt one (which is how a standard game of Blackjack starts). Your choice for a move will be selected (the option to hit, stand, double down, etc.) and you can type the appropriate choice. The game will be played and at the end, a winner will be chosen!

## Rules of Blackjack
1. The point of the game is to try to get to as close to the value 21 as possible without going over
2. Player puts in a bet before they are dealt any cards
3. Player gets dealt 3 cards, dealer gets two cards, one face-up (if the dealer gets a facecard or an ace, they will peak at the second card to see if they get blackjack)
4. The player can choose to **hit** (which means take another card), **stand** (which means that they do not want to take another card), **split** (this can only be done if the player is dealt two cards of the same value, and they will get two hands instead of just one, but they must put in the same amount of money as the first bet; ***this can only be done once per game***) or **double down** (this means that the player can get dealt one more card, but they have to double their original bet and after that they cannot make another turn)
5. If the player chooses to hit, stand or double down and they go over 21, then they lose and do not get any of their bet back (this is known as a **bust**)
6. If the dealer goes over 21, then the dealer loses and everyone at the table receives 1.5X their bet that did not bust
7. If a player is dealt a (10 or a face card [which has the value 10]) and an ace, then that is a **blackjack** and the player wins 2x their bet
8. If the dealer gets dealt a blackjack, then everyone at the table loses
9. If the player hits 5 times (meaning that they have 7 cards), that is known as a **7 card charlie** and the player wins 1.5x their original bet
10. An ace is worth 11 (hard 11) in general but it becomes worth a 1 (soft ace) when the player's overall hand goes over 11 excluding the ace (so if they get dealt a face card, a 4 and an ace, instead of that being 25 where the ace is an 11, the hand becomes a 15; if the player is dealt an ace and a 7 however then that is 18).
11. The dealer must stand when his score is 17.
12. If the player gets dealt a Blackjack or gets 21, then the game ends.