# sys 이용해 입력 시간 줄이기
import sys
num = int(sys.stdin.readline())

# list는 벡터처럼 추가할 때 마다 메모리 증가
# 이 문제는 메모리가 매우 낮아서 sort() O(nlogn)보다 적은 시간 복잡도 필요
# 정렬 이용하지 않고 배열만 사용하여 O(n)으로 메모리 최대한 적게 쓰는 문제
# arr = list()
arr = [0] * 10001  # [0 for _ in range(10000)] 동일한 정적배열 선언 방법

# 입력
for i in range(num):
    arr[int(sys.stdin.readline())] += 1

# 정렬 원소 출력
for i in range(10001):
    for j in range(arr[i]):
        sys.stdout.write(str(i) + '\n') # 문자열 출력이 디폴트이므로 정수를 문자로 변환


