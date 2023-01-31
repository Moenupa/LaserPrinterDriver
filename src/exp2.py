
# Generated by usbrply
# cmd: .\env\Scripts\usbrply --wrapper --setup -p .\usbcap\exp3_loc.pcapng

import binascii
import time
import usb1
from usb1 import USBDeviceHandle

ALLOW_TIMEOUT = 2000


def validate_read(expected, actual, msg):
    if expected != actual:
        print('Failed %s' % msg)
        print('  Expected; %s' % binascii.hexlify(expected,))
        print('  Actual:   %s' % binascii.hexlify(actual,))
        #raise Exception('failed validate: %s' % msg)


def replay(dev: USBDeviceHandle):
    def bulkRead(endpoint, length, timeout=None):
        return dev.bulkRead(endpoint, length, timeout=(ALLOW_TIMEOUT if timeout is None else timeout))

    def bulkWrite(endpoint, data, timeout=None):
        dev.bulkWrite(endpoint, data, timeout=(ALLOW_TIMEOUT if timeout is None else timeout))
    
    def controlRead(bRequestType, bRequest, wValue, wIndex, wLength,
                    timeout=None):
        return dev.controlRead(bRequestType, bRequest, wValue, wIndex, wLength,
                    timeout=(ALLOW_TIMEOUT if timeout is None else timeout))

    def controlWrite(bRequestType, bRequest, wValue, wIndex, data,
                     timeout=None):
        dev.controlWrite(bRequestType, bRequest, wValue, wIndex, data,
                     timeout=(ALLOW_TIMEOUT if timeout is None else timeout))

    def interruptRead(endpoint, size, timeout=None):
        return dev.interruptRead(endpoint, size,
                    timeout=(ALLOW_TIMEOUT if timeout is None else timeout))

    def interruptWrite(endpoint, data, timeout=None):
        dev.interruptWrite(endpoint, data, timeout=(ALLOW_TIMEOUT if timeout is None else timeout))

    # Generated by usbrply
    # Source: Windows pcap (USBPcap)
    # cmd: .\env\Scripts\usbrply --wrapper --setup -p .\usbcap\exp3_loc.pcapng
    # PCapGen device hi: selected device 5
    # Generated from packet 25/26
    controlWrite(0x40, 0xA1, 0xC39C, 0xCC8B, b"")
    # Generated from packet 27/28
    controlWrite(0x40, 0x9A, 0x0F2C, 0x0007, b"")
    # Generated from packet 29/30
    controlWrite(0x40, 0xA4, 0x00DF, 0x0000, b"")
    # Generated from packet 31/32
    controlWrite(0x40, 0xA4, 0x009F, 0x0000, b"")
    # Generated from packet 33/34
    buff = controlRead(0xC0, 0x95, 0x0706, 0x0000, 2)
    validate_read(b"\x9F\xEE", buff, "packet 33/34")
    # Generated from packet 35/36
    controlWrite(0x40, 0x9A, 0x2727, 0x0000, b"")
    # Generated from packet 37/38
    buff = controlRead(0xC0, 0x95, 0x0706, 0x0000, 2)
    validate_read(b"\x9F\xEE", buff, "packet 37/38")
    # Generated from packet 39/40
    controlWrite(0x40, 0x9A, 0x2727, 0x0000, b"")
    # Generated from packet 41/42
    bulkWrite(0x02, b"\x0A\x00\x04\x00")
    # WARNING: Packet 43 missing submit.  URB ID: 0xFFFFC70D18915A20
    # Generated from packet 45/46
    bulkWrite(0x02, b"\xFF\x00\x04\x00")
    # Generated from packet 44/47
    buff = bulkRead(0x82, 0x0003)
    validate_read(b"\x04\x00\x24", buff, "packet 44/47")
    # Generated from packet 49/50
    bulkWrite(0x02, b"\x28\x00\x0B\x14\x00\x00\x00\x00\x00\x00\x00")
    # Generated from packet 48/51
    buff = bulkRead(0x82, 0x0001)
    validate_read(b"\x09", buff, "packet 48/51")
    # Generated from packet 53/54
    bulkWrite(0x02, b"\x20\x00\x0B\x01\x97\x01\x98\x00\xD8\x00\xE6")
    # Generated from packet 52/55
    buff = bulkRead(0x82, 0x0001)
    validate_read(b"\x09", buff, "packet 52/55")
    # Generated from packet 57/58
    bulkWrite(0x02, b"\x21\x00\x04\x00")
    # Generated from packet 56/59
    # buff = bulkRead(0x82, 0x0001)
    # validate_read(b"\x09", buff, "packet 56/59")
    # Generated from packet 61/62
    buff = controlRead(0xC0, 0x95, 0x0706, 0x0000, 2)
    validate_read(b"\x9F\xEE", buff, "packet 61/62")
    # Generated from packet 63/64
    controlWrite(0x40, 0xA4, 0x00FF, 0x0000, b"")
    # WARNING: 1 pending complete requests
    # PcapGen: generated 65 packets
    # PcapGen device filter: dropped 24 / 65 packets

def open_dev(usbcontext=None):
    if usbcontext is None:
        usbcontext = usb1.USBContext()
    
    print('Scanning for devices...')
    for udev in usbcontext.getDeviceList(skip_on_error=False):
        vid = udev.getVendorID()
        pid = udev.getProductID()
        if (vid, pid) == (0x1a86, 0x7523):
            print("")
            print('Found device')
            print('Bus %03i Device %03i: ID %04x:%04x' % (
                udev.getBusNumber(),
                udev.getDeviceAddress(),
                vid,
                pid))
            return udev.open()
    raise Exception("Failed to find a device")

if __name__ == "__main__":
    import argparse 
    
    parser = argparse.ArgumentParser(description='Replay captured USB packets')
    args = parser.parse_args()

    usbcontext = usb1.USBContext()
    dev = open_dev(usbcontext)
    dev.claimInterface(0)
    dev.resetDevice()
    replay(dev)


