# Programa feito com base no tutorial do site: https://youtu.be/eWRfhZUzrAc?si=0drcz09D3SoLy2_R
# Rock, paper, scissors game

import random

def get_choices():
    player_choice = input("Enter a choice (rock, paper, scissors): ")
    computer_choice = random.choice(["rock", "paper", "scissors"]) # random.choices() escolhe uma opção aleatória dentre todas da lista, indicada pelos [] 

    # um dicionário contém pares de chave-valor (as chaves são únicas, os valores podem repetir)
    choices = {"player": player_choice, "computer": computer_choice}
    return choices

def  check_win(player, computer):
    print(f"You chose {player}, computer chose {computer}")
    if player == computer:
        return "It's a tie!"
    
    elif player == "rock":
        if computer == "scissors":
            return "Rock smashes scissors! You win!"
        else:
            return "Paper covers rock! You lose."
        
    elif player == "paper":
        if computer == "rock":
            return "Paper covers rock! You win!"
        else:
            return "Scissors cuts paper! You lose."
        
    elif player == "scissors":
        if computer == "paper":
            return "Scissors cuts paper! You win!"
        else:
            return "Rock smashes scissors! You lose."    

choices = get_choices() # retorna o dicionário inteiro com as escolhas do jogador e do computador
result = check_win(choices["player"], choices["computer"]) # retorna os resultados dos valores contidos em cada chave do dicionário -> a busca é feita pelo nome da chave
print(result)
