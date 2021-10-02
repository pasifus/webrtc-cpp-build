from conans import ConanFile, CMake, tools
import os

class TestPackageConan(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake", "cmake_find_package"

    # https://docs.conan.io/en/latest/reference/conanfile/methods.html#build
    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    # https://docs.conan.io/en/latest/reference/conanfile/methods.html#test
    def test(self):
        if not tools.cross_building(self.settings):
            bin_path = os.path.join(os.getcwd(), "bin", "test_package")
            self.output.info("bin_path: %s" % bin_path)
            self.run(bin_path, run_environment=True)