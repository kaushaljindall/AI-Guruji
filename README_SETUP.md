# AI Guruji System Setup

## System Architecture
- **Backend**: FastAPI (Python)
  - Port: `8000`
  - Location: `/backend`
  - Services: RAG (FAISS), LLM (Gemini/OpenAI), TTS, Slide Generation.
- **Frontend**: React + Vite + Tailwind CSS
  - Port: `5173`
  - Location: `/frontend`
  - Feature: Real-time 3D Avatar (React Three Fiber).

## 📋 Prerequisites
Ensure you have the following installed before starting:
1.  **Python 3.10+**
2.  **Node.js 18+**
3.  **FFmpeg**: CRITICAL for audio/video features (TTS, Slides).
    - **Automatic Install**: Run `install_ffmpeg.bat`.
    - **Manual Setup (Recommended)**: Wait for the next section if automatic fails.
    - *Verify with `ffmpeg -version`*
    - **See `MANUAL_FFMPEG_SETUP.md` for detailed instructions.**

## 🚀 Quick Start (Recommended)

**Option 1: Use Startup Scripts**
```bash
# Terminal 1: Start Backend
start_backend.bat

# Terminal 2: Start Frontend  
start_frontend.bat
```

**Option 2: Manual Start**

### 1. Start Backend
The backend handles PDF parsing, RAG context, and Lecture Script generation.

```bash
cd backend

# 1. Create & Activate Virtual Environment
python -m venv venv
# Windows:
venv\Scripts\activate
# Mac/Linux:
# source venv/bin/activate

# 2. Install Python Dependencies
pip install -r requirements.txt

# 3. Start the Server
uvicorn app.main:app --reload
```
*API Docs available at http://localhost:8000/docs*

### 2. Start Frontend
The frontend renders the 3D Classroom experience.

```bash
cd frontend

# 1. Install Node Dependencies
npm install

# 2. Start Dev Server
npm run dev
```
*App available at http://localhost:5173*

## 📁 File Structure
- `backend/app/main.py`: Entry point for FastAPI.
- `backend/app/services/llm_service.py`: Handles Gemini + OpenAI logic.
- `frontend/src/App.jsx`: Main routing & Processing UI using Ziva.
- `frontend/src/components/Show.jsx`: The Lecture Room (Slides + Avatar).
- `frontend/src/components/Ziva.jsx`: The 3D Avatar Component.
