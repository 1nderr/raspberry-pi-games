# Raspberry Pi Games & Projects

A collection of Python programs and games designed to run on a Raspberry Pi with GPIO-connected LEDs and buttons.

## Requirements

- Raspberry Pi (any model with GPIO pins)
- Python 2
- `RPi.GPIO` library (pre-installed on Raspbian)
- `pygame` (for the Stroop Effect Game)
- LEDs, buttons, resistors, and jumper wires as needed per project

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/1nderr/raspberry-pi-games.git
   cd raspberry-pi-games
   ```

2. Install pygame (only needed for the Stroop Effect Game):

   ```bash
   sudo apt-get install python-pygame
   ```

3. Run any script:
   ```bash
   python <script_name>.py
   ```

> All scripts must be run on a Raspberry Pi with the appropriate GPIO hardware connected. Press `Ctrl+C` to exit any running program.

---

## Projects

### Blink LED

**`blinkLED.py`**

A simple introductory script that turns on an LED connected to a GPIO pin for 5 seconds, then turns it off and cleans up.

**Hardware:**

- 1 LED connected to a GPIO pin of your choice

**Usage:**

```bash
python blinkLED.py
```

**How it works:**

1. You are prompted to enter the GPIO pin number your LED is connected to.
2. The LED turns on for 5 seconds.
3. The GPIO pins are cleared and the program exits.

<!-- ![Blink LED](docs/blinkLED.png) -->

---

### Stoplight

**`stoplight.py`**

Simulates a traffic stoplight by cycling through green, yellow, and red LEDs in sequence, each staying on for 3 seconds.

**Hardware:**

- 3 LEDs (green, yellow, red) connected to GPIO pins of your choice

**Usage:**

```bash
python stoplight.py
```

**How it works:**

1. You are prompted to enter the GPIO pin numbers for the green, yellow, and red LEDs.
2. The lights cycle continuously: green -> yellow -> red.
3. Press `Ctrl+C` to stop and clean up GPIO pins.

<!-- ![Stoplight](docs/stoplight.png) -->

---

### LED Cycle

**`LEDcycle.py`**

Cycles through 4 LEDs one at a time using a single button press. Each press advances to the next LED in the sequence.

**Hardware:**

- 1 button
- 4 LEDs connected to GPIO pins of your choice

**Usage:**

```bash
python LEDcycle.py
```

**How it works:**

1. You are prompted to enter the GPIO pin numbers for the button and 4 LEDs.
2. Press the button to light up the first LED.
3. Each subsequent press advances to the next LED, looping back to the first after the fourth.
4. Press `Ctrl+C` to stop and clean up GPIO pins.

<!-- ![LED Cycle](docs/LEDcycle.png) -->

---

### Calculator

**`calculator.py`**

A hardware-based calculator that uses 4 physical buttons to perform addition, subtraction, multiplication, and division on two numbers.

**Hardware:**

- 4 buttons connected to GPIO pins 4, 17, 27, and 22

**Usage:**

```bash
python calculator.py
```

**Controls:**
| Button | GPIO Pin | Operation |
|--------|----------|----------------|
| 1 | 4 | Addition (+) |
| 2 | 17 | Subtraction (-)|
| 3 | 27 | Multiplication (\*)|
| 4 | 22 | Division (/) |

**How it works:**

1. Enter two numbers when prompted.
2. Press a button to perform the corresponding operation.
3. Once all four operations have been used at least once, you can enter new numbers.
4. Press `Ctrl+C` to exit.

<!-- ![Calculator](docs/calculator.png) -->

---

### Stroop Effect Game

**`StroopEffectGame.py`**

A memory and psychology-based game built on the [Stroop Effect](https://en.wikipedia.org/wiki/Stroop_effect). Color words are displayed in mismatched ink colors (e.g., the word "Green" in red text). You must remember the **ink color** (not the word) and answer questions using physical buttons.

**Hardware:**

- 4 buttons connected to GPIO pins 4 (Red), 17 (Green), 27 (Blue), and 22 (Yellow)
- A display/monitor connected to the Raspberry Pi

**Dependencies:**

- `pygame`

**Usage:**

```bash
python StroopEffectGame.py
```

**Controls:**
| Button | GPIO Pin | Color |
|--------|----------|--------|
| 1 | 4 | Red |
| 2 | 17 | Green |
| 3 | 27 | Blue |
| 4 | 22 | Yellow |

**How to play:**

1. Press the **Red button** to start.
2. **Level 1:** Four color words flash on screen in mismatched ink colors. Remember the ink color of each word in order.
3. After all words are shown, you are asked "What was color number X?" for each one. Press the button matching the **ink color** (not the word).
4. Correct answers earn +1 point, wrong answers lose -1 point.
5. Score 4/4 on Level 1 to advance to **Level 2**, which shows 8 words.
6. Score 8/8 on Level 2 to win the game.

<!-- ![Stroop Effect Game](docs/stroop.png) -->
