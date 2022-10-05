# from extractors.woori import extract_woori_jobs
from extractors.wwr import extract_wwr_jobs
from extractors.indeed import extract_indeed_jobs
from extractors.file import save_to_file

# print("WOORI JOBS:  ")
# woori_jobs = extract_woori_jobs("")
# print(woori_jobs)

keyword = input("What do you want to search for? ")

indeed_jobs = extract_indeed_jobs(keyword)
wwr_jobs = extract_wwr_jobs(keyword)
jobs = indeed_jobs + wwr_jobs

save_to_file(keyword, jobs)