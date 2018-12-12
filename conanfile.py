from conans import ConanFile, CMake


class croncppConan(ConanFile):
    name = "httplib"
    version = "master"
    description = "C++11 header-only HTTP/HTTPS sever library https://github.com/keko950/cpp-httplib"
    license = "MIT"
    url = "https://github.com/omaralvarez/conan-httplib"
    repo_url = "https://github.com/keko950/cpp-httplib"
    author = "Yuji Hirose, Omar Alvarez"
    exports_sources = "include/*"
    no_copy_source = True

    def source(self):
        self.run_command("git clone %s" % (self.repo_url))
    
    def run_command(self, cmd, cwd=None):
        self.output.info(cmd)
        self.run(cmd, True, cwd)

    def build(self):
        cmake = CMake(self)
        cmake.configure(source_folder="cpp-httplib")
        cmake.install()

    def package(self):
        pass

    def package_id(self):
        self.info.header_only()