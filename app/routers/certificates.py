from fastapi import APIRouter
from typing import List, Dict

router = APIRouter(prefix="/api/certificates", tags=["certificates"])

CERTIFICATES: List[Dict] = [
    {
        "title": "Python (Basic)",
        "issuer": "HackerRank",
        "date": "2023-03",
        "image": "/static/img/certificates/Python_basic.png",
        "verify_url": "https://www.hackerrank.com/certificates/2f6a8b6e0a53"
    },
    {
        "title": "Problem Solving (Basic)",
        "issuer": "HackerRank",
        "date": "2024-05",
        "image": "/static/img/certificates/problem_solving_basic.png",
        "verify_url": "https://www.hackerrank.com/certificates/8500e2842179"
    },
    {
        "title": "Intro to TensorFlow",
        "issuer": "DeepLearning.AI / Coursera",
        "date": "2023-11",
        "image": "/static/img/certificates/Intro_Tensorflow.png",
        "verify_url": "https://www.coursera.org/account/accomplishments/verify/UW54FB5KLFQX"
    },
    {
        "title": "Convolutional Neural Networks",
        "issuer": "DeepLearning.AI / Coursera",
        "date": "2024-02",
        "image": "/static/img/certificates/CNN.png",
        "verify_url": "https://www.coursera.org/account/accomplishments/verify/B3YSRJRSHLH4"
    },
    {
        "title": "Natural Language Processing",
        "issuer": "DeepLearning.AI / Coursera",
        "date": "2024-04",
        "image": "/static/img/certificates/NLP.png",
        "verify_url": "https://www.coursera.org/account/accomplishments/verify/XW8C7DPEULNF"
    },
    {
        "title": "Machine Learning",
        "issuer": "Stanford / Coursera",
        "date": "2023-09",
        "image": "/static/img/certificates/ML.png",
        "verify_url": "https://www.coursera.org/account/accomplishments/verify/APD3VTT52M8X"
    },
]

@router.get("/")
def get_certificates():
    return CERTIFICATES
