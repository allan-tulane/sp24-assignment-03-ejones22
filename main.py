import math, queue
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
    insertS, insertT = fast_align_MED(S, T[1:], MED)
    deleteS, deleteT = fast_align_MED(S[1:], T, MED)

    insertC = 1 + len(insertS)
    deleteC = 1 + len(deleteS)

    if insertC <= deleteC:
      MED[(S, T)] = ("-" + insertS, T[0] + insertT)
    else:
      MED[(S, T)] = (S[0] + deleteS, "-" + deleteT)

  return MED[(S, T)]


