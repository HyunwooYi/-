import pickle

filepath='score.bin'


def save(s):
    with open(filepath, 'wb') as file:
            pickle.dump(s, file)


def load():
    with open(filepath, 'rb') as file:
            d = pickle.load(file)

    return d


def input_scores():
    s = []
    i = 1
    while True:
        n = int(input(f'#{i}?'))
        if n<0:
            break
        s.append(n)
        i+=1
    return s

def get_average(s):
    total = 0
    for n in s:
        total += n
    return total / len(s)

def show_scores(d):
    for n in d:
        print(n, end=' ')
    print()

# 주 프로그램
print('[점수입력]')
scores = input_scores()
# 저장하기
save(scores)

print('\n[점수출력]')
print('개인점수:', end='')
show_scores(scores)

avg = get_average(scores)
print(f'평균:{avg:.1f}')
    

print('\n[파일읽기]')
d = load()
print('\n[점수출력]')
print('개인점수:', end='')
show_scores(d)

    
