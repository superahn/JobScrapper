
from requests import get
from bs4 import BeautifulSoup

def extract_woori_jobs(keyword):  
  base_url = "https://woorimel.com/board/melbourne-jobs?category_id=1&sfield=post_both&skeyword="  
  response = get(f"{base_url}{keyword}")
  if response.status_code != 200:
    print("Can't search!")
  else:
    results = []
    soup = BeautifulSoup(response.text, 'html.parser')
    job_list = soup.find('div', class_="board-list-rows")
    jobs = job_list.find_all("div", class_="board-list-row")
    for job in jobs:
      subject = job.find("div", class_="board-list-article-subject")
      anchors = subject.find_all('a')
      anchor = anchors[1]
      link = anchor['href']
      title = anchor['title']

      content = job.find("div", class_="board-list-article-content")
      content_anchor = content.find('a')
      title = content_anchor.string

      job_data= {
        'link': link,
        'position': title,
        'content': content.get_text()
      }
      results.append(job_data)
    return results
