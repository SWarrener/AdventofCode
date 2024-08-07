#My part 2 fails, see further below for something from online. 

def findLocationNumber(targetnum):
    keys = maps.keys()
    
    for key in keys:
        for set in maps[key]:
            source = int(set[1])
            dest = int(set[0])
            modifier = int(set[2])
            if targetnum >= source and targetnum <= source + modifier:
                targetnum = dest + (targetnum-source)
                break

    return targetnum

def findLocationRanges(ranges, key):
    locationranges = []
    for range in ranges:
        highdealt = range[1]
        lowdealt = range[0]
        for set in maps[key]:
            source = int(set[1])
            dest = int(set[0])
            modifier = int(set[2])
            low = range[0]
            high = range[1]
            if low >= source and high <= source+modifier:
                locationranges.append([dest + (low-source), dest + (high-source)])
                highdealt = 0
                lowdealt = 0
                break
            elif (low >= source and low <= source+modifier) and high >= source+modifier:
                locationranges.append([dest + (low-source), dest + modifier])
                lowdealt = source+modifier+1
                continue
            elif low <= source and (high <= source+modifier and high >= source):
                locationranges.append([dest, dest + (high-source)])
                highdealt = source-1
                continue
        if highdealt != lowdealt:
            locationranges.append([lowdealt, highdealt])
    return locationranges

with open("input5.txt") as f:
    seeds = []
    maps = {}
    category = ""
    for line in f.readlines():
        if line[:5] == "seeds":
            seeds = line[7:-1].split(" ")
            continue
        if not line[0].isdigit() and line[0] != "\n":
            category = line[:line.find(" ")]
            maps[category] = []
        if line[0].isdigit():
            nums = line[:-1].split(" ")
            maps[category].append(nums)

lowestlocation = 10000000000

for seed in seeds:
    location = findLocationNumber(int(seed))
    lowestlocation = min(location, lowestlocation)

print(f"The answer to part 1 is: {lowestlocation}")

ranges = [[int(seeds[i]), int(seeds[i])+int(seeds[i+1])] for i in range(0, len(seeds), 2)]

keys = maps.keys()

for key in keys:
    ranges = findLocationRanges(ranges, key)

lowestlocation = 10000000000

for range in ranges:
    lowestlocation = min(range[0], lowestlocation)

print(f"The answer to part 2 is: {lowestlocation}")


import sys
import re
from collections import defaultdict
D = open("input5.txt").read().strip()
L = D.split('\n')

parts = D.split('\n\n')
seed, *others = parts
seed = [int(x) for x in seed.split(':')[1].split()]

class Function:
  def __init__(self, S):
    lines = S.split('\n')[1:] # throw away name
    # dst src sz
    self.tuples: list[tuple[int,int,int]] = [[int(x) for x in line.split()] for line in lines]
    #print(self.tuples)
  def apply_one(self, x: int) -> int:
    for (dst, src, sz) in self.tuples:
      if src<=x<src+sz:
        return x+dst-src
    return x

  # list of [start, end) ranges
  def apply_range(self, R):
    A = []
    for (dest, src, sz) in self.tuples:
      src_end = src+sz
      NR = []
      while R:
        # [st                                     ed)
        #          [src       src_end]
        # [BEFORE ][INTER            ][AFTER        )
        (st,ed) = R.pop()
        # (src,sz) might cut (st,ed)
        before = (st,min(ed,src))
        inter = (max(st, src), min(src_end, ed))
        after = (max(src_end, st), ed)
        if before[1]>before[0]:
          NR.append(before)
        if inter[1]>inter[0]:
          A.append((inter[0]-src+dest, inter[1]-src+dest))
        if after[1]>after[0]:
          NR.append(after)
      R = NR
    return A+R

Fs = [Function(s) for s in others]

P1 = []
for x in seed:
  for f in Fs:
    x = f.apply_one(x)
  P1.append(x)
print(min(P1))

P2 = []
pairs = list(zip(seed[::2], seed[1::2]))
for st, sz in pairs:
  # inclusive on the left, exclusive on the right
  # e.g. [1,3) = [1,2]
  # length of [a,b) = b-a
  # [a,b) + [b,c) = [a,c)
  R = [(st, st+sz)]
  for f in Fs:
    R = f.apply_range(R)
  #print(len(R))
  P2.append(min(R)[0])
print(min(P2))