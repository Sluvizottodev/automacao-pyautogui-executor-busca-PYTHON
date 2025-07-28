# 🖱️ Automação com PyAutoGUI

Este repositório contém scripts simples de automação utilizando a biblioteca [PyAutoGUI](https://pyautogui.readthedocs.io/en/latest/), desenvolvidos para executar tarefas repetitivas no Windows, como abrir o navegador, fazer buscas no YouTube e utilizar a calculadora.

---

## 📁 Estrutura de Pastas

```bash
.
├── buscar-video-youtube.py         # Abre o Chrome, entra no YouTube e busca um vídeo
├── conta-na-calculadora.py         # Abre a Calculadora do Windows e faz uma conta
└── pyautogui-position.py           # Mostra a posição atual do cursor do mouse na tela
```

---

## 🔧 Requisitos

* **Python 3.x**
* **Bibliotecas**:

  * `pyautogui`
  * `pyperclip`
  * `time` (padrão do Python)

### Instalação

Para instalar as bibliotecas necessárias, use:

```bash
pip install pyautogui pyperclip
```

> **Dica**: Execute os scripts com a tela desobstruída e o sistema operacional em uso normal para evitar comportamentos inesperados.

---

## 🚀 Scripts

### 1. `buscar-video-youtube.py`

Este script:

* Abre o navegador Google Chrome
* Acessa o site do YouTube
* Busca por um termo específico (ex: "lofi girl")
* Clica no primeiro vídeo da lista de resultados

> Útil para automatizar a abertura de vídeos ou músicas de forma rápida.

---

### 2. `conta-na-calculadora.py`

Este script:

* Abre a Calculadora do Windows
* Realiza uma conta simples (por exemplo: `2025 - 2005`)

> Ideal para automatizar operações básicas, útil em testes ou demonstrações.

---

### 3. `pyautogui-position.py`

Este script:

* Aguarda 5 segundos
* Imprime a posição atual do cursor do mouse na tela

> Usado para descobrir as coordenadas que você deve usar ao aplicar `pyautogui.click(x, y)`.

---

## 📌 Observações Importantes

* As coordenadas usadas nos cliques (`pa.click(x, y)`) variam conforme a resolução e layout do seu monitor. Ajuste conforme necessário.
* Use o script `pyautogui-position.py` para identificar essas posições de forma prática.
* Esses exemplos são educativos e podem ser adaptados e expandidos conforme suas necessidades.

---

## 📚 Referência

* [Documentação oficial do PyAutoGUI](https://pyautogui.readthedocs.io/en/latest/)
* [Pyperclip - Manipulação de clipboard](https://pyperclip.readthedocs.io/en/latest/)

---

Feito com ❤️ para transmitir experiência e conhecimento com Python.
