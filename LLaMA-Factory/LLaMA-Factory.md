下拉代码仓库
git clone https://github.com/hiyouga/LLaMA-Factory.git
预安装准备
pip cache purge #清理缓存
pip install --upgrade pip
pip install bitsandbytes>=0.39.0
cd LLaMA-Factory
pip install -e ".[torch,metrics]"
