from distutils.version import LooseVersion, StrictVersion

print LooseVersion("2.3.1") < LooseVersion("10.1.2")
print StrictVersion("2.3.1") < StrictVersion("10.1.2")

"""
True
True
"""
