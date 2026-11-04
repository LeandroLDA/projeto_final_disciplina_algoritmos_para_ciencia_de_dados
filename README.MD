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

Este repositório contém o sistema desenvolvido para o projeto final da disciplina de **Algoritmos para Ciência de Dados** do Mestrado Profissional (MECAI) do ICMC-USP[cite: 1]. 

O sistema integra algoritmos próprios implementados em Python, avaliando como as características dos dados e a frequência de consultas/atualizações afetam o desempenho computacional e as escolhas de projeto[cite: 1]. O contexto de aplicação é o **Monitoramento de Equipamentos Industriais**[cite: 7].

## 📌 Contexto e Base de Dados

O domínio escolhido aborda a manutenção preditiva em caminhões pesados, utilizando a base de dados real **SCANIA Component X Dataset**[cite: 10]. Este *dataset* contém séries temporais multivariadas com leituras operacionais, registros de reparo e especificações de frotas[cite: 10, 11].

Para adequação às restrições do projeto:
- Foi gerado um **identificador inteiro não negativo e único** para cada leitura de sensor (`id_leitura`), mantido imutável durante o ciclo de vida do registro[cite: 2].
- As especificações categóricas originais e anonimizadas (ex: `Cat0`, `Cat1`[cite: 15]) foram enriquecidas sinteticamente para fornecer um atributo textual relevante ao domínio, conforme exigido pela modelagem[cite: 2].

## 🏗️ Arquitetura e Estrutura de Pastas

O sistema foi desenhado sob o paradigma de Orientação a Objetos, utilizando contratos explícitos e injeção de dependências (Padrão *Strategy*) para intercambiar algoritmos sem alterar a lógica de serviço[cite: 3].

```text
📦 projeto_final_disciplina_algoritmos_para_ciencia_de_dados
 ┣ 📂 .github
 ┃ ┣ 📂 ISSUE_TEMPLATE      # Padrões para Bug, Feature e Task
 ┃ ┗ 📂 workflows           # CI/CD com GitHub Actions para Pytest
 ┣ 📂 data
 ┃ ┣ 📂 experiments         # Saídas geradas (.csv) com resultados de desempenho[cite: 2]
 ┃ ┣ 📂 processed           # Dataset da Scania com enriquecimento sintético de ID e textos
 ┃ ┗ 📂 raw                 # Arquivos originais anonimizados do SCANIA Component X
 ┣ 📂 docs                  # Relatórios, diagramas de classes e artefatos de defesa[cite: 8]
 ┣ 📂 notebooks             # Exploração de dados (EDA) e plotagem de gráficos finais[cite: 4]
 ┣ 📂 src                   # Núcleo do sistema OO
 ┃ ┣ 📜 domain.py           # Entidades (Registros) com encapsulamento rigoroso[cite: 3]
 ┃ ┣ 📜 experiments.py      # Executor isolado para medição de tempos e comparações[cite: 6]
 ┃ ┣ 📜 hashtable.py        # Tabela Hash própria com política de resolução de colisões[cite: 5]
 ┃ ┣ 📜 repository.py       # Repositório central, gerenciamento de coleções e índices[cite: 3]
 ┃ ┣ 📜 searching.py        # Algoritmos de busca (Binária, Sequencial, Indexada/Exponencial)[cite: 4]
 ┃ ┗ 📜 sorting.py          # Algoritmos de ordenação (Merge/Quick Sort, Heapsort, Elementar)[cite: 4]
 ┣ 📂 tests                 # Suite de testes automatizados unitários e de integração[cite: 7]
 ┃ ┣ 📜 test_domain.py
 ┃ ┗ 📜 test_algorithms.py
 ┣ 📜 .gitignore
 ┣ 📜 README.md
 ┗ 📜 requirements.txt      # Dependências explícitas (pytest, pandas, matplotlib)[cite: 4, 8]

```

## 🚀 Funcionalidades e Requisitos Técnicos

* **Ordenação:** Três algoritmos próprios (elementar, estrutural recursiva e Heapsort) operando sob uma interface comum.


* **Busca:** Métodos sequencial, binário e um método adicional avançado operando sobre os dados no repositório.


* **Tabela Hash:** Estrutura própria encapsulando inserção, consulta, remoção e estudo de fator de carga.


* **Experimentos:** Execução e comparação padronizada (usando `time.perf_counter_ns`), exportando configuração, tamanho, distribuição e repetições.



## 🛠️ Como Reproduzir (Guia Rápido)

Para testar as funcionalidades pelo terminal, sem depender de extensões de editores:

**1. Clone o repositório e acesse a pasta:**

```bash
git clone [https://github.com/LeandroLDA/projeto_final_disciplina_algoritmos_para_ciencia_de_dados.git](https://github.com/LeandroLDA/projeto_final_disciplina_algoritmos_para_ciencia_de_dados.git)
cd projeto_final_disciplina_algoritmos_para_ciencia_de_dados

```

**2. Crie e ative um ambiente virtual (Recomendado):**

```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
# ou
venv\Scripts\activate     # Windows (PowerShell)

```

**3. Instale as dependências:**

```bash
pip install -r requirements.txt

```

**4. Execute os testes unitários de consistência:**

```bash
pytest tests/

```

**5. Rode o executor de experimentos:**

```bash
python -m src.experiments

```

---

Projeto acadêmico desenvolvido em cumprimento aos requisitos da disciplina do MECAI / ICMC-USP. Referências bibliográficas completas encontram-se na documentação na pasta `/docs`.
