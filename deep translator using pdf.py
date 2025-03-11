import streamlit as st
import fitz  # PyMuPDF
from deep_translator import GoogleTranslator
from PIL import Image
import numpy as np

# Set constants
WHITE = (1, 1, 1)
textflags = fitz.TEXT_DEHYPHENATE
to_urdu = GoogleTranslator(source="en", target="ur")

# Streamlit interface
st.title("PDF Translation to Urdu")
st.write("Upload a PDF file in English to translate it into Urdu.")

# File upload option
uploaded_file = st.file_uploader("Upload your PDF file", type="pdf")

if uploaded_file:
    try:
        # Open the uploaded PDF
        with open("temp.pdf", "wb") as f:
            f.write(uploaded_file.read())
        
        doc = fitz.open("temp.pdf")

        # Add translation layer
        ocg = doc.add_ocg("urdu", on=True)

        # Process each page
        for page in doc:
            print(f"Processing page {page.number + 1} of {len(doc)}")
            
            blocks = page.get_text("blocks", flags=textflags)
            for block in blocks:
                bbox = block[:4]
                text = block[4]
                
                # Translate text to Urdu
                urdu = to_urdu.translate(text)
                
                # Extract the background color of the bounding box
                pix = page.get_pixmap(clip=fitz.Rect(*bbox))
                img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
                avg_color = np.array(img).mean(axis=(0, 1)).astype(int)
                
                # Normalize the color values to a range [0, 1] for PyMuPDF
                normalized_bg_color = (avg_color[0] / 255, avg_color[1] / 255, avg_color[2] / 255)

                # Calculate font size based on bounding box dimensions
                box_width = bbox[2] - bbox[0]
                box_height = bbox[3] - bbox[1]
                
                # Set font size proportional to the box size, ensuring it fits
                font_size = min(box_width, box_height)*0.6  # Adjust 0.2 as necessary for better fit
                
                # Ensure the font size is not too small
                font_size = max(font_size, 10)  # Minimum font size for readability

                # Draw the translated text with the matching background
                page.draw_rect(bbox, color=None, fill=normalized_bg_color, oc=ocg)
                
                # Insert the translated Urdu text with RTL (Right-To-Left) direction
                page.insert_htmlbox(
                    bbox,
                    urdu,
                    css=f"""
                        * {{
                            font-family: sans-serif;
                            background-color: rgb({avg_color[0]}, {avg_color[1]}, {avg_color[2]});
                            font-size: {font_size}px;  /* Scalable font size */
                            text-align: right;         /* Right alignment for RTL text */
                            /* direction: rtl;*/            /* Right-to-left direction for Urdu */
                            margin: 0;
                            padding: 0;
                            overflow-wrap: break-word; /* Handle long words */
                        }}
                    """,
                    oc=ocg
                )

        # Save the translated PDF
        output_file = "translated-urdu.pdf"
        doc.subset_fonts()
        doc.ez_save(output_file)

        st.success("Translation completed!")
        with open(output_file, "rb") as f:
            st.download_button(
                label="Download Translated PDF",
                data=f,
                file_name="translated-urdu.pdf",
                mime="application/pdf"
            )
    except Exception as e:
        st.error(f"An error occurred: {e}")
