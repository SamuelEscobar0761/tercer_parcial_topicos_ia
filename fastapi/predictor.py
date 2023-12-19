from ultralytics import YOLO

PATH = "E:/UPB/topicos ia/tercer_parcial_topicos_ia/" #Path absoluto necesario de cambiar para el correcto funcionamiento
MODEL_PATH = f"{PATH}primer_parcial_topicos_ia/model/best1.pt"
MODEL_PERSONS_PATH = f"{PATH}primer_parcial_topicos_ia/model/yolov8n.pt"

class GunsPredictor:
    def __init__(self, model_path: str = MODEL_PATH):
        self.model = YOLO(model_path)
    
    def predict_file(self, file_path: str):
        results = self.model([file_path])

        # Asume que el primer elemento de results es el objeto Results deseado
        result_obj = results[0]

        # Accede a las cajas delimitadoras y a las clases detectadas
        boxes = result_obj.boxes

        # Cuenta las pistolas detectadas
        num_pistols = len(boxes.xywh)

        return num_pistols, boxes.xywh

class PersonsPredictor:
    def __init__(self, model_path: str = MODEL_PERSONS_PATH):
        self.model = YOLO(model_path)
    
    def predict_file(self, file_path: str):
        results = self.model([file_path])

        # Asume que el primer elemento de results es el objeto Results deseado
        result_obj = results[0]

        # Accede a las cajas delimitadoras y a las clases detectadas
        boxes = result_obj.boxes
        classes = boxes.cls  # Usamos 'cls' en lugar de 'labels'

        # Cuenta las pistolas detectadas
        num_persons = sum(1 for cls in classes if result_obj.names[int(cls)] == 'person')
        persons_boxes = []
        for i in range(0, num_persons):
            persons_boxes.append(boxes.xywh[i])
        return num_persons, persons_boxes