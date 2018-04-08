# bilddagboken-dayviews-exporter
Exports your images from Dayviews (previously known as Bilddagboken)

## How-to
1. Under settings, make your profile visible to all visitors
2. Go to the first image that you have uploaded and look in the URL of the page. Here you will see the ID of the first image. Assign this ID to imageId in script.py 
3. Add the name of your account in script.py
4. Run the script. All your images are now downloaded one by one to the output folder.

If the script somehow fails in the middle of downloading your images, simply look at the last printed URL in your console. Assign this ID to imageId and re-run the script.
