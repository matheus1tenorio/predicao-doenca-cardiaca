# Predição de Doença Cardíaca

## Sobre o Projeto

Este projeto utiliza técnicas de Machine Learning para prever a presença de doença cardíaca com base em informações clínicas dos pacientes.

Foi realizado a exploração dos dados, treinamento e avaliação dos modelos de Machine Learning usando a ferramenta do Jupyter Notebook. A aplicação foi desenvolvida em Python utilizando Streamlit para a interface web e o algoritmo K-Nearest Neighbors (KNN) para realizar as predições.

Você pode acessar a aplicação de forma online em: https://predicao-doenca-cardiaca.streamlit.app/

<img width="1326" height="749" alt="Captura de tela 2026-06-08 174225" src="https://github.com/user-attachments/assets/48d2f464-f817-42cc-80fb-435599299399" />
<img width="953" height="863" alt="Captura de tela 2026-06-08 174317" src="https://github.com/user-attachments/assets/eb40d871-37e2-43f2-99c3-5aa6cfd16f20" />
<img width="1050" height="860" alt="Captura de tela 2026-06-08 174245" src="https://github.com/user-attachments/assets/799729e5-3481-4552-8baf-ecd8d8496465" />

## Tecnologias Utilizadas

* Python
* Pandas
* NumPy
* Scikit-Learn
* Streamlit
* Joblib

## Dataset

O conjunto de dados utilizado neste projeto foi obtido no Kaggle:

Soriano, F. (2021). *Heart Failure Prediction Dataset*. Kaggle. Disponível em: https://www.kaggle.com/datasets/fedesoriano/heart-failure-prediction

O conjunto de dados utilizado contém informações clínicas de pacientes, incluindo:

* Idade
* Sexo
* Pressão arterial em repouso
* Colesterol
* Glicemia em jejum
* Frequência cardíaca máxima
* Tipo de dor no peito
* Eletrocardiograma em repouso
* Angina induzida por exercício
* Oldpeak
* Inclinação do segmento ST

Variável alvo:

* HeartDisease (0 = ausência de doença cardíaca, 1 = presença de doença cardíaca)

## Etapas do Projeto

### 1. Análise Exploratória dos Dados (EDA)

* Distribuição das variáveis
* Análise bivariada
* Correlação entre atributos
* Heatmap
* Entre outros

### 2. Pré-processamento

* Tratamento de inconsistências
* Tratamento de outliers
* Encoding das variáveis categóricas
* Padronização dos dados
* Entre outros

### 3. Modelagem

Foram avaliados os seguintes algoritmos:

* Logistic Regression
* KNN
* SVM
* Random Forest
* XGBoost

### 4. Avaliação

As métricas utilizadas foram:

* Accuracy
* Precision
* Recall
* F1-Score
* ROC-AUC

## Melhor Modelo

O algoritmo KNN apresentou o melhor desempenho geral e foi selecionado como modelo final da aplicação.

## Como Executar

Acesse de forma online: https://predicao-doenca-cardiaca.streamlit.app/

Acesse de forma local:

- Instale as dependências:

```bash
pip install -r requirements.txt
```

- Execute a aplicação:

```bash
streamlit run app.py
```


