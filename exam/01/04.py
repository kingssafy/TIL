# 파일명 변경 금지
def cipher(word, n):
    # 아래에 코드를 작성하시오.
    # word는 모두 소문자로만 구성되어 있습니다.
    # n은 양의 정수입니다.
    # 암호화된 문자열을 반환합니다.
    result = ""
    for character in word:

        #소문자로 구성된 알파벳을 받아올때 해당 아스키코드값에서
        #a의 아스키 코드 값을 빼서
        # {a:0, b:1,-,-,--, z:25} 이렇게 배정되게합니다
        #그리고 오른쪽으로 밀어낼 거리n 을 각 문자열마다 더해주고 그 더해준값에서
        # 26으로 나눠 준 나머지 만을 구해냅니다
        # 왜냐하면 z: 25인데 여기다가 1을 더하면 26으로 이상한 문자가 나올 수 있기때문에
        # % 26을 취해주어서 a~z 의 영역내에 있을 수 있게 합니다.
        # for instance) 25 + 1은 26으로 알파벳 소문자 영역을 벗어나는데
        # %26 을취해주면 0이되면서 기대했던값인 a의 숫자가됩니다.
        #그리고 마지막에 ord('a') 값을 더해주고 chr을 씌워주면 원하는대로 딱 변형이됩니다.
        result += chr((ord(character)-ord('a') + n)%26 + ord('a'))
        #빈 문자열 result를 정의한 후 += operator로 문자열을 하나씩 앞에서 부터 쌓ㅇ아줬습니다
    return result
        #그리고 쌓인문자열리턴

# 아래의 코드는 수정하지마세요. 
if __name__ == '__main__':
    print(cipher('apple', 1))
    print(cipher('apple', 27))
    print(cipher('zoo', 2))