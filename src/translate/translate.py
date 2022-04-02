import re
from google.cloud import translate

def translate_text(text, project_id="holycalorie"):
  if(text != None):
    client = translate.TranslationServiceClient()
    location = "global"
    parent = f"projects/{project_id}/locations/{location}"

    response = client.translate_text(
        request={
            "parent": parent,
            "contents": [text],
            "mime_type": "text/plain",
            "source_language_code": "pl",
            "target_language_code": "en",
        }
    )

    for translation in response.translations:
        print("Translated text: {}".format(translation.translated_text))

    return response.translations[0].translated_text

def remove_alternatives(text):
    result = re.sub("\s(or|and)\s.*", "", text)
    result = re.sub("\(.*\) ", "", result)
    result = re.sub("\*", "", result)

    return result
