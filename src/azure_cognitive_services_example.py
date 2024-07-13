import os
from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import ImageAnalysisMode
from msrest.authentication import CognitiveServicesCredentials
from dotenv import load_dotenv

load_dotenv()

# Replace with your Azure Cognitive Services endpoint and key
endpoint = os.getenv('AZURE_COGNITIVE_SERVICES_ENDPOINT')
subscription_key = os.getenv('AZURE_COGNITIVE_SERVICES_KEY')

credentials = CognitiveServicesCredentials(subscription_key)
client = ComputerVisionClient(endpoint, credentials)

# Example image URL for analysis
image_url = "https://example.com/image.jpg"

features = ["categories", "description"]
image_analysis = client.analyze_image(image_url, visual_features=features, details=None, language='en')

if image_analysis.description.captions:
    print(f"Description: {image_analysis.description.captions[0].text}")
else:
    print("No description found.")
