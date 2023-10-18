FROM python:3

WORKDIR /educational_modules

COPY ./requirements.txt /educational_modules/

RUN python.exe -m pip install --upgrade pip

RUN pip install -r requirements.txt

COPY . /educational_modules/

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
