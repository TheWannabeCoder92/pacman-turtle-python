# Episode 9 – Custom Shapes & Game Audio

In this final episode, we add the finishing touches that make the game feel complete — visuals and sound effects!

We replace the default shapes with custom images and add game audio to enhance the player experience.

### 🛠️ What’s covered:
- Loading and registering custom shapes for Pac-Man and enemies
- Updating the player and enemy appearances using image assets
- Adding sound effects for:
  - Game start
  - Pellet collection
  - Player death
- Playing audio clips at the right moments during gameplay

By the end of this episode, the game not only plays well — it *looks* and *sounds* like a real arcade experience. Congratulations on completing the full Pac-Man in Python series!

---

### 🔊 How to Play Sound on Different Operating Systems

To play sound effects, we use the `os.system()` function to call system-level audio commands. The exact command depends on your operating system:

#### 🐧 Linux (using `aplay`)
```python
os.system("aplay sound.wav > /dev/null 2>&1 &")

- The & at the end plays the sound in the background.

- > /dev/null 2>&1 hides any terminal output.

#### 🪟 Windows (using `start`)
```python
os.system("start sound.wav")

#### 🍎 macOS (using afplay)
```python
os.system("afplay sound.wav")

📁 Note: Make sure your .wav & .gif files are saved in the same directory as your Python script, or provide the full path to the file.
