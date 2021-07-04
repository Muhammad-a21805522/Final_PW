import matplotlib.pyplot as plt
import base64
from io import BytesIO


def get_graph():
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')
    buffer.close()
    return graph


def get_plot(x, y):
    plt.switch_backend('AGG')
    plt.figure(figsize=(10, 5))
    plt.title('Comentários')
    plt.plot(x, y)
    plt.tight_layout()
    graph = get_graph()
    return graph


def media(x):
    return sum(x) / len(x)


def corrigir(respostas):
    nota = 0
    if respostas[0] == 'combustao':
        nota += 10
    if respostas[1] == 'tesla3':
        nota += 10
    if respostas[2] == 'tesla3':
        nota += 10
    if respostas[3] == '075kw':
        nota += 10
    if respostas[4] == 'eletricos':
        nota += 10
    if respostas[5] == '1505':
        nota += 10
    if respostas[6] == 'eletricos':
        nota += 10
    if respostas[7] == '30min':
        nota += 10
    if respostas[8] == 'teslas':
        nota += 10
    if respostas[9] == 'eletricos':
        nota += 10
    return nota

def get_graphv2():
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')
    buffer.close()
    return graph

def get_plotv2(x, y):
    plt.switch_backend('AGG')
    plt.figure(figsize=(10, 4))
    plt.title('Quizz')
    plt.bar(x, y)
    plt.tight_layout()
    plt.ylim([0,100])
    graph = get_graphv2()
    return graph
