import apprise
apobj = apprise.Apprise()
config = apprise.AppriseConfig()
config.add('/home/pi/.config/apprise')
apobj.add(config)
def button_callback(channel):
    apobj.notify(
        body='YOUR DOORBELL IS BELLING GO RUN NOW!',
        title='DoorBellBot_v0.1',
    )