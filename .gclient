solutions = [
  {
    "name": "src",
    "url": "https://webrtc.googlesource.com/src.git",
    "managed": False,
    "custom_deps": {
        "src/third_party/accessibility_test_framework": None,
        "src/third_party/android_support_test_runner": None,
        "src/third_party/gtest-parallel": None,
        "src/tools/luci-go": None,
        "src/tools/swarming_client": None,
    },
    "custom_hooks": [
        {"name": "Generate component metadata for tests"},
        {"name": "test_fonts"},
        {"name": ""},
    ],
  },
]
