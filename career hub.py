import tkinter as tk
from tkinter import messagebox
import sqlite3

# =========================
# DATABASE
# =========================

database = sqlite3.connect("careerhub.db")
cursor = database.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    education TEXT,
    skills TEXT,
    experience TEXT,
    about TEXT
)
""")

database.commit()


# =========================
# MAIN APP
# =========================

app = tk.Tk()
app.title("CareerHub")
app.geometry("900x600")
app.resizable(False, False)
app.configure(bg="#f4f4f4")


# =========================
# CLEAR SCREEN
# =========================

def clear_screen():
    for widget in app.winfo_children():
        widget.destroy()


# =========================
# HOME SCREEN
# =========================

def home():

    clear_screen()

    # Header
    header = tk.Frame(app, bg="#20232a", height=90)
    header.pack(fill="x")

    tk.Label(
        header,
        text="CareerHub",
        font=("Arial", 28, "bold"),
        fg="white",
        bg="#20232a"
    ).pack(pady=25)

    # Welcome
    tk.Label(
        app,
        text="Build your portfolio. Find your next opportunity.",
        font=("Arial", 18),
        bg="#f4f4f4"
    ).pack(pady=50)

    # Create profile button
    tk.Button(
        app,
        text="CREATE MY PROFILE",
        font=("Arial", 13, "bold"),
        width=25,
        height=2,
        command=create_profile
    ).pack(pady=15)

    # Find jobs button
    tk.Button(
        app,
        text="FIND JOBS",
        font=("Arial", 13, "bold"),
        width=25,
        height=2,
        command=find_jobs
    ).pack(pady=15)

    # Footer
    tk.Label(
        app,
        text="CareerHub • Beginner Career Platform",
        font=("Arial", 10),
        bg="#f4f4f4",
        fg="gray"
    ).pack(side="bottom", pady=20)


# =========================
# CREATE PROFILE
# =========================

def create_profile():

    clear_screen()

    tk.Label(
        app,
        text="Create Your Profile",
        font=("Arial", 25, "bold"),
        bg="#f4f4f4"
    ).pack(pady=25)

    form = tk.Frame(app, bg="#f4f4f4")
    form.pack()

    # Name
    tk.Label(
        form,
        text="Full Name",
        bg="#f4f4f4",
        font=("Arial", 11)
    ).grid(row=0, column=0, sticky="w", pady=6)

    name = tk.Entry(form, width=55)
    name.grid(row=0, column=1, pady=6)

    # Education
    tk.Label(
        form,
        text="Education",
        bg="#f4f4f4",
        font=("Arial", 11)
    ).grid(row=1, column=0, sticky="w", pady=6)

    education = tk.Entry(form, width=55)
    education.grid(row=1, column=1, pady=6)

    # Skills
    tk.Label(
        form,
        text="Skills",
        bg="#f4f4f4",
        font=("Arial", 11)
    ).grid(row=2, column=0, sticky="w", pady=6)

    skills = tk.Entry(form, width=55)
    skills.grid(row=2, column=1, pady=6)

    # Experience
    tk.Label(
        form,
        text="Experience",
        bg="#f4f4f4",
        font=("Arial", 11)
    ).grid(row=3, column=0, sticky="w", pady=6)

    experience = tk.Entry(form, width=55)
    experience.grid(row=3, column=1, pady=6)

    # About
    tk.Label(
        form,
        text="About You",
        bg="#f4f4f4",
        font=("Arial", 11)
    ).grid(row=4, column=0, sticky="nw", pady=6)

    about = tk.Text(form, width=41, height=5)
    about.grid(row=4, column=1, pady=6)

    # Save profile
    def save_profile():

        if name.get().strip() == "":
            messagebox.showwarning(
                "Missing Name",
                "Please enter your name."
            )
            return

        cursor.execute("""
        INSERT INTO users
        (name, education, skills, experience, about)
        VALUES (?, ?, ?, ?, ?)
        """, (
            name.get(),
            education.get(),
            skills.get(),
            experience.get(),
            about.get("1.0", tk.END)
        ))

        database.commit()

        messagebox.showinfo(
            "Profile Created",
            "Your CareerHub profile has been saved!"
        )

        home()

    tk.Button(
        app,
        text="SAVE PROFILE",
        font=("Arial", 12, "bold"),
        width=20,
        command=save_profile
    ).pack(pady=20)

    tk.Button(
        app,
        text="← Back",
        command=home
    ).pack()


# =========================
# FIND JOBS
# =========================

def find_jobs():

    clear_screen()

    tk.Label(
        app,
        text="Find Jobs",
        font=("Arial", 25, "bold"),
        bg="#f4f4f4"
    ).pack(pady=25)

    search_frame = tk.Frame(app, bg="#f4f4f4")
    search_frame.pack()

    search = tk.Entry(
        search_frame,
        width=50,
        font=("Arial", 12)
    )
    search.grid(row=0, column=0, padx=5)

    jobs = [
        ("Python Intern", "Remote", "Beginner"),
        ("Web Developer", "Islamabad", "Entry Level"),
        ("Graphic Designer", "Lahore", "Freelance"),
        ("Content Writer", "Remote", "Part Time"),
        ("Social Media Assistant", "Karachi", "Entry Level"),
        ("Junior Python Developer", "Lahore", "Beginner"),
        ("UI Designer", "Islamabad", "Entry Level")
    ]

    job_list = tk.Listbox(
        app,
        width=75,
        height=14,
        font=("Arial", 12)
    )
    job_list.pack(pady=25)

    def display_jobs():

        job_list.delete(0, tk.END)

        keyword = search.get().lower()

        for title, location, level in jobs:

            job = f"{title}  |  {location}  |  {level}"

            if keyword in job.lower():
                job_list.insert(tk.END, job)

    tk.Button(
        search_frame,
        text="SEARCH",
        command=display_jobs
    ).grid(row=0, column=1)

    display_jobs()

    tk.Button(
        app,
        text="← Back",
        command=home
    ).pack()


# =========================
# START APPLICATION
# =========================

home()

app.mainloop()

database.close()