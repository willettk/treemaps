"""
Copyright (C) 2010 Laszlo Simon

This file is part of Treemap.

Treemap is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

Treemap is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with Treemap. If not, see <http://www.gnu.org/licenses/>.

Author : Laszlo Simon <laszlo.simon@gmail.com>
"""

import sys

from math import sqrt


def calcsum(ref):
  """ Calculates the sum of value fields in a complex structure,
      where complex structure means multiple arrays of dicts """ 
  sum = 0
  if type(ref) is list:
    for i in ref:
      sum += calcsum(i)  
  
  elif type(ref) is dict:
    sum = ref['value']
  
  return sum


def divide(datas, O, A, B, sum, f):
  """ Divides the box specified with O corner and A, B side vectors 
      recursively """
  if (type(datas[0]) is dict) and (len(datas) == 1):
    datas[0]['O'] = O
    datas[0]['A'] = A
    datas[0]['B'] = B
    
    w = datas[0]['A'][0] + datas[0]['B'][0]
    h = datas[0]['A'][1] + datas[0]['B'][1]
      
    print >>f, \
          datas[0]['name'],'\t',\
          datas[0]['O'][0],'\t',\
          datas[0]['O'][1],'\t',\
          w,'\t',h

  elif (len(datas) == 1) and (type(datas[0]) is list):
    divide(datas[0],O,A,B,sum,f)
  else:
    datas0 = []
    datas1 = []
        
    a = sqrt(A[0]**2 + A[1]**2)
    b = sqrt(B[0]**2 + B[1]**2)
    
    a0 = 0
    i  = 0
        
    while ((i == 0) or (a0 < (b * 0.4))) and (i < len(datas)-1):
      itemsum = calcsum(datas[i])
      a0 += itemsum / sum / b
      datas0.append(datas[i])
      i += 1
        
    for i in range(i,len(datas)):
      datas1.append(datas[i])

    Onew = O
    Anew = B
    Bnew = [ a0 * A[0] / a, a0 * A[1] / a ]
 
    if (b > a0):
      divide(datas0, O, Anew, Bnew, sum, f)
    else:
      divide(datas0, O, Bnew, Anew, sum, f)    

    Onew = [ O[0] + a0 * A[0] / a, O[1] + a0 * A[1] / a ]
    Anew = B
    Bnew = [ (a - a0) * A[0] / a, (a - a0) * A[1] / a ]

    if (b > (a - a0)):
      divide(datas1, Onew, Anew, Bnew, sum, f)
    else:
      divide(datas1, Onew, Bnew, Anew, sum, f)


#
#   M A I N 
#

infile  = sys.argv[1]
outfile = sys.argv[2]
width   = float(sys.argv[3])
height  = float(sys.argv[4])

execfile(infile)

sum = calcsum(data);

f = open(outfile, 'w');

print >>f, "Name\tLeft\tTop\tWidth\tHeight";

O = [0, 0]
A = [width, 0]
B = [0, height]

divide(data, O, A, B, sum/(width*height), f);

f.close();
