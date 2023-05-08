# ChatGPT on Terminal and Python NoteBooks

Pequeños ejemplos de uso de la api de OpenAI usando python para:

- Usar chatgpt desde la terminal (chat.py)
- Chatbot de terminal usando la api de ChatGPT (ChatBot.py)
- Integración de ChatGPT en un NoteBook de python para añadir celdas de codigo automaticamente (noteGPT.ipynb)

### Requisitos

- VScode
- Python 3
- Instalar las extensiones de python de VScode
- Crear una carpeta para el proyecto con un entorno virtual de python y activarlos

```bash
mkdir terminalGPT

cd terminalGPT

py -m venv .\venv

.\venv\Scripts\activate
```

- Instalar las siguientes bibliotecas de python

```bash
pip install openai

pip install beautifulsoup4

pip install pandas

pip install matplotlib
```

- Tener un clave privada de OpenAI
    - Tener usuario de OpenAI
    - Crear la api key en [(https://platform.openai.com/](https://platform.openai.com/)
    - Es posible que les sea solicitada información de facturación, pueden proporcionar una tarjeta de crédito o debito, no se preocupen por que los costos de uso de la api de ChatGPT son bastante bajos. [https://openai.com/pricing](https://openai.com/pricing)

---

### Ejemplos de prompts para el notebook

- Español:
    - Científico de datos de Python
    - Haz scraping de [https://www.imdb.com/chart/top/?ref_=nv_mv_250](https://www.imdb.com/chart/top/?ref_=nv_mv_250) con python y BeautifulSoup, obtenga el titulo, año y rating, finalmente  añade la informaciñon  a un dataframe  de pandas
    - con el dataframe resultante haz una grafica usando matplotlib donde el eje x represente el año y el eje y representa el rating
    - ¿Puedo tener los valores de los ejes ordenados de menor a mayor tanto en el eje x como en el eje y usando solo matlpotlib?
    - ¿puedo hacer el mismo grafico con matplotlib pero mas ancho y con las etiques del eje x en vertical?

- Ingles
    - Python data scientist
    - Scrape this [https://www.imdb.com/chart/top/?ref_=nv_mv_250](https://www.imdb.com/chart/top/?ref_=nv_mv_250) with python and BeautifulSoup, get movie title, year and rating and put it on a pandas dataframe
    - With the resulting dataframe make a graph using matplotlib where the x axis represents the year and the y axis represents the rating
    - Can i have the values of the axes sorted from smallest to largest both the x axis and the y axis using just matlpotlib
    - Can I make the same plot with matplotlib but wider and with the x-axis labels vertical?