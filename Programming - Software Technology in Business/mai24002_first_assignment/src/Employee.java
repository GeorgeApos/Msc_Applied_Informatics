import java.util.logging.Level;

public class Employee {

    private String name;
    private LevelOfEducation levelOfEducation;
    private MasterExperience masterExperience;
    private int yearsOfExperience;
    private boolean isMarried;

    private int numOfChildren;
    private int salary;
    private int allowance;

    public Employee(String name, String levelOfEducation,
                    String masterExperience, int yearsOfExperience,
                    boolean isMarried, int numOfChildren, int salary) {
        this.name = name;
        this.levelOfEducation = validateLevelOfEducation(levelOfEducation);
        this.masterExperience = validateMasterExperience(masterExperience);
        this.yearsOfExperience = yearsOfExperience;
        this.isMarried = isMarried;
        this.numOfChildren = numOfChildren;
        this.salary = salary;
        this.allowance = 0;
    }

    private MasterExperience validateMasterExperience(String masterExperience) {
        if (masterExperience.equals("TYPE_0") || masterExperience.equals("TYPE_1") || masterExperience.equals("TYPE_2")) {
            return MasterExperience.valueOf(masterExperience);
        } else {
            throw new IllegalArgumentException("Invalid masterExperience value. Please provide 'TYPE_0', 'TYPE_1' or 'TYPE_2'.");
        }
    }

    private LevelOfEducation validateLevelOfEducation(String levelOfEducation) {
        if (levelOfEducation.equals("PE") || levelOfEducation.equals("DE") || levelOfEducation.equals("TE")) {
            return LevelOfEducation.valueOf(levelOfEducation);
        } else {
            throw new IllegalArgumentException("Invalid levelOfEducation value. Please provide 'PE', 'DE' or 'TE'.");
        }
    }

    public void showEmployeeInfo() {
        System.out.println("==================================");
        System.out.println("Name: " + this.name);
        System.out.println("Level of education: " + this.levelOfEducation);

        if(this.masterExperience.equals(MasterExperience.TYPE_0)) {
            System.out.println("Master's degree: No");
        } else if(this.masterExperience.equals(MasterExperience.TYPE_1)) {
            System.out.println("Master's degree: Yes, but no PhD");
        } else if(this.masterExperience.equals(MasterExperience.TYPE_2)) {
            System.out.println("Master's degree: Yes and PhD");
        }

        System.out.println("Years of experience: " + this.yearsOfExperience);
        System.out.println("Married: " + this.isMarried);
        System.out.println("Number of children: " + this.numOfChildren);
        System.out.println("Salary: " + this.salary + " euros");
        System.out.println("Monthly salary: " + giveMonthlySalary() + " euros");
        System.out.println("==================================");
    }

    public int giveMonthlySalary() {
        return this.salary + this.allowance;
    }

    public void changeAllowance(int allowanceYearsOfService, int allowanceChildren) {
        int yearsOfServiceAllowance = allowanceYearsOfService * this.yearsOfExperience;
        int childrenAllowance = allowanceChildren * this.numOfChildren;
        int maritalAllowance = this.isMarried ? 50 : 0;
        int masterExperienceAllowance = 0;

        if(this.masterExperience.equals(MasterExperience.TYPE_1)) {
            masterExperienceAllowance = 50;
        } else if(this.masterExperience.equals(MasterExperience.TYPE_2)) {
            masterExperienceAllowance = 100;
        }

        this.allowance = yearsOfServiceAllowance + childrenAllowance + maritalAllowance + masterExperienceAllowance;
    }

    public void changeNumberOfChildren(int change) {
        int updatedNumberOfChildren = this.numOfChildren + change;

        if (updatedNumberOfChildren >= 0) {
            this.numOfChildren = updatedNumberOfChildren;
        } else {
            System.out.println("Error! Number of children cannot be negative!");
        }
    }

    public void updateYearsOfExperience() {
        this.yearsOfExperience += 1;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public LevelOfEducation getLevelOfEducation() {
        return levelOfEducation;
    }

    public void setLevelOfEducation(LevelOfEducation levelOfEducation) {
        this.levelOfEducation = levelOfEducation;
    }

    public MasterExperience getMasterExperience() {
        return masterExperience;
    }

    public void setMasterExperience(MasterExperience masterExperience) {
        this.masterExperience = masterExperience;
    }

    public int getYearsOfExperience() {
        return yearsOfExperience;
    }

    public void setYearsOfExperience(int yearsOfExperience) {
        this.yearsOfExperience = yearsOfExperience;
    }

    public boolean isMarried() {
        return isMarried;
    }

    public void setMarried(boolean married) {
        isMarried = married;
    }

    public int getNumOfChildren() {
        return numOfChildren;
    }

    public void setNumOfChildren(int numOfChildren) {
        this.numOfChildren = numOfChildren;
    }

    public int getSalary() {
        return salary;
    }

    public void setSalary(int salary) {
        this.salary = salary;
    }

    public int getAllowance() {
        return allowance;
    }

    public void setAllowance(int allowance) {
        this.allowance = allowance;
    }
}
