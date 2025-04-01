# Example spider for scrapyd-k8s

[Scrapyd-k8s](https://github.com/q-m/scrapyd-k8s) is an application for
deploying and running Scrapy spiders as either Docker instances or Kubernetes
jobs. Its intention is to be compatible with [scrapyd](https://scrapyd.readthedocs.io/),
but adapt to a container-based environment.

This spider is an example spider, used in the standard configuration of scrapyd-k8s,
so that one can get started easily.

## Scraped site

This project contains two spiders. The `quotes` spider returns quotes from
[quotes.toscrape.com](https://quotes.toscrape.com).

The `static` spider returns a single dummy quote without accessing the network.
This can be used for testing. There are several settings and environment variables
that modify its behaviour:
- spider setting `STATIC_TEXT` - quote text (default _To be, or not to be_)
- spider setting `STATIC_AUTHOR` - quote author (default _Shakespeare_)
- environment variable `STATIC_TAGS` - quote tags (default _static_)
- spider setting `STATIC_SLEEP` - time to sleep in the spider (default _0_)

## Running locally

Make sure you have this project checked out.

```sh
git clone https://github.com/q-m/scrapyd-k8s-spider-example.git
cd scrapyd-k8s-spider-example
```

### From the console

When you have Python and Scrapy installed, you can run this directly from the
command-line:

```sh
$ scrapy list
```
> ```
> quotes
> static
> ```
```sh
$ scrapy crawl quotes
```
> ```
> [scrapy.utils.log] INFO: Scrapy 2.9.0 started (bot: example)
> [scrapy.core.engine] INFO: Spider opened
> [scrapy.core.engine] DEBUG: Crawled (200) <GET http://quotes.toscrape.com/> (referer: None)
> [scrapy.core.scraper] DEBUG: Scraped from <200 http://quotes.toscrape.com/>
> {'text': 'The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking.', 'author': 'Albert Einstein', 'tags': 'change'}
> ...
> [scrapy.core.engine] INFO: Spider closed (shutdown)
> ```

(output redacted for readability)

### With Docker

This spider is really meant to be run with Docker. First you need to build an image.

```sh
docker build -t example --label org.scrapy.spiders=quote .
docker inspect example -f '{{ .Config.Labels | json }}'
```
> ```
> {"org.scrapy.project":"example","org.scrapy.spiders":"quote"}
> ```

Now you can run scrapy as usual, with Docker:
```sh
docker run --rm example scrapy list
```
> ```
> quotes
> static
> ```

```sh
docker run --rm example scrapy crawl quotes
```
> ```
> [scrapy.utils.log] INFO: Scrapy 2.11.0 started (bot: example)
> [scrapy.core.engine] INFO: Spider opened
> [scrapy.core.engine] DEBUG: Crawled (200) <GET http://quotes.toscrape.com/> (referer: None)
> [scrapy.core.scraper] DEBUG: Scraped from <200 http://quotes.toscrape.com/>
> {'text': 'The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking.', 'author': 'Albert Einstein', 'tags': 'change'}
> ...
> [scrapy.core.engine] INFO: Spider closed (shutdown)
> ```

(output redacted for readability)

## Spider as Docker image

- Spiders are distributed as Docker images.
- One can run `scrapy crawl <spider>` in the container to run a spider,
  without any additional setup (so set `SCRAPY_SETTINGS_MODULE`).
- Each Docker image has specific labels to indicate its project and spiders.
  * `org.scrapy.project` - the project name
  * `org.scrapy.spiders` - the spiders (those returned by `scrapy list`, comma-separated)

Please see the [Github Action](./.github/workflows/container.yml) for an
example of how to build such a container. In short, first build the container,
then run the container to obtain the list of spiders, then add labels to the
container so it can work with scrapyd-k8s.

## License

This software is distributed under the [MIT license](LICENSE.md).
