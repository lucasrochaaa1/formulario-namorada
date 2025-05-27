import streamlit as st

st.set_page_config(page_title="Surpresa para você 💖")

st.title("✨ Formulário do Amor ✨")
st.write("Responda com carinho 💌")

# Perguntas
destino = st.text_input("1. Onde você gostaria de ir em nosso próximo encontro?")
comida = st.radio("2. O que você prefere comer?", ["Pizza 🍕", "Sushi 🍣", "Hambúrguer 🍔", "Massa 🍝", "Outro"])
mensagem = st.text_area("3. Quer deixar uma mensagem pra mim? 💬")

# Botão de envio
if st.button("Enviar ❤️"):
    st.success("Obrigado pelo tempo para responder. Obrigado pela parceria! Te amo! 💖")

    st.write("----")
    st.subheader("Suas respostas:")
    st.write(f"📍 Destino: {destino}")
    st.write(f"🍽️ Comida preferida: {comida}")
    st.write(f"💌 Mensagem: {mensagem}")
