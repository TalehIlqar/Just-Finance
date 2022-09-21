FROM python:3.8

WORKDIR /just_finance

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .