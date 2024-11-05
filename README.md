# Breweries-Data-Pipeline

Este projeto utiliza a API Open Brewery DB para construir um pipeline de dados em uma Arquitetura de Data Lake seguindo a abordagem medallion (Bronze, Silver e Gold). 

## Índice
1. [API](#api)
2. [Ferramenta de Orquestração](#ferramenta-de-orquestração)
3. [Linguagem](#linguagem)
4. [Containerização](#containerização)
5. [Monitoramento e Alertas](#monitoramento-e-alertas)
6. [Serviços em Nuvem](#serviços-em-nuvem)

---

## 1. API
Utilizada a API Open Brewery DB para buscar dados de cervejarias. A API tem um endpoint listar cervejaria e está disponível no link abaixo:

- Documentação: [Open Brewery DB API](https://www.openbrewerydb.org/)

## 2. Ferramenta de Orquestração
Optamos pelo Apache Airflow para orquestrar o pipeline de dados devido a suas funcionalidades robustas para:

- **Agendamento**: O pipeline executa diariamente para coletar dados atualizados.
- **Tentativas de Reexecução**: Configuramos tentativas de reexecução para lidar com falhas temporárias.
- **Tratamento de Erros**: Incluímos um tratamento de erros com notificações para falhas em tarefas críticas.

A documentação encontra-se no documento 'airflow.pdf'.(encaminhada por e-mail)

### Arquivos de Configuração (enviado por e-mail/anexo)
- Os seguintes arquivos:  
- **airflow.pdf** contém os exemplos criados no airflow.
- **gcp_docker.pdf** contém a configuração e execução do Docker e Cloud.
- **monitoramento_alertas.pdf** define uma sugestão de monitoramento e alerta.

## 3. Linguagem
Utilizei a linguagem Python para a criação desse projeto.

## 4. Containerização
Para modularizar o ambiente, criei 03 contêineres Docker:

- **Contêiner 1**: Consumo da API (Camada Bronze) - (arquivo em anexo)

- **Contêiner 2**: Transformação e Particionamento (Camada Silver) - (arquivo em anexo)

- **Contêiner 3**: Agregação e Relatórios (Camada Gold) - (arquivo em anexo)

A documentação encontra-se no gcp_docker.pdf'(encaminhada por e-mail).

## 5. Monitoramento e Alerta
A documentação desse processo encontra-se no 'monitoramento_alertas.pdf'(encaminhada por e-mail).

## 6. Serviços em Nuvem
A ferramenta utilizada foi o Google Cloud Platform(GCP).
A documentação encontra-se no gcp_docker.pdf' (encaminhada por e-mail).