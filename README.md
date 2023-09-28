![Ikman.lk Web Scraper](https://socialify.git.ci/ishan-anuranga/Ikman.lk-Web-Scraper/image?font=Rokkitt&language=1&name=1&owner=1&pattern=Plus&theme=Light)

# <p style="text-align: center;">Ikman.lk Web Scraper</p>

![GitHub last commit](https://img.shields.io/github/last-commit/ishan-anuranga/Ikman.lk-Web-Scraper/main?style=flat-square)

⚠️ **Disclaimer**: This project is purely for educational purposes only! The creator is not liable for any unintended or improper use of this tool.

Welcome to the Ikman.lk Web Scraper, a Python tool that allows you to scrape Ikman.lk for search results and save them as a convenient CSV file.

## 🚀 Features

- Retrieve detailed information from Ikman.lk search results.
- Save the extracted data as a CSV file for easy analysis.

## 📋 Extracted Data

The scraper extracts the following details from each search result:

| Detail           | Description                                          |
| ---------------- | ---------------------------------------------------- |
| Title            | Title of the ad                                      |
| Link             | Link to the ad                                       |
| Premium Member   | Indicates whether the poster is a premium member    |
| Verified Member  | Indicates whether the poster is a verified member   |
| Location         | Location of the item in the ad                      |
| Category         | Category of the ad                                   |
| Price            | Price of the item                                    |
| Top Ad           | Indicates whether the ad is a top ad                |
| Image            | Image link of the ad                                 |

## 🛠️ Installation

1. Clone this repository to your local machine:

```bash
git clone https://github.com/ishan-anuranga/Ikman.lk-Web-Scraper.git
```

2. Navigate to the project directory:

```bash
cd Ikman.lk-Web-Scraper
```

3. Install the required Python packages:

```bash
pip install -r requirements.txt
```

## 📖 Usage

To scrape Ikman.lk for a given search query and a specific number of pages and save the results as a CSV file, follow these steps:

1. Run the scraper from the console with the desired query and number of pages:

```bash
python main.py --query "iphone 15" --num_pages 2 --save
```

That's it! The scraper will start collecting data, and you'll find the CSV file with the results in the project directory.

## 🤝 Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request to improve this project.

## 📄 License
This project is licensed under the MIT License - see the [LICENSE](https://github.com/ishan-anuranga/ikman.lk-web-scraper/blob/main/LICENSE) file for details.

---

Made with ❤️ by [Ishan](https://github.com/ishan-anuranga)