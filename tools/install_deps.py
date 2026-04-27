# tools/install_deps.py
import os
import sys
import platform
import subprocess
from rich.console import Console

console = Console()

def install_nmap():
    system = platform.system()
    try:
        if system == "Windows":
            console.print("[*] Installing Nmap (Windows)...", style="bold yellow")
            subprocess.check_call(["winget", "install", "nmap"])
        elif system == "Linux":
            console.print("[*] Installing Nmap (Linux)...", style="bold yellow")
            subprocess.check_call(["sudo", "apt", "install", "-y", "nmap"])
        else:
            console.print("[!] Unsupported OS for auto Nmap install.", style="bold red")
    except Exception as e:
        console.print(f"[!] Failed to install Nmap: {e}", style="bold red")

def install_python_deps():
    console.print("[*] Installing Python dependencies...", style="bold yellow")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "rich", "requests", "dnspython"])
        console.print("[+] Python dependencies installed.", style="bold green")
    except Exception as e:
        console.print(f"[!] Failed to install dependencies: {e}", style="bold red")

def clone_modules():
    # Sherlock
    sherlock_path = os.path.join("modules", "sherlock")
    if not os.path.exists(sherlock_path):
        console.print("[*] Cloning Sherlock...", style="bold yellow")
        os.makedirs("modules", exist_ok=True)
        subprocess.check_call(["git", "clone", "https://github.com/sherlock-project/sherlock.git", sherlock_path])
    else:
        console.print("[*] Updating Sherlock...", style="bold yellow")
        subprocess.check_call(["git", "-C", sherlock_path, "pull"])

    # Holehe
    holehe_path = os.path.join("modules", "holehe")
    if not os.path.exists(holehe_path):
        console.print("[*] Cloning Holehe...", style="bold yellow")
        subprocess.check_call(["git", "clone", "https://github.com/megadose/holehe.git", holehe_path])
    else:
        console.print("[*] Updating Holehe...", style="bold yellow")
        subprocess.check_call(["git", "-C", holehe_path, "pull"])

def main():
    console.print("[+] Starting dependency setup...", style="bold green")
    install_python_deps()
    clone_modules()
    install_nmap()
    console.print("[+] All dependencies are ready!", style="bold green")
    input("\nPress ENTER to return...")

if __name__ == "__main__":
    main()
