from conans import ConanFile, CMake, tools


class HobbitsConan(ConanFile):
    name = "hobbits"
    version = "unstable"
    license = "MIT"
    author = "Adam Nash adam@smr.llc"
    url = "https://github.com/Mahlet-Inc/hobbits-packager"
    description = "Packager for hobbits to be used for plugin development"
    topics = ("hobbits", "qt")
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False], "fPIC": [True, False]}
    default_options = {
        "shared": True,
        "fPIC": True,
        "qt:shared": True
        }
    generators = "cmake"
    
    requires = [
        ("qt/5.15.2"),
        ("hobbits-cpython/3.9.1")
    ]

    def config_options(self):
        if self.settings.os == "Windows":
            del self.options.fPIC

    def _configure_cmake(self):
        if self.settings.os == "Windows":
            cmake = CMake(self)
        else:
            cmake = CMake(self, generator="Ninja")
        defs = {
            "BUILDING_WITH_CONAN" : 1,
            "JUST_LIBS" : 1
        }
        if self.settings.build_type == "Release":
            defs["QT_NO_DEBUG"] = 1
        cmake.configure(source_folder="hobbits", defs=defs)
        return cmake

    def source(self):
        self.run("git clone https://github.com/Mahlet-Inc/hobbits.git")
        self.run("git checkout develop", cwd="hobbits")

    def build(self):
        cmake = self._configure_cmake()
        cmake.build()

    def package(self):
        cmake = self._configure_cmake()
        cmake.install()

        self.copy("*.h", dst="include", src="include/hobbits")
        self.copy("*.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.dylib", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["hobbits-core", "hobbits-widgets", "hobbits-python"]

