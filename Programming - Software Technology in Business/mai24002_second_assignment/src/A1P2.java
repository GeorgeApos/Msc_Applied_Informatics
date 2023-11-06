public class A1P2 {
    public static void main(String[] args) {
        Contact workContact1 = new Contact("Kassandrou 150", "Thessaloniki", 54634, "2310234567");
        Contact residentialContact1 = new Contact("Egnatia 40", "Thessaloniki", 44656, "2310897678");
        Loaner lender1 = new Loaner("Papadopoulos Periklhs", residentialContact1, workContact1, 5000);

        Contact workContact2 = new Contact("Egnatias 156", "Thessaloniki", 54006, "2310000000");
        Loaner lender2 = new Loaner("Stelios Xinogalos", workContact2, workContact2, 4000);

        for (int i = 0; i < 4; i++) {
            lender1.Reminder();
        }

        lender2.payment(4000);
        lender1.payment(2000);

        lender1.Reminder();

        lender1.payment(3000);
    }
}