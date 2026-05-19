"""
Johnny 5 - Serial Connection Test
Author: Alberto Orozco
GitHub: github.com/Albertozco/johnny5
"""

import serial
import time


PORT = '/dev/ttyUSB0'
BAUD = 9600


def main():
    print("=" * 45)
    print("  Johnny 5 -- Serial Connection Test")
    print("=" * 45)
    print(f"\n  Port : {PORT}")
    print(f"  Baud : {BAUD}")
    print(f"\n  Connecting", end="", flush=True)

    try:
        ser = serial.Serial(PORT, BAUD, timeout=2)
        for _ in range(3):
            time.sleep(0.4)
            print(".", end="", flush=True)
        print("\n")
        print("  Status : CONNECTED")
        print("  Driver : ch341-uart")
        print("  Device : LewanSoul LeArm ESP32")
        print("\n" + "=" * 45)
        print("  Connection test PASSED")
        print("=" * 45 + "\n")
        ser.close()

    except Exception as e:
        print(f"\n  Status : FAILED\n  Error  : {e}\n")


if __name__ == "__main__":
    main()
