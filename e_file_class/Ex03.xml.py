import xml.etree.ElementTree as et

# tree = et.ElementTree(file='./data/temp2.xml')
# root = tree.getroot()
# print('root:', root.tag)
#
# for child in root:
#     #print(child.tag)
#     for grandchild in child:
#         print(child.attrib)
#         print(grandchild.tag + "/" +grandchild.text)


# sample.xml 파일을 읽어서 항목별 총합 구하기
print('===sample.xml 파일을 읽어서 항목별 총합 구하기===')
tree1 = et.ElementTree(file='./data/sample.xml')
root1 = tree1.getroot()
print('root:', root1.tag) #items

sum = 0
for fruit, price, count in root1:
    sum = int(price.text) * int(count.text)
    print('{}의 합산 결과 : '.format(fruit.text), sum)
# print('{}의 총합 : '.format(root1[0][0].text),(int(root1[0][1].text) * int(root1[0][2].text)))
# print('{}의 총합 : '.format(root1[1][0].text),(int(root1[1][1].text) * int(root1[1][2].text)))
# print('{}의 총합 : '.format(root1[2][0].text),(int(root1[2][1].text) * int(root1[2][2].text)))
# print('{}의 총합 : '.format(root1[3][0].text),(int(root1[3][1].text) * int(root1[1][2].text)))

