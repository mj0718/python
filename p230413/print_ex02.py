note = open('D:\\webservice\\python\\p230413\\test.txt', 'w') #절대 경로의 쓰기 모드로

print('one')
print('two', file=note)
print('three')

note.close() #자원 해제