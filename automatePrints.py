import pyautogui
import time
import os


# Seta pasta para salvar os print's pasta destino
local_prints = "C:\\Users\\alex.lopes\\projectsPython\\prints\\"

# Verifica a quantidade de print's dentro da pasta destino
local_prints_qnt = os.listdir("C:\\Users\\alex.lopes\\projectsPython\\prints\\")

# Verifica a quantidades de arquivos dentro da pasta e seta o nome do arquivo
qnt_local_arq = len(local_prints_qnt)
if qnt_local_arq == 0 :
    namePrint = 'screenshot%s' % qnt_local_arq
else: 
    qnt_local_arq = qnt_local_arq + 1 
    namePrint = 'screenshot%s' % qnt_local_arq

# Realiza o print da tela 
img1 = pyautogui.screenshot() 
img1.save(r"C:\Users\alex.lopes\projectsPython\prints\%s.png" % namePrint)

# Verifica se o print foi salvo dentro da pasta
salve_done = False
if os.path.exists(local_prints + "%s.png" % namePrint):
    salve_done = True 
    print('Arquivo salvo com sucesso ! ')


