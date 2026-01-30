import sqlite3
import os
from rich.console import Console
from rich.table import Table

console = Console()
DB_PATH = os.path.join("logs", "factory.db")

def init_factory():
    if not os.path.exists("logs"): os.makedirs("logs")
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    # Table unique pour croiser pseudo et email
    c.execute('''CREATE TABLE IF NOT EXISTS intel 
                 (platform TEXT PRIMARY KEY, sherlock_found INTEGER DEFAULT 0, holehe_found INTEGER DEFAULT 0)''')
    conn.commit()
    conn.close()

def add_data(platform, source):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    # On insère ou on met à jour le compte trouvé
    c.execute(f"INSERT OR IGNORE INTO intel (platform) VALUES (?)", (platform,))
    if source == "sherlock":
        c.execute("UPDATE intel SET sherlock_found = 1 WHERE platform = ?", (platform,))
    elif source == "holehe":
        c.execute("UPDATE intel SET holehe_found = 1 WHERE platform = ?", (platform,))
    conn.commit()
    conn.close()

def get_report():
    init_factory()
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT * FROM intel WHERE sherlock_found = 1 OR holehe_found = 1")
    rows = c.fetchall()
    
    table = Table(title="🏭 RAPPORT GÉNÉRAL DE L'USINE", style="bold cyan")
    table.add_column("PLATEFORME", style="white")
    table.add_column("PSEUDO (Sherlock)", justify="center")
    table.add_column("EMAIL (Holehe)", justify="center")
    table.add_column("FIABILITÉ", justify="center")

    for row in rows:
        name, s, h = row
        score = "⭐" if (s + h) == 1 else "🔥 HAUTE (Match !)"
        table.add_row(
            name.upper(), 
            "[green]OUI[/green]" if s else "[red]NON[/red]",
            "[green]OUI[/green]" if h else "[red]NON[/red]",
            f"[bold yellow]{score}[/bold yellow]"
        )
    console.print(table)
    conn.close()