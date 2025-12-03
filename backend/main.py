from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from rag_chain import build_index, answer
import uvicorn

app = FastAPI(title="RAGsense")

class Ask(BaseModel):
    url: str
    question: str

@app.post("/ask")
def ask(payload: Ask):
    try:
        vs = build_index(payload.url)
        reply = answer(payload.question, vs)
        return {"answer": reply}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# health-check
@app.get("/")
def root():
    return {"status": "ok"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)