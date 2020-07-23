from bs4 import BeautifulSoup
import requests
import pprint
import json

page = requests.get("https://www.misteraladin.com/train/search-train-result?type=1&origin=JKT-ALL&destination=BD-ALL&departDate=2020-07-25&returnDate=2020-07-25&adult=1&child=0&infant=0")
soup = BeautifulSoup(page.content, "lxml")
# print(soup.prettify())
class_list = soup.find("div", {'class': 'train_list_result_wo'})
# print(class_list)
list_hasil=[]
for awal in class_list.findAll("div",{'class':'panel panel-default br-8'}) :
    for awal2 in awal.findAll('div',{'class':'col-md-10 hor-clear col-xs-12'}):
    # print(awal)
        for awal1 in awal2.findAll("p", {'class': 'mb-0 res-xs'}):
            maskapai = awal1.find('b').get_text()
        for kelas1 in awal.find_all("p",{'class': 'res-xs-bottom'}):
            hasil_kelas = kelas1.get_text()
        for jam1 in awal.find_all("p",{'class': 'text-bold'}):
            hasil_jam = jam1.find('b').get_text()
        for sampai1 in awal.find_all("p", {'class': 'text-bold f-r-xs'}):
            hasil_sampai = sampai1.find('b').get_text()
        for harga1 in awal.find_all("p", {'class': 'text-bold text-orange res-price-xs'}):
            hasil_harga = harga1.find('b').get_text()
        for status in awal.find_all("p", {'class': 'text-danger mb-0 pull-right'}):
            hasil_status = status.get_text()

        # print("Maskapai :\t"+maskapai)
        # print("Kelas :\t"+hasil_kelas)
        # print("Keberangkatan :\t"+hasil_jam)
        # print("Sampai :\t"+hasil_sampai)
        # print("Biaya :\t"+hasil_harga)
        # print("Status :\t"+hasil_status)
        #
        # print()
        my_dict = {
            "Maskapai": maskapai,
            "Kelas": hasil_kelas,
            "Keberangkatan": hasil_jam,
            "Sampai": hasil_sampai,
            "Biaya": hasil_harga,
            "Status": hasil_status
         }
        list_hasil.append(my_dict)
pprint.pprint(list_hasil)
with open('crawling_html.json', 'w') as outfile:
    json.dump(list_hasil, outfile)