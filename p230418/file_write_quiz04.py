''' 
[문제] 사용자가 입력한 데이터가 파일에 저장되도록 하시오.
파일이 없으면 새로 생성하고, 기존에 있는 파일이면 데이터가 추가되어 저장
파일명 : userInputData.txt
입력 데이터가 없으면 입력 종료
'''

# file = open(r'D:\webservice\python\p230418\userInputData.txt', 'a', encoding='UTF-8') 
# while True:
#     data = input('기록할 데이터 입력 >> ')
#     if not data:
#         break
#     file.write(data+'\n')
# file.close()

#with open('D:/webservice/python/p230418/userInputData.txt', 'a', encoding='UTF-8') as user:
#with open(r'D:\webservice\python\p230418\userInputData.txt', 'a', encoding='UTF-8') as user:
with open('D:\\webservice\\python\\p230418\\userInputData.txt', 'a', encoding='UTF-8') as user:
    while True:
        data = input('기록할 데이터 입력 >> ')
        if data=='':
            break
        user.write(data + '\n')