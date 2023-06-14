import requests
from bs4 import BeautifulSoup


def get_citations_needed_count(url):
    """
    Scrape a Wikipedia page and return the number of citations needed.

    Args:
        url: The URL of the Wikipedia page.

    Returns:
        The number of citations needed as an integer.
    """
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    citations_needed = soup.find_all(text="citation needed")
    return len(citations_needed)


def get_citations_needed_report(url):
    """
    Scrape a Wikipedia page and generate a report of passages needing citations.

    Args:
        url: The URL of the Wikipedia page.

    Returns:
        A string containing the report with each citation listed in the order found.
    """
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    citations_needed = soup.find_all(text="citation needed")
    report = ""
    for citation in citations_needed:
        passage = citation.find_parent('p').text
        report += f"Citation needed for: \"{passage}\"\n\n"
    return report


# Example usage
url = "https://en.wikipedia.org/wiki/History_of_Mexico"

citation_count = get_citations_needed_count(url)
print(f"Number of citations needed: {citation_count}\n")

citation_report = get_citations_needed_report(url)
print("Citations needed:\n")
print(citation_report)
