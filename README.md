# **MVP Machine Learning**
![Banner MVP Machine Learning](https://github.com/Penichezito/MVP-MachineLearning/blob/main/frontend/app/src/assets/mvp-banner-ml.jpg)

## **Visão Geral**

Este notebook demonstra um projeto de Machine Learning para construir um modelo de classificação que prevê se um determinado laptop deve ser recomendado aos clientes. O conjunto de dados original contém informações sobre vários laptops, incluindo preço, fabricante, categoria, especificações de tela, GPU, sistema operacional, CPU, RAM, armazenamento, peso e preço.

Este projeto tem como objetivo desenvolver um modelo de machine learning para classificação utilizando técnicas clássicas e bibliotecas como Scikit-learn, Pandas e Numpy. O modelo será treinado, otimizado e avaliado de forma detalhada em um notebook Google Colab. Posteriormente, será integrado a uma aplicação full-stack simples para realizar predições em tempo real.
Este notebook demonstra um projeto de Machine Learning para construir um modelo de classificação que prevê se um determinado laptop deve ser recomendado aos clientes. O conjunto de dados original contém informações sobre vários laptops, incluindo preço, fabricante, categoria, especificações de tela, GPU, sistema operacional, CPU, RAM, armazenamento, peso e preço.

## **Requisitos**
- Linguagem: Python
- **Bibliotecas Principais:** Scikit-learn, Pandas, NumPy, Flask (ou framework similar para o backend)
- **Ferramentas:** Google Colab, PyTest
- **Estrutura do Projeto**
  - **notebook.ipynb:** Contém o código para pré-processamento de dados, treinamento do modelo, otimização de hiperparâmetros e avaliação.
  - **backend/api:** Backend da aplicação Flask, responsável por carregar o modelo e realizar as predições.
  - **frontend/app-front:** Contém uma aplicação simples Frontend usando React + Vite para a interface do usuário.
  - **tests:** Diretório com os testes automatizados utilizando PyTest.

# **Etapas do Projeto/Requisitos MVP**

## **Coleta e Preparação dos Dados:**
- Escolha e Preparação do Modelo (Dataset)
- Carregar o conjunto de dados.
- Dividir os dados em conjuntos de treino e teste.
- Realizar pré-processamento (normalização, padronização).

## **Modelagem:**
- Treinar modelos utilizando KNN, Árvore de Decisão, Naive Bayes e SVM.
- Otimizar hiperparâmetros utilizando técnicas como Grid Search ou Randomized Search.
- Avaliar os modelos utilizando métricas apropriadas (acurácia, precisão, recall, F1-score).
- Seleção do Melhor Modelo:
- Comparar os modelos e escolher o que apresentar o melhor desempenho.
- Exportar o modelo selecionado para uso na aplicação.
- Desenvolvimento da Aplicação:
- Criar uma interface web simples utilizando Flask e um framework frontend (nesse caso foi escolhido o React utilizando o Vite).
- Carregar o modelo no backend.
- Permitir ao usuário inserir novos dados.
- Realizar a predição e exibir o resultado.

## **Testes Automatizados:**
Implementar testes para verificar o desempenho do modelo.
Definir métricas e thresholds para avaliar se o modelo atende aos requisitos.

## **Segurança:**

- Aplicar técnicas de anonimização de dados para proteger a privacidade.
- Considerar outras práticas de segurança, como validação de entrada e proteção contra ataques.

## Etapas e explicação do Notebook

1. **Carregamento e Preparação de Dados:** Os dados são carregados, os valores ausentes são tratados e o problema de regressão é transformado em um problema de classificação usando clustering K-Means.

2. **Engenharia de Recursos:** O One-Hot Encoding é usado para converter recursos categóricos em numéricos.

3. **Seleção de Modelo:** Vários modelos de classificação são avaliados, incluindo KNN, Árvore de Decisão, Naive Bayes, SVM e Random Forest.

4. **Validação Cruzada:** A validação cruzada estratificada de 10 vezes é usada para avaliar o desempenho do modelo.

5. **Otimização de Hiperparâmetros:** O GridSearchCV é usado para encontrar os melhores hiperparâmetros para os modelos.

6. **Avaliação do Modelo:** O modelo final é avaliado no conjunto de teste e sua precisão é relatada.

7. **Simulação de Previsão:** Um novo conjunto de dados de amostra é usado para simular como o modelo faria previsões em dados não vistos.

## Resultados

O modelo KNN com os melhores hiperparâmetros (métrica euclidiana e 7 vizinhos) atinge uma alta precisão no conjunto de teste. O notebook demonstra o processo de construção, avaliação e uso de um modelo de Machine Learning para um problema de classificação.

# Como Iniciar/Executar seu projeto

## *Clone o repositório:*

Bash
```
git clone https://github.com/Penichezito/MVP-MachineLearning.git
```

### ** BACKEND - Python Flask Openapi3**

É altamente recomendável criar um ambiente virtual

**Criação do ambiente virtual e instalação das dependências:**
Bash
```
python -m venv venv   
```

**Ativa o ambiente virtual criado**
```
venv/bin/activate ou   #ativa o ambiente virtual linux e mac
```
```
venv/Script/activate   #ativa venv no windows
```
**Instalando dependências contigas no arquivo requirements.txt**
```
pip install -r requirements.txt  
```

## **FRONTEND React + Vite**

!()[]

**Configuração do Vite: No terminal, crie um novo projeto e instale as dependências:**

Criar a estrutura inicial do Vite (caso não tenha copiado o projeto e queira fazer um novo frontend)
```
npm create vite@latest my-react-app -- --template react
```

*Entrar na pasta criada*
```
cd my-react-app
```

Instalar os pacotes npm
```
npm install
```

Rodar aplicação
```
npm run dev
```

### *Execute o notebook:*

Bash
```
jupyter notebook notebook.ipynb
```

### *Inicie o servidor Flask:*

Bash
```
python app.py
ou
flask --app app run --debug
```

*Acesse a aplicação no navegador:*
http://127.0.0.1:5000


## Pytest (Testes automatizados)

Este projeto utiliza pytest para realizar testes automatizados, garantindo a funcionalidade e a integridade do modelo de recomendação de laptops.

**Estrutura dos Testes**
***Os testes estão localizados no arquivo test_model.py e cobrem as seguintes áreas:***
- Carregamento de dados de teste: Os dados são carregados de um arquivo CSV e divididos em conjuntos de treino e teste.
- Treinamento do modelo: O teste verifica se o modelo pode ser treinado corretamente com os dados fornecidos.
- Predições do modelo: O teste verifica se o modelo pode fazer predições com os dados de teste.
- Acurácia do modelo: O teste calcula a acurácia das predições do modelo e verifica se ela atende a um limiar definido.

### **Como Executar os Testes**
***Para executar os testes, siga os passos abaixo:***

**Instale as dependências:**
sh
```
pip install -r requirements.txt
```
**Execute o pytest: No terminal, navegue até o diretório do projeto e execute:**
sh
```
pytest test_model.py
```

**Exemplo de Saída dos Testes**
***A saída do pytest indicará se os testes passaram ou falharam, fornecendo detalhes sobre cada caso de teste.***

```
=========================== test session starts ===========================
platform linux -- Python 3.x.x, pytest-6.x.x, py-1.x.x, pluggy-0.x.x
collected 3 items                                                            

test_model.py ...                                                     [100%]

============================ 3 passed in 0.03s =============================
```

## *Próximos Passos(sugestões)*
- Deploy: Implementar o deploy da aplicação em um ambiente de produção.
- Monitoramento: Implementar um sistema de monitoramento para acompanhar o desempenho do modelo em produção.
- Melhorias: Tente melhorar o modelo através da coleta de novos dados e refinamento dos algoritmos.
- Observações:
 - Personalize: Adapte este README.md para refletir especificamente o seu projeto.
 - Detalhes: Inclua mais detalhes sobre as etapas, como as métricas utilizadas e os hiperparâmetros ajustados.
 - Contribuições: Fique a vontade para contribuir com o projeto adicionando melhorias e sugestões
