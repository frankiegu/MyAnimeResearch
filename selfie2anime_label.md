# 标注标签工程设计

for 分类任务
语义相关的特征（resnet 多旁路/组卷积，stage模式，推荐使用 强inception架构【Inception-v1】）
逐层递减参数量
除去分辨率尺寸相关，单纯的blurpooling（maxpool，avgpool）
（在每一阶段拥有一定的底层特征解耦-表征能力）
用剪枝（dropout）剪底层与部分中层
并在各级语义做不同的优化器（底层用SGD+Wasserstein距离正则，高层用带动量的，直接softmax+CE（也可以用度量学习contrastive+margin））

语义需要尽可能直路，而且多（路由）分支
提出三层语义表征
尽可能寻找图像的重复模式，但又不至于变成线条检测

## 底层语义

## 中间级语义

## 高级语义



