📈 StockWise – Smart Indian Stock Market Companion

StockWise is a full-stack FinTech web application that simplifies investing and personal finance for Indian users.
It combines real-time market data, AI-driven insights, budget tracking, and an interactive chatbot to help users make informed and confident financial decisions.

🚀 Features
💹 Stock & Market Insights

Live Index Data: Real-time tracking of NIFTY 50, Bank NIFTY, and NIFTY IT indices.

Exchange Comparison: View and compare stock performance across NSE and BSE.

Curated Market News: Top financial headlines via NewsAPI for quick market updates.

💰 Personal Finance & AI Tools

Budget & Investment Tracker: Manage income, expenses, and visualize savings with AI-based investment recommendations.

Personal Investment Advisor: AI analyzes portfolio diversification and generates weekly performance insights.

Mr. Market Chatbot: Your personal financial assistant powered by OpenRouter AI, answering queries and explaining market terms.

🔐 Additional Features

Secure user authentication with Flask-Login.

Glassmorphic UI built using Bootstrap 5 and Animate.css.

Responsive, modern, and interactive user interface.

🧠 Tech Stack
Category	Technologies
Frontend	HTML5, CSS3, JavaScript, Bootstrap 5, Animate.css
Backend	Python (Flask), Flask-Login, Flask-SQLAlchemy
AI & APIs	OpenRouter (AI Chatbot), NewsAPI (Market News)
Database	SQLite / PostgreSQL for user portfolios & transactions
⚙️ Installation & Setup
1️⃣ Clone the repository
git clone https://github.com/your-username/StockWisee.git
cd stockwise

2️⃣ Install dependencies
pip install flask flask_sqlalchemy flask_login openai requests

3️⃣ Set API keys

Open views.py (or config file) and replace with your NewsAPI and OpenRouter keys:

NEWS_API_KEY = "your_news_api_key"
OPENROUTER_API_KEY = "your_openrouter_api_key"

4️⃣ Run the application
python main.py


Access the app at:
👉 http://127.0.0.1:5000/

🧭 Project Structure
StockWise/
│
├── main.py                 # Application entry point
├── models.py               # Database models
├── views.py                # App routes and logic
├── templates/              # HTML templates
├── static/                 # CSS, JS, and assets
└── requirements.txt        # Dependencies

🌟 Why StockWise?

Simplifies financial planning for both beginners and active investors.

Unites market insights, budgeting, and AI-driven advice in one place.

Promotes data-driven decision-making and smarter investment habits.

📈 Future Enhancements

Integration with UPI/digital payments for investment tracking.

Support for mutual funds and ETFs.

Advanced portfolio analytics and risk scoring.

👨‍💻 Contributors

Developed by: Saurish Chandra and Arka Sengupta and Shaurya Singh
For hackathon submission under the FinTech – Digital Finance & Budgeting Solutions category.
