import tkinter as tk
from tkinter import Canvas
import psutil
import math


class CpuUsageMeter:
    def __init__(self, root):
        self.root = root
        self.root.title("CPU Usage Meter")

        # Set up canvas area
        self.canvas = Canvas(root, width=300, height=300, bg="white")
        self.canvas.pack()

        # Dial properties
        self.center_x, self.center_y = 150, 150
        self.radius = 90
        self.draw_dial()

        # CPU usage label
        self.usage_label = tk.Label(root, text="CPU Usage: 0%", font=("Helvetica", 16))
        self.usage_label.pack(pady=10)

        # Timer to update CPU usage
        self.update_meter()

    def draw_dial(self):
        """Draws the static elements of the dial (circle, tick marks, and labels)."""
        # Draw the outer circle
        self.canvas.create_oval(
            self.center_x - self.radius - 20,
            self.center_y - self.radius - 20,
            self.center_x + self.radius + 20,
            self.center_y + self.radius + 20,
            outline="black", width=2
        )

        # Draw tick marks and labels
        for i in range(0, 101, 10):  # Ticks for 0% to 100%
            angle = (i / 100) * 180  # Map percentage to 180 degrees
            radian = math.radians(180 - angle)

            # Outer tick mark position
            x1 = self.center_x + (self.radius + 10) * math.cos(radian)
            y1 = self.center_y - (self.radius + 10) * math.sin(radian)

            # Inner tick mark position
            x2 = self.center_x + self.radius * math.cos(radian)
            y2 = self.center_y - self.radius * math.sin(radian)

            # Draw tick mark
            self.canvas.create_line(x1, y1, x2, y2, fill="black", width=2)

            # Position for numbers
            label_x = self.center_x + (self.radius + 25) * math.cos(radian)
            label_y = self.center_y - (self.radius + 25) * math.sin(radian)

            # Draw the percentage text
            self.canvas.create_text(label_x, label_y, text=f"{i}%", font=("Helvetica", 10))

    def update_meter(self):
        """Updates the meter pointer and CPU usage label in real-time."""
        # Get current CPU usage
        cpu_usage = psutil.cpu_percent(interval=0.1)

        # Update CPU usage label
        self.usage_label.config(text=f"CPU Usage: {cpu_usage:.1f}%")

        # Clear old pointer
        self.canvas.delete("pointer")

        # Calculate angle for pointer based on CPU usage
        angle = (cpu_usage / 100) * 180  # Map 0-100% to 0-180 degrees
        radian = math.radians(180 - angle)

        # Pointer position
        pointer_x = self.center_x + self.radius * math.cos(radian)
        pointer_y = self.center_y - self.radius * math.sin(radian)

        # Draw pointer
        self.canvas.create_line(
            self.center_x, self.center_y, pointer_x, pointer_y,
            fill="red", width=3, tags="pointer"
        )

        # Schedule the next update
        self.root.after(1000, self.update_meter)


# Run the program
if __name__ == "__main__":
    import psutil  # Ensure psutil is installed

    root = tk.Tk()
    app = CpuUsageMeter(root)
    root.mainloop()