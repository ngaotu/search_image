# app.py
from flask import Flask, request, jsonify, render_template
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
from PIL import Image
import torch

app = Flask(__name__)

# Load mô hình CLIP
model = SentenceTransformer('clip-ViT-B-32')

# Load chỉ mục FAISS
index = faiss.read_index('image_embeddings.index')

# Đường dẫn đến thư mục hình ảnh
image_folder = '/path/to/images'
image_files = sorted(glob(os.path.join(image_folder, '*.jpg')))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    query = request.files.get('query')
    text = request.form.get('text')
    if query:
        # Nếu query là hình ảnh
        img = Image.open(query.stream)
        query_embedding = model.encode(img, convert_to_tensor=True)
    elif text:
        # Nếu query là văn bản
        query_embedding = model.encode(text, convert_to_tensor=True)
    else:
        return jsonify({'results': []})
    
    # Tìm kiếm với FAISS
    query_embedding = query_embedding.detach().numpy().astype('float32')
    distances, indices = index.search(query_embedding.reshape(1, -1), 5)
    
    # Lấy đường dẫn hình ảnh
    results = [image_files[i] for i in indices.flatten()]
    
    return jsonify({'results': results})

if __name__ == '__main__':
    app.run(debug=True)