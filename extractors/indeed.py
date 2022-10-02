from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def extract_indeed_jobs(keyword, where="Melbourne+VIC"):
  base_url = "https://au.indeed.com/jobs?"
  url = f"{base_url}q={keyword}&limit=50&l={where}"  

  options = Options()
  options.add_argument("--no-sandbox")
  options.add_argument("--disable-dev-shm-usage")
  
  browser = webdriver.Chrome(options=options)
  browser.get(url)
  
  results = []
  soup = BeautifulSoup(browser.page_source, "html.parser")
  job_list = soup.find("ul", class_="jobsearch-ResultsList")
  jobs = job_list.find_all("li", recursive=False)
  for job in jobs:
    zone = job.find("div", class_="mosaic-zone")
    if zone == None:
      anchor = job.select_one("h2 a")
      link = anchor["href"]
      position = anchor.find("span")
  
      company_info = job.find("div", class_="companyInfo")
      company = company_info.find("span", class_="companyName")
      region = company_info.find("div", class_="companyLocation")
      job_data = {
        'link': f"https://au.indeed.com{link}",
        'company': company.string,
        'region': region.string,
        'position': position.string
      }
      results.append(job_data)
  return results