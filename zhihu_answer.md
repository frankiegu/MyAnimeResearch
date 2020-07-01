深度学习（机器学习）AI的发展将对动画制作与ACG生态产生什么影响？ - huaji0353的回答 - 知乎
https://www.zhihu.com/question/380922982/answer/1092289800

只统计调查>2016年的相关，并且是公开，能够检索到的信息
引言
kawaii makes world accelerate !!
--by SerialLain3170

修改&合成任意动画片段，用于动漫二创！
又或者 打破第四面墙 让动漫角色/waifu 活起来，与TA们交谈！
让现实世界看起来像动漫一样？让你的朋友变成熟悉的动漫角色？
再者，终极创作工具！很有想法，但又无绘画能力的人，创作出作品来，至 实现娱乐多模态生态？
等....等....

新闻


论文收集
（圣人惠）大佬的动漫深度论文收集：SerialLain3170/awesome-animepapers
我做的整理收集：huaji0353：[200606]整理

过时的awesome list
dimpurr/awesome-acg-machine-learning
deeppomf/DeepLearningAnimePapers

数据集
（ 清晰 低损 正脸 小数据集 3.5K）kaggle@arnaud58/selfie2anime

点兔角色40k画像数据集 kaggle@rignak/gochiusa-faces


经典
nagadomi/lbpcascade_animeface
rezoo/illustration2vec
nagadomi/waifu2x
makegirlsmoe/makegirlsmoe_web
lllyasviel/style2paints
16/7年媒体吹了一波chainer上色 效果都差的很，这里不补

twitter@myccyycy @_aixile之间的对话
目前发现一个正式的小型会议 MANPU 和一个同人研讨会 Sig2D 。
sig2d是comike的社团，里面的人是谁我也不太清楚。这类社团其实还有不少（好像官网已经挂了）
MANPU 是东大aizawa研搞的，基本都是和其他会议一起workshop的形式，是可以去投论文的
waifu2x是nagadomi神的兴趣本位的产品，illustration2vec的作者在pfn，后来pfn的taizan在i2v的数据集上训练了paintschainer，style2paints的作者看到了paintschainer开始研究上色，那人是苏州大学一个本科生，那人很神奇，他居然用他的laptop训练了style2paints。。。。
话说 makegirlsmoe 的曝光率太高了，加上 waifu2x 和 illustration2vec (引用极多) 感觉这仨是曝光度最高的 AnimeML Project 没有更多了 (

23333

网红>1k star
（现实场景动漫风）TachibanaYoshino/AnimeGAN
（anime Upscaler 动漫4K超分）bloc97/Anime4K
（真人动漫脸 tensorflow）taki0112/UGATIT
（"手残有救"，手绘草图生成动漫脸）youyuge34/PI-REC arxiv1903.10146
（去码）deeppomf/DeepCreamPy

其他复现
（pytorch resnet50+512x512danbooru2019）anthony-dipofi/danbooru-tagger
Mckinsey666/ACGAN-Conditional-Anime-Generation
（LFFD mxnet）cheese-roll/light-anime-face-detector
bellchenx/R-CNN-Anime-Face-Recognizer
qhgz2013/anime-face-detector
lengjiayi/VAE_animeface
jerryli27/AniSeg
seekerzz/Keras-Illustration2Vec
bellchenx/CycleGAN-PyTorch
Pie31415/AnimeGen
jerryli27/TwinGAN
（Fast anime face detection pytorch）WynMew/AnimeFaceBoxes
（A Faster-RCNN based）qhgz2013/anime-face-detector
（deep cascaded regression）kanosawa/anime_face_landmark_detection

以上是部分列举，更多可以看我的github star：@huaji0353
可玩demo
不统计任何在线网站，引流压力
freedomofkeima/MoeFlow
（resnet50+Dbooru2018）RF5/danbooru-pretrained
（stylegan预训练模型）a312863063/seeprettyface-ganerator-dongman
@Gwern This Waifu Does Not Exist
2019-02-26-stylegan-faces-network-02048-016041.pkl
2019-03-08-stylegan-animefaces-network-02051-021980.pkl
2019-04-30-stylegan-danbooru2018-portraits-02095-066083.pkl
2020-01-11-skylion-stylegan2-animeportraits-networksnapshot-024664.pkl
（TensorFlow resnet multi-label）KichangKim/DeepDanbooru
（exceptionally large）I filtered input images with tag count >= 20, so it may be 1.5~2M images, 1.5TB size.

消息源
weibo@fly51fly
twitter@roadrunner01
qiita(chainer)
reddit@AnimeResearch

个人研究（现活跃）
US：twitter@gwern&shawwn，大佬们的讨论github@tensorfork/tensorfork/issues
（PS：thiswaifudoesnotexist V4要来了！基于biggan，将是全身插画生成！重命名为GANBOORU）
JP：github@SerialLain3170|twitter@NieA7_3170，github@freedomofkeima
WynMew，dragonmeteor，t_takasaka

企业/公司 
©FPN*preferrednetworks'crypko，dwango'nico，radius5'cre8tiveai，OLM，DeNA，BANDAI，Adobe
twitter@SizigiStudios
我的twitter@huaji0353，在喜欢过的推里，很多相关，也会转发各种动态

非主流方案的SOTA
（stylegan2+selfie2anime）

（U-NET+styleGAN）

（DenseNet用于超分辨率）


Other
协同作画；草图指导

《SmartPaint: a co-creative drawing system based on generative adversarial networks》

原始回答
3D动画，自动中割（那个动画还真有供机器学习的数据集，就是要不少钱



顺便一提这个里面的角色，東北きりたん，是公开数据集可用于音声合成的

提出的概念（粗字为已有的研究方向）
可用于研究用途的动画/漫画/插画数据集
角色脸部识别/分类/向量特征化：角色元数据库
插画/漫画/动画分类/向量特征化：片段/分镜描述，视觉元数据库，插画索引
二次创作/素材抽取，角色脸部迁移deepanimefake，动画摘要/转漫画，便民插画/动画搜索
动漫风迁移：现实背景动画风格化，从自拍生成动漫脸，摄影合成/修改
角色生成：动漫脸生成animeface，语义指导脸部生成，全身立绘生成，3D语义指导生成
草稿/草图抽取：草稿简化，插画逆向
用户指导自动上色，全自动上色，自动光影，基于见色本/插画参照
自动中割/补帧/动画：单帧风格迁移，live2d/emote结合，自动嘴型序列帧，动作中割，动作/表情差分，3D深度估计
插画超分/去码/补全（inpaint）
轻小说阅读个性化/辅助，生成/写作辅助，对话理解&生成，聊天机器人，故事/世界观模型生成（TRPG，视觉小说），动画理解/转小说
监督作画/台词




只看图像处理的话主要也就是在玩GAN，角色设计启发，动画中割，上色或者生成。
（上色都是segmentation CNN

短时间內没有出现与强大语言模型结合的，少数据集训练，迁移学习模型蒸馏等等新技术


对于动漫数据集在模型可解释方面做的人也很少，除了那篇《Anime Style Space ...》Sitao Xiang et al. 没人单独做
纠结啊，又不能扔paper，太老的16年前的，基本都是水文，16年后深度网络来了，也都是在现实数据集上用动画数据集复现，效果还差，看了好些都没啥很亮眼的trick
数据集的理论研究也是严重不足

最后，喜闻乐见的娘化（twitter@minux302）

minux302/status/1274703119876714498

话说。。。你们为什么这么喜欢用cartoon呢？
survey后，anime 动漫/二次元（博客，等其他UGC站） 国人用的最多，学术上 sketch cartoon comic，推特reddit，github等 常用anime做关键词眼
统一 一下关键词不好吗？？

keyword 关于学术用严格定义
animation，用于动画，动起来这方面的研究，主词（main）
在你搜索相关内容时可以选取使用以下关键词（供搜索索引）

animate|anime|cartoon|アニメ
animate 基本不用
取决于你使用数据集的风格
请看这个issue，关于cartoon数据集的收集：github@pytorch/vision/issues/2042
cartoon 非日系ACGN的其他风格；（eg：爱奇艺cartoon数据集，Caricature, a type of exaggerated artistic portrait, amplifies the distinctive, yet nuanced traits of human faces
PS：当你使用cartoon的时候请注意，医疗用语也有个CT Cartoon Medical的关键词，cartoon被用于很多地方？？
anime 日本动画，日系作画风格插画，日系ACGN；比例较大
学术上推荐作为副词（prefix）使用

comic|manga|まんが
这里无明显定义，多用manga。但如果大量日漫风格，使用anime做副词即可

face|portrait
face 纯脸部，五官
portrait 头部画像，类似证件照

sketch|illustration|イラスト
sketch 草稿，原画，线稿
illustration 插画（eg：pixiv
但为了区分一般艺术作品（adobe最喜欢用这个词了。。。），常用anime副词做限制

深度学习任务
ディープラーニング 機械学習 深層学習 自動生成
detection|recognition|segmentation|embedding|generation
video summarization|compression

提出的trick:
动漫图像的low-level（低层级）特征（超分辨率、质量增强及去噪等），低级特征不需要高级特征语义，可以自由选取（实验loss下降得下去不）通过自监督的shortcuts完成这些任务
对于动画上色作业，是否可以取代，训练一个网络让其从零（草稿原画）开始上色，而是从前后两个已上色的分镜做参照（时间连续性），训练一个短时记忆网络来给中割的动画草稿上色？
关于动漫视频摘要；图片流一帧帧处理，那确实难 但如果用字幕（时间连续性），利用duration与文字内容，上去预测场景切割位置 然后用时间点反过来标注视频
关于智能摄影/调色滤镜（低层级特征）；如今的低质量（贫穷）摄影，色彩设计对动画观感影响颇大，本来内容还行的动画，用了这种新技法，瞬间低了一个档次让观众没兴趣看。我提出，色彩&摄影重控制对抗网络，两个不同制作的动画。像cyclegan一样，G学习怎么将低制作，渲染成高制作的色彩&摄影感，D学习鉴别是否是高制作


Q：收集动画，插画，漫画，等等进行机器学习研究的法律，版权问题？
A：除生成模型以外，无任何问题，（不限于“非商业用途”），收集动漫数据对第三方进行培训并发布经过培训的模型是安全的。
PS：这就是为什么很多人称日本是机器学习天堂了（
从第三方的原始数据创建数据库，通过对数据库进行标签处理等来创建学习数据集并提供和出售数据集的行为 - OK（分类模型，检测模型等）
用第三方的学习数据集执行机器学习以生成训练模型并提供和出售训练模型的行为 - NG
生成模型严格定义上是侵犯版权的
由于“与“复制”或“适应”相对应的行为，除非获得版权所有者的同意，否则原则上是侵犯版权。
但公众方面，部分宽松，但边界未知？
在进行生成数据集并将其出售给公众的业务时，一定程度上使用数据集中包含的受版权保护的作品的行为（例如，在销售站点上发布一小部分数据的行为）。等）也是可以接受的。但是，此处允许的使用行为是“次要使用”（“公开展示的演示文稿使用的部分的比例，使用的部分的数量以及使用它受限于显示时的显示准确度和其他因素“），因此无限制的作品不可用。
参考：
日本改正著作権法「著作権法４７条の７」
進化する機械学習パラダイス ～改正著作権法が日本のAI開発をさらに加速する～
機械学習に使うデータセットの著作権について
