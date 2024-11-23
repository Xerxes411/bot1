import streamlit as st
from openai import OpenAI

import streamlit as st

enable = st.checkbox("Enable camera")
picture = st.camera_input("Take a picture", disabled=not enable)

if picture:
    st.image(picture)

st.balloons()
# Show title and description.
st.title("♫ Berserk ♫")
st.write(
   "Esta es una aplicación impulsada por OpenAI, un modelo que genera respuestas ♫◄‼‼►♫. "
   "Para usar esta aplicación, necesitas proporcionar una clave de API de OpenAI, la cual puedes obtener. [here](https://platform.openai.com/account/api-keys). "
   "Aquí te recomiendo un video de una entrevista a MrBeast hecha por El bicho, SIUUUUUUUUUU [Enlace a Youtube](https://www.youtube.com/watch?v=aDF_ESN80r8)."
)
openai_api_key = st.secrets["api_key"] 
# Create an OpenAI client.
client = OpenAI(api_key=openai_api_key)

prompt = st.chat_input("What is up?")
if prompt==None:
   st.stop()

with st.chat_message("user"):
   st.markdown(prompt)

# Generate a response using the OpenAI API.

stream = client.chat.completions.create(
        model="gpt-4o-mini",  
        messages=[
            {"role": "system", "content": "You are an assistant."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=800,
        temperature=0,
    )
respuesta = stream.choices[0].message.content
with st.chat_message("assistant"):
   st.write(respuesta)
