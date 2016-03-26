//
//  main.c
//  euler_problem_14
//
//  Created by Digvijay Makwana on 2014-12-07.
//  Copyright (c) 2014 Digvijay Makwana. All rights reserved.
//

// NOTES: Ran it with int's but there were overflow issues. long solved them

#include <stdio.h>
#define mill 1000001

long nextNumber(long number){
    long newNum = -1;
    if (number == 1){
        return newNum;
    }
    else if (number % 2 == 0){
        newNum = number/2;
    }
    else {
        newNum = 3*number + 1;
    }
    if (newNum < 1){
        return -1;
    }
    else{
        return newNum;
    }
    
}

long lengthOfChain(long* list, long number){
    if (number == -1){
        return 0;
    }
    if (number == 1){
        return 1;
    }
    if (number > mill - 1){
        return 1 + lengthOfChain(list, nextNumber(number));
    }
    if (list[number] != 0){
        return list[number];
    }
    list[number] = 1 + lengthOfChain(list, nextNumber(number));
    return list[number];
}


int main(int argc, const char * argv[]){
    printf("STARTED\n");
    long nextNumberArray[mill] = {0};
    nextNumberArray[1] = 1;
    long number = mill-1;
    long maxChainLength = 0, chainLength = 0;
    while (number > 0){
        chainLength = lengthOfChain(nextNumberArray, number);
        if (chainLength > maxChainLength){
            maxChainLength = chainLength;
            printf("Number: %lu, Length: %lu\n", number, maxChainLength);
        }
        number--;
    }
    return 0;
}