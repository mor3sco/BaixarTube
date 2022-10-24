
import webbrowser as wb
import PySimpleGUI as sg
import time
from pytube import YouTube

def executar_download(link, path):
        video = YouTube(link)
        video.streams.get_highest_resolution().download(output_path=path)

sg.theme('Reddit')

layout = [
        [sg.Text("Link do Video: "), sg.InputText(size=(40,1))],
        [sg.Text("Onde colocar:  "), sg.InputText(size=(40,1)),sg.FolderBrowse("Procurar")],
        [sg.Button('Baixar')],
        ]
#janela
janela = sg.Window('Baixador de videos YouTube', layout)
#ler os eventos
while True:
    event, values= janela.read()
    if event == sg.WINDOW_CLOSED:
        break
    elif event == 'Baixar':
        executar_download(values[0],values[1])
        sg.popup_ok("Download Realizado!")
janela.close()
       
