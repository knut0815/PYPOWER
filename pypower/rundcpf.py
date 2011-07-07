# Copyright (C) 1996-2011 Power System Engineering Research Center
# Copyright (C) 2010-2011 Richard Lincoln
#
# PYPOWER is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published
# by the Free Software Foundation, either version 3 of the License,
# or (at your option) any later version.
#
# PYPOWER is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with PYPOWER. If not, see <http://www.gnu.org/licenses/>.

"""Runs a DC power flow.
"""

from ppoption import ppoption
from runpf import runpf


def rundcpf(casedata='case9', ppopt=None, fname='', solvedcase=''):
    """Runs a DC power flow.

    @see: L{runpf}
    """
    ## default arguments
    ppopt = ppoption(ppopt, PF_DC=True)

    return runpf(casedata, ppopt, fname, solvedcase)
