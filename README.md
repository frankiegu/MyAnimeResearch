# AnimeResearch
personal research in Anime workflow

## Abstract
日式动漫（アニメ）
作画式的创作方式，作为特有的一种艺术风格（日式漫画创作
不同与美式，drama，等其它影视作品的剧情设计

以及衍生出的萌元素，糅合日本特有的文化

在剧情上本质上是轻小说（人物对话，文字特效（简称脑补））
在画面表现上是日式漫画（夸张的表情，视觉语言，分镜）

## keywords
动漫 工作流 制作 视觉语言 可计算 逆向工程 素材 二次创作

## paper
Computational manga and anime. SIGGRAPH Asia 2013 Courses

## 日式动画制作流程
剧本脚本->分镜->人设->layout原画->色彩->美术背景->动画->上色->摄影->配音

分镜（picture action dialog）

剧情->动作与形->细节/关键帧->动画

### 相关职位
剧本脚本家
分镜 絵コンテ storyboard
演出
原画
作画/监督
人物设计
美术背景
色彩设计
动画
摄影
上色
音乐
...

## 逆向工程关键
移除字幕

### 通过鉴别-移除作画无关的特征

目标：演出，人物设定，色彩指定
移除：摄影后期特效，摄影指定（pan，slied...），背景，配音
前景sheet，手工作画
背景BG，美术设定
动画的后期摄影合成，前景和背景制作不同，根据色彩进行拆分，得到前景人物与背景序列

### 寻找不变元素
基于reference
Graph Matching based Anime Colorization with Multiple References
