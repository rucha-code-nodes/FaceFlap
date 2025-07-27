🎮🧑‍🦽 FaceFlap 🚀🐤

🎮 Flappy Bird controlled with head movements — no hands needed!
♿️ Designed for accessibility using real-time face tracking via webcam.


## ♿ Why We Developed the Head-Controlled Game

We created this feature as a part of our mission to make gaming more **inclusive and accessible**.
Many traditional games rely on **hand-based input** (keyboard, mouse, or touch), which creates a barrier for individuals with **physical disabilities**.

🎯 **Our Goal:**
To enable **differently-abled users** — especially those who cannot use their hands — to enjoy interactive gameplay using only **head movements**.

---

## 👤 Who It's For

* 🧑‍🦽 **Individuals with motor impairments**
* 🎓 **Students learning about computer vision in real-world applications**
* 👩‍💻 **Developers exploring gesture/face-based input systems**
* 🧠 **Researchers and hobbyists in accessibility tech**

---



We’ve included a fun **bonus game**:
A **head-controlled version of Flappy Bird** 🐤 — move your head **up/down/left/right** to fly and dodge pipes!

### ⚙️ How It Works:

* Uses your **webcam and face tracking** to detect head movement
* Controls the bird using facial direction via OpenCV
* No keyboard needed — just your head movements!

---

### 🛑 Disabled by Default

This feature is **not active by default**. To play the game:

1. Ensure your webcam is working.

2. Uncomment or run `main.py`:

   ```bash
   python main.py
   ```

3. Or run directly:

   ```bash
   python modules/game.py
   ```

---

### 📁 Game Files:

* `modules/game.py` — Main game logic with head control
* `modules/head_control.py` — Handles head movement detection via webcam
* `main.py` — Entry point to launch the game

> 💡 *Note:* Game assets (backgrounds, bird, pipes) must be present at correct paths or updated accordingly.


