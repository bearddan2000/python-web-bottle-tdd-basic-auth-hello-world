FROM python:latest

COPY bin/ /app

WORKDIR /app

RUN pip install -r requirements.txt

RUN mkdir -p /app/allure-report

VOLUME [ "/app/allure-report" ]

RUN rm -Rf .pytest_cache

CMD [ "pytest", "-v", "-s", "--alluredir=/app/allure-report" ]
