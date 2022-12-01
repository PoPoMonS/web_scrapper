from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def get_page_count(keyword):
    options = Options()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    browser = webdriver.Chrome(options=options)
    base_url = "https://kr.indeed.com/jobs"
    browser.get(f"{base_url}?q={keyword}")

    soup = BeautifulSoup(browser.page_source, "html.parser")
    nav = soup.find("nav", role="navigation")
    pages = nav.find_all("div", recursive=False)
    browser.close()
    if len(pages) == 0:
        return 1
    elif len(pages) >= 2:
        return len(pages) - 1


def indeed_extractor(keyword):
    pages = get_page_count(keyword)

    results = []

    for page in range(pages):
        options = Options()
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")

        browser = webdriver.Chrome(options=options)
        base_url = "https://kr.indeed.com/jobs"
        print(f"Request Page {page+1}")
        browser.get(f"{base_url}?q={keyword}&start={page*10}")

        soup = BeautifulSoup(browser.page_source, "html.parser")
        job_list = soup.find("ul", class_="jobsearch-ResultsList")
        jobs = job_list.find_all("li", recursive=False)
        for job in jobs:
            is_mosaic_zone = job.find("div", class_="mosaic-zone", recursive=False)
            if is_mosaic_zone == None:
                anchor = job.find("h2", class_="jobTitle").find("a")
                link = anchor["href"]
                title = anchor.find("span")
                company = job.find("span", class_="companyName")
                region = job.find("div", class_="companyLocation")

                job_data = {
                    "job_title": title.string.replace(",", " "),
                    "company_name": company.string.replace(",", " "),
                    "region": region.string.replace(",", " "),
                    "link": f"https://kr.indeed.com{link}",
                }

                results.append(job_data)
        browser.close()

    return results
