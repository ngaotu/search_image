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
# @app.route('/search', methods=['POST'])
# def search():
#     image = request.files.get('image')
#     text = request.form.get('text')
#     results = []

#     if image:
#         image.save("temp_image.jpg")
#         results = image_search.search_by_image("temp_image.jpg")
#     elif text:
#         results = image_search.search_by_text(text)

#     return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)
