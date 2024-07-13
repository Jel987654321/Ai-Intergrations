
import tensorflow as tf

# Load a pre-trained TensorFlow model (example: MobileNetV2) 
model = tf.keras.applications.MobileNetV2()

# Perform inference (example: classify an image)
image_path = 'path/to/your/image.jpg'
image = tf.keras.preprocessing.image.load_img(image_path, target_size=(224, 224))
image_array = tf.keras.preprocessing.image.img_to_array(image)
image_array = tf.keras.applications.mobilenet_v2.preprocess_input(image_array)
predictions = model.predict(tf.expand_dims(image_array, axis=0))
decoded_predictions = tf.keras.applications.mobilenet_v2.decode_predictions(predictions, top=3)[0]

# Print top 3 predictions
for _, label, score in decoded_predictions:
    print(f'{label}: {score:.2f}')
