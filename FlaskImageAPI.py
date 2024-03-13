from flask import Flask, request

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        return "No file part in the request", 400
    
    file = request.files['file']
    
    if file.filename == '':
        return "No selected file", 400
    
    # You can save the file to disk if needed
    # file.save('uploaded_image.jpg')
    
    # Or you can read the file into memory and store it in a variable
    image_data = file.read()
    
    # Now you can perform further processing with image_data
    
    return "Image uploaded successfully", 200

if __name__ == '__main__':
    app.run(debug=True)
