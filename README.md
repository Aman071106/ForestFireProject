# 🔥 Forest Fire Prediction Project

This project aims to predict the likelihood and severity of forest fires using machine learning models based on meteorological and geographical data.

## 📁 Project Structure

```
ForestFireProject/
├── models/          # Trained ML models
├── notebooks/       # Jupyter notebooks for EDA, training, etc.
├── app/             # Frontend UI or Streamlit app
├── backend/         # Backend endpoints (e.g., FastAPI/Flask)
│   └── endpoints.py
├── frontend/
│   └── app.py       # Frontend script
├── requirements.txt # Python dependencies
├── README.md
```

## 📊 Features

- Exploratory Data Analysis (EDA)
- Feature Engineering
- Model Training (Ridge, Lasso, etc.)
- Performance Evaluation

## 🧪 Technologies Used

- Python
- Pandas, NumPy, Matplotlib, Seaborn
- Scikit-learn
- FastAPI/Flask
- AWS Elastic Beanstalk
- GitHub Actions / CodePipeline (CI/CD)

## 🚀 Deployment

Deployment is done via AWS Elastic Beanstalk using GitHub CI/CD.

## 📌 How to Run

1. Clone the repo:
   ```bash
   git clone https://github.com/<your-username>/ForestFireProject.git
   cd ForestFireProject
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the app (example with Streamlit):
   ```bash
   python run app/backend/endpoints.py
   streamlit run app/frontend/app.py
   ```

## 👨‍💻 Author

- **Aman Gupta**
