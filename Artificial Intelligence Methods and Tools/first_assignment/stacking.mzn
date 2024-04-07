include "globals.mzn";

% Define parameters
int: num_blocks = 10;
set of int: BLOCKS = 1..num_blocks;
int: stack_blocks = 3;
set of int: STACK = 1..stack_blocks;

% Heights and widths of the blocks
array[BLOCKS] of int: height = [2,1,3,1,4,2,5,5,4,2];
array[BLOCKS] of int: width =  [3,2,3,2,2,1,3,2,3,3];

% Decision variables: which block goes into which stack
array[STACK] of var BLOCKS: stack1;
array[STACK] of var BLOCKS: stack2;

% Constraints

% Ensure each block is used only once in either stack
constraint all_different(stack1 ++ stack2);

% Ensure the total height of both stacks is the same
constraint sum(i in STACK)(height[stack1[i]]) = sum(i in STACK)(height[stack2[i]]);

% Ensure each block in stack1 has equal or greater width than the one below it
constraint forall(i in 1..(stack_blocks-1))(
    width[stack1[i]] >= width[stack1[i+1]]
);

% Ensure each block in stack2 has equal or greater width than the one below it
constraint forall(i in 1..(stack_blocks-1))(
    width[stack2[i]] >= width[stack2[i+1]]
);

% Solve the problem
solve minimize sum(i in STACK)(height[stack1[i]]) + sum(j in STACK)(height[stack2[j]]);

% Output the solution
output ["stack1 = \(stack1);\nstack2 = \(stack2);\n"];

