import logging

# 12 equal temperament
TUNE = [
  'C',
  'C#',
  'D',
  'D#',
  'E',
  'F',
  'F#',
  'G',
  'G#',
  'A',
  'A#',
  'B',
]

'''
to change a tune by offset
'''
def tuner(root, offset):

  ltune = len(TUNE)

  if (abs(offset) not in range(0, ltune + 1)):
    logging.error('illegal offset: {}'.format(offset))
    return root
  #if not [1, 12]

  try:
    root = root.upper()
    old_idx = TUNE.index(root)
  except:
    print('illegal root: {}'.format(root))
    return root
  #try

  new_idx = (old_idx + offset + ltune) % ltune
  return TUNE[new_idx]
#tuner


'''
some specifical pitch intervals
'''

def perfect_1st(root):
  return tuner(root, 0)
# perfect_1st

def minor_2nd(root):
  return tuner(root, 1)
# minor_2nd

def major_2nd(root):
  return tuner(root, 2)
# major_2nd

def minor_3rd(root):
  return tuner(root, 3)
# minor_3rd

def major_3rd(root):
  return tuner(root, 4)
# major_3rd

def perfect_4th(root):
  return tuner(root, 5)
# perfect_4th

def augmented_4th(root):
  return tuner(root, 6)
# augmented_4th

def diminished_5th(root):
  return tuner(root, 6)
# diminished_5th

def perfect_5th(root):
  return tuner(root, 7)
# perfect_5th

def minor_6th(root):
  return tuner(root, 8)
# minor_6th

def major_6th(root):
  return tuner(root, 9)
# major_6th

def minor_7th(root):
  return tuner(root, 10)
# minor_7th

def major_7th(root):
  return tuner(root, 11)
# major_7th

def perfect_8th(root):
  return tuner(root, 12)
# perfect_8th


if __name__ == '__main__':
  print(tuner('C', -2))
  print(perfect_4th('C#'))
  print(minor_3rd('D'))
