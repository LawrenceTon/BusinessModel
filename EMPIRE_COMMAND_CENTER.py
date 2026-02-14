import os
import tkinter as tk
from tkinter import ttk
from datetime import datetime

class EmpireGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("CYBORG_ET | EMPIRE COMMAND CENTER v3.0")
        self.root.geometry("900x600")
        self.root.configure(bg="#0a0a0a")
        
        # Style Configuration
        style = ttk.Style()
        style.theme_use('clam')
        style.configure("TFrame", background="#0a0a0a")
        style.configure("TLabel", background="#0a0a0a", foreground="#00ff00", font=("Courier", 10))
        style.configure("Header.TLabel", font=("Courier", 18, "bold"), foreground="#00ff00")
        style.configure("Vault.TLabelframe", background="#0a0a0a", foreground="#00ff00")
        style.configure("Vault.TLabelframe.Label", background="#0a0a0a", foreground="#00ff00")

        # Title
        header = ttk.Label(root, text="EMPIRE COMMAND CENTER", style="Header.TLabel")
        header.pack(pady=20)

        # Main Container
        main_frame = ttk.Frame(root)
        main_frame.pack(fill="both", expand=True, padx=20)

        # Left Column: Vault Status
        self.vault_frame = ttk.LabelFrame(main_frame, text=" [1] STRATEGIC VAULTS ", style="Vault.TLabelframe")
        self.vault_frame.pack(side="left", fill="both", expand=True, padx=10, pady=10)
        
        self.vault_text = tk.Text(self.vault_frame, bg="#0f0f0f", fg="#00ff00", font=("Courier", 10), borderwidth=0)
        self.vault_text.pack(fill="both", expand=True, padx=5, pady=5)

        # Right Column: Progress & Goals
        right_frame = ttk.Frame(main_frame)
        right_frame.pack(side="right", fill="both", expand=True, padx=10, pady=10)

        # Progress Section
        self.prog_label = ttk.Label(right_frame, text="EXECUTION PROGRESS: 0%", font=("Courier", 12, "bold"))
        self.prog_label.pack(anchor="w")
        self.progress = ttk.Progressbar(right_frame, orient="horizontal", length=300, mode="determinate")
        self.progress.pack(fill="x", pady=10)

        # Goals Section
        goal_frame = ttk.LabelFrame(right_frame, text=" [2] GOAL ARCHITECTURE ", style="Vault.TLabelframe")
        goal_frame.pack(fill="both", expand=True, pady=10)
        
        goals = [
            "DAILY: Contact 50 Prospects",
            "MONTHLY: Secure 1 Deal",
            "QUARTERLY: Accumulate PHP 50,000",
            "ANNUAL: Apply for FDA LTO"
        ]
        for goal in goals:
            g = ttk.Label(goal_frame, text=f" > {goal}")
            g.pack(anchor="w", padx=10, pady=2)

        # Bottom: Treasury
        self.treasury_label = ttk.Label(root, text="TREASURY: PHP 0.00 | SEED: PHP 0.00 (10% Law)", font=("Courier", 10))
        self.treasury_label.pack(pady=20)

        self.update_dashboard()

    def update_dashboard(self):
        # Scan Vaults
        vaults = ['VAULT_1_BLUEPRINT', 'VAULT_2_INFILTRATION', 'VAULT_3_TREASURY']
        self.vault_text.delete('1.0', tk.END)
        total_files = 0
        
        for v in vaults:
            path = f"./{v}"
            files = os.listdir(path) if os.path.exists(path) else []
            self.vault_text.insert(tk.END, f"\n{v}\n{'-'*30}\n")
            for f in sorted(files):
                self.vault_text.insert(tk.END, f"  > {f}\n")
                if v == 'VAULT_1_BLUEPRINT': total_files += 1

        # Calculate Progress
        percent = (total_files / 6) * 100 if total_files <= 6 else 100
        self.progress['value'] = percent
        self.prog_label.config(text=f"EXECUTION PROGRESS: {percent:.1f}%")

if __name__ == "__main__":
    root = tk.Tk()
    app = EmpireGUI(root)
    root.mainloop()
