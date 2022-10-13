# Texas Hold'em Hands
## Instructions

Texas Hold'em is a Poker variant in which each player is given two "hole cards".
Players then proceed to make a series of bets while five "community cards" are dealt.
If there are more than one player remaining when the betting stops, a showdown takes place in which players reveal 
their cards. 

Each player makes the best poker hand possible using five of the seven available cards (community cards +
the player's hole cards).

Possible hands are, in descending order of value:

1. Straight-flush:
   * Five consecutive ranks of the same suit
   * Higher rank is better
2. Four-of-a-kind:
   * Four cards with the same rank 
   * Tiebreaker is first the rank, then the rank of the remaining card
3. Full house
   * Three cards with the same rank, two with another
   * Tiebreaker is first the rank of the three cards, then rank of the pair
4. Flush 
   * Five cards of the same suit
   * Higher ranks are better, compared from high to low rank
5. Straight 
   * Five consecutive ranks
   * Higher rank is better
6. Three-of-a-kind
   * Three cards of the same rank
   * Tiebreaker is: 
      1. The rank of the three cards
      2. the highest other rank
      3. the second-highest other ran
7. Two pair:
   * Two cards of the same rank, two cards of another rank
   * Tiebreaker is
     1. the rank of the high pair
     2. the rank of the low pair 
     3. the rank of the remaining card
8. Pair 
   * two cards of the same rank
   * Tiebreaker is 
     * first the rank of the two cards
     * the three other ranks.
9. Nothing 
   * Tiebreaker is the rank of the cards, from high to low

Given hole cards and community cards, complete the function **hand** to return the type of hand (as written above, you 
can ignore case) and a list of ranks in decreasing order of significance, to use for comparison against other hands of 
the same type, of the best possible hand.

    hand(["A♠", "A♦"], ["J♣", "5♥", "10♥", "2♥", "3♦"])
    # ...should return ("pair", ranks: ["A", "J", "10", "5"]})

    hand(["A♠", "K♦"], ["J♥", "5♥", "10♥", "Q♥", "3♥"])
    # ...should return ("flush", ["Q", "J", "10", "5", "3"])
 
for Straights with an Ace, only the ace-high straight is accepted. An ace-low straight is invalid (i.e. `A,2,3,4,5` is invalid)

This is consistent with the author's reference solution. ~docgunthrop

## Reference
Taken from CodeWars.com here: https://www.codewars.com/kata/524c74f855025e2495000262/train/python