为了在Linux系统中创建并配置`/var/log/auth.log`日志文件，按照以下步骤操作：

### 步骤 1：检查rsyslog服务状态

首先，确保rsyslog服务正在运行。使用以下命令检查服务状态：

```bash
sudo systemctl status rsyslog
```

如果服务未运行，启动它：

```bash
sudo systemctl start rsyslog
```

并确保它设置为开机启动：

```bash
sudo systemctl enable rsyslog
```

### 步骤 2：编辑rsyslog配置文件

打开rsyslog的配置文件：

```bash
sudo nano /etc/rsyslog.conf
```

查找是否有以下行（可能被注释掉）：

```bash
authpriv.* /var/log/auth.log
```

如果没有，添加这行。如果有，则取消注释（去掉前面的`#`）。

### 步骤 3：创建log目录（如果需要）

确保`/var/log`目录存在。如果不存在，创建它：

```bash
sudo mkdir -p /var/log
```

### 步骤 4：设置正确的文件权限

确保rsyslog有权限写入`/var/log/auth.log`。通常，rsyslog以`syslog`用户或`syslog`组运行。检查当前用户和组：

```bash
ps -o user,group -p $(pgrep rsyslog)
```

然后，设置`/var/log/auth.log`的权限：

```bash
sudo chown syslog:syslog /var/log/auth.log
sudo chmod 640 /var/log/auth.log
```

### 步骤 5：重新加载rsyslog配置

保存配置文件后，重新加载rsyslog以应用更改：

```bash
sudo systemctl reload rsyslog
```

### 步骤 6：测试配置

执行一个认证操作，例如使用`su`切换用户或登录，然后查看`/var/log/auth.log`是否被更新：

```bash
tail -f /var/log/auth.log
```

在另一个终端中执行认证操作，看看日志是否记录了相关信息。

### 步骤 7：检查journalctl日志（可选）

如果仍然没有记录，可以使用`journalctl`查看系统日志：

```bash
journalctl --unit=systemd-logind -f
```

这可能显示认证相关的日志信息。

### 总结

通过以上步骤，你应该能够配置系统以生成并记录`/var/log/auth.log`日志文件。确保rsyslog配置正确，服务运行，权限设置正确，并测试配置是否生效。