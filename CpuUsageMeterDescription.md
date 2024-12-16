# CpuUsageMeter

## Description

**CpuUsageMeter** is a Python application that visualizes the CPU usage of your system in real-time. It provides a graphical representation in the form of a circular gauge or dial. The dial is updated every second, displaying the current CPU usage percentage with a moving needle and corresponding percentage labels for easier readability.

This program uses the `Tkinter` library for creating the graphical interface and `psutil` for accessing the real-time CPU usage data.

---

## Features

- Displays real-time CPU usage as a percentage (0% to 100%).
- Graphical circular dial includes:
  - Pointer (needle) indicating the current CPU usage.
  - Percentage labels (`0%`, `10%`, ..., `100%`) around the dial for better readability.
  - Dynamic updates every second.
- Minimal and user-friendly design.

---

## Requirements

Before running the application, make sure the following requirements are met:

- **Python Version**: Python 3.6 or later.
- **Libraries**:
  - `psutil`
  - `tkinter` (comes pre-installed with Python in most environments)

---

## Installation

1. **Install Python**  
   Ensure you have Python 3.6 or later installed. You can download it from [python.org](https://www.python.org).

2. **Install Required Libraries**  
   Use `pip` to install `psutil` if it's not already installed:
   ```bash
   pip install psutil
   ```

   Note: `tkinter` is included with most standard Python installations, so no additional installation is required.

---

## How to Run

1. Save the program file, e.g., **CpuUsageMeter.py**.
2. Open a terminal or command prompt.
3. Navigate to the directory containing **CpuUsageMeter.py**.
4. Run the application using the following command:
   ```
   python CpuUsageMeter.py
   ```

---

## Usage

Once the application is running:
- A graphical window will appear displaying the CPU usage dial.
- The needle moves in real-time to reflect the current system's CPU usage.
- Percentage readings (`0%` to `100%`) around the dial allow easy interpretation of the usage percentage.

---

## Tested Environments

- Python 3.8 on macOS, Windows 10, and Ubuntu 20.04.

---

## Example Output

The GUI window includes:
- A circular dial representing CPU usage.
- Dynamic updates of the needle position and CPU usage label.
- Percentage markers (`0%`, `10%`, ..., `100%`) around the scale.

---

## Notes

- The application uses `psutil` to fetch CPU usage data, so make sure that the library is installed before running the program.
- The real-time updates occur every second with minimal load on your CPU.

Enjoy monitoring your system's performance with this simple and elegant CPU Usage Meter! 😊