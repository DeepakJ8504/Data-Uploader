import csv
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

import requests

from validator import is_valid_customer_data, data_type

api_url = "https://cromaapi-612730900229.asia-south1.run.app/upload/"

headers = {
    'Content-Type': 'application/json',
    'cmId': '1006883'  # if needed
}
BATCH_SIZE = 3000

def convert(file: str, stream: str = "val"):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_dir, file)
    data = []

    with open(file_path, mode='r', encoding='utf-8-sig') as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            data.append(row)

    if stream == "val":
        return validate_data(data)
    else:
        return multi_thread_convert(data)

def chunked(iterable):
    for i in range(0, len(iterable), BATCH_SIZE):
        yield iterable[i:i + BATCH_SIZE]

def multi_thread_convert(data: list):
    chunk_data = chunked(data)

    results = []
    with ThreadPoolExecutor(max_workers=1) as executor:
        futures = [executor.submit(send_data, chunk, idx+1) for idx, chunk in enumerate(chunk_data)]

        # Wait for all uploads to finish
        for future in as_completed(futures):
            results.append(future.result())

    return all(results)

def send_data(chunk: list, idx: int):
    try:
        time.sleep(5)
        response = requests.post(api_url, json={"data": chunk}, headers=headers)
        print("Status Code:", response.status_code, idx)
        time.sleep(5)
        return response.ok
    except Exception as e:
        print(e)


def validate_data(chunk: list):
    try:
        response = is_valid_entries(chunk)
        print("Status Code:", response)
        return response
    except Exception as e:
        print(e)

def is_valid_entries(chunk: list):
    try:
        data_type(chunk[0])
        return is_valid_customer_data(chunk)
    except Exception as e:
        print(e)
