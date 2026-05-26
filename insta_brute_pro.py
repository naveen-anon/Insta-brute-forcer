import time
import sys
import random
import os
import datetime

# Professional High-Tech Terminal Colors
GREEN = '\033[92m'
RED = '\033[91m'
YELLOW = '\033[93m'
CYAN = '\033[96m'
WHITE = '\033[97m'
GRAY = '\033[90m'
RESET = '\033[0m'

def generate_massive_wordlist():
    if not os.path.exists("massive_wordlist.txt"):
        words = ["password", "instagram", "admin", "login", "shadow", "cyber", "hidden", "secure", "hacker", "system"]
        chars = ["123", "2024", "2025", "2026", "007", "!", "@", "#"]
        
        with open("massive_wordlist.txt", "w") as f:
            for w in words:
                for c1 in chars:
                    for c2 in chars:
                        f.write(f"{w}{c1}{c2}\n")
                        f.write(f"{c1}{w}{c2}\n")
                        f.write(f"{w.capitalize()}{c1}\n")

def get_timestamp():
    return datetime.datetime.now().strftime("%H:%M:%S")

def run_advanced_simulation():
    generate_massive_wordlist()
    
    # --- PRO DESIGNER BANNER WITH YOUR CREDENTIALS ---
    print(f"{CYAN}=======================================================================")
    print(f"    ⚡ INSTAGRAM BRUTE-FORCE ATTACKING TOOL // AUTOMATED CLI v5.2 ⚡   ")
    print(f"=======================================================================")
    print(f"{WHITE}  [•] Developer : {GREEN}Naveen Khatri")
    print(f"{WHITE}  [•] Instagram : {YELLOW}@coding_with_naveen")
    print(f"{WHITE}  [•] GitHub    : {CYAN}@naveen-anon")
    print(f"{CYAN}======================================================================={RESET}\n")
    
    # Input Target
    username = input(f"{WHITE}[?] Enter Target Instagram Username: @{RESET}").strip()
    if not username:
        print(f"{RED}[-] Error: Target identifier cannot be blank.{RESET}")
        return

    # Phase 1: Environment Setup
    print(f"\n{GRAY}[{get_timestamp()}] [INFO] Initializing Brute-Force Framework...{RESET}")
    time.sleep(1.2)
    print(f"{GRAY}[{get_timestamp()}] [INFO] Establishing multi-routing Tor Proxy Chains...{RESET}")
    time.sleep(1.5)
    print(f"{GREEN}[✓] 5 Proxy Nodes Configured Successfully (Tunnel Latency < 32ms){RESET}")
    
    # Phase 2: Metadata Fetching
    print(f"\n{GRAY}[{get_timestamp()}] [INFO] Connecting to Instagram Graph API v21.0...{RESET}")
    time.sleep(2)
    target_uid = random.randint(50000000, 99999999)
    print(f"{GRAY}[{get_timestamp()}] [DATA] Target Identity Verified: Node-ID [{target_uid}]{RESET}")
    print(f"{GRAY}[{get_timestamp()}] [DATA] Security Protocol: SHA-256 Double Salted Authentication{RESET}")
    time.sleep(1)
    
    # Wordlist Status
    total_lines = len(open('massive_wordlist.txt').readlines())
    print(f"\n{YELLOW}[*] Payload Loaded: 'massive_wordlist.txt' ({total_lines:,} Vectors){RESET}")
    print(f"{RED}[!] Starting Brute-Force Attack Vectors. Press Ctrl+C to Safe-Abort.{RESET}\n")
    time.sleep(2.5)
    
    start_time = time.time()
    attempts = 0
    
    # Custom target password
    custom_password = "1@3#6₹8&2$$"
    
    # Phase 3: High-Speed Bruteforce Stream
    with open("massive_wordlist.txt", "r") as wordlist:
        for line in wordlist:
            password = line.strip()
            attempts += 1
            
            # Simulated Proxy Hop
            if attempts % 120 == 0:
                fake_ip = f"{random.randint(45,190)}.{random.randint(10,254)}.{random.randint(2,254)}.{random.randint(20,99)}"
                sys.stdout.write(f"\n{YELLOW}[{get_timestamp()}] [WARN] Rate limit threshold reached. Rotating Tunnel -> IP: {fake_ip}{RESET}\n")
                time.sleep(0.4)
            
            # Live CLI Output Stream
            sys.stdout.write(
                f"\r{GRAY}[Count: {attempts:,}]{RESET} "
                f"Testing: {password:<22} | "
                f"Response: {RED}401-Unauthorized (Auth Fail){RESET}"
            )
            sys.stdout.flush()
            
            time.sleep(0.002)
            
            # --- FIX: Trigger point ko 1500 par set kiya hai taaki loop khatam hone se pehle chale ---
            if attempts == 1500:
                print("\n")
                print(f"{GREEN}[{get_timestamp()}] [!] MATCH FOUND! Injecting payload and terminating threads...{RESET}")
                time.sleep(2)
                
                # Attack Success Banner
                print(f"\n{GREEN}=====================================================================")
                print(f"             💥 BRUTE-FORCE ATTACK SUCCESSFULLY COMPLETED 💥         ")
                print(f"=====================================================================")
                print(f"  [+] Attack Status    : {RED}TARGET COMPROMISED{GREEN}")
                print(f"  [+] Target Account   : @{username}")
                print(f"  [+] Compromised Key  : {WHITE}{custom_password}{GREEN}")
                print(f"  [+] Total Attempts   : {attempts:,} Vectors")
                print(f"  [+] Engine Signature : NK-BruteForce/v5.2")
                print(f"  [+] Execution Time   : {time.time() - start_time:.2f} Seconds")
                print(f"=====================================================================")
                print(f"{GRAY}Developed by Naveen Khatri // Github: @naveen-anon // Insta: @coding_with_naveen{RESET}\n")
                return

    print(f"\n{RED}[-] Brute-force terminated. Wordlist exhausted without matching.{RESET}\n")

if __name__ == "__main__":
    try:
        run_advanced_simulation()
    except KeyboardInterrupt:
        print(f"\n\n{RED}[!] Operations suspended by operator. Flushing memory logs...{RESET}\n")
                  
