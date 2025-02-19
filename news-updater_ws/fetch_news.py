import requests
from bs4 import BeautifulSoup

# 定义目标新闻网站
YAHOO_FINANCE_URL = "https://finance.yahoo.com"
BLOOMBERG_MARKETS_URL = "https://www.bloomberg.com/markets"

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

def fetch_yahoo_news():
    """ 抓取Yahoo Finance的新闻 """
    response = requests.get(YAHOO_FINANCE_URL, headers=HEADERS)
    if response.status_code != 200:
        print("Failed to retrieve Yahoo Finance news page")
        return []

    soup = BeautifulSoup(response.text, 'html.parser')
    articles = soup.find_all('li', class_='js-stream-content')

    news_list = []
    for article in articles[:5]:  # 只抓取前5条新闻，防止数据过载
        title_tag = article.find('h3')
        link_tag = article.find('a')

        if not title_tag or not link_tag:
            continue

        title = title_tag.get_text(strip=True)
        link = link_tag['href']
        
        # Yahoo Finance的链接有时是相对路径，需要补全
        if not link.startswith('http'):
            link = YAHOO_FINANCE_URL + link

        # 获取摘要（有些文章没有摘要）
        summary = "No summary available"
        summary_tag = article.find('p')
        if summary_tag:
            summary = summary_tag.get_text(strip=True)

        news_list.append({
            'title': title,
            'url': link,
            'summary': summary
        })

    return news_list

def fetch_bloomberg_news():
    """ 抓取Bloomberg Markets的新闻 """
    response = requests.get(BLOOMBERG_MARKETS_URL, headers=HEADERS)
    if response.status_code != 200:
        print("Failed to retrieve Bloomberg Markets news page")
        return []

    soup = BeautifulSoup(response.text, 'html.parser')
    articles = soup.find_all('article')  # Bloomberg的新闻通常在 <article> 标签中

    news_list = []
    for article in articles[:5]:  # 只抓取前5条新闻
        title_tag = article.find('h3')
        link_tag = article.find('a')

        if not title_tag or not link_tag:
            continue

        title = title_tag.get_text(strip=True)
        link = link_tag['href']

        # Bloomberg的链接有时是相对路径，需要补全
        if not link.startswith('http'):
            link = "https://www.bloomberg.com" + link

        # 获取摘要（部分新闻没有摘要）
        summary = "No summary available"
        summary_tag = article.find('p')
        if summary_tag:
            summary = summary_tag.get_text(strip=True)

        news_list.append({
            'title': title,
            'url': link,
            'summary': summary
        })

    return news_list

def save_news(yahoo_news, bloomberg_news, file_name='latest_news.md'):
    """ 保存新闻到 Markdown 文件 """
    with open(file_name, 'w', encoding='utf-8') as file:
        file.write("# 📰 Latest Financial News\n\n")

        # Yahoo Finance 新闻
        file.write("## Yahoo Finance\n\n")
        for news in yahoo_news:
            file.write(f"### {news['title']}\n")
            file.write(f"**Summary:** {news['summary']}\n\n")
            file.write(f"[Read more]({news['url']})\n\n")
            file.write("---\n\n")

        # Bloomberg Markets 新闻
        file.write("## Bloomberg Markets\n\n")
        for news in bloomberg_news:
            file.write(f"### {news['title']}\n")
            file.write(f"**Summary:** {news['summary']}\n\n")
            file.write(f"[Read more]({news['url']})\n\n")
            file.write("---\n\n")

if __name__ == "__main__":
    yahoo_news = fetch_yahoo_news()
    bloomberg_news = fetch_bloomberg_news()
    save_news(yahoo_news, bloomberg_news)
    print('✅ Successfully updated Yahoo Finance & Bloomberg news!')
