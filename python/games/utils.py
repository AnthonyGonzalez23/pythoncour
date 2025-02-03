from rich.console import Console

console = Console()

def afficher_gagnant(result):
    console.print(result, style="bold blue")

def afficher_score(user_score, pc_score):
    console.print(f"Score - Vous: {user_score}, Ordinateur: {pc_score}", style="bold green")