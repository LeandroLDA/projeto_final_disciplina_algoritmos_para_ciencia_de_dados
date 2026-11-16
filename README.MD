# ⚙️ Sistema de Organização e Análise de Dados: Manutenção Preditiva (Scania)

<div align="center">

[![Python](https://img.shields.io/badge/python-3.10+-blue.svg?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Testes Automatizados](https://img.shields.io/github/actions/workflow/status/LeandroLDA/projeto_final_disciplina_algoritmos_para_ciencia_de_dados/pytest.yml?style=for-the-badge&label=Testes%20Automatizados)](https://github.com/LeandroLDA/projeto_final_disciplina_algoritmos_para_ciencia_de_dados/actions)
![Commits](https://img.shields.io/github/commit-activity/t/LeandroLDA/projeto_final_disciplina_algoritmos_para_ciencia_de_dados?style=for-the-badge&label=commits)
![Último commit](https://img.shields.io/github/last-commit/LeandroLDA/projeto_final_disciplina_algoritmos_para_ciencia_de_dados?style=for-the-badge&label=%C3%BAltimo%20commit)
![Issues Abertas](https://img.shields.io/github/issues/LeandroLDA/projeto_final_disciplina_algoritmos_para_ciencia_de_dados?style=for-the-badge&color=blue&label=issues%20abertas)
![Issues Fechadas](https://img.shields.io/github/issues-closed/LeandroLDA/projeto_final_disciplina_algoritmos_para_ciencia_de_dados?style=for-the-badge&color=purple&label=issues%20fechadas)

</div>

Este repositório contém o sistema desenvolvido para o projeto final da disciplina de **Algoritmos para Ciência de Dados** do Mestrado Profissional (MECAI) do ICMC-USP[cite: 1]. 

O sistema integra algoritmos próprios implementados em Python, avaliando como as características dos dados e a frequência de consultas/atualizações afetam o desempenho computacional e as escolhas de projeto[cite: 1]. O contexto de aplicação é o **Monitoramento de Equipamentos Industriais**[cite: 7].

## 📌 Contexto e Base de Dados

O domínio escolhido aborda a manutenção preditiva em caminhões pesados, utilizando a base de dados real **SCANIA Component X Dataset**[cite: 10, 13]. Este *dataset* contém séries temporais multivariadas com leituras operacionais e registros de reparo[cite: 10, 14].

Para adequação às restrições estritas do projeto[cite: 2]:
- Foi gerado um **identificador inteiro não negativo e único** para cada registro (`id_registro`) através de uma *window function* na extração via DuckDB, sendo mantido imutável durante o ciclo de vida da instância[cite: 2, 5].
- O atributo textual obrigatório e relevante ao domínio não advém de categorias genéricas, mas sim do cruzamento das leituras com os rótulos de reparo (`train_tte.csv`), traduzindo o indicador de falha para a coluna de texto `status_equipamento` (ex: `'Falha e Reparo'` ou `'Operacao Normal'`)[cite: 2, 11].
- Foram preservados apenas os atributos numéricos de caráter cumulativo (ex: `time_step`, `171_0`, `100_0`), descartando histogramas multidimensionais para otimizar o processamento dos algoritmos de busca e ordenação[cite: 4, 10].

## 🏗️ Arquitetura e Estrutura de Pastas

O sistema foi desenhado sob o paradigma de Orientação a Objetos, utilizando contratos explícitos e injeção de dependências (Padrão *Strategy*) para intercambiar algoritmos sem alterar a lógica de serviço[cite: 3].

```text
📦 projeto_final_disciplina_algoritmos_para_ciencia_de_dados
 ┣ 📂 .github
 ┃ ┣ 📂 ISSUE_TEMPLATE      # Padrões para Bug, Feature e Task
 ┃ ┗ 📂 workflows           # CI/CD com GitHub Actions para Pytest
 ┣ 📂 data
 ┃ ┣ 📂 experiments         # Saídas geradas (.csv) com resultados de desempenho[cite: 2]
 ┃ ┣ 📂 processed           # Amostra unificada (scania_amostra_10k.csv) gerada pelo DuckDB
 ┃ ┗ 📂 raw                 # Arquivos brutos (ignorados no git). Sincronizados via Hugging Face Hub
 ┣ 📂 docs                  # Relatórios, diagramas de classes e artefatos de defesa
 ┣ 📂 notebooks             # Exploração de dados (EDA) e plotagem de gráficos finais[cite: 4]
 ┣ 📂 src                   # Núcleo do sistema OO
 ┃ ┣ 📜 hub.py              # Script para pull/push de dados processados via Hugging Face
 ┃ ┣ 📜 ingestion.py        # Pipeline out-of-core com DuckDB (Join, transformação textual e amostragem)
 ┃ ┣ 📜 domain.py           # Entidades (Registros) com encapsulamento rigoroso[cite: 3]
 ┃ ┣ 📜 experiments.py      # Executor isolado para medição de tempos e comparações[cite: 3, 6]
 ┃ ┣ 📜 hashtable.py        # Tabela Hash própria com política de resolução de colisões
 ┃ ┣ 📜 repository.py       # Repositório central, gerenciamento de coleções e índices[cite: 3]
 ┃ ┣ 📜 searching.py        # Algoritmos de busca (Binária, Sequencial, Indexada/Exponencial)
 ┃ ┗ 📜 sorting.py          # Algoritmos de ordenação (Merge/Quick Sort, Heapsort, Elementar)
 ┣ 📂 tests                 # Suite de testes automatizados unitários e de integração[cite: 7]
 ┃ ┣ 📜 test_domain.py
 ┃ ┗ 📜 test_algorithms.py
 ┣ 📜 .env                  # Variáveis de ambiente (HF_TOKEN) - Ignorado no controle de versão
 ┣ 📜 .gitignore
 ┣ 📜 README.md
 ┗ 📜 requirements.txt      # Dependências (pytest, pandas, matplotlib, duckdb, huggingface_hub)[cite: 4, 8]