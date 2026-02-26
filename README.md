# Sentiment Analysis API: NLP & Deployment

## Project Motivation
This repository demonstrates the deployment phase of the machine learning lifecycle. It was developed to showcase proficiency in Natural Language Processing (NLP) and software engineering by wrapping an analytical model in a RESTful API—a critical skill for translating academic models into scalable, real-world applications.

## Methodology
The objective is to expose a text-analysis model via an API endpoint that evaluates the linguistic polarity of unstructured text data.
1. **Lexical Analysis:** Utilizing the `TextBlob` library to perform lexicon-based sentiment scoring, mapping text to a mathematical polarity scale from -1.0 (highly negative) to 1.0 (highly positive).
2. **API Architecture:** Implementing **FastAPI** to construct a high-performance web server capable of handling POST requests.
3. **Data Validation:** Using `pydantic` models to enforce strict type-hinting and request payload validation, ensuring robust API interactions.

## Technical Implementation
* **Language:** Python
* **Core Frameworks:** `FastAPI`, `Uvicorn` (ASGI Server)
* **NLP Library:** `TextBlob`
* **Architecture:** Microservice design separating the NLP logic (`src/analyzer.py`) from the routing and server configuration (`main.py`).

## CI/CD & Deployment
This API is actively deployed on a cloud environment. It utilizes a Continuous Deployment (CD) pipeline integrated directly with GitHub. Any commits pushed to the `main` branch automatically trigger a server rebuild and dependency installation on **Render**, ensuring the live endpoint is always running the latest model architecture.

## Future Work & Limitations
To advance this service, future iterations will explore:
* Upgrading the lexicon-based model to a transformer-based architecture (e.g., **BERT**) for deeper contextual understanding.
* Containerizing the application using **Docker** for seamless, environment-agnostic deployment.
* Adding automated unit tests using `pytest` to establish a robust CI/CD pipeline.

## Replication Instructions
To run this API locally:
```bash
git clone [https://github.com/Aquib-Aadee/sentiment-analysis-api.git](https://github.com/Aquib-Aadee/sentiment-analysis-api.git)
cd sentiment-analysis-api
pip install -r requirements.txt
python main.py