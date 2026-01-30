import os
import sys
import subprocess
from rich.console import Console
from rich.panel import Panel
from factory_core import add_data

console = Console()

def run_scanner():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        
        # Interface de demande propre
        console.print(Panel.fit(
            "[bold cyan]SHERLOCK ENGINE - IDENTITY SEARCH[/bold cyan]\n"
            "[dim]Enregistrement automatique des correspondances dans l'usine.[/dim]",
            border_style="cyan"
        ))

        target = console.input("\n[bold #1DA1F2]┌───[[/bold #1DA1F2][bold white]root@osichef[/bold white][bold #1DA1F2]]\n└──╼ Pseudo (ou 'q' pour quitter) : [/bold #1DA1F2]").strip()

        if target.lower() == 'q' or not target:
            break

        console.print(f"\n[bold yellow][*] Scan de '{target}' en cours...[/bold yellow]\n")

        # Configuration des chemins
        root = os.path.join("modules", "sherlock")
        # Chemin direct vers le script pour éviter l'erreur "No module named sherlock"
        script_path = os.path.join(root, "sherlock", "sherlock.py")

        try:
            # On vérifie si le fichier existe avant de lancer
            if not os.path.exists(script_path):
                console.print(f"[bold red][!] Erreur : Fichier introuvable dans {script_path}[/bold red]")
                console.print("[yellow][*] Tentative d'installation automatique...[/yellow]")
                subprocess.run([sys.executable, "-m", "pip", "install", "."], cwd=root)
            
            # Lancement avec capture en temps réel
            process = subprocess.Popen(
                [sys.executable, script_path, target, "--timeout", "5", "--print-found"],
                cwd=root, 
                stdout=subprocess.PIPE, 
                stderr=subprocess.STDOUT, 
                text=True, 
                encoding='utf-8',
                errors='replace'
            )

            # Lecture et injection Usine
            for line in process.stdout:
                clean_line = line.strip()
                if clean_line:
                    print(clean_line)
                    if "Found!" in clean_line:
                        # Extraction du nom du site (ex: Instagram)
                        try:
                            site = clean_line.split(':')[0].replace('[+]', '').strip().lower()
                            add_data(site, "sherlock")
                        except:
                            pass

            process.wait()
            console.print(f"\n[bold green][+] Scan terminé. Données injectées dans l'usine.[/bold green]")
            input("\nAppuie sur Entrée pour scanner un autre pseudo...")
            
        except Exception as e:
            console.print(f"[bold red][!] Erreur critique : {e}[/bold red]")
            input("\nAppuie sur Entrée pour continuer...")

if __name__ == "__main__":
    run_scanner()