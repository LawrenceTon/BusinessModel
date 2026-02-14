import os
import json
import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime

class EmpireOSv2:
    def __init__(self, root):
        self.root = root
        self.root.title("CYBORG_ET | EMPIRE OS v2.0 | COMMAND")
        self.root.geometry("800x600")
        self.root.configure(bg="#050505")
        
        self.vaults = ['VAULT_1_BLUEPRINT', 'VAULT_2_INFILTRATION', 'VAULT_3_TREASURY']
        self.log_file = "strike_logs.json"

        # Style
        style = ttk.Style()
        style.theme_use('clam')
        style.configure("TFrame", background="#050505")
        style.configure("TLabel", background="#050505", foreground="#00ff00", font=("Courier", 10))
        style.configure("Header.TLabel", font=("Courier", 20, "bold"), foreground="#00ff00")
        style.configure("Vault.TLabelframe", background="#050505", foreground="#00ff00")
        style.configure("Vault.TLabelframe.Label", foreground="#00ffff", font=("Courier", 12, "bold"))
        style.configure("Strike.TButton", font=("Courier", 12, "bold"), foreground="#ff0000", background="#220000")

        # Layout
        header = ttk.Label(root, text="EMPIRE OS v2.0", style="Header.TLabel")
        header.pack(pady=20)

        main_frame = ttk.Frame(root)
        main_frame.pack(fill="both", expand=True, padx=20)

        # 1. Vault Monitor
        self.monitor_frame = ttk.LabelFrame(main_frame, text=" [ VAULT MONITOR ] ", style="Vault.TLabelframe")
        self.monitor_frame.pack(side="left", fill="both", expand=True, padx=5)
        self.vault_status = {}
        for v in self.vaults:
            lbl = ttk.Label(self.monitor_frame, text=f"{v}: SCANNING...")
            lbl.pack(anchor="w", padx=10, pady=5)
            self.vault_status[v] = lbl

        # 2. Strike Control & Calculator
        right_frame = ttk.Frame(main_frame)
        right_frame.pack(side="right", fill="both", expand=True, padx=5)

        # Hydra Strike
        strike_frame = ttk.LabelFrame(right_frame, text=" [ ATTACK VECTOR ] ", style="Vault.TLabelframe")
        strike_frame.pack(fill="x", pady=5)
        ttk.Button(strike_frame, text="LOG HYDRA STRIKE (50)", style="Strike.TButton", command=self.log_strike).pack(fill="x", padx=10, pady=10)

        # Babylonian Calculator
        calc_frame = ttk.LabelFrame(right_frame, text=" [ BABYLONIAN CALC ] ", style="Vault.TLabelframe")
        calc_frame.pack(fill="both", expand=True, pady=5)
        ttk.Label(calc_frame, text="Input Revenue (PHP):").pack(pady=5)
        self.revenue_entry = ttk.Entry(calc_frame)
        self.revenue_entry.pack(pady=5)
        ttk.Button(calc_frame, text="CALCULATE TITHE", command=self.calculate_tithe).pack(pady=5)
        self.result_label = ttk.Label(calc_frame, text="SEED GOLD (10%): 0.00", font=("Courier", 10, "bold"))
        self.result_label.pack(pady=10)

        self.refresh_vaults()

    def refresh_vaults(self):
        for v in self.vaults:
            if os.path.exists(v):
                files = os.listdir(v)
                status = "ACTIVE" if files else "EMPTY"
                color = "#00ff00" if files else "#ffff00"
                self.vault_status[v].config(text=f"{v}: {status} ({len(files)} items)", foreground=color)
            else:
                self.vault_status[v].config(text=f"{v}: MISSING", foreground="#ff0000")
        self.root.after(5000, self.refresh_vaults)

    def log_strike(self):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        entry = {"timestamp": timestamp, "type": "HYDRA_STRIKE", "contacts": 50}
        
        logs = []
        if os.path.exists(self.log_file):
            with open(self.log_file, "r") as f:
                try: logs = json.load(f)
                except: logs = []
        
        logs.append(entry)
        with open(self.log_file, "w") as f:
            json.dump(logs, f, indent=4)
        
        messagebox.showinfo("STRIKE LOGGED", f"Hydra Strike confirmed at {timestamp}.\n50 contacts registered in {self.log_file}.")

    def calculate_tithe(self):
        try:
            rev = float(self.revenue_entry.get())
            tithe = rev * 0.10
            self.result_label.config(text=f"SEED GOLD (10%): {tithe:,.2f} PHP")
            messagebox.showinfo("TITHE CALCULATED", f"10% Law Applied.\nSeed Fund: {tithe:,.2f} PHP\nOperating Capital: {rev-tithe:,.2f} PHP")
        except:
            messagebox.showerror("INPUT ERROR", "Please enter a valid numeric value.")

if __name__ == "__main__":
    root = tk.Tk()
    app = EmpireOSv2(root)
    root.mainloop()
