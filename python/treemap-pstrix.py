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
import random
 

def load(input):
  data = []

  f = open(input, 'r')
  f.readline()
  
  for line in f:
    line = line.rstrip()   
    array = line.split('\t')

    data.append({
      'name'  : array[0].rstrip(),
      'left'  : float(array[1]),
      'top'   : float(array[2]),
      'width' : float(array[3]),
      'height': float(array[4])
    })
    
  f.close()
  
  return(data)


def save(output, data, w, h):
  
  f = open(output, 'w')

  print >>f, '''
  \\documentclass[]{article}
  \\RequirePackage{pstricks}
  \\usepackage{pst-all}      
  \\renewcommand\\familydefault{\\sfdefault}
  \\begin{document}
    \\noindent
    \\thispagestyle{empty}
    \\begin{center}
    \\begin{pspicture}(%(w)d,%(h)d)
  ''' % { 'w': w, 'h': h} 

  for box in data:    
    name = box['name']
    texname = name.replace("_","\\_")
                 
    L = box['left']
    T = h - box['top']
    R = box['left'] + box['width']
    B = h - (box['top'] + box['height'])
  
    rnd = random.random()
    color1 = 0.5 + 0.5 * rnd
    color2 = 0.4 + 0.4 * rnd
    
    if box['width'] > box['height']:
      TX = L + 0.1
      TY = T - 0.1
      rot = 0
    else:
      TX = L + 0.1
      TY = B + 0.1
      rot = 90
      
    print >>f, '''
     \\newrgbcolor{color1%(name)s}{%(color1)f %(color1)f 1}
     \\newrgbcolor{color2%(name)s}{%(color2)f %(color2)f 1}
     \\psframe[linewidth=0.5pt,
               fillstyle=gradient,
               gradangle=0,
               gradbegin=color1%(name)s,
               gradend=color2%(name)s](%(L)f,%(T)f)(%(R)f,%(B)f) 
     \\psclip{\\psframe[linestyle=none](%(L)f,%(T)f)(%(R)f,%(B)f)}
     \\rput[tl]{%(rot)f}(%(TX)f,%(TY)f){\\tiny %(texname)s}
     \\endpsclip  
    ''' % { 'name': name,
            'texname': texname,
            'color1': color1, 
            'color2': color2,
            'L': L, 'T': T,
            'R': R, 'B': B, 
            'TX': TX, 'TY': TY, 
            'rot': rot}

  print >>f, """
    \\end{pspicture}
    \\end{center}
  \\end{document}
  """

  f.close()


#
#   M A I N
#

input   = sys.argv[1]
output  = sys.argv[2]
w       = float(sys.argv[3])
h       = float(sys.argv[4])
#input   = 'test.csv'
#output  = 'test.tex'
#w       = 14
#h       = 14

data = load(input)

save(output, data, w, h)
