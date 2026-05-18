# Johnny 5 — AI Automation Testbed

A 6 degree of freedom robotic arm wired to industrial-grade data acquisition hardware and controlled by Python. Not a demo. A repeatable, open architecture for intelligent automation that translates directly to real production environments.

## The Problem

After 15 years in manufacturing across semiconductor, medical device, and automotive environments, the pattern is always the same. Millions of dollars in equipment. Intelligence layer almost nowhere. Operators making decisions based on gut feel because the system was never designed to tell them anything useful.

This project is where that changes.

## Hardware

| Component | Details |
|-----------|---------|
| LewanSoul LeArm | 6DOF open source robotic arm, serial bus servos (LX-224) |
| NI cDAQ-9174 | USB DAQ chassis |
| NI 9205 | 32-channel 16-bit analog input |
| NI 9485 | 8-channel solid state relay |
| NI 9401 | Digital I/O |
| NI 9263 | 4-channel analog output |
| ESP32 controller | Serial bus communication, 7.5V 6A power |
| Tugboat | Custom build — i7-7700K, 64GB RAM, RTX 3090, Ubuntu 22.04 |

## Software Stack

- Python 3.10
- pyserial — serial bus servo control
- nidaqmx — NI DAQ integration (coming)
- OpenCV — computer vision layer (coming)

## Build Roadmap

- [x] Phase 0 — Hardware assembly and mechanical verification
- [x] Phase 0 — Serial connection established (ttyUSB0, 9600 baud)
- [ ] Phase 1 — Python serial control of all 6 joints, homing routine, waypoints
- [ ] Phase 2 — NI DAQmx integration layer
- [ ] Phase 3 — Force feedback via NI 9219 and load cell on gripper
- [ ] Phase 4 — Computer vision, OpenCV, object detection, pick and place
- [ ] Phase 5 — Anomaly detection via NI 9234, vibration signature monitoring
- [ ] Phase 6 — Full closed loop system — sees, decides, acts autonomously

## Project Structure

```
johnny5/
└── src/
    ├── test_connection.py   # Serial connection verification
    └── servo_control.py     # LX-224 servo control — Phase 1
```

## Follow the Build

This is not a highlight reel. Every step is documented honestly including the learning curve.

LinkedIn: [Alberto Orozco](https://www.linkedin.com/in/alberto-orozco-21113166/)

---

*The people who spend their weekends turning ideas into something real in a home lab are the ones who walk into Monday with something nobody can teach in a classroom.*
