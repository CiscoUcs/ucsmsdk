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

import warnings


def deprecated(replaced_by_func):
    """
    This decorator is used to mark functions as deprecated. It also points
    the user to the newer function that should be used instead.
    """
    def wrap(f):
        def new_func(*args, **kwargs):
            warnings.simplefilter('always', DeprecationWarning)
            warnings.warn(
                "Call to deprecated function " + f.__name__ +
                ". This method is replaced by " + replaced_by_func.__name__,
                category=DeprecationWarning, stacklevel=2)
            warnings.simplefilter('default', DeprecationWarning)
            return f(*args, **kwargs)
        new_func.__dict__.update(f.__dict__)
        new_func.__doc__ = f.__doc__
        new_func.__name__ = f.__name__
        return new_func
    return wrap
