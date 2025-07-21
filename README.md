# 📊 Instagram Follower Analyzer GUI

A Python-based GUI app to analyze your Instagram followers and followings.

It tells you:
- ❌ **Traitors** — People you follow but they don’t follow you back
- 🫶 **Fans** — People who follow you but you don’t follow back
- 🤝 **Mutuals** — Accounts where both follow each other

Each list is saved as a `.txt` file:
- `traitors.txt`
- `fans.txt`
- `mutuals.txt`

---

## 🛠 Features

- ✅ Clean Tkinter-based interface
- 🔐 Safe login using Instagram `sessionid` (no password required)
- 🔍 Live progress in a built-in console
- 💾 Automatically saves lists as text files
- 🧠 Uses [Instaloader](https://instaloader.github.io/) under the hood

---

## 🚀 How to Run

### 1. Clone the Repo or Copy Code
```bash
git clone https://github.com/yourusername/insta-follower-analyzer
cd insta-follower-analyzer
```

### 2. Install Python Requirements

pip install instaloader

3. Run the Script

python insta_gui.py



🧾 How to Get Your Instagram Session ID

> Instagram uses a sessionid cookie to keep you logged in. We'll use this safely (no password needed) to analyze your followers.



🔍 Steps to Get sessionid:

✅ For Chrome:

1. Open instagram.com and log in to your account.


2. Right-click anywhere on the page and select "Inspect" or press Ctrl+Shift+I.


3. Go to the Application tab.


4. In the left menu, under Storage, click on Cookies → https://www.instagram.com


5. Find the cookie named sessionid and copy its value.



✅ For Firefox:

1. Login to Instagram and right-click → Inspect Element


2. Go to Storage > Cookies


3. Copy the value of the sessionid



🛑 Never share this session ID with anyone — it can be used to access your Instagram account.


---

🖼 Interface Preview

<img src="preview.png" width="600">
---

📁 Output Example

traitors.txt


user1
user2
user3

fans.txt


followerA
followerB

mutuals.txt


friend1
friend2
friend3


---

📌 Notes

This app does not use Instagram's official API (which is restricted). It uses cookies for safer access.

Avoid running it repeatedly in a short time — Instagram may temporarily restrict access.

No password is stored or transmitted.



---

📄 License

MIT License — Feel free to modify and use!


---

👨‍💻 Author

Made with ❤️ by [Pralin Khaira](www.instagram.com/tbh.yoursss/)
