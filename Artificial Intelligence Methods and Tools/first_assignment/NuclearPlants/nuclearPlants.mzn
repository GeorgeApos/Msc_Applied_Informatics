% Include the globals file
include "globals.mzn";

% Declare the number of plants
int: no_plants;

% Define the set of plants
set of int: PLANTS = 1..no_plants;

% Define the time frame
set of int: TIME = 0..100;

% Declare arrays for plant supply and needs
array[PLANTS] of int: supply;
array[PLANTS] of int: needs;

% Define variables for plant supply and end time
array[PLANTS] of var int: plant_supply = [supply[i] | i in PLANTS];
array[PLANTS] of var TIME: end_time = [end[i] | i in PLANTS];

% Declare the number of problems and define the not_sim array
int: problems;
array[1..problems, 1..2] of PLANTS: not_sim; 

% Declare variables for start and end times
array[PLANTS] of var TIME: start; 
array[PLANTS] of var TIME: end; 

% Declare a variable for the end of supply time
var TIME: end_of_supply; 

% Define variables for the rounded-up needs/supply ratio
array[PLANTS] of var TIME: ceil_needs_supply = [ceil(needs[i] / supply[i]) | i in PLANTS];

% Constraint to ensure end time is calculated correctly
constraint forall(i in PLANTS)(
    end[i] = start[i] + ceil(needs[i] / supply[i])
);

% Constraint to ensure cumulative water supply does not exceed total_water_supply
constraint cumulative(start, ceil_needs_supply, plant_supply, 120);

% Constraint to enforce restrictions on simultaneous supply for certain plants
constraint forall(i in 1..problems)(
    (start[not_sim[i, 1]] + ceil_needs_supply[not_sim[i, 1]] <= start[not_sim[i, 2]]) \/
    (start[not_sim[i, 2]] + ceil_needs_supply[not_sim[i, 2]] <= start[not_sim[i, 1]])
);

% Constraint to ensure end_of_supply reflects the maximum end time of all plants
constraint end_of_supply = max(end_time);


% Output the start times and end_of_supply time
output ["start = \(start);\nend_of_supply = \(end_of_supply);"];
