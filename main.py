import customtkinter
import libs

def solve():
	ans = libs.solve(question.get("0.0", "end"))
	answer.configure(state="normal")
	answer.delete("0.0", "end")
	answer.insert("0.0", ans)
	answer.configure(state="disable")

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry("1000x550")

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

lable = customtkinter.CTkLabel(master=frame, text="Question", font=("Roboto", 24))
lable.pack(pady=12, padx=10)

question = customtkinter.CTkTextbox(master=frame, width=880, height=120,  font=("Roboto", 16))
question.pack(pady=20, padx=30)

button = customtkinter.CTkButton(master=frame, text="Solve", font=("Arial", 17), command=solve)
button.pack(pady=8, padx=10)

answer = customtkinter.CTkTextbox(master=frame, width=880, height=120, state="disable", font=("Roboto", 16))
answer.pack(pady=20, padx=30)

root.mainloop()