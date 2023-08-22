FROM python:3.8

WORKDIR /usr/app

COPY . .

RUN pip install -r requirements.txt

EXPOSE 8501

CMD streamlit run webapp.py
