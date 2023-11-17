import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        FilmProgram filmProgram = new FilmProgram();
        Scanner scanner = new Scanner(System.in);
        boolean continueInput = true;

        // Question b: Reading data for all the films
        System.out.println("***** QUESTION b: read data for all the films *****");
        while (continueInput) {
            System.out.print("Give title? ");
            String title = scanner.nextLine();

            System.out.print("Give director? ");
            String director = scanner.nextLine();

            System.out.print("Give playing time? ");
            int playingTime = scanner.nextInt();
            scanner.nextLine(); // Consume newline left-over

            System.out.print("The film is candidate for Oscar? (true/false) ");
            boolean candidacy = scanner.nextBoolean();
            scanner.nextLine(); // Consume newline left-over

            System.out.print("Give show date? ");
            String showDate = scanner.nextLine();

            Film film = new Film(title, director, playingTime, showDate);
            film.setCandidacy(candidacy);
            filmProgram.storeFilm(film);

            System.out.print("Continue? (y/n) ");
            String input = scanner.nextLine();
            continueInput = input.equalsIgnoreCase("y");
        }

        // Question c: Showing the list of all the films
        System.out.println("***** QUESTION c: show the list of all the films *****");
        filmProgram.showFilms(filmProgram.getList());

        // Question d: Showing the list of films that are candidates for OSCAR
        System.out.println("***** QUESTION d: show the list of films that are candidate for OSCAR *****");
        filmProgram.showFilms(filmProgram.candidateFilms());

        // Question e: Showing the list of films shown on a specific month
        System.out.println("***** QUESTION e: show the list of films shown on November *****");
        System.out.print("Give the month to see the program of films? ");
        int month = scanner.nextInt();
        scanner.nextLine(); // Consume newline left-over
        filmProgram.showFilms(filmProgram.monthFilms(month));

        // Question f: Calculating and displaying the mean time of all films
        System.out.println("***** QUESTION f: mean time of all films *****");
        System.out.println("The mean playing time of all the films in the collection is " + filmProgram.filmsMeanTime());

    // Question g: Searching for films
        System.out.println("***** QUESTION g: search for films *****");
        Scanner scanner1 = new Scanner(System.in);

        System.out.print("Give the title of the film for searching? ");
        String searchTitle1 = scanner1.nextLine();
        filmProgram.findFilm(searchTitle1);

        System.out.print("Give the title of another film for searching? ");
        String searchTitle2 = scanner1.nextLine();
        filmProgram.findFilm(searchTitle2);

        scanner.close();
        scanner1.close();
    }
}
