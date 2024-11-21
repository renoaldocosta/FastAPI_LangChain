---
noteId: "cda86c60a82811efa557f9dca5bcd96a"
tags: []

---

# FastAPI_LangChain

---

# LLM API with FastAPI

## Table of Contents
- [FastAPI\_LangChain](#fastapi_langchain)
- [LLM API with FastAPI](#llm-api-with-fastapi)
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Features](#features)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Configuration](#configuration)
  - [Running the Application](#running-the-application)
  - [API Endpoints](#api-endpoints)
    - [GET `/llm_routes`](#get-llm_routes)
    - [POST `/llm_routes/fake_llm`](#post-llm_routesfake_llm)
    - [POST `/llm_routes/translate_huggingface`](#post-llm_routestranslate_huggingface)
    - [POST `/llm_routes/translate`](#post-llm_routestranslate)
  - [Project Structure](#project-structure)
  - [Dependencies](#dependencies)
  - [Contributing](#contributing)
  - [License](#license)

## Introduction

This project is a **FastAPI** application that provides an API for interacting with various Language Learning Models (LLMs). It integrates with **LangChain**, **Hugging Face**, and **OpenAI** to offer functionalities such as text translation and response generation using both fake and real LLMs.

## Features

- **Fake LLM**: Simulates responses based on predefined prompts.
- **Hugging Face Integration**: Translates text from English to German using Hugging Face's `Helsinki-NLP/opus-mt-en-de` model.
- **OpenAI Integration**: Translates text from English to French using OpenAI's GPT-3.5-turbo model.
- **Modular Routes**: Organized API routes for scalability and maintainability.
- **Environment Configuration**: Secure handling of API keys using environment variables.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- **Python 3.8+**: Make sure Python is installed on your system. You can download it from [here](https://www.python.org/downloads/).
- **Git**: To clone the repository. Download from [here](https://git-scm.com/downloads).
- **API Keys**:
  - **Hugging Face API Token**: Sign up at [Hugging Face](https://huggingface.co/) to obtain your API token.
  - **OpenAI API Key**: Sign up at [OpenAI](https://platform.openai.com/signup) to obtain your API key.

## Installation

Follow these steps to set up the project locally:

1. **Clone the Repository**

   ```bash
   git clone https://github.com/renoaldocosta/llm-api-fastapi.git
   cd llm-api-fastapi
   ```

2. **Create a Virtual Environment**

   It's recommended to use a virtual environment to manage dependencies.

   ```bash
   python3 -m venv venv
   ```

3. **Activate the Virtual Environment**

   - **On macOS/Linux:**

     ```bash
     source venv/bin/activate
     ```

   - **On Windows:**

     ```bash
     venv\Scripts\activate
     ```

4. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

## Configuration

The application uses environment variables to securely manage API keys. Follow the steps below to configure them:

1. **Create a `.env` File**

   In the root directory of the project, create a file named `.env`.

   ```bash
   touch .env
   ```

2. **Add the Following Variables to `.env`**

   ```env
   HUGGINGFACEHUB_API_TOKEN=your_huggingface_api_token_here
   OPENAI_API_KEY=your_openai_api_key_here
   ```

   Replace `your_huggingface_api_token_here` and `your_openai_api_key_here` with your actual API tokens.

## Running the Application

Start the FastAPI server using **Uvicorn**:

```bash
uvicorn main:app --reload
```

- **`main`**: Refers to the `main.py` file.
- **`app`**: The FastAPI instance in `main.py`.
- **`--reload`**: Enables auto-reloading on code changes (useful for development).

The server will start at `http://127.0.0.1:8000/`.

## API Endpoints

Once the server is running, you can access the interactive API documentation at `http://127.0.0.1:8000/docs`.

### GET `/llm_routes`

**Description**: Root endpoint for the LLM API.

**Response**:

```json
{
  "message": "This is an API for LLMs"
}
```

### POST `/llm_routes/fake_llm`

**Description**: Generates a response using a fake LLM based on the provided prompt.

**Request Body**:

```json
{
  "prompt": "your_prompt_here"
}
```

**Response**:

```json
{
  "response": "Generated response based on the prompt."
}
```

**Example**:

```bash
curl -X POST "http://127.0.0.1:8000/llm_routes/fake_llm" -H "Content-Type: application/json" -d '{"prompt": "hello"}'
```

**Response**:

```json
{
  "response": "Hi there!"
}
```

### POST `/llm_routes/translate_huggingface`

**Description**: Translates text from English to German using Hugging Face's `Helsinki-NLP/opus-mt-en-de` model.

**Request Body**:

```json
{
  "text": "Your text to translate here."
}
```

**Response**:

```json
{
  "text_translated": "Translated text in German."
}
```

**Example**:

```bash
curl -X POST "http://127.0.0.1:8000/llm_routes/translate_huggingface" -H "Content-Type: application/json" -d '{"text": "Hello, how are you?"}'
```

**Response**:

```json
{
  "text_translated": "Hallo, wie geht es dir?"
}
```

### POST `/llm_routes/translate`

**Description**: Translates text from English to French using OpenAI's GPT-3.5-turbo model.

**Request Body**:

```json
{
  "text": "Your text to translate here."
}
```

**Response**:

```json
{
  "text_translated": "Translated text in French."
}
```

**Example**:

```bash
curl -X POST "http://127.0.0.1:8000/llm_routes/translate" -H "Content-Type: application/json" -d '{"text": "Good morning!"}'
```

**Response**:

```json
{
  "text_translated": "Bonjour!"
}
```

## Project Structure

```
.
├── .gitignore
├── README.md
├── main.py
├── Parte2
│   └── routes
│       └── llms.py
└── requirements.txt
```

- **`.gitignore`**: Specifies intentionally untracked files to ignore.
- **`README.md`**: Project documentation (this file).
- **`main.py`**: Entry point of the FastAPI application.
- **`Parte2/routes/llms.py`**: Contains the API routes related to LLMs.
- **`requirements.txt`**: Lists all Python dependencies.

## Dependencies

The project relies on the following Python packages:

- **fastapi**: FastAPI framework for building APIs.
- **uvicorn**: ASGI server implementation for serving FastAPI apps.
- **langchain**: Framework for building applications with language models.
- **langchain_community**: Community extensions for LangChain.
- **langchain-openai**: OpenAI integrations for LangChain.
- **python-dotenv**: Loads environment variables from a `.env` file.
- **huggingface_hub**: Interface to interact with Hugging Face models.
- **langchain-huggingface**: Hugging Face integrations for LangChain.

These dependencies are listed in `requirements.txt` and can be installed using:

```bash
pip install -r requirements.txt
```

## Contributing

Contributions are welcome! Please follow these steps:

1. **Fork the Repository**

2. **Create a New Branch**

   ```bash
   git checkout -b feature/YourFeature
   ```

3. **Make Your Changes**

4. **Commit Your Changes**

   ```bash
   git commit -m "Add some feature"
   ```

5. **Push to the Branch**

   ```bash
   git push origin feature/YourFeature
   ```

6. **Open a Pull Request**

## License

This project is licensed under the [MIT License](LICENSE).

---

**Note**: Ensure that your `.env` file is not committed to version control to keep your API keys secure. The `.gitignore` file is configured to ignore the `.env` file by default.