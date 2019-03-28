# Android-Tools
A few small Android-related scripts

## getprop.py
Works similar to `getprop` on Android 9 systems.

## rmprop.py
Allows to delete selected keys from the `/data/property/persistent_properties` (Android 9) file. Mostly useful after accidentally setting persistent keys using `setprop` and then not being able to remove them anymore.

## Requirements
- Python 3
- protobuf
