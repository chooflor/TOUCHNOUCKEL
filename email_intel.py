# email_intel.py
import subprocess
import sys
import os
from rich.console import Console

console = Console()

def run_holehe():
    console.print("[bold yellow][*] Recherche des comptes associés à un email...[/bold yellow]")
    email = console.input("\n[bold yellow]┌───[[/bold yellow][bold white]root@osichef[/bold white][bold yellow]]\n└──╼ Email : [/bold yellow]").strip()
    if not email:
        console.print("[bold red][!] Aucun email saisi.[/bold red]")
        input("\nAppuie sur Entrée pour continuer...")
        return

    # Chemin vers Holehe dans modules/
    holehe_dir = os.path.join("modules", "holehe")
    holehe_main = os.path.join(holehe_dir, "holehe", "main.py")

    # Vérifie si Holehe existe localement
    if not os.path.exists(holehe_main):
        console.print("[bold red][!] Holehe non trouvé dans modules/holehe. Lance install_deps.py[/bold red]")
        input("\nAppuie sur Entrée pour continuer...")
        return

    console.print(f"[bold cyan][*] Lancement de Holehe pour : {email}[/bold cyan]")

    try:
        # Exécute Holehe avec Python
        result = subprocess.run([
            sys.executable,
            holehe_main,
            email,
            "--no-color"
        ], cwd=holehe_dir, capture_output=True, text=True)

        # Affiche le résultat
        if result.stdout:
            print(result.stdout)
        if result.stderr:
            print(result.stderr)

    except Exception as e:
        console.print(f"[bold red][!] Erreur : {e}[/bold red]")

    input("\nAppuie sur Entrée pour continuer...")

if __name__ == "__main__":
    run_holehe()
