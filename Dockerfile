FROM python:3.8

RUN set -ex \
	 mkdir -p /usr/src/app/
WORKDIR /usr/src/app/

COPY . /usr/src/app/
RUN set -ex \ 
	pip3 install --no-cache-dir -r requirements.txt \
	&& rm requirements.txt

CMD ["python3", "factorial.py"]
