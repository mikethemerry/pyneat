"""
pyNEAT
Copyright (C) 2007-2008 Brian Greer

This program is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public License
as published by the Free Software Foundation; either version 2
of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
"""

class Innovation:
   NEURON  = 0
   SYNAPSE = 1

   def __init__(self, inId, outId, weight = 0.0, traitId = -1, oldId = -1, recurrent = False, type=NEURON, idA = -1, idB = -1, newNeuronId = -1):
      self.inId        = inId
      self.outId       = outId
      self.weight      = weight
      self.traitId     = traitId
      self.oldId       = oldId
      self.recurrent   = recurrent
      self.type        = type
      self.idA         = idA
      self.idB         = idB
      self.newNeuronId = newNeuronId
