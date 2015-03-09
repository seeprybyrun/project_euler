import time

class Card:
    def __init__(self,s):
        # rank
        self.rank = s[0]
        if self.rank == 'T':
            self.rank = 10
        elif self.rank == 'J':
            self.rank = 11
        elif self.rank == 'Q':
            self.rank = 12
        elif self.rank == 'K':
            self.rank = 13
        elif self.rank == 'A':
            self.rank = 14
        else:
            self.rank = int(self.rank)
        # suit
        self.suit = s[1]

class Hand:
    def __init__(self,cards):
        self.cards = [Card(c) for c in cards]
        self.ranks = [c.rank for c in self.cards]
        self.numOfEachRank = [self.ranks.count(c) for c in set(self.ranks)]
        self.counts = { r : self.ranks.count(r) for r in self.ranks }
        self.handRank = self.findHandRank()
    def findHandRank(self):
        if self.isStraight() and self.isFlush:
            self.highCard = self.findHighCard()
            return 8
        elif self.hasNKind(4):
            for r in self.counts:
                if self.counts[r] == 4:
                    self.kindRank = r
                if self.counts[r] == 1:
                    self.highCard = 1
            return 7
        elif self.hasFullHouse():
            for r in self.counts:
                if self.counts[r] == 3:
                    self.kindRank3 = r
                if self.counts[r] == 2:
                    self.kindRank2 = r
            return 6
        elif self.isFlush():
            self.ranks = sorted(self.ranks)
            return 5
        elif self.isStraight():
            self.highCard = self.findHighCard()
            return 4
        elif self.hasNKind(3):
            self.highCards = []
            for r in self.counts:
                if self.counts[r] == 3:
                    self.kindRank = r
                if self.counts[r] == 1:
                    self.highCards.append(r)
            self.highCards = sorted(self.highCards)
            return 3
        elif self.hasTwoPair():
            self.kindRanks = []
            for r in self.counts:
                if self.counts[r] == 1:
                    self.highCard = r
                if self.counts[r] == 2:
                    self.kindRanks.append(r)
            self.kindRanks = sorted(self.kindRanks)
            return 2
        elif self.hasPair():
            self.highCards = []
            for r in self.counts:
                if self.counts[r] == 1:
                    self.highCards.append(r)
                if self.counts[r] == 2:
                    self.kindRank = r
            self.highCards = sorted(self.highCards)
            return 1
        else:
            self.ranks = sorted(self.ranks)
            return 0
    def isStraight(self):
        if len(set(self.ranks)) < 5:
            return False
        return max(self.ranks)-min(self.ranks) == 4 or sorted(self.ranks) == [2,3,4,5,14]
    def isFlush(self):
        suits = [c.suit for c in self.cards]
        return len(set(suits)) == 1
    def hasNKind(self,n):
        return n in self.numOfEachRank
    def hasFullHouse(self):
        return sorted(self.numOfEachRank) == [2,3]
    def hasTwoPair(self):
        return sorted(self.numOfEachRank) == [1,2,2]
    def hasPair(self):
        return sorted(self.numOfEachRank) == [1,1,1,2]
    def findHighCard(self):
        if sorted(self.ranks) == [2,3,4,5,14]:
            return 5
        return max(self.ranks)
    def compareTo(self,h):
        """returns -1 if h is a better hand, +1 if self is a better hand, and 0 if the hands are tied"""
        if self.handRank > h.handRank:
            return 1
        elif self.handRank < h.handRank:
            return -1

        # if hand ranks are tied...
        r = self.handRank

        # straight flush or straight: check for highest card
        if r == 8 or r == 4:
            if self.highCard > h.highCard:
                return 1
            elif self.highCard < h.highCard():
                return -1

        # four-of-a-kind: check the rank appearing four times, then check the remaining rank
        elif r == 7:
            if self.kindRank4 > h.kindRank4:
                return 1
            elif self.kindRank4 < h.kindRank4:
                return -1
            if self.highCard > h.highCard:
                return 1
            elif self.highCard < h.highCard:
                return -1

        # full house: check the rank appearing 3 times, then check the rank appearing 2 times
        elif r == 6:
            if self.kindRank3 > h.kindRank3:
                return 1
            elif self.kindRank3 < h.kindRank3:
                return -1
            if self.kindRank2 > h.kindRank2:
                return 1
            elif self.kindRank2 < h.kindRank2:
                return -1

        # flush or high card: compare each highest rank, then go downward until one wins
        elif r == 5 or r == 0:
            for i in range(4,-1,-1):
                if self.ranks[i] > h.ranks[i]:
                    return 1
                elif self.ranks[i] < h.ranks[i]:
                    return -1

        # three-of-a-kind: compare the rank appearing 3 times, then compare the remaining ranks descending
        elif r == 3:
            if self.kindRank > h.kindRank:
                return 1
            elif self.kindRank < h.kindRank:
                return -1
            for i in range(1,-1,-1):
                if self.highCards[i] > h.highCards[i]:
                    return 1
                elif self.highCards[i] < h.highCards[i]:
                    return -1

        # two-pair: compare the ranks of the pairs, descending, then the high card
        elif r == 2:
            for i in range(1,-1,-1):
                if self.kindRanks[i] > h.kindRanks[i]:
                    return 1
                elif self.kindRanks[i] < h.kindRanks[i]:
                    return -1
            if self.highCard > h.highCard:
                return 1
            elif self.highCard < h.highCard:
                return -1

        # pair: compare the pair, then the ranks of the remaining cards, descending
        elif r == 1:
            if self.kindRank > h.kindRank:
                return 1
            elif self.kindRank < h.kindRank:
                return -1
            for i in range(2,-1,-1):
                if self.highCards[i] > h.highCards[i]:
                    return 1
                elif self.highCards[i] < h.highCards[i]:
                    return -1

        # tie!
        return 0

t0 = time.clock()

f = open('p054_poker.txt','r')
#f = open('p054_poker_test.txt','r')
hands = f.readlines()
f.close()

answer = 0

for hand in hands:
    cards = hand.split()
    player1 = cards[:5]
    player2 = cards[5:]
    hand1 = Hand(player1)
    hand2 = Hand(player2)
    gameResult = hand1.compareTo(hand2)
    winner = ''
    if gameResult > 0:
        winner = 'player1'
        answer += 1
    elif gameResult < 0:
        winner = 'player2'
    else:
        winner = 'tie'
    #print '{} vs {}: {}'.format(player1,player2,winner)

print 'answer: {0}/{1}'.format(answer,len(hands))
print 'milliseconds elapsed: {0}'.format(1000*(time.clock()-t0))
