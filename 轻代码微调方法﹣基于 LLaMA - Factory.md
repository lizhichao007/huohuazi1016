# 1、 LLaMA - Factory 的安装部署
```bash
    git clone https://github.com/hiyouga/LLaMA-Factory.git
```

# 2、 LLaMA - Factory 必备项安装

```bash
pip3 install --upgrade pip 
pip3 install bitsandbytes >=0.39.0
cd LLaMA-Factory
#安装核心依赖（默认开启FlashAttention优化）   
pip3 install -e ".[torch,metrics]"
```

# 3、 LLaMA - Factory 的主要子目录说明

    config ：存放自定义模型训练脚本
    data ：存放示例的训练数据集样本，采用 json 格式
    examples ：存放示例的训练脚本，包括 train_full 、 train_lora 、 train_qlora 、 inference（推理）、 merge_lora （模型合并）
    saves ：微调模型临时存放目录
    models ：模型合并临时存放目录

# 4、训练模板制作

    在examples目录下找到train_lora子目录，复制llama3_lora_sft.yaml文件的一个备份，进行修改，重新命名，比如deepseek_lora.yaml,存放到config目录中

# 5、准备数据
模板要求（支持单轮/多轮对话）：
```json
[
  {
    "conversation": [
      {"role": "user", "content": "如何做番茄炒蛋？"},
      {"role": "assistant", "content": "1. 鸡蛋打散..."}
    ]
  },
  {
    "conversation": [
      {"role": "user", "content": "LLM微调有哪些方法?"},
      {"role": "assistant", "content": "常见方法包括..."},
      {"role": "user", "content": "哪种显存占用最低？"},
      {"role": "assistant", "content": "LoRA+梯度检查点..."}
    ]
  }
]
```
数据格式转换（已有原始数据时）：
```bash
python scripts/preprocess_data.py \
  --input your_data.json \
  --output formatted_data.json \
  --template alpaca  # 可选模板: moss, chatglm3, qwen
```
阶段3：启动训练（4种经典场景配置）
📌 场景1：低成本单卡LoRA微调
```bash
CUDA_VISIBLE_DEVICES=0 python src/train_bash.py \
  --stage sft \
  --model_name_or_path meta-llama/Llama-2-7b-hf \
  --dataset formatted_data \
  --template default \
  --lora_target q_proj,v_proj  \  # 关键：选择LoRA注入层
  --per_device_train_batch_size 8 \ 
  --gradient_accumulation_steps 4 \
  --learning_rate 2e-5 \
  --max_grad_norm 0.5 \
  --val_size 0.1 \
  --max_samples 1000 \
  --fp16 \
  --output_dir outputs/llama2-lora
```
📌 场景2：8GB显卡QLoRA训练
```yaml
# 修改train_args/qlora.yaml
quantization_bit: 4
lora_config:
  r: 64
  target_modules: ["q_proj","k_proj"]
train:
  per_device_train_batch_size: 2
  gradient_accumulation_steps: 16
```
```bash
python src/train_bash.py --config train_args/qlora.yaml
```
阶段4：结果验证（1分钟）
```python
from transformers import pipeline

# 加载合并后的模型（自动融合LoRA权重）
generator = pipeline("text-generation", 
                    model="outputs/llama2-lora/merged",
                    device=0)

question = "帮我写封英文会议邀请函"
response = generator(question, 
                   max_new_tokens=300,
                   temperature=0.7,
                   do_sample=True)
print(response[0]['generated_text'])
```
⚡ 高级技巧
- 1.混合精度优化：在3060等显卡启用--bf16可提速30%
- 2.显存节省：添加--flash_attn和--gradient_checkpointing可降低40%显存
- 3.并行训练：多卡训练时增加--ddp_find_unused_parameters False
- 4.监控指标：TensorBoard实时记录损失曲线
```bash
tensorboard --logdir outputs/llama2-lora/runs
```
🛠️ 常见问题排查
问题现象	解决方案
OOM显存不足	降低batch_size，增加gradient_accumulation_steps
Loss不下降	检查数据格式，尝试调大learning_rate（1e-5→3e-5）
生成结果乱码	添加--model_name_or_path中的tokenizer路径
推理速度慢	导出ONNX格式：python scripts/export_onnx.py

最新支持：LLaMA-Factory已支持 Llama3-8B/70B, Qwen1.5, DeepSeek-MoE 等20+主流架构，可在/models目录查看完整支持列表。