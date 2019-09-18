# AnimeResearch
personal research in Anime workflow

## Abstract
日式动画（アニメ）制作已经高度分工化，每一个步骤都拥有极高的水平

作画的创作方式，作为特有的一种艺术风格

> 日式漫画创作，shoujo bishoujo manga

> 萌系动漫 ：大而有表现力的**眼睛**，夸张的动作，专注在头发和脸部特征上（moe anime evolution）

不同与美式，drama，等其它影视作品的剧情设计


以及衍生出的萌元素，糅合日本的文化


在剧情应用与轻小说一致（人物对话，文字特效（俗称文字脑补））

但又在画面表现上是日式漫画（夸张的表情或者不符合现实的透视以及位置动作表现 独特的**视觉语言**系统）

其他，在 人物设计，音乐创作，背景美术，摄影后期，3DCG）也有独特的风格，这里暂且不展开论述

### 独特的演出与叙事方式 - GALGAME
以故事、角色为卖点，游戏性/互动性单一，高度依赖于二次元文化系统，几乎只有日本人在制作Galgame

Galgame的演出的要求是要以最低的制作成本达成尽可能高的视听效果，这个要求决定了Galgame演出的的特点。 

素材的复用，人物立绘差分，以及表情由此诞生

以下是视觉语言的解析@神田空太

通过立绘画面的变化，例如出画与入画（角色在场景或对话的加入与离开），上下来回轻微位移（点头、鞠躬、高兴地跳起来，或者角色一些比较高昂的情绪），左右来回轻微位移（摇头拒绝的动作或者惊吓的情绪）

由于只使用立绘，通常会使用第一次人称的叙事方式

副语言（或称第二语义）与声音效果SE不做过多论述论述

## keywords
动漫 工作流 制作 视觉语言 可计算 逆向工程 素材 二次创作

## 日式动画制作流程（参考《アニメを仕事に! トリガー流アニメ制作進行読本》
剧本脚本->**（分镜演出+设定->layout 原画）**->色彩指定->美术背景->动画（清稿）->上色->摄影->配音

分镜由演出家绘制，视觉版的脚本 storyboard/cut - （picture 形 action 事 dialogue 语言）

剧情->动作与形->细节/关键帧->动画

### 职位
监督
剧本脚本家/系列构成
演出（分镜 絵コンテ storyboard）
角色设计
作画/监督
原画
色彩设计
美术设定
美术背景
动画
摄影

## overview and survey 研究调查
2013 颜检出，图割向量化

2014 waifu2x SR超分

2016 vanilla GAN（ACGAN,DCGAN,VAE）

2017 getchu danbroou dataset，动漫角色生成，自动上色，线稿提取，自动中割

2018 高分辨率动漫角色生成，styleGAN-anime

2019 waifulab sel2anime 等


## 逆向工程关键实现
### Our Approach
对于作画艺术，需要学习作画者的时间序列（CNN+RNN，LSTM）

由于数码作画与后期的离散性，我们需要一种通用模型能够抽取以下特征


goal：演出（人物动作即中割），人物设定，色彩指定

defficet：摄影后期与特效，3DCG，摄影指定（panorama，sliding...），配音音效

抽出前景sheet - 动画线稿 人物色指定

抽出背景BG - 美术设定

高层语义抽出 - 演出 剧本

### method
1. 动画的后期摄影合成，前景和背景制作不同，根据此抽出，得到前景与背景序列

2. 标记少量前景角色，细分角色区域，并训练分类模型，分离所有角色动作帧

3. 动作帧关键帧抽出，分类

### Anime Face Recognition
  + Face Part Segmentation (Eyes & Hair)
  + Eyes & Hair Color Distribution Calculation with Deep Learning

#### Algorithms:

Face Detection (Faster RCNN)
Semantic Segmentation (Segnet variant)
Color Distribution (K-Means)


