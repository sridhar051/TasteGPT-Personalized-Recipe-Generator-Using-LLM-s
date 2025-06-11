# TasteGPT: Personalized Recipe Generator using LLMs

This repository contains a Jupyter notebook demonstrating how to build a personalized recipe generator powered by Large Language Models (LLMs). The notebook walks through setting up dependencies, connecting to APIs, and evaluating generated recipes.

## Getting Started

1. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

2. **Run the notebook**

   Open `LLM_Sridhar_Kandi.ipynb` in Jupyter or Google Colab and execute the cells step by step. The notebook downloads models, processes user preferences, and generates recipes using OpenAI and other LLM-powered tools.

## Project Structure

- `LLM_Sridhar_Kandi.ipynb` – main notebook containing the code and explanations.
- `requirements.txt` – list of Python packages needed to run the notebook.
- `app.py` – optional Streamlit application for quick deployment.

## Deployment

You can deploy a simple web interface using **Streamlit**. First set your OpenAI API key and then launch the app:

```bash
export OPENAI_API_KEY="YOUR-KEY"
streamlit run app.py
```

The app prompts you for ingredients or a dish name and generates a recipe using OpenAI's API.

## Notes

The notebook was developed in Google Colab and may prompt to install additional packages during execution. Ensure that you have access to the necessary API keys (for example, OpenAI) if required by the cells.

Feel free to adapt the code for your own recipe ideas or integrate it into a larger application.
