# 🚀 Space Duel

> **My first ever game project.**
>A simple two-player spaceship shooter built with **Python** and **Pygame**.

This project marks the beginning of my game development journey. 

---

## 🎮 Gameplay

Two players battle from opposite ends of the screen.

- 🟡 Yellow starts at the top.
- 🔴 Red starts at the bottom.
- Each player has **5 HP**.
- First player to reduce the opponent's health to zero wins.

---

## 🎮 Controls

| Action | Yellow (P1) | Red (P2) |
|--------|-------------|----------|
| Move | W A S D | Arrow Keys |
| Shoot | Left Ctrl | Right Ctrl |

---

## 📦 Requirements


- Python 3.x
- Pygame
- Electricity
- A potato with a display output 

```bash
pip install pygame
```

---

## 📁 Assets

Create an `Assets/` folder beside `main.py` and place:

- spaceship_yellow.png
- spaceship_red.png
- Gun+Silencer.mp3
- Grenade+1.mp3

Also place:

- bg.jpg

next to `main.py`.

---

## ▶️ Run

```bash
python main.py
```

---

## 💀 Developer's Note

This was written before I learned about things like clean architecture, design patterns, or why global variables have a bad reputation.

I'm leaving it here because progress is more interesting when you can see where it started.
