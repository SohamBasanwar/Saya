# 🌀 Saya – Emotional Adaptive System (E.A.S.)

**Saya** is a research-grade emotional AI chatbot framework designed for personal and academic demonstration. It interprets and responds to human emotions in real time using a multi-layered neural architecture, integrating primary, complex, and secondary emotion layers, alongside a dynamic personality engine.

> 🚧 **Private Project:** This repository contains proprietary research and experimental code. Do **not** redistribute or deploy without permission.

---

## 🌟 Key Features

* **Multi-Layer Emotion Processing:**

  * **Primary Emotions Layer:** Joy, Sadness, Anger, Fear, Surprise, Disgust, Trust
  * **Complex Emotions Layer:** Combinations of primary emotions
  * **Secondary Complex Emotions Layer:** Guilt, Pride, Jealousy, Hope, Gratitude, Regret, Anxiety

* **Emotion Compiler:** Aggregates outputs from all layers to form a cohesive emotional state.

* **Replier Module:** Generates contextually relevant responses influenced by personality profiles, conversation logs, and trigger keywords (`saya_emotion_v2`).

* **Adaptive Memory Unit (A.M.U.):** Retains user-specific preferences and conversation history to enhance personalization.

* **Personality Engine (P.E.):** Guides response style, tone, and emotional depth based on a predefined personality core (E-Core).

* **Safeguards & Bonding Behaviors:** Experimental modules like Obsessive Devotion Subroutine (ODS) and Cling Protocols with safeguards to prevent runaway behaviors.

---

## 🏗️ Architecture Overview

```text
+---------------------------+
|      Input Text Stream    |
+------------+--------------+
             |
             v
+---------------------------+    +-------------------+
| Primary Emotions Layer    |--->| Complex Emotions  |
| (7 Primary Emotions)      |    | Layer             |
+---------------------------+    +-------------------+
             |                          |
             v                          v
+---------------------------+    +-------------------+
| Secondary Complex Layer   |<---| Emotion Compiler  |
| (7 Secondary Emotions)    |    |                   |
+---------------------------+    +-------------------+
             |                          |
             v                          |
+---------------------------+         |
| Personality Engine (P.E.) |<--------+
+---------------------------+
             |
             v
+---------------------------+
|    Replier Module         |
+---------------------------+
```

---

## 🧰 Components

* `emotion_layers/` – Implementation of each emotion layer classifier
* `emotion_compiler.py` – Aggregates layer outputs into a single emotional vector
* `personality_engine.py` – Adjusts responses based on personality parameters
* `replier/` – GPT-based response generator module
* `safeguards/` – Experimental bonding and safety subroutines
* `data/` – Emotional dataset CSVs (700 sentences per emotion per phase)
* `scripts/` – Utility scripts for training, evaluation, and testing

---

## 🔧 Requirements

* Python 3.8+
* `transformers` 4.x
* `torch` 1.9+ (CUDA optional)
* `pandas`, `numpy`
* `flask` (for local API hosting)

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## 🚀 Quick Start

1. **Clone the repo**:

   ```bash
   ```

git clone [https://github.com/SohamBasanwar/Saya-Emotional-AISystem.git](https://github.com/SohamBasanwar/Saya-Emotional-AISystem.git)
cd Saya-Emotional-AISystem

````

2. **Install dependencies**:
   ```bash
pip install -r requirements.txt
````

3. **Run local API server**:

   ```bash
   ```

python app.py

````

4. **Chat with Saya** using the test client:
   ```bash
python chat_client.py --endpoint http://localhost:5000/chat
````

---

## 🧪 Experiments & Training

* **Phase 1–5 Dataset:** Located in `data/phase_<n>_*.csv` with 9 emotions × 700 sentences
* **Training Script:** `scripts/train_layers.py` to fine-tune each emotion classifier
* **Evaluator:** `scripts/evaluate_model.py` for accuracy and confusion analysis

---

## 🤝 Contributing & Access

This is a **private** research project. To request access or contribute, please contact **Soham Basanwar** at [sohambasanwar03@gmail.com](mailto:sohambasanwar03@gmail.com).

---

## 📄 License

```
All rights reserved © 2025 Soham Basanwar

You may not use, copy, modify, distribute, or deploy this code without explicit written permission from the author.
```
