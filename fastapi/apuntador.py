import os
import cv2 as cv
import numpy as np

class Apuntador:
    def __init__(self, model_path, image_array):
        self.BODY_PARTS = {
            "Nose": 0, "Neck": 1, "RShoulder": 2, "RElbow": 3, "RWrist": 4,
            "LShoulder": 5, "LElbow": 6, "LWrist": 7, "RHip": 8, "RKnee": 9,
            "RAnkle": 10, "LHip": 11, "LKnee": 12, "LAnkle": 13, "REye": 14,
            "LEye": 15, "REar": 16, "LEar": 17, "Background": 18
        }

        self.POSE_PAIRS = [
            ["Neck", "RShoulder"], ["Neck", "LShoulder"], ["RShoulder", "RElbow"],
            ["RElbow", "RWrist"], ["LShoulder", "LElbow"], ["LElbow", "LWrist"],
            ["Neck", "RHip"], ["RHip", "RKnee"], ["RKnee", "RAnkle"], ["Neck", "LHip"],
            ["LHip", "LKnee"], ["LKnee", "LAnkle"], ["Neck", "Nose"], ["Nose", "REye"],
            ["REye", "REar"], ["Nose", "LEye"], ["LEye", "LEar"]
        ]

        self.image_width = 600
        self.image_height = 600
        self.threshold = 0.2
        self.net = cv.dnn.readNetFromTensorflow(model_path)
        self.img = image_array
        self.points = []

    @staticmethod
    def is_arm_extended(shoulder, elbow, wrist):
        shoulder_to_elbow = np.linalg.norm(np.array(shoulder) - np.array(elbow))
        elbow_to_wrist = np.linalg.norm(np.array(elbow) - np.array(wrist))
        shoulder_to_wrist = np.linalg.norm(np.array(shoulder) - np.array(wrist))
        return np.isclose(shoulder_to_elbow + elbow_to_wrist, shoulder_to_wrist, atol=10)

    def process_image(self):
        photo_height, photo_width = self.img.shape[:2]
        self.net.setInput(cv.dnn.blobFromImage(self.img, 1.0, (self.image_width, self.image_height),
                                               (127.5, 127.5, 127.5), swapRB=True, crop=False))

        out = self.net.forward()
        out = out[:, :19, :, :]

        assert(len(self.BODY_PARTS) == out.shape[1])

        for i in range(len(self.BODY_PARTS)):
            heatMap = out[0, i, :, :]
            _, conf, _, point = cv.minMaxLoc(heatMap)
            x = (photo_width * point[0]) / out.shape[3]
            y = (photo_height * point[1]) / out.shape[2]
            self.points.append((int(x), int(y)) if conf > self.threshold else None)


        for pair in self.POSE_PAIRS:
            partFrom, partTo = pair
            idFrom, idTo = self.BODY_PARTS[partFrom], self.BODY_PARTS[partTo]

            if self.points[idFrom] and self.points[idTo]:
                cv.line(self.img, self.points[idFrom], self.points[idTo], (0, 255, 0), 3)
                cv.ellipse(self.img, self.points[idFrom], (3, 3), 0, 0, 360, (0, 0, 255), cv.FILLED)
                cv.ellipse(self.img, self.points[idTo], (3, 3), 0, 0, 360, (0, 0, 255), cv.FILLED)

    def is_any_arm_extended(self):
        # Check both arms
        right_extended = self.is_arm_extended(
            self.points[self.BODY_PARTS["RShoulder"]],
            self.points[self.BODY_PARTS["RElbow"]],
            self.points[self.BODY_PARTS["RWrist"]]) if all(
            self.points[idx] for idx in [self.BODY_PARTS["RShoulder"], self.BODY_PARTS["RElbow"], self.BODY_PARTS["RWrist"]]) else False

        left_extended = self.is_arm_extended(
            self.points[self.BODY_PARTS["LShoulder"]],
            self.points[self.BODY_PARTS["LElbow"]],
            self.points[self.BODY_PARTS["LWrist"]]) if all(
            self.points[idx] for idx in [self.BODY_PARTS["LShoulder"], self.BODY_PARTS["LElbow"], self.BODY_PARTS["LWrist"]]) else False

        return right_extended or left_extended

    def which_arm_is_extended(self):
        # Check each arm
        if self.is_any_arm_extended():
            if self.is_arm_extended(self.points[self.BODY_PARTS["RShoulder"]],
                                    self.points[self.BODY_PARTS["RElbow"]],
                                    self.points[self.BODY_PARTS["RWrist"]]):
                return "Right"
            elif self.is_arm_extended(self.points[self.BODY_PARTS["LShoulder"]],
                                      self.points[self.BODY_PARTS["LElbow"]],
                                      self.points[self.BODY_PARTS["LWrist"]]):
                return "Left"
        return None

    def save_image(self, folder_name="poses", file_name="pose.jpg"):
        # Crear la carpeta si no existe
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)
        
        # Ruta completa para guardar la imagen
        save_path = os.path.join(folder_name, file_name)
        
        # Guardar la imagen
        cv.imwrite(save_path, self.img)
        print(f"Imagen guardada en: {save_path}")
