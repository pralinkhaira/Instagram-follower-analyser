import tkinter as tk
from tkinter import messagebox, scrolledtext
import instaloader

def log(message):
    console_text.config(state=tk.NORMAL)
    console_text.insert(tk.END, message + "\n")
    console_text.see(tk.END)
    console_text.config(state=tk.DISABLED)
    root.update_idletasks()

def fetch_and_save():
    username = username_entry.get().strip()
    sessionid = sessionid_entry.get().strip()

    console_text.config(state=tk.NORMAL)
    console_text.delete("1.0", tk.END)
    console_text.config(state=tk.DISABLED)

    if not username or not sessionid:
        messagebox.showerror("Input Error", "Please enter both Username and Session ID.")
        return

    try:
        log("✅ Validating inputs...")
        L = instaloader.Instaloader()
        L.context._session.cookies.set('sessionid', sessionid, domain='.instagram.com')

        log("🔗 Connecting to Instagram...")
        profile = instaloader.Profile.from_username(L.context, username)
        log("✅ Username and Session ID validated.")

        log("📥 Fetching followers...")
        followers = set()
        for follower in profile.get_followers():
            followers.add(follower.username)
        log(f"👥 Total Followers: {len(followers)}")

        log("📤 Fetching following...")
        followees = set()
        for followee in profile.get_followees():
            followees.add(followee.username)
        log(f"➡️ Total Following: {len(followees)}")

        # Calculate categories
        traitors = followees - followers
        fans = followers - followees
        mutuals = followers & followees

        with open("traitors.txt", "w") as f:
            f.write("\n".join(sorted(traitors)))

        with open("fans.txt", "w") as f:
            f.write("\n".join(sorted(fans)))

        with open("mutuals.txt", "w") as f:
            f.write("\n".join(sorted(mutuals)))

        log(f"\n📄 Results:\n- Traitors (Not following you back): {len(traitors)}")
        log(f"- Fans (Follow you, but you don't): {len(fans)}")
        log(f"- Mutuals (Both follow): {len(mutuals)}")
        log("✅ Files saved: traitors.txt, fans.txt, mutuals.txt")
        messagebox.showinfo("Success", "Follower analysis complete!")

    except Exception as e:
        messagebox.showerror("Error", f"Something went wrong:\n{str(e)}")
        log(f"❌ Error: {e}")

# GUI Setup
root = tk.Tk()
root.title("Instagram Follower Analyzer")
root.geometry("500x550")
root.resizable(False, False)

tk.Label(root, text="Instagram Username").pack(pady=5)
username_entry = tk.Entry(root, width=50)
username_entry.pack()

tk.Label(root, text="Session ID (from browser cookies)").pack(pady=5)
sessionid_entry = tk.Entry(root, show="*", width=50)
sessionid_entry.pack()

tk.Button(root, text="Start Analysis", command=fetch_and_save, bg="#1976D2", fg="white", font=("Arial", 11, "bold")).pack(pady=15)

tk.Label(root, text="🔍 Console Output", font=("Arial", 10, "bold")).pack()

console_text = scrolledtext.ScrolledText(root, height=15, width=60, state=tk.DISABLED, font=("Consolas", 9))
console_text.pack(pady=5)

tk.Label(root, text="Results will be saved as:\ntraitors.txt, fans.txt, mutuals.txt", fg="gray").pack(pady=5)

root.mainloop()
