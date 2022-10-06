from requests import get
from bs4 import BeautifulSoup

def extract_wwr_jobs(keyword):
  base_url = "https://weworkremotely.com/remote-jobs/search?term="  
  response = get(f"{base_url}{keyword}")
  if response.status_code != 200:
    print("Can't search!")
  else:
    results = []
    soup = BeautifulSoup(response.text, 'html.parser')
    jobs = soup.find_all('section', class_="jobs")
    for job_section in jobs:
      job_posts = job_section.find_all('li')
      job_posts.pop(-1)
      for post in job_posts:
        anchors = post.find_all('a')
        anchor = anchors[1]
        link = anchor['href']
        # company, kind, region = anchor.find_all('span', class_='company')
        company_info = anchor.find_all('span', class_='company')
        company = company_info[0]
        kind = company_info[1]

        region = anchor.find('span', class_='region company')    
        title = anchor.find('span', class_='title')
        job_data= {
          'link': f"https://weworkremotely.com{link}",
          'company': company.string,
          'region': region.string if region != None else "",
          'position': title.string
        }
        results.append(job_data)
    return results