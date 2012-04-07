import random
import sys

def mimic_dict(flist, limit):
  dict = {}
  """Returns mimic dict mapping each word to list of words which follow it."""
  flist = flist.split()
  for i in range(len(flist) - 1): 
    if dict.get(flist[i]): 
        dict[flist[i]].append(flist[i + 1]) 
    else: 
        dict[flist[i]] = [flist[i + 1]]   
  k = 0
  word = 'the'
  newlist = ['The']
  while k < limit:
    if dict.get(word):
      templist = dict[word]
      word = random.choice(templist)
      newlist.append(word)
    else:
      word = 'the'
    k += 1
  while True:
    if dict.get(word):
      templist = dict[word]
      word = random.choice(templist)
      newlist.append(word)
    else:
      word = 'the'
    if word[-1] == '!' or word == 'Swag' or word == 'swag':
      break
  return ' '.join(newlist)
