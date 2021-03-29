from flask import Flask,jsonify,request
from flask_restful import reqparse, Resource , Api
import PIL.Image
#init 
app = Flask(__name__)

#wrap Api to the app
api= Api(app)

parser = reqparse.RequestParser()

#Resources
class Image(Resource):
    def post(self):
        #receive th request
        file = request.files['img']
        print(file)
        # Save the image 
        file.save('img_r.jpg')
        #print(file)
        #Read the image
        img= PIL.Image.open(file.stream)
        
        return jsonify({'img':[img.width,img.height]})
        # return jsonify({"t":"v"})
#endpoint
api.add_resource(Image,'/image')

if __name__ == '__main__':
    app.run(debug=True)

