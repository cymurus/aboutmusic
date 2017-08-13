from tuner import *
import logging
import sys

'''
TODO:
(资料来源于 https://www.douban.com/group/topic/11563595/)
伊奥尼亚音阶（自然大调） C D E F G A B C 
多利亚音阶 C D D# F G A A# C 
弗利几亚音阶 C C# D# F G G# A# C 
利底亚音阶 C D E F# G A B C 
混合利底亚音阶 C D E F G A A# C 
爱奥利亚音阶（自然小调） C D D# F G G# A# C 
洛克里亚音阶 C C# D# F F# G# A# C 
大调五声音阶 C D E G A 
小调五声音阶 C D# F G A# C 
和声小调音阶 C D D# F G G# B C 
全半减音阶 C D D# F F# G# A B C 
半全减音阶 C C# D# E F# G A A# C 
全音音阶 C D E F# G# A# 
布鲁斯音阶 C D# F F# G A# C 
混合布鲁斯音阶 C D# E F F# G A# C 
大弗利几亚音阶 （弗拉门戈） C C# E F G G# A# C 
大利底亚音阶 C D E F# G A A# C 
超级洛克里亚音阶（alter） C C# D# E F# G# A# C 
旋律大调音阶 C D E F G G# A# C 
吉普赛音阶 C D# F# G G# A# C 
匈牙利音阶 C D# E F# G A A# C 
匈牙利小调音阶 C D D# F# G G# B C 
Jazz Bebop属音阶 C D E F G A A# B C 
辅助布鲁斯音阶 C D D# E F F# G A A# C 
旋律小调音阶 C D D# F G A B C 
和声大调音阶 C D E F G G# B C 
日本音阶 C C# F G A# C 
'''



SCALES = {
  'M': [0, 2, 4, 5, 7, 9, 11], # natural major mode
  'm': [9, 11, 0, 2, 4, 5, 7], # natural minor mode
  '5': [0, 2, 4, 7, 9], # five-tone scale
}




def check_scale_name(scale):
  if scale[0] not in TUNE:
    return False
  #illegal tune

  if scale[1:] not in SCALES:
    return False
  #illegal scale

  return True
#check scale



def parse_scale(scale):

  if not check_scale_name(scale):
    logging.error('illegal scale: {}'.format(scale))
    return ''
  #illegal

  tunes = []

  keynote = scale[0]
  mode = scale[1:]
  ltune = len(TUNE)

  for i in SCALES[mode]:
    k_idx = TUNE.index(keynote)
    new_idx = (k_idx + i) % ltune
    tunes.append(TUNE[new_idx])

  return tunes
#parse scale


if __name__ == '__main__':
  if len(sys.argv):
    scale = sys.argv[1]
    print(" ".join(parse_scale(scale)))