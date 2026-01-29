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

# --- CONFIGURATION ---
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
    """Lance un script externe situé dans le même dossier"""
    if os.path.exists(script_name):
        try:
            console.print(f"\n[bold cyan][*] Initialisation du module : {script_name}...[/bold cyan]")
            time.sleep(1)
            # On utilise sys.executable pour s'assurer d'utiliser le même Python que le menu
            subprocess.run([sys.executable, script_name])
        except Exception as e:
            console.print(f"\n[bold red][!] Erreur lors de l'exécution : {e}[/bold red]")
            input("\nAppuie sur Entrée pour continuer...")
    else:
        console.print(f"\n[bold red][!] ERREUR : Le fichier '{script_name}' est introuvable.[/bold red]")
        console.print(f"[dim]Assure-toi que '{script_name}' est dans le dossier : {os.getcwd()}[/dim]")
        time.sleep(3)

# --- SECTION 1 : SOCIAL NETWORK ---
def social_section():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        console.print(Align.center(generate_hacker_colors(EXOTIC_BANNER)))
        
        social_content = (
            "\n[bold #1DA1F2]── INVESTIGATION ──[/bold #1DA1F2]\n"
            " [bold #1DA1F2]1[/bold #1DA1F2] ➔ [white]USERNAME SCANNER[/white]\n"
            " [bold #1DA1F2]2[/bold #1DA1F2] ➔ [white]USERFINDER[/white]\n"
            "\n[bold #1DA1F2]── ANALYSIS ──[/bold #1DA1F2]\n"
            " [bold #1DA1F2]3[/bold #1DA1F2] ➔ [white]FRIENDSHIP LINKER[/white]\n"
            " [bold #1DA1F2]4[/bold #1DA1F2] ➔ [white]DISCORD TOKEN CHECKER[/white]\n"
            "\n[bold #1DA1F2]── EXTRACTION ──[/bold #1DA1F2]\n"
            " [bold #1DA1F2]5[/bold #1DA1F2] ➔ [white]MASS DOWNLOADER[/white]\n"
            "\n [bold white]6[/bold white] ➔ [yellow]BACK TO MAIN CORE[/yellow]\n"
        )
        
        console.print(Align.center(Panel(social_content, title="[bold #1DA1F2]─── SOCIAL ARCHITECT ───[/bold #1DA1F2]", border_style="#1DA1F2", padding=(1, 5), expand=False)))
        
        choice = Prompt.ask("\n[bold #1DA1F2]┌───[[/bold #1DA1F2][bold white]root@osichef[/bold white][bold #1DA1F2]]\n└──╼ [/bold #1DA1F2]", choices=["1", "2", "3", "4", "5", "6"], show_choices=False)
        
        if choice == "1":
            # C'est ici que la magie opère : on appelle le fichier externe
            execute("user_scan.py")
        elif choice == "6": 
            break
        else:
            console.print(f"\n[bold yellow][!] Module {choice} non lié ou en développement...[/bold yellow]")
            time.sleep(1.5)

# --- LES AUTRES SECTIONS (Vides pour l'instant) ---
def virus_builder_section():
    # ... (Garde ton code précédent ici)
    pass

def attack_section():
    # ... (Garde ton code précédent ici)
    pass

def osint_section():
    # ... (Garde ton code précédent ici)
    pass

def tools_section():
    # ... (Garde ton code précédent ici)
    pass

# --- MENU PRINCIPAL ---
def main_menu():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        console.print(Align.center(generate_hacker_colors(EXOTIC_BANNER)))
        console.print(Align.center(Text("⚡ SYSTEM STATUS: OPERATIONAL ⚡", style="bold #00FF00 blink")))
        
        menu_content = (
            "\n[bold #00FF00]1[/bold #00FF00] ➔ [white]SOCIAL NETWORK[/white]\n"
            "[bold #00FF00]2[/bold #00FF00] ➔ [white]VIRUS BUILDER[/white]\n"
            "[bold #00FF00]3[/bold #00FF00] ➔ [white]ATTACK[/white]\n"
            "[bold #00FF00]4[/bold #00FF00] ➔ [white]OSINT[/white]\n"
            "[bold #00FF00]5[/bold #00FF00] ➔ [white]TOOLS[/white]\n"
            "\n[bold red]6[/bold red] ➔ [bold red]EXIT[/bold red]\n"
        )
        
        console.print(Align.center(Panel(menu_content, title="[bold #FFFFFF]─── SECURITY INTERFACE ───[/bold #FFFFFF]", border_style="#00FF00", padding=(1, 5), expand=False)))
        
        choice = Prompt.ask("\n[bold #00FF00]┌───[[/bold #00FF00][bold white]root@osichef[/bold white][bold #00FF00]]\n└──╼ [/bold #00FF00]", choices=["1", "2", "3", "4", "5", "6"], show_choices=False)
        
        if choice == "1": social_section()
        elif choice == "2": virus_builder_section()
        elif choice == "3": attack_section()
        elif choice == "4": osint_section()
        elif choice == "5": tools_section()
        elif choice == "6": break

if __name__ == "__main__":
    main_menu()