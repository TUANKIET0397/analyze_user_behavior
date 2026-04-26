# Project Name: Analyze User Behavior

# Description

This project is designed to analyze user behavior through machine learning algorithms and provide insights for better decision-making. The project is divided into two parts:

- Front-End: A React application built with Vite, which interacts with the back-end API to visualize and present data.
- Back-End: Provides the API to process data, perform analysis, and return results.

## 🎯 Front-End (Vite)

### 📋 Description

The front-end application is built using **React** and communicates with the back-end API. The user interface is designed to visualize data and insights, including user interaction patterns.

This is a dashboard page that shows product insights based on user data.

### 🔧 Installation

1. Clone the repository

```bash
git clone https://github.com/TUANKIET0397/analyze_user_behavior.git

cd analyze_user_behavior
cd front-end
```

2. Install dependencies

```bash
npm install
```

### ⚙️ Configuration

- Create a `.env` file in the front-end root (the port must match the backend server)

```bash
VITE_API_BACKEND = http://127.0.0.1:8001
```

- Running the Front-End

```bash
npm run dev
```

The application will be running at http://localhost:5173

## 📃 Back-End

### 📋 Description

The back-end application is built with **FastAPI**, responsible for receiving requests from the front-end, processing them using machine learning algorithms, and returning the results.

### 🔧 Installation

1. Clone the repository

```bash
git clone https://github.com/TUANKIET0397/analyze_user_behavior.git

cd analyze_user_behavior
cd back-end
```

2. Install dependencies

```bash
pip install -r requirements.txt
```

### ⚙️ Configuration

To start the back-end application, using FastAPI:

```bash
python -m uvicorn app.main:app --reload --port 8001
```

The back-end server will be running at http://localhost:8001
