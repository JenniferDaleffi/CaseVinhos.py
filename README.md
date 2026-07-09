# Tech Challenge Data Analytics FIAP, 2026 | Fase 2

## Integrantes

- Bruno Querobin Francisco – RM371779

- Henrique dos Reis Machado - RM372837

- Jennifer Eduarda Vieira Daleffi – RM374013

- Leonardo de Carvalho Melo – RM370240 

- Renan Simões de Farias – RM371818 

<h3 align="center"> 🍷 Case de Vinhos 🍷 </h3>

<table align="center">
  <tr>
    <td align="center" style="padding: 10px;">
      <img src="https://github.com/user-attachments/assets/549919ba-db08-44b3-8209-ace69288f2a9" width="120" height="120" style="border-radius: 10px; object-fit: cover;" /><br>
      <sub><b>Bruno</b></sub><br>
      <a href="https://github.com/BrunoQF" target="_blank"><img width="20" height="20" src="https://img.icons8.com/ios-filled/50/github.png" alt="github"/></a>
    </td><td align="center" style="padding: 10px;">
      <img src="https://github.com/user-attachments/assets/71df3046-85db-49c9-a109-67e733f521ab" width="120" height="120" style="border-radius: 10px; object-fit: cover;" /><br>
      <sub><b>Henrique</b></sub><br>
      <a href="https://github.com/IkkiMachado/" target="_blank"><img width="20" height="20" src="https://img.icons8.com/ios-filled/50/github.png" alt="github"/></a>
    </td><td align="center" style="padding: 10px;">
      <img src="https://github.com/user-attachments/assets/b900a0fb-239f-41d9-aa24-c1a3ec473af7" width="120" height="120" style="border-radius: 10px; object-fit: cover;" /><br>
      <sub><b>Jennifer</b></sub><br>
      <a href="https://github.com/JenniferDaleffi/" target="_blank"><img width="20" height="20" src="https://img.icons8.com/ios-filled/50/github.png" alt="github"/></a>
    </td><td align="center" style="padding: 10px;">
      <img src="https://github.com/user-attachments/assets/be1754d2-6580-46e6-820b-b816f83188b8" width="120" height="120" style="border-radius: 10px; object-fit: cover;" /><br>
      <sub><b>Leonardo</b></sub><br>
      <a href="https://github.com/LeoMelo95/" target="_blank"><img width="20" height="20" src="https://img.icons8.com/ios-filled/50/github.png" alt="github"/></a>
    </td><td align="center" style="padding: 10px;">
      <img src="https://github.com/user-attachments/assets/d47f8585-e513-45bb-9e8b-5451113feeb8" width="120" height="120" style="border-radius: 10px; object-fit: cover;" /><br>
      <sub><b>Renan</b></sub><br>
      <a href="https://github.com/ElRekan/" target="_blank"><img width="20" height="20" src="https://img.icons8.com/ios-filled/50/github.png" alt="github"/></a>
    </td>
  </tr>
</table>

# Descrição do projeto: Análise Exploratória e Classificação da Qualidade de Vinhos 🍷 

## Descrição do Projeto

Este projeto realiza uma Análise Exploratória de Dados (EDA) utilizando uma base de dados de qualidade de vinhos, com o objetivo de compreender como as características físico-químicas influenciam na qualidade final da bebida.

Além da exploração dos dados, a variável original **quality** é transformada em uma variável binária (**quality_binary**), permitindo tratar o problema como uma tarefa de **classificação binária**, onde:

- **1:** Vinhos de alta qualidade (nota maior ou igual a 7);
- **0:** Vinhos de qualidade baixa ou intermediária (nota menor que 7).

Durante o projeto são realizadas etapas de limpeza, análise estatística, visualização gráfica, preparação dos dados e avaliação de modelos de Machine Learning para prever a qualidade dos vinhos.

## Tecnologias Utilizadas

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Google Colab / Jupyter Notebook

## Objetivos

- Compreender a estrutura da base de dados;
- Identificar padrões e relações entre as variáveis;
- Preparar os dados para modelagem;
- Construir e avaliar modelos de classificação;
- Comparar métricas de desempenho para selecionar o melhor modelo.

## Base de Dados

A base utilizada é **WineQT.csv**, contendo informações físico-químicas de diferentes vinhos, como:

- Acidez fixa e volátil;
- Ácido cítrico;
- Açúcar residual;
- Cloretos;
- Dióxido de enxofre;
- Densidade;
- pH;
- Sulfatos;
- Teor alcoólico;
- Qualidade do vinho.

## Resultado Esperado

Ao final do projeto, espera-se obter um modelo capaz de classificar corretamente se um vinho possui alta qualidade ou não, utilizando apenas suas características físico-químicas.

# ▶️ Como rodar notebooks (.ipynb) no VS Code com Colab

Siga o passo a passo abaixo para executar seus notebooks diretamente no VS Code usando o Google Colab.

## 🔧 Passo 1: Instalar extensão

Clique no ícone de **Extensões** no menu lateral esquerdo e pesquise por `colab`.

<img width="359" height="320" alt="Image" src="https://github.com/user-attachments/assets/632e2059-946d-41d4-a958-e81b0a37b124" />

---

## 📦 Passo 2: Instalar a extensão correta

Instale a **primeira extensão** que aparecer na busca.  
Ela deve ser a oficial do Google (com verificação).

<img width="678" height="183" alt="Image" src="https://github.com/user-attachments/assets/6838ebca-3319-4790-8260-2476f1b90b90" />

<img width="295" height="70" alt="Image" src="https://github.com/user-attachments/assets/d99101e5-4da2-4c92-a11f-a04720f23ac7" />

## 📂 Passo 3: Abrir o notebook

Abra seu arquivo `.ipynb` e clique em **Run All** para executar todas as células.

<img width="978" height="478" alt="Image" src="https://github.com/user-attachments/assets/eda6da6d-1fbb-48a0-a5d5-641b2aad9de4" />

---

## ⚙️ Passo 4: Selecionar kernel

Clique em **Select Another Kernel**.

<img width="609" height="91" alt="Image" src="https://github.com/user-attachments/assets/6aa4fb11-9c6b-40be-b7be-d0802c2211a6" />

---

## ☁️ Passo 5: Escolher Colab

Selecione a opção **Colab** como ambiente de execução.

<img width="617" height="138" alt="Image" src="https://github.com/user-attachments/assets/42d817d7-f107-4ddd-98ad-827621ceeb0d" />

---

## 🔗 Passo 6: Conectar

Clique em **Auto Connect**.

<img width="610" height="176" alt="Image" src="https://github.com/user-attachments/assets/0a15e16f-e2ba-46a5-b8b8-7bfb9009af1a" />

---

## 🔐 Passo 7: Login

Faça login na sua conta Google e autorize o acesso.  
Depois, escolha a opção para ser redirecionado ao VS Code.

<img width="780" height="313" alt="Image" src="https://github.com/user-attachments/assets/4cc05c1c-a9c5-46ec-a52c-4196f435ef02" />

---

## 🐍 Passo 8: Executar com Python

Selecione o kernel **Python (Ipykernel)** e rode o notebook normalmente.

<img width="598" height="162" alt="Image" src="https://github.com/user-attachments/assets/1040db1d-5b6e-4bce-8ad2-ab9141615346" />