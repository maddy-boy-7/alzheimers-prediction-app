# 🧠 Alzheimer's Prediction System — Streamlit App

A replica of [alzheimers-prediction.streamlit.app](https://alzheimers-prediction.streamlit.app) built with Python and Streamlit.

## 📁 Project Structure

```
streamlit_app/
├── streamlit_app.py          ← Main entry point
├── config.py                 ← All constants, categories, team info
├── train_model.py            ← Trains the Logistic Regression model
├── setup.py                  ← One-click setup (images + deps + model)
├── run_streamlit.bat         ← Double-click to launch the app
├── requirements.txt          ← Python dependencies
├── .streamlit/
│   ├── config.toml           ← Dark purple theme
│   └── secrets.toml          ← API keys (fill these in!)
├── assets/
│   └── css/styles.css        ← App stylesheet
│   └── images/               ← Background, banner, sidebar images
├── model/
│   └── alzheimer_model.pkl   ← Generated after running setup.py
└── streamlit_pages/
    ├── _home_page.py         ← Home / Introduction page
    ├── _predict_alzheimer.py ← ML Prediction page
    ├── _chat_page.py         ← AI ChatBot page
    ├── _latest_news.py       ← Latest Alzheimer's News page
    └── _team_members.py      ← Team Members page
```

## 🚀 Quick Start (Windows)

### Option A — Double-click launch
1. Double-click **`run_streamlit.bat`**
2. Wait for setup to complete
3. Browser opens automatically at **http://localhost:8501**

### Option B — Manual
```bash
cd streamlit_app
python setup.py          # First run only: copies images, installs deps, trains model
streamlit run streamlit_app.py
```

## 📋 Pages

| Page | Description |
|------|-------------|
| **Home** | Introduction to Alzheimer's Disease |
| **Predict Alzheimer's** | Enter patient data → get AI prediction (CN / LMCI / AD) |
| **ChatBot** | AI-powered Q&A about Alzheimer's |
| **Latest News** | Live news feed via NewsAPI |
| **Team Members** | Developer profiles with LinkedIn/GitHub links |

## 🔑 Optional API Keys

Edit `.streamlit/secrets.toml` to enable full features:

| Key | Feature | Where to get |
|-----|---------|--------------|
| `NEWS_API` | Live news articles | [newsapi.org](https://newsapi.org) (free) |
| `HF_GMAIL` / `HF_PASS` | Full AI ChatBot | [huggingface.co](https://huggingface.co) |

The app works without these keys — it falls back to sample articles and a built-in rule-based chatbot.

## 🤖 Model Details

- **Algorithm**: Logistic Regression (matching the original app)
- **Classes**: `CN` (Cognitively Normal) · `LMCI` (Late Mild Cognitive Impairment) · `AD` (Alzheimer's Disease)
- **Features**: Age, Education, MMSE score, Race, APOE Genotype, Ethnicity, APOE4 allele count, Gender, Imputed Genotype
- **Training data**: Replace `train_model.py` synthetic data with the real ADNI dataset for production accuracy
