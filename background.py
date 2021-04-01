# import cv2
#
# img = cv2.imread('yellow.jpg')
# encode_param=[int(cv2.IMWRITE_JPEG_QUALITY),1]
# result,encimg=cv2.imencode('.jpg',img,encode_param)
# if False==result:
#     print ('could not encode image!')
#     quit()
#
# decimg=cv2.imdecode(encimg,1)
# cv2.imshow('result', decimg)
# cv2.waitKey(0)
# cv2.imwrite('decimg2.jpg',decimg)


from urllib.request import urlopen
from bs4 import BeautifulSoup
import openpyxl
import requests
import urllib3

excel_file = openpyxl.Workbook()
excel_sheet = excel_file.active
excel_sheet.column_dimensions['B'].width = 200

num = 0
excel_sheet.append(['번호', '제목'])
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
res=requests.get("홈페이지 주소", verify=False).text
requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)
soup = BeautifulSoup(res, "html.parser")

#print(soup.find_all())
print("a", soup.find_all( class_='fl'))
data = soup.find_all('a', class_='fl')
for item in data:
    num += 1
    excel_sheet.append([num, item.get_text()])
    print(item.get_text())

cell_A1 = excel_sheet['A1']
cell_A1.alignment = openpyxl.styles.Alignment(horizontal="center")

cell_B1 = excel_sheet['B1']
cell_B1.alignment = openpyxl.styles.Alignment(horizontal="center")

excel_file.save('정리.xlsx')
excel_file.close()