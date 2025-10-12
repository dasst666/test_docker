FROM ubuntu:18.04 AS base
RUN apt-get update
RUN apt-get install -y python3 python3-pip

FROM base AS development
COPY main.py /main.py 
CMD ["python3", "/main.py"]

FROM development AS production
COPY prod.py /prod.py
CMD ["python3", "/prod.py"]
