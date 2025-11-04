from flask import Blueprint, render_template, current_app
from flask_login import login_required, current_user
import requests
from datetime import datetime
from flask import request, jsonify
from openai import OpenAI

views = Blueprint('views', __name__)

# Intro page route (unauthenticated)
@views.route('/')
def intro():
    return render_template("intro.html")

# Home dashboard route (authenticated)
@views.route('/home')
@login_required
def home():
    market_data = {
        "NIFTY_50": get_nse_index_data("NIFTY_50"),
        "BANK_NIFTY": get_nse_index_data("BANK_NIFTY"),
        "NIFTY_IT": get_nse_index_data("NIFTY_IT")
    }

    news_articles = fetch_stock_news()

    return render_template(
        "home.html",
        user=current_user,
        market_data=market_data,
        news_articles=news_articles,
        last_updated=datetime.now().strftime("%H:%M:%S")
    )

# User details route
@views.route('/user-details')
@login_required
def user_details():
    return render_template("user-details.html", user=current_user)

# Market comparison route
@views.route('/compare-markets')
@login_required
def compare_markets():
    return render_template("compare.html", user=current_user)

# AI Chatbot route
@views.route('/mr-market', methods=['POST'])
@login_required
def mr_market():
    user_msg = request.json.get("message")

    try:
        response = client.chat.completions.create(
            extra_headers={
                "HTTP-Referer": "https://yourdomain.com",  # optional
                "X-Title": "StockWise"  # optional
            },
            model="nvidia/llama-3.3-nemotron-super-49b-v1:free",
            messages=[
                {"role": "system", "content": "You are Mr. Market, a helpful assistant specialized in the Indian stock market."},
                {"role": "user", "content": user_msg}
            ]
        )
        reply = response.choices[0].message.content
        return jsonify({"reply": reply})
    except Exception as e:
        print("Chatbot error:", e)
        return jsonify({"reply": "Sorry, Mr. Market is facing technical difficulties at the moment."}), 500

# Helper functions
def get_nse_index_data(symbol):
    mock_data = {
        "NIFTY_50": {
            "data": [{
                "lastPrice": "22800.45",
                "pChange": 0.95,
                "quantityTraded": "13458000"
            }]
        },
        "BANK_NIFTY": {
            "data": [{
                "lastPrice": "48750.20",
                "pChange": -0.42,
                "quantityTraded": "9800000"
            }]
        },
        "NIFTY_IT": {
            "data": [{
                "lastPrice": "34100.75",
                "pChange": 1.22,
                "quantityTraded": "5600000"
            }]
        }
    }
    return mock_data.get(symbol, None)

def fetch_stock_news():
    api_key = "eda84e16e2da442eb1d883146df0e7c4"  # Change your API key
    url = f"https://newsapi.org/v2/everything?q=indian+stock+market&language=en&sortBy=publishedAt&apiKey={api_key}"

    try:
        response = requests.get(url)
        response.raise_for_status()
        articles = response.json().get("articles", [])
        return articles[:5]  # return top 5
    except Exception as e:
        current_app.logger.error(f"News API Error: {e}")
        return []

# OpenRouter client setup
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="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"
)