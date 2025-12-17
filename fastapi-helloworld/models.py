{
	"source": $.source,
    "accountId":$.customer.bill.partyId,
    "id_billTo": $.customer.bill.addressId,
    "id_shipTo":$.customer.ship[0].addressId,
    "id_billToSfdcId": $.customer.bill.addressSfdcId,
     "ReceivedShipToAddressOnly":$.customer.bill.receivedShipToAddressOnly default false,
    "id_shipToSfdcId":$.customer.ship[0].addressSfdcId,
    "poNumber":$.poNumber,
    "refPriceBook":"T&F_Pricebook",
    "SalesChannel":$.channel,
    "OrderDeliveryMethod":"Preferred%20Shipping%20Method",
    "products":$.lines map(items,index) -> if(items.id=="0123456789") items.id else items.externalId,
   "pricebookEntries": $.lines map (item,index)-> (if(item.id=="0123456789") item.id else item.externalId) ++ "T&F_Pricebook" ++ $.currencyIsoCode,
    "recordType": p('secure::sf.requestPayload.recordType')
}