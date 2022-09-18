FROM python:3.8

WORKDIR /just_finance

COPY requirements.txt ./
RUN apt-get update && apt-get install -y \
gettext
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "gunicorn", "--bind", "0.0.0.0", "-p", "8000",  "just_finance.wsgi"  ]