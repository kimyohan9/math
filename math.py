import os
from openai import OpenAI
import streamlit as st

os.environ["OPENAI_API_KEY"] = "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"
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

st.title('😁수학단어를 물어보세요😁')

keyword = st.text_input("어떤 단어가 어려우시나요?")

if st.button('생성하기'):
    with st.spinner('찾는중입니다'):
        chat_completion = client.chat.completions.create(
            messages=[
            {
                "role": "user",
                "content": keyword,
            },
            {
                "role": "system",
                "content": "입력받은 단어을 쉽게 예시와 활용법과 함께 설명해줘",
            }
            ],
            model="gpt-4o",
        )
        result = chat_completion.choices[0].message.content
        st.write(result)