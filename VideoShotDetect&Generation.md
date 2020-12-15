video shot detection/Shot Boundaries Detection
镜头边界检测/分镜头边界检测
with Information Extraction
https://en.wikipedia.org/wiki/Shot_transition_detection
https://github.com/WalternativE/fableshotdetection
http://fableshotdetection.azurewebsites.net/

### video analytics
vapoursynth hist.Color2

### videocut
https://github.com/mifi/lossless-cut
https://github.com/bartekmotyl/simple-video-cutter
https://github.com/kanehekili/VideoCut
（with subtitle cut）https://github.com/antiboredom/videogrep

### timeline
https://github.com/PixarAnimationStudios/OpenTimelineIO

### 标注工具设计
预训练的标注CNN，逐帧转成1D spectrum，可视化标注

### 实现1
[快速打轴，目标是实现video semantic spectrum的网络](https://www.bilibili.com/video/BV1ps411b7as?p=2)

### 术语 term
A shot is a sequence of frames shot uninterruptedly by one camera. There are several film transitions usually used in film editing to juxtapose adjacent shots; In the context of shot transition detection they are usually group into two types

Effects Detection
(dissolve, fade in fade out, and sliding in sliding out
Abrupt Transitions
突然转变 -这是从一个镜头到另一个镜头的突然转变，即一个帧属于第一帧，下一帧属于第二帧。它们也称为硬切割或简单切割。

Gradual Transitions(wipes
渐进过渡 -在这种过渡中，使用彩色，空间或空间彩色效果将两个镜头组合在一起，从而逐渐将一个镜头替换为另一个镜头。这些通常也称为柔和过渡，可以有多种类型，例如擦拭，溶解，褪色 ...
“检测切割”是指获得切割位置；更准确地说，硬切为“帧i和帧i + 1之间的硬切”，软切为“从帧i到帧j的软切”。
https://en.wikipedia.org/wiki/Film_editing


切割检测的每种方法都基于两阶段原理：

计分 –数字视频的每对连续帧都有一定的分数，表示这两个帧之间的相似/不相似。
决策 –评估先前计算出的所有分数，如果认为分数较高，则检测为削减。

指标
Recall is the probability that an existing cut will be detected:
Precision is the probability that an assumed cut is in fact a cut:
F1 is a combined measure that results in high value if, and only if, both precision and recall result in high values:

https://github.com/AnyiRao/SceneSeg
https://cvhci.anthropomatik.kit.edu/~mtapaswi/projects-storygraphs.html

(with SubtitleManager)
https://github.com/BitFloyd/deepsbd

https://github.com/AlphaPav/Video-Shot-Detection
Video shot detection in four algorithms: Histogram Intersect, Moment Invariant(Humoment), Motion Vector(Optical Flow), Twin Comparison(Based on Histogram).

https://github.com/ccyanxyz/video_shot_detection
(with timeline hist)
1.Color histogram
2.Moment invariants
3.Intersect
4.Union

https://github.com/hoffsupes/Shot-boundary-detection-using-SVM-s-Aritificial-Neural-Networks-and-kNN
使用监督学习技术的镜头边界检测
镜头是一次连续拍摄的连续帧。两个镜头之间的差异区域称为镜头边界。
采取各种区分特征，如帧方差，均值，L2-范数等，然后使用各种分类器比较其性能。
The Linear SVM以92.99％的分类精度实现最佳性能。

https://pyscenedetect.readthedocs.io/en/latest/


### video Generation, Temporal 是关键词
kinetics-600 https://blog.csdn.net/liuxiao214/article/details/80144375
YouTube annotation clips
youtubeVOS.py
https://github.com/Fafa87/SEP/blob/master/tests/test_loaders/test_youtube.py
DVD-GAN: https://github.com/MaxVoloskiy/CV_Assignment3/blob/master/README.md

