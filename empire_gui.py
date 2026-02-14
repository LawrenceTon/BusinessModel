import os
from datetime import datetime

def run_gui():
    vaults = ['VAULT_1_BLUEPRINT', 'VAULT_2_INFILTRATION', 'VAULT_3_TREASURY']
    print(f"\n{'='*60}")
    print(f" CYBORG_ET | EMPIRE OS v1.0 | {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print(f"{'='*60}\n")
    
    for vault in vaults:
        path = os.path.join("./", vault)
        if not os.path.exists(path):
            os.makedirs(path)
            
        files = os.listdir(path)
        status = "[ACTIVE]" if files else "[EMPTY - ACTION REQUIRED]"
        print(f" {vault:<25} {status}")
        
        for file in sorted(files):
            print(f"   > {file}")
        print("-" * 60)

if __name__ == "__main__":
    run_gui()
