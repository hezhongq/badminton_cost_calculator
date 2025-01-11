import tkinter as tk
from tkinter import messagebox

def calculate_cost():
    try:
        # Get input values
        bird_cost = float(entry_bird_cost.get())
        num_birdies = int(entry_num_birdies.get())
        attendees = entry_attendees.get().split(",")
        
        # Calculate results
        num_people = len(attendees)
        total_cost = bird_cost * num_birdies
        cost_per_person = total_cost / num_people
        
        # Display the result
        result = f"{num_birdies}颗球，{num_people}个人，${cost_per_person:.2f}/人"
        messagebox.showinfo("结果", result)
    except ValueError:
        messagebox.showerror("错误", "请输入有效的数字和人员名单")

# Create the main window
window = tk.Tk()
window.title("Badminton Cost Calculator")

# Create input labels and entries
tk.Label(window, text="每颗球的费用 ($):").grid(row=0, column=0, padx=10, pady=5)
entry_bird_cost = tk.Entry(window)
entry_bird_cost.grid(row=0, column=1, padx=10, pady=5)

tk.Label(window, text="使用了多少颗球:").grid(row=1, column=0, padx=10, pady=5)
entry_num_birdies = tk.Entry(window)
entry_num_birdies.grid(row=1, column=1, padx=10, pady=5)

tk.Label(window, text="参加人员 (用逗号分隔):").grid(row=2, column=0, padx=10, pady=5)
entry_attendees = tk.Entry(window)
entry_attendees.grid(row=2, column=1, padx=10, pady=5)

# Create the calculate button
calculate_button = tk.Button(window, text="计算", command=calculate_cost)
calculate_button.grid(row=3, columnspan=2, pady=10)

# Run the application
window.mainloop()
