#!/bin/bash
# Copyright (C) 2010 Laszlo Simon
#
# This file is part of Treemap.
#
# Treemap is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Treemap is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Treemap. If not, see <http://www.gnu.org/licenses/>.
#
# Author : Laszlo Simon <laszlo.simon@gmail.com>

name=$1

w=14
h=14

python python/treemap-engine.py $name csv/$name.csv $w $h
python python/treemap-pstrix.py csv/$name.csv tex/$name.tex $w $h
# latex $name.tex
# dvips $name.dvi
# eps2eps $name.ps $name.eps
# ps2pdf $name.ps
