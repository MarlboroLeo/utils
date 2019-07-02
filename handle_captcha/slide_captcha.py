# coding=utf-8
# @Time    : 2019/7/2 14:58
# @Author  : Leau
# @File    : slide_captcha.py
import cv2


"""
PIL 剪裁图片
code_img = Image.open('{}_full.png'.format(self.policy_no))
capcha = code_img.crop((882, 405, 968, 435))
"""

@staticmethod
def cut_captcha(file_name):
    """剪裁验证码"""
    target_gray1 = cv2.imread(file_name)
    # print(target_gray1.shape)
    cropped = target_gray1[18:42, 25:50]  # 裁剪坐标为[y0:y1, x0:x1]  30  24
    cv2.imwrite("cut"+file_name, cropped)

@staticmethod
def captcha_calculation(file_name):
    """计算位移"""
    target_gray2 = cv2.imread("cut"+file_name)
    template_rgb = cv2.imread("grayBack.png", 0)
    target_rgb = cv2.cvtColor(target_gray2, cv2.COLOR_BGR2GRAY)
    res = cv2.matchTemplate(target_rgb, template_rgb, cv2.TM_CCOEFF_NORMED)
    value = cv2.minMaxLoc(res)
    # print(value)
    # print(value[3][0] - 23)
    return value[3][0] - 23

@staticmethod
def get_tracks(S):
    """
    :param S: 缺口距离Px
    :return:
    """
    S += 20
    v = 0
    t = 0.2
    forward_tracks = []
    current = 0
    mid = S * 3 / 5  # 减速阀值
    while current < S:
        if current < mid:
            a = 2  # 加速度为+2
        else:
            a = -3  # 加速度-3
        s = v * t + 0.5 * a * (t ** 2)
        v = v + a * t
        current += s
        forward_tracks.append(round(s))

    back_tracks = [-3, -3, -2, -2, -2, -2, -2, -1, -1, -1]
    # print(forward_tracks)
    # print(sum(forward_tracks) - 19)
    return {'forward_tracks': forward_tracks, 'back_tracks': back_tracks}

def slide(self, tracks):
    """
    滑动滑块拼图
    :param tracks: {'forward_tracks': forward_tracks, 'back_tracks': back_tracks}
    :return:
    """
    # 假动作
    self.slider.move_by_offset(xoffset=random.randint(200, 800), yoffset=random.randint(200, 800)).perform()
    # 滑块元素
    slide_element = self.driver.find_element_by_id("slideBar")
    self.slider.move_to_element(slide_element)
    self.slider.click_and_hold()
    for track in tracks.get('forward_tracks'):  # 向右滑
        self.slider.move_by_offset(xoffset=track, yoffset=0)
    for track in tracks.get('back_tracks'):  # 向左滑
        self.slider.move_by_offset(xoffset=track, yoffset=0)

    time.sleep(1)  # 0.5秒后释放鼠标
    self.slider.release().perform()
    time.sleep(1)
    if slide_element.get_attribute("style") != "left: 236px;":
        print("滑动验证码不成功继续尝试")
        self.driver.save_screenshot("error_slide.png")
        self.Wait("refreshBtn")
        self.slide(tracks)

