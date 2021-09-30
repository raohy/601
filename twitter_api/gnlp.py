from google.api_core.client_options import ClientOptions
from google.cloud import automl_v1

def inline_text_payload(file_path):
    with open(file_path, 'rb') as ff:
        content = ff.read()
    return {'text_snippet': {'content': content, 'mime_type': 'text/plain'} }

def pdf_payload(file_path):
    return {'document': {'input_config': {'gcs_source': {'input_uris': [file_path] } } } }

def get_prediction(file_path, model_name):
    options = ClientOptions(api_endpoint='automl.googleapis.com')
    prediction_client = automl_v1.PredictionServiceClient(client_options=options)
    payload = inline_text_payload(file_path)
    params = {}
    request = prediction_client.predict(name=model_name, payload=payload)
    return request 

if __name__ == '__main__':
    file_path='data2.csv'
    model_name='projects/209609468506/locations/us-central1/models/TST1068749491454083072'
    print(get_prediction(file_path, model_name))
