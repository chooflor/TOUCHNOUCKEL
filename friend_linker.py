import os
import time
import requests
import webbrowser
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

console = Console()

def run_linker():
    os.system('cls' if os.name == 'nt' else 'clear')
    
    console.print(Panel.fit(
        "[bold #1DA1F2]FRIENDSHIP LINKER[/bold #1DA1F2]\n"
        "[white]Est-ce que ces deux personnes se connaissent ?[/white]",
        border_style="#1DA1F2"
    ))

    console.print("\n[yellow]Entrez les PSEUDOS exacts (ex: instagram, twitter, jeux video)[/yellow]")
    
    user1 = console.input("\n[bold #1DA1F2]┌───[[/bold #1DA1F2][bold white]root@osichef[/bold white][bold #1DA1F2]]\n├──╼ Premier Pseudo : [/bold #1DA1F2]").strip()
    user2 = console.input("[bold #1DA1F2]└──╼ Deuxième Pseudo : [/bold #1DA1F2]").strip()

    if not user1 or not user2:
        return

    console.print(f"\n[bold yellow][*] Recherche de liens entre '{user1}' et '{user2}'...[/bold yellow]\n")

    # On prépare le tableau des résultats simplifiés
    table = Table(header_style="bold cyan")
    table.add_column("Ce qu'on cherche", style="white")
    table.add_column("Lien de preuve (Clique dessus)", style="blue underline")

    # Liste des recherches simplifiées
    searches = [
        ("Discutent-ils ensemble ?", f'https://www.google.com/search?q="{user1}"+"AND+"{user2}"'),
        ("Se parlent-ils sur Twitter ?", f'https://www.google.com/search?q=site:twitter.com+"{user1}"+"{user2}"'),
        ("Sont-ils identifiés sur Insta ?", f'https://www.google.com/search?q=site:instagram.com+"{user1}"+"{user2}"'),
        ("Sont-ils sur le même forum ?", f'https://www.google.com/search?q="{user1}"+"{user2}"+site:forum.*'),
        ("Mentions sur Reddit", f'https://www.google.com/search?q=site:reddit.com+"{user1}"+"{user2}"')
    ]

    for desc, link in searches:
        table.add_row(desc, link)

    console.print(table)
    
    console.print("\n[dim]Conseil : Si Google affiche des résultats, c'est qu'il existe un lien entre eux.[/dim]")
    
    # Demande pour ouvrir tout d'un coup
    if console.input("\n[bold green]Voulez-vous ouvrir toutes les recherches maintenant ? (y/n) : [/bold green]").lower() == 'y':
        for _, link in searches:
            webbrowser.open(link)
            time.sleep(0.5)

    input("\nAppuie sur Entrée pour revenir...")

if __name__ == "__main__":
    run_linker()