#
# tun interface implementation for i2p.tun
#

try:
    import pytun
except ImportError:
    print("no module pytun, i2p.tun won't work without it")
    raise

def opentun(ifname):
    return pytun.TunTapDevice(ifname)
