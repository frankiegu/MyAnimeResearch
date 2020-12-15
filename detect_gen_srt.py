## Author : Nicolas Farrugia, February 2020
## Author @huaji0353
#https://pytorch.org/docs/stable/torchvision/io.html
##https://github.com/brain-bzh/videoannotation/blob/master/run_generate_srt.py
import torch
from torchvision.io import read_video
import torchvision.transforms as T
from tqdm import tqdm
import os
import sys
import datetime
from foranytest import *
import time

def gen_srt(strlabel,onset,srtfile,duration=4,num=1):

    starttime = onset
    endtime = starttime + duration

    string_start = datetime.time(0,starttime//60,starttime%60).strftime("%H:%M:%S")

    string_end = datetime.time(0,endtime//60,endtime%60).strftime("%H:%M:%S")

    with open(srtfile,'a') as f:
        f.write("{}\n".format(num+1))
        f.write("{starttime} --> {endtime}\n".format(starttime=string_start,endtime=string_end))
        f.write("{}\n".format(strlabel))
        f.write("\n")


videofile = sys.argv[1]
srtfile = 'a_detect.srt'

if os.path.isfile(srtfile):
    os.remove(srtfile)

# prepare the image transformer 
transforms = T.Compose([
        T.ToPILImage(),
        T.CenterCrop((1920,1920)),
        T.Resize((256,256)),
        T.ToTensor(),
])

#fps = 23.976
fps = 24

nbsec = 4

beg_film = 12*60+54
end_film = 14*60+31


n=0
with torch.no_grad():    
    for curstart in tqdm(range(beg_film,end_film,nbsec)):
        start = curstart
        end = curstart + (1/fps)

        vframes, aframes, info = read_video(filename=videofile,start_pts = start,end_pts=end,pts_unit='sec')
        vframes = vframes.permute(0,3,1,2)
        
        vframes = transforms(vframes[0]).unsqueeze(0)
        #save=T.Compose([T.ToPILImage()])
        #save(vframes).save('vframes.png')
        #time.sleep(2)
        #continue
        
        ### make predictions for object detection
        with torch.no_grad():
            out = net(vframes)#shape torch.Size([1, 6000])
            score, pred = torch.topk(out, k = 20)
            tags = print_tags_by_idx(pred)

        # process output of Imagenet Classes and print results:

        textplaces=''
        for si,ti in zip(score,tags):
            textplaces += ti + ': {:.4f} \n'.format(si.cpu().numpy())

        ### Generate final string
        annotation_str = f"{textplaces}"
        #print(annotation_str)

        ### Append to srt file with timecode 
        gen_srt(annotation_str,start,srtfile=srtfile,num=n)
        n=n+1