"""
Johnny 5 - LewanSoul LX-224 Serial Bus Servo Control
Author: Alberto Orozco
GitHub: github.com/Albertozco/johnny5

Hardware:
- CP2102 USB to TTL adapter on /dev/ttyUSB1
- LX-224 servo bus data line connected to TX and RX (half duplex)
- Common ground between adapter and arm power supply
- Arm powered by 7.5V 6A adapter

Protocol:
Packet format: 0x55 0x55 ID LENGTH CMD [PARAMS] CHECKSUM
Baud rate: 9600
Position range: 0 to 1000 (500 = center)
Time in milliseconds

Servo ID Map (verify with manual):
1 = Base rotation
2 = Shoulder
3 = Elbow
4 = Wrist pitch
5 = Wrist rotation
6 = Gripper
"""

import serial
import time

# Serial port config
PORT = '/dev/ttyUSB1'
BAUD = 9600

# LX-224 command codes
CMD_MOVE = 1

# Servo IDs
SERVO_BASE        = 1
SERVO_SHOULDER    = 2
SERVO_ELBOW       = 3
SERVO_WRIST_PITCH = 4
SERVO_WRIST_ROT   = 5
SERVO_GRIPPER     = 6

# Position constants
POS_CENTER = 500
POS_MIN    = 0
POS_MAX    = 1000


def checksum(data):
    """LX-224 checksum: bitwise NOT of sum of data bytes, take low byte."""
    return (~sum(data)) & 0xFF


def build_packet(servo_id, cmd, params):
    """Build a complete LX-224 command packet."""
    length = len(params) + 3
    data = [servo_id, length, cmd] + params
    cs = checksum(data)
    return bytes([0x55, 0x55] + data + [cs])


def move_servo(ser, servo_id, position, time_ms=1000):
    """
    Move a single servo to a target position.

    Args:
        ser:      open serial.Serial object
        servo_id: servo ID 1 through 6
        position: target position 0 to 1000 (500 = center)
        time_ms:  move duration in milliseconds
    """
    position = max(POS_MIN, min(POS_MAX, position))
    params = [
        position & 0xFF,
        (position >> 8) & 0xFF,
        time_ms & 0xFF,
        (time_ms >> 8) & 0xFF
    ]
    packet = build_packet(servo_id, CMD_MOVE, params)
    ser.write(packet)
    print(f"  Servo {servo_id} -> position {position} in {time_ms}ms | {packet.hex()}")


def home_all(ser):
    """Send all servos to center position."""
    print("\nHoming all servos to center...")
    for servo_id in range(1, 7):
        move_servo(ser, servo_id, POS_CENTER, 1500)
        time.sleep(0.1)
    print("Home command sent. Wait for motion to complete.")


def test_single_joint(ser, servo_id=1):
    """
    Test a single joint by moving it off center and back.
    Start with servo 1 (base) as it is safest to observe.
    """
    print(f"\nTesting servo {servo_id}...")
    print("  Moving to 600...")
    move_servo(ser, servo_id, 600, 1000)
    time.sleep(1.5)
    print("  Moving back to center 500...")
    move_servo(ser, servo_id, 500, 1000)
    time.sleep(1.5)
    print("  Test complete.")


def main():
    print("=" * 45)
    print("  Johnny 5 - Servo Control")
    print("=" * 45)
    print(f"\n  Port : {PORT}")
    print(f"  Baud : {BAUD}\n")

    try:
        ser = serial.Serial(PORT, BAUD, timeout=1)
        time.sleep(0.1)
        print("  Status : CONNECTED\n")

        # Test base joint first - safest to observe
        test_single_joint(ser, servo_id=SERVO_BASE)

        # Uncomment to home all servos
        # home_all(ser)

        ser.close()
        print("\n" + "=" * 45)
        print("  Done. Serial port closed.")
        print("=" * 45 + "\n")

    except serial.SerialException as e:
        print(f"\n  Serial error: {e}")
        print("  Check /dev/ttyUSB1 exists and permissions are set.")
        print("  Run: sudo chmod 666 /dev/ttyUSB1\n")


if __name__ == "__main__":
    main()
