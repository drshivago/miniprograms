//
//  main.cpp
//  perceptron
//
//  Created by zero on 1/5/18.
//  Copyright © 2018 zero. All rights reserved.
//

#include <iostream>

bool perceptron(int[]);

int main(int argc, const char * argv[]) {
    int ber[] = {6, 9};
    std::cout << perceptron(ber);
    
    return 0;
}
bool perceptron(int nums[2]){
    float sum(0.0);
    float bias[] = {5.4, 6.8};
    sum = (nums[0]*bias[0]) + (nums[1]*bias[1]);
    std::cout << sum << std::endl;
    if(sum >= 0){
        return true;
    }else{
        return false;
    }
}
