from extractors.woori import extract_woori_jobs
# from extractors.wwr import extract_wwr_jobs
# from extractors.indeed import extract_indeed_jobs

# print("WWR JOBS:  ")
# wwr_jobs = extract_wwr_jobs("python");
# print(wwr_jobs)

# print("indeed JOBS:  ")
# indeed_jobs = extract_indeed_jobs("python");
# print(indeed_jobs)

woori_jobs = extract_woori_jobs("")
print(woori_jobs)