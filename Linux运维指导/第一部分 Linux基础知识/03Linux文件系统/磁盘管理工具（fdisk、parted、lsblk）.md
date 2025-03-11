

# Linux磁盘管理工具指南：fdisk、parted、lsblk等命令详解

欢迎来到Linux磁盘管理工具的冒险之旅！让我们一起探索这些强大的工具，让你的磁盘管理变得轻松愉快！✨

---

## 1. 什么是磁盘管理工具？

在Linux系统中，磁盘管理是操作系统管理员的日常任务之一。常见的磁盘管理工具包括`fdisk`、`parted`、`lsblk`等，它们可以帮助你查看、创建、修改和删除磁盘分区。这些工具的强大功能可以让你轻松地管理磁盘空间，优化存储效率。

---

## 2. lsblk：查看磁盘和分区信息

`lsblk`是一个非常直观的工具，用于列出块设备（磁盘和分区）的信息。它是Linux系统中的“磁盘信息查询大师”！🔍

### 基本用法

```bash
lsblk
```

### 输出解释

- **NAME**：设备名称（如sda、sdb等）。
- **MAJ:MIN**：主设备号和次设备号。
- **RM**：是否是可移动设备（0表示固定，1表示可移动）。
- **RO**：是否只读（0表示可写，1表示只读）。
- **TYPE**：设备类型（如disk表示磁盘，part表示分区）。
- **MOUNTPOINT**：挂载点。

### 示例

```bash
lsblk
```

输出示例：

```
NAME   MAJ:MIN RM   SIZE RO TYPE MOUNTPOINT
sda      8:0    0 238.5G  0 disk
├─sda1   8:1    0   512M  0 part /boot/efi
└─sda2   8:2    0 238G   0 part /
```

- **解读**：`sda`是一个238.5GB的磁盘，分为两个分区：`sda1`（512MB，挂载在`/boot/efi`）和`sda2`（238G，挂载在根目录`/`）。

**提醒**：`lsblk`是一个快速查看磁盘信息的工具，适合日常使用！但它不会显示分区表类型（如MBR或GPT）。

---

## 3. fdisk：传统的磁盘分区工具

`fdisk`是一个功能强大的磁盘分区工具，支持MBR分区表格式。它是Linux系统中经典的分区工具！OldData but gold! 💎

### 基本用法

```bash
sudo fdisk /dev/sdb
```

### 常用命令

在`fdisk`交互界面中，输入以下命令：

- **`p`**：显示当前分区表。
- **`n`**：创建新分区。
- **`d`**：删除分区。
- **`w`**：写入分区表并退出。
- **`q`**：退出不保存更改。

### 创建分区示例

1. 进入`fdisk`：
   ```bash
   sudo fdisk /dev/sdb
   ```

2. 输入`n`创建新分区。

3. 选择分区类型：
   - **`p`**：主分区。
   - **`e`**：扩展分区。

4. 选择分区编号（默认从1开始）。

5. 设置分区大小（默认单位是扇区，可以输入`+2G`表示2GB）。

6. 完成分区后，输入`w`保存并退出。

### 输出示例

```bash
sudo fdisk -l /dev/sdb
```

输出示例：

```
Disk /dev/sdb: 238.5 GiB, 256060514304 bytes, 500118192 sectors
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disklabel type: dos
Disk identifier: 0x12345678

Device     Boot   Start        End    Sectors   Size Id Type
/dev/sdb1          2048     1023999   1022048   500M 7  HPFS/NTFS/exFAT
```

- **解读**：`/dev/sdb`磁盘有一个分区`/dev/sdb1`，大小为500MB，类型为NTFS。

**提醒**：`fdisk`仅支持MBR分区表，不支持GPT分区表！如果你需要管理GPT分区表，建议使用`parted`！

---

## 4. parted：支持GPT分区表的工具

`parted`是一个功能强大的磁盘分区工具，支持MBR和GPT分区表格式。它是现代Linux系统的首选工具！🌟

### 基本用法

```bash
sudo parted /dev/sdb
```

### 常用命令

在`parted`交互界面中，输入以下命令：

- **`print`**：显示当前分区表。
- **`mkpart`**：创建新分区。
- **`rm`**：删除分区。
- **`quit`**：退出。

### 创建分区示例

1. 进入`parted`：
   ```bash
   sudo parted /dev/sdb
   ```

2. 输入`mkpart`创建新分区：
   ```bash
   mkpart primary ext4 0 2G
   ```

   - **解释**：创建一个主分区，文件系统类型为ext4，大小从0到2GB。

3. 输入`print`查看分区表：
   ```bash
   print
   ```

4. 输入`quit`退出。

### 输出示例

```bash
sudo parted -l /dev/sdb
```

输出示例：

```
Model: ATA WDC WD2500FBBB- (scsi)
Disk /dev/sdb: 256GB
Sector size (logical/physical): 512B/512B
Partition Table: gpt
Disk Flags: 

Number  Start   End    Size   File system  Name  Flags
1      1049kB  1074MB 1064MB ext4
```

- **解读**：`/dev/sdb`磁盘有一个GPT分区表，包含一个大小为1064MB的ext4分区。

**提醒**：`parted`支持GPT分区表，适合现代大容量磁盘！但它不支持MBR和GPT混用。

---

## 5. 其他磁盘管理工具

### 5.1 mkfs：格式化分区

`mkfs`用于创建文件系统。常见的文件系统类型包括`ext4`、`ntfs`、`vfat`等。

#### 命令格式

```bash
sudo mkfs -t <文件系统类型> /dev/sdX
```

#### 示例

```bash
sudo mkfs -t ext4 /dev/sdb1
```

- **解释**：将`/dev/sdb1`分区格式化为ext4文件系统。

### 5.2 mount 和 umount：挂载和卸载分区

#### 挂载分区

```bash
sudo mount /dev/sdb1 /mnt
```

- **解释**：将`/dev/sdb1`挂载到`/mnt`目录。

#### 卸载分区

```bash
sudo umount /mnt
```

- **解释**：卸载`/mnt`目录。

### 5.3 df 和 du：查看磁盘使用情况

#### 查看挂载点

```bash
df -h
```

#### 查看文件和目录大小

```bash
du -sh /home
```

**提醒**：`df`显示磁盘空间使用情况，`du`显示文件和目录的大小。两者结合使用可以更好地管理磁盘空间！🌟

---

## 6. 总结

Linux磁盘管理工具的强大功能让你轻松掌控磁盘空间！通过`lsblk`快速查看磁盘信息，通过`fdisk`和`parted`管理分区，通过`mkfs`格式化分区，通过`mount`和`umount`挂载和卸载分区。这些工具就像你的磁盘管理助手，帮助你高效完成任务！🚀

**最后提醒**：在分区和格式化之前，务必备份重要数据！磁盘操作可能会导致数据丢失！⚠️