

# 安装 Linux 的准备工作指南

Installing Linux can be an exciting journey into the world of open-source operating systems! Before you dive into the installation process, it's essential to lay a solid foundation by preparing everything properly. Let's go through the key steps and considerations to ensure a smooth installation experience.

## 1. 确定安装类型

### 1.1 全盘安装 vs 双系统安装

- **全盘安装**：如果你打算完全使用 Linux 并且不再需要其他操作系统，可以选择全盘安装。这样会将整个硬盘分区给 Linux，适合追求简洁和高效的新手。
- **双系统安装**：如果你希望保留 Windows 或其他操作系统，可以选择双系统安装。这样可以在启动时选择进入哪个系统。不过，双系统安装需要更多的磁盘管理技巧，分区规划时要特别小心！

### 1.2 目标发行版

选择一个适合你的 Linux 发行版是关键！以下是一些流行的发行版：

- **Ubuntu**：适合新手，界面友好，社区支持强大。
- **Fedora**：注重最新技术和稳定性，适合喜欢尝鲜的用户。
- **Debian**：稳定可靠，适合服务器环境。
- **Arch Linux**：需要一定的技术背景，但高度可定制。
- **Linux Mint**：基于 Ubuntu，适合希望使用熟悉界面的用户。

**小贴士**：如果你不确定，可以从 Ubuntu 或 Linux Mint 开始，它们非常适合新手。

## 2. 硬件准备

### 2.1 电脑硬件

- **处理器 (CPU)**：现代 Linux 发行版对大多数 CPU 都有良好支持，特别是 x86_64 架构。
- **内存 (RAM)**：建议至少 2GB RAM（对于轻量级发行版如 Xubuntu 或 Lubuntu），4GB 或更高 RAM 适合桌面环境如 Ubuntu。
- **存储设备**：确保至少有 20GB 的可用空间（对于基本安装），更多空间则更好，尤其是如果你计划安装大量软件或数据。

### 2.2 硬件兼容性

- **显卡驱动**：确保你的显卡驱动受支持。大多数现代显卡（如 NVIDIA、AMD、Intel）都有良好的开源驱动支持，但有些高级功能可能需要专有驱动。
- **网络适配器**：确保你的网络适配器（有线或无线）在 Linux 下有良好的支持。
- **BIOS/UEFI 设置**：检查 BIOS/UEFI 是否支持你选择的安装方式（如 UEFI 启动）。

**小贴士**：如果你使用的是笔记本电脑，建议在安装前查阅该型号的 Linux 兼容性报告。

## 3. 安装介质准备

### 3.1 下载 ISO 镜像

- 访问你选择的发行版官方网站，下载最新版本的 ISO 镜像。
- 网址：
    https://mirrors.aliyun.com/
    https://mirrors.tuna.tsinghua.edu.cn/
    https://mirrors.163.com/
- **验证 ISO 文件**：下载完成后，验证 ISO 文件的完整性，通常通过校验和（如 MD5、SHA256）来确保文件未损坏。

### 3.2 制作启动介质

- **工具**：使用工具如 **Rufus**（Windows）或 **Balena Etcher**（跨平台）将 ISO 镜像刻录到 USB 闪存盘或 DVD。
- **注意事项**：
  - 确保 USB 闪存盘至少有 8GB 空间。
  - 刻录过程中不要拔出 USB 闪存盘，以免损坏数据。

**小贴士**：如果你不确定如何制作启动 USB，可以参考发行版的官方指南。

## 4. 数据备份

- **重要数据**：在进行任何磁盘操作前，务必备份重要数据。格式化磁盘或分区会删除所有数据！
- **工具**：使用云存储（如 Google Drive、iCloud）或外部硬盘进行备份。

**警告**：分区操作可能导致数据丢失！请确保备份所有重要文件。

## 5. 网络配置

- **有线网络**：确保网线连接正常。
- **无线网络**：安装后可能需要额外配置无线网卡驱动。
- **DNS 设置**：如果你经常更换网络环境，建议熟悉 DNS 配置。

**小贴士**：安装完成后，可以通过命令行快速测试网络连接：`ping google.com`

## 6. 安全设置

- **root 密码**：在安装过程中设置一个强密码，用于 root 用户。
- **用户账户**：创建一个普通用户账户，避免日常使用 root 权限。

**警告**：记住 root 密码！丢失后可能导致系统无法访问。

## 7. 安装后的初步设置

- **时区和语言**：安装完成后，设置正确的时区和语言环境。
- **软件仓库**：配置软件仓库以获取最新的软件包。
- **防火墙**：启用防火墙（如 UFW 或 Firewalld）以增强安全性。

**小贴士**：安装完成后，可以通过以下命令更新系统：`sudo apt update && sudo apt upgrade`

## 8. 安装提示

- **分区操作**：如果你不确定如何分区，可以选择自动分区选项。但建议学习一些基本的分区知识。
- **网络驱动**：某些网络适配器可能需要额外驱动，安装完成后可以查找解决方案。
- **耐心**：安装过程可能需要一些时间，特别是下载和安装软件包时。

**总结**

安装 Linux 是一个充满乐趣的过程，但准备工作同样重要。通过本文的指南，你可以更好地规划和准备，确保安装顺利进行。祝你在 Linux 的世界里探索愉快！ 🚀

**最后提醒**：安装前再次检查所有数据是否备份，分区是否正确，启动介质是否可用！