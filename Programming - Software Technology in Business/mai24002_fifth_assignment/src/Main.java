import java.util.ArrayList;

public class Main {

    public static void main(String[] args) {


        School school1 = new School("1st Highschool Polygyros", "Papadopoulos");
        School school2 = new School("17th Highschool Thessaloniki", "Nikolaou");
        School school3 = new School("3rd Highschool Patras", "Iosifidou");

        ArrayList<School> schools = new ArrayList<School>();
        schools.add(school1);
        schools.add(school2);
        schools.add(school3);

        Teacher teacher1 = new FullTimeTeacher("Smith", "100001", 1500, 0.15, 5);
        Teacher teacher2 = new FullTimeTeacher("Johnson", "100002", 1700, 0.18, 6);
        Teacher teacher3 = new FullTimeTeacher("Williams", "100003", 1600, 0.17, 4);
        Teacher teacher4 = new FullTimeTeacher("Jones", "100004", 1800, 0.2, 5);

        Teacher teacher5 = new AssociateTeacher("Brown", "100005", 10,  170);
        Teacher teacher6 = new AssociateTeacher("Davis", "100006", 12,  150);
        Teacher teacher7 = new AssociateTeacher("Miller", "100007", 11,  120);
        Teacher teacher8 = new AssociateTeacher("Wilson", "100008", 13,  130);

        school1.addTeacher(teacher1);
        school1.addTeacher(teacher5);
        school1.addTeacher(teacher6);
        school2.addTeacher(teacher8);
        school2.addTeacher(teacher2);
        school2.addTeacher(teacher3);
        school3.addTeacher(teacher4);
        school3.addTeacher(teacher7);

        InputForm form = new InputForm(schools);

    }

}
