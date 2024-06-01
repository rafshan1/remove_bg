from rembg import remove
from PIL import Image
import io
import streamlit as st

st.image("remove_bg.png")
upload_file = st.file_uploader("Choose your image!", type=['jpg', 'jpeg', 'png'])

if upload_file is not None:
    input_image = Image.open(upload_file)
    
    st.write("Processing....")
    output_image = remove(input_image)

    output_buffer = io.BytesIO()
    output_image.save(output_buffer, format="PNG")

    output_buffer.seek(0)
    st.image(output_image, caption='Background removal complete', use_column_width=True)
    
    st.download_button(
        label='Click here to download',
        file_name='Remove_bg.png',
        data=output_buffer,
        mime='image/png'
    )
