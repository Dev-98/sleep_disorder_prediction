FROM python:3.10-slim

ENV APP_HOME /app
WORKDIR $APP_HOME

COPY . ./

RUN pip install -r requirements.txt


CMD streamlit run webapp.py
