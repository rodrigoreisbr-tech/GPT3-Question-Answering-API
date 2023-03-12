# GPT3-Question-Answering-API

<p>Olá! Neste código, estamos usando a biblioteca <strong>Streamlit</strong> para criar uma interface de usuário para interagir com o modelo <strong>ChatGPT</strong>, treinado pela <strong>OpenAI</strong>.</p>
<p>Primeiro, importamos as bibliotecas necessárias, como <strong>Streamlit</strong>, <strong>Decouple</strong>, <strong>OpenAI</strong>, <strong>PIL</strong>, e <strong>OS</strong>. Em seguida, definimos algumas variáveis, como a resposta do modelo, tokens de prompt e de completions, e o custo total da resposta.</p>
<p>Depois disso, criamos a função <strong>"make_request"</strong> para enviar uma pergunta ao modelo e obter a resposta.</p>
<p>Em seguida, usamos o <strong>Streamlit</strong> para criar uma interface com três perguntas (nome da empresa, função pretendida, e descrição da vaga), e armazenamos as respostas do usuário em uma lista.</p>
<p>Com base nas respostas do usuário, criamos um prompt para o modelo <strong>ChatGPT</strong>, solicitando informações sobre as habilidades necessárias para a função, dicas para se preparar para entrevistas, e a missão e visão da empresa.</p>
<p>Quando o usuário clica no botão <strong>"Enviar para análise"</strong>, a função <strong>"make_request"</strong> é chamada com o prompt, e a resposta do modelo é exibida na tela. Além disso, as estatísticas de uso do modelo são exibidas na barra lateral, como o número de tokens de prompt e completions usados, e o custo total da requisição.</p>
<p>Esse código é uma maneira fácil e eficiente de usar o modelo <strong>ChatGPT</strong> da <strong>OpenAI</strong> para responder a perguntas específicas. Você pode personalizá-lo para suas próprias necessidades, alterando o prompt e as perguntas da interface do usuário.</p>

We're using Streamlit to create a user interface for interacting with the ChatGPT model trained by OpenAI. After importing necessary libraries, we define variables for the model response, prompt tokens, and completion tokens.

We create a function "make_request" to send a question to the model and obtain the response.

Then, we use Streamlit to create an interface with three questions, storing the user's responses in a list. Based on the user's responses, we create a prompt for the ChatGPT model, requesting information about necessary skills for the job, interview tips, and the company's mission and vision.

When the user clicks the "Send for Analysis" button, the "make_request" function is called with the prompt, and the model's response is displayed on the screen. The sidebar displays usage statistics, such as the number of tokens used and the cost of the request.

This code is an easy and efficient way to use the OpenAI ChatGPT model to answer specific questions. You can customize it for your own needs by changing the prompt and user interface questions.
