import apprise

apobj = apprise.Apprise()
config = apprise.AppriseConfig()
config.add('/home/pi/.config/apprise')
apobj.add(config)
apobj.notify(
    body='YOUR DOORBELL IS BELLING GO RUN NOW!',
    title='DoorBell',
)