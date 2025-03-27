import subprocess

# 替换为实际的IP地址、用户名和密码
ip_address = '71.49.252.82'
username = 'root'
password = 'Huawei@123'
command = 'ls -l'

# 构造SSH命令
ssh_command = f"ssh {username}@{ip_address} '{command}'"

# 执行SSH命令
result = subprocess.run(ssh_command, shell=True, capture_output=True, text=True)

# 输出结果
print("标准输出:", result.stdout)
print("标准错误:", result.stderr)