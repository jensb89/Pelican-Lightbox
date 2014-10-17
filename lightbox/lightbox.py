"""
Lightbox
------------------------

This plugins adds a 'data-lightbox' attribute to all links on pictures,
which is needed when using the lightbox2 javascript (http://lokeshdhakar.com/projects/lightbox2/)

"""

from os import path
from pelican import signals
from bs4 import BeautifulSoup

import logging
logger = logging.getLogger(__name__)

def content_object_init(instance):

    if instance._content is not None:
        content = instance._content
        soup = BeautifulSoup(content)

        if 'img' in content:
            for img in soup('img'):
                logger.debug('PATH: %s', instance.settings['PATH'])
                logger.debug('img.src: %s', img['src'])

                img_path, img_filename = path.split(img['src'])

                logger.debug('img_path: %s', img_path)
                logger.debug('img_fname: %s', img_filename)

                lightbox_style = 'image' # All images on the same page are combined into a set

                fig = img.find_parent('a')
                if fig:
                    if not(fig.get('data-lightbox')):
                        fig['data-lightbox'] = lightbox_style
                        fig['data-title'] = img_filename

        instance._content = soup.decode()


def register():
    signals.content_object_init.connect(content_object_init)
