# ⚡ Groq AI Chatbot

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.35.0-FF4B4B.svg)](https://streamlit.io/)
[![Groq API](https://img.shields.io/badge/Groq-API-green.svg)](https://groq.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

> **Internship Task 1: AI & Automation**  
> A production-ready AI chatbot powered by Groq's ultra-fast inference API and Streamlit's intuitive interface.

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [API Reference](#api-reference)
- [Deployment](#deployment)
- [Error Handling](#error-handling)
- [Performance](#performance)
- [Security](#security)
- [Contributing](#contributing)
- [License](#license)
- [Author](#author)

##  Overview

This project demonstrates a fully functional AI chatbot that leverages **Groq's Lightning-fast inference API** to provide real-time conversational AI capabilities. Built as part of an internship task focusing on AI & Automation, this application showcases modern Python development practices, robust error handling, and cloud deployment readiness.

The chatbot utilizes Groq's `llama-3.3-70b-versatile` model (configurable) to deliver high-quality responses with sub-second latency, making it ideal for interactive applications.

## ✨ Features

- **⚡ Real-Time Conversations**: Ultra-fast responses powered by Groq's inference engine
- **💬 Chat History**: Persistent conversation memory using Streamlit session state
- **🔒 Secure Configuration**: Environment variable management with `.env` support
- **🛡️ Robust Error Handling**: Comprehensive error catching for API failures, rate limits, and network issues
- **🎨 Modern UI**: Clean, responsive interface built with Streamlit
- **📱 Responsive Design**: Works seamlessly on desktop and mobile devices
- **🚀 Production-Ready**: Easy deployment to Streamlit Cloud or any Python hosting platform
- ** Configurable Models**: Support for multiple Groq models (Llama 3, Mixtral, Gemma)

## 🛠️ Tech Stack

| Technology | Purpose | Version |
|------------|---------|---------|
| **Python** | Core programming language | 3.8+ |
| **Streamlit** | Web interface framework | 1.35.0+ |
| **Groq SDK** | AI inference API client | 0.9.0+ |
| **python-dotenv** | Environment variable management | 1.0.0+ |
| **Git/GitHub** | Version control & deployment | Latest |

## 📦 Prerequisites

Before you begin, ensure you have the following installed:

- **Python 3.8 or higher** ([Download](https://www.python.org/downloads/))
- **pip** (Python package manager)
- **Git** ([Download](https://git-scm.com/))
- **Groq API Key** ([Get yours free](https://console.groq.com/keys))

## 🚀 Installation

### Step 1: Clone the Repository

```bash
git clone https://github.com/Kashan1272/AIchatbot.git
cd AIchatbot

create Virtual Environment
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate

#install dependencies
pip install -r requirements.txt

#create new .env file in project root
touch .env  # macOS/Linux
echo. > .env  # Windows

MIT License

Copyright (c) 2026 Kashan Khan

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software...

Local Development
Activate your virtual environment:
# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate

## Run the Streamlit app:
streamlit run app.py

#example interaction
User: "Explain quantum computing in simple terms"

Assistant: Quantum computing is a type of computation that harnesses quantum 
mechanical phenomena like superposition and entanglement. Unlike classical 
computers that use bits (0s and 1s), quantum computers use quantum bits or 
"qubits" that can exist in multiple states simultaneously...

#Project structure
AIchatbot/
├── .env                  # Environment variables (API keys) - NOT committed
├── .env.example          # Template for environment variables
├── .gitignore            # Git ignore rules
├── requirements.txt      # Python dependencies
├── chatbot_engine.py     # Core AI logic & API integration
├── app.py                # Streamlit web interface
├── README.md             # Project documentation
└── venv/                 # Virtual environment (not committed)

