FROM python:3.11-slim as base

COPY requirements.txt /opt/app/requirements.txt

WORKDIR /opt/app
RUN pip3 install --no-cache-dir --disable-pip-version-check -r requirements.txt

### Builder stage
FROM base as builder

WORKDIR /usr/src/app

COPY . /usr/src/app/

# use egg because it contains precompiled bytecode
RUN python3 setup.py clean bdist_egg && \
    mv dist/*.egg /scrapy-spider.egg

### App stage
FROM base

COPY --from=builder /scrapy-spider.egg /usr/local/lib/

USER nobody

# make sure scrapy can run the spiders without extra setup
ENV PYTHONPATH=/usr/local/lib/scrapy-spider.egg
ENV SCRAPY_SETTINGS_MODULE=example.settings
LABEL org.scrapy.project=example
# LABEL org.scrapy.spiders is set by the build script

WORKDIR /
