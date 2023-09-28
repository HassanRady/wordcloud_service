import uvicorn
from fastapi import FastAPI, Request

from wordcloud_generator import get_wordcloud_from_text, get_wordcloud_from_frequencies


app = FastAPI()

@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.get("/health")
async def health():
    return {"status": "ok"}

@app.post("/wordcloud/text")
async def get_wordcloud(request: Request):
    request = await request.json()
    return {"output": get_wordcloud_from_text(request['input'])}

@app.post("/wordcloud/frequency")
async def get_wordcloud_from_frequencies(request: Request):
    request = await request.json()
    return {"output": get_wordcloud_from_frequencies(request['input'])}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001)