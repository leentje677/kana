# 🦊 KitsuKana (キツカナ)

> **Kana today, Kanji tomorrow!** 🇯🇵

KitsuKana is a modern, interactive web app designed to help you master Japanese Hiragana, Katakana, and basic Vocabulary. Built with a calm "Sage Green" glassmorphism aesthetic, it focuses on a distraction-free and engaging learning experience.

🔗 **[Live Demo](https://leentje677.github.io/kana/)**

## ✨ Features

* **📚 Multiple Study Modes:** Practice Hiragana, Katakana (Seion, Dakuon, Yōon), or jump straight into Vocabulary words.
* **🧠 Smart Validation:** Accepts answers in **Romaji** ("neko") or **English Meaning** ("cat") for vocabulary words.
* **🔊 Native Audio:** Hear the correct pronunciation instantly using browser-native Text-to-Speech.
* **🔥 Gamification:** Track your **Fire Streak** and Accuracy percentage to stay motivated.
* **🔁 Weak Mode:** The app remembers which characters you get wrong and lets you specifically review them.
* **📱 Mobile Optimized:** A responsive design that works perfectly on desktop, tablets, and phones.
* **🌙 Dark Mode:** A dedicated toggle for late-night study sessions.

## 🛠️ Tech Stack

* **HTML5**
* **CSS3** (Glassmorphism, CSS Variables, Animations)
* **Vanilla JavaScript** (No frameworks, lightweight & fast)

## 🚀 How to Run Locally

Since this is a static web application, you don't need to install Node.js or any dependencies.

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/leentje677/kana.git](https://github.com/leentje677/kana.git)
    ```
2.  **Open the folder:**
    Navigate to the project directory.
3.  **Launch:**
    Simply double-click `index.html` to open it in your browser.

*(Note: For the best experience, use a local server like "Live Server" in VS Code to ensure all audio features work correctly.)*

## 🎨 Customization

### Adding New Words
All data is stored in `kana-data.js`. You can easily add your own vocabulary:

1.  Open `kana-data.js`.
2.  Find the `Vocabulary` object.
3.  Add a new entry following this format:
    ```javascript
    "ねこ": { romaji: ["neko"], meaning: "cat" },
    ```

## 📝 Credits

Created by **Leander**.
* Design inspired by modern Glassmorphism trends.
* Icons and aesthetic centered around the "Kitsune" (Fox) theme.

---
*Happy Learning! 頑張ってください (Ganbatte kudasai)!*
