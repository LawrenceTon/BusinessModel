import os
import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
import winsound # Standard Windows sound library

class ImperialCommandCenter:
    def __init__(self, root):
        self.root = root
        self.root.title("CYBORG_ET | IMPERIAL EXECUTION ENGINE | v5.0")
        self.root.geometry("1200x800")
        self.root.configure(bg="#050505")
        
        self.daily_contacts = 0
        self.inflow = 0.0
        self.seed = 0.0

        # Imperial Theme
        self.style = ttk.Style()
        self.style.theme_use('clam')
        self.style.configure("TFrame", background="#050505")
        self.style.configure("TLabel", background="#050505", foreground="#00ff00", font=("Courier", 10))
        self.style.configure("Header.TLabel", font=("Courier", 22, "bold"), foreground="#00ff00")
        self.style.configure("Goal.TLabelframe", background="#050505", foreground="#00ff00")
        self.style.configure("Goal.TLabelframe.Label", foreground="#00ffff", font=("Courier", 12, "bold"))

        # Header & Clock
        self.header = ttk.Label(root, text="EMPIRE STATUS: ACTIVE INFILTRATION", style="Header.TLabel")
        self.header.pack(pady=10)
        
        # Dashboard Layout
        self.top_paned = ttk.Panedwindow(root, orient=tk.HORIZONTAL)
        self.top_paned.pack(fill="both", expand=True, padx=20)

        # 1. Left: Strategic Vaults (The Plan)
        self.vault_frame = ttk.LabelFrame(self.top_paned, text=" [ VAULTS ] ", style="Goal.TLabelframe")
        self.top_paned.add(self.vault_frame, weight=1)
        self.tree = ttk.Treeview(self.vault_frame, show="tree")
        self.tree.pack(fill="both", expand=True)
        self.tree.bind("<Double-1>", self.on_file_click)

        # 2. Middle: Daily Instructions (The Steps)
        self.task_frame = ttk.LabelFrame(self.top_paned, text=" [ COMMAND LOGIC ] ", style="Goal.TLabelframe")
        self.top_paned.add(self.task_frame, weight=2)
        
        self.instr_text = tk.Text(self.task_frame, bg="#0a0a0a", fg="#00ffff", font=("Courier", 11), state='disabled', wrap='word')
        self.instr_text.pack(fill="both", expand=True, padx=5, pady=5)

        # 3. Right: Input & Alarm (Execution)
        self.exec_frame = ttk.Frame(self.top_paned)
        self.top_paned.add(self.exec_frame, weight=1)

        # Daily Goal Entry
        goal_input = ttk.LabelFrame(self.exec_frame, text=" [ DAILY EXECUTION ] ", style="Goal.TLabelframe")
        goal_input.pack(fill="x", pady=5)
        ttk.Label(goal_input, text="Contacts Made:").pack()
        self.contact_entry = ttk.Entry(goal_input)
        self.contact_entry.pack(pady=5)
        ttk.Button(goal_input, text="LOG PROGRESS", command=self.log_execution).pack(pady=5)

        # Treasury Log
        money_input = ttk.LabelFrame(self.exec_frame, text=" [ TREASURY ] ", style="Goal.TLabelframe")
        money_input.pack(fill="x", pady=5)
        self.money_entry = ttk.Entry(money_input)
        self.money_entry.pack(pady=5)
        ttk.Button(money_input, text="LOG INFLOW", command=self.log_money).pack(pady=5)

        self.status_label = ttk.Label(self.exec_frame, text="CONTACTS: 0/50\nSEED: PHP 0.00", font=("Courier", 12, "bold"))
        self.status_label.pack(pady=20)

        self.load_instructions()
        self.refresh_tree()

    def load_instructions(self):
        steps = """
--- DAILY INSTRUCTIONS ---
1. Open 07_ZERO_BUDGET_SCRIPT.
2. Find 50 Indian/Chinese manufacturers via LinkedIn/Directories.
3. Send 50 emails. LOG PROGRESS on the right.
4. ALARM will trigger if goal is not met by EOD.

--- MONTHLY GOALS ---
- Secure 1 distribution partnership.
- Close 1 lead-gen retainer (Target: PHP 10k+).

--- QUARTERLY ---
- Accumulate PHP 50,000 in Seed Reserve.
- Validate 3 high-demand generic drug lines.

--- ANNUAL ---
- Finalize legal entity.
- Apply for FDA License to Operate (LTO).
        """
        self.instr_text.config(state='normal')
        self.instr_text.insert(tk.END, steps)
        self.instr_text.config(state='disabled')

    def log_execution(self):
        try:
            val = int(self.contact_entry.get())
            self.daily_contacts += val
            self.status_label.config(text=f"CONTACTS: {self.daily_contacts}/50\nSEED: PHP {self.seed:,.2f}")
            if self.daily_contacts >= 50:
                messagebox.showinfo("VICTORY", "Daily Goal Met. Momentum Sustained.")
            else:
                # Play alert sound
                winsound.Beep(1000, 500) 
            self.contact_entry.delete(0, tk.END)
        except: pass

    def log_money(self):
        try:
            val = float(self.money_entry.get())
            self.inflow += val
            self.seed += val * 0.10
            self.status_label.config(text=f"CONTACTS: {self.daily_contacts}/50\nSEED: PHP {self.seed:,.2f}")
            self.money_entry.delete(0, tk.END)
        except: pass

    def refresh_tree(self):
        vaults = ['VAULT_1_BLUEPRINT', 'VAULT_2_INFILTRATION', 'VAULT_3_TREASURY']
        for v in vaults:
            node = self.tree.insert("", "end", text=v, open=True)
            if os.path.exists(v):
                for f in os.listdir(v):
                    self.tree.insert(node, "end", text=f, values=(v,))

    def on_file_click(self, event):
        item = self.tree.selection()[0]
        filename = self.tree.item(item, "text")
        parent_v = self.tree.item(item, "values")
        if parent_v:
            path = os.path.join(parent_v[0], filename)
            with open(path, 'r') as f:
                content = f.read()
            self.instr_text.config(state='normal')
            self.instr_text.delete('1.0', tk.END)
            self.instr_text.insert(tk.END, f"--- FILE DATA: {filename} ---\n\n{content}")
            self.instr_text.config(state='disabled')

if __name__ == "__main__":
    root = tk.Tk()
    app = ImperialCommandCenter(root)
    root.mainloop()
