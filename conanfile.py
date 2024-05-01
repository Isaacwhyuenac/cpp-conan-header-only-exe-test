from conan import ConanFile
from conan.tools.cmake import CMakeToolchain, CMake, cmake_layout, CMakeDeps


class my_algorithmRecipe(ConanFile):
    name = "my_algorithm"
    version = "0.0.1"
    package_type = "library"

    # Optional metadata
    license = "<Put the package license here>"
    author = "<Put your name here> <And your email here>"
    url = "<Package recipe repository url here, for issues about the package>"
    description = "<Description of my_algorithm package here>"
    topics = ("<Put some tag here>", "<here>", "<and here>")

    # Binary configuration
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False], "fPIC": [True, False]}
    default_options = {"shared": False, "fPIC": True}

    # Sources are located in the same place as this recipe, copy them to the recipe
    # exports_sources = "CMakeLists.txt", "src/*", "include/*"
    exports_sources = "CMakelists.txt", "common/*", "core/*"

    def requirements(self):
        self.requires("spdlog/1.14.0")
        self.requires("fmt/10.2.1")

    def config_options(self):
        if self.settings.os == "Windows":
            self.options.rm_safe("fPIC")

    def configure(self):
        if self.options.shared:
            self.options.rm_safe("fPIC")

    def layout(self):
        cmake_layout(self)

    def generate(self):
        deps = CMakeDeps(self)
        deps.generate()
        tc = CMakeToolchain(self)
        tc.generate()

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        cmake = CMake(self)
        cmake.install()

    def package_info(self):
        # self.cpp_info.libs = ["my_algorithm"]
        self.cpp_info.components["common"].libs = ["common"]
        self.cpp_info.components["common"].set_property("cmake_target_aliases", ["test_foundation::common"])
        self.cpp_info.components["common"].set_property("cmake_target_name", "common")
        self.cpp_info.components["common"].bindirs = []
        self.cpp_info.components["common"].libdirs = []

        self.cpp_info.components["core"].libs = ["core"]
        self.cpp_info.components["core"].requires = ["common"]
        self.cpp_info.components["core"].set_property("cmake_target_aliases", ["test_foundation::core"])
        self.cpp_info.components["core"].set_property("cmake_target_name", "core")