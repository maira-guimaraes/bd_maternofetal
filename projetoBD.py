import streamlit as st
import mysql.connector

# Função para conectar ao banco de dados MySQL
def connect_to_db():
    db_connection = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="Dominique.2018#",
        database="materno_fetal"
    )
    return db_connection

# Função para inserir dados no banco de dados
def insert_data_into_db(data):
    db_connection = connect_to_db()
    cursor = db_connection.cursor()
    query = """
    INSERT INTO formulario_mf (
        idade, escolaridade, cidade_residencia, estado_residencia, maternidade_parto, local_acompanhamento_prenatal,
        tipo_parto, idade_gestacional, avaliacao_risco, num_consultas_prenatal, tempo_espera_atendimento,
        visita_domiciliar, acesso_consultas, acesso_exames_laboratoriais, acesso_exames_imagem,
        orientacao_aleitamento, colocacao_nascidos_colos_peitos, acompanhante_escolha_parto,
        respeito_escolha_local_parto, plano_individual_parto, liberdade_posicao_trabalho_parto,
        silencio_maternidade, respeito_privacidade_parto, apoio_empatico_trabalho_parto,
        oferta_liquidos_trabalho_parto, metodos_alivio_dor_nao_invasivos, mal_atendimento,
        nao_atendida_necessidade, agressao_verbal, agressao_fisica, uso_episiotomia, lavagem_utero,
        infusao_intravenosa
    ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    cursor.execute(query, data)
    db_connection.commit()
    cursor.close()
    db_connection.close()

# Função principal para executar o Streamlit
def main():
    st.title('Cadastro Materno Fetal')
    st.write('Este cadastro tem o objetivo de coletar informações sobre sua trajetória como gestante e parturiente, preencha com atenção.')

    # Dados sociodemográficos
    st.write('Dados Sociodemográficos')
    idade = st.number_input('Idade', min_value=0, max_value=50, step=1)
    escolaridade = st.text_input('Escolaridade', '')
    cidade_residencia = st.text_input('Cidade de Residência', '')
    estado_residencia = st.text_input('Estado de Residência', '')
    maternidade_parto = st.text_input('Maternidade de Realização do Parto', '')
    local_acompanhamento_prenatal = st.text_input('Local do Acompanhamento Pré-natal', '')

    # Características das parturientes
    st.write('Características das parturientes')
    tipo_parto = st.text_input('Tipo de Parto', '')
    idade_gestacional = st.number_input('Idade Gestacional do Parto (em semanas)', min_value=0, max_value=50, step=1)
    avaliacao_risco = st.text_input('Avaliação de Risco de Parto', '')
    num_consultas_prenatal = st.number_input('Número de Consultas no Pré-natal', min_value=0, max_value=50, step=1)
    tempo_espera_atendimento = st.number_input('Tempo de Espera pelo Atendimento Inicial na Internação (em minutos)', min_value=0, max_value=1440, step=15)
    st.write('Marque a caixa de seleção se você teve acesso a:')
    visita_domiciliar = st.checkbox('Visita Domiciliar por Agente Comunitário de Saúde após a Alta da Maternidade')

    # Informações recebidas
    st.write('Informações recebidas')
    acesso_consultas = st.checkbox('Acesso às Consultas')
    acesso_exames_laboratoriais = st.checkbox('Acesso aos Exames Laboratoriais')
    acesso_exames_imagem = st.checkbox('Acesso aos Exames de Imagem')
    orientacao_aleitamento = st.checkbox('Orientação e Ajuda para a Prática do Aleitamento Materno na Maternidade')

    # Equidade e consideração de suas opiniões
    st.write('Equidade e consideração de suas opiniões')
    colocacao_nascidos_colos_peitos = st.checkbox('Recém-nascidos colocados nos colos ou peitos imediatamente após o nascimento')
    acompanhante_escolha_parto = st.checkbox('Acompanhante de sua escolha no momento do parto')
    respeito_escolha_local_parto = st.checkbox('Respeito à escolha da mãe sobre o local do parto')
    plano_individual_parto = st.checkbox('Plano individual de parto')
    liberdade_posicao_trabalho_parto = st.checkbox('Liberdade de posição e movimento durante o trabalho de parto')
    silencio_maternidade = st.checkbox('Silêncio da maternidade')
    respeito_privacidade_parto = st.checkbox('Respeito ao direito da mulher à privacidade no local do parto')
    apoio_empatico_trabalho_parto = st.checkbox('Apoio empático pelos prestadores de serviço durante o trabalho de parto e parto')
    oferta_liquidos_trabalho_parto = st.checkbox('Oferta de líquidos por via oral durante o trabalho de parto e parto')
    metodos_alivio_dor_nao_invasivos = st.checkbox('Métodos não invasivos e não farmacológicos de alívio da dor, como massagem e técnicas de relaxamento, durante o trabalho de parto')

    # Ocorrência de situação desrespeitosa e práticas prejudiciais
    st.write('Ocorrência de situação desrespeitosa e práticas prejudiciais')
    mal_atendimento = st.checkbox('Mal Atendimento')
    nao_atendida_necessidade = st.checkbox('Não foi atendida/ouvida em sua necessidade')
    agressao_verbal = st.checkbox('Agressão Verbal')
    agressao_fisica = st.checkbox('Agressão Física')
    uso_episiotomia = st.checkbox('Uso liberal e rotineiro de episiotomia')
    lavagem_utero = st.checkbox('Lavagem uterina rotineira após o parto')
    infusao_intravenosa = st.checkbox('Infusão intravenosa de rotina no trabalho de parto')

    # Botão para enviar o formulário
    if st.button('Enviar formulário'):
        data = (
            idade, escolaridade, local_residencia, maternidade_parto, local_acompanhamento_prenatal, 
            tipo_parto, idade_gestacional, avaliacao_risco, num_consultas_prenatal, tempo_espera_atendimento, 
            visita_domiciliar, acesso_consultas, acesso_exames_laboratoriais, acesso_exames_imagem, 
            orientacao_aleitamento, colocacao_nascidos_colos_peitos, acompanhante_escolha_parto, 
            respeito_escolha_local_parto, plano_individual_parto, liberdade_posicao_trabalho_parto, 
            silencio_maternidade, respeito_privacidade_parto, apoio_empatico_trabalho_parto, 
            oferta_liquidos_trabalho_parto, metodos_alivio_dor_nao_invasivos, mal_atendimento, 
            nao_atendida_necessidade, agressao_verbal, agressao_fisica, uso_episiotomia, lavagem_utero, 
            infusao_intravenosa
        )
        insert_data_into_db(data)
        st.success('Dados enviados com sucesso!')

# Execução do programa principal
if __name__ == '__main__':
    main()
