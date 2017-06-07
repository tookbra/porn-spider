FROM python:3.5
ENV PATH /usr/local/bin:$PATH
ADD . /porn
WORKDIR /porn
RUN pip install -r requirements.txt
CMD ["python", "-u", "bootstrap.py"]