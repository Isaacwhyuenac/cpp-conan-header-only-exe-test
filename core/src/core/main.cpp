//
// Created by Isaac Lefrançois on 5/1/24.
//
#include <iostream>
#include "common/algorithm.h"
#include "core/core_algorithm.h"

int main() {

    int a = 2;
    int b = 3;

    int c = add(a, b);
    int d = multiply(a, b);

    std::cout << "a + b = " << c << std::endl;
    std::cout << "a * b = " << d << std::endl;
    return 0;
}