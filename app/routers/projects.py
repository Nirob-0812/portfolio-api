from fastapi import APIRouter
from typing import List, Dict

router = APIRouter(prefix="/api/projects", tags=["projects"])

# category keys: ml | dl | web | app | algo | robotics | automation | notebook
PROJECTS: List[Dict] = [
   
    #----------Deployed projects-------------
    {
        "title": "AI Assistant Platform (API + UI)",
        "description": "FastAPI backend with static JS UI for Q&A, images, and content.",
        "tech": ["Python", "FastAPI", "MCP", "LLM (Gemini/HF)"],
        "url": "https://nirob-0812.github.io/ai-task-ui/",
        "category": "deployed"
    },
    # -------- Deep Learning / CV ----------
    {
        "title": "Violence Detection",
        "description": "Deep-learning pipeline to detect violence in video frames.",
        "tech": ["Python", "PyTorch/TensorFlow", "OpenCV"],
        "url": "https://github.com/Nirob-0812/Violence-Detection",
        "category": "dl",
    },
    {
        "title": "Object Detection using YOLO",
        "description": "YOLOv8-based object detection with pre-trained weights and sample inference.",
        "tech": ["Python", "Ultralytics YOLOv8", "OpenCV"],
        "url": "https://github.com/Nirob-0812/Object_Detection_Yolo",
        "category": "dl",
    },
    {
        "title": "Handwritten Digit Classification (Keras)",
        "description": "Neural net for digit recognition; training loops and accuracy curves.",
        "tech": ["Python", "TensorFlow/Keras", "NumPy"],
        "url": "https://github.com/Nirob-0812/DL_Exercise/tree/master/Hand_Digit_Classification",
        "category": "dl",
    },
    {
        "title": "Activation Functions (DL)",
        "description": "Activation functions explained with plots and code.",
        "tech": ["Python", "NumPy", "Matplotlib"],
        "url": "https://github.com/Nirob-0812/DL_Exercise/tree/master/Activation_Function",
        "category": "dl",
    },

    # --------------- Machine Learning ---------------
    {
        "title": "ML Exercises",
        "description": "Hands-on ML exercises: regression, classification, model evaluation.",
        "tech": ["Python", "scikit-learn", "Pandas"],
        "url": "https://github.com/Nirob-0812/ML_Exercise",
        "category": "ml",
    },
    {
        "title": "Decision Tree (Exercises)",
        "description": "Decision-tree classification/regression with feature importance.",
        "tech": ["Python", "scikit-learn", "Pandas"],
        "url": "https://github.com/Nirob-0812/ML_Exercise/tree/master/Decision_tree_exercise",
        "category": "ml",
    },
    {
        "title": "Iris Flower Classification",
        "description": "Classic multi-class classification with visualizations.",
        "tech": ["Python", "scikit-learn", "Seaborn"],
        "url": "https://github.com/Nirob-0812/ML_Exercise/tree/master/Iris_flower_classification",
        "category": "ml",
    },
    {
        "title": "Random Forest (Exercises)",
        "description": "Ensemble modeling experiments and hyper-parameter tuning.",
        "tech": ["Python", "scikit-learn"],
        "url": "https://github.com/Nirob-0812/ML_Exercise/tree/master/Random_forest_exercsie",
        "category": "ml",
    },
    {
        "title": "SVM (Exercises)",
        "description": "Support Vector Machine experiments across kernels and C/γ sweeps.",
        "tech": ["Python", "scikit-learn", "NumPy"],
        "url": "https://github.com/Nirob-0812/ML_Exercise/tree/master/SVM_Exercise",
        "category": "ml",
    },
    {
        "title": "House Price Prediction (Multivariate)",
        "description": "Multiple linear regression with preprocessing and error analysis.",
        "tech": ["Python", "scikit-learn", "Pandas"],
        "url": "https://github.com/Nirob-0812/ML_Exercise/tree/master/House_price_Multivariate",
        "category": "ml",
    },
    {
        "title": "Insurance Cost Prediction",
        "description": "Predicting medical insurance charges with regression baselines.",
        "tech": ["Python", "scikit-learn", "Pandas"],
        "url": "https://github.com/Nirob-0812/ML_Exercise/tree/master/Insurance_Prediction",
        "category": "ml",
    },

    # --------------- ML Projects (problem sets) ---------------
    {
        "title": "Diabetes Prediction",
        "description": "End-to-end classification pipeline from the medical dataset.",
        "tech": ["Python", "scikit-learn", "Pandas"],
        "url": "https://github.com/Nirob-0812/ML-Project/tree/master/Diabates%20Prediction",
        "category": "ml",
    },
    {
        "title": "Heart Disease Prediction",
        "description": "Cardio-risk classifier with model comparison & metrics.",
        "tech": ["Python", "scikit-learn", "Matplotlib"],
        "url": "https://github.com/Nirob-0812/ML-Project/tree/master/Heart%20Disease%20Prediction",
        "category": "ml",
    },
    {
        "title": "Loan Status Prediction",
        "description": "Credit risk classification with feature encoding & validation.",
        "tech": ["Python", "scikit-learn", "Pandas"],
        "url": "https://github.com/Nirob-0812/ML-Project/tree/master/Loan%20Status%20Prediction",
        "category": "ml",
    },
    {
        "title": "Spam Mail Prediction",
        "description": "Email spam classifier; text preprocessing and logistic regression.",
        "tech": ["Python", "scikit-learn", "NLTK"],
        "url": "https://github.com/Nirob-0812/ML-Project/tree/master/Mail%20Prediction",
        "category": "ml",
    },

    # ------------------- Web -------------------
    {
        "title": "Portfolio (GitHub Pages)",
        "description": "Static portfolio site (earlier iteration).",
        "tech": ["HTML", "CSS"],
        "url": "https://github.com/Nirob-0812/mhnirob.github.io",
        "category": "web",
    },

    # ------------------- Apps (Flutter) -------------------
    {
        "title": "Booking App (Flutter)",
        "description": "Demo booking flows & state management.",
        "tech": ["Dart", "Flutter"],
        "url": "https://github.com/Nirob-0812/booking_app",
        "category": "app",
    },
    {
        "title": "CRUD with Firestore + GetX",
        "description": "Flutter CRUD app using Firestore & GetX.",
        "tech": ["Dart", "Flutter", "Firestore", "GetX"],
        "url": "https://github.com/Nirob-0812/Crud_With_Firestore_and_Getx",
        "category": "app",
    },
    {
        "title": "Todo App (Flutter)",
        "description": "Task manager with clean widgets and layout.",
        "tech": ["Dart", "Flutter"],
        "url": "https://github.com/Nirob-0812/Todo-App-Flutter",
        "category": "app",
    },
    {
        "title": "Calculator (Flutter)",
        "description": "Polished calculator UI & interaction.",
        "tech": ["Dart", "Flutter"],
        "url": "https://github.com/Nirob-0812/Calculator-Flutter-",
        "category": "app",
    },
    {
        "title": "UI from Figma (Flutter)",
        "description": "Pixel-perfect mobile UI recreated from Figma design.",
        "tech": ["Dart", "Flutter", "Figma"],
        "url": "https://github.com/Nirob-0812/UI_Design_from_Figma-Flutter-",
        "category": "app",
    },

    # --------------- Programming / Algorithms ---------------
    {
        "title": "CP Using Python",
        "description": "Competitive-programming solutions in clean, testable Python.",
        "tech": ["Python", "Algorithms", "DSA"],
        "url": "https://github.com/Nirob-0812/CP_Using_Python",
        "category": "algo",
    },
    {
        "title": "CP Using C++",
        "description": "Competitive-programming solutions in clean, testable Python.",
        "tech": ["C++", "Algorithms", "DSA"],
        "url": "https://github.com/Nirob-0812/Codeforces-cpp-Code",
        "category": "algo",
    },

    {
        "title": "All Varsity Tasks (C++)",
        "description": "C++ coursework and data-structures practice.",
        "tech": ["C++"],
        "url": "https://github.com/Nirob-0812/AllTaskOfVarsity",
        "category": "algo",
    },
    {
        "title": "acade.studio",
        "description": "C++ sandbox for algorithms and performance practice.",
        "tech": ["C++"],
        "url": "https://github.com/Nirob-0812/acade.studio",
        "category": "algo",
    },

    # ---------------- Robotics / ROS ----------------
    {
        "title": "ROS2 Workspace",
        "description": "C++ ROS2 workspace for robotics nodes and experiments.",
        "tech": ["C++", "ROS2"],
        "url": "https://github.com/Nirob-0812/ros2_ws",
        "category": "robotics",
    },

    # ---------------- Notebooks / Study ----------------
    {
        "title": "Colab Notebooks",
        "description": "Reusable Colab notebooks for ML/DL prototyping.",
        "tech": ["Python", "Colab", "Jupyter"],
        "url": "https://github.com/Nirob-0812/Colab_Notebooks",
        "category": "notebook",
    },
]


@router.get("/")
def get_projects():
    return PROJECTS
