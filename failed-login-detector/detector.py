

def analisar_log(caminho_arquivo):
    suspeitos = {}
    contagem = {}
    
    with open(caminho_arquivo) as arquivo:
     for linha in arquivo:
        partes = linha.split()
        ip = partes [0]
        status = partes [2]
    
        if status == "FAILED" :
            contagem[ip] = contagem.get(ip , 0) + 1
            
    for ip , quantidade in contagem.items():
      if quantidade >= 3:
          suspeitos[ip] = quantidade 

    return suspeitos



suspeitos = analisar_log("login.log")
print (suspeitos)

