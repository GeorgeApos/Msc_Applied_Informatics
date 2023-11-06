public class Contact {
    private String address;
    private String town;
    private int zipCode;
    private String phoneNumber;

    public Contact(String address, String town, int zipCode, String phoneNumber) {
        this.address = address;
        this.town = town;
        this.zipCode = zipCode;
        this.phoneNumber = phoneNumber;
    }

    public String getPhoneNumber() {
        return phoneNumber;
    }

    public void setPhoneNumber(String phoneNumber) {
        this.phoneNumber = phoneNumber;
    }

    public void setAddress(String address) {
        this.address = address;
    }

    public void setTown(String town) {
        this.town = town;
    }

    public void setZipCode(int zipCode) {
        this.zipCode = zipCode;
    }

    public void setFullAddress(String address, String town, int zipCode) {
        this.address = address;
        this.town = town;
        this.zipCode = zipCode;
    }

    public String getFullAddress() {
        if (address != null && town != null && zipCode != 0) {
            return address + ", " + town + ", " + zipCode;
        } else {
            StringBuilder result = new StringBuilder();
            if (address == null) {
                result.append("Missing address.\n");
            }
            if (town == null) {
                result.append("Missing town.\n");
            }
            if (zipCode == 0) {
                result.append("Missing zip code.\n");
            }
            return result.toString();
        }
    }
}
