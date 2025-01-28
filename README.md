# Classical_fields

Simulation of classical fields using Pygame for visualization!

## Current Version
A realistic parameter simulation of the Sun, Mercury, Venus, Earth, Moon, Mars, and the asteroid belt.

---

## Controls
- **Camera Movement**  
  Use the arrow keys (up, down, left, and right). This is managed through the class method `move_observer`, which moves all particle objects in the specified direction.  

- **Zoom In and Zoom Out**  
  Controlled via a scale that relates meters to screen pixels.  
  - Press the **Z** key to zoom out.  
  - Press the **X** key to zoom in.  

- **Time Multiplier**  
  The simulation runs in real-time, but the speed can be adjusted.  
  - Use the number keys **0 to 9** to increase the time multiplier linearly.

---

## Running the Simulation
It is recommended to run the simulation by modifying the files `main.py` and `simulation.py`.  
However, there is an executable available in the `/build` directory.

---

### Requirements
- **Python 3.9 or higher**  
- **Pygame library** (install via `pip install pygame`)  

---

### How to Contribute
Feel free to submit issues or pull requests if you would like to contribute to improving the simulation.

---

### License
This project is licensed under the MIT License. See the `LICENSE` file for more details.