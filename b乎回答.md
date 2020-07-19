深度学习（机器学习）AI的发展将对动画制作与ACG生态产生什么影响？ - huaji0353的回答 - 知乎
https://www.zhihu.com/question/380922982/answer/1092289800

深度学习（机器学习）AI的发展将对动画制作与ACG生态产生什么影响？
动画制作，动画产业，机器学习，深度学习（Deep Learning），生成对抗网络（GAN）

深度学习&动漫相关 但不限于：

1.现况调查，实际应用，任务清单，你提出的trick

2.学术研究方向相关

3.公众领域的影响与产业影响（不限于 二创，平民创作；动画制作，制作流程，国外中下游外包等等）

4.未来将能实现的任务

5.等等

你已邀请 某人路过顺便 宁星远 Gingo Amane Nagatsuki myccyycy Rrupmid Nyche 刘冬煜 何之源 SECRET WANG MrPhD 川岛木村 KevinLi君 Li Miaomiao 李睿 小岛美奈子 不可思议的巫女 扬之水 Jsgfery David 9 Bluebear 橘 吉野 灵剑 Qp只会睡觉 开心的派大星 咲花 夕小瑶 酱紫君 等 27 人

huaji0353
7 人赞同了该回答
只统计调查>2016年的相关，并且是公开，能够检索到的信息
大量注重 学术研究方向相关调查


kawaii makes world accelerate !! --by SerialLain3170



修改&合成任意动画片段，用于动漫二创！

又或者 打破第四面墙 让动漫角色/waifu 活起来，与TA们交谈！

让现实世界看起来像动漫一样？让你的朋友变成熟悉的动漫角色？

再者，终极创作工具！给很有想法，想做，但又无能力实现的人，创作出作品来

等....等....



新闻
嘛，AT-X社长都这样说了2333

我认为还是有点言重了，具体的话还是因为，2016年的热潮（16/7年日媒吹了一波chainer上色），加上研究后没啥真实应用，热潮退了后，结果研究还是太少了

现在GANs图像方面，很成熟了，研究能够实用化！（不是手冢治虫漫画那种找几个programmer，拿着SOTA一跑，一调就完事了，，，而是需要针对研究）
论文收集
（圣人惠）大佬的动漫深度论文收集：SerialLain3170/awesome-animepapers

我做的整理收集：huaji0353：[200606]整理

dimpurr/awesome-acg-machine-learning

deeppomf/DeepLearningAnimePapers



数据集
Gwern的 Danbooru2019: A Large-Scale Crowdsourced and Tagged Anime Illustration Dataset

Gwern的 Anime Crop Datasets: Faces, Figures, & Hands

（ 清晰 低损 正脸 小数据集 3.5K）kaggle@arnaud58/selfie2anime


点兔角色40k画像数据集（我带有介绍相关） kaggle@rignak/gochiusa-faces




经典
nagadomi/lbpcascade_animeface

rezoo/illustration2vec

nagadomi/waifu2x

makegirlsmoe/makegirlsmoe_web

lllyasviel/style2paints

16/7年日媒吹了一波chainer上色 效果都差的很，这里不补



twitter@myccyycy @_aixile之间的对话

目前发现一个正式的小型会议 MANPU 和一个同人研讨会 Sig2D 。
sig2d是comike的社团，里面的人是谁我也不太清楚。这类社团其实还有不少（好像官网已经挂了）
MANPU 是东大aizawa研搞的，基本都是和其他会议一起workshop的形式，是可以去投论文的
waifu2x是nagadomi神的兴趣本位的产品，illustration2vec的作者在pfn，后来pfn的taizan在i2v的数据集上训练了paintschainer，style2paints的作者看到了paintschainer开始研究上色，那人是Soochow University的一个本科生，那人很神奇，他居然用他的laptop训练了style2paints。。。。
话说 makegirlsmoe 的曝光率太高了，加上 waifu2x 和 illustration2vec (引用极多) 感觉这仨是曝光度最高的 AnimeML Project 没有更多了 (

23333



网红（>1k star）
公众领域产生的影响

（白箱...-现实场景动漫风SOTA）SystemErrorWang/White-box-Cartoonization

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

以上是部分列举，不再更新补充，更多可以看我的github star：@huaji0353
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
twitter@roadrunner01

qiita

reddit@AnimeResearch（gwern大佬开的）

reddit@ML

@arxivdaliy



个人研究
（现活跃）

US：twitter@gwern&shawwn，大佬们的讨论github@tensorfork/tensorfork/issues

gwern的 Making Anime Faces With StyleGAN 是的必看的一篇blog！
who is gwern?

这位大佬是制作了thiswaifudoesnotexist（TWDNE）和danbooru201x等等数据集，深度学习研究者，训练动漫等艺术娱乐类的数据集的GANs模型，个人有TPU集群（不然怎么），是动漫数据集研究的主力！
TWDNEv4要来了！或许基于biggan而不是stylegan，将是全身插画生成！重命名为GANBOORU
JP：github@SerialLain3170|twitter@NieA7_3170，github@freedomofkeima

WynMew，dragonmeteor，t_takasaka，Zampie

CN scholar：Tien-Tsin Wong (CUHK)，以及Style2Paints Research（？）

（stylegan2在动漫数据集上的研究）csdn@3D_DLW



企业/公司
©FPN*preferrednetworks'crypko，Adobe Research

twitter@SizigiStudioszigiStudios

dwango'nico，radius5'cre8tiveai，OLM，DeNA，BANDAI

我的twitter@huaji0353，在喜欢过的推里，很多相关，也会转发各种动态


非主流方案的SOTA
（stylegan2+selfie2anime）


（U-NET+styleGAN）


（DenseNet用于超分辨率）




application
协同作画；草图指导


《SmartPaint: a co-creative drawing system based on generative adversarial networks》


东北ずん子的机器学习生态圈
偏商业授权使用


中文名：豆打地平线
（赞助给动画整个工程文件）

dwango的自动中割



在VOCALOID圈爆火的【AIきりたん】

详细请萌娘一下东北切蒲英与NEUTRINO
Singing Voice Synthesis歌声合成

用于音声合成的标注数据集（无料 禁止商业使用）



第二个声源，众筹
基于深度学习【NSF】的歌曲合成 NEUTRINO（NEURAL SINGING SYNTHESIZER）

official@n3utrino.work

github@r9y9/nnsvs

twitter@SHACHI_KRTN




提出的概念（粗字为已有的研究方向）


图像处理（特定领域的数据集 - 动漫数据集研究）：

可用于研究用途的动画/漫画/插画数据集/库

角色脸部识别/分类/向量特征化：角色元数据库

插画/漫画/动画分类/向量特征化：片段/分镜描述，视觉元数据库，插画索引

二次创作/素材抽取，角色脸部迁移，动画摘要/转漫画，便民插画/动画搜索

动漫风迁移：现实背景动画风格化，从自拍生成动漫脸，摄影合成/修改，anime2anime

角色生成：动漫脸生成animeface，语义指导脸部生成，全身立绘生成，3D语义指导生成

草稿/草图抽取：草稿简化，插画复原，素材抽取

用户指导自动上色，全自动上色，自动光影，基于见色本/插画参照

自动中割/补帧/动画，神经渲染/2D转3D：单帧风格迁移，live2d/emote结合，自动嘴型序列帧，动作中割，动作/表情差分，3D深度估计，mmd2anime/神经卡渲

插画超分/去码/补全（inpaint）



非图像处理方向（通用性很强，所以不需要详细介绍）：

音乐合成系统，etc...

轻小说阅读个性化/辅助，生成/写作辅助，对话理解&生成，聊天机器人，故事/世界观模型生成（TRPG，视觉小说），动画理解/转小说



其他扩展方向：

监督作画/台词








由于这块跟常规数据集不一样，数据集问题大，研究资料很少，更别谈亮眼的paper了，除了那篇 arXiv:1805.07997v1 没人会去单独做，充其量也就是在现实数据集上用动画数据集复现，看了好些都没啥为了针对动漫图像的trick

欢迎有卡，有时间的大佬对此领域贡献研究！



喜闻乐见的娘化
（twitter@minux302）


minux302/status/1274703119876714498

tensorflow娘

2333

NN娘


吐槽

话说。。。你们为什么这么喜欢用cartoon呢？

survey后，anime 动漫/二次元（博客，等其他UGC站） 国人用的最多，学术上 sketch cartoon comic，推特reddit，github等 常用anime做关键词眼

统一 一下关键词不好吗？？



keyword 关于学术用严格定义
Cartoon与Anime的主要的区别是什么？
​
www.zhihu.com
图标
animation，用于动画，动起来这方面的研究，主词（main）

在你搜索相关内容时可以选取使用以下关键词（供搜索索引）



animate|anime|cartoon|アニメ

animate 基本不用

取决于你使用数据集的风格

请看这个issue，关于cartoon数据集的收集：github@pytorch/vision/issues/2042

cartoon 非日系ACGN的其他风格；（eg：爱奇艺cartoon数据集，Caricature, a type of exaggerated artistic portrait, amplifies the distinctive, yet nuanced traits of human faces

PS：当你使用cartoon的时候请注意，医疗用语也有个CT Cartoon Medical的关键词，谷歌学术搜cartoon给一大堆这玩意

anime 日本动画，日系作画风格插画，日系ACGN；比例较大

学术上推荐作为副词（prefix）使用



comic|manga|まんが

这里无明显定义，多用manga。但如果大量日漫风格，使用anime做副词即可



face|portrait

face 纯脸部，五官

portrait 头部画像，类似证件照

其实区分开很重要，portrait远比face复杂


sketch|illustration|イラスト

sketch 草稿，原画，线稿

illustration 插画（eg：pixiv

但为了区分一般艺术作品（adobe最喜欢用这个词了。。。），常用anime副词做限制



深度学习任务

ディープラーニング 機械学習 深層学習 自動生成

detection|recognition|segmentation|embedding|generation

video summarization|compression



提出的trick:（加入数据标注站的设计，移至github更新）
动漫图像的low-level（低层级）特征（超分辨率、质量增强及去噪等），低级特征不需要高级特征语义，可以自由选取（实验loss下降得下去不）通过自监督的shortcuts完成这些任务

对于动画上色作业，是否可以取代，训练一个网络让其从零（草稿原画）开始上色，而是从前后两个已上色的分镜做参照（时间连续性），训练一个短时记忆网络来给中割的动画草稿上色？

关于动漫视频摘要；图片流一帧帧处理，那确实难 但如果用字幕（时间连续性），利用duration与文字内容，上去预测场景切割位置 然后用时间点反过来标注视频

github@huaji0353/AnimeResearch



附录01
huaji0353：[动漫深度学习研究指北]之数据集



@spillerrec/overmix


pad摄影合成成一张

Stitching anime screenshots

result

Super Resolution

Logo detection and removal

摄影效果加减


Q：收集动画，插画，漫画，等等进行机器学习研究的法律，版权问题？
题外话：dtmstation对AIきりたん的作者做了个专访，就提到了这个

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
编辑于 07-18

crane07-15
大佬您好，我是即将踏入机器学习领域的新人，麻烦想问一下对二次元做机器学习具体有怎样的现实意义，可以作为研究课题吗，对这个方向很感兴趣但又担心研究价值会不会不能让老师们认同
huaji0353 (作者) 回复crane07-18
这块跟常规数据集不一样，数据集问题大（版权等等的问题），研究资料很少，更别谈亮眼的trick了；没有卡，还是新人，就不要当主攻了吧；爱好，拿anime跑跑常规模型玩玩就行（（（
关于现实意义，我已经在回答中举了这块能做的任务
说服导师嘛，你可以引用前不久的抖音的那个动漫anime滤镜，卡通肖像的实际娱乐价值（与anime不同cartoon卡通国内研究很多）等等，还有日本动画anime这种风格可能也不能符合导师们的价值观吧（（（


匿名用户
3 人赞同了该回答
谢谢huaji0353邀请。

他的回答挺全面了，我说点其他的吧。

就目前(2020.4)来说，用于制作的实际应用很可能是没有的。

专业软件实装的只有CSP的系列，有姿态识别、上色和线条处理功能。

最近还有个拿深度学习制作手冢治虫漫画的应用，但是目前未看到成品。

有一些朋友和我讨论过引入深度学习程序用于实际制作的项目，不过目前暂时也并未使用。其中一个朋友的流程是主NPR辅助少量人工的路线，我们主要讨论了两个应用方向，光影处理、线稿处理。

光影处理方面，ProjectHAT合作的项目LineShader(ShadeSkecth)目前也已经在CVPR2020发表，不过基于个人判断，这个东西并不会实用化。后续会基于这个开发更贴近流程的应用，比如基于学习的NPR、模型及贴图处理。NPR的光影也算是个学界以为解决了，但是实际上并未解决的问题。现在流程里，主要就是模型法线修改，灯光打光死抠，合成后期死修了。对于一般项目，可能只做法线修改，但是高端项目的话，是要全做下来的。著名的例子就是Polygon Pictures的可怕的Nuke脚本了（由于要修的很多，以致一段时间是在720p制作，之后放大的）。NPR的最核心就是f(NdotL, ...)，从式子上看要不修改法线，要不修改灯光。但是对于绘画来说，很多时候是非物理的，不遵循一般的光线传输的(Light Transport)，也不遵循一般的几何的。比如一个经典例子，灯光打到人脸上时，不能有阴影，但是特定角度下，又需要有半脸的阴影，这对于渲染器来说，如果不修改法线再配合特殊的打光和阴影遮罩，这就是不可能的事了。所以，要解决这个问题，必须要依赖数据驱动的方法。这也是正是LineShader立项的原因，并且也希望通过公开的数据可以进一步活跃相关的研究。

至于线条处理，虽然低端项目里NPR程序输出的线条还可以，不过在高端项目里还是有所欠缺的。从我个人来看，同样和光影属于一样的尴尬地位。很多时候为了得到好看的线，还需要对模型和输出进行大量的工作（有兴趣的人可以试试拿主流的NPR程序渲染Stanford系列模型，表现最好的应该是Blender的Freestyle）。近期CVPR2020上也发表了偏使用学习方法处理线条的文章，不过限于数据问题，这个文章也很难应用于实际制作。在线条上，还是存在几个老问题，线条的取舍和线条的表现。其中线条的表现是比较制约其发展的，而且也是极依赖数据驱动方法的。很多时候，一般人在缺乏对比时观察线条不一定能发现区别，但是存在更好的对比时，就是这1像素的差距，都会有很明显的不同，玄学说法上就是线条的张力与动感什么的。线条的表现，其实很大程度会影响画面的认知结果的，比如线条的粗细会暗示几何的情况，所以在一些描线NPR里会提供基于一些几何的线条风格控制方法，目前最主要的也是通过几何和光影基于一些启发式的方法去进行风格化（CVPR那篇作者写过一篇TOG，是用学习做的，并分析了影响的因素）。不过对于绘画，很多时候几何也只是因素之一，作者的主观意图也会极大的影响绘画中的技法使用，所以单单从几何上出发肯定是无法解决这个问题的，必须依赖于数据驱动的学习，而制约这个发展的，主要是从业人员少和数据稀少了。

直接面向制作最终画面的辅助外，可能应用还是比较多的，比如处理，参考及娱乐等。我想PaintChainer、Style2paint系列（包括CSP内置的）应该为很多绘画提供了底稿和上色参考。而Crypko、Makegirlsmoe、Waifunotexist提供了很多头像生成的娱乐以及参考。至于风格转换上，真人到漫画、照片到绘画也提供了很多的娱乐。至于漫画方面，有一些漫画处理和翻译的程序在被使用，不过这个不属于我认为的面向制作最终画面的范围。Crypko后续的面部及动画生成可能是第一个在娱乐和制作里实际的应用了。



待续

一些研究现状（数据和研究人员）
一些前沿应用和研究（不完全是深度学习的）
引用
如果有兴趣可以私聊。

编辑于 04-24
​已赞同 3​
​
