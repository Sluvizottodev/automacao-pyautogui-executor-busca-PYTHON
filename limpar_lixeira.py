import winshell

try:
    winshell.recycle_bin().empty(confirm=True, show_progress=False, sound=False)
    print("Lixeira esvaziada com sucesso!")
except Exception as e:
    print("A lixeira já estava vazia ou houve erro:", e)
#confirm=True: Pedir confirmação ao usuário.
#show_progress=False: sem exibir barra de progresso.
#sound=False: sem emitir som durante a operação.