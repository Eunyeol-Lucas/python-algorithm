P = int(input())
for i in range(P):
    arr = list(map(int, input().split()))

    T, arr = arr[0], arr[1:]

    cnt = 0
    for i in range(1, 20):
        for j in range(i):
            if arr[i] < arr[j]:
                # 현재 숫자가 앞에 숫자 중에 자기보다 큰 숫자가 있는 경우 자리를 바꿔줌
                tmp = arr[i]
                arr.pop(i)
                arr.insert(j, tmp)
                cnt += i - j
                break
    print(f'{T} {cnt}')


'''
4
1 900 901 902 903 904 905 906 907 908 909 910 911 912 913 914 915 916 917 918 919
2 919 918 917 916 915 914 913 912 911 910 909 908 907 906 905 904 903 902 901 900
3 901 902 903 904 905 906 907 908 909 910 911 912 913 914 915 916 917 918 919 900
4 918 917 916 915 914 913 912 911 910 909 908 907 906 905 904 903 902 901 900 919
'''
