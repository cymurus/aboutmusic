from tuner import *
import logging
import sys

'''
TODO:
(资料来源于 https://www.douban.com/group/topic/11563595/)
1 伊奥尼亚音阶（自然大调） 1 2 3 4 5 6 7 1 
2 多利亚音阶 1 2 b3 4 5 6 b7 1 
3 弗利几亚音阶 1 b2 b3 4 5 b6 b7 1 
4 利底亚音阶 1 2 3 #4 5 6 7 1 
5 混合利底亚音阶 1 2 3 4 5 6 b7 1 
6 爱奥利亚音阶（自然小调） 1 2 b3 4 5 b6 b7 1 
7 洛克里亚音阶 1 b2 b3 4 b5 b6 b7 1 
8 大调五声音阶 1 2 3 5 6 
9 小调五声音阶 1 b3 4 5 b7 1 
10 和声小调音阶 1 2 b3 4 5 b6 7 1 
11 全半减音阶 1 2 b3 4 b5 b6 bb7 7 1 
12 半全减音阶 1 b2 b3 3 b5 5 6 b7 1 
13 全音音阶 1 2 3 #4 #5 #6 
14 布鲁斯音阶 1 b3 4 b5 5 b7 1 
15 混合布鲁斯音阶 1 b3 3 4 b5 5 b7 1 
16 大弗利几亚音阶 （弗拉门戈） 1 b2 3 4 5 b6 b7 1 
17 大利底亚音阶 1 2 3 #4 5 6 b7 1 
18 超级洛克里亚音阶（alter） 1 b2 b3 b4 b5 b6 b7 1 
19 旋律大调音阶 1 2 3 4 5 b6 b7 1 
20 吉普赛音阶 1 b3 #4 5 b6 b7 1 
21 匈牙利音阶 1 #2 3 #4 5 6 b7 1 
22 匈牙利小调音阶 1 2 b3 #4 5 b6 7 1 
23 Jazz Bebop属音阶 1 2 3 4 5 6 b7 7 i 
24 辅助布鲁斯音阶 1 2 b3 3 4 #4 5 6 b7 i 
25 旋律小调音阶 1 2 b3 4 5 6 7 i 
26 和声大调音阶 1 2 3 4 5 b6 7 i 
27 日本音阶 1 b2 4 5 b7 i 
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