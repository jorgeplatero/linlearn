# Web App for Linear Classification Exploration

This application provides an interactive platform to explore the fundamental concepts of linear 
classification. By manipulating the model weights (slope and intercept) directly, users can observe 
the impact of their adjustments on the decision boundary line and model accuracy in real-time.

### Prerequisites

Ensure you have Python 3.11 installed on your system.

Install the virtual environment support:

```bash
sudo apt update && sudo apt install python3.11-venv
```

### Installation

Clone the repository and install the dependencies:

```bash
#clone the repository
git clone https://github.com/jorgeplatero/linlearn.git
cd linlearn-web-app

#create the virtual environment
python -m venv venv

#activate the virtual environment
source venv/bin/activate

#install dependencies
pip install -r requirements.txt
```

### How to Run the Application

With the virtual environment activated, run the following command to start the app locally:

```bash
streamlit run app.py
```

### Technologies

| Component | Technology | Version | Description |
| :--- | :--- | :--- | :--- |
| **Frontend/App** | **Streamlit** | `1.32.2` | Framework for web application development |
| **Data Analysis** | **Pandas** | `2.2.1` | Library for data manipulation |
| **Visualization** | **Plotly** |`5.20.0` | Library for dynamic and interactive charts |
| **Language** | **Python** | `>=3.11` | Language for script development |
| **Enviroment** | **Venv** | `-` | Manager for dependency isolation |

### Deployment

The web application is available via Streamlit Cloud.

Link to the web app: https://linlearn.streamlit.app
