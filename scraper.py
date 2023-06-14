import requests
from bs4 import BeautifulSoup

def get_citations_needed_count(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    citations_needed = []
    for p in soup.find_all("p"):
        if p.find("b", text="Citation needed"):
            citations_needed.append(p)

    return len(citations_needed)

def get_citations_needed_report(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    citations_needed = []
    for p in soup.find_all("p"):
        if p.find("b", text="Citation needed"):
            citations_needed.append(p)

    report = ""
    for citation in citations_needed:
        report += citation.text + "\n"

    return report

if __name__ == "__main__":
    url = "https://en.wikipedia.org/wiki/History_of_Mexico"
    count = get_citations_needed_count(url)
    report = get_citations_needed_report(url)

    print("Number of citations needed:", count)
    print("Report:", report)