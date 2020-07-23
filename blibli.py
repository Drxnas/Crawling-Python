import requests
import json
import pprint

list_product = []
new = []
ins = 0
for i in range(19):
    url = "https://www.blibli.com/backend/search/products?page="+str(i)+"&start=0&category=HA-1000002&sort=7&channelId=web&showFacet=true"

    payload = {}
    headers = {
        'Cookie': 'Blibli-User-Id=a0544ebe-6d83-4052-b729-aea314b173f4; Blibli-Is-Member=false; Blibli-Is-Remember=false; Blibli-Session-Id=386b5a30-aff8-4acf-be96-3bb672d8ef64; Blibli-Signature=6a26d883c39515b2e5bf212c865d02ab285ee6b7; bm_sz=2F9E20ED9C08A5E8683B254C7D742E62~YAAQPts4fcI7eXdzAQAARENPegiFDiyYo3GaYuisysJilFnBrHWnn+EUonPaBq57W+74glKOWtWCspu4L1t8FTCeL7nGNH5LnWfDMpiffk9Mqnzoob6XHxVYY34U8jbHc9FISkjU9lBHrCwt3sMZCMfo9L2NBC4ipfWIHFYb29XxD43ovKX20rapPmN5q1M=; _abck=C2CA53CF0BD9959FBC8162A9730F5FCF~-1~YAAQPts4fRA9eXdzAQAAFFZRegS3TOF/Obfd+uqSpmshAAfF1ZPSpsoPbFvmbWmY5odPFChhp+akfTlGLgbpW+ZvCrhpSrD/mPOTZ7pJBkpPrxzaX8X/iHqJ0dZxfD75Kl/f8PoZ1D6QRV7oZclwcJqbEz53EOLGZVBLmNgxYWYxCbkDfdCmw98zvfm5LaE2qIW9DQWnTWhHAagHQoygxPJKt+gszVvSKpHSGq4cdUNTJ3Vw15HEezBRQBSHDppZkfHHtO/P3eWQMim/baLCgvzv9KAbTOtzC9KzHSJolyXx6smHt+hjZ9bBiJReoUZGs3b54LCV+g==~0~-1~-1; ak_bmsc=E15D22C558DAD7C8668FD07A7F91268B17201D6D78520000B648195F266EF475~plmOAqZaoSlDBTcQeuKs4eUlatXZcjZkDdjmlMBSpzjZjFTUtOV8TkVivr84MZDiFDPgeq2xPWhi4dsUlspkwTJGuMJdb7nb+rsz9Gh2ybsbNBdBj8GJ6RQ00P7a6mFh6UYnf1drYW+v64p6ffnSFhHVLFu2SPqyaIRnxkWhRtensYdO6d8hPOv7A5E9OrB9YkY2pUs04363dasuIdBK5A/wfbWds7u6jHXOHQqaUEgTk='
    }

    response = requests.request("GET", url, headers=headers, data = payload)

    # print(response.text.encode('utf8'))


    data = response.json()
    # print(data[])
    dt = data["data"]["products"]
    print(dt)

    for product in dt :
        # product_name = product["name"]
        # print(product_name)
        # new.append(name)
        # product_price = product["price"]["minPrice"]
        # new.append(price)
        ins+=1
        # my_dict = {
        #     "name": product_name,
        #     "price": product_price
        # }
        list_product.append(product)
# print(j)

#
# jsonData = json.dumps(new)
pprint.pprint(json.dumps(list_product))
print(ins)