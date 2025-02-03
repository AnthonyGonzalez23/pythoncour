# games/utils.py
from rich.console import Console

console = Console()

def afficher_gagnant(result):
    console.print(result, style="bold green" if "gagnez" in result else "bold red")

def afficher_score(user_score, pc_score):
    console.print(f"Score: Vous {user_score} - Ordinateur {pc_score}", style="bold blue")