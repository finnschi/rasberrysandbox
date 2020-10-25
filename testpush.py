import apprise

# Create an Apprise instance
apobj = apprise.Apprise()
config = apprise.AppriseConfig()
config.add('/home/pi/.config/apprise.yml')
apobj.add(config)
# Add all of the notification services by their server url.
# A sample email notification:
# Then notify these services any time you desire. The below would
# notify all of the services loaded into our Apprise object.
apobj.notify(
    body='YOUR DOORBELL IS BELLING GO RUN NOW!',
    title='DoorBell',
    tag="telegram",
)