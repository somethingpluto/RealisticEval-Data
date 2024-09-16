#!/bin/bash

source ~/anaconda3/etc/profile.d/conda.sh

# chatglm3
echo "chatglm3 start"
conda activate chatglm3

python /home/whut/chx/chatglm3/main.py --languages python javascript typescript c\&cpp --rounds 1 | tee chatglm3.txt

conda deactivate
echo "chatglm3 finish"

# codegeex4
echo "codegeex4 start"
conda activate codegeex4
python /home/whut/chx/codegeex4/main.py --languages python javascript typescript c\&cpp --rounds 1 | tee codegeex4.txt
conda deactivate
echo "codegeex4 finish"

# codellama
echo "codellama start"
conda activate pytorch
python /home/whut/chx/codellama/main.py --languages python javascript typescript c\&cpp --rounds 1 | tee codellama.txt
conda deactivate
echo "codellama finish"

# codegen2.5
echo "codegen2.5 start"
conda activate codegen25
python /home/whut/chx/codegen2.5/main.py --languages python javascript typescript --rounds 1 | tee codegen25.txt
conda deactivate
echo "codegen2.5 finish"

# deepseek
echo "deepseek start"
conda activate pytorch
python /home/whut/chx/deepseek/main.py --languages python javascript typescript c\&cpp --rounds 1 | tee deepseek.txt
conda deactivate
echo "deepseek finish"

# llama
echo "llama start"
conda activate pytorch
python /home/whut/chx/llama/main.py --languages python javascript typescript c\&cpp --rounds 1 | tee llama.txt
conda deactivate
echo "llama finish"

# mistral
echo "mistral start"
conda activate mistral
python /home/whut/chx/mistral/main.py --languages python javascript typescript c\&cpp --rounds 1 | tee mistral.txt
conda deactivate
echo "mistral finish"

# phi
echo "phi start"
conda activate Phi3
python /home/whut/chx/phi/main.py --languages python javascript typescript c\&cpp --rounds 1 | tee phi.txt
conda deactivate
echo "phi finish"

# starcoder2
echo "starcoder2 start"
conda activate Phi3
python /home/whut/chx/starcoder2/main.py --languages python javascript typescript c\&cpp --rounds 1 | tee starcoder2.txt
conda deactivate
echo "starcoder2 finish"