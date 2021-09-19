import psutil

p = psutil.Proces(37189)
print(p.num_fd())