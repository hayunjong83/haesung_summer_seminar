# 💡 여름방학 해성여자고등학교 캡스톤 탐구 프로젝트

---

## 📌 프로젝트 개요

- **프로젝트 기간**: 2025년 7월 22일 ~ 2025년 7월 25일  
- **참여 학생**: 해성여자고등학교 여름방학 특별 탐구 활동

### 🎯 문제 인식

학교 정문 앞에 **킥보드가 무질서하게 많이 놓여 있어** 통행에 위험을 느끼는 일이 많았습니다.  
이 문제를 인공지능 기술로 탐지하고 해결 방안을 모색하기 위해,  
**YOLO 객체 탐지 모델을 활용해 킥보드의 수를 세는 시스템**을 만들어 보았습니다.

---

## 📂 학습 데이터 및 YOLO 모델

- 🔗 **데이터셋 출처 (Roboflow)**:  
  [https://universe.roboflow.com/your-workspace/kickboard-detection](https://universe.roboflow.com/your-workspace/kickboard-detection)

- 📘 **YOLOv8 학습 코드 (Google Colab)**:  
  [https://colab.research.google.com/drive/your_colab_link](https://colab.research.google.com/drive/your_colab_link)

### 💬 추가 설명

YOLOv8을 사용하여 직접 킥보드 탐지 모델을 학습하였습니다.  
이미지 전처리, Bounding Box 정제, mAP 성능 확인 등의 과정을 거쳤고,  
소형 모델을 활용해 비교적 빠르고 정확하게 킥보드를 탐지할 수 있도록 설정하였습니다.

---

## 🖼️ YOLO 탐지 결과 비교

| 일반 YOLO 모델 | 학습한 킥보드 전용 YOLO 모델 |
|----------------|-----------------------------|
| ![일반 YOLO 결과](kickboard_results1.jpg) | ![학습 모델 결과](kickboard_results2.jpg) |

### 🧪 실행 방법

아래 코드를 사용하여 원하는 이미지에서 킥보드를 탐지할 수 있습니다:

```bash
python test.py
```

## 💭 느낀 점과 아쉬운 점
인공지능이 생각보다 친숙하다는 걸 알게 되었어요.
처음에는 어려울 줄 알았지만, 코드를 하나하나 따라 하면서 충분히 이해할 수 있었습니다.

내가 발견한 문제를 스스로 해결해보는 경험이 뜻깊었어요.
학교 앞 킥보드 문제처럼 실제 생활 속의 문제를 AI로 분석해보니 정말 뿌듯했습니다.

시간이 더 있었다면 실시간 CCTV 영상 분석까지 해보고 싶었어요.
YOLO가 이미지를 잘 분석해주는 걸 보면서, 이걸 실시간으로 연결하는 데까지 확장하고 싶다는 욕심이 생겼습니다.