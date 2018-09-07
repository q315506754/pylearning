import pdb

# python -m pdb debugger2.py
s = '0'
n = int(s)
# 用命令c继续运行
pdb.set_trace()  # 运行到这里会自动暂停
print(10 / n)
