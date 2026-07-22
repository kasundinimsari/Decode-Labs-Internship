import customtkinter as ctk
import string
import pyperclip

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

COMMON={"password","123456","12345678","qwerty","admin","abc123","welcome"}

app=ctk.CTk()
app.title("Password Strength Checker")
app.geometry("560x560")
app.resizable(False,False)

def toggle():
    if entry.cget("show")=="*":
        entry.configure(show="")
        show_btn.configure(text="Hide")
    else:
        entry.configure(show="*")
        show_btn.configure(text="Show")

def copy_pw():
    pw=entry.get().strip()
    if not pw:
        status.configure(text="Nothing to copy!",text_color="orange")
        return
    pyperclip.copy(pw)
    status.configure(text="Password copied!",text_color="lightgreen")

title=ctk.CTkLabel(app,text="🔐 Password Strength Checker",font=("Segoe UI",28,"bold"))
title.pack(pady=20)

entry=ctk.CTkEntry(app,width=360,height=42,placeholder_text="Enter your password",show="*",font=("Segoe UI",15))
entry.pack()

show_btn=ctk.CTkButton(app,text="Show",width=90,command=toggle)
show_btn.pack(pady=10)

progress=ctk.CTkProgressBar(app,width=360)
progress.pack(pady=10)
progress.set(0)

result=ctk.CTkLabel(app,text="Waiting for password...",font=("Segoe UI",18,"bold"))
result.pack()

score_lbl=ctk.CTkLabel(app,text="Score: 0/5")
score_lbl.pack()

checklist=ctk.CTkLabel(app,text="",justify="left",font=("Consolas",13))
checklist.pack(pady=10)

suggest=ctk.CTkLabel(app,text="")
suggest.pack()

status=ctk.CTkLabel(app,text="")
status.pack(pady=5)

def analyse(*_):
    pw=entry.get().strip()
    if not pw:
        progress.set(0)
        result.configure(text="Enter a password",text_color="white")
        score_lbl.configure(text="Score: 0/5")
        checklist.configure(text="")
        suggest.configure(text="")
        status.configure(text="")
        return
    if pw.lower() in COMMON:
        progress.set(0.1)
        progress.configure(progress_color="red")
        result.configure(text="Very Weak",text_color="red")
        score_lbl.configure(text="Score: 0/5")
        checklist.configure(text="✖ Common password")
        suggest.configure(text="Use a unique password.")
        return
    score=0
    checks=[
        ("Length (8+)",len(pw)>=8),
        ("Uppercase",any(c.isupper() for c in pw)),
        ("Lowercase",any(c.islower() for c in pw)),
        ("Number",any(c.isdigit() for c in pw)),
        ("Symbol",any(c in string.punctuation for c in pw)),
    ]
    lines=[]
    for name,ok in checks:
        if ok: score+=1
        lines.append(("✔ " if ok else "✖ ")+name)
    checklist.configure(text="\n".join(lines))
    progress.set(score/5)
    score_lbl.configure(text=f"Score: {score}/5")
    if score<=2:
        result.configure(text="Weak",text_color="red")
        progress.configure(progress_color="red")
        crack="Minutes"
    elif score<=4:
        result.configure(text="Medium",text_color="orange")
        progress.configure(progress_color="orange")
        crack="Days"
    else:
        result.configure(text="Strong",text_color="green")
        progress.configure(progress_color="green")
        crack="Years"
    suggest.configure(text=f"Estimated crack time: {crack}")

entry.bind("<KeyRelease>",analyse)

btn=ctk.CTkButton(app,text="Analyze Password",command=analyse,height=40)
btn.pack(pady=8)

copy=ctk.CTkButton(app,text="Copy Password",command=copy_pw,height=40)
copy.pack()

app.mainloop()
