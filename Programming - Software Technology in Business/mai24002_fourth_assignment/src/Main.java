import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Branch branch = new Branch("Thessaloniki, Tsimiski Branch");

        PartTimeEmployee pte1 = new PartTimeEmployee("Nikolaou", "067832710", 4);
        FullTimeEmployee pte2 = new FullTimeEmployee("Papadopoulos", "067832711", 1300);

        branch.addEmployee(pte1);
        branch.addEmployee(pte2);

        branch.setEmployeeHours();
        branch.printPayroll("DECEMBER");

    }
}
