from conans import ConanFile, CMake, tools
import os

class httplibTestConan(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    requires = "httplib/0.5.6@omaralvarez/stable"
    generators = "cmake"

    def build(self):
        cmake = CMake(self)
        if self.options['httplib'].openssl:
            cmake.definitions["WITH_OPENSSL"] = True
        # Current dir is "test_package/build/<build_id>" and CMakeLists.txt is in "test_package"
        cmake.configure()
        cmake.build()

    def test(self):
        os.chdir("bin")
        self.run(".%sexample" % os.sep)