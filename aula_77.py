"""
Exercício

Sistema de perguntas e respostas
"""

import os
import time

# Lista de perguntas

perguntas = [
    {
        "Pergunta": "Qual é o maior oceano do mundo?",
        "Respostas": ["Oceano Atlântico", "Oceano Índico", "Oceano Ártico", "Oceano Pacífico"],
        "Certa": "Oceano Pacífico"
    },
    {
        "Pergunta": "Quem foi o primeiro homem a pisar na Lua?",
        "Respostas": ["Yuri Gagarin", "Alan Shepard", "Buzz Aldrin", "Neil Armstrong"],
        "Certa": "Neil Armstrong"
    },
    {
        "Pergunta": "Qual é o maior país em área territorial do mundo?",
        "Respostas": ["Estados Unidos", "Canadá", "China", "Rússia"],
        "Certa": "Rússia"
    },
    {
        "Pergunta": "Em que ano o Brasil se tornou independente de Portugal?",
        "Respostas": ["1822", "1808", "1889", "1500"],
        "Certa": "1822"
    },
    {
        "Pergunta": 'Qual é o elemento químico representado pelo símbolo "O"?',
        "Respostas": ["Ouro", "Oxigênio", "Osmium", "Ósmio"],
        "Certa": "Oxigênio"
    }
]

# Limpar o terminal

os.system('cls')

# Exibir as perguntas

for pergunta in perguntas:
    print(f"{pergunta["Pergunta"]}\n")
    time.sleep(0.5)

    for alternativas in pergunta["Respostas"]:
        print(alternativas)
        time.sleep(0.5)

    resposta = input("\nResposta: ")

    if resposta == pergunta["Certa"]:
        print("\nResposta Correta\n")
    else:
        print("\nResposta Errada\n")
    
    time.sleep(1)
    os.system('cls')
        
