from googleapiclient.discovery import build
import requests
import re
import time

API_KEY = 'AIzaSyC4Mr7wjKfREnX9VmxNMFuiUt4XyelCTNg'
SEARCH_ENGINE_ID = '268aaf8850a3440fc'



def google_search(query, api_key, cse_id, **kwargs):
    service = build("customsearch","v1",developerKey=api_key)
    res = service.cse().list(q=query,cx=cse_id,**kwargs).execute()
    return res['items']



def extract_emails(text):
    # Regular expressions for different types of email domains
    yahoo_pattern = r'\b[A-Za-z0-9._%+-]+@yahoo\.com\b'
    gmail_pattern = r'\b[A-Za-z0-9._%+-]+@gmail\.com\b'
    custom_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

    # Find all matches for each pattern
    yahoo_emails = re.findall(yahoo_pattern, text)
    gmail_emails = re.findall(gmail_pattern, text)
    custom_emails = re.findall(custom_pattern, text)

    # Combine all email types into one list
    emails = yahoo_emails + gmail_emails + custom_emails

    return emails


def search_and_extract_emails(query,num_results=10):
    all_emails = set()
    start_index = 1
    while len(all_emails) < num_results:
           results = google_search(
                     query,
                     API_KEY,
                     SEARCH_ENGINE_ID,
                     num = min(10, num_results - len(all_emails)),
                     start=start_index
                     )
           if not results:
              break
           print(results)
           for result in results:
               emails = extract_emails(result['link'])
               all_emails.update(emails)
               time.sleep(1)

           start_index += 10
    return list(all_emails)[:num_results]



query = "site:instagram.com -inurl:(explore|directory|p|reel|stories|guide) -intitle:(posts|followers|following) -intitle:""(official)" "-intitle:""(verified)" "-""Follow us" "+""travel photographer" "+""landscape" "+""wildlife" "-""wedding" "-""portrait"
result = search_and_extract_emails(query,num_results=10)
print(result)
