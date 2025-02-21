防止远程登录掉线
[root@localhost ~]# TMOUT=0
查看文件哈希值
[root@localhost ~]# sha256sum anaconda-ks.cfg
aeed1febf0fcf3d4a42757f6f0f137d6b675525a87b4ba675db8ffe40c40e34c  anaconda-ks.cfg
linux命令行快捷键
  Ctrl + U 向前清除   Ctrl + K 向后清除    Ctrl+ a 命令的行首   ctrl + e   命令的行尾
vim编辑器快捷键
  0 行首 e 行尾 gg 文档行首 G 文档行尾
编辑shell脚本小技巧
  set -x   //写在脚本里边执行的时候可以顺便检查脚本的错误和显示执行过程
  set -e   //表示任何语句执行的结果不是true，则应该退出。防止错误像滚雪球一样继续变大
$# 表示脚本程序的命令参数个数活函数的参数个数
$$ 表示该脚本程序的进程号，常用于生成文件名唯一的临时文件
$? 表示脚本程序或函数的返回状态值，正常为0，否则为非零的错误号。
$* 表示所有的脚本参数或函数参数
$! 表示最近一个在后台运行的进程的进程号
暴力卸载
  fusermount -zu /dev/sda1
重新生成grub.cfg文件
  grub2-mkconfig -o /boot/grub2/grub.cfg
Ctrl+z 直接将正在编辑的文件丢到后台
fg 重新恢复到前台继续编辑（foreground）
记录linux中的一举一动  /var/log/secrue 或者/var/log/messages
查看Linux系统支持的语言
[root@localhost ~]# locale -a
查看Linux系统显示年月日
[root@localhost ~]# date +%Y%m%d
20250220
查看Linux系统的时分秒
[root@localhost ~]# date +%H%M%S
085118
date -s 20080523 //设置成20080523，这样会把具体时间设置成空00:00:00
date -s 01:01:01 //设置具体时间，不会对日期做更改
[root@localhost ~]# echo 01234 | tr '0-9' 'a-z'
abcde
[root@localhost ~]# echo "hello world" | sed 's/world/universe/'
hello universe
强制删除rpm包
[root@localhost ~]# rpm -e --nodeps gdm-3.28.3-39.el8.x86_64
查看系统启动项
[root@localhost ~]# sudo systemctl list-unit-files --type=service
查看服务的详细信息
[root@localhost ~]# sudo systemctl cat NetworkManager.service
# /usr/lib/systemd/system/NetworkManager.service
[Unit]
Description=Network Manager
Documentation=man:NetworkManager(8)
Wants=network.target
After=network-pre.target dbus.service
Before=network.target network.service

[Service]
Type=dbus
BusName=org.freedesktop.NetworkManager
ExecReload=/usr/bin/dbus-send --print-reply --system --type=method_call --dest=org.freedesktop.NetworkManager /org/freedesktop/NetworkManager org.freedesktop.NetworkManager.Reload uint32:0
#ExecReload=/bin/kill -HUP $MAINPID
ExecStart=/usr/sbin/NetworkManager --no-daemon
Restart=on-failure
# NM doesn't want systemd to kill its children for it
KillMode=process
#CapabilityBoundingSet=CAP_NET_ADMIN CAP_DAC_OVERRIDE CAP_NET_RAW CAP_NET_BIND_SERVICE CAP_SETGID CAP_SETUID CAP_SYS_MODULE CAP_AUDIT_WRITE CAP_KILL CAP_SYS_CHROOT

# ibft settings plugin calls iscsiadm which needs CAP_SYS_ADMIN (rh#1371201)
CapabilityBoundingSet=CAP_NET_ADMIN CAP_DAC_OVERRIDE CAP_NET_RAW CAP_NET_BIND_SERVICE CAP_SETGID CAP_SETUID CAP_SYS_MODULE CAP_AUDIT_WRITE CAP_KILL CAP_SYS_CHROOT CAP_SYS_ADMIN

ProtectSystem=true
ProtectHome=read-only

[Install]
WantedBy=multi-user.target
Also=NetworkManager-dispatcher.service

# We want to enable NetworkManager-wait-online.service whenever this service
# is enabled. NetworkManager-wait-online.service has
# WantedBy=network-online.target, so enabling it only has an effect if
# network-online.target itself is enabled or pulled in by some other unit.
Also=NetworkManager-wait-online.service
查看Linux网卡的速度
[root@localhost ~]# watch -n 1 ifconfig
Linux系统显示ens192网络接口详细信息
[root@localhost ~]# ethtool eth0
Settings for ens192:
        Supported ports: [ TP ]
        Supported link modes:   1000baseT/Full
                                10000baseT/Full
        Supported pause frame use: No
        Supports auto-negotiation: No
        Supported FEC modes: Not reported
        Advertised link modes:  Not reported
        Advertised pause frame use: No
        Advertised auto-negotiation: No
        Advertised FEC modes: Not reported
        Speed: 10000Mb/s #显示网络接口的当前传输速度，如1000Mb/s表示千兆以太网
        Duplex: Full
        Port: Twisted Pair #显示网络接口的物理端口类型，如twisted pair表示双绞线。
        PHYAD: 0
        Transceiver: internal
        Auto-negotiation: off
        MDI-X: Unknown
        Supports Wake-on: uag
        Wake-on: d
        Link detected: yes  #表示是否检测到网络连接。yes表示检测到连接，no表示未检测到。
查看操作系统的运行级别
[root@localhost ~]# runlevel
N 5
列出系统中打开的文件和进程
[root@localhost ~]# lsof
查看启动端口
[root@localhost ~]# lsof -i:22
重新挂载
sudo mount -o rw,remount /
查看ssh的版本
[root@kwephis1914886 ~]# ssh -V
OpenSSH_8.2p1, OpenSSL 1.1.1f  31 Mar 2020
检查sshd配置文件是否正确
[root@kwephis1914886 ~]# sshd -t /etc/ssh/sshd_config
Extra argument /etc/ssh/sshd_config.
