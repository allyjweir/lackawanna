__author__ = 'allyjweir'
import os
import errno
import pdb
import textract
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.conf import settings


def make_sure_path_exists(path):
    try:
        os.makedirs(path)
    except OSError as exception:
        if exception.errno != errno.EEXIST:
            raise


def get_text(file):
    '''An InMemoryUploadedFile is passed to this function however Textract requires a path to a file in order to interact with it. To handle this, we will temporarily store the file, complete processing and then delete that temporary file.'''

    path = default_storage.save('tmp/' + file.name, ContentFile(file.read()))
    pdb.set_trace()

    text = None

    try:
        text = textract.process(os.path.join(settings.MEDIA_ROOT, path))
    except:
        print ("textract failed to read the file")

    # Still delete the temporary file if it fails to parse
    path = default_storage.delete('tmp/' + file.name)

    return text
