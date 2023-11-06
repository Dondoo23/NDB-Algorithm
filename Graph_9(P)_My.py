n = int(input())
arr = [0] * (n+1)

for i in range(1, n+1):
    inp = list(map(int, input().split()))
    
    # 마지막은 -1로 끝임을 나타내므로 의미X
    inp.pop()
    # 첫 원소는 현재 강의의 강의시간을 나타내므로 따로 빼줌
    last = inp.pop(0)

    # 나머지 원소들은 선수 강의들의 번호
    if not inp: # 선수 강의들이 존재하지 않으면 현재 강의의 강의시간만
        arr[i] = last
    else: # 선수 강의들이 존재하면 선수 강의들을 쭉 둘러보고 가장 강의시간이 긴 선수강의만 선택
          # 동시에 강의를 들을 수 있으므로 가장 긴 선수강의만 확인하면 된다
        n_arr = []
        for j in inp:
            n_arr.append(arr[j])
            max_val = max(n_arr)
        arr[i] = max_val + last # 가장 긴 선수강의의 시간과 현재 강의 시간을 더해서
        
    print(arr[i])