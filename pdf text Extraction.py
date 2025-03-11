import fitz  # PyMuPDF
from deep_translator import GoogleTranslator

def extract_and_translate_paragraphs(pdf_path, target_language="ur"):
    paragraphs = []
    translated_paragraphs = []
    translator = GoogleTranslator(source="auto", target=target_language)

    doc = fitz.open(pdf_path)
    for page_num in range(len(doc)):
        page = doc[page_num]
        # Extract text blocks
        blocks = page.get_text("blocks")
        for block in blocks:
            raw_paragraph = block[4].strip()
            if raw_paragraph:
                # Merge broken lines (joins lines unless separated by a blank line)
                cleaned_paragraph = " ".join(line.strip() for line in raw_paragraph.splitlines() if line.strip())
                paragraphs.append(cleaned_paragraph)
                # Translate the paragraph
                translated_paragraph = translator.translate(cleaned_paragraph)
                # Add RTL embedding for proper direction
                translated_paragraph = f"\u202b{translated_paragraph}"
                translated_paragraphs.append(translated_paragraph)

    return paragraphs, translated_paragraphs

# Usage
pdf_file = "Artificial_intelligence_241223_155933-1.pdf"
original_paragraphs, translated_paragraphs = extract_and_translate_paragraphs(pdf_file, target_language="ur")

# Display both original and translated paragraphs in the terminal
for i, (original, translated) in enumerate(zip(original_paragraphs, translated_paragraphs), start=1):
    print(f"Paragraph {i}:\nOriginal:\n{original}\n\nTranslated:\n{translated}\n")
    print("-" * 80)
