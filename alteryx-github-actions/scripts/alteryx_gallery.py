from AlteryxGallery import AlteryxGalleryAPI as ag
from decouple import config
import os

client_key = config('client_key')
client_secret = config('client_secret')
apiLocation = config('gallery_url')


# build list of workflows for publishing
workflows = []
cwd = os.getcwd()
for root, dirs, files in os.walk(cwd):
	for file in files:
		if file.endswith(".yxmd"):
			workflows.append(os.path.join(cwd, file))

# TODO: loging check for files
print(workflows)


# Connect to Gallery and publish workflow
con = ag.Gallery(apiLocation, client_key, client_secret)

print(con)



# subs = con.subscription()

# print(f"test output of subscriptions:")
# # print(con.subscription())
# print(subs)
