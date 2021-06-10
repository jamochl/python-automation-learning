#include <iostream>
#include <fstream>
#include <string>

int main() {
    std::ifstream secrets_file("secret_pass.txt");
    std::string secret_password;
    secrets_file >> secret_password;

    std::cout << "Secret password is: " << secret_password << "\n";

    std::cout << "Please enter Password" << "\n";

    std::string input_password;
    std::cin >> input_password;

    if (input_password == secret_password) {
        std::cout << "Correct!" << "\n";
    } else {
        std::cout << "Access Denied!" << "\n";
    }
    return 0;
}
