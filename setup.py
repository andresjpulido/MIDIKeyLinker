from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='midikeylink',
    version='0.0.1',
    description='With MIDI KeyLink, you can easily assign MIDI messages from your MIDI controller or device to specific keyboard shortcuts or mouse commands within your favourite software applications.',
    long_description=readme,
    author='Andres Pulido',
    author_email='andresjpulido@gmail.com',
    url='https://github.com/andresjpulido/MIDIKeyLinker',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)