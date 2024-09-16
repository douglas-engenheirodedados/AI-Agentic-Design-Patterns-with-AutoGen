from autogen import ConversableAgent

# Configuração do modelo de linguagem
llm_config = {"model": "gpt-3.5-turbo"}

# Criando um agente
agente = ConversableAgent(
    name="meu_agente",
    llm_config=llm_config,
    human_input_mode="NEVER"
)

# Testando o agente
resposta = agente.generate_reply(
    messages=[{"content": "Olá, como você está?", "role": "user"}]
)
print(resposta)