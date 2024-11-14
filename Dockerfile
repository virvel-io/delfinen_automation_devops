FROM python:3.10-slim

# Set up the working directory and install dependencies
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY map.py .
COPY get_weather.py .
COPY streamlit_app.py .

# Expose the required port (8501 by default for Streamlit)
EXPOSE 8501

# Start the Streamlit app
CMD ["streamlit", "run", "streamlit_app.py"]