import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import cv2
import numpy as np
from ultralytics import YOLO

# YOLOv8 모델 불러오기 (사전학습된 모델 사용)
model = YOLO("yolo11s.pt")  # yolov8s.pt 등 다른 모델도 가능

# tkinter 앱 생성
root = tk.Tk()
root.title("YOLO 객체 탐지 앱")
root.geometry("900x700")

# 전역 변수
img_panel = None
output_img = None

# 이미지 탐지 및 표시 함수
def detect_objects():
    global output_img, img_panel
    if not output_img:
        messagebox.showwarning("경고", "먼저 이미지를 업로드하세요.")
        return

    # OpenCV 이미지를 YOLO로 추론
    results = model(output_img)[0]
    result_img = results.plot()  # 탐지된 결과 그리기 (NumPy 배열 반환)

    # OpenCV(BGR) → PIL(RGB)
    result_img_rgb = cv2.cvtColor(result_img, cv2.COLOR_BGR2RGB)
    result_pil = Image.fromarray(result_img_rgb)
    result_pil.thumbnail((800, 600))  # 크기 제한

    # tkinter에 표시
    tk_img = ImageTk.PhotoImage(result_pil)
    img_panel.configure(image=tk_img)
    img_panel.image = tk_img

# 이미지 업로드 함수
def upload_image():
    global output_img, img_panel
    filepath = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png;*.bmp")])
    if not filepath:
        return

    # OpenCV로 이미지 읽기
    output_img = cv2.imread(filepath)

    # PIL로 변환하여 표시
    img = cv2.cvtColor(output_img, cv2.COLOR_BGR2RGB)
    pil_img = Image.fromarray(img)
    pil_img.thumbnail((800, 600))  # 표시용 크기 제한
    tk_img = ImageTk.PhotoImage(pil_img)

    if img_panel:
        img_panel.configure(image=tk_img)
        img_panel.image = tk_img
    else:
        img_panel = tk.Label(root, image=tk_img)
        img_panel.image = tk_img
        img_panel.pack(pady=10)

# 버튼
btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="이미지 업로드", command=upload_image, width=20).pack(side="left", padx=10)
tk.Button(btn_frame, text="YOLO 탐지 실행", command=detect_objects, width=20).pack(side="left", padx=10)

root.mainloop()
