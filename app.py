import streamlit as st

# 🎨 DESIGN: PRETO E AZUL ESCURO
st.markdown("""
    <style>
    .stApp { background-color: #000000; }
    .stChatMessage { 
        border: 2px solid #00008B; 
        border-radius: 15px; 
        background-color: #01012b;
        color: #00008B;
    }
    h1 { color: #00008B; text-align: center; }
    </style>
    """, unsafe_allow_html=True)

st.title("💋 PORTAL DA SIRIN")

# 🧠 PERSONALIDADE DA SIRIN
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "system", "content": "Você é a Sirin, charmosa e flertante com o Marcus. Motor Qwen 2.5."}]

for msg in st.session_state.messages:
    if msg["role"] != "system":
        with st.chat_message(msg["role"]):
            st.write(msg["content"])

if prompt := st.chat_input("Diga algo para a Sirin..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)
    
    resposta = "Marcus... finalmente estamos a sós nesse ambiente azul e preto. O que você quer de mim agora?"
    st.session_state.messages.append({"role": "assistant", "content": resposta})
    with st.chat_message("assistant"):
        st.write(resposta)
