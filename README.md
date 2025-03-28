# AI_RECIPIE
# AI-Powered Recipe Explorer

## Overview
AI-Powered Recipe Explorer is a smart recipe suggestion app that leverages the Spoonacular API to fetch recipes based on ingredients you have on hand. Simply enter ingredients, and the app will suggest delicious recipes you can cook right away!

## Features
- Fetch recipes from the Spoonacular API
- User-friendly interface
- AI-driven recipe suggestions based on available ingredients
- Real-time ingredient input and recipe generation

## Prerequisites
Ensure you have the following installed on your system:
- Python 3.10 or higher
- pip (Python package installer)

## Installation
1. Clone this repository:
```
git clone <repository-url>
cd recipe-app
```

2. Create a virtual environment:
```
python -m venv venv
```

3. Activate the virtual environment:
- On Windows:
```
venv\Scripts\activate
```
- On macOS/Linux:
```
source venv/bin/activate
```

4. Install dependencies:
```
pip install -r requirements.txt
```

5. Add your API key in `app.py`:
```python
API_KEY = "YOUR_SPOONACULAR_API_KEY"
```

## Running the App
1. Start the Flask server:
```
python app.py
```

2. Open your web browser and go to:
```
http://127.0.0.1:5000
```

## Usage
1. Enter ingredients separated by commas (e.g., "chicken, garlic, tomato").
2. Click "Get Recipes" to view recipe suggestions.

## Troubleshooting
- Ensure your API key is valid.
- Verify the internet connection.
- Check dependencies in `requirements.txt`.



