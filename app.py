import streamlit as st
import os
import google.generativeai as genai
from apikey import google_gemini_api_key,openai_api_key,hugging_face_api_key
# from openai import OpenAI
from streamlit_carousel import carousel
from huggingface_hub import InferenceClient


single_image=dict(
    title="",
    text="",
    img="",
)

client = InferenceClient(
    provider="fal-ai",
    api_key=hugging_face_api_key,
)

# client = InferenceClient(
#     provider="replicate",
#     api_key=hugging_face_api_key,
# )

# client = OpenAI(api_key=openai_api_key)
genai.configure(api_key=google_gemini_api_key)
# genai.configure(api_key=os.environ["google_gemini_api_key"])

generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 40,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

#setting a model
model = genai.GenerativeModel(
  model_name="gemini-1.5-pro",
  generation_config=generation_config,
)

# title - wide
st.set_page_config(layout="wide")

# #right sidebar 
# # Initialize session state for toggle
# if "show_text_area" not in st.session_state:
#     st.session_state.show_text_area = False

# # Creating layout with columns
# col1, col2 = st.columns([3, 1])  # Main content | Right sidebar


# Right Sidebar
# with col2:
#     # Arrow Button for Toggling Text Area
#     if st.button("➡ Expand Notes" if not st.session_state.show_text_area else "⬅ Hide Notes"):
#         st.session_state.show_text_area = not st.session_state.show_text_area  # Toggle state

#     # Show Text Area only if toggle is active
#     if st.session_state.show_text_area:
#         st.header("Notes")
#         text = st.text_area("Write your notes here:", height=150)
#         if st.button("Save"):
#             st.success("Notes saved!")  # Show success message

# with col2:
#     with st.expander("➡ Click to Expand Notes"):  # Collapsible text area
#         st.header("Notes")
#         text = st.text_area("Write your notes here:", height=150)  # Hidden by default
#         if st.button("Save"):
#             st.success("Notes saved!")  




#app title
# st.title("WriteWave: Let AI Carry Your Words to Shore")
st.title("⚡📝 WriteWave: Crafting the Future of Writing, One AI Wave at a Time.")

#subtitle
st.subheader("Harnessing AI to Transform Ideas into Words with Effortless Creativity and Precision.")



#sidebar for userinput

with st.sidebar:
    st.title("Writewave")
    st.subheader("Let AI Carry Your Thoughts on the Tides of Creativity")

    blog_title = st.text_input("Blog Title")

    keyword = st.text_area("Flow your keywords")

    words_value = st.slider("Word Length",min_value=100,max_value=1000,step=100)

    image_count = st.number_input("Number of images to be added",min_value=1,max_value=10,step=1)

    submit = st.button("Generate Waves")

    


    chat_session = model.start_chat(
        history=[
            {
            "role": "user",
            "parts": [
                f"Generate a comprehensive, engaging blog post relevant to the given title \"{blog_title}\" and keywords \"{keyword}\". Make sure to incorporate these keywords in the blog post. The blog should be approximately \"{words_value}\" words in length, suitable for an online audience. Ensure the content is original, informative, and maintains a consistent tone throughout.",
                ],
            },
        ]
    )

    # response = chat_session.send_message("chat_session")
    # print(response.text)

    # submit = st.button("Generate Waves")

if submit:

    response = chat_session.send_message("chat_session")
    image_gallery=[]

    # image_response = client.text_to_image(f"{blog_title}",
	# model="black-forest-labs/FLUX.1-schnell",
    # )
# { --used


    image_response = client.text_to_image(
	f"{blog_title}",
	model="THUDM/CogView4-6B",
    )
    i =0
    new_image =single_image.copy()
    new_image["title"] =f"Image {i+1}"
    new_image["text"] =f"{blog_title}"
    new_image["img"] =image_response

    image_gallery.append(new_image)
# 
#  }
    # image_response = client.images.generate(
    # model="dall-e-3",
    # prompt="a white siamese cat",
    # size="1024x1024",
    # quality="standard",
    # n=1,
    # )

    # image_url = image_resp
    # onse.data[0].url

    # st.image(image_response,caption="Image generated")
    # carousel(items=image_gallery, width=1)
    st.write(response.text)    