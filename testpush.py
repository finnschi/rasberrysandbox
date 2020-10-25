import apprise

# Create an Apprise instance
apobj = apprise.Apprise()

# Add all of the notification services by their server url.
# A sample email notification:
apobj.add('tgram://1308991529:AAG6R_lZ5RMEjOirzQt3cQIj00IPTjpRC-I/-433421664')

##https://api.telegram.org/bot1308991529:AAG6R_lZ5RMEjOirzQt3cQIj00IPTjpRC-I/getUpdates
# Then notify these services any time you desire. The below would
# notify all of the services loaded into our Apprise object.
apobj.notify(
    body='YOUR DOORBELL IS BELLING GO RUN NOW!',
    title='DoorBell',
)