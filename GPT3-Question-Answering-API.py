#importar as bibliotecas
import streamlit as st
from decouple import config 
import openai
import os
from PIL import Image

response = False
prompt_tokens = 0
completion_tokens = 0
total_tokens_used = 0
cost_of_response = 0 


#definir os request para o ChatGPT
def make_request(question_input: str):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": f"{question_input}"},
        ]
    )
    return response

st.header ("Semana Python")
st.markdown("---")

if "OPEN_API_KEY" not in os.environ:
    st.error("A chave da API da OpenAI não foi definida corretamente.")
    st.stop()

#openai.api_key = "minha chave api"
openai.api_key = os.environ["OPEN_API_KEY"]

perguntas = [
    "Qual o nome da empres?",
    "Para qual funcao voce esta aplicando?",
    "Coloque a descricao da vaga que voce encontrou:"
]

user_responses= []

resposta_01 =  st.text_input(perguntas[0])
user_responses.append(resposta_01)

resposta_02 =  st.text_input(perguntas[1])
user_responses.append(resposta_02)

resposta_03 =  st.text_area(perguntas[2], height=200)
user_responses.append(resposta_03)

#prompt = f"Me diga quais as mairos cidades do mundo."
prompt = f"A empresa {user_responses[0]} esta contratando para a posicao de{user_responses[1]}. Como base na descricao da vaga fornecida abaixo, quais sao as principais habilidades exigidas para funcao? Alem disso, o que voce recomendaria para se preparar para esta posicao e para possiveis entrevistas? Por fim fornecer a missao e vissao da empresa {user_responses[0]}? Essa e a descricao da vaga: {user_responses[2]} responda em portugues e ingles e fala as principais perguntas de entrevistas"

rerun_button = st.button("Enviar para analise")
st.markdown("""---""")

if rerun_button:
    response = make_request(prompt)
else:
    pass

if response:
    st.write("Resposta:")
    st.write(response["choices"][0]["message"]["content"])

    prompt_tokens = response["usage"]["prompt_tokens"]
    completion_tokens = response["usage"]["completion_tokens"]
    total_tokens_used = response["usage"]["total_tokens"]
    cost_of_response = total_tokens_used * 0.000002

else:
    pass

with st.sidebar:
    st.image(Image.open('logo.png'))
    st.title("Estatiscas de uso:")
    st.markdown("""---""")
    st.write("Token de propmpt: ", prompt_tokens)
    st.write("Token de Completions usados: ", completion_tokens)
    st.write("Total de Tokens usados: ", total_tokens_used)
    st.write("Custo total da Requisicao : ${:.8f}".format(cost_of_response))