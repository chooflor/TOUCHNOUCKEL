import os, sys, subprocess
from factory_core import add_data

def run():
    email = input("Email : ")
    # On lance Holehe
    process = subprocess.run(["holehe", email, "--only-used"], capture_output=True, text=True, shell=True)
    
    for line in process.stdout.split('\n'):
        if "[+]" in line:
            site = line.split('[+]')[1].strip().lower()
            add_data(site, "holehe")
    print("Données envoyées à l'usine.")

if __name__ == "__main__":
    run()