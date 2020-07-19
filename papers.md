首发于
动漫深度图像处理


[200711]动漫深度学习论文&code仓库整理

NewTOP
STomoya/animeface（几乎日更，85commits，大量GAN复现&实验结果）

已复现（ACGAN DCGAN GAN PGGAN StyleGAN WGAN WGAN_gp cGAN pix2pix pixelshuffle SRGAN DiffAugment(2020 Data-Efficient GAN Training. Zhao) ）






Paper
Modeling Artistic Workflows for Image Generation and Editing

线稿/草稿阶段上色（EdgeConnect(getchu face) dataset）

效果太好！但是使用 getchu face & 模型抽出的线稿 作为配对数据集，如果给真人插画师的线稿，非gal立绘，直接就懵了吧

http://arxiv.org/abs/2007.07238v1





SON OF ZORN’S LEMMA TARGETED STYLE TRANSFER USING INSTANCE-AWARE SEMENTIC SEGMENTATION

把二次元（这里是卡通）人物增强&然后与现实融合（Harmonization）的工作


https://arxiv.org/abs/1701.02357





Hair Shading Style Transfer for Manga with cGAN

漫画头发给Shading一下，效果不好

https://www.scitepress.org/Link.aspx?doi=10.5220%2f0008961405870594



Deep-Eyes: Fully Automatic Anime Character Colorization with Painting of Details on Empty Pupils

之前的工作，整体上色的效果很差，本文就是对单独对眼睛/瞳，进行上色的工作

https://diglib.eg.org/handle/10.2312/egs20201023


The input layer has four channels to input the grayscale line drawing and the hint image of pupils.（他这是什么鬼，输入是瞳孔的RGB+灰度线稿？？）



A CNN-Based Tool to Index Emotion on Anime Character Stickers

【视觉搜索】就是把emoji跟你的动漫表情包进行pair，然后你只要emoji就能自动贴上去

https://doi.org/10.1109/ISM46123.2019.00071





Unpaired Image-to-Image Translation using Adversarial Consistency Loss

https://arxiv.org/abs/2003.04858




Two-Stage Sketch Colorization With Color Parsing

https://ieeexplore.ieee.org/document/8944253


吐槽：style2paint也用的这几张插画线稿做的演示，还有不少paper也喜欢用第一张（



Reference-Based Sketch Image Colorization using Augmented-Self Reference and Dense Semantic Correspondence

https://arxiv.org/abs/2005.05207



Line Art Correlation Matching Network for Automatic Animation Colorization

https://arxiv.org/abs/2004.06718



Deep Line Art Video Colorization with a Few References

https://arxiv.org/abs/2003.10685



PaintsTorch: a User-Guided Anime Line Art Colorization Tool with Double Generator Conditional Adversarial Network

https://dl.acm.org/doi/fullHtml/10.1145/3359998.3369401



CartoonRenderer: An Instance-based Multi-Style Cartoon Image Translator

https://arxiv.org/abs/1911.06102



Unsupervised Discovery of Interpretable Directions in the GAN Latent Space

https://arxiv.org/abs/2002.03754




Towards Diverse Anime Face Generation: Active Label Completion and Style Feature Network

https://diglib.eg.org/bitstream/handle/10.2312/egs20191016/065-068.pdf


他的效果不是很好，可能是用的过时模型，没有任何训练trick，但这个Label Completion本人是很看好的；

PS：给gwern大佬发了，他说有点华而不实....



Repositories
pit-ray/SPADE-pix2pix-for-Anime

pit-ray/Anime-Semantic-Segmentation-GAN

shiwang0211/anime_classification

miracleyoo/anime-2-cosplay（动漫cos）

anthony-dipofi/danbooru-tagger（又一个多标签标注模型）

apple2373/pytorch-small-dataset-image-generation（预训练 128x128 biggan）

reppy4620/SimCLR4Paint（simCLR 自监督框架 无预训练模型）

B-Step62/anime-GANs（他训的SAGAN怎么这么棒？？）


Atom-101/Danbooru-Dataset-Maker（从数据库下载，制作特定tags的训练集）

fire-eggs/Danbooru2019





comment
在？为什么这么氵？


在？anime为什么加es
