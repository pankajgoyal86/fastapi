import requests


URL = "https://api.uat.taylorfrancis.net/uat/api/v1/orderhandler/edi/orders"

header = {
    "client_id":"b5bf29925b8a43e4949b0ad47aa9eb8b",
    "client_secret":"16aFc88C0523476C86A3cB9a7282b02E"
}

body = {
    "orders": [
        {
            "channel": "EDI",
            "source": "EDI",
            "type": "Regular",
            "receivedDateTime": "2025-04-21T14:08:51.126Z",
            "poNumber": "POAut75763_1",
            "poDate": "2025-04-21",
            "currencyIsoCode": "USD",
            "preferences": {
                "allowBackorder": False,
                "futureShipDate": "2025-04-21",
                "customerCancelRequestDate": "2025-04-23"
            },
            "customer": {
                "ship": [
                    {
                        "san": "7801564"
                    }
                ],
                "bill": {
                    "san": "AMAZON"
                }
            },
            "lines": [
                {
                    "sequenceId": "1",
                    "quantity": 1,
                    "quantityType": "Each",
                    "salePrice": 100.75,
                    "externalId": "9780367355913",
                    "externalIdType": "ISBN13",
                    "type": "Order Product"
                },
                {
                    "sequenceId": "2",
                    "quantity": 1,
                    "quantityType": "Each",
                    "salePrice": 100.75,
                    "externalId": "9780415210843",
                    "externalIdType": "ISBN13",
                    "type": "Order Product"
                },
                {
                    "sequenceId": "3",
                    "quantity": 1,
                    "quantityType": "Each",
                    "salePrice": 100.75,
                    "externalId": "9781032204406",
                    "externalIdType": "ISBN13",
                    "type": "Order Product"
                }
            ]
        }
    ]
}

resp = requests.post(URL, json=body, headers=header)
resp.raise_for_status()
print(resp.json())
