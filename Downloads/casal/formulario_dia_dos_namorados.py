import streamlit as st
import smtplib
from email.message import EmailMessage

# Mostra a foto no topo (troque pelo nome do arquivo ou link)
st.image("foto_casal.jpg", width=400)  # se for arquivo local
# st.image("https://link-da-sua-foto.jpg", width=400)  # se for URL

st.title("Fala minha parceira, inovei isso aqui para saber o que você prefere fazer no Dia dos Namorados 💖")

# Perguntas
presente = st.text_input("O que você quer de presente?")
lanche_ou_jantar = st.radio("Lanche ou Jantar?", ["Lanche", "Jantar"])
mensagem_ela = st.text_area("Quer dizer algo especial?")

if st.button("Enviar respostas"):
    EMAIL_ADDRESS = "lc.rochaaa@hotmail.com"        # seu email Outlook
    EMAIL_PASSWORD = "Flamengo2019*"            # senha de app do Outlook

    msg = EmailMessage()
    msg['Subject'] = 'Respostas do formulário do Dia dos Namorados'
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = EMAIL_ADDRESS

    corpo = f"""
    Respostas da minha parceira:

    O que quer de presente: {presente}
    Prefere: {lanche_ou_jantar}
    Mensagem especial: {mensagem_ela}

    Obrigado pela parceria! Te amo 💖
    """

    msg.set_content(corpo)

    try:
        with smtplib.SMTP('smtp.office365.com', 587) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            smtp.send_message(msg)
        st.success("Respostas enviadas com sucesso! Obrigado por responder ❤️")
    except Exception as e:
        st.error(f"Erro ao enviar email: {e}")
