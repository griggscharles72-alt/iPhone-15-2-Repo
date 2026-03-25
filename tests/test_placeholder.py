import unittest
from drcore_lib import hardware, transport, artifacts, state

class CoreSharedTest(unittest.TestCase):
    def test_scan_devices(self):
        devices = hardware.scan_connected_devices()
        self.assertIsInstance(devices, list)

    def test_serial_ports(self):
        ports = transport.enumerate_serial_ports()
        self.assertIsInstance(ports, list)

    def test_artifact_log(self):
        fname = artifacts.save_log("test", "message")
        self.assertTrue(fname.endswith("test.log"))

    def test_state_record(self):
        state.init_db()
        state.record_device_event("dummy_dev", "connected")
