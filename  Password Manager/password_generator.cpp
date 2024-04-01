#include <iostream>
#include <cstdlib>
#include <ctime>

int main() {
    // Seed random number generator
    std::srand(std::time(0));

    // Generate a random password
    const int password_length = 12;
    std::string password;
    for (int i = 0; i < password_length; ++i) {
        password.push_back('A' + std::rand() % 26);
    }

    std::cout << password << std::endl;

    return 0;
}
