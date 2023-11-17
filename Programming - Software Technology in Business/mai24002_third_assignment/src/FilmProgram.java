import java.util.ArrayList;

public class FilmProgram {
    private ArrayList<Film> list;

    public FilmProgram() {
        this.list = new ArrayList<>();
    }

    public void storeFilm(Film film) {
        list.add(film);
    }

    public ArrayList<Film> getList() {
        return list;
    }

    public ArrayList<Film> candidateFilms() {
        ArrayList<Film> candidateList = new ArrayList<>();
        for (Film film : list) {
            if (film.isCandidacy()) {
                candidateList.add(film);
            }
        }
        return candidateList;
    }

    public ArrayList<Film> monthFilms(int month) {
        ArrayList<Film> monthList = new ArrayList<>();
        for (Film film : list) {
            String[] dateParts = film.getShowDate().split("/");
            int filmMonth = Integer.parseInt(dateParts[1]);
            if (filmMonth == month) {
                monthList.add(film);
            }
        }
        return monthList;
    }

    public double filmsMeanTime() {
        if (list.isEmpty()) {
            return 0;
        }
        int totalPlayingTime = 0;
        for (Film film : list) {
            totalPlayingTime += film.getPlayingTime();
        }
        return (double) totalPlayingTime / list.size();
    }

    public void findFilm(String title) {
        boolean found = false;
        for (Film film : list) {
            if (film.getTitle().equalsIgnoreCase(title)) {
                film.print();
                found = true;
                break;
            }
        }
        if (!found) {
            System.out.println("The film " + title + " does not belong to the collection.");
        }
    }

    public void showFilms(ArrayList<Film> alist) {
        for (Film film : alist) {
            film.print();
        }
    }
}
