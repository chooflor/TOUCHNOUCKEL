import os
import sys
import subprocess
from rich.console import Console
from rich.panel import Panel

console = Console()

def run_sherlock():
    os.system('cls' if os.name == 'nt' else 'clear')
    console.print(Panel("[bold cyan]OSICHEF - SHERLOCK ENGINE[/bold cyan]", border_style="cyan"))
    
    target = console.input("\n[bold #00FF00]┌───[[/bold #00FF00][bold white]root@osichef[/bold white][bold #00FF00]]\n└──╼ Pseudo cible : [/bold #00FF00]")
    if not target: return

    # Chemins potentiels dans ton repo GitHub
    base_dir = os.path.dirname(os.path.abspath(__file__))
    # Le code source est maintenant souvent dans sherlock_project
    sherlock_path = os.path.join(base_dir, "modules", "sherlock")

    console.print(f"\n[bold yellow][*] Analyse de '{target}' en cours...[/bold yellow]\n")

    try:
        # Tentative 1 : Lancement via le module installé
        result = subprocess.run(["sherlock", target, "--timeout", "5", "--print-found"], shell=True)
        
        # Tentative 2 : Si la commande 'sherlock' n'est pas reconnue, on lance le script local
        if result.returncode != 0:
            script_path = os.path.join(sherlock_path, "sherlock", "sherlock.py")
            if os.path.exists(script_path):
                subprocess.run([sys.executable, script_path, target, "--timeout", "5", "--print-found"])
            else:
                console.print("[red][!] Erreur : Impossible de localiser le moteur Sherlock.[/red]")
                
    except Exception as e:
        console.print(f"[bold red][!] Erreur système : {e}[/bold red]")

if __name__ == "__main__":
    run_sherlock()
    input("\nAppuie sur Entrée pour quitter...")