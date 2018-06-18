# -*- coding: utf-8 -*-

# ############################################################################
# This example demonstrates how to use the MultipartEncoderMonitor to create a
# progress bar using clint.
# ############################################################################

from clint.textui.progress import Bar as ProgressBar
from requests_toolbelt import MultipartEncoder, MultipartEncoderMonitor

import requests


def create_callback(encoder):
    encoder_len = encoder.len
    bar = ProgressBar(expected_size=encoder_len, filled_char='=')

    def callback(monitor):
        bar.show(monitor.bytes_read)

    return callback


def create_upload():
    return MultipartEncoder({
            'file': ("test.img", open('test.img', 'rb'), 'text/plain')
        })


if __name__ == '__main__':
    encoder = create_upload()
    callback = create_callback(encoder)
    monitor = MultipartEncoderMonitor(encoder, callback)
    r = requests.post('http://localhost:9000/upload', data=monitor,
                      headers={'Content-Type': monitor.content_type})
    print('\nUpload finished! (Returned status {0} {1})'.format(
        r.status_code, r.reason
        ))
