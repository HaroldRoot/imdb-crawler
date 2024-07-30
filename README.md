# IMDb Crawler

## English

### Description

This Python script uses Selenium to scrape and display movie titles from IMDb for a user-specified year. It prompts the user to enter a year within a valid range (1894 to the current year), constructs a search URL based on that year, and navigates to the IMDb search results page. The script then extracts and prints the titles of all movies released in the specified year, handling pagination to ensure all titles are collected. It also manages exceptions and ensures the browser is closed properly at the end.

### Requirements

- Python 3.x
- Selenium
- ChromeDriver (or another WebDriver compatible with your browser)

### Installation

1. Install Selenium using pip:

    ```bash
    pip install selenium
    ```

2. Download the appropriate WebDriver for your browser and ensure it's in your system's PATH. For Chrome, you can download ChromeDriver from [here](https://developer.chrome.com/docs/chromedriver/downloads).

### Usage

1. Run the script:

    ```bash
    python crawler.py
    ```

2. Enter the desired year when prompted.

3. The script will print the titles of all movies released in that year.

### Notes

- Ensure that your WebDriver version matches your browser version.
- The script handles pagination and should work for most years, but may need adjustments for very large datasets or changes in IMDb's website structure.

### License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 中文

### 描述

这个 Python 脚本使用 Selenium 从 IMDb 上抓取并显示指定年份的电影标题。它会提示用户输入一个有效范围内的年份（1894 年至当前年份），根据该年份构造搜索 URL，并导航到 IMDb 搜索结果页面。然后，脚本提取并打印指定年份发布的所有电影标题，处理分页以确保所有标题都被收集。脚本还处理异常，并确保在结束时正确关闭浏览器。

### 需求

- Python 3.x
- Selenium
- ChromeDriver（或与您的浏览器兼容的其他 WebDriver）

### 安装

1. 使用 pip 安装 Selenium：

    ```bash
    pip install selenium
    ```

2. 下载适用于您的浏览器的 WebDriver，并确保它在系统的 PATH 中。对于 Chrome，您可以从 [这里](https://developer.chrome.com/docs/chromedriver/downloads?hl=zh-cn) 下载 ChromeDriver。

### 使用方法

1. 运行脚本：

    ```bash
    python crawler.py
    ```

2. 当提示输入年份时，输入所需的年份。

3. 脚本将打印该年份发布的所有电影标题。

### 注意事项

- 确保您的 WebDriver 版本与浏览器版本匹配。
- 脚本处理分页并适用于大多数年份，但可能需要根据 IMDb 网站结构的变化进行调整。

### 许可证

本项目采用 MIT 许可证 - 详细信息见 [LICENSE](LICENSE) 文件。
