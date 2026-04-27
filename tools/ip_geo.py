# tools/ip_geo.py
import requests
import os
from rich.console import Console
from rich.panel import Panel

console = Console()

def get_ip_location(ip):
    try:
        url = f"http://ip-api.com/json/{ip}"
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": f"HTTP {response.status_code}"}
    except Exception as e:
        return {"error": str(e)}

def run_ip_geo():
    os.system('cls' if os.name == 'nt' else 'clear')
    console.print(Panel("[bold #1DA1F2]─── IP GEOLOCATION ───[/bold #1DA1F2]", border_style="#1DA1F2"))
    
    ip = console.input("\n[bold #1DA1F2]┌───[[/bold #1DA1F2][bold white]root@osichef[/bold white][bold #1DA1F2]]\n└──╼ IP Address : [/bold #1DA1F2]").strip()
    if not ip:
        console.print("[bold red][!] No IP entered.[/bold red]")
        input("\nPress Enter to return...")
        return

    console.print(f"\n[bold yellow][*] Fetching location for IP: {ip}...[/bold yellow]")
    data = get_ip_location(ip)

    if "error" in data:
        console.print(f"[bold red][!] Error: {data['error']}[/bold red]")
    else:
        console.print(f"\n[bold green]Location Info for {ip}:[/bold green]")
        for key, value in data.items():
            console.print(f"{key.capitalize()}: {value}")

    input("\nPress Enter to return...")

if __name__ == "__main__":
    run_ip_geo()
