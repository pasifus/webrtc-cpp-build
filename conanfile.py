from conans import ConanFile
import os

class Webrtc(ConanFile):
    name = "webrtc"
    license = "BSD"
    description = "Chromium webrtc"
    url = "https://webrtc.googlesource.com/"
    settings = "os", "compiler", "build_type", "arch"
    options = { "build_path": "ANY" }
    default_options = { "build_path": None }

    # https://docs.conan.io/en/latest/reference/conanfile/methods.html#requirements
    def requirements(self):
        if(self.settings.os == "Linux"):
            self.requires("glib/2.69.1")

    # https://docs.conan.io/en/latest/reference/conanfile/methods.html#package-id
    def package_id(self):
        del self.info.options.build_path

    # https://docs.conan.io/en/latest/reference/conanfile/methods.html#package-id
    def package_id(self):
        # delete listeng to compiler.version
        del self.info.settings.compiler.version
        # delete listeng to options.build_path
        del self.info.options.build_path
        
    # https://docs.conan.io/en/latest/reference/conanfile/methods.html#package
    def package(self):
        incude_path = os.path.join(str(self.options.build_path), "include")
        lib_path = os.path.join(str(self.options.build_path), "lib")
        self.output.info("incude_path: %s" % incude_path)
        self.output.info("lib_path: %s" % lib_path)
        self.copy("*", dst="include", src=incude_path, keep_path=True)
        self.copy("*", dst="lib", src=lib_path, keep_path=True)

    # https://docs.conan.io/en/latest/reference/conanfile/methods.html#package-info
    def package_info(self):
        self.cpp_info.includedirs.append('include/third_party/abseil-cpp')
        self.cpp_info.includedirs.append('include/third_party/libyuv/include')
        if(self.settings.os == "Windows"):
            self.cpp_info.defines.append('WEBRTC_WIN')
            self.cpp_info.defines.append('WIN32_LEAN_AND_MEAN')
            self.cpp_info.libs = ["libwebrtc"]
            self.cpp_info.system_libs.extend(["secur32", "winmm", "dmoguids", "wmcodecdspuuid", "msdmo", "Strmiids"])
        else:
            self.cpp_info.libs = ["webrtc"]
            self.cpp_info.defines.append('WEBRTC_POSIX')
            if(self.settings.os == "Macos"):
                self.cpp_info.defines.append('WEBRTC_MAC') 
                self.cpp_info.frameworks.extend(["Cocoa", "Foundation", "IOKit", "Security", "SystemConfiguration"])
            elif(self.settings.os == "Linux"):
                self.cpp_info.defines.append('WEBRTC_LINUX')
                self.cpp_info.system_libs.extend(["glib-2.0", "pthread"])
            elif(self.settings.os == "iOS"):
                self.cpp_info.defines.append('WEBRTC_MAC')
                self.cpp_info.defines.append('WEBRTC_IOS')
                self.cpp_info.frameworks.extend(["AVFoundation", "CFNetwork", "Foundation", "Security", "SystemConfiguration", "UIKit"])
            elif(self.settings.os == "Android"):
                self.cpp_info.defines.append('WEBRTC_LINUX')
                self.cpp_info.defines.append('WEBRTC_ANDROID')
                # self.cpp_info.defines.append('WEBRTC_ANDROID_OPENSLES')
            else:
                raise Exception("not valid os: ", self.settings.os)