[app]

# (str) Title of your application
title = 一年级数学练习

# (str) Package name
package.name = mathpractice

# (str) Package domain (needed for android/ios packaging)
package.domain = org.mathpractice

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (list) List of inclusions using pattern matching
#source.include_patterns = assets/*,images/*.png

# (list) Source files to exclude (let empty to not exclude anything)
#source.exclude_exts = spec

# (str) Application versioning (method 1)
version = 1.0

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
requirements = python3,kivy

# (str) Presplash of the application
#presplash.filename = %(source.dir)s/data/presplash.png

# (str) Icon of the application
#icon.filename = %(source.dir)s/data/icon.png

# (str) Supported orientation (one of landscape, sensorLandscape, portrait or all)
orientation = portrait

# (list) List of service to declare
#services = NAME:ENTRYPOINT_TO_PY,python2:NAME:ENTRYPOINT_TO_PY

#
# Android specific
#

# (list) Permissions
android.permissions = INTERNET

# (int) Target Android API, should be as high as possible.
#android.api = 27

# (int) Minimum API your APK will support.
#android.minapi = 21

# (int) Android NDK version to use
#android.ndk = 19b

# (int) Android SDK version to use
#android.sdk = 27

# (str) Android NDK directory (if empty, it will be automatically downloaded.)
#android.ndk_path =

# (str) Android SDK directory (if empty, it will be automatically downloaded.)
#android.sdk_path =

# (str) ANT directory (if empty, it will be automatically downloaded.)
#android.ant_path =

# (bool) If True, then skip trying to update the Android sdk
# This can be useful to avoid excess Internet downloads or save time
# when an update is due and you just want to test/build your package
# android.skip_update = False

# (bool) Whether to patch your source for Android compatibility
# android.patch_src = False

#
# Python for android specifics
#

# (str) python-for-android fork to use, can override 'p4a_branch' in local.properties
#p4a.fork = python-for-android

# (str) python-for-android branch to use, check if p4a.fork is set to a custom fork
#p4a.branch = master

# (str) python-for-android specific commit to use, check if p4a.fork is set to a custom fork
#p4a.commit = HEAD

# (str) python-for-android git clone directory (if empty, it will be automatically cloned from github)
#p4a.source_dir =

# (str) The directory in which python-for-android should look for your own build recipes (if any)
#p4a.recipes_dir =

# (str) Filename to the hook for p4a
#p4a.hook =

# (str) Bootstrap to use for android builds
# p4a.bootstrap = sdl2

# (int) Number of parallel build jobs
#p4a.num_jobs =

# (int) Android logcat filters to use
#android.logcat_filters = *:S python:D

# (bool) Copy library instead of making a libpymodules.so
#android.copy_libs = 1

#
# iOS specific
#

# (str) Path to a custom kivy-ios folder
#ios.kivy_ios_dir = ../kivy-ios
# Alternately, specify the python-for-ios tool to use
#ios.toolchain = python-for-ios

#
# macOS specific
#

# (str) Path to a custom kivy-macos folder
#macos.kivy_macos_dir = ../kivy-macos

#
# Windows specific
#

# (str) Path to custom kivy-mdos folder
#windows.kivy_mdos_dir = ../kivy-mdos

#
# General extras
#

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (str) Presplash filename
#presplash.filename = presplash.png

# (str) Icon filename
#icon.filename = icon.png