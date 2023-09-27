from Scraper import Scraper
import argparse
import datetime


def main():
    parser = argparse.ArgumentParser(
        description="Ikman.lk Web Scraper",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument("-q", "--query", default="iphone", help="search query")
    parser.add_argument(
        "-n", "--num_pages", default=1, type=int, help="number of pages to extract"
    )
    parser.add_argument(
        "-s", "--save", action="store_true", help="save the result as csv"
    )
    args = vars(parser.parse_args())

    scraper = Scraper()
    scraped_data = scraper.scrape(args["query"], args["num_pages"])
    print("extracted", len(scraped_data), "rows")

    if args["save"]:
        scraped_data.to_csv(
            f'{args["query"]} - '
            f'{args["num_pages"]} pages - '
            f'{datetime.datetime.now().strftime("%m-%d-%Y %H-%M-%S %p")}.csv',
            index=False,
        )


if __name__ == "__main__":
    main()
