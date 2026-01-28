import os
import time
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.prompt import Prompt
from rich.align import Align

console = Console()

# --- CONFIGURATION ---
TOOL_NAME = "OSICHEF"

# Bannière OSICHEF style Hacker
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

# --- SECTION 1 : SOCIAL NETWORK (Réorganisée) ---
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
        
        console.print(Align.center(Panel(
            social_content, 
            title="[bold #1DA1F2]─── SOCIAL ARCHITECT ───[/bold #1DA1F2]", 
            border_style="#1DA1F2", 
            padding=(1, 5), 
            expand=False
        )))
        
        console.print("\n")
        choice = Prompt.ask(
            "[bold #1DA1F2]┌───[[/bold #1DA1F2][bold white]root@osichef[/bold white][bold #1DA1F2]]\n└──╼ [/bold #1DA1F2]", 
            choices=["1", "2", "3", "4", "5", "6"], show_choices=False
        )
        
        if choice == "6": 
            break
        else:
            console.print(f"\n[bold yellow][!] Module {choice} en attente d'injection...[/bold yellow]")
            time.sleep(1)

# --- SECTION 3 : ATTACK ---
def attack_section():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        console.print(Align.center(generate_hacker_colors(EXOTIC_BANNER)))
        attack_content = (
            "\n[bold red]1[/bold red] ➔ [white]DDOS ATTACK[/white]\n"
            "[bold red]2[/bold red] ➔ [white]SQL INJECTION[/white]\n"
            "[bold white]3[/bold white] ➔ [yellow]BACK TO MAIN CORE[/yellow]\n"
        )
        console.print(Align.center(Panel(attack_content, title="[bold red]─── ATTACK MODULES ───[/bold red]", border_style="red", padding=(1, 5), expand=False)))
        choice = Prompt.ask("\n[bold red]┌───[[/bold red][bold white]root@osichef[/bold white][bold red]]\n└──╼ [/bold red]", choices=["1", "2", "3"], show_choices=False)
        if choice == "3": break

# --- SECTION 4 : OSINT ---
def osint_section():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        console.print(Align.center(generate_hacker_colors(EXOTIC_BANNER)))
        osint_content = (
            "\n[bold green]1[/bold green] ➔ [white]USER LOOKUP[/white]\n"
            "[bold green]2[/bold green] ➔ [white]ADDRESS INTEL[/white]\n"
            "[bold green]3[/bold green] ➔ [white]VEHICLE RECON[/white]\n"
            "[bold green]4[/bold green] ➔ [white]DISCORD ANALYZER[/white]\n"
            "[bold green]5[/bold green] ➔ [white]EMAIL & PHONE[/white]\n"
            "[bold white]6[/bold white] ➔ [yellow]BACK TO MAIN CORE[/yellow]\n"
        )
        console.print(Align.center(Panel(osint_content, title="[bold green]─── OSINT INVESTIGATION ───[/bold green]", border_style="green", padding=(1, 5), expand=False)))
        choice = Prompt.ask("\n[bold green]┌───[[/bold green][bold white]root@osichef[/bold white][bold green]]\n└──╼ [/bold green]", choices=["1", "2", "3", "4", "5", "6"], show_choices=False)
        if choice == "6": break

# --- SECTION 5 : TOOLS ---
def tools_section():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        console.print(Align.center(generate_hacker_colors(EXOTIC_BANNER)))
        tools_content = (
            "\n[bold cyan]1[/bold cyan] ➔ [white]TOOL_NAME_1[/white]\n"
            "[bold cyan]2[/bold cyan] ➔ [white]TOOL_NAME_2[/white]\n"
            "[bold white]3[/bold white] ➔ [yellow]BACK TO MAIN CORE[/yellow]\n"
        )
        console.print(Align.center(Panel(tools_content, title="[bold cyan]─── UTILITY BOX ───[/bold cyan]", border_style="cyan", padding=(1, 5), expand=False)))
        choice = Prompt.ask("\n[bold cyan]┌───[[/bold cyan][bold white]root@osichef[/bold white][bold cyan]]\n└──╼ [/bold cyan]", choices=["1", "2", "3"], show_choices=False)
        if choice == "3": break

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
            "[bold red]6[/bold red] ➔ [bold red]EXIT[/bold red]\n"
        )
        
        console.print(Align.center(Panel(menu_content, title="[bold #FFFFFF]─── SECURITY INTERFACE ───[/bold #FFFFFF]", border_style="#00FF00", padding=(1, 5), expand=False)))
        
        console.print("\n")
        choice = Prompt.ask(
            "[bold #00FF00]┌───[[/bold #00FF00][bold white]root@osichef[/bold white][bold #00FF00]]\n└──╼ [/bold #00FF00]", 
            choices=["1", "2", "3", "4", "5", "6"], show_choices=False
        )
        
        if choice == "1": social_section()
        elif choice == "2": console.print("\n[yellow][!] Module Virus Builder bientôt disponible...[/yellow]"); time.sleep(1)
        elif choice == "3": attack_section()
        elif choice == "4": osint_section()
        elif choice == "5": tools_section()
        elif choice == "6": 
            console.print("[bold red][!] Shutdown sequence initiated...[/bold red]")
            time.sleep(0.5)
            break

if __name__ == "__main__":
    main_menu()