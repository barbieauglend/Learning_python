n = int(input())

input_list = map(int, input().split())
print(sorted(list(set(input_list)))[-2])