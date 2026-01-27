import os
import time
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.prompt import Prompt
from rich.align import Align

console = Console()

# --- CONFIGURATION ---
TOOL_NAME = "INJECTOR-X"

EXOTIC_BANNER = """
 ██████╗██╗   ██╗██████╗ ███████╗██████╗ 
██╔════╝╚██╗ ██╔╝██╔══██╗██╔════╝██╔══██╗
██║      ╚████╔╝ ██████╔╝█████╗  ██████╔╝
██║       ╚██╔╝  ██╔══██╗██╔══╝  ██╔══██╗
╚██████╗   ██║   ██████╔╝███████╗██║  ██║
 ╚═════╝   ╚═╝   ╚═════╝ ╚══════╝╚═╝  ╚═╝
"""

def generate_hacker_colors(text_str):
    colored_text = Text()
    colors = ["#004400", "#008800", "#00FF00", "#FFFFFF", "#00FF00", "#00AA00"]
    for i, char in enumerate(text_str):
        color = colors[(i // 4) % len(colors)]
        colored_text.append(char, style=f"bold {color}")
    return colored_text

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
        
        console.print(Align.center(Panel(
            menu_content,
            title="[bold #FFFFFF]─── SECURITY INTERFACE ───[/bold #FFFFFF]",
            border_style="#00FF00",
            padding=(1, 5),
            expand=False
        )))
        
        console.print("\n")
        choice = Prompt.ask(
            "[bold #00FF00]┌───[[/bold #00FF00][bold white]root@injector[/bold white][bold #00FF00]]\n└──╼ [/bold #00FF00]", 
            choices=["1", "2", "3", "4", "5"],
            show_choices=False
        )
        
        if choice == "1":
            console.print("\n[bold #00FF00][!] ACCESSING DOMAIN MODULE...[/bold #00FF00]")
            target = console.input("[bold white] Target URL/IP >> [/bold white]")
            console.print(f"[bold #00FF00][+] Injection des paquets sur {target}...[/bold #00FF00]")
            time.sleep(2)
            console.print("\n[bold white]====>[/bold white] [bold #00FF00]Appuie sur Entrée pour revenir au noyau...[/bold #00FF00]")
            input()
            
        elif choice == "5":
            console.print("[bold red][!] Shutdown sequence initiated...[/bold red]")
            time.sleep(0.5)
            break

if __name__ == "__main__":
    main_menu()