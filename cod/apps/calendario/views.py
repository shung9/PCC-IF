#from django.shortcuts import render, redirect
#from google.oauth2.credentials import Credentials
#from google_auth_oauthlib.flow import Flow
#from googleapiclient.discovery import build


#def ver(request):
 #   return render(request, 'turmas/rew.html')

#def google_auth(request):
 #   flow = Flow.from_client_secrets_file(
  #      'C:/Users/Emerson/Desktop/github OFC/PCC-IF/cod/apps/calendario/credentials.json',
   #     scopes=['https://www.googleapis.com/auth/calendar'],
   #     redirect_uri=request.build_absolute_uri('/google-auth-redirect')
    #)

    #if 'code' in request.GET:
     #   flow.fetch_token(authorization_response=request.build_absolute_uri())
      #  credentials = flow.credentials  
       # request.session['google_credentials'] = credentials.to_json()

       # return redirect('/google-calendar')

    #else:
     #   auth_url, _ = flow.authorization_url(prompt='consent')
      #  return redirect(auth_url)

#def google_auth_redirect(request):
   # return render(request, 'google_auth_redirect.html')

#def google_calendar(request):
   # credentials = Credentials.from_authorized_user_info(json.loads(request.session['google_credentials']))
    #service = build('calendar', 'v3', credentials=credentials)
    #events_result = service.events().list(calendarId='primary', timeMin='2022-04-10T00:00:00Z', timeMax='2022-04-17T00:00:00Z', singleEvents=True, orderBy='startTime').execute()
    #events = events_result.get('items', [])
    #return render(request, 'google_calendar.html', {'events': events})
