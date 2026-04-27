# tools/dns_enum.py
import dns.resolver
from rich.console import Console
from rich.panel import Panel
import os

console = Console()

def run_dns_enum():
    os.system('cls' if os.name == 'nt' else 'clear')
    console.print(Panel("[bold #1DA1F2]─── DNS ENUMERATION ───[/bold #1DA1F2]", border_style="#1DA1F2"))
    domain = console.input("\n[bold #1DA1F2]┌───[[/bold #1DA1F2][bold white]root@osichef[/bold white][bold #1DA1F2]]\n└──╼ Domain : [/bold #1DA1F2]").strip()
    if not domain: return

    console.print(f"\n[bold yellow][*] Enumerating DNS for: {domain}\n")
    records = ["A", "AAAA", "MX", "TXT", "NS", "SOA", "SRV", "CNAME"]
    for record in records:
        try:
            answers = dns.resolver.resolve(domain, record)
            console.print(f"[bold green]{record} Record(s)[/bold green]")
            for rdata in answers:
                console.print(f"  - {rdata}")
        except dns.resolver.NoAnswer:
            console.print(f"[bold red]{record} Record: NOT FOUND[/bold red]")
        except Exception as e:
            console.print(f"[bold red]Error fetching {record}: {e}[/bold red]")

    input("\nPress Enter to return...")

if __name__ == "__main__":
    run_dns_enum()
