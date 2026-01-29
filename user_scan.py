import os
import sys
import time
import re
import webbrowser
import requests

try:
    from rich.console import Console
    from rich.table import Table
    from rich.panel import Panel
    from rich.text import Text
    from rich.align import Align
    from rich.progress import track
except ImportError:
    print("\n[!] Erreur : 'rich' est requis. Installe-le avec : pip install rich")
    sys.exit()

console = Console()

# --- CONFIGURATION VISUELLE (Identique à injector.py) ---
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

def get_steam_info(username):
    url = f"https://steamcommunity.com/id/{username}"
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            steam_id_match = re.search(r'"steamid":"(\d+)"', response.text)
            bio_match = re.search(r'<div class="profile_summary">(.*?)</div>', response.text, re.DOTALL)
            id64 = steam_id_match.group(1) if steam_id_match else "Introuvable"
            bio = "Pas de biographie."
            if bio_match:
                bio = re.sub('<[^<]+?>', '', bio_match.group(1)).strip()
                bio = (bio[:150] + '...') if len(bio) > 150 else bio
            return {"found": True, "url": url, "id64": id64, "bio": bio}
    except:
        pass
    return {"found": False}

def scan_username():
    os.system('cls' if os.name == 'nt' else 'clear')
    
    # Affichage du titre OSICHEF
    console.print(Align.center(generate_hacker_colors(EXOTIC_BANNER)))
    console.print(Align.center(Text("⚡ MODULE : USERNAME SCANNER ⚡", style="bold cyan")))
    console.print("\n")

    # Le prompt style Terminal Linux
    username = console.input("[bold #00FF00]┌───[[/bold #00FF00][bold white]root@osichef[/bold white][bold #00FF00]]\n└──╼ Entrez le pseudo cible : [/bold #00FF00]")
    
    if not username:
        return

    # 1. SCAN DES RÉSEAUX SOCIAUX
    social_sites = {
        "Instagram": f"https://www.instagram.com/{username}/",
        "TikTok": f"https://www.tiktok.com/@{username}",
        "GitHub": f"https://github.com/{username}",
        "Twitter/X": f"https://twitter.com/{username}",
        "Twitch": f"https://www.twitch.tv/{username}"
    }

    table = Table(title=f"\n[bold yellow]RAPPORTS D'EXTRACTION : {username}[/bold yellow]", border_style="cyan")
    table.add_column("Plateforme", style="cyan")
    table.add_column("Status", justify="center")
    table.add_column("Lien", style="blue")

    console.print(f"\n[bold green][*] Analyse des flux sociaux...[/bold green]")
    
    for site, url in track(social_sites.items(), description="Scanning..."):
        try:
            headers = {'User-Agent': 'Mozilla/5.0'}
            r = requests.get(url, timeout=5, headers=headers)
            if r.status_code == 200:
                table.add_row(site, "[green]TROUVÉ[/green]", url)
            else:
                table.add_row(site, "[red]ABSENT[/red]", "---")
        except:
            table.add_row(site, "[yellow]ERREUR[/yellow]", "Connexion échouée")

    console.print(table)

    # 2. ANALYSE STEAM
    steam = get_steam_info(username)
    if steam["found"]:
        console.print("\n")
        console.print(Panel(
            f"[white]URL  :[/white] {steam['url']}\n"
            f"[white]ID64 :[/white] [cyan]{steam['id64']}[/cyan]\n"
            f"[white]BIO  :[/white] {steam['bio']}",
            title="[bold blue]STEAM PROFILE DETECTED[/bold blue]",
            border_style="blue",
            expand=False
        ))

    # 3. GOOGLE DORKS
    query = f'"{username}" -site:instagram.com -site:twitter.com'
    search_url = f"https://www.google.com/search?q={query}"
    console.print(f"\n[bold magenta][*] Recherche web étendue (Dorks) :[/bold magenta]\n[underline]{search_url}[/underline]")
    
    ans = console.input("\n[bold yellow]Ouvrir les résultats Google ? (y/n) : [/bold yellow]")
    if ans.lower() == 'y':
        webbrowser.open(search_url)

if __name__ == "__main__":
    scan_username()
    console.print("\n[bold cyan]─── MISSION TERMINÉE ───[/bold cyan]")
    input("Appuyez sur Entrée pour retourner au noyau...")