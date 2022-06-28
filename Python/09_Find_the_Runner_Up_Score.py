res = list(arr)
sec = min(res)
for i in range(n):
  if sec <= res[i] < max(res):
    sec = res[i]

print(sec)
