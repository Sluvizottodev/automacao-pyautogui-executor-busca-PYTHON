import winshell

try:
    winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=False)
    print("Lixeira esvaziada com sucesso!")
except Exception as e:
    print("A lixeira já estava vazia ou houve erro:", e)
