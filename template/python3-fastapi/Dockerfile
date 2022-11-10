FROM --platform=${TARGETPLATFORM:-linux/amd64} ghcr.io/openfaas/of-watchdog:0.9.10 as watchdog
FROM --platform=${TARGETPLATFORM:-linux/amd64} python:3.10-slim-buster as build

COPY --from=watchdog /fwatchdog /usr/bin/fwatchdog
RUN chmod +x /usr/bin/fwatchdog

RUN apt update && apt install -y musl-dev gcc make

# Add non root user
RUN useradd -ms /bin/bash app
RUN chown app /home/app

USER app

ENV PATH=$PATH:/home/app/.local/bin

WORKDIR /home/app/

COPY requirements.txt   .
USER root
RUN pip install -r requirements.txt
USER app
COPY main.py           .

RUN mkdir -p function
RUN touch ./function/__init__.py
WORKDIR /home/app/function/
COPY function/requirements.txt	.
RUN pip install --user -r requirements.txt

WORKDIR /home/app/

USER root
# remove build dependencies
RUN apt remove musl-dev gcc make -y && apt autoremove
COPY function function
RUN chown -R app:app ./
USER app

ENV fprocess="uvicorn main:app --workers 1 --host 0.0.0.0 --port 8000 --reload"

ENV cgi_headers="true"
ENV mode="http"
ENV upstream_url="http://127.0.0.1:8000"

HEALTHCHECK --interval=5s CMD [ -e /tmp/.lock ] || exit 1

CMD ["fwatchdog"]
