# Weblate memory to translations
Convert Weblate translation memory to translations

## How to use

1. Log in to any instance of Weblate
2. Click on your profile -> Translation memory
3. Download the file you need as JSON
4. Go to the project itself
5. Open the original localization file (e.g. English)
6. Files -> Download translation
7. Download the script
8. Place the script and the two files in the same folder
9. Adjust the filenames at the end of the script, make sure to match the output locale code you need
10. Run the script
11. Go back to the project
12. Open the target localization file (your language)
13. Files -> Upload translation
14. Select the output file and options you prefer
15. Upload!

## Why

For some reason, a Weblate project I translated suddenly lost my translations for one file. After a short panic, I found out that my profile has automatically stored the translation memory based on my previous work. 

Tried downloading and uploading it directly, both JSON and TMX formats failed to upload. Then I downloaded the JSON file, compared the structure to the original localization file and wrote a script to automatically generate translations from it.
