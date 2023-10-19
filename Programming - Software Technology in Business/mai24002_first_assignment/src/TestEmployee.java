import java.security.spec.ECPoint;

public class TestEmployee {

    public static void main(String[] args) {
        Employee employee1 = new Employee("Eleni Papadopoulou", "PE", "TYPE_2", 25, true, 2, 1800);
        Employee employee2 = new Employee("Nikos Papadopoulos", "PE", "TYPE_1", 4, true, 2, 1200);

        employee1.showEmployeeInfo();
        employee2.showEmployeeInfo();

        System.out.println("***Changing Eleni's number of children");
        employee1.changeNumberOfChildren(-3);

        System.out.println("***Changing Eleni's number of children");
        employee1.changeNumberOfChildren(-2);

        System.out.println("***Changing Eleni's monthly salary");
        employee1.changeAllowance(10, 30);

        employee1.showEmployeeInfo();

        System.out.println("***Changing Niko's monthly salary");
        employee2.changeAllowance(10, 30);

        employee2.showEmployeeInfo();

        //Extra => Check level of education and master's degree values

        // Illegal Argument Exception for level of education
//        Employee employee3 = new Employee("Maria Papadopoulou", "PROTOVATHMIA", "TYPE_2", 25, true, 2, 1800);

        //Illegal Argument Exception for master's degree
//        Employee employee4 = new Employee("Vasiliki Papadopoulou", "PE", "TYPE_5", 25, true, 2, 1800);
    }
}
