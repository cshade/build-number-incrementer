import pytest
import plistlib
import tempfile
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from increment_build_number import increment_build_number

@pytest.fixture
def sample_plist():
    data = {'CFBundleVersion': '42'}
    with tempfile.NamedTemporaryFile(delete=False) as tf:
        plistlib.dump(data, tf)
        tf_name = tf.name
    yield tf_name
    os.remove(tf_name)

@pytest.fixture
def sample_gradle():
    content = 'versionName "1.2.3"\nversionCode 42\n'
    with tempfile.NamedTemporaryFile(delete=False, mode='w+') as tf:
        tf.write(content)
        tf_name = tf.name
    yield tf_name
    os.remove(tf_name)

def test_increment_build_number(sample_plist, sample_gradle):
    increment_build_number(sample_plist, sample_gradle)

    # Check plist increment
    with open(sample_plist, 'rb') as f:
        data = plistlib.load(f)
    assert data['CFBundleVersion'] == '43'

    # Check gradle increment
    with open(sample_gradle, 'r') as f:
        content = f.read()
    assert 'versionCode 43' in content
