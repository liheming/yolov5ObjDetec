#
import cv2
import os

"""python+opencv实现图片视频互相转换"""


class MediaTool:
    mp4Path = './static/video/123.mp4'
    targetPath = './static/mp4Img/'
    filename = './static/video/result.mp4'
    width = 200
    height = 300

    def mp4toimg(self):

        vc = cv2.VideoCapture(self.mp4Path)
        self.width = vc.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.height = vc.get(cv2.CAP_PROP_FRAME_HEIGHT)
        print(self.width)
        print(self.height)
        c = 1
        if vc.isOpened():
            rval, frame = vc.read()
        else:
            rval = False
        while rval:
            rval, frame = vc.read()
            if rval:
                cv2.imwrite(self.targetPath + str(c) + '.jpg', frame)
                c = c + 1
                cv2.waitKey(1)
        vc.release()

    def imgtomp4(self):
        fps = 0.8
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        video_writer = cv2.VideoWriter(filename=self.filename, fourcc=fourcc, fps=fps,
                                       frameSize=(2160, 1440))  # 图片实际尺寸，不然生成的视频会打不开
        for i in range(0, 6):
            p = i
            if os.path.exists(self.targetPath + str(p) + '.jpg'):  # 判断图片是否存在
                img = cv2.imread(filename=self.targetPath + str(p) + '.jpg')
                cv2.waitKey(100)
                video_writer.write(img)
        video_writer.release()
