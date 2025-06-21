[app]
title = MP3TestApp
package.name = mp3test
package.domain = org.example
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,mp3,wav
version = 0.1
requirements = python3,kivy
orientation = portrait
fullscreen = 1
android.permissions = WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE,INTERNET
android.api = 33
android.minapi = 21
android.ndk = 25b
android.ndk_api = 21
android.archs = arm64-v8a,armeabi-v7a
# Optional: Reduce size
# android.use_custom_cflags = True
# android.cflags = -Os

# (str) Android entry point, default is ok
entrypoint = main.py

[buildozer]
log_level = 2
warn_on_root = 1