# 📜 PDF to Urdu Translator

## 📝 Overview
This project is a **PDF to Urdu Translator** that extracts text from a PDF file, translates it into Urdu while preserving the document's formatting and structure, and provides the translated version for download. The tool ensures that tabular data, headings, and paragraphs remain intact.

## 🚀 Features
- 🏗 Extracts text from PDF while preserving formatting
- 🌍 Translates text from English to Urdu using OpenAI's GPT API
- 🤖 Supports **Deep Translator** for alternative translation models
- 📂 Supports structured document conversion (tables, paragraphs, headings)
- 🖥️ Simple web-based interface with **Streamlit**
- 📥 Upload and **download translated HTML**

## 🔧 Technologies Used
- **Python** (Backend Processing)
- **Streamlit** (Frontend UI)
- **OpenAI GPT API** (Translation Engine)
- **Deep Translator** (Alternative Translation Models)
- **pdfminer.six / PyMuPDF** (PDF Parsing)
- **BeautifulSoup** (HTML Parsing & Modification)

## 🤖 Best Translation Models Used
- **OpenAI GPT (3.5/4)** - High-quality, context-aware translations
- **Google Translator (via Deep Translator)** - Reliable and accurate translations
- **M2M-100 (Facebook AI)** - Supports direct Urdu translation without intermediary languages
- **MBart-50 (Multilingual BART by Facebook)** - Effective for complex language structures
- **NLLB-200 (No Language Left Behind)** - Advanced multilingual translation model

## 🏗 Installation
### **1️⃣ Clone the Repository**
```sh
git clone https://github.com/your-username/pdf-to-urdu.git
cd pdf-to-urdu
```

### **2️⃣ Create a Virtual Environment (Optional but Recommended)**
```sh
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate    # On Windows
```

### **3️⃣ Install Dependencies**
```sh
pip install -r requirements.txt
```

## 🔄 Usage
### **Run the Application**
```sh
streamlit run app.py
```

### **Steps to Translate a PDF**
1. Open the web app.
2. Upload a **PDF file**.
3. Click **Translate** to process the document.
4. Download the **translated document** in Urdu.

## 🖼️ Screenshot
*(Add a screenshot of your Streamlit UI for better understanding)*

## 🔗 Future Enhancements
- ✅ Support for multiple languages
- ✅ Optimize translation API usage to reduce cost
- ✅ Enable PDF reformatting to match original document styling
- ✅ Add OCR support for scanned PDFs
- ✅ Integrate more AI-based translation models for accuracy

## 🤝 Contributing
Contributions are welcome! Feel free to fork this repo and submit a pull request.

---
📩 **Developed by:** Anwar Shaik | [LinkedIn](https://www.linkedin.com/in/anwar-sk-86b631201) | [GitHub](https://github.com/minion536)

