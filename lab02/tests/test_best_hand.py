'''
Test the best_hand function.
'''

import sys
from pathlib import Path
sys.path.append(Path(__file__).parents[1])

import itertools
from random import shuffle
from lab02.lab02 import best_hand

def solution(hand):
  pass

def test_best_hand():
  ranks = '23456789TJQKA'
  suite = 'CDHS'
  deck = [r+s for r in ranks for s in suite]
  shuffle(deck)
  for i, hand in enumerate(itertools.combinations(deck, 7)):
    if i == 20:
      break
    assert best_hand(hand) == solution(hand)