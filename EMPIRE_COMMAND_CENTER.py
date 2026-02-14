import os
from datetime import datetime

class UnifiedEmpireOS:
    def __init__(self):
        self.vaults = ['VAULT_1_BLUEPRINT', 'VAULT_2_INFILTRATION', 'VAULT_3_TREASURY']
        self.goals = {
            "Daily": "Contact 50 Prospects via 07_ZERO_BUDGET_SCRIPT",
            "Monthly": "Secure 1 Lead Generation Deal",
            "Quarterly": "Accumulate PHP 50,000 Seed Capital",
            "Annual": "Apply for FDA License to Operate (LTO)"
        }

    def get_vault_status(self):
        status_data = {}
        for v in self.vaults:
            files = os.listdir(f'./{v}') if os.path.exists(f'./{v}') else []
            status_data[v] = files
        return status_data

    def display(self):
        vault_data = self.get_vault_status()
        v1_files = len(vault_data['VAULT_1_BLUEPRINT'])
        # Completion based on 6 core blueprint docs + initial infiltration docs
        prog = (v1_files / 6) * 100 if v1_files <= 6 else 100
        
        print(f"\n{'='*70}")
        print(f" CYBORG_ET | UNIFIED EMPIRE COMMAND | {datetime.now().strftime('%Y-%m-%d %H:%M')}")
        print(f"{'='*70}")
        
        print(f"\n[1. STRATEGIC VAULT STATUS]")
        for vault, files in vault_data.items():
            status = "[ACTIVE]" if files else "[EMPTY - ACTION REQUIRED]"
            print(f" {vault:<25} {status}")
            for f in sorted(files):
                print(f"   > {f}")

        print(f"\n[2. EXECUTION PROGRESS: {prog:.1f}%]")
        # ASCII characters used for terminal compatibility
        bar = "#" * int(prog/5) + "-" * (20 - int(prog/5))
        print(f" [{bar}]")

        print(f"\n[3. GOAL ARCHITECTURE & NEXT STEPS]")
        for period, goal in self.goals.items():
            print(f" {period:<10}: {goal}")

        print(f"\n[4. TREASURY LEDGER (10% LAW)]")
        print(" > Total Inflow: PHP 0.00  |  Seed Reserve: PHP 0.00")
        print(f"{'='*70}\n")

if __name__ == "__main__":
    app = UnifiedEmpireOS()
    app.display()
