FROM python:3 
WORKDIR /app


# RUN apt-get update
# RUN apt-get install -y tdsodbc unixodbc-dev
# RUN apt install unixodbc-bin -y
# RUN apt-get clean -y

EXPOSE 5000
COPY . .
RUN pip install -r requirements.txt && rm -rf /root/.cache


ENTRYPOINT ["python3","app.py"]


# docker build -t socket-server . 
# docker run -d -p 5000:5000 socket-server 
