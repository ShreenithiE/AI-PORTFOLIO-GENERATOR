**AI-PORTFOLIO-GENERATOR**



An elite open-source portfolio engineering engine powered by FastAPI and Gemini 2.5 Flash. Automatically extracts, normalizes, and architecturally translates raw GitHub metadata and repository assets into structured, production-grade resume and portfolio data blocks.

 **AI-PORTFOLIO-GENERATOR🚀**


 
AI-PORTFOLIO-GENERATOR is a high-performance backend processing engine built with FastAPI and powered by the Google Gemini 2.5 Flash model. It programmatically transforms raw, live GitHub repository footprints, developer metadata, and media assets into structured, industry-ready engineering portfolio profiles.

By analyzing real codebase distributions and parsing README files for media artifacts, the engine generates hyper-realistic technical resumes, structured project timelines, and verified portfolios using formal JSON schemas.

**✨ Features**



Live GitHub Metadata Scraper: Dynamically polls the GitHub API for raw repository payloads, filtering forks to focus exclusively on original development work.

Automated Media Parsing: Uses regular expressions to scan remote README.md layouts, automatically detecting and extracting live video links (.mp4, .gif, .mov, etc.) or embedded YouTube links.

Structured Gemini Orchestration: Leverages the latest google-genai SDK using gemini-2.5-flash with strict JSON schema configuration (response_schema) to ensure guaranteed, type-safe portfolio data output.

Professional Resume Architecture: Translates open-source software contributions into sophisticated, industry-grade corporate experience records without artificial data fabrication.

Robust Static Mounting: Serves frontend applications seamlessly via direct FastAPI static folder mapping.



**🛠️ Tech Stack**



Backend Framework: FastAPI (Python 3.10+)

AI/LLM Engine: Google GenAI SDK (gemini-2.5-flash)

Data Validation & Schemas: Pydantic v2

Environment Management: Python Dotenv

Asynchronous HTTP Client: Requests

**📂 Project Structure**




Plaintext
├── app/
│   ├── main.py         
│   └── .env          

├── static/
│   └── index.html      
├── requirements.txt     
└── README.md           
**📹 Video Description



https://github.com/user-attachments/assets/0c866a28-5218-4a0f-b55c-6e3f0aa969a5**

**🖼️ Images of the Portfolio**



🚀 Getting Started
**1. Create and Activate a Virtual Environment**


Bash
python -m venv venv
# On Windows:


venv\Scripts\activate
# On macOS/Linux:



source venv/bin/activate
**2. Install Dependencies**



Bash
pip install -r requirements.txt
**3. Set Up Environment Variables**



Create a .env file in the root directory:

Code snippet
GEMINI_API_KEY="PASTE_YOUR_GEMINI_API_KEY"
**4. Run the Server**


Bash
python -m uvicorn main:app --reload



**<img width="1612" height="815" alt="image" src="https://github.com/user-attachments/assets/e11a2032-dacf-4f1e-b716-bd335caa44aa" />**





**<img width="1598" height="841" alt="image" src="https://github.com/user-attachments/assets/44fcdd33-a014-4651-a447-9949755e4029" />**




**<img width="1822" height="822" alt="image" src="https://github.com/user-attachments/assets/3e333591-d848-4f1d-8aba-eeb6bab894cd" />**




**<img width="1788" height="820" alt="image" src="https://github.com/user-attachments/assets/eaa96bbf-fb71-4952-8649-3889516c33da" />**




**✍️ Author
SHREENITHI**
