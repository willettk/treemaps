#!/usr/bin/python
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

import sys, os

def load(input):
  data = []
  f = open(input, 'r')  
  for line in f:
    line = line.rstrip()   
    array = line.rsplit()
    data.append({'name'  : ' '.join(array[0:len(array)-1]),
                 'value'  : float(array[len(array)-1])})
  f.close()
  return data


def save(output, data):
  f = open(output, 'w')
  print >>f, "data = [" 
  for record in data:
    print >>f, "{ 'name' : '%(name)s', 'value' : %(value)f	}," \
               % { 'name': record['name'], 'value': record['value'] }
  print >>f, "      ]"
  f.close()


def compare(x, y):
  if x['value'] > y['value']:
    return 1
  elif x['value'] == y['value']:
    return 0
  else:  #x['value'] < y['value']
    return -1
 

#
# M A I N
#

inputfile = sys.argv[1]
outputfile = inputfile+'.py'

data = load(inputfile)

data.sort(compare);

save(outputfile, data)

os.system('bash treemap.sh '+outputfile)
