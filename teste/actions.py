# -*- coding: utf-8 -*-
"""
--------
Actions
--------

Este arquivo contem as Custom Actions do Filebrowser.

Biografia:

* _a link: http://django-filebrowser.readthedocs.org/en/latest/admin.html#custom-actions

Autores: 

* Alisson Barbosa Ferreira <alissonbf@hotmail.com>
    
Data:

==============  ==================
Criação         Atualização
==============  ==================
04/02/2015      04/02/2015
==============  ==================

---------------
"""

# PYTHON IMPORTS
import os
from tempfile import NamedTemporaryFile

# DJANGO IMPORTS
from django.http import HttpResponseRedirect
from django.utils.translation import ugettext_lazy as _
from django.contrib import messages
from django.core.files import File

# FILEBROWSER IMPORTS
from filebrowser.settings import VERSION_QUALITY, STRICT_PIL

# PIL import
if STRICT_PIL:
    from PIL import Image
else:
    try:
        from PIL import Image
    except ImportError:
        import Image


def applies_to_all_images(fileobject):
    "Set image filetype"
    return fileobject.filetype == 'Image'

def applies_to_all_videos(fileobject):
    "Set video filetype"
    return fileobject.filetype == 'Video'

def applies_to_all_files(fileobject):
    "Set all filetype"
    return True

def convert_image(request, fileobjects, operation):
    "Transpose image"
    for fileobject in fileobjects:
        root, ext = os.path.splitext(fileobject.filename)
        f = fileobject.site.storage.open(fileobject.path)
        im = Image.open(f)
        new_image = im.convert(operation)
        tmpfile = File(NamedTemporaryFile())

        try:
            new_image.save(tmpfile, format=Image.EXTENSION[ext], quality=VERSION_QUALITY, optimize=(os.path.splitext(fileobject.path)[1].lower() != '.gif'))
        except IOError:
            new_image.save(tmpfile, format=Image.EXTENSION[ext], quality=VERSION_QUALITY)

        try:
            saved_under = fileobject.site.storage.save(fileobject.path, tmpfile)
            if saved_under != fileobject.path:
                fileobject.site.storage.move(saved_under, fileobject.path, allow_overwrite=True)
            fileobject.delete_versions()
        finally:
            tmpfile.close()
            f.close()

        messages.add_message(request, messages.SUCCESS, _("Action applied successfully to '%s'" % (fileobject.filename)))



def make_monochrome(request, fileobjects):
    """
        Faz a imagem ficar preto e branco
    """
    convert_image(request, fileobjects, 'L')

make_monochrome.short_description = u'Tornar monocromático'
make_monochrome.applies_to = applies_to_all_images


def flv_to_mp4(request, fileobjects):
    """
        Converte um arquivo de video
    """
    pass

flv_to_mp4.short_description = u'Converter flv para mp4'
flv_to_mp4.applies_to = applies_to_all_files