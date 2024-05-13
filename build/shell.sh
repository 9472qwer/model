#!/bin/bash


cp shell.sh ../

# 删除build目录下所有内容
rm -rf *

# 运行cmake
cmake ..

# 编译项目
make

# 将脚本复制到build目录下
cp ../shell.sh ./

rm ../shell.sh
