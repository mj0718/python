# 문자열 함수:format
# '문자열'.format()
# '문자열{}'.format(값)

apple, banana = 5, 7
print('사과가', apple, '개 있고, 바나나는', banana, '개 있다.')
print('사과가 %d개 있고, 바나나는 %d개 있다.'%(apple, banana))
#print('사과가 %d개 있고, 바나나는 %d개 있다.'%(apple)) #서식문자는 여러번 사용 불가능
print('사과가 %d개 있고, 바나나는 %d개 있다.'%(apple, apple))

print('사과가 {}개 있고, 바나나는 {}개 있다.'.format(apple, banana))
print('사과가 {0}개 있고, 바나나는 {1}개 있다.'.format(apple, banana))
print('사과가 {0}개 있고, 바나나는 {0}개 있다.'.format(apple)) #여러번 쓸 수 있음

# f문자열 포맷팅: python 3.6부터 지원
print(f'사과가 {apple}개 있고, 바나나는 {banana}개 있다.')

fruit = f'사과가 {apple}개 있고, 바나나는 {banana}개 있다.'
print('[fruit]', fruit)

print(f'{apple}')
print(f'{apple:7}')
print(f'{apple:07}')
print(f'{apple:<7}') #왼쪽 정렬
print(f'{apple:>7}') #오른쪽 정렬
print(f'{apple:^7}') #가운데 정렬
print(f'{apple:0^7}') 
print(f'{apple:#^7}') 
print(f'{apple:!^7}') 