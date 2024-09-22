from autogen import ConversableAgent, config_list_from_json
from src.utils import get_azure_openai_config

# Configuração do modelo de linguagem para Azure
azure_config = get_azure_openai_config()

config_list = [{
    "model": azure_config["deployment_name"],
    "api_key": azure_config["api_key"],
    # "api_base": azure_config["api_base"],
    "api_type": "azure",
    "api_version": azure_config["api_version"]
}]

llm_config = {"config_list": config_list}

# Criando um agente
agente = ConversableAgent(
    name="meu_agente",
    llm_config=llm_config,
    human_input_mode="NEVER"
)

# Testando o agente
try:
    resposta = agente.generate_reply(
        messages=[{"content": "Olá, Me conte uma piada, não vale do livro de matematica", 
                    "role": "user"}]
    )
    print(resposta)
except Exception as e:
    print(f"Ocorreu um erro: {str(e)}")