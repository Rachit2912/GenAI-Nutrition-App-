from dotenv import load_dotenv
load_dotenv()
import streamlit as st
import os 
import google.generativeai as genai
from PIL import Image

genai.configure(api_key = os.getenv("AIzaSyDlOHFLmgqFR6GZfdpCbZoAxpT1vgeszfk"))


##``
def get_gemini_response(input,image,prompt):
    model = genai.GenerativeModel('gemini-pro-vision')
    response = model.generate_content([input,image[0],prompt])
    return response.text



def input_image_setup(uploaded_file):
    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()

        image_parts = [
            {
                "mime_type": uploaded_file.type,
                "data": bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("no file uploaded")



## 
input_prompt = """you are an expert in nutritionist where you need to see the food items from the image and calculate the total calories, also provide the details of every food in below format:

1. Item 1 - no of calories
2. Item 2 - no of calories
----
----
"""


st.set_page_config(page_title = "app")
st.header("ai app")
input = st.text_input("Input Prompt : ",key ="input")
uploaded_file = st.file_uploader("choose an image..", type = ["jpg","jpeg","png"])
image = ""
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image,caption="uploaded image.",use_column_width = True)
submit = st.button("tell me the total calories")


if submit:
    image_data = input_image_setup(uploaded_file)
    response = get_gemini_response(input_prompt,image_data,input)
    st.subheader("the response is :")
    st.write(response)


