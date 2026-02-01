import os
import sys
import subprocess
from rich.console import Console
from rich.panel import Panel

console = Console()

def run_sherlock():
    os.system('cls' if os.name == 'nt' else 'clear')
    console.print(Panel("[bold cyan]SHERLOCK ENGINE - IDENTITY RECONNAISSANCE[/bold cyan]", border_style="cyan"))
    
    target = console.input("\n[bold #00FF00]┌───[[/bold #00FF00][bold white]root@osichef[/bold white][bold #00FF00]]\n└──╼ Target Username : [/bold #00FF00]")
    if not target: return

    base_dir = os.path.dirname(os.path.abspath(__file__))
    sherlock_path = os.path.join(base_dir, "modules", "sherlock")

    console.print(f"\n[bold yellow][*] Analyzing digital footprint for: {target}...[/bold yellow]\n")

    try:
        # Priority 1: System-wide module
        result = subprocess.run(["sherlock", target, "--timeout", "5", "--print-found"], shell=True)
        
        # Priority 2: Local script fallback
        if result.returncode != 0:
            script_path = os.path.join(sherlock_path, "sherlock", "sherlock.py")
            if os.path.exists(script_path):
                subprocess.run([sys.executable, script_path, target, "--timeout", "5", "--print-found"])
            else:
                console.print("[bold red][!] Error: Sherlock source files not found in modules.[/bold red]")

    except Exception as e:
        console.print(f"[bold red][!] Execution failed: {e}[/bold red]")
    
    input("\n[Scan Completed] Press Enter to return...")

if __name__ == "__main__":
    run_sherlock()