import java.util.ArrayList;

public class School {

    private String name;
    private String principal;

    private ArrayList<Teacher> teachers = new ArrayList<>();

    public School(String name, String manager_name) {
        this.name = name;
        this.principal = manager_name;
    }

    public String getName() {
        return this.name;
    }

    public String getManagerName() {
        return this.principal;
    }

    public void setName(String name) {
        this.name = name;
    }

    public void setManagerName(String manager_name) {
        this.principal = manager_name;
    }

    public String toString() {
        return "School: " + this.name + "\nManager: " + this.principal;
    }

    public void addTeacher(Teacher teacher) {
        this.teachers.add(teacher);
    }

    public ArrayList<Teacher> getTeachers() {
        return teachers;
    }

    public void setTeachers(ArrayList<Teacher> teachers) {
        this.teachers = teachers;
    }

}
