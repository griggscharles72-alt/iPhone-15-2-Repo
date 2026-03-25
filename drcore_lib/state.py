import os
import sqlite3

STATE_DB = os.path.join(os.getcwd(), "state", "state.db")

def init_db():
    os.makedirs(os.path.dirname(STATE_DB), exist_ok=True)
    conn = sqlite3.connect(STATE_DB)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS device_events
                 (timestamp TEXT, device_id TEXT, event TEXT)''')
    conn.commit()
    conn.close()

def record_device_event(device_id, event):
    conn = sqlite3.connect(STATE_DB)
    c = conn.cursor()
    c.execute("INSERT INTO device_events VALUES (datetime('now'),?,?)", (device_id,event))
    conn.commit()
    conn.close()
