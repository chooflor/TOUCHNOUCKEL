# tools/nmap_scan.py
import os
import subprocess
from rich.console import Console
from rich.panel import Panel

console = Console()

def run_nmap_scan():
    os.system('cls' if os.name == 'nt' else 'clear')
    console.print(Panel("[bold red]─── NMAP SCANNER ───[/bold red]", border_style="red"))

    target = console.input("\n[bold red]┌───[[/bold red][bold white]root@osichef[/bold white][bold red]]\n├──╼ Target IP/Domain : [/bold red]").strip()
    if not target:
        console.print("[bold red][!] No target provided.[/bold red]")
        input("\nPress Enter to return...")
        return

    scan_type = console.input("[bold red]└──╼ Scan Type ([1] Quick, [2] Full, [3] Custom) : [/bold red]").strip()

    cmd = ["nmap", "-Pn"]
    if scan_type == "1":
        cmd += ["-F", target]
    elif scan_type == "2":
        cmd += ["-p-", target]
    elif scan_type == "3":
        custom_args = console.input("[bold red]└──╼ Custom Args (ex: -sV -A -p 22,80,443) : [/bold red]").strip()
        cmd += custom_args.split() + [target]
    else:
        cmd += ["-F", target]

    console.print(f"\n[bold yellow][*] Running: {' '.join(cmd)}[/bold yellow]\n")

    try:
        result = subprocess.run(cmd, capture_output=True, text=True)
        console.print("[bold green]Scan Results:[/bold green]")
        console.print(result.stdout)
        if result.stderr:
            console.print("[bold red]Errors:[/bold red]")
            console.print(result.stderr)
    except FileNotFoundError:
        console.print("[bold red][!] Nmap is not installed or not in PATH.[/bold red]")
    except Exception as e:
        console.print(f"[bold red][!] Error: {e}[/bold red]")

    input("\nPress Enter to return...")

if __name__ == "__main__":
    run_nmap_scan()
