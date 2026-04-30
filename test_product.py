from api_client import APIClient
from payload import product_payload

def test_get_product():
    client = APIClient()
    response = client.get_product()
    print(response.json())
    assert response.status_code == 200

def test_create_product():
    client = APIClient()
    payload = product_payload("Laptop", 999.99)
    response = client.create_product(payload)

    print(response.json())

    print(response.status_code)
    assert response.status_code in [200, 201]

def test_update_product():
    client = APIClient()
    payload = product_payload("samsung s24", 999.99)
    create_response = client.create_product(payload)

    print(create_response.json())
    
    
    record_id = create_response.json().get("data",{}).get("id")
    print("created record ID:",    record_id)
    assert record_id is not None, "Failed to create product, no record ID returned"
    
    update_response=client.update_product(record_id, product_payload("samsung fold 7", 2999.99))
    
    print(update_response.json())
    assert update_response.status_code == 200
    