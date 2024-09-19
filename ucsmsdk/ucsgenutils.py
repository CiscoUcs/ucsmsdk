# Copyright 2015 Cisco Systems, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#  http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


"""
This module contains the SDK general utilities.
"""

from __future__ import print_function
from __future__ import unicode_literals

import os
import sys
import platform
import re
import subprocess

import logging
import six
from six.moves import range

log = logging.getLogger('ucs')

from .ucsexception import UcsWarning, UcsValidationException

AFFIRMATIVE_LIST = ['true', 'True', 'TRUE', True, 'yes', 'Yes', 'YES']

reserved_keywords = [
    "and", "as", "assert", "break", "class", "continue", "def", "del", "elif",
    "else", "except", "exec", "finally", "for", "from", "global", "if",
    "import", "in", "is", "lambda", "not", "or", "pass", "print", "raise",
    "return", "try", "while", "with", "yield"]


def is_python_reserved(word):
    """
    Check if it is python reserved word.
    """

    return word in reserved_keywords


def to_safe_prop(word):
    """
    Check if it is python reserved word, if yes returns word after prefixing
    it with 'r_'
    """
    return 'r_' + word if is_python_reserved(word) else word


def from_safe_prop(word):
    """
    removes 'r_' from word.
    """
    return re.sub("^r_", "", word)


def to_python_propname(word):
    """
    Converts any word to lowercase word separated by underscore
    """

    return re.sub('_+', '_',
                  re.sub('^_', '',
                    re.sub(r'[/\-: +]', '_',
                      re.sub('([A-Z]+)([A-Z])([a-z0-9])', r'\g<1>_\g<2>\g<3>',
                        re.sub('([a-z0-9])([A-Z])', r'\g<1>_\g<2>',(word,
                          to_safe_prop(word))[is_python_reserved(word)])
                             )))).lower()


def convert_to_python_var_name(name):
    """converts a ucs server variable to python recommended format

    Args:
        name (str): string to be converted to python recommended format
    """

    pattern = re.compile(r"(?<!^)(?=[A-Z])")
    python_var = re.sub(pattern, '_', name).lower()
    if python_var != "class":
        return python_var
    else:
        return "class_"


def word_l(word):
    """ Method makes the first letter of the given string as lower case. """

    return word[0].lower() + word[1:]


def word_u(word):
    """ Method makes the first letter of the given string as capital. """

    return word[0].upper() + word[1:]


def make_dn(rn_array):
    """ Method forms Dn out of array of rns. """

    return '/'.join(rn_array)


class FileReadStream(object):
    """Internal class to show the progress while reading file."""

    def __init__(self, path, progress_cb):
        self._fhandle = open(path, 'rb')
        # Set the seek positin to the end of the file
        # and calcualte the total file size
        self._fhandle.seek(0, os.SEEK_END)
        self._tsize = self._fhandle.tell()

        # Reset the position to the beginning of the file
        self._fhandle.seek(0)

        self._progress_cb = progress_cb

    def __len__(self):
        return self._tsize

    def read(self, size):
        data = self._fhandle.read(size)
        self._progress_cb(self._tsize, size)
        return data


class Progress(object):
    """ Internal class to show the progress in chunks of custom percentage """

    def __init__(self, interval=10):
        self._seen = 0.0
        self._interval = interval
        self._percent = interval

    def update(self, total, size, name=None):
        from sys import stdout

        self._seen += size
        percent = self._seen * 100 / total
        if percent < self._percent:
            return
        status = r"%10d  [%3.2f%%]" % (self._seen, percent)
        status = status + chr(8) * (len(status) + 1)
        stdout.write("\r%s" % status)
        stdout.flush()
        self._percent += self._interval


def download_file(driver, file_url, file_dir, file_name, progress=Progress()):
    """
    Downloads the file from web server

    Args:
        driver (UcsDriver)
        file_url (str): url to download the file
        file_dir (str): The directory to download to
        file_name (str): The destination file name for the download

    Returns:
        None

    Example:
        driver = UcsDriver()\n
        download_file(driver=UcsDriver(), file_url="http://fileurl", file_dir='/home/user/backup', file_name='my_config_backup.xml')
    """

    import os

    destination_file = os.path.join(file_dir, file_name)
    response = driver.post(uri=file_url, read=False)

    if sys.version_info > (3, 0):
        # Python 3 code in this block
        file_size = int(response.headers['Content-Length'])
    else:
        # Python 2 code in this block
        file_size = int(response.info().getheaders("Content-Length")[0])

    print("Downloading: %s Bytes: %s" % (file_name, file_size))

    file_handle = open(destination_file, 'wb')
    block_sz = 64
    while True:
        r_buffer = response.read(128 * block_sz)
        if not r_buffer:
            break

        file_handle.write(r_buffer)
        progress.update(file_size, len(r_buffer))
    print('Downloading Finished.')
    file_handle.close()


def upload_file(driver, uri, file_dir, file_name, progress=Progress()):
    """
    Uploads the file on web server

    Args:
        driver (UcsDriver)
        uri (str): url to upload the file
        file_dir (str): The directory to download to
        file_name (str): The destination file name for the download

    Returns:
        None

    Example:
        driver = UcsDriver()\n
        upload_file(driver=UcsDriver(), uri="http://fileurl", file_dir='/home/user/backup', file_name='my_config_backup.xml')
    """
    stream = FileReadStream(os.path.join(file_dir, file_name), progress.update)
    response = driver.post(uri, data=stream)
    if not response:
        raise ValueError("File upload failed.")


def read_in_chunks(file_object, chunk_size=10*1024*1024):
    """(generator) to read a file piece by piece.
    Default chunk size: 10MB."""
    while True:
        data = file_object.read(chunk_size)
        if not data:
            break
        yield data


def generate_uri_for_chunks(uri, counter, flag):
    """(generator) to generate uri for chunks
     and return URI"""
    index = uri.rfind("/")
    if flag == 0 :
        res = uri[ : index ] + "/" + str(counter) + uri[index : ]
        return res
    else :
        res = uri[ : index ] + "/merge-" + str(counter) + uri[index : ]
        return res


def upload_firmware(driver, uri, file_dir, file_name, progress=Progress()):
    """
    Uploads the file on web server

    Args:
        driver (UcsDriver)
        uri (str): url to upload the file
        file_dir (str): The directory to download to
        file_name (str): The destination file name for the download

    Returns:
        None

    Example:
        driver = UcsDriver()\n
        upload_firmware(driver=UcsDriver(), uri="http://fileurl", file_dir='/home/user/backup', file_name='my_config_backup.xml')
    """
    # Change encoding to ISO-8859-1 for python <=2.x
    def_encoding = sys.getdefaultencoding() # Old encoding type : e.g ascii
    set_default_encoding('ISO-8859-1')

    content_path = os.path.join(file_dir, file_name)
    content_size = os.path.getsize(content_path)

    if not os.path.exists(content_path):
        raise IOError("File does not exist")

    f = open(content_path,'rb')
    chunk_size = 10*1024*1024
    counter = 0
    flag = 0

    for chunk in read_in_chunks(f, chunk_size):
        if len(chunk) > 0:
            try:
                counter += 1
                chunk_uri = generate_uri_for_chunks(uri, counter, flag)
                response = driver.post(chunk_uri, data = chunk)
                progress.update(content_size, len(chunk))
                if not response:
                    raise ValueError("File upload failed.")
            except Exception as e:
                raise Exception(e)
    try:
        counter += 1
        flag = 1
        merge_uri = generate_uri_for_chunks(uri, counter, flag)
        response = driver.post(merge_uri)
        if not response:
            raise ValueError("File upload failed.")
    except Exception as e:
        raise Exception(e)

    # Reset to default encoding
    set_default_encoding(def_encoding)


def check_registry_key(java_key):
    """ Method checks for the java in the registry entries. """

    # Added KEY_WOW64_64KEY, KEY_ALL_ACCESS. This lets 32bit python access
    # registry keys of 64bit Application on Windows supporting 64 bit.

    try:
        from _winreg import ConnectRegistry, HKEY_LOCAL_MACHINE, OpenKey, \
            QueryValueEx, KEY_WOW64_64KEY, KEY_ALL_ACCESS
    except:
        from winreg import ConnectRegistry, HKEY_LOCAL_MACHINE, OpenKey, \
            QueryValueEx, KEY_WOW64_64KEY, KEY_ALL_ACCESS

    path = None
    try:
        a_reg = ConnectRegistry(None, HKEY_LOCAL_MACHINE)
        r_key = OpenKey(a_reg, java_key, 0, KEY_WOW64_64KEY + KEY_ALL_ACCESS)
        for i_cnt in range(1024):
            current_version = QueryValueEx(r_key, "CurrentVersion")
            if current_version is not None:
                key = OpenKey(r_key, current_version[0])
                if key is not None:
                    path = QueryValueEx(key, "JavaHome")
                    return path[0]
    except Exception:
        UcsWarning("Not able to access registry.")
        return None


def is_binary_in_path(path, binary):
    """
    Checks if the given binary is available in the specified path.

    Returns:
        True or False (Boolean)
    """
    import os

    def is_exe(fpath):
        return os.path.isfile(fpath) and os.access(fpath, os.X_OK)

    path = path.strip('"')
    exe_file = os.path.join(path, binary)
    if is_exe(exe_file):
        return True
    return False


def get_binary_path(binary):
    """
    Checks the environment PATH variable for the specified binary file.
    If found, it returns the path in which it was found.

    Example:
        path = get_binary_path('javaws')
    """
    import os

    fpath, fname = os.path.split(binary)
    if fpath:
        raise UcsValidationException("Expects only binary name, not Path.")
    for path in os.environ["PATH"].split(os.pathsep):
        if is_binary_in_path(path, fname):
            return path
    return None


def get_java_installation_path():
    """
    Method returns the java installation path in the windows or
    Linux environment.
    """

    if platform.system() in ["Linux", "Darwin"]:
        path = os.environ.get('JAVA_HOME')
        # is javaws in $JAVA_HOME?
        if path and is_binary_in_path(path, 'javaws'):
            return path + '/' + 'javaws'

        # is javaws available in system path?
        path = get_binary_path('javaws')
        if path:
            return path + '/' + 'javaws'

        # javaws was not found
        raise UcsValidationException(
            "Please make sure JAVA is installed and variable JAVA_HOME"
            "is set properly.")

    # Get JavaPath for Windows
    # elif os.name == "nt":
    elif platform.system() == "Windows" or platform.system() == "Microsoft":

        path = os.environ.get('JAVA_HOME')

        if path is None:
            path = check_registry_key(
                r"SOFTWARE\\JavaSoft\\Java Runtime Environment\\")

        if path is None:  # Check for 32 bit Java on 64 bit machine.
            path = check_registry_key(
                r"SOFTWARE\\Wow6432Node\\JavaSoft\\Java Runtime Environment")

        if not path:
            raise UcsValidationException("Please make sure JAVA is installed.")
        else:
            path = os.path.join(path, 'bin')
            path = os.path.join(path, 'javaws.exe')
            if not os.path.exists(path):
                raise UcsValidationException(
                    "javaws.exe is not installed on System at path <%s>." % (
                        path))
            else:
                return path


def check_output(*popenargs, **kwargs):
    """
    Internal method to handle upload/download data from server.
    """

    if 'stdout' in kwargs:
        raise ValueError('stdout argument not allowed, it will be overridden.')
    process = subprocess.Popen(stdout=subprocess.PIPE, *popenargs, **kwargs)
    output, unused_err = process.communicate()
    ret_code = process.poll()
    if ret_code:
        cmd = kwargs.get("args")
        if cmd is None:
            cmd = popenargs[0]
        raise subprocess.CalledProcessError(ret_code, cmd, output=output)
    return output


def get_java_version():
    """
    Method to get java version.
    """

    try:
        subprocess.check_output
    except Exception:
        subprocess.check_output = check_output

    java_ver_full_str = subprocess.check_output(["java", "-version"],
                                                stderr=subprocess.STDOUT)

    java_ver_full_str = java_ver_full_str.decode()
    java_ver_match = re.match(r'java version.*?"(.*?)"', java_ver_full_str)
    java_ver_str = java_ver_match.groups()[0]
    return java_ver_str


def get_md5_sum(filename):
    """
    Method to get md5sum for the image.

    Args:
        filename (str): file for which md5sum is to be computed
    """

    import hashlib

    md5_obj = hashlib.md5()
    file_handler = open(filename, 'rb')
    for chunk in iter(lambda: file_handler.read(128 * md5_obj.block_size), b''):
        md5_obj.update(chunk)

    file_handler.close()
    return md5_obj.hexdigest()


def get_sha_hash(input_string):
    """
    Method returns the sha hash digest for a given string.

    Args:
        input_string (str): the input string for which sha has to be computed
    """

    import hashlib

    return hashlib.md5(input_string).digest()


def expand_key(key, clen):
    """
    Internal method supporting encryption and decryption functionality.
    """
    import hashlib
    from array import array

    blocks = (clen + 19) / 20
    x_key = []
    seed = key
    for i_cnt in range(blocks):
        seed = hashlib.md5(key + seed).digest()
        x_key.append(seed)
    j_str = ''.join(x_key)
    return array('L', j_str)


def encrypt_password(password, key):
    """
    Encrypts the password using the given key.

    Args:
        password (str): password to be encrypted
        key (str): key to be used to encrypt the password
    """

    from time import time
    from array import array
    import hmac
    import base64

    h_hash = get_sha_hash
    uhash = h_hash(','.join(str(x) for x in
                            [repr(time()), repr(os.getpid()),
                             repr(len(password)),
                             password, key]))[:16]
    k_enc, k_auth = h_hash('enc' + key + uhash), h_hash('auth' + key + uhash)
    pwd_len = len(password)
    password_stream = array('L', password + '0000'[pwd_len & 3:])
    x_key = expand_key(k_enc, pwd_len + 4)

    for i_cnt in range(len(password_stream)):
        password_stream[i_cnt] = password_stream[i_cnt] ^ x_key[i_cnt]

    cipher_t = uhash + password_stream.tostring()[:pwd_len]
    auth = hmac.new(cipher_t, k_auth).digest()
    encrypt_str = cipher_t + auth[:8]
    encoded_str = base64.encodestring(encrypt_str)
    encrypted_password = encoded_str.rstrip('\n')
    return encrypted_password


def decrypt_password(cipher, key):
    """
    Decrypts the password using the given key with which the password
    was encrypted first.
    """

    import base64
    from array import array

    h_hash = get_sha_hash

    cipher += "\n"
    cipher = base64.decodestring(cipher)
    cipher_len = len(cipher) - 16 - 8

    uhash = cipher[:16]
    password_stream = cipher[16:-8] + "0000"[cipher_len & 3:]
    # auth = cipher[-8:]

    k_enc = h_hash('enc' + key + uhash)
    # k_auth = h_hash('auth' + key + uhash)
    # vauth = hmac.new(cipher[-8:], k_auth, sha).digest()[:8]

    password_stream = array('L', password_stream)
    x_key = expand_key(k_enc, cipher_len + 4)

    for i in range(len(password_stream)):
        password_stream[i] = password_stream[i] ^ x_key[i]

    decrypted_password = password_stream.tostring()[:cipher_len]
    return decrypted_password


def iteritems(d):
    """
    Factor-out Py2-to-3 differences in dictionary item iterator methods
    """

    try:
        return six.iteritems(d)
    except AttributeError:
        return d.items()

def add_escape_chars(xml_str):
    return xml_str.replace("\n", "&#xA;")

def remove_invalid_chars(xml_str):
    replace_dict = {
        '<': '&lt;',
        '>': '&gt;',
        '&': '&amp;'
    }
    to_repl = {}
    for value in re.findall('"([^"]*)"', xml_str):
        for key in replace_dict.keys():
            if key in value:
                if value in to_repl:
                    to_repl[value] = to_repl[value].replace(key,
                                                            replace_dict[key])
                else:
                    to_repl[value] = value.replace(key, replace_dict[key])
    for each in to_repl:
        xml_str = xml_str.replace(each, to_repl[each])
    return xml_str


def set_default_encoding(encoding_str):
    if sys.version_info[:2] <= (2, 7):
       # If Python 2.7 or older, then set 'ISO-8859-1' as default encoding
        reload(sys)
        sys.setdefaultencoding(encoding_str)
