import math
import queue
from collections import Counter

####### Problem 3 #######

test_cases = [('book', 'back'), ('kookaburra', 'kookybird'), ('elephant', 'relevant'), ('AAAGAATTCA', 'AAATCA')]
alignments = [('b--ook', 'bac--k'), ('kook-ab-urr-a', 'kooky-bi-r-d-'), ('relev--ant','-ele-phant'), ('AAAGAATTCA', 'AAA---T-CA')]

def MED(S, T):
    # TO DO - modify to account for insertions, deletions and substitutions
    if (S == ""):
        return(len(T))
    elif (T == ""):
        return(len(S))
    else:
        if (S[0] == T[0]):
            return(MED(S[1:], T[1:]))
        else:
            return(1 + min(MED(S, T[1:]), MED(S[1:], T)))


def fast_MED(S, T, MED={}):
  if (S, T) in MED:
    return MED[(S, T)]

  if S == "":
    return len(T)

  elif T == "":
    return len(S)
    
  elif S[0] == T[0]:
    x = fast_MED(S[1:], T[1:], MED)
    
  else:
    insert_cost = fast_MED(S, T[1:], MED)
    delete_cost = fast_MED(S[1:], T, MED)
    
    x = min(insert_cost, delete_cost) + 1
    MED[(S, T)] = x
  return x

def fast_align_MED(S, T, MED={}):
  if (S, T) in MED:
      return MED[(S, T)]

  elif T == "":
      MED[(S, T)] = (S, "-" * len(S))
  elif S == "":
      MED[(S, T)] = ("-" * len(T), T)

  elif S[0] == T[0]:
      align_S, align_T = fast_align_MED(S[1:], T[1:], MED)
      MED[(S, T)] = (S[0] + align_S, T[0] + align_T)
  else:
      insert_S, insert_T = fast_align_MED(S, T[1:], MED)
      delete_S, delete_T = fast_align_MED(S[1:], T, MED)

      ins_cost = 1 + len(insert_S)
      del_cost = 1 + len(delete_S)

      if ins_cost <= del_cost:
          MED[(S, T)] = ("-" + insert_S, T[0] + insert_T)
      else:
          MED[(S, T)] = (S[0] + delete_S, "-" + delete_T)

  return MED[(S, T)]

def test_align():
  for i in range(len(test_cases)):
    S, T = test_cases[i]
    align_S, align_T = fast_align_MED(S, T)
    print(align_S == alignments[i][0] and align_T == alignments[i][1])


test_align()

