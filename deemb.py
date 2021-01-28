'''De-embed touchstone'''

import skrf as rf
import numpy as np

# Open method
def open(raw, dummy):
    open = dummy[0]
    y_dut = raw.y - open.y
    dut = rf.Network(s=rf.y2s(y_dut), z0=raw.z0, frequency=raw.frequency)
    return dut

# Short method
def short(raw, dummy):
    short = dummy[0]
    z_dut = raw.z - short.z
    dut = rf.Network(s=rf.z2s(z_dut), z0=raw.z0, frequency=raw.frequency)
    return dut

# Open_short method
def open_short(raw, dummy):
    open_dummy = (dummy[0], )
    short_dummy = (dummy[1], )
    dut = open(raw, open_dummy)
    dut = short(dut, short_dummy)
    return dut

# Open_short method
def short_open(raw, dummy):
    short_dummy = (dummy[0], )
    open_dummy = (dummy[1], )
    dut = short(raw, short_dummy)
    dut = open(dut, open_dummy)
    return dut

# Split-I method
def spliti(raw, dummy):
    thru = dummy[0]
    n = raw.frequency.f.shape[0]
    z_left = np.empty((n,2,2), dtype=complex)
    z_left[:,0,0] = (2 * thru.z[:,0,0] + 2 * thru.z[:,0,1] + 2 * thru.z[:,1,0] + 2 * thru.z[:,1,1]) / 4
    z_left[:,0,1] = (2 * thru.z[:,0,0] + 2 * thru.z[:,0,1] + 2 * thru.z[:,1,0] + 2 * thru.z[:,1,1]) / 4
    z_left[:,1,0] = (2 * thru.z[:,0,0] + 2 * thru.z[:,0,1] + 2 * thru.z[:,1,0] + 2 * thru.z[:,1,1]) / 4
    z_left[:,1,1] = (2 * thru.z[:,0,0] + 2 * thru.z[:,0,1] + 2 * thru.z[:,1,0] + 2 * thru.z[:,1,1]) / 4
    left = rf.Network(s=rf.z2s(z_left), z0=raw.z0, frequency=raw.frequency)
    right = left.flipped()
    dut = left.inv ** raw ** right.inv
    return dut

# Split-Pi method
def splitpi(raw, dummy):
    thru = dummy[0]
    n = raw.frequency.f.shape[0]
    y_left = np.empty((n,2,2), dtype=complex)
    y_left[:,0,0] = (thru.y[:,0,0] - thru.y[:,1,0] + thru.y[:,1,1] - thru.y[:,0,1]) / 2
    y_left[:,0,1] = (2 * thru.y[:,1,0] + 2 * thru.y[:,0,1]) / 2
    y_left[:,1,0] = (2 * thru.y[:,1,0] + 2 * thru.y[:,0,1]) / 2
    y_left[:,1,1] = (- 2 * thru.y[:,1,0] - 2 * thru.y[:,0,1]) / 2
    left = rf.Network(s=rf.y2s(y_left), z0=raw.z0, frequency=raw.frequency)
    right = left.flipped()
    dut = left.inv ** raw ** right.inv
    return dut

# Split-T method
def splitt(raw, dummy):
    thru = dummy[0]
    n = raw.frequency.f.shape[0]
    z_left = np.empty((n,2,2), dtype=complex)
    z_left[:,0,0] = (thru.z[:,0,0] + thru.z[:,1,0] + thru.z[:,1,1] + thru.z[:,0,1]) / 2
    z_left[:,0,1] = (2 * thru.z[:,1,0] + 2 * thru.z[:,0,1]) / 2
    z_left[:,1,0] = (2 * thru.z[:,1,0] + 2 * thru.z[:,0,1]) / 2
    z_left[:,1,1] = (2 * thru.z[:,1,0] + 2 * thru.z[:,0,1]) / 2
    left = rf.Network(s=rf.z2s(z_left), z0=raw.z0, frequency=raw.frequency)
    right = left.flipped()
    dut = left.inv ** raw ** right.inv
    return dut

# ICS(Imittance Cancellation by Swapping)-Y method
def icsy(raw, dummy):
    thru = dummy[0]
    h = raw ** thru.inv
    h_ = h.flipped()
    y_dut = (h.y + h_.y) / 2
    dut = rf.Network(s=rf.y2s(y_dut), z0=raw.z0, frequency=raw.frequency)
    return dut

# ICS-Z method
def icsz(raw, dummy):
    thru = dummy[0]
    h = raw ** thru.inv
    h_ = h.flipped()
    z_dut = (h.z + h_.z) / 2
    dut = rf.Network(s=rf.z2s(z_dut), z0=raw.z0, frequency=raw.frequency)
    return dut

# ICS-YZ method
def icsyz(raw, dummy):
    thru = dummy[0]
    acs = icsy(raw, thru)
    ics = icsz(raw, thru)
    y_dut = (acs.y + ics.y) / 2
    dut = rf.Network(s=rf.y2s(y_dut), z0=raw.z0, frequency=raw.frequency)
    return dut

# ICS-ZY method
def icszy(raw, dummy):
    thru = dummy[0]
    acs = icsy(raw, thru)
    ics = icsz(raw, thru)
    z_dut = (acs.z + ics.z) / 2
    dut = rf.Network(s=rf.z2s(z_dut), z0=raw.z0, frequency=raw.frequency)
    return dut

# L2L method, which return thru network.
def l2l(line, line2):
    thru = line ** line2.inv ** line
    return thru