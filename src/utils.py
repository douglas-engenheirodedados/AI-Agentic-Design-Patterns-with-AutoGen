import sys
import os
from pathlib import Path

# Adiciona o diretório raiz do projeto ao Python path
project_root = Path(__file__).parents[1]
sys.path.append(str(project_root))

# Add your utilities or helper functions to this file.

import os
from dotenv import load_dotenv, find_dotenv

# these expect to find a .env file at the directory above the lesson.                                                                                                                     # the format for that file is (without the comment)                                                                                                                                       #API_KEYNAME=AStringThatIsTheLongAPIKeyFromSomeService                                                                                                                                     
def load_env():
    # Obtém o diretório do arquivo atual (utils.py)
    current_dir = os.path.dirname(os.path.abspath(__file__))
    # Vai para o diretório pai (raiz do projeto)
    project_dir = os.path.dirname(current_dir)
    # Caminho para o arquivo .env
    dotenv_path = os.path.join(project_dir, '.env')
    # Carrega as variáveis de ambiente
    load_dotenv(dotenv_path)

def get_openai_api_key():
    load_env()
    openai_api_key = os.getenv("OPENAI_API_KEY")
    return openai_api_key

def get_azure_openai_config():
    load_dotenv()
    return {
        "api_key": os.getenv("AZURE_OPENAI_API_KEY"),
        "api_base": os.getenv("AZURE_OPENAI_ENDPOINT"),
        "api_version": os.getenv("AZURE_OPENAI_API_VERSION"),
        "deployment_name": os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME")
    }
