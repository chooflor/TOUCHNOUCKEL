import os
from rich.console import Console
from factory_core import get_report

console = Console()

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    # Appel de la fonction de rapport centralisée
    get_report()
    
    console.print("\n[dim]Appuie sur Entrée pour fermer le rapport et retourner au menu...[/dim]")
    input()

if __name__ == "__main__":
    main()