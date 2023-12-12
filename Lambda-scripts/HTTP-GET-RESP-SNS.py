import requests
import boto3
def sns_message():
     sns_topic_arn = '<provide your sns topic arn>'
     sns_client = boto3.client('sns', region_name='us-west-1')
     message = "Jenkins server is down! Please investigate."
     sns_client.publish(
         TargetArn=sns_topic_arn,
         Message=message,
         Subject="Jenkins Server Down"
     )
 
def check_jenkins_status():
    jenkins_url = '<Specify your URL>'
    global sns_topic_arn
    try:
        response = requests.head(jenkins_url, auth() timeout=20)  # Increase timeout if needed
        if response.status_code == 200:
            print("Jenkins server is up!")
        else:
            sns_message()
    except requests.exceptions.Timeout:
        sns_message()
        print("Timeout occurred. Jenkins server might be slow to respond.")
        # Handle timeout scenario here, for example, send a notification about timeout
    except requests.exceptions.RequestException as e:
        sns_message()
        print("Error accessing Jenkins server:", e)
        # Handle other request exceptions here
    except Exception as e:
        sns_message()
        print("Other error occurred:", e)
        # Handle other exceptions
       
def lambda_handler(event, context):
    try:
        check_jenkins_status()
    except Exception as e:
        print("Lambda function error:", e)
# Manually invoke the lambda_handler function for testing
lambda_handler(None, None)
