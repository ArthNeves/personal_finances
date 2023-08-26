import streamlit as st
import pandas as pd
import os
from datetime import datetime

# Function to calculate budget allocation
def calculate_budget(salary):
    expenses = 0.5 * salary
    wants = 0.2 * salary
    investments = 0.2 * salary
    development = 0.1 * salary
    return expenses, wants, investments, development

# Function to recommend investment portfolio
def recommend_portfolio(amount, goal):
    if goal == 'Short Term':
        debt_funds = amount
        equity_funds = 0
        crypto = 0
        gold = 0
        reits = 0
    elif goal == 'Mid Term':
        debt_funds = 0.7 * amount
        equity_funds = 0.3 * amount
        crypto = 0
        gold = 0
        reits = 0
    else:
        debt_funds = 0.15 * amount
        equity_funds = 0.6 * amount
        crypto = 0.1 * amount
        gold = 0.05 * amount
        reits = 0.05 * amount
    return debt_funds, equity_funds, crypto, gold, reits
def save_to_csv(data, filename):
    now = pd.Timestamp.now()
    data = data.append({'Datetime': now}, ignore_index=True)

    # Verifica se já existe uma entrada com a mesma data e hora
    same_datetime_row = data[data['Datetime'] == now]

    if not same_datetime_row.empty:
        # Substitui os valores da mesma data e hora
        data.loc[same_datetime_row.index[0]] = {'Datetime': now}

    data.to_csv(filename, index=False)

def main():

    # Main page content
    st.set_page_config(page_title='ContaCerta - Seu amigo financeiro 🤑', page_icon="	:money_mouth_face:",)
    st.title("**ContaCerta** - _Seu amigo financeiro_ :money_mouth_face: ")
    st.write("---")

    # Sidebar options
    option = st.sidebar.selectbox(
        'Selecione uma opção:',
        ('Calculadora de orçamento', 'Consultor de investimentos', 'Cursos de investimento','Sobre'),
    )

    # Add a note to the sidebar
    st.sidebar.write("---")
    st.sidebar.write('''
                        
                        **Observação:** Escolha seu **Risco - Recompensa** com prudência e invista seu dinheiro **com sabedoria** de acordo com seus *objetivos*.
                        
                        **_Bom investimento_** :heart:
                                                        ''')


    if option == 'Calculadora de orçamento':
        st.write('### Calculadora de orçamento')
        col, buff = st.columns((1, 1))
        with col:
            salary = st.number_input('Insira seu salário mensal (por exemplo: 500.000):',  step=500)

        if salary:
            expenses, wants, investments, development = calculate_budget(salary)
            st.write('### Alocação de verba')
            st.write(f'*50% para* `Despesas`: **R${expenses:.2f}**')
            st.write(f'*20% para* `Coisas que quero`: **R${wants:.2f}**')
            st.write(f'*20% para* `Fundo de Investimentos e Emergência`: **R${investments:.2f}**')
            st.write(f'*10% para* `Autodesenvolvimento`: **R${development:.2f}**')
        if st.button('Save'):
            save_to_csv(pd.DataFrame({
                'Category': ['Expenses', 'Wants', 'Investments', 'Development', 'Data'],
                'Amount': [expenses, wants, investments, development, pd.Timestamp.now()],
                # 'Datetime': [pd.Timestamp.now()]  # Adicionar a coluna de data e hora
            }), 'budget_allocation.csv')
            st.write('Data saved successfully!')

    elif option == 'Consultor de investimentos':
        st.write('### Consultor de investimentos')
        col, buff = st.columns((1, 1))
        with col:
            amount = st.number_input('Insira o valor do investimento: (por exemplo: 5000)',  step=500)
            goal = st.selectbox('Selecione sua meta de investimento:', ('Curto prazo', 'Médio Prazo', 'Longo prazo'))

        if amount and goal:
            st.write("---")
            st.write('#### Recommended Investment Portfolio')
            debt_funds, equity_funds, crypto, gold, reits = recommend_portfolio(amount, goal)
            st.write(f'`Fundos de dívida externa`: **R${debt_funds:.2f}**')
            st.write(f'`Fundos de ações`: **R${equity_funds:.2f}**')
            st.write(f'`Crypto`: **R${crypto:.2f}**')
            st.write(f'`Tesouro direto`: **R${gold:.2f}**')
            st.write(f'`Fundos imobiliários`: **R${reits:.2f}**')
        if st.button('Save'):
            save_to_csv(pd.DataFrame({
                'Asset': ['Fundos de dívida externa', 'Fundos de ações', 'Crypto', 'Tesouro direto', 'Fundos imobiliários'],
                'Amount': [debt_funds, equity_funds, crypto, gold, reits],
                'Datetime': [pd.Timestamp.now()]  # Adicionar a coluna de data e hora
            }), 'investment_portfolio.csv')
            st.write('Data saved successfully!')

    elif option == 'Cursos de investimento':
        st.write('### Cursos de investimento')
        st.markdown('''
        # Grátis
            https://www.udemy.com/course/orcamento-pessoal-e-familiar-renda-extra/
                    
            https://www.udemy.com/course/minicurso-gratuito-introducao-a-investimentos/
                
            https://www.udemy.com/course/tesouro-direto-intermediario-e-avancado/
                    
        # Melhores aplicativos para organizar suas finaças
                    
            https://www.youtube.com/watch?v=vQG4bC2MPLc

                    ''')


    

    else:
        st.write('### Sobre')
        st.markdown('''
        *ContaCerta* is developed by **Arthur Neves** (AI developer, Data Engineer, Python Backend developer)

        * Github Repo of ContaCerta - 
        * Connect me on LinkedIn - https://www.linkedin.com/in/arthur-neves-perfil/
        # Feedback
            https://www.notion.so/Feedbacks-5441638510dc48609d6431afff6d9d2a?pvs=4

        ''')

if __name__ == "__main__":
    main()