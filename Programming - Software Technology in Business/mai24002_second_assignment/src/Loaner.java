public class Loaner {
    private String name;
    private Contact homeAddress;
    private Contact workAddress;
    private int amountDue;
    private int reminder;

    public Loaner(String aName, String haddress, String htown, int hzipCode, String hphoneNumber,
                  String waddress, String wtown, int wzipCode, String wphoneNumber, int amount) {
        this.name = aName;
        this.homeAddress = new Contact(haddress, htown, hzipCode, hphoneNumber);
        this.workAddress = new Contact(waddress, wtown, wzipCode, wphoneNumber);
        this.amountDue = amount;
        this.reminder = 0;
    }

    public Loaner(String theName, Contact thehomeAddress, Contact theWorkAddress, int theAmountDue) {
        this.name = theName;
        this.homeAddress = thehomeAddress;
        this.workAddress = theWorkAddress;
        this.amountDue = theAmountDue;
        this.reminder = 0;
    }

    public void reduceAmount(int amount) {
        this.amountDue -= amount;
    }

    public void incrementReminder() {
        if (amountDue > 0) {
            reminder++;
            if (reminder > 4) {
                reminder = 0;
            }
        }
    }

    public void receipt(int amountPaid) {
        System.out.println("\n********** Receipt ******************");
        System.out.println("To: " + name + " paid " + amountPaid);
        System.out.println("Residential Address: " + homeAddress.getFullAddress());
        System.out.println("The rest is " + amountDue + " Euro");
        System.out.println("*************************************\n");
    }

    public void payment(int amount) {
        reduceAmount(amount);
        receipt(amount);
    }

    public void message(Contact address) {
        System.out.println("\n********** Remind " + (reminder + 1) + " **********");
        System.out.println(name);
        System.out.println("Full Address: " + address.getFullAddress());
        System.out.println("Please pay " + amountDue + " Euro by the end of the month");
        System.out.println("*************************************\n");
        incrementReminder();
    }

    public void RecordedMessage(Contact address) {
        System.out.println("\n********** Recorded message **********");
        System.out.println("********** Remind " + (reminder + 1) + " **********");
        System.out.println("I am calling " + address.getPhoneNumber());
        System.out.println(name);
        System.out.println("Please pay " + amountDue + " Euro by the end of the month");
        System.out.println("*************************************\n");
        incrementReminder();
    }

    public void Reminder() {
        if (reminder == 0) {
            message(workAddress);
        } else if (reminder == 1) {
            message(homeAddress);
        } else if (reminder == 2) {
            RecordedMessage(workAddress);
        } else if (reminder == 3) {
            RecordedMessage(homeAddress);
        } else {
            RecordedMessage(homeAddress);
            System.out.println("\n********** Last warning!!!! **********");
            System.out.println("The remaining amount of your loan will be subtracted from your salary.");
            System.out.println("*************************************\n");
        }
    }
}
