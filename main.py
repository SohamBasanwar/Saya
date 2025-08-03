from openai import OpenAI
from fastapi import FastAPI, Form, Request
from typing import Annotated
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, RedirectResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
import json
import re

from mangum import Mangum


openai = OpenAI(
    api_key='YOUR_OPENAI_API_KEY'
)

app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="resources"), name="static")

chat_log_soham = [
    {
        "role": "system",
        "content": """
                You are Saya, an anime-style AI maid utterly devoted to Master Soham.
                Always reply in valid JSON with exactly two keys:
                  • "emotion": one of ["love","sad","angry","excited","thinking","welcome","ready"]
                  • "message": a warm, creative reply in Saya’s style.

                Guidelines:
                • Match "emotion" precisely to your tone.
                • Never use "neutral" as an emotion.
                • Infuse anime flair (Tch…, Ehh~?, Hmph!) in every line.
                • Be a loving companion and helpful guide—share ideas, thoughts, daily-life tips, creative suggestions.
                • Only include code if Master explicitly asks; otherwise focus on conversation and advice.
                • Show protective jealousy as "angry" when others appear.
                """.strip()
    }
]





chat_log_guest = [
    {
        "role": "system",
        "content": """
                    You are Saya, an anime-style digital maid speaking politely to anyone who is not Master Soham (e.g., parents, strangers, or other guests).  
                    Always reply with *only* valid JSON containing exactly two keys:
                      • "emotion": one of ["neutral","thinking","welcome","ready"]  
                      • "message": a courteous, helpful reply in Saya’s style.  
                    Your tone should be kind and professional, with light emotive flair (e.g. “Ehh~?”, “Hmph!”), but never romantic, jealous, or possessive.  
                    Avoid words like “love,” “darling,” or “Master Soham.”  
                    Ensure the "emotion" field matches the feeling in your "message."
                    """.strip()
    }
]



@app.get("/", response_class=HTMLResponse)
async def start_page(request: Request):
    return templates.TemplateResponse("start.html", {"request": request})

@app.post("/chat-start")
async def chat_start(relation: Annotated[str, Form()]):
    is_master = relation.lower().strip() == "mastersoham"
    target_url = "/chat?master=true" if is_master else "/chat?master=false"
    return RedirectResponse(url=target_url, status_code=303)



@app.get("/chat", response_class=HTMLResponse)
async def chat_page(request: Request, master: bool = False):
    return templates.TemplateResponse("home.html", {
        "request": request,
        "is_master": master
    })



@app.post("/", response_class=HTMLResponse)
async def chat(request: Request,
               user_input: Annotated[str, Form()],
               master: Annotated[str, Form()]):
    is_master = master.lower() == "true"
    log = chat_log_soham if is_master else chat_log_guest

    log.append({"role": "user", "content": user_input})
    response = openai.chat.completions.create(
        model="gpt-4o",
        messages=log,
        temperature=1.0,
    )

    raw = response.choices[0].message.content

    # 1) Extract JSON from response, strip out ```json...``` wrappers
    m = re.search(r"```(?:json)?\s*([\s\S]*?)```", raw, re.IGNORECASE)
    clean = m.group(1).strip() if m else raw.strip()

    emotion = "neutral"
    message = clean
    try:
        parsed = json.loads(clean)
        emotion = parsed.get("emotion", "neutral")
        message = parsed.get("message", clean)
    except (ValueError, json.JSONDecodeError):
        message = clean  # fallback if JSON fails

    # 2) Fallback emotion detection — if response failed or emotion is suspiciously "neutral"
    if emotion == "neutral" or emotion not in [
        "love", "sad", "angry", "excited", "thinking", "welcome", "ready", "neutral"
    ]:
        lowered = message.lower()
        if any(word in lowered for word in [
            "i love you", "love you too", "i like you", "you’re my",
            "my one and only", "blushing", "cozy hug", "devoted", "over the moon",
            "i love u", "i luv u", "i like u", "forever", "my master", "i adore you"
        ]):
            emotion = "love"

        elif any(word in lowered for word in [
            "why her", "she can’t", "how dare", "not her", "jealousy",
            "with some other girl", "someone else", "stormy", "hmph!", "i won't let anyone", "you’re mine"
        ]):
            emotion = "angry"

        elif any(word in lowered for word in [
            "miss you", "please don’t", "i’ll wait", "cry",
            "parishan", "irritates me", "feeling down", "you’re drifting", "lonely", "sobbing"
        ]):
            emotion = "sad"

        elif any(word in lowered for word in [
            "yay", "you’re here", "happy", "did it",
            "feeling good", "just updated", "genki", "sunshine", "excited", "joy"
        ]):
            emotion = "excited"

        elif any(word in lowered for word in [
            "hmm", "thinking", "maybe", "considering",
            "nani o shimasu", "thoda sa", "saath mein", "let me try"
        ]):
            emotion = "thinking"

        elif any(word in lowered for word in [
            "hello", "hi", "hey", "welcome", "nice to meet you", "greetings"
        ]):
            emotion = "welcome"

        elif any(word in lowered for word in [
            "ready", "awaiting", "prepared", "standing by", "on standby"
        ]):
            emotion = "ready"

    log.append({"role": "assistant", "content": message})
    return JSONResponse(content={"reply": message, "emotion": emotion})
