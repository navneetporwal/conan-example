from conans import ConanFile, CMake, tools


class ConanBoostConan(ConanFile):
    name = "ConanBoost"
    version = "10.1"
    license = "<Put the package license here>"
    author = "<Put your name here> <And your email here>"
    url = "<Package recipe repository url here, for issues about the package>"
    description = "<Description of Hello here>"
    topics = ("<Put some tag here>", "<here>", "<and here>")
    settings = "os", "compiler", "build_type", "arch"
    requires = "boost_date_time/1.69.0@bincrafters/stable"
    #options = {"shared": [True, False]}
    #default_options = {"shared": False}
    generators = "cmake"
    #exports_sources = "conan-boost/*"

    def source(self):
        self.run("git clone https://github.com/nrundle/conan-boost.git")
        tools.replace_in_file("conan-boost/CMakeLists.txt", "cmake_minimum_required (VERSION 3.13.4)", '''cmake_minimum_required (VERSION 3.9.1) ''')

    def build(self):
        cmake = CMake(self)
        cmake.configure(source_folder="conan-boost")
        cmake.build()

        # Explicit way:
        #self.run('cmake %sconan-boost %s'% (self.source_folder, cmake.command_line))
        #self.run('cmake -B .')
        #self.run('cmake --build .')
        # self.run("cmake --build . %s" % cmake.build_config)

    def package(self):
        #self.copy("*.h", dst="include", src="hello")
        #self.copy("*hello.lib", dst="lib", keep_path=False)
        #self.copy("*.dll", dst="bin", keep_path=False)
        #self.copy("*.so", dst="lib", keep_path=False)
        #self.copy("*.dylib", dst="lib", keep_path=False)
        self.copy("conan_boost", dst="bin", src="bin", keep_path=False)

    def package_info(self):
        #self.cpp_info.libs = ["conan-boost"]
        self.cpp_info.bindirs = ['bin']
        self.cpp_info.requires = "boost_date_time/1.69.0@bincrafters/stable"

