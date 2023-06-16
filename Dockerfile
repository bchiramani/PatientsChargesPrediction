FROM python:3.7 

RUN pip install virtualenv 
ENV VIRTUAL_ENV=/env 
RUN virtualenv venv -p python3  
ENV PATH="VIRTUAL_ENV/bin:$PATH"  

WORKDIR /app  
ADD . /app  

RUN pip install -r requirements.txt  

EXPOSE 5000

CMD ["python" , "app.py"]
