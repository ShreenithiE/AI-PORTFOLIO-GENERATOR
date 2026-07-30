import os
import json
import base64
import re
import requests
from fastapi import FastAPI, HTTPException, Form
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse, RedirectResponse
from pydantic import BaseModel, Field
from google import genai
from google.genai import types
from dotenv import load_dotenv

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
load_dotenv(os.path.join(BASE_DIR, ".env"))

STATIC_DIR = os.path.join(BASE_DIR, "static")

app = FastAPI(title="Folio AI Master Engine")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ProjectItem(BaseModel):
    title: str = Field(description="Project name matching the real GitHub repository name")
    description: str = Field(description="Detailed engineering bullet point showing tech milestones achieved.")
    tech_used: list[str] = Field(description="3-4 technologies used.")
    has_preview: bool = Field(description="True if the project has a detected demo video, GIF, or preview asset link, False otherwise.")
    preview_url: str = Field(description="The extracted raw video url, GIF url, or media link found inside the README. Leave blank if none.")

class ExperienceItem(BaseModel):
    company: str = Field(description="The open-source project or repository context acting as the working environment")
    role: str = Field(description="Engineering title like 'Lead Contributor', 'Open Source Developer', or 'Core Architect'")
    duration: str = Field(description="Estimated timeline based on GitHub project updates")
    details: str = Field(description="Strictly realistic highlights detailing architectural decisions, feature builds, or bug resolutions.")

class DynamicPortfolio(BaseModel):
    full_name: str = Field(description="Candidate's name")
    headline: str = Field(description="Advanced clean engineering title")
    bio: str = Field(description="A 3-sentence professional bio based strictly on the target profile and real code footprints.")
    skills: list[str] = Field(description="List of core tools and programming languages parsed from GitHub languages.")
    career_history: list[ExperienceItem] = Field(description="Chronology of professional-grade experiences modeled directly out of your real GitHub development work.")
    inferred_projects: list[ProjectItem] = Field(description="Top open-source repositories enhanced into professional summaries.")

def extract_readme_media(username: str, repo_name: str):
    """Parses the remote repository README.md content to extract explicit video or GIF assets."""
    try:
        url = f"https://api.github.com/repos/{username}/{repo_name}/readme"
        headers = {"User-Agent": "Folio-Engine-App"}
        response = requests.get(url, headers=headers, timeout=5)
        if response.status_code == 200:
            content_b64 = response.json().get("content", "")
            readme_text = base64.b64decode(content_b64).decode("utf-8", errors="ignore")
            
            video_matches = re.findall(r'(?:src=|!\[.*?\]\()([^"\'>\s)]+\.(?:mp4|webm|gif|mov))', readme_text, re.IGNORECASE)
            if video_matches:
                return True, video_matches[0]
                
            yt_match = re.search(r'(?:youtube\.com/watch\?v=|youtu\.be/)([a-zA-Z0-9_-]+)', readme_text)
            if yt_match:
                return True, f"https://www.youtube.com/embed/{yt_match.group(1)}"
    except Exception:
        pass
    return False, ""

def fetch_live_github(username: str):
    try:
        url = f"https://api.github.com/users/{username}/repos?sort=updated&per_page=5"
        headers = {"User-Agent": "Folio-Engine-App"}
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code == 200:
            return response.json()
    except Exception:
        pass
    return []

@app.post("/api/sync-profile", response_model=DynamicPortfolio)
async def sync_profile(
    fullname: str = Form(...),
    title: str = Form(""),  
    github_user: str = Form(...),
    linkedin_url: str = Form("")
):
    gemini_key = os.environ.get("GEMINI_API_KEY")
    
    if not gemini_key or gemini_key.startswith("PASTE_YOUR") or gemini_key == "AIzaSyYourActualKeyHere":
        gemini_key = "AQ.Ab8RN6LZybpFvlLAOF--rBpqLMnUvdXkSJ8Utz4COoqVVQPACg"

    if not gemini_key:
        raise HTTPException(status_code=500, detail="GEMINI_API_KEY configuration setup missing.")

    github_raw = fetch_live_github(github_user)
    github_context = []
    
    if isinstance(github_raw, list):
        for r in github_raw:
            if not r.get("fork"):
                name = r.get("name")
                has_media, media_url = extract_readme_media(github_user, name)
                github_context.append({
                    "name": name,
                    "description": r.get("description") or "Production repository context layout.",
                    "lang": r.get("language") or "Python/JavaScript",
                    "has_media": has_media,
                    "media_url": media_url
                })

    prompt = f"""
    You are an elite Technical Resume Architect and Portfolio Designer.
    Analyze the raw input components:
    - Declared Name: {fullname}
    - Declared Target Role: {title}
    - Real Live GitHub Repositories metadata with structural media parameters: {json.dumps(github_context)}
    - Provided LinkedIn Profile Link: {linkedin_url}
    
    CRITICAL INSTRUCTIONS:
    1. Populate fields matching the DynamicPortfolio JSON schema data layout.
    2. DO NOT fabricate fake companies. Translate their repository builds into professional experience blocks using 'Open Source Development / Project {github_user}' as the environment layout.
    3. If a repository has 'has_media' as true in the metadata, preserve that exact 'media_url' in the 'preview_url' property block and set 'has_preview' to true.
    """

    try:
        client = genai.Client(api_key=gemini_key)
        ai_res = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=prompt,
            config=types.GenerateContentConfig(
                response_mime_type="application/json",
                response_schema=DynamicPortfolio,
                temperature=0.2
            ),
        )
        return json.loads(ai_res.text)
    except Exception as e:
        print(f"CRITICAL ENGINE FAULT: {str(e)}")
        raise HTTPException(status_code=500, detail=f"AI Engine Runtime Failure: {str(e)}")

@app.get("/app")
@app.get("/app/")
async def redirect_old_path():
    return RedirectResponse(url="/")

@app.get("/")
async def serve_homepage():
    return FileResponse(os.path.join(STATIC_DIR, "index.html"))

app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")