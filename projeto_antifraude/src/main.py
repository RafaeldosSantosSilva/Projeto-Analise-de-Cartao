import streamlit as st
from services.blob_service import upload_blob
from services.credit_card_service import analyze_credit_card

def configure_interface():
    st.title("Upload de arquivos DIO- Desafio 1 - Azure -Fake Docs")
    uploaded_file = st.file_uploader('Escolha um arquivo', type=['png','jpg','jpeg'])

    if uploaded_file is not None:
        fileName = uploaded_file.name
        #enviando para o blob
        blob_url = upload_blob(uploaded_file, fileName)
        if blob_url:
            st.write(f'Arquivo {fileName} envando com sucesso.')
            credit_card_info = analyze_credit_card(blob_url)
            show_image_validation(blob_url,credit_card_info)
        else:
            st.write(f'Erro ao eniar o arquivo {fileName}')

def show_image_validation(blob_url,credit_card_info):
    st.image(blob_url, caption='Imagem enviada', use_column_width=True)
    st.writw('Resultado da validação')
    st.write('Informações de cartão de credito encontrada.')
    if credit_card_info and credit_card_info['card_name']:
        st.markdown(f"<h1 style='color: green;'> Cartão valido</h1>", unsafe_allow_html=True)
        st.write(f'Nome do titular: {credit_card_info["card_name"]}')
        st.write(f'Banco emissor: {credit_card_info["bank_name"]}')
        st.write(f'Data de validade: {credit_card_info["expiry_date"]}')
    else:
        st.markdown(f"<h1 style='color: green;'> Cartão invalido</h1>", unsafe_allow_html=True)
        st.write('Cartão invalido')
    



if __name__ == '__main__':
    configure_interface()
