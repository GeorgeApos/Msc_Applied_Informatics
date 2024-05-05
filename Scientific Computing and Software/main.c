//
// Created by geoapos on 5/5/2024.
//

#include <stdio.h>
#include "first_assignment.h"
#include "second_assignment.h"

int main(){
    printf("Select the assignment you want to run:\n");
    printf("1. First Assignment\n");
    printf("2. Second Assignment\n");
    int choice;
    scanf("%d", &choice);

    while(choice != 1 && choice != 2){
        printf("Invalid choice. Please select 1 or 2\n");
        scanf("%d", &choice);
    }

    if(choice == 1){
        main1();
    } else {
        main2();
    }

    return 0;
}