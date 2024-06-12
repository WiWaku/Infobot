FROM python:3.10-alpine

WORKDIR /

RUN pip install aiogram aioschedule requests google-api-python-client==2.79.0 google-auth-httplib2==0.1.0 google-auth-oauthlib=1.0.0

COPY env.py .
COPY main.py .
COPY router.py .
COPY schema.py .
COPY services.py .
COPY states.py .
COPY telegram.py .
COPY payment_instructions.mp4 .
COPY day-check.txt .
COPY credentials.json .
COPY token.pickle .




EXPOSE 5000

CMD ["python", "main.py"]
