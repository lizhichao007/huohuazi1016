

要使用 `uv`（可能指 `virtualenv` 或 `virtualenvwrapper`）构建虚拟环境，请按照以下步骤操作：

### 1. 安装工具
首先，安装所需的工具。如果是 `virtualenv`：
```bash
pip install virtualenv
```
如果是 `virtualenvwrapper`，请先安装 `virtualenv`，然后安装 `virtualenvwrapper`：
```bash
pip install virtualenvwrapper
```

### 2. 创建虚拟环境
使用 `virtualenv` 创建环境：
```bash
virtualenv myenv
```

或者使用 `virtualenvwrapper` 创建环境：
```bash
mkvirtualenv myenv
```

### 3. 激活虚拟环境
对于 `virtualenv`，激活命令是：
```bash
source myenv/bin/activate  # Linux/Mac
myenv\Scripts\activate     # Windows
```

使用 `virtualenvwrapper` 的话，创建环境时已经激活，切换环境时使用：
```bash
workon myenv
```

### 4. 安装依赖
在激活的环境中，使用 `pip` 安装项目所需的包：
```bash
pip install requests
```

### 5. 退出虚拟环境
使用 `deactivate` 命令退出：
```bash
deactivate
```

### 6. 删除虚拟环境
删除不再需要的环境：
```bash
rm -rf myenv
```

或者使用 `virtualenvwrapper` 删除：
```bash
rmvirtualenv myenv
```

### 7. 管理多个环境
每个项目创建独立的虚拟环境，保持依赖管理清晰。

### 注意事项
- 确保安装了正确的工具。
- 环境激活后，终端提示会改变，表示当前环境。
- 安装依赖时，确保在激活的环境中进行，避免影响全局安装。

通过以上步骤，您可以轻松使用 `uv`（如 `virtualenv` 或 `virtualenvwrapper`）构建和管理项目的虚拟环境。


使用 uv 创建隔离的 Python 环境：

uv sync --extra torch --extra metrics --prerelease=allow
在环境中运行 LLaMA-Factory：

uv run --prerelease=allow llamafactory-cli train examples/train_lora/llama3_lora_pretrain.yaml
