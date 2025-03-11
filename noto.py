import streamlit as st
import fitz  # PyMuPDF
from deep_translator import GoogleTranslator
from io import BytesIO
from bidi.algorithm import get_display  # For right-to-left rendering
import arabic_reshaper  # For reshaping Arabic script

# Translator setup
translator = GoogleTranslator(source="en", target="ur")

# Streamlit interface
st.title("PDF Translation to Urdu")
st.write("Upload a PDF file in English to translate it into Urdu.")

# File upload option
uploaded_file = st.file_uploader("Upload your PDF file", type="pdf")

# Include a translate button
if uploaded_file and st.button("Translate"):
    try:
        # Open the uploaded PDF
        pdf_bytes = uploaded_file.read()
        pdf_document = fitz.open(stream=pdf_bytes, filetype="pdf")

        # Corrected font path using double backslashes
        urdu_font_path = r"Noto_Nastaliq_Urdu\\NotoNastaliqUrdu-VariableFont_wght.ttf"

        total_pages = len(pdf_document)
        progress_bar = st.progress(0)  # Initialize a progress bar
        status_text = st.empty()  # For displaying status messages

        # Process each page
        for page_num in range(total_pages):
            page = pdf_document[page_num]
            text_blocks = page.get_text("blocks")  # Extract text blocks

            for block in text_blocks:
                bbox = block[:4]  # Coordinates of the text block
                text = block[4].strip()  # Extract the actual text

                if text:  # Only translate non-empty blocks
                    # Translate the text to Urdu
                    urdu_text = translator.translate(text)
                    reshaped_text = arabic_reshaper.reshape(urdu_text)
                    bidi_text = get_display(reshaped_text)

                    # Clear the original text area with white background
                    page.draw_rect(bbox, color=None, fill=(1, 1, 1))

                    # Manually adjust for right-aligned text (for Urdu)
                    right_x = bbox[2]  # Rightmost x-coordinate
                    y_position = bbox[1]  # Use the top y-coordinate for vertical positioning

                    # Insert the translated text at the adjusted position
                    page.insert_text(
                        (right_x, y_position),  # Right-aligned position
                        bidi_text,
                        fontsize=10,
                        fontfile=urdu_font_path,  # Use the custom Urdu font
                        color=(0, 0, 0),  # Black color for text
                    )

            # Update progress
            progress = (page_num + 1) / total_pages
            progress_bar.progress(progress)
            status_text.text(f"Processing page {page_num + 1} of {total_pages}")

        # Save the translated PDF to memory
        output_pdf = BytesIO()
        pdf_document.save(output_pdf)
        pdf_document.close()

        # Provide download button
        st.success("Translation completed!")
        st.download_button(
            label="Download Translated PDF",
            data=output_pdf.getvalue(),
            file_name="translated-urdu.pdf",
            mime="application/pdf"
        )

    except Exception as e:
        st.error(f"An error occurred: {e}")
