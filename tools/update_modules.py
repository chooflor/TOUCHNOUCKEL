# tools/update_modules.py
import os
import subprocess
from rich.console import Console

console = Console()

def update_modules():
    console.print("[*] Updating Sherlock...", style="bold yellow")
    sherlock_path = os.path.join("modules", "sherlock")
    if os.path.exists(sherlock_path):
        subprocess.run(["git", "-C", sherlock_path, "pull"])
    else:
        console.print("[!] Sherlock not found.", style="bold red")

    console.print("[*] Updating Holehe...", style="bold yellow")
    holehe_path = os.path.join("modules", "holehe")
    if os.path.exists(holehe_path):
        subprocess.run(["git", "-C", holehe_path, "pull"])
    else:
        console.print("[!] Holehe not found.", style="bold red")

    console.print("[+] Modules updated.", style="bold green")
    input("\nPress ENTER to return...")

if __name__ == "__main__":
    update_modules()
