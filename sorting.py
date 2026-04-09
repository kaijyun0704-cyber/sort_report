import time
import random

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key

def quick_sort(arr):
    if len(arr) <= 1: return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def merge_sort(arr):
    if len(arr) <= 1: return arr
    mid = len(arr) // 2
    L = merge_sort(arr[:mid])
    R = merge_sort(arr[mid:])
    res, i, j = [], 0, 0
    while i < len(L) and j < len(R):
        if L[i] < R[j]: res.append(L[i]); i += 1
        else: res.append(R[j]); j += 1
    res.extend(L[i:]); res.extend(R[j:])
    return res

if __name__ == "__main__":
    print("--- 實驗開始 ---")
    sizes = [1000, 3000, 5000]
    for n in sizes:
        print(f"\n數據量 n = {n}:")
        data = [random.randint(0, 10000) for _ in range(n)]
        # 測試各排序法
        for func in [bubble_sort, selection_sort, insertion_sort, quick_sort, merge_sort]:
            temp = data.copy()
            start = time.time()
            if func.__name__ in ['quick_sort', 'merge_sort']:
                temp = func(temp)
            else:
                func(temp)
            print(f"{func.__name__}: {time.time()-start:.4f} 秒")
    print("\n--- 實驗結束 ---")