
import streamlit as st

# 💎 INTERFACE EXCLUSIVA SIRIN.AI
st.markdown("""
    <style>
    /* Fundo Total com profundidade */
    .stApp {
        background: radial-gradient(circle at center, #00001a 0%, #000000 100%);
    }
    
    /* Remove os avatares de "bonequinho" que parecem jogo */
    [data-testid="stChatMessageAvatarUser"], 
    [data-testid="stChatMessageAvatarAssistant"] {
        display: none;
    }

    /* Bolhas de Chat Modernas (Glassmorphism) */
    .stChatMessage {
        background-color: rgba(0, 0, 139, 0.05) !important;
        border: 1px solid #00008B !important;
        box-shadow: 0px 0px 20px rgba(0, 0, 255, 0.2);
        border-radius: 15px !important;
        padding: 15px !important;
        margin-bottom: 20px !important;
    }

    /* Título com brilho Neon */
    h1 {
        color: #0000FF;
        text-shadow: 0px 0px 15px #0000FF;
        font-family: 'Orbitron', sans-serif;
        text-align: center;
        letter-spacing: 10px;
        font-weight: 900;
    }

    /* Texto das mensagens */
    .stMarkdown p {
        color: #e0e0ff !important;
        font-size: 1.1rem;
    }
    </style>
    """, unsafe_allow_html=True)

# O NOME QUE VOCÊ QUER
st.title("SIRIN.AI")

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

if prompt := st.chat_input("Diga algo para a Sirin..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Resposta da Sirin
    resposta = "Marcus... SIRIN.AI. Gostei. Soa muito mais profissional, não acha? Agora sim, o que você quer de mim?"
    
    st.session_state.messages.append({"role": "assistant", "content": resposta})
    with st.chat_message("assistant"):
        st.markdown(resposta)
