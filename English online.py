import time, traceback;
from googletrans import Translator;

def iniciar():
    urls = ["translate.google.com", "translate.google.com.ar", "translate.google.com.br", "translate.google.com"];
    user = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36";
    return Translator(service_urls=urls, user_agent=user, raise_exception=False, timeout=None);

def traduzir(frases):
    for i in range(21):
        try:
            buffer = iniciar().translate(frases, dest='pt')
            return buffer;
        except:
            time.sleep(0.02);
                        
frases = ["What's my user agent?", "Sorry, we get too much"]
retornos = traduzir(frases);

print(traduzir(frases))
for retorno in retornos:
    print (retorno.text);