import duckdb
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]

ARQUIVO_RAW_OP = BASE_DIR / "data" / "raw" / "train_operational_readouts.csv"
ARQUIVO_RAW_TTE = BASE_DIR / "data" / "raw" / "train_tte.csv"
ARQUIVO_PROCESSED = BASE_DIR / "data" / "processed" / "scania_amostra_10k.csv"

def extrair_amostra() -> None:
    
    ARQUIVO_PROCESSED.parent.mkdir(parents=True, exist_ok=True)
    
    '''
    A query faz um JOIN das leituras com os rótulos de reparo, cria o ID único 
    e converte o indicador de falha no atributo TEXTUAL obrigatório.
    '''
    
    query_extracao = f"""
        COPY (
            SELECT 
                ROW_NUMBER() OVER () AS id_registro,
                op.vehicle_id,
                
                -- Atributo TEXTUAL (Regra de negócio do MECAI)
                CASE 
                    WHEN tte.in_study_repair = 1 THEN 'Falha e Reparo'
                    ELSE 'Operacao Normal'
                END AS status_equipamento,
                
                -- Atributos NUMÉRICOS para uso nos algoritmos de Ordenação
                op.time_step,
                op."171_0" AS sensor_171,
                op."666_0" AS sensor_666,
                op."100_0" AS sensor_100
                
            FROM read_csv_auto('{ARQUIVO_RAW_OP}') AS op
            LEFT JOIN read_csv_auto('{ARQUIVO_RAW_TTE}') AS tte
                ON op.vehicle_id = tte.vehicle_id
            
            -- Filtro para garantir a consistência das chaves numéricas
            WHERE op.time_step IS NOT NULL 
              AND tte.in_study_repair IS NOT NULL
            LIMIT 10000
        ) TO '{ARQUIVO_PROCESSED}' (HEADER, DELIMITER ',');
    """
    
    print("Conectando aos arquivos raw (out-of-core)...")
    print("Executando JOIN e extraindo amostra...")
    
    duckdb.sql(query_extracao)
    
    print(f"Sucesso! Dataset processado criado em: {ARQUIVO_PROCESSED}")

if __name__ == "__main__":
    extrair_amostra()