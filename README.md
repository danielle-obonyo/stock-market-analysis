**S\&P 500 Stock Price Prediction Project**



&#x20;**1. Project Overview**



This project analyzes historical S\&P 500 stock prices from 2013 to 2018. It explores data storage formats, performs data processing and technical indicator calculations, develops stock price prediction models, and presents the results through an interactive Streamlit dashboard.



&#x20;**2. Technologies and Libraries**



\- \*\*Python:\*\* Main programming language.

\- \*\*Pandas:\*\* Data cleaning, processing, and analysis.

\- \*\*NumPy:\*\* Numerical operations.

\- \*\*Polars:\*\* High-performance data processing.

\- \*\*PyArrow:\*\* Parquet file handling.

\- \*\*Scikit-learn:\*\* Machine learning models and evaluation.

\- \*\*Streamlit:\*\* Interactive dashboard development.

\- \*\*Plotly:\*\* Interactive data visualizations.



&#x20;**3. Project Components**



***Part 1: Benchmarking Storage Formats***

Compared CSV and Parquet storage formats using different compression methods: uncompressed, Snappy, and ZSTD. Evaluated file sizes and read performance across different dataset scales.



***Part 2: Data Processing and Predictive Modelling***

Processed stock price data using Pandas and Polars. Calculated the 5-day Simple Moving Average (SMA) and 14-day Relative Strength Index (RSI).



Developed and evaluated Linear Regression and Random Forest models to predict the next closing price. A baseline model was also used for comparison.



&#x20;***Part 3: Interactive Dashboard***

Developed a Streamlit dashboard that allows users to:

\- Select a stock ticker.

\- Filter stock data by date.

\- View historical closing prices.

\- Compare actual and predicted closing prices.

\- Compare model performance using Mean Absolute Error (MAE).

\- Visualize SMA and RSI technical indicators.



**4. Analysis and Design Decisions**



&#x20;***Part 1: Benchmarking Storage Formats***



CSV and Parquet were compared using different compression methods. Parquet was selected for its faster read performance and smaller file sizes. Uncompressed Parquet provided the fastest read times, while ZSTD achieved the greatest storage reduction of approximately 66%. Snappy offered a balance between speed and compression.



***Part 2: Data Processing and Predictive Modelling***



Pandas was used for data cleaning and analysis because of its extensive data manipulation capabilities. Polars was included to compare processing speed, and it completed the tested processing task approximately 2.94 times faster than Pandas.



Linear Regression and Random Forest were selected to compare two predictive modelling approaches. Linear Regression achieved a lower MAE (0.904) than Random Forest (1.378) and the baseline model (0.904 approximately). The results suggest that Linear Regression performed slightly better, although the baseline's similar performance indicates that predicting the next closing price remains challenging.



&#x20;***Part 3: Interactive Dashboard***



Streamlit was selected to create an interactive dashboard without requiring a separate web application framework. Plotly was used to create interactive charts that allow users to explore stock prices, model predictions, and technical indicators.



&#x20;**5. How to Run the Project**



&#x20;**Prerequisites**

\- Python installed on your computer.

\- The project files downloaded or extracted into one folder.



&#x20;**Setup Instructions**



1\. Open Anaconda Prompt or a terminal in the main project folder.

2\. Create a virtual environment:



&#x20;  **`python -m venv .venv`**



3\. Activate the environment:



&#x20;  *Windows:*

&#x20;  **`.venv\\Scripts\\activate`**



&#x20;  *Mac/Linux:*

&#x20;  **`source .venv/bin/activate`**



4\. Install the required libraries:



&#x20;  **`python -m pip install -r requirements.txt`**



5\. Navigate to the dashboard folder:



&#x20;  **`cd dashboard`**



6\. Launch the dashboard:



&#x20;  **`python -m streamlit run app.py`**



7\. Open the local URL displayed in the terminal to access the dashboard.





&#x20;**6. Project Files**



\- `all\_stocks\_5yr.csv`: Original stock dataset.

\- `stock\_prediction\_results.csv`: Model prediction results.

\- `stock\_data\_with\_indicators.csv`: Processed stock data containing technical indicators.

\- `requirements.txt`: Required Python libraries.

\- `README.md`: Project overview and setup instructions.

\- `notebooks/`: Jupyter notebooks containing the analysis and modelling code.

\- `dashboard/`: Streamlit dashboard application.

\- `benchmarks/`: Storage format benchmark results and comparison graphs.

\- `screenshots/`: Individual dashboard screenshots.

\- `Dashboard\_Screenshots.pdf`: PDF presentation of the dashboard screenshots.



&#x20;**7. Conclusion**



The project demonstrates how storage format selection, data processing tools, predictive modelling, and interactive visualization can support stock market data analysis.

