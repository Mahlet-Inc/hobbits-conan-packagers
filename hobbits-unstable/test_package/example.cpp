#include "hobbits/hobbitscoreconfig.h"
#include "hobbits/hobbitspythonconfig.h"
#include <iostream>

int main() {
    std::cout << "Hobbits Core Version: " << HobbitsCoreConfig::VERSION << "\n";
    std::cout << "Hobbits Python Version: " << HobbitsPythonConfig::PYTHON_VERSION << "\n";
}
