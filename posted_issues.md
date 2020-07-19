https://github.com/SystemErrorWang/White-box-Cartoonization/issues/17
anime2anime is possible? #17

#### Today's low quality (poor) anime, but content was still well!
####  **color design/color model**（见色本） and **after effect**（动画摄影/后期） is significant impact audience perception.
#### 这里说的影响，就是画面，色彩&后期效果。内容是：作画；画风，原画，线条人设这些。

举例：（摄影故意拉高光，唐突色彩设计审美，低成本动画，...）
> 恋爱小行星的色彩，白日，夜晚场景
> 请问你要来点兔子吗？，头发边缘高光（光圈 halo）

**Sooo?, Not**
###  real2anime ,not selfie2anime , anime2anime is possible ? 
#### what kind method make it real?
> 不同于，此repo的现实滤镜，动画里的内容是很相近的，即使不引入注意力机制、空域标准化 等....手段
> 估计也能搞出能看的效果（[推荐阅读，使用patch based discriminator ](https://github.com/SystemErrorWang/White-box-Cartoonization/issues/17#issuecomment-653328767)）

transfer between two anime series
实现出来（我吹爆！），要是搞出业界都能满足的那甚好！（救救业界⑧，审美都要奇怪了...）
把京阿尼画风给迁移到新海诚那上面？
又或者把PA迁到京阿尼上面（想看PA版K-ON! 2333）？

### **mmd2anime** : 卡通渲染相关，将mmd粗模，等3DCG渲染成特定动画风格
用于训练分镜，演出的设计，漫画分镜设计（等我补一个支持3D人偶的分镜软件）
> 灵感来源于[动画制作中的layout](https://i0.hdslb.com/bfs/album/705100470465c322de3bc91b157ad58354102a9a.jpg)
> 既然这么难学习位置关系，那就3D直接风格化吧，保留的内容几乎是等同，并且可以用3Dlayout的骨架信息代替帧帧手工的关键点标注；与其折腾于2D手绘互转，3D预渲染的效果与成绩应该是非常可观的！

低成本实现 中高的动画品质，mmd2anime+anime2anime可能是方向

mmd[舞蹈](https://www.bilibili.com/video/av3903564)/[小剧场](https://www.bilibili.com/video/av38508) 
参考BanG Dream [第一季 2D动画](https://www.bilibili.com/bangumi/media/md5807)；[第二季 3DCG](https://www.bilibili.com/bangumi/media/md4762002),[第三季 3DCG](https://www.bilibili.com/bangumi/media/md28224078)

#### not noly that , is possible transfer these gega（原画） and sakuga（作画） style ?
对于内容，（作画）画风，原画，线条人设这些复杂边缘语义，嘛
作画风格迁移，是时空特征，动画自动中割研究资料也很少，很难（

再就是
### re-implement a anime version deepfakeface ?
动画换脸，例如下边这是个 亚丝娜<->御坂 的cyclegan。
[cyclegan-for-unsupervised-translation-in-anime](https://bellchen.me/research/cs/gan/cyclegan-for-unsupervised-translation-in-anime/)
[youtube - deepfakeanime](https://www.youtube.com/watch?v=uqqrXGWf5MQ)

二创，能网红。

### 附，版权问题：
生成模型严格定义上是侵犯版权的（嘛，你复制了，修改了人家的作品）
但公众方面，部分宽松，但边界未知？（就看人家告不告你，你国版权方搞不搞事；用有名的，或那旧番老番，那种倒闭了的动画公司估计稳）
> 日本改正著作権法「著作権法４７条の７」
> 進化する機械学習パラダイス ～改正著作権法が日本のAI開発をさらに加速する～
> 機械学習に使うデータセットの著作権について





https://github.com/SystemErrorWang/White-box-Cartoonization/issues/11
数据集 #11


### 7/12重写

### 巡礼

专门做完layout（基本语义布局）后的[bili video](https://www.bilibili.com/video/av94309755)
cutmix [幸运星巡礼](https://zhuanlan.zhihu.com/p/158097617)

[bili 动态 例](https://h.bilibili.com/49399777)
[bili 动态 例](https://h.bilibili.com/49108595)

### 二三次元对比，动漫x现实

[风格化，调色后期](https://www.bilibili.com/video/BV1gb411K78p)

摄影合成/图像融合 二次元与现实融合（Image Harmonization）
@msinsanity [link](https://vk.com/msinsanity)

@[bilibili-go海盗](https://h.bilibili.com/18259362)
并且提供的白背景的分割素材（动态id：22632857，看评论）
（已询问up，无对照合集）
（如果你们觉得可以利用，我可以将他的相册都爬下来）

### 动漫梗图，少样本标注 作数据增广
anime related style / content parody collection
例如danbooru里的【parody，meme，alternate】使用的特殊tag

梗推荐：
Sailor Moon Redraw | #sailormoonredraw
#STAYHOMEwithTRIGGER
Tokyo snowfalls Japanese TV interviewed a couple | #Special Feeling/Special Mood 特別な気分
shiba inu&fox | #Right-Hook Dog 右フック犬
drink resting on breasts | #tapioca Challenge #タピオカチャレンジ
未来日記 由乃 Yandere Pose | Yuno Face #Yandere Trance
新房45° シャフト角度 | #Shaft Head Tilt






（但动画anime这方面没人做，我想做，但1没大量生肉资源，2也没能力写个标注系统什么的）

> 话说谷歌最近有篇，自动计数君：[《Counting Out Time: Class Agnostic Video Repetition Counting in the Wild》](https://ai.googleblog.com/2020/06/repnet-counting-repetitions-in-videos.html)，应该能拿来用一用

但是我想，不仅仅是loop，而是片段（例如sakugabooru）
针对不同任务，压制不同分辨率的片段
然后用于 **视频摘要，视频理解，视频压缩，视频风格迁移** 等任务，
例如danbooru众包的方式来标注，制作出动画数据集

sakugabooru.com X animeloop.org ?
animebooru设计：
充分利用与设计
元信息：动画公司，导演，分镜演出作监
视频：动作行为，场景，标注粗细度（例如danbooru），摄影效果，此分镜的关键帧（用于视频理解的增广） 等等
音声轨：效果音，对话音声，背景音乐，等等

prepare a datasets like these
summe tvsum 
http://cvlab.hanyang.ac.kr/coview2019/
https://www.crcv.ucf.edu/THUMOS14/download.html
gwern works ([danbooru2019 etc.](https://www.gwern.net/Crops#danbooru2019-portraits))

关于收集动画，插画，漫画，等等进行机器学习研究的法律，版权问题？
除生成模型以外，无任何问题，（不限于“非商业用途”），收集动漫数据对第三方进行培训并发布经过培训的模型是安全的。
从第三方的原始数据创建数据库，通过对数据库进行标签处理等来创建学习数据集并提供和出售数据集的行为 - OK（分类模型，检测模型等）
用第三方的学习数据集执行机器学习以生成训练模型并提供和出售训练模型的行为 - NG
参考：
> 日本改正著作権法「著作権法４７条の７」
> 進化する機械学習パラダイス ～改正著作権法が日本のAI開発をさらに加速する～
> 機械学習に使うデータセットの著作権について
