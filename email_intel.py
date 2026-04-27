import os
import sys
import subprocess
from rich.console import Console
from rich.panel import Panel

console = Console()

def run_holehe():
    os.system('cls' if os.name == 'nt' else 'clear')
    console.print(Panel("[bold green]HOLEHE ENGINE - EMAIL INTELLIGENCE[/bold green]", border_style="green"))
    
    target_email = console.input("\n[bold #00FF00]┌───[[/bold #00FF00][bold white]root@osichef[/bold white][bold #00FF00]]\n└──╼ Target Email : [/bold #00FF00]")
    
    if not target_email:
        return

    base_path = os.path.dirname(os.path.abspath(__file__))
    holehe_root = os.path.join(base_path, "modules", "holehe")

    console.print(f"\n[bold yellow][*] Investigating registered accounts for: {target_email}...[/bold yellow]\\n")

    try:
        # Priority 1: System-wide command
        subprocess.run(["holehe", target_email], shell=True)
    except Exception:
        # Priority 2: Local core script fallback
        script_path = os.path.join(holehe_root, "holehe", "core.py")
        if os.path.exists(script_path):
            subprocess.run([sys.executable, script_path, target_email])
        else:
            console.print("[bold red][!] Error: Holehe engine not found in modules.[/bold red]")

    input("\n[Intelligence Gathering Completed] Press Enter to return...")

if __name__ == "__main__":
    run_holehe()