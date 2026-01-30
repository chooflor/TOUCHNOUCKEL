import os
import sys
import subprocess
from rich.console import Console
from rich.panel import Panel

console = Console()

def run_holehe():
    os.system('cls' if os.name == 'nt' else 'clear')
    console.print(Panel("[bold green]OSICHEF - ENGINE: HOLEHE (EMAIL OSINT)[/bold green]", border_style="green"))
    
    target_email = console.input("\n[bold #00FF00]┌───[[/bold #00FF00][bold white]root@osichef[/bold white][bold #00FF00]]\n└──╼ Email cible : [/bold #00FF00]")
    
    if not target_email:
        return

    # Chemin vers le dossier holehe dans ton GitHub
    base_path = os.path.dirname(os.path.abspath(__file__))
    holehe_root = os.path.join(base_path, "modules", "holehe")

    console.print(f"\n[bold yellow][*] Vérification des réseaux liés à : {target_email}...[/bold yellow]\n")

    try:
        # On tente de lancer holehe via la commande système
        subprocess.run(["holehe", target_email], shell=True)
    except Exception:
        # Plan B : Lancement direct du script si la commande n'est pas dans le PATH
        script_path = os.path.join(holehe_root, "holehe", "core.py") # Note: le point d'entrée peut varier selon les versions
        if os.path.exists(holehe_root):
            # On utilise le module via python -m
            subprocess.run([sys.executable, "-m", "holehe.core", target_email], cwd=holehe_root)
        else:
            console.print("[bold red][!] Erreur : Dossier 'modules/holehe' introuvable.[/bold red]")

if __name__ == "__main__":
    run_holehe()
    input("\nAppuie sur Entrée pour revenir au noyau...")