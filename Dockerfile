FROM python:3.9

WORKDIR /Udemy_clone_project

COPY ./requirements.txt /Udemy_clone_project/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /Udemy_clone_project/requirements.txt

# 
COPY ./src/app.py /Udemy_clone_project/

# 
CMD ["uvicorn", "src.app:app", "--host", "0.0.0.0", "--port", "80"]