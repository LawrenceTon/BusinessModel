import os
import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime

class InteractiveEmpireGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("CYBORG_ET | INTERACTIVE EMPIRE COMMAND | v4.0")
        self.root.geometry("1100x700")
        self.root.configure(bg="#0a0a0a")
        
        self.inflow = 0.0
        self.seed = 0.0

        # Styles
        style = ttk.Style()
        style.theme_use('clam')
        style.configure("TFrame", background="#0a0a0a")
        style.configure("TLabel", background="#0a0a0a", foreground="#00ff00", font=("Courier", 10))
        style.configure("Header.TLabel", font=("Courier", 20, "bold"), foreground="#00ff00")

        # Header
        ttk.Label(root, text="SYSTEM STATUS: DOMINANCE ENGAGED", style="Header.TLabel").pack(pady=10)

        # Main Layout
        self.paned = ttk.Panedwindow(root, orient=tk.HORIZONTAL)
        self.paned.pack(fill="both", expand=True, padx=20, pady=10)

        # Left: File Explorer
        self.file_frame = ttk.LabelFrame(self.paned, text=" [ STRATEGIC VAULTS ] ")
        self.paned.add(self.file_frame, weight=1)
        
        self.tree = ttk.Treeview(self.file_frame, columns=("Type"), show="tree")
        self.tree.pack(fill="both", expand=True)
        self.tree.bind("<Double-1>", self.on_file_click)

        # Middle: Content Viewer
        self.content_frame = ttk.LabelFrame(self.paned, text=" [ DATA STREAM ] ")
        self.paned.add(self.content_frame, weight=2)
        
        self.content_text = tk.Text(self.content_frame, bg="#0f0f0f", fg="#00ff00", font=("Courier", 10), state='disabled')
        self.content_text.pack(fill="both", expand=True)

        # Right: Control Panel
        self.control_frame = ttk.Frame(self.paned)
        self.paned.add(self.control_frame, weight=1)

        # Treasury Input
        input_frame = ttk.LabelFrame(self.control_frame, text=" [ TRANSACTION TERMINAL ] ")
        input_frame.pack(fill="x", padx=5, pady=5)
        
        ttk.Label(input_frame, text="Amount (PHP):").pack(pady=2)
        self.amount_entry = ttk.Entry(input_frame)
        self.amount_entry.pack(pady=5)
        
        ttk.Button(input_frame, text="LOG INFLOW", command=self.log_money).pack(pady=5)

        # Metrics
        self.metrics_label = ttk.Label(self.control_frame, text="TREASURY DATA:\nInflow: 0.00\nSeed: 0.00", font=("Courier", 11, "bold"))
        self.metrics_label.pack(pady=20)

        self.refresh_tree()

    def refresh_tree(self):
        for item in self.tree.get_children(): self.tree.delete(item)
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
            self.content_text.config(state='normal')
            self.content_text.delete('1.0', tk.END)
            self.content_text.insert(tk.END, content)
            self.content_text.config(state='disabled')

    def log_money(self):
        try:
            val = float(self.amount_entry.get())
            self.inflow += val
            self.seed += val * 0.10
            self.metrics_label.config(text=f"TREASURY DATA:\nInflow: {self.inflow:,.2f}\nSeed: {self.seed:,.2f}")
            self.amount_entry.delete(0, tk.END)
            messagebox.showinfo("Dominance", f"PHP {val} Logged. {val*0.10} Harvested for Seed.")
        except:
            messagebox.showerror("Error", "Invalid numeric input.")

if __name__ == "__main__":
    root = tk.Tk()
    app = InteractiveEmpireGUI(root)
    root.mainloop()
