import boto3
import json

palabras=["neonazi", "Estúpido,", "majadero,", "traidor", "Imbécil!"]

def get_text(image, bucket):

    client=boto3.client('rekognition','us-east-1')
    response=client.detect_text(Image={'S3Object':{'Bucket':bucket,'Name':image}})
                        
    textDetections=response['TextDetections']

    for t in response['TextDetections']:
        print(t['DetectedText'] + ':' + str(t['Confidence']))
    
    print ('Detected text\n----------')
    for text in textDetections:
        for i in palabras:
            if i.lower() == text['DetectedText'].lower():
                print ('Palabrota detectada: ' + text['DetectedText'])
                print ('Confidence: ' + "{:.2f}".format(text['Confidence']) + "%")
                print()
    return len(textDetections)

    
def main():

    bucket='elbucketalejandro'
    image='DuFHSk7WoAABzrk.jpeg'
    text_count=get_text(image,bucket)
    print("Nº palabras: " + str(text_count))

main()