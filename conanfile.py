from conans import ConanFile, CMake


class httplibConan(ConanFile):
    name = "httplib"
    version = "0.2.6"
    description = "C++11 header-only HTTP/HTTPS sever library https://github.com/yhirose/cpp-httplib"
    license = "MIT"
    url = "https://github.com/omaralvarez/conan-httplib"
    repo_url = "https://github.com/yhirose/cpp-httplib"
    topics = ("cpp", "http", "header-only")
    generators = "cmake"
    exports_sources = "*.h"
    no_copy_source = True
    options = { "openssl": [True, False] }
    default_options = { "openssl": True }

    def source(self):
        self.run("git clone -b 'v%s' --single-branch --depth 1 %s" % (self.version, self.repo_url))
    
    def requirements(self):
        if self.options.openssl:
            self.requires.add("OpenSSL/1.1.1c@conan/stable")

    def _configure_cmake(self):
        cmake = CMake(self)
        cmake.configure(source_folder="cpp-httplib")
        return cmake

    def build(self):
        cmake = self._configure_cmake()
        cmake.build()

    def package(self):
        cmake = self._configure_cmake()
        cmake.install()
    
    def package_id(self):
        self.info.header_only()
