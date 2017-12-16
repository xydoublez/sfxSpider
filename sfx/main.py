from scrapy import cmdline


def main():
    cmdline.execute(['scrapy', 'crawl', 'myspider'])


if __name__ == '__main__':
    main()
