# AI-PORTFOLIO-GENERATOR
An elite open-source portfolio engineering engine powered by FastAPI and Gemini 2.5 Flash. Automatically extracts, normalizes, and architecturally translates raw GitHub metadata and repository assets into structured, production-grade resume and portfolio data blocks.




# Folio AI Master Engine 🚀

Folio AI Master Engine is a high-performance backend processing engine built with **FastAPI** and powered by the **Google Gemini 2.5 Flash** model. It programmatically transforms raw, live GitHub repository footprints, developer metadata, and media assets into structured, industry-ready engineering portfolio profiles. 

By analyzing real codebase distributions and parsing README files for media artifacts, the engine generates hyper-realistic technical resumes, structured project timelines, and verified portfolios using formal JSON schemas.

---

## ✨ Features

- **Live GitHub Metadata Scraper:** Dynamically polls the GitHub API for raw repository payloads, filtering forks to focus exclusively on original development work.
- **Automated Media Parsing:** Uses regular expressions to scan remote `README.md` layouts, automatically detecting and extracting live video links (`.mp4`, `.gif`, `.mov`, etc.) or embedded YouTube links.
- **Structured Gemini Orchestration:** Leverages the latest `google-genai` SDK using `gemini-2.5-flash` with strict JSON schema configuration (`response_schema`) to ensure guaranteed, type-safe portfolio data output.
- **Professional Resume Architecture:** Translates open-source software contributions into sophisticated, industry-grade corporate experience records without artificial data fabrication.
- **Robust Static Mounting:** Serves frontend applications seamlessly via direct FastAPI static folder mapping.

---

## 🛠️ Tech Stack

- **Backend Framework:** FastAPI (Python 3.10+)
- **AI/LLM Engine:** Google GenAI SDK (`gemini-2.5-flash`)
- **Data Validation & Schemas:** Pydantic v2
- **Environment Management:** Python Dotenv
- **Asynchronous HTTP Client:** Requests

---

## 📂 Project Structure

```text
├── app/
│   ├── main.py         
│   └── .env          

├── static/
│   └── index.html      
├── requirements.txt     
└── README.md           

 __VIDEO DESCRIPTION__


https://github.com/user-attachments/assets/0c866a28-5218-4a0f-b55c-6e3f0aa969a5


**IMAGES OF THE PORTFOLIO**




<img width="1612" height="815" alt="image" src="https://github.com/user-attachments/assets/33902c56-849d-40a2-9252-3db8607dcf17" />


<img width="1822" height="822" alt="image" src="https://github.com/user-attachments/assets/d0addea9-ad84-4574-94e8-fe3021a41592" />

<img width="1788" height="820" alt="image" src="https://github.com/user-attachments/assets/b60eabab-84df-4bf8-9383-3e6303e66a43" />

**
**Create and activate a virtual environment****
  -->python -m venv venv
  -->venv\Scripts\activate

  
****Install the dependencies:****
  -->pip install -r requirements.txt

**Set up your environment variables:**
Create a .env file in the root directory:
  --> GEMINI_API_KEY="PASTE_YOUR_GEMINI_API_KEY"
**Running the Server**
-->  python -m uvicorn main:app --reload

**AUTHOR**
**SHREENITHI**




