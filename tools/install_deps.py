import os
import sys
import platform
import subprocess
from rich.console import Console

console = Console()

def is_command_installed(command):
    try:
        subprocess.run([command, "--version"], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False

def install_git():
    system = platform.system()
    try:
        if system == "Windows":
            console.print("[*] Installing Git (Windows)...", style="bold yellow")
            subprocess.check_call(["winget", "install", "--id", "Git.Git", "-e", "--source", "winget"])
        elif system == "Linux":
            console.print("[*] Installing Git (Linux)...", style="bold yellow")
            subprocess.check_call(["sudo", "apt", "install", "-y", "git"])
        else:
            console.print("[!] Unsupported OS for Git install.", style="bold red")
            return False
        return True
    except Exception as e:
        console.print(f"[!] Failed to install Git: {e}", style="bold red")
        return False

def install_nmap():
    if is_command_installed("nmap"):
        console.print("[*] Nmap is already installed.", style="bold green")
        return

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
        subprocess.check_call([sys.executable, "-m", "pip", "install", "rich", "requests", "dnspython", "holehe", "sherlock-project"])
        console.print("[+] Python dependencies installed.", style="bold green")
    except Exception as e:
        console.print(f"[!] Failed to install dependencies: {e}", style="bold red")

def clone_modules():
    if not is_command_installed("git"):
        console.print("[!] Git not found. Installing Git...", style="bold red")
        if not install_git():
            console.print("[!] Git install failed. Skipping module cloning.", style="bold red")
            return

    sherlock_path = os.path.join("modules", "sherlock")
    if not os.path.exists(sherlock_path):
        console.print("[*] Cloning Sherlock...", style="bold yellow")
        os.makedirs("modules", exist_ok=True)
        try:
            subprocess.check_call(["git", "clone", "https://github.com/sherlock-project/sherlock.git", sherlock_path])
        except Exception as e:
            console.print(f"[!] Failed to clone Sherlock: {e}", style="bold red")
    else:
        console.print("[*] Updating Sherlock...", style="bold yellow")
        try:
            subprocess.check_call(["git", "-C", sherlock_path, "pull"])
        except Exception as e:
            console.print(f"[!] Failed to update Sherlock: {e}", style="bold red")

    holehe_path = os.path.join("modules", "holehe")
    if not os.path.exists(holehe_path):
        console.print("[*] Cloning Holehe...", style="bold yellow")
        try:
            subprocess.check_call(["git", "clone", "https://github.com/megadose/holehe.git", holehe_path])
        except Exception as e:
            console.print(f"[!] Failed to clone Holehe: {e}", style="bold red")
    else:
        console.print("[*] Updating Holehe...", style="bold yellow")
        try:
            subprocess.check_call(["git", "-C", holehe_path, "pull"])
        except Exception as e:
            console.print(f"[!] Failed to update Holehe: {e}", style="bold red")

def main():
    console.print("[+] Starting dependency setup...", style="bold green")
    install_python_deps()
    clone_modules()
    install_nmap()
    console.print("[+] All dependencies are ready!", style="bold green")
    input("\nPress ENTER to return...")

if __name__ == "__main__":
    main()