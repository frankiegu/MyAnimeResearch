# 标注标签工程设计
```
语义相关的特征（resnet 多旁路/组卷积，stage模式，推荐使用 强inception架构【Inception-v1】）
（在每一阶段拥有一定的底层特征解耦-表征能力，pool是为了增加高层的特征表征能力，特征离散稀疏【手工安排也可以，引入label competition learning更好】）

除去分辨率尺寸相关trick，只用 单纯的blurpooling（maxpool，avgpool）
用剪枝（dropout）剪底层与部分中层
并在各级语义设置不同的优化器

语义需要尽可能直路，而且多（路由）分支
提出三层语义表征

底层尽可能寻找图像的重复模式，但又不至于变成线条检测，所以尽可能宽浅
ResNeXt+relu型,SGD+Wasserstein正则

中层是在尽可能寻找底层特征的对应模式，由于语义表征程度不一样，需要很深的中间层
densenet+tanh型，最后一层不要pool，

高层完美解耦（高级特征图），不能引入任何trick（norm，等）或改变尺寸（pooling），在处理成梯度之前需要构思精妙的损失函数（可以用度量学习contrastive+margin）
此层可能用NAS寻找更好，用带动量的SGD
```

## 底层语义

## 中间级语义

## 高级语义



