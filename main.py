import deemb as de
import skrf as rf
import os
import sys
from pathlib import Path

'''
This script applies de-embedding to all files in the "raw" directory at once.
The supported methods are as follows.
- open
- short
- open_short
- short_open
- spliti
- splitpi
- splitt
- icsy
- icsz
- icsyz
- icszy
'''

method = 'open'

# Import raw files
raw_files = os.listdir('./raw')

# Import dummies
if method in {'open'}:
    dummy = (rf.Network('dummy/open.s2p'), )
elif method in {'short'}:
    dummy = (rf.Network('dummy/short.s2p'), )
elif method in {'open_short'}:
    dummy = (rf.Network('dummy/open.s2p'), rf.Network('dummy/short.s2p'))
elif method in {'short_open'}:
    dummy = (rf.Network('dummy/short.s2p'), rf.Network('dummy/open.s2p'))
elif method in {'spliti', 'splitpi', 'splitt', 'icsy', 'icsz', 'icsyz', 'icszy'}:
    dummy = (rf.Network('dummy/thru.s2p'), )
else:
    print('ERROR: No such a de-embedding method.')
    sys.exit()

# Run de-embedding
for raw_file in raw_files:
    raw = rf.Network('./raw/' + raw_file)
    dut = eval('de.' + method)(raw, dummy)
    dut.frequency.unit = 'Hz'
    dut.write_touchstone(filename=(Path(raw_file).stem+'_'+method), dir='./output', form='ri')
    print("'" + (Path(raw_file).stem) + '_' + method + ".s2p';")