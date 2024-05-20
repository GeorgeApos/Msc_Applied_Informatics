//
// Created by geoapos on 5/5/2024.
//

#include <stdio.h>
#include "first_assignment.h"
#include "second_assignment.h"
#include "parallel_second_assignment.h"

int main(){
    int choice = 0;
    do {
        printf("Select the assignment you want to run:\n");
        printf("1. First Assignment\n");
        printf("2. Second Assignment\n");
        printf("3. Parallel Second Assignment\n");
        printf("0. Exit\n");
        scanf("%d", &choice);

        do {
            if(choice < 0 || choice > 3){
                printf("Invalid choice. Please select a valid assignment.\n");
                scanf("%d", &choice);
            }
        } while(choice < 0 || choice > 3);

        if(choice == 1){
            main1();
        } else if (choice == 2){
            main2();
        } else if (choice == 3){
            //printf("Not implemented yet.\n");
            main3();
        } else {
            printf("Exiting...\n");
        }
    }while(choice != 0);

    return 0;
}