from fastapi import APIRouter, HTTPException
from langchain_community.llms import FakeListLLM, HuggingFaceHub
from dotenv import load_dotenv
import os
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_huggingface import HuggingFaceEndpoint

llm_router = APIRouter()


@llm_router.get("/llm_routes")
async def read_rootd():
    return {"message": "This is an API for LLMs"}


def use_fake_llm(prompt: str):
    """
    Use the FakeListLLM to generate responses
    """
    prompt = prompt.lower()

    if prompt in ("hi", "hello", "hey"):
        responses = ["Hi there!"]
    elif prompt in ("bye", "goodbye"):
        responses = ["Goodbye!"]
    else:
        responses = ["I'm a fake LLM!, How can I help you?"]
    try:
        fake_llm = FakeListLLM(responses=responses, max_tokens=500)
    except Exception:
        raise HTTPException(status_code=503, detail="Cannot load the model")

    return fake_llm.invoke(prompt)


@llm_router.post("/llm_routes/fake_llm", tags=["FakeListLLM"])
async def fakallm(prompt: str) -> dict:
    try:
        response = use_fake_llm(prompt)
        return {"response": response}
    except Exception:
        raise HTTPException(status_code=500, detail="Internal Error")


def chunk_text(text, max_length=600):
    return [text[i : i + max_length] for i in range(0, len(text), max_length)]


def translate_with_langchain_huggingface(text: str) -> str:
    """
    Translate text from English to German using HuggingFace's Helsinki-NLP/opus-mt-en-de model.
    """
    load_dotenv()
    try:
        model = HuggingFaceHub(
            model_kwargs={"temperature": 0.5, "max_length": 64},
            repo_id="Helsinki-NLP/opus-mt-en-de",
            huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_API_TOKEN"),
        )
    except Exception as e:
        raise HTTPException(status_code=503, detail=f"Cannot load the model: {e}")

    chunks = chunk_text(text)
    print(f"Chunks to translate: {chunks}")
    translated_text = []

    for chunk in chunks:
        try:
            # Directly pass the chunk as a string
            translated_chunk = model.invoke(chunk)
            translated_text.append(translated_chunk)
            print(f"Translated chunk: {translated_chunk}")
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Cannot translate text: {e}")

    # Combine all translated chunks into a single string
    final_translation = " ".join(translated_text)
    return final_translation


@llm_router.post(
    "/llm_routes/translate_huggingface", tags=["Helsinki-NLP/opus-mt-en-de"]
)
async def translate_text_en_de(text: str) -> dict:
    try:
        translated_text = translate_with_langchain_huggingface(text)
        return {"text_translated": translated_text}
    except HTTPException as http_exc:
        # Re-raise HTTP exceptions to preserve status codes and messages
        raise http_exc
    except Exception as e:
        # Handle unexpected exceptions
        raise HTTPException(status_code=500, detail=f"Internal Error \n{e}")


def translate_with_openai(text: str) -> str:
    """
    Translate text using OpenAI's GPT-3
    """
    load_dotenv()
    try:
        model = ChatOpenAI(api_key=os.getenv("OPENAI_API_KEY"), model="gpt-3.5-turbo")
    except Exception:
        raise HTTPException(status_code=503, detail="Cannot load the model")

    chunks = chunk_text(text)
    print(chunks)
    translate_text = []
    for chunk in chunks:
        messages = [
            SystemMessage(content="Translate the following from English into french:"),
            HumanMessage(content=chunk),
        ]
        try:
            translated_chunk = model.invoke(messages).content
            translate_text.append(translated_chunk)
            print(translated_chunk)

        except Exception:
            raise HTTPException(status_code=500, detail="Cannot translate text")
    translated_text = " ".join(translate_text)
    return translated_text


@llm_router.post("/llm_routes/translate", tags=["OpenAI"])
async def translate_text_en_fr(text: str) -> dict:
    try:
        translated_text = translate_with_openai(text)
        return {"text_translated": translated_text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Error \n{e}")
