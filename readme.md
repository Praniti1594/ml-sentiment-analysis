
---

# ⭐  Sentiment Analysis Using Machine Learning  

This project is a **sentiment analysis system** built using **Python (scikit-learn)** and served through a **Flask backend** with a minimal frontend for testing.

It takes a movie review as input and predicts whether the sentiment is **Positive** or **Negative** using a trained Machine Learning model.

---

# 🚀 **Key Features**

* Machine Learning sentiment classifier (TF-IDF + ML models)
* Trained on IMDB Reviews Dataset
* Flask backend with `/predict` API endpoint
* Simple HTML UI
* Postman-ready API
* Modular folder structure (data, model, app)

---

# 🧠 **Models Trained & Why the Best Model Performed Well**

### **1. Logistic Regression**

* High accuracy
* Works extremely well for text classification
* Handles high-dimensional TF-IDF vectors
* Fast to train and lightweight
* **Best performance among all models**

### **2. Naive Bayes (MultinomialNB)**

* Good baseline
* Very fast
* Works well with word frequencies
* Slightly lower accuracy compared to Logistic Regression

### **3. Support Vector Machine (SVM)**

* Good for text
* Accuracy similar but slightly lower than Logistic Regression

### **Why Logistic Regression Was Best**

| Reason                       | Explanation                                                            |
| ---------------------------- | ---------------------------------------------------------------------- |
| Handles sparse text data     | TF-IDF produces large sparse matrices — LR performs very well on those |
| Captures linear separability | Sentiment classification is often linearly separable                   |
| Balanced bias vs variance    | Gives stable predictions                                               |
| Fast inference               | Perfect for APIs                                                       |

📌 **Final Model Used:** Logistic Regression
📌 **Accuracy Achieved:** *Highest among all models you tested*
📌 **Vectorizer Used:** TF-IDF with stopwords removal

---

# 📊 **How Accuracy Improved**

During training:
1. Started with **Bag-of-Words** → moderate accuracy
2. Shifted to **TF-IDF** → accuracy improved
3. Tried multiple models → Logistic Regression performed best
4. Tuned hyperparameters → further improvement

Improvements came from:

* Removing stopwords
* Using TF-IDF instead of BOW
* Testing multiple ML models
* Cleaning dataset (punctuation, lowercase, etc.)

---

# 🧪 **Dataset Used**

**IMDB Movie Reviews Dataset**
Contains:

* 50K labelled reviews
* Balanced positive & negative samples
* Perfect for sentiment analysis tasks

Stored locally:

```
data/imdb_reviews.csv
```

---

# 🔧 **Tech Stack**

### **Backend**

* Python
* Flask
* scikit-learn
* pandas
* joblib

### **Frontend**

* HTML
* Fetch API

---

# 🧩 **Project Structure**

```
ml-sentiment-project/
│── data/
│     └── imdb_reviews.csv
│── model/
│     └── vectorizer.pkl
│     └── model.pkl
│── app.py
│── index.html
│── readme.md
│── requirements.txt
│── venv/
```

---

# ⚙️ **How the API Works**

### **Endpoint: `/predict`**

**Method:** POST
**Input:** JSON

```json
{
   "text": "The movie was fantastic!"
}
```

**Output:** JSON

```json
{
   "sentiment": "Positive"
}
```

---

# 🖥️ **How to Run This Project Locally**

### 1️⃣ **Clone the Repository**

```
git clone https://github.com/YOUR_USERNAME/ml-sentiment-analysis.git
cd ml-sentiment-analysis
```

### 2️⃣ **Create Virtual Environment**

```
python -m venv venv
```

### 3️⃣ **Activate it**

Windows:

```
venv\Scripts\activate
```

### 4️⃣ **Install Dependencies**

```
pip install -r requirements.txt
```

### 5️⃣ **Run the Flask App**

```
python app.py
```

### 6️⃣ **Open Frontend**

Double-click:

```
index.html
```

or test API in Postman:

POST → `http://127.0.0.1:5000/predict`

---



