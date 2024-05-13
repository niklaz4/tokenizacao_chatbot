import nltk
from nltk.chat.util import Chat, reflections
from textblob import TextBlob

nltk.download('stopwords')
nltk.download('punkt')

# Definição dos padrões de perguntas e respostas para o chatbot
pares = [
    ['Oi', ['Olá, como posso ajudar?']],
    ['Como você está', ['Estou bem, obrigado. E você?', 'Tudo bem!']],
    ['Quem é você?', ['Sou seu professor virtual.', ' Me chame de Prof.']],
    ['Qual é seu objetivo?', ['Meu objetivo é ajudar a responder suas perguntas.', 'Estou aqui para ensinar.']]
]

# Inicializar o chatbot com os pares de perguntas e respostas
chatbot = Chat(pares, reflections)

# Função para análise de sentimento usando TextBlob
def analisar_sentimento(texto):
    blob = TextBlob(texto)
    polaridade = blob.sentiment.polarity
    if polaridade > 0:
        return "Isso parece positivo!"
    elif polaridade < 0:
        return "Isso parece negativo."
    else:
        return "Não consigo determinar o sentimento com certeza."

# Função para iniciar o chat
def iniciar_chat():
    print("Olá! Digite 'sair' para encerrar o chat")
    while True:
        mensagem = input("Você: ")
        if mensagem.lower() == 'sair':
            print("Chat encerrado.")
            break

        resposta = chatbot.respond(mensagem)
        print("Prof: ", resposta)

        # Pedir ao usuário para digitar algo para análise de sentimento
        mensagem_usuario = input("Digite algo para análise de sentimento:")

        # Analisar o sentimento da mensagem e imprimir o resultado
        resultado_sentimento = analisar_sentimento(mensagem_usuario)
        print("Análise de sentimento: ", resultado_sentimento)

# Função principal
def main():
    # Iniciar o chat
    iniciar_chat()

# Executar a função principal
if __name__ == "__main__":
    main()
