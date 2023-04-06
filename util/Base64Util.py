import base64

import cv2
import numpy as np


class Base64Util:
    @staticmethod
    def get_base64_str(image_file):
        try:
            with open(image_file, 'rb') as f:
                img_data = f.read()
                uri = base64.b64encode(img_data)
                img_show = "data:image/png;base64," + uri.decode('utf-8')
            return img_show
        except Exception as e:
            print(f"img_to_base64 error:{e}")

    @staticmethod
    def get_press_base64_str(input_file, output_file, x=0, y=0):
        try:
            img = cv2.imdecode(np.fromfile(input_file, dtype=np.uint8), cv2.IMREAD_UNCHANGED)

            in_y, in_x = img.shape[:2]
            if (x):
                # 等比缩小为x=
                fxy = x / in_x
            elif (y):
                # 等比缩小为y=
                fxy = y / in_y
            else:
                fxy = 1

            # 按比例缩放,fx:x轴缩放比例,fy:y轴缩放比例
            output_img = cv2.resize(img, (0, 0), fx=fxy, fy=fxy, interpolation=cv2.INTER_AREA)
            cv2.imencode('.png', output_img)[1].tofile(output_file)
            image_code = Base64Util.get_base64_str(output_file)
            return image_code
        except Exception as e:
            print(f"img_to_base64 error:{e}")


if __name__ == '__main__':
    input_file = '/Users/tao.ding/PycharmProjects/atas-easy-test-py/screen/Login success-1.png'
    output_file = '/Users/tao.ding/PycharmProjects/atas-easy-test-py/screen/Login success-1.png'
    print(Base64Util.get_press_base64_str(input_file, output_file, 200, 200))
    # print(Base64Util.get_base64_str(input_file))
