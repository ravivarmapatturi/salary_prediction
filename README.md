# Salary Prediction Web Application

This project involves building a machine learning web application to predict developer salaries using data from the Stack Overflow Developer Survey 2023. The application was developed from scratch in Python using the Streamlit framework, which allows for the easy creation of interactive web applications.

## Key Features:

### Data Collection and Analysis:
- **Dataset**: Sourced from the Stack Overflow Developer Survey 2023, providing real-world insights into developer salaries based on various factors such as experience, education, and job roles.
- **Data Analysis**: The data was analyzed to identify trends and patterns that could influence salary predictions.

### Model Building:
- Various machine learning algorithms were tested and evaluated to find the best model for salary prediction.
- Features were selected, preprocessing techniques were applied, and hyperparameter tuning was performed to optimize model performance.
- The final model was chosen for its accuracy and ability to generalize well to new data.

### Web Application Development:
- The selected model was integrated into a user-friendly web application built using Streamlit.
- Users can input relevant data (experience, education, job roles) and receive salary predictions based on the trained model.
- The application allows users to explore the impact of different variables on predicted salaries, making it a valuable tool for understanding salary dynamics in the tech industry.

---

## How to Set Up and Run the Application

Follow these steps to set up and run the Salary Prediction Web Application on your Ubuntu server.

### Step 1: System Setup

First, ensure your system is up to date and install the necessary packages:

```bash
sudo apt update
sudo apt-get update
sudo apt upgrade -y
sudo apt install git curl unzip tar make sudo vim wget -y
```

Step 2: Clone the GitHub Repository
Next, clone the repository containing the project code:

```bash
git clone https://github.com/ravivarmapatturi/salary_prediction.git
cd salary_prediction
```

Step 3: Install Python and Required Libraries
If Python3 and pip are not already installed, run the following command to install them:

```bash
sudo apt install python3-pip
Now, install the required Python packages from the requirements.txt file:
```

```bash
pip3 install -r requirements.txt
Step 4: Run the Application
You can choose to run the Streamlit application either temporarily (for testing purposes) or permanently (in the background).
```

To temporarily run the Streamlit application:
```bash

python3 -m streamlit run app.py
```

To run the application permanently (in the background):

```bash
nohup python3 -m streamlit run app.py &
```

Step 5: Access the Web Application
Once the application is running, you can access it in your browser using the following URL:

http://3.87.225.123:8501/

