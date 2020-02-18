FROM python

RUN pip3 install flask

WORKDIR /app

COPY app.py /app

ENTRYPOINT ["python3"]

EXPOSE 8080

CMD ["app.py"]
