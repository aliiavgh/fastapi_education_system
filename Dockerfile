FROM python:3.9
# Set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /home/hello/Documents/LAB/Udemy_clone_project
COPY ./requirements.txt /Udemy_clone_project/requirements.txt
# Install poetry:
RUN pip install --no-cache-dir --upgrade -r /Udemy_clone_project/requirements.txt
# Copy in the config files:
COPY COPY ./src/app.py /Udemy_clone_project/
RUN chmod 777 prestart.sh
RUN chmod 777 run.sh
# Install only dependencies:
RUN poetry install --no-root --no-dev
COPY ./app /code/app/
WORKDIR /home/hello/Documents/LAB/Udemy_clone_project
EXPOSE 8000

CMD ["uvicorn", "src.app:app", "--host", "0.0.0.0", "--port", "80"]
ENV PYTHONPATH "/Udemy_clone_project"