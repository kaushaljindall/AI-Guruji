import os
import sys

# Get the project root (where this script is)
project_root = os.path.dirname(os.path.abspath(__file__))
backend_dir = os.path.join(project_root, 'backend')

# Change to backend directory for proper .env loading
os.chdir(backend_dir)

# Add backend to Python path so 'app' module can be imported
sys.path.insert(0, backend_dir)

print("=" * 60)
print("AI GURUJI DIAGNOSTIC REPORT")
print("=" * 60)

# 1. Check Environment Variables
print("\n[1] API Keys Configuration:")
from dotenv import load_dotenv
load_dotenv()

gemini_key = os.getenv("GEMINI_API_KEY", "")
openai_key = os.getenv("OPENAI_API_KEY", "")

if gemini_key and len(gemini_key) > 20:
    print(f"   ✅ GEMINI_API_KEY found ({len(gemini_key)} chars)")
else:
    print(f"   ❌ GEMINI_API_KEY missing or invalid")

if openai_key and len(openai_key) > 20:
    print(f"   ✅ OPENAI_API_KEY found ({len(openai_key)} chars)")
else:
    print(f"   ⚠️  OPENAI_API_KEY missing (optional fallback)")

# 2. Check RAG Index
print("\n[2] RAG Vector Store:")
try:
    from app.services.rag_service import rag_service
    print(f"   ✅ RAG Service loaded")
    print(f"   📊 Index vectors: {rag_service.index.ntotal}")
    print(f"   📄 Chunks stored: {len(rag_service.chunks)}")
    
    if rag_service.index.ntotal > 0:
        test_results = rag_service.search("overview", k=2)
        print(f"   🔍 Search test: Found {len(test_results)} results")
    else:
        print(f"   ⚠️  Index is empty - please upload a PDF first")
except Exception as e:
    print(f"   ❌ RAG Service error: {e}")

# 3. Check LLM Service
print("\n[3] LLM Service:")
try:
    from app.services.llm_service import llm_service
    print(f"   ✅ LLM Service initialized")
    print(f"   🤖 Provider: {llm_service.provider}")
except Exception as e:
    print(f"   ❌ LLM Service error: {e}")

# 4. Test Generation
print("\n[4] Test Lecture Generation:")
if rag_service.index.ntotal > 0:
    try:
        from app.core.prompts import TEACHER_SYSTEM_PROMPT
        context = "\n".join(rag_service.search("test", k=3))
        print(f"   📝 Context length: {len(context)} chars")
        
        print(f"   🔄 Attempting LLM call...")
        result = llm_service.generate_lecture_content(TEACHER_SYSTEM_PROMPT, context[:1000])
        print(f"   ✅ Generation SUCCESS!")
        print(f"   📊 Generated slides: {len(result.get('slides', []))}")
    except Exception as e:
        print(f"   ❌ Generation FAILED: {e}")
        import traceback
        traceback.print_exc()
else:
    print(f"   ⏭️  Skipped (no data in index)")

print("\n" + "=" * 60)
print("DIAGNOSTIC COMPLETE")
print("=" * 60)
