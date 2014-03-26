#!/usr/bin/env python
# -*- coding: utf-8 -*-

def My_Sort(card):
    tmp = sorted([cards.index(i) for i in card])
    return [cards[i] for i in tmp]


def Royal_Flush(card):
    nums = card[0]
    suit = card[1]
    tmp = My_Sort(nums)
    if tmp == ['10','J','Q','K','A']:
        if len(set(suit)) == 1:
            return 10
    return False

def Straight_Flush(card):
    nums = card[0]
    suit = card[1]
    tmp = My_Sort(nums)
    tmp1 = cards.index(tmp[0])
    if tmp == cards[tmp1:tmp1+len(tmp)]:
        if len(set(suit)) == 1:
            return 9
    return False

def Four_Kind(card):
    nums = card[0]
    tmp = [nums.count(i) for i in nums]
    if max(tmp) == 4:
        return 8
    return False

def Full_House(card):
    nums = card[0]
    tmp = [nums.count(i) for i in nums]
    if max(tmp) == 3 and len(set(nums)) == 2:
        return 7
    return False

def Flush(card):
    suit = card[1]
    if len(set(suit)) == 1:
        return 6
    return False

def Straight(card):
    nums = card[0]
    tmp = My_Sort(nums)
    tmp1 = cards.index(tmp[0])
    if tmp == cards[tmp1:tmp1+len(tmp)]:
        return 5
    return False

def Three_Kind(card):
    nums = card[0]
    tmp = [nums.count(i) for i in nums]
    if max(tmp) == 3 and len(set(nums)) == 3:
        return 4
    return False

def Two_Pair(card):
    nums = card[0]
    tmp = [nums.count(i) for i in nums]
    if max(tmp) == 2 and len(set(nums)) == 3:
        return 3
    return False

def One_Pair(card):
    nums = card[0]
    tmp = [nums.count(i) for i in nums]
    if max(tmp) == 2 and len(set(nums)) == 4:
        return 2
    return False

def My_Cmp(card1, card2):
    play1 = Royal_Flush(card1)
    if not play1:
        play1 = Straight_Flush(card1)
    if not play1:
        play1 = Four_Kind(card1)
    if not play1:
        play1 = Full_House(card1)
    if not play1:
        play1 = Flush(card1)
    if not play1:
        play1 = Straight(card1)
    if not play1:
        play1 = Three_Kind(card1)
    if not play1:
        play1 = Two_Pair(card1)
    if not play1:
        play1 = One_Pair(card1)
    if not play1:
        play1 = 1
    play2 = Royal_Flush(card2)
    if not play2:
        play2 = Straight_Flush(card2)
    if not play2:
        play2 = Four_Kind(card2)
    if not play2:
        play2 = Full_House(card2)
    if not play2:
        play2 = Flush(card2)
    if not play2:
        play2 = Straight(card2)
    if not play2:
        play2 = Three_Kind(card2)
    if not play2:
        play2 = Two_Pair(card2)
    if not play2:
        play2 = One_Pair(card2)
    if not play2:
        play2 = 1 
    if play1 > play2:
        return True
    elif play1 == play2:
        if play1 == 2:
            m1 = filter(lambda x:card1[0].count(x)==2,card1[0])[0]
            l1 = My_Sort(filter(lambda x:card1[0].count(x) == 1, card1[0]))
            l1.reverse()
            m2 = filter(lambda x:card2[0].count(x)==2,card2[0])[0]
            l2 = My_Sort(filter(lambda x:card2[0].count(x) == 1, card2[0]))
            l2.reverse()
            if cards.index(m1) > cards.index(m2):
                return True
            elif cards.index(m1) == cards.index(m2):
                for i in range(len(l1)):
                    if cards.index(l1[i]) > cards.index(l2[i]):
                        return True
                    elif  cards.index(l1[i]) == cards.index(l2[i]):
                        pass
                    else:
                        return False
            else:
                return False
        elif play1 == 1:
            l1 = My_Sort(card1[0])
            l1.reverse()
            l2 = My_Sort(card2[0])
            l2.reverse()
            for i in range(len(l1)):
                if cards.index(l1[i]) > cards.index(l2[i]):
                    return True
                elif  cards.index(l1[i]) == cards.index(l2[i]):
                    pass
                else:
                    return False
        else:
            return False         
    else:
        return False


if __name__ == '__main__':
    cards = ['2','3','4','5','6','7','8','9','T','J','Q','K','A']
    data = open('poker.txt').readlines()
    total = 0
    for line in data:
        card1 = ([i[0] for i in line.split()[:5]],[i[1] for i in line.split()[:5]])
        card2 = ([i[0] for i in line.split()[5:]],[i[1] for i in line.split()[5:]])
        if My_Cmp(card1, card2):
            total += 1
    print total
