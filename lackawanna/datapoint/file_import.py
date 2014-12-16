__author__ = 'allyjweir'
import os
import errno
import pdb
import textract
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.conf import settings
import magic


def make_sure_path_exists(path):
    try:
        os.makedirs(path)
    except OSError as exception:
        if exception.errno != errno.EEXIST:
            raise


def get_text(InMemoryUploadedFile):
    '''An InMemoryUploadedFile is passed to this function however Textract requires a path to a file in order to interact with it. To handle this, we will temporarily store the file, complete processing and then delete that temporary file.'''

    path = default_storage.save('tmp/' + InMemoryUploadedFile.name, ContentFile(InMemoryUploadedFile.read()))

    text = None

    try:
        text = textract.process(os.path.join(settings.MEDIA_ROOT, path))
    except:
        print ("textract failed to read the file")

    # Still delete the temporary file if it fails to parse
    path = default_storage.delete('tmp/' + InMemoryUploadedFile.name)

    return text


'''
Django docs suggest trusting the user uploads a valid file but verify this to make sure that the file is safe to store.
This is done using the python-magic library.
'''
def is_file_valid(InMemoryUploadedFile):
    trusted = InMemoryUploadedFile.content_type

    m = magic.Magic(mime=True)
    verified = m.from_buffer(InMemoryUploadedFile.read())

    if trusted == verified:
        return True
    else:
        return False


'''
This matches the Mime type to one of the options in the database model for Datapoint.
Will extract the first section from the Mime Type (for example 'image' from 'image/png') and use this to define the file's type.

Using this as a reference: http://en.wikipedia.org/wiki/Internet_media_type#List_of_common_media_types
'''
def get_filetype(InMemoryUploadedFile):
    type = InMemoryUploadedFile.content_type
    type = type.split("/")

    if (type[1] == "pdf"):
        return type[1]  # Separate if statement due to "application/pdf". Diffferent structure to rest of Mime Types we care about.
    else:
        return type[0]  # Returns things like 'video', 'audio', 'image', 'text'


'''
Made under the assumption that the thing after the last "." will be the filetype.
This works even if it tries something silly like "file.jpg.pdf". It will still extract the "pdf" bit.
'''
def get_file_extension(InMemoryUploadedFile):
    filename = InMemoryUploadedFile.name
    filename = filename.split(".")

    return filename[-1]  # Return the last element, ie the filetype.
