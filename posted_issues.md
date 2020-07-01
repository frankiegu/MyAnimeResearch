
#### Today's low quality (poor) anime, but content was still well!
####  **color design/color model**（见色本） and **after effect**（动画摄影/后期） is significant impact audience perception.
#### 这里说的影响，就是画面，色彩&后期效果。内容是，（作画）画风，原画，线条人设这些复杂边缘语义（不考虑修改）。

举例：（摄影故意拉高光，唐突色彩设计审美，低成本动画，...）
> 恋爱小行星的色彩，白日，夜晚场景
> 请问你要来点兔子吗？，头发边缘高光（光圈 halo）

#### so, not real2anime ,not selfie2anime , anime2anime is possible ? and what kind method make it real?
不同于，此repo的现实滤镜，动画里的内容是很相近的，即使不引入注意力机制、空域标准化 等....手段
估计也能搞出能看的效果
transfer between two anime series
把京阿尼画风给迁移到新海诚上面？
又或者把PA迁到京阿尼上面（想看PA版K-ON! 2333）？
....

实现出来（我吹爆！），要是搞出业界都能满足的那甚好！

#### not noly that , is possible transfer these gega（原画） and sakuga（作画） style ?
对于内容，（作画）画风，原画，线条人设这些复杂边缘语义，嘛
作画风格迁移，是时空特征，动画自动中割研究资料也很少，很难（

再就是
or re-implement a anime version deepfakeface ?
动画换脸，例如下边这是个 亚丝娜<->御坂 的cyclegan。
[cyclegan-for-unsupervised-translation-in-anime](https://bellchen.me/research/cs/gan/cyclegan-for-unsupervised-translation-in-anime/)
[youtube - deepfakeanime](https://www.youtube.com/watch?v=uqqrXGWf5MQ)

二创，能网红。

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
