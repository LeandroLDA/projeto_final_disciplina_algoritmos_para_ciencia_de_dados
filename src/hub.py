import os
from pathlib import Path
from dotenv import load_dotenv
from huggingface_hub import HfApi

load_dotenv()
HF_TOKEN = os.getenv("HF_TOKEN")
HF_REPO_ID = "algoritmos-mecai-usp/scania_x_component"

# A raiz do seu projeto local (onde estão as pastas src/, data/, docs/)
BASE_DIR = Path(__file__).resolve().parents[1]

def push_raw_data() -> None:
    """
    Pega APENAS o conteúdo da pasta local 'data/raw' e sobe para 
    a pasta 'data/raw' no repositório do Hugging Face.
    """
    api = HfApi(token=HF_TOKEN)
    pasta_local_raw = BASE_DIR / "data" / "raw"
    
    print(f"Subindo arquivos de {pasta_local_raw} para data/raw no HF...")
    
    api.upload_folder(
        folder_path=str(pasta_local_raw),
        path_in_repo="data/raw", 
        repo_id=HF_REPO_ID,
        repo_type="dataset",
    )
    print("Upload concluído!")
    
def push_processed_data() -> None:
    """
    Pega APENAS o conteúdo da pasta local 'data/processed' e sobe para 
    a pasta 'data/processed' no repositório do Hugging Face.
    """
    api = HfApi(token=HF_TOKEN)
    pasta_local_processed = BASE_DIR / "data" / "processed"
    
    print(f"Subindo arquivos de {pasta_local_processed} para data/processed no HF...")
    
    api.upload_folder(
        folder_path=str(pasta_local_processed),
        path_in_repo="data/processed",
        repo_id=HF_REPO_ID,
        repo_type="dataset",
    )
    print("Upload dos dados processados concluído!")
    
def push_experiments_data() -> None:
    """
    Pega APENAS o conteúdo da pasta local 'data/experiments' e sobe para 
    a pasta 'data/experiments' no repositório do Hugging Face.
    """
    api = HfApi(token=HF_TOKEN)
    pasta_local_experiments = BASE_DIR / "data" / "experiments"
    
    print(f"Subindo arquivos de {pasta_local_experiments} para data/experiments no HF...")
    
    api.upload_folder(
        folder_path=str(pasta_local_experiments),
        path_in_repo="data/experiments", 
        repo_id=HF_REPO_ID,
        repo_type="dataset",
    )
    print("Upload dos experimentos concluído!")

def pull_proc_exp_data() -> None:
    """
    Baixa a estrutura, exceto ('data/raw') do HF para a máquina local.
    Dessa forma, apenas a amostra em que serão aplicados os experimentos ocuparão 
    o computador.
    """

    api = HfApi() 
    
    print("Baixando arquivos do repositório no hugging face")
    api.snapshot_download(
        repo_id=HF_REPO_ID,
        repo_type="dataset",
        local_dir=str(BASE_DIR),
        allow_patterns=["data/*"],
        ignore_patterns=["data/raw/*"] # Comente este comando caso queira todo o dataset ( ele tem mais de 1,5Gb)
    )
    print("Download concluído! Os dados estão prontos na pasta data/")

if __name__ == "__main__":
    '''
    Escolha se quer subir ou baixar e rode o script no terminal da pasta raiz do projeto 'python -m src/hub.py'
    dentro deste if, descomente as ações desejadas e comente o resto.
    '''
    # push_raw_data() # sobe os dados brutos
    # push_processed_data() # sobe os dados processados
    # push_experiments_data() # sobe os dados dos experimentos
         
    pull_proc_exp_data() # baixa os dados exceto os dados brutos.