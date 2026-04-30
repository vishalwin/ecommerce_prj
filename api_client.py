import requests
from config import BASE_URL, PROJECT_ID, HEADERS

class APIClient:
    def __init__(self):
        self.base_url = BASE_URL
        self.project_id = PROJECT_ID
        self.headers = HEADERS


    def endpoint(self, record_id=None):
        url = f"{self.base_url}/projects/collections/products/records"
        if record_id:
            url = f"{url}/{record_id}"
        return f"{url}?project_id=={self.project_id}"
        
    def send_request(self, method, record_id=None, payload=None):
            url = self.endpoint(record_id)
            return requests.request(method=method, url=url, headers=self.headers,
                                     json=payload)
    def get_product(self):
        url = f"{BASE_URL}/collections/products/records?project_id={self.project_id}"
        return requests.get(url, headers=self.headers)
    

    def update_product(self, record_id, payload):
        return self.send_request("PUT", record_id=record_id,payload=payload)
    
    def delete_product(self, record_id):
        return self.send_request("DELETE", record_id=record_id)
    def create_product(self, payload):
         url = f"{BASE_URL}/collections/products/records?project_id={self.project_id}"
         return requests.post(url, headers=self.headers, json=payload)
    def header_method():
        pass