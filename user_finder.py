import os
import sys
import time
import requests
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

console = Console()

# Configuration pour imiter un vrai navigateur (Anti-Blocage)
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

def check_site(name, url_template, target, table):
    url = url_template.format(target)
    try:
        # Petite pause de sécurité
        time.sleep(0.5)
        
        response = requests.get(url, headers=HEADERS, timeout=5)
        
        # Codes de réussite courants
        if response.status_code == 200:
            table.add_row(name, "[bold green]FOUND[/bold green]", url)
        elif response.status_code == 404:
            table.add_row(name, "[dim red]NOT FOUND[/dim red]", "-")
        else:
            # Parfois les sites renvoient 403 (Interdit) ou 429 (Trop de requêtes)
            table.add_row(name, f"[yellow]PROTECTED ({response.status_code})[/yellow]", "-")
            
    except Exception:
        table.add_row(name, "[red]ERROR[/red]", "-")

def run_user_finder():
    os.system('cls' if os.name == 'nt' else 'clear')
    
    console.print(Panel.fit(
        "[bold #1DA1F2]USER FINDER PRO - TARGETED SCAN[/bold #1DA1F2]\n"
        "[white]Stealth verification on major platforms[/white]",
        border_style="#1DA1F2"
    ))

    target = console.input("\n[bold #1DA1F2]┌───[[/bold #1DA1F2][bold white]root@osichef[/bold white][bold #1DA1F2]]\n└──╼ Target Username : [/bold #1DA1F2]").strip()

    if not target:
        return

    console.print(f"\n[bold yellow][*] Scanning Major Targets for '{target}'...[/bold yellow]\n")

    table = Table(header_style="bold #1DA1F2")
    table.add_column("Platform", style="cyan")
    table.add_column("Status", justify="center")
    table.add_column("Profile URL", style="white")

    # --- LISTE DES CIBLES (AJOUT DE STEAM & TWITCH) ---
    targets = [
        ("Instagram", "https://www.instagram.com/{}/"),
        ("TikTok", "https://www.tiktok.com/@{}"),
        ("Twitter/X", "https://twitter.com/{}"),
        ("Steam", "https://steamcommunity.com/id/{}/"),  
        ("Twitch", "https://www.twitch.tv/{}"),          
        ("GitHub", "https://github.com/{}"),
        ("Reddit", "https://www.reddit.com/user/{}/"),
        ("Snapchat", "https://www.snapchat.com/add/{}"),
        ("Pinterest", "https://www.pinterest.com/{}/"),
        ("Spotify", "https://open.spotify.com/user/{}")
    ]

    with console.status("[bold green]Checking databases...[/bold green]", spinner="dots"):
        for name, url_pattern in targets:
            check_site(name, url_pattern, target, table)

    console.print(table)
    
    console.print(f"\n[bold green][+] Scan finished.[/bold green]")
    input("\nPress Enter to return...")

if __name__ == "__main__":
    run_user_finder()