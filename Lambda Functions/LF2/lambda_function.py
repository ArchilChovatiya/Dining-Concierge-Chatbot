
import boto3
from botocore.exceptions import ClientError

def sendEmail(restaurants,userPreferences):
    # This address must be verified with Amazon SES.
    sender = "aniketsaliya123@gmail.com"
    
    subject = "Here are your Restaurant Recommendations!"
    region = "us-east-1"
    
    cuisine=userPreferences['cuisine']
    people=userPreferences['people']
    date=userPreferences['date']
    time=userPreferences['time']
    recipient=userPreferences['email']

        
    # The email body for recipients with non-HTML email clients.
    body = "<h3> Hello! There, Here are some " + str(cuisine) + " restaurant suggestions for " + str(people) + " people, for " + str(date) + " at " + str(time) + "</h3><br><br>" 
    
    body += "<ol>"
    for  restaurant in restaurants:
        address=""
        for val in restaurant['address']:
            address+=val+", "
        body +='''<li>
        Name: {name} <br>
        Address: {address} <br>
        Phone: {phone} <br>
        Rating: {rating}/5.0 <br>
        </li>'''.format(name=restaurant["restaurent"], address=address[0:-2], phone=restaurant["phone"], rating= restaurant["rating"])
    body +="</ol>"
    charset = "UTF-8"
    # Create a new SES resource and specify a region.
    client = boto3.client('ses',region_name=region)
    # Try to send the email.
    try:
        #Provide the contents of the email.
        response = client.send_email(
            Destination={
                'ToAddresses': [
                    recipient,
                ],
            },
            Message={
                'Body': {
                    'Html': {
                        'Charset': charset,
                        'Data': body,
                    },
                },
                'Subject': {
                    'Charset': charset,
                    'Data': subject,
                },
            },
            Source=sender,

           
        )
    # Display an error if something goes wrong.	
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        print("Email sent! Message ID:"),
        print(response['MessageId'])