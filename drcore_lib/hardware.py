import os
import subprocess

def scan_connected_devices():
    devices = []
    try:
        usb_out = subprocess.check_output(["lsusb"]).decode()
        devices.extend(usb_out.strip().split('\n'))
    except:
        devices.append("USB scan failed")
    try:
        serials = [f"/dev/{p}" for p in os.listdir("/dev") if "tty" in p]
        devices.extend(serials)
    except:
        devices.append("Serial scan failed")
    try:
        can_out = subprocess.check_output(["ip","link"]).decode()
        can_ifaces = [line.split(":")[1].strip() for line in can_out.splitlines() if "can" in line]
        devices.extend(can_ifaces)
    except:
        devices.append("CAN scan failed")
    return devices
