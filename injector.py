import os
import time
import subprocess
import sys
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.prompt import Prompt
from rich.align import Align

console = Console()

# --- CONFIGURATION VISUELLE ---
EXOTIC_BANNER = """
            ██████╗ ███████╗██╗ ██████╗██╗  ██╗███████╗███████╗
          ██╔═══██╗██╔════╝██║██╔════╝██║  ██║██╔════╝██╔════╝
          ██║   ██║███████╗██║██║     ███████║█████╗  █████╗  
         ██║   ██╝╚════██║██║██║     ██╔══██║██╔══╝  ██╔══╝  
        ╚██████╗ ███████║██║╚██████╗██║  ██║███████╗██║     
        ╚═════╝ ╚══════╝╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝     
"""

def generate_hacker_colors(text_str):
    colored_text = Text()
    colors = ["#004400", "#008800", "#00FF00", "#FFFFFF", "#00FF00", "#00AA00"]
    for i, char in enumerate(text_str):
        color = colors[(i // 4) % len(colors)]
        colored_text.append(char, style=f"bold {color}")
    return colored_text

def execute(script_name):
    """Lance un script en nettoyant l'écran immédiatement pour une transition invisible"""
    if os.path.exists(script_name):
        try:
            os.system('cls' if os.name == 'nt' else 'clear')
            subprocess.run([sys.executable, script_name])
        except Exception as e:
            console.print(f"\n[bold red][!] Erreur Système : {e}[/bold red]")
            input("\nAppuie sur Entrée pour continuer...")
    else:
        console.print(f"\n[bold red][!] Fichier '{script_name}' introuvable.[/bold red]")
        time.sleep(1)

# --- SECTION 1 : SOCIAL NETWORK (Identité & Pseudos) ---
def social_section():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        console.print(Align.center(generate_hacker_colors(EXOTIC_BANNER)))
        
        social_content = (
            "\n[bold #1DA1F2]── RECHERCHE D'IDENTITÉ ──[/bold #1DA1F2]\n"
            " [bold #1DA1F2]1[/bold #1DA1F2] ➔ [white]SHERLOCK ENGINE[/white] [dim](Recherche Pseudos)[/dim]\n"
            " [bold #1DA1F2]2[/bold #1DA1F2] ➔ [white]USERFINDER PRO[/white]\n"
            "\n[bold #1DA1F2]── ANALYSE DE COMPTE ──[/bold #1DA1F2]\n"
            " [bold #1DA1F2]3[/bold #1DA1F2] ➔ [white]FRIENDSHIP LINKER[/white]\n"
            " [bold #1DA1F2]4[/bold #1DA1F2] ➔ [white]DISCORD TOKEN CHECKER[/white]\n"
            " [bold #1DA1F2]5[/bold #1DA1F2] ➔ [white]MASS MEDIA DOWNLOADER[/white]\n"
            "\n [bold white]6[/bold white] ➔ [yellow]RETOUR AU NOYAU[/yellow]\n"
        )
        
        console.print(Align.center(Panel(social_content, title="[bold #1DA1F2][ SOCIAL NETWORK MODULE ][/bold #1DA1F2]", border_style="#1DA1F2", padding=(1, 5), expand=False)))
        choice = Prompt.ask("\n[bold #1DA1F2]┌───[[/bold #1DA1F2][bold white]root@osichef[/bold white][bold #1DA1F2]]\n└──╼ [/bold #1DA1F2]", choices=["1", "2", "3", "4", "5", "6"], show_choices=False)
        
        if choice == "1": execute("user_scan.py")
        elif choice == "4": execute("discord_check.py")
        elif choice == "6": break

# --- SECTION 2 : VIRUS BUILDER ---
def virus_section():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        console.print(Align.center(generate_hacker_colors(EXOTIC_BANNER)))
        virus_content = (
            "\n[bold green]1[/bold green] ➔ [white]RAT BUILDER[/white]\n"
            "[bold green]2[/bold green] ➔ [white]KEYLOGGER ENGINE[/white]\n"
            "\n[bold white]3[/bold white] ➔ [yellow]RETOUR[/yellow]\n"
        )
        console.print(Align.center(Panel(virus_content, title="[bold green][ VIRUS BUILDER ][/bold green]", border_style="green", expand=False)))
        choice = Prompt.ask("\n[bold green]┌───[[/bold green][bold white]root@osichef[/bold white][bold green]]\n└──╼ [/bold green]", choices=["1", "2", "3"], show_choices=False)
        if choice == "3": break

# --- SECTION 3 : ATTACK ---
def attack_section():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        console.print(Align.center(generate_hacker_colors(EXOTIC_BANNER)))
        attack_content = (
            "\n[bold red]1[/bold red] ➔ [white]DDOS ATTACK[/white]\n"
            "[bold red]2[/bold red] ➔ [white]SQL INJECTION[/white]\n"
            "\n[bold white]3[/bold white] ➔ [yellow]RETOUR[/yellow]\n"
        )
        console.print(Align.center(Panel(attack_content, title="[bold red][ ATTACK MODULES ][/bold red]", border_style="red", expand=False)))
        choice = Prompt.ask("\n[bold red]┌───[[/bold red][bold white]root@osichef[/bold white][bold red]]\n└──╼ [/bold red]", choices=["1", "2", "3"], show_choices=False)
        if choice == "3": break

# --- SECTION 4 : OSINT & FACTORY (Coordonnées & Data) ---
def osint_section():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        console.print(Align.center(generate_hacker_colors(EXOTIC_BANNER)))
        
        osint_content = (
            "\n[bold green]── RECHERCHE TECHNIQUE ──[/bold green]\n"
            " [bold green]1[/bold green] ➔ [white]HOLEHE EMAIL INTEL[/white] [dim](Injection Usine)[/dim]\n"
            " [bold green]2[/bold green] ➔ [white]ADDRESS & GEOLOC[/white]\n"
            " [bold green]3[/bold green] ➔ [white]VEHICLE & PLATE RECON[/white]\n"
            " [bold green]4[/bold green] ➔ [white]DISCORD ANALYZER[/white]\n"
            "\n[bold cyan]── CORRÉLATION (L'USINE) ──[/bold cyan]\n"
            " [bold cyan]5[/bold cyan] ➔ [bold cyan]FACTORY REPORT[/bold cyan] [blink]🔥[/blink]\n"
            " [bold cyan]6[/bold cyan] ➔ [white]PURGE DATABASE[/white]\n"
            "\n [bold white]7[/bold white] ➔ [yellow]RETOUR AU NOYAU[/yellow]\n"
        )
        
        console.print(Align.center(Panel(osint_content, title="[bold green][ OSINT & FACTORY ][/bold green]", border_style="green", padding=(1, 5), expand=False)))
        choice = Prompt.ask("\n[bold green]┌───[[/bold green][bold white]root@osichef[/bold white][bold green]]\n└──╼ [/bold green]", choices=["1", "2", "3", "4", "5", "6", "7"], show_choices=False)
        
        if choice == "1": execute("email_intel.py")
        elif choice == "5": execute("factory_report.py")
        elif choice == "7": break

# --- MENU PRINCIPAL ---
def main_menu():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        console.print(Align.center(generate_hacker_colors(EXOTIC_BANNER)))
        console.print(Align.center(Text("⚡ SYSTEM STATUS: OPERATIONAL ⚡", style="bold #00FF00 blink")))
        
        menu_content = (
            "\n[bold #00FF00]1[/bold #00FF00] ➔ [white]SOCIAL NETWORK[/white] [dim](Pseudos)[/dim]\n"
            "[bold #00FF00]2[/bold #00FF00] ➔ [white]VIRUS BUILDER[/white]\n"
            "[bold #00FF00]3[/bold #00FF00] ➔ [white]ATTACK MODULES[/white]\n"
            "[bold #00FF00]4[/bold #00FF00] ➔ [white]OSINT & FACTORY[/white] [dim](Data Engine)[/dim]\n"
            "[bold #00FF00]5[/bold #00FF00] ➔ [white]TOOLS[/white]\n"
            "\n[bold red]6[/bold red] ➔ [bold red]EXIT SYSTEM[/bold red]\n"
        )
        
        console.print(Align.center(Panel(menu_content, title="[bold #FFFFFF]─── OSICHEF SECURITY HUB ───[/bold #FFFFFF]", border_style="#00FF00", padding=(1, 5), expand=False)))
        choice = Prompt.ask("\n[bold #00FF00]┌───[[/bold #00FF00][bold white]root@osichef[/bold white][bold #00FF00]]\n└──╼ [/bold #00FF00]", choices=["1", "2", "3", "4", "5", "6"], show_choices=False)
        
        if choice == "1": social_section()
        elif choice == "2": virus_section()
        elif choice == "3": attack_section()
        elif choice == "4": osint_section()
        elif choice == "6": 
            console.print("[bold red]Déconnexion...[/bold red]")
            time.sleep(1)
            break

if __name__ == "__main__":
    main_menu()