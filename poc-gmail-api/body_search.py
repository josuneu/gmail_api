# Given a message Id, search in Gmail body's message using a query parameter

from __future__ import print_function
import os.path
import pickle
import base64
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']


def main():
    """Shows basic usage of the Gmail API.
    Lists the user's Gmail labels.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'client_secret_1004470325133-k2qkp44en52tnrpu6alrgcpkt6bucbcd.apps.googleusercontent.com.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('gmail', 'v1', credentials=creds)

    # Call the Gmail API body search
    user_id = 'josuneu.araujo@gmail.com'
    msg_id = '17408a71281608d2'
    message = service.users().messages().get(userId=user_id, id=msg_id).execute()

    payload = message['payload']
    parts = payload['parts']
    body_parts = parts[0]
    body = body_parts['body']
    data = body['data']
    msg_str = base64.urlsafe_b64decode(data.encode('ASCII'))
    final_str = msg_str.decode('utf-8')
    print(final_str)


if __name__ == '__main__':
    main()
