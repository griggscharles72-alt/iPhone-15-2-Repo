from drcore_lib import hardware, artifacts, state, logging

state.init_db()
devices = hardware.scan_connected_devices()
print("Connected devices:")
for d in devices:
    print(d)

artifacts.save_log("scan_example", f"Devices found: {len(devices)}")
logging.log_info("Example scan completed")
