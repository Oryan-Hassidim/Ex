
def up_and_right_core(so_far, n, k, lst):
    if n == 0 == k:
        lst.append(so_far)
        return
    if n > 0:
        up_and_right_core(so_far + 'u', n - 1, k, lst)
    if k > 0:
        up_and_right_core(so_far + 'r', n, k - 1, lst)

def up_and_right(n,k, lst):
    up_and_right_core('', n, k, lst)
    
lst = []
up_and_right(1, 1, lst)
print(*lst, sep='\n', end='\n\n')

lst.clear()
up_and_right(1, 2, lst)
print(*lst, sep='\n', end='\n\n')

lst.clear()
up_and_right(2, 1, lst)
print(*lst, sep='\n', end='\n\n')

lst.clear()
up_and_right(2, 2, lst)
print(*lst, sep='\n', end='\n\n')
