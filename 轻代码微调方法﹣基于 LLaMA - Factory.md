# 1、 LLaMA - Factory 的安装部署
```bash
    git clone https://github.com/hiyouga/LLaMA-Factory.git
```

# 2、 LLaMA - Factory 必备项安装

```bash
pip3 install -- upgrade pip 
pip3 install bitsandbytes >=0.39.0
cd LLaMA-Factory
#安装核心依赖（默认开启FlashAttention优化）   
pip3 install - e ".[torch,metrics]"
```

# 3、 LLaMA - Factory 的主要子目录说明

    config ：存放自定义模型训练脚本
    data ：存放示例的训练数据集样本，采用 json 格式
    examples ：存放示例的训练脚本，包括 train_full 、 train_lora 、 train_qlora 、 inference（推理）、 merge_lora （模型合并）
    saves ：微调模型临时存放目录
    models ：模型合并临时存放目录

# 4、训练模板制作

    在examples目录下找到train_lora子目录，复制llama3_lora_sft.yaml文件的一个备份，进行修改，重新命名，比如deepseek_lora.yaml,存放到config目录中
