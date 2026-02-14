import os
from datetime import datetime

def display_status():
    vault_path = "./"
    print(f"--- CYBORG_ET EMPIRE OS | {datetime.now().strftime('%Y-%m-%d %H:%M')} ---")
    
    for folder in ['VAULT_1_BLUEPRINT', 'VAULT_2_INFILTRATION', 'VAULT_3_TREASURY']:
        files = os.listdir(os.path.join(vault_path, folder))
        status = "[ACTIVE]" if files else "[EMPTY - ACTION REQUIRED]"
        print(f"{folder}: {status}")
        for f in files:
            print(f"  > {f}")
    print("-" * 50)

if __name__ == "__main__":
    display_status()