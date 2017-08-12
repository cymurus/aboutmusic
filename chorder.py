from tuner import *
import logging
import sys

'''
chord rules according to the pitch interval
'''

CHORD_RULE = {
  # 3
  '': 'Tt', # major chord
  'm': 'tT', # minor chord
  'aug': 'TT', # augmented chord
  'dim': 'tt', # diminished chord
  'sus4': 'fS', # suspended 4
  'sus2': 'fs', # suspended 2
  # 7
  '7': 'TtT', # major chord
  'dom7': 'Ttt', # dominant chord
  'm7': 'tTt', # minor chord
  'hdim7': 'ttT', # minor chord
  'dim7': 'ttt', # minor chord
  '7sus4': 'fSt', # dominant 7 suspended 4,
  '7sus2': 'fst', # dominant 7 suspended 2
}


PITCH_INTERVAL_MAP = {
  's': minor_2nd,
  'S': major_2nd,
  't': minor_3rd,
  'T': major_3rd,
  'f': perfect_4th,
}

'''
check if the chrod name is illegal
'''
def check_chord_name(chord):
  if chord[0] not in TUNE:
    return False
  #illegal tune

  if chord[1:] not in CHORD_RULE:
    return False
  #illegal chord

  return True
#check chord name


'''
output tunes of a chord
'''
def parse_chord(chord):

  if not check_chord_name(chord):
    logging.error('illegal chord: {}'.format(chord))
    return ''
  #illegal

  root = chord[0]
  chord = chord[1:]

  tunes = [root,]

  pis = CHORD_RULE[chord]

  for pi in pis:
    root = PITCH_INTERVAL_MAP[pi](root)
    tunes.append(root)
  #for pis

  return tunes
#parse chord


if __name__ == '__main__':
  
  if len(sys.argv):
    chord_name = sys.argv[1]
    print(" ".join(parse_chord(chord_name)))
