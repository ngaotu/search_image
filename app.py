from flask import Flask, request, jsonify, render_template
# from models.model import CLIPModel, FAISSIndex, ImageSearch

app = Flask(__name__)

# Initialize models
# clip_model = CLIPModel()
# faiss_index = FAISSIndex(dimension=512)
# image_search = ImageSearch(clip_model, faiss_index)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route("/search", methods=["POST"])
def search():
    # Xử lý tìm kiếm và lấy danh sách ảnh
    image_urls = [
        "https://mir-s3-cdn-cf.behance.net/project_modules/fs/e01a1c145370057.629d9d0a30f4a.png",  # Thay bằng URL ảnh thật
        "https://mir-s3-cdn-cf.behance.net/project_modules/fs/e01a1c145370057.629d9d0a30f4a.png",
        "https://mir-s3-cdn-cf.behance.net/project_modules/fs/e01a1c145370057.629d9d0a30f4a.png",
        "https://mir-s3-cdn-cf.behance.net/project_modules/fs/e01a1c145370057.629d9d0a30f4a.png"
    ]
    return render_template("result.html", image_urls=image_urls)

if __name__ == '__main__':
    app.run(debug=True)
